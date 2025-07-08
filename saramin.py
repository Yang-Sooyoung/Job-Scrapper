import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.saramin.co.kr/zf_user/jobs/list/domestic"
QUERY = "?page=11&loc_cd=101080,101070,101010,101200&cat_kewd=87,89,84&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2&tab=domestic#searchTitle"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def parse_job_item(job_html):
    def safe_text(selector, attr=None):
        el = job_html.select_one(selector)
        if el:
            return el.get(attr).strip() if attr else el.get_text(strip=True)
        return ""

    title = safe_text("div.job_tit a", "title")
    company = safe_text("div.col.company_nm > a.str_tit")
    location = safe_text("div.col.recruit_info p.work_place")
    deadline = safe_text("div.col.support_info span.date")

    # 공고 상세 페이지 링크 추출
    link_suffix = safe_text("div.job_tit a", "href")
    link = f"https://www.saramin.co.kr{link_suffix}" if link_suffix else ""

    return {
        "title": title,
        "company": company,
        "location": location,
        "deadline": deadline,
        "link": link
    }

def get_jobs_from_page(page, params):
    params = params.copy()
    params["page"] = page
    res = requests.get(BASE_URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    job_items = soup.select("div.list_item")
    jobs = [parse_job_item(job) for job in job_items]
    print(f"페이지 {page}: {len(jobs)}개 수집됨")
    return jobs

def crawl_jobs_from_saramin(max_page, params):
    all_jobs = []
    for page in range(1, max_page + 1):
        page_jobs = get_jobs_from_page(page, params)
        all_jobs.extend(page_jobs)
    print(f"전체 수집 완료: {len(all_jobs)}개 공고")
    return all_jobs