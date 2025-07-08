import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = "https://www.wanted.co.kr/wdlist/518/660?country=kr&job_sort=job.popularity_order&years=-1&tags=10564&tags=10537&tags=10401&selected=660&locations=all"

def scroll_to_bottom(driver, pause_time=1.5, max_scrolls=30):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for scroll in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def crawl_jobs_from_wanted():
    options = Options()
    # options.add_argument("--headless")  # UI 없이 실행할 경우
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)
    scroll_to_bottom(driver, pause_time=1.5, max_scrolls=30)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    jobs = []
    job_cards = soup.select("li.Card_Card__aaatv")

    for card in job_cards:
        a_tag = card.select_one("a[data-attribute-id='position__click']")
        if not a_tag:
            continue

        title = a_tag.get("data-position-name", "").strip()
        company = a_tag.get("data-company-name", "").strip()
        location = card.select_one("span.CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l")
        location_text = location.get_text(strip=True) if location else ""
        link = "https://www.wanted.co.kr" + a_tag["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location_text,
            "deadline": "",  # 마감 정보 없음
            "link": link,
        })

    print(f"전체 수집 완료: {len(jobs)}개 공고")
    return jobs

if __name__ == "__main__":
    jobs = crawl_jobs_from_wanted()