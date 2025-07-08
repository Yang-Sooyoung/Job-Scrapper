import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def scroll_to_bottom(driver, pause_time=1.5, max_scrolls=30):
    last_height = driver.execute_script("return document.body.scrollHeight")
    scrolls = 0

    while scrolls < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
        scrolls += 1


def crawl_jobs_from_jumpit():
    options = Options()
    # options.add_argument("--headless")  # 이 줄을 활성화하면 헤드리스 모드로 실행됨
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        url = "https://www.jumpit.co.kr/positions?tags=Java,Spring%20Boot,AWS,MySQL&sort=popular"
        driver.get(url)
        scroll_to_bottom(driver, pause_time=1.5, max_scrolls=30)

        # 공고 a 태그가 로드될 때까지 대기
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title]"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

    except Exception as e:
        print("공고 로딩 실패:", e)
        with open("jumpit_page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        return []

    finally:
        driver.quit()

    jobs = []
    job_cards = soup.select("div.sc-d609d44f-0.grDLmW")

    for card in job_cards:
        link_tag = card.find("a", href=True)
        if not link_tag:
            continue

        link = "https://www.jumpit.co.kr" + link_tag["href"]
        title = link_tag.get("title", "").strip()

        company_tag = card.select_one("div.sc-15ba67b8-2.ixzmqw > span")
        company = company_tag.get_text(strip=True) if company_tag else ""

        location_tag = card.select_one("ul.sc-15ba67b8-1.cdeuol > li")
        location = location_tag.get_text(strip=True) if location_tag else ""

        deadline_tag = card.select_one("div.sc-d609d44f-3.hwTKyC > span")
        deadline = deadline_tag.get_text(strip=True) if deadline_tag else "상시"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "deadline": deadline,
            "link": link,
        })
    print(f"전체 수집 완료: {len(jobs)}개 공고")
    return jobs

if __name__ == "__main__":
    jobs = crawl_jobs_from_jumpit()
    