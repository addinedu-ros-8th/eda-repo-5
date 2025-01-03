# 🐶 반려동물과 함께하는 세상
![웰시 멍멍이](https://github.com/user-attachments/assets/f4a11148-2211-40ca-b964-f792453e16c6)

## ☀️ 개요 
현재 대한민국은 수도권으로 인구가 집중되는 쏠림 현상을 보이고 있고, 2014년부터 시행한 반려동물 등록제와 각 가정에서 반려동물에 대한 인식이 바뀌어 가족구성원으로 받아들이고 있어 반려동물을 양육하는 가정이 증가하고 있습니다. 이러한 흐름속에서 많은 인구가 거주하는 서울시는 과연 반려동물을 키우기 적합한 도시인지에 대한 의문이 생겼습니다.   

<img src="https://github.com/user-attachments/assets/bec0f21a-cd8d-43d3-bdbc-ebc6535b86a5" width="500" height="350" />
<img src="https://github.com/user-attachments/assets/8b5ad36e-54cb-4637-8bb4-183d5b45bc08" width="500" height="350" />
<p align="center"><img src="https://github.com/user-attachments/assets/7d4eb033-0f6a-4c30-8233-f005f5bbbaae" width="500" height="550" /></p>

저희는 이번 프로젝트를 통해 서울시에서 반려동물을 키우는 각 가정들의 양육 형태와 주변 환경을 조사하여 서울시가 반려동물을 키우기 적합한 도시인지 분석해볼 것입니다.

## 서울시 반려동물 현황
1. 반려동물 등록 현황
  - 자치구별 등록 현황
2. 형태별 반려동물 양육 비율
  - 가구원수별 반려동물 양육 비율
  - 소득구간별 반려동물 양육 비율
  - 거주형태별 반려동물 양육 비율
  - 점유형태별 반려동물 양육 비율
3. 자치구별 입양 형태(상위 5개 자치구)
  - 판매업소, 지인입양, 유기동물입양, 인터넷 구매 비율
4. 자치구별 인프라 현황
  - 동물병원 밀집도
  - 공원 밀집도
  - 위탁관리업 밀집도
  - 미용업 밀집도


## 💥 가설
1. 과연 반려동물 등록 수가 많을 수록 유기율이 높을까?
2. 급여수준이 높은 지역구는 반려동물을 많이 키우는가?
3. 서울시에서 특정 품종은 유기동물로 등록될 가능성이 있는가?
4. 서울시 각 구별 공원수가 많을수록 대형견을 키울 가능성이 있는가?
5. 만족도가 높은 인프라시설이 많은 지역은 반려동물을 많이 키울것이다.
6. 지역에 공원이 많을수록 반려동물 등록건수가 많은가?
7. 서울시 반려동물 등록건수와 인프라 시설수와의 관계 분석
8. 과연 3대 지랄견으로 불리는 코카 스패니얼, 비글, 슈나우저는 유기율이 높을까?

## 멤버 구성
|구성원|역할|
|------|---|
|신동철(팀장)|네이버 리뷰 크롤링, 데이터 설계 및 구축, 데이터 분석 및 시각화|
|송원준(팀원)|구글맵 리뷰 크롤링, 감성모델링, 데이터 분석 및 시각화|
|이우재(팀원)|카카오맵 리뷰 크롤링, 반려동물 등록 및 유기 데이터 수집, 데이터 분석 및 시각화|

## 💻 사용 스택
|분류|사용기술|
|------|---|
|언어|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|
|운영체제|<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">|
|통합개발환경|<img src="https://img.shields.io/badge/vscode-147EFB?style=for-the-badge&logo=xcode&logoColor=white"> <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">|
|데이터베이스|<img src="https://img.shields.io/badge/AWS RDS-527FFF?style=for-the-badge&logo=amazonwebservices&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">|
|라이브러리|<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <br><img src="https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/googlemaps-4285F4?style=for-the-badge&logo=googlemaps&logoColor=white">|
|협업툴|<img src="https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white"> <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white"> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">|
## 🔗 데이터 수집 경로
[공공데이터포털](https://www.data.go.kr)   
[서울열린데이터광장](https://data.seoul.go.kr/)   
[카카오맵](https://map.kakao.com/)   
[구글맵](https://www.google.co.kr/maps)   
[네이버지도](https://map.naver.com/)   
[국가동물보호정보시스템](https://www.animal.go.kr/)  
[농림축산식품부](https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?data_id=20210806000000001532)
