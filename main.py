from saramin import crawl_jobs_from_saramin
from jobkorea import crawl_jobs_from_jobkorea
from wanted import crawl_jobs_from_wanted
from jumpit import crawl_jobs_from_jumpit
from save import save_to_file

if __name__ == "__main__":
    site = input("크롤링할 사이트를 선택하세요 (saramin / jobkorea / wanted / jumpit): ").strip()

    if site == "saramin":
        params = {
            "cat_kewd": "87,89,84",
            "loc_cd": "101080,101070,101010,101200",
            "search_optional_item": "n",
            "search_done": "y",
            "panel_count": "y",
            "preview": "y",
            "isAjaxRequest": "0",
            "page_count": "50",
            "sort": "RL",
            "type": "domestic",
            "is_param": "1",
            "isSearchResultEmpty": "1",
            "isSectionHome": "0",
            "searchParamCount": "2",
        }
        max_page = 31
        jobs = crawl_jobs_from_saramin(max_page, params)
        save_to_file(jobs, source="saramin")
    elif site == "jobkorea":
        jobs = crawl_jobs_from_jobkorea(max_page=20)
        save_to_file(jobs, source="jobkorea")
    elif site == "wanted":
        jobs = crawl_jobs_from_wanted()
        save_to_file(jobs, source="wanted")
    elif site == "jumpit":
        jobs = crawl_jobs_from_jumpit()
        save_to_file(jobs, source="jumpit")
    else:
        print("지원하지 않는 사이트입니다.")
        exit()

    print("크롤링 및 저장 완료")