import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.jobkorea.co.kr/Recruit/Home/_GI_List/"

def crawl_jobs_from_jobkorea(max_page=20):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1'
    })

    jobs = []

    for page in range(1, max_page + 1):
        data = {
            'isDefault': 'true',
            'condition[local]': 'I010,I080,I070',
            'condition[career]': '1,2',
            'condition[ikwrd]': '10000382793,10000381662',
            'page': page,
            'direct': '0',
            'order': '20',
            'pagesize': '40',
            'tabindex': '0',
            'onePick': '0',
            'confirm': '0',
            'profile': '0',
        }

        resp = session.post(BASE_URL, data=data)
        if resp.status_code != 200:
            print(f"페이지 {page} 요청 실패: {resp.status_code}")
            break

        soup = BeautifulSoup(resp.text, 'html.parser')
        cards = soup.select("tr.devloopArea")
        print(f"페이지 {page}: {len(cards)}개 수집됨")

        if not cards:
            break

        for card in cards:
            t = card.select_one("td.tplTit strong a")
            if not t:
                continue
            title = t.text.strip()
            link = "https://www.jobkorea.co.kr" + t['href']
            company = card.select_one("td.tplCo a").text.strip()
            loc = card.select_one("p.etc span.cell").text.strip()
            dl = card.select_one("td.odd span.date").text.strip()
            jobs.append({
                "title": title, "company": company, "location": loc,
                "deadline": dl, "link": link
            })

    print(f"전체 수집 완료: {len(jobs)}개 공고")
    return jobs