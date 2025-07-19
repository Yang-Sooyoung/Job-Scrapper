### 🧾 Job Scrapper

> 채용 플랫폼에서 개발자 채용 공고를 자동으로 수집하여 엑셀 파일로 저장하는 Python 기반 웹 크롤링 프로젝트입니다.\
> 사람인, 잡코리아, 원티드, 점핏 등을 대상으로, 기술 스택/위치/경력 등의 조건에 맞는 공고를 수집하고 정리합니다.

<br/>

### 주요 기능

* ✅ 점핏(Jumpit) 채용 공고 크롤링
* ✅ 사람인(Saramin) 공고 수집 및 Excel 저장
* ✅ 잡코리아(JobKorea) 공고 스크롤 기반 크롤링
* ✅ Selenium 기반 UI 상호작용 (필터 선택, 스크롤 등)
* ✅ openpyxl을 사용한 Excel 파일 생성 및 저장
* ✅ 기술 스택, 경력, 지역, 회사명 등 필터링 기능
* ✅ 로그인 없이 사용 가능

<br/>

### 기술 스택

| 구성 요소 | 사용 기술                                                        |
| ----- | ------------------------------------------------------------ |
| 언어    | Python 3.10+                                                 |
| 크롤링   | `requests`, `BeautifulSoup`, `Selenium`, `webdriver-manager` |
| 자동화   | `time`, `re`, `os`, `datetime`                               |
| 엑셀 저장 | `openpyxl`                                                   |
| 실행 환경 | Windows / WSL / Mac 모두 가능 (ChromeDriver 필요)                  |

<br/>

### 디렉토리 구조

```
Job-Scrapper/
├── jumpit.py         # 점핏 크롤러
├── saramin.py        # 사람인 크롤러
├── jobkorea.py       # 잡코리아 크롤러
├── wanted.py         # 원티드 크롤러
├── save.py           # 공통 Excel 저장 로직
└── main.py           # 크롤러 실행 진입
```

<br/>

### 실행 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 크롤러 실행

```bash
# 예시: 점핏 크롤링 실행
python main.py
```

> 각 사이트별로 크롤러 파일을 직접 실행할 수도 있습니다.
> 예: `python jumpit.py`

<br/>

### 결과 예시

* 수집된 채용 정보는 `/output` 폴더 내 `.xlsx` 엑셀 파일로 저장됩니다.
* 파일명 예: `jumpit_jobs_2025-07-19.xlsx`

| 회사명     | 포지션     | 지역 | 경력    | 기술스택                |
| ------- | ------- | -- | ----- | ------------------- |
| (예시) 토스 | 백엔드 개발자 | 서울 | 3년 이상 | Java, Spring, MySQL |

<br/>

### 구현 포인트

* 점핏: 필터 조건 적용된 URL에서 직접 요청 후 파싱
* 사람인: `requests` + `BeautifulSoup` 조합으로 빠르게 크롤링
* 잡코리아: 필터 버튼 클릭, 무한 스크롤, 팝업 닫기 등 Selenium UI 자동화 구현
* 모든 크롤러는 로그인 없이 사용 가능

<br/>

### 만든 이유

* 개발자 이직/구직 시, 여러 사이트에 흩어진 공고를 한 번에 수집하기 위한 **실용적인 자동화 도구**를 만들고자 시작하였습니다.
* Python과 웹 크롤링 기술을 실제 업무/이직 준비에 적용하는 데 중점을 두었습니다.

</br>

#### 🙋‍♀️ 만든 사람

- 👩‍💻 이름: 양수영 (Yang Sooyoung)
- 🔗 GitHub: [@Yang-Sooyoung](https://github.com/Yang-Sooyoung)

<br/>

