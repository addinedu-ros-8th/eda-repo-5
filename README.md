# 🐶 반려동물과 함께하는 세상
![웰시 멍멍이](https://github.com/user-attachments/assets/f4a11148-2211-40ca-b964-f792453e16c6)

## ☀️ 개요 
---
현재 대한민국은 수도권으로 인구가 집중되는 쏠림 현상을 보이고 있고, 2014년부터 시행한 반려동물 등록제와 각 가정에서 반려동물에 대한 인식이 바뀌어 가족구성원으로 받아들이고 있어 반려동물을 양육하는 가정이 증가하고 있습니다. 이러한 흐름속에서 많은 인구가 거주하는 서울시는 과연 반려동물을 키우기 적합한 도시인지에 대한 의문이 생겼습니다.   

<img src="https://github.com/user-attachments/assets/bec0f21a-cd8d-43d3-bdbc-ebc6535b86a5" width="500" height="350" />
<img src="https://github.com/user-attachments/assets/8b5ad36e-54cb-4637-8bb4-183d5b45bc08" width="500" height="350" />
<p align="center"><img src="https://github.com/user-attachments/assets/7d4eb033-0f6a-4c30-8233-f005f5bbbaae" width="500" height="550" /></p>

저희는 이번 프로젝트를 통해 서울시에서 반려동물을 키우는 각 가정들의 양육 형태와 주변 환경을 조사하여 서울시가 반려동물을 키우기 적합한 도시인지 분석해볼 것입니다.

## 멤버 구성
---
|구성원|역할|
|------|---|
|신동철(팀장)|네이버 리뷰 크롤링, 데이터 설계 및 구축, 데이터 분석 및 시각화|
|송원준(팀원)|구글맵 리뷰 크롤링, 감성모델링, 데이터 분석 및 시각화|
|이우재(팀원)|카카오맵 리뷰 크롤링, 반려동물 등록 및 유기 데이터 수집, 데이터 분석 및 시각화|
---
## 💻 사용 스택
---
|분류|사용기술|
|------|---|
|언어|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|
|운영체제|<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> <img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">|
|통합개발환경|<img src="https://img.shields.io/badge/vscode-147EFB?style=for-the-badge&logo=xcode&logoColor=white"> <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">|
|데이터베이스|<img src="https://img.shields.io/badge/AWS RDS-527FFF?style=for-the-badge&logo=amazonwebservices&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">|
|라이브러리|<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"> <br><img src="https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/googlemaps-4285F4?style=for-the-badge&logo=googlemaps&logoColor=white">|
|협업툴|<img src="https://img.shields.io/badge/Confluence-172B4D?style=for-the-badge&logo=confluence&logoColor=white"> <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white"> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">|
---
## 🔗 데이터 수집 경로
---
[공공데이터포털](https://www.data.go.kr)   
[서울열린데이터광장](https://data.seoul.go.kr/)   
[카카오맵](https://map.kakao.com/)   
[구글맵](https://www.google.co.kr/maps)   
[네이버지도](https://map.naver.com/)   
[국가동물보호정보시스템](https://www.animal.go.kr/)  
[농림축산식품부](https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do?data_id=20210806000000001532)
---
## 🐯 ER 다이어그램
---
![image](https://github.com/user-attachments/assets/b5cf3823-0cfc-4143-9b91-fba84542ac3b)

## 서울시 반려동물 현황
---
### 🎯 주제: 서울시에서 반려동물을 키우기 좋은 자치구는?

### 1. 반려동물 등록 현황
  - 자치구별 등록 현황
    <img width="1324" alt="image" src="https://github.com/user-attachments/assets/e4b8439b-ff9b-4c99-a51c-01d385aaba1f" />
    
### 2. 형태별 반려동물 양육 비율
  - 가구원수별 반려동물 양육 비율
    
    ![image](https://github.com/user-attachments/assets/fc8b04e0-3281-45f9-a5f7-fe5ac2bc8c38)
    
  - 거주형태별 반려동물 양육 비율
    
    ![image](https://github.com/user-attachments/assets/f2686b8b-08fb-4ff6-984a-737cfe55bb87)
    
  - 점유형태별 반려동물 양육 비율
    
    ![image](https://github.com/user-attachments/assets/04fecc0f-89b8-4444-b5ea-83e71e2a018d)
    
### 3. 자치구별 입양 형태(상위 5개 자치구)
  - 판매업소
    
    <img width="1325" alt="image" src="https://github.com/user-attachments/assets/1eb89f67-c89d-4809-be00-e8c98fc0acb7" />
    
  - 지인입양
    
    <img width="1328" alt="image" src="https://github.com/user-attachments/assets/9e831c37-f4ed-4581-84ba-b9dfab7ad402" />
    
  - 유기동물입양
    
    <img width="1326" alt="image" src="https://github.com/user-attachments/assets/fe853737-e19b-42fe-ad6f-907b923825d3" />
    
  - 인터넷 구매 비율
    
    <img width="1329" alt="image" src="https://github.com/user-attachments/assets/542cc647-661b-44fd-9d84-14f04a0683c1" />
    
### 4. 자치구별 인프라 현황
  - 동물병원 밀집도
    
    <img width="1324" alt="image" src="https://github.com/user-attachments/assets/c1c684f0-b564-43f9-bb42-2577ff8e3ad8" />
    
  - 공원 밀집도
    
    <img width="1342" alt="image" src="https://github.com/user-attachments/assets/6de80dae-3fe6-433f-afa5-504341c0fa8c" />
    
  - 위탁관리업 밀집도
    
    <img width="1330" alt="image" src="https://github.com/user-attachments/assets/a527690d-0fc9-4307-b0af-2459129263b4" />
    
  - 미용업 밀집도
    
    <img width="1328" alt="image" src="https://github.com/user-attachments/assets/2f5d86db-b741-492f-bcef-8a58a1aa3396" />

## 💥 가설
---
### 1. 과연 반려동물 등록 수가 많을 수록 유기율이 높을까?

  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/30ce2a54-435f-427d-a5a4-ad8a71ff1c36" />
  
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/7489c03f-e1db-4360-841e-894e8b21a00d" />
  
  <img width="1333" alt="image" src="https://github.com/user-attachments/assets/b5bf091b-7781-413a-a1bd-545a78b21424" />
 
### 2. 급여수준이 높은 지역구는 반려동물을 많이 키우는가?

  <img width="1326" alt="image" src="https://github.com/user-attachments/assets/c0067165-1152-4c1a-b0ca-53255361d9d7" />
  
  <img width="1330" alt="image" src="https://github.com/user-attachments/assets/4a9b2678-2bfc-4ea7-a5e3-0f9c50f8d9a7" />
  
  <img width="1331" alt="image" src="https://github.com/user-attachments/assets/bce3b1b6-8eff-4f84-971d-ddaf02f7da2c" />
  
  <img width="1329" alt="image" src="https://github.com/user-attachments/assets/6e99d58d-cc10-4d5d-b40e-1a3aff6010c1" />  
  
  <img width="1330" alt="image" src="https://github.com/user-attachments/assets/ab5bb1ab-2bef-45a8-b463-6628c6979027" />
  

### 3. 서울시에서 특정 품종은 유기동물로 등록될 가능성이 있는가?
  <img width="1328" alt="image" src="https://github.com/user-attachments/assets/4bd74cc0-487d-456b-95ed-86b09ed17dd5"/>
  
  <img width="1324" alt="image" src="https://github.com/user-attachments/assets/ef6d4b69-f27e-4e8a-a154-2641fbca6e99" />
  
  <img width="1318" alt="image" src="https://github.com/user-attachments/assets/97f16d33-9088-47da-95ee-518d4df0c0c2" />
  
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/35d3538f-df0a-45db-8929-5f543c559359" />
  
  <img width="1335" alt="image" src="https://github.com/user-attachments/assets/09b8c741-e2e6-4e2f-ae35-944086e8b2fe" />
  
  <img width="1328" alt="image" src="https://github.com/user-attachments/assets/6424cea0-f5e6-4e59-b236-5368214c49d0"/>
  
  <img width="1325" alt="image" src="https://github.com/user-attachments/assets/556faee2-206b-4357-a6f6-122157c6c993" />
  
  <img width="1328" alt="image" src="https://github.com/user-attachments/assets/baed3d1b-00b5-4fca-9b11-9d5dff379c0b" />
  
  <img width="1328" alt="image" src="https://github.com/user-attachments/assets/2b32b402-1030-498e-91bd-13c18a6b7109" />
  
  <img width="1331" alt="image" src="https://github.com/user-attachments/assets/8c9ef7a8-3216-48fc-9361-914b05d83be3" />

4### 4. 서울시 각 구별 공원수가 많을수록 대형견을 키울 가능성이 있는가?
  <img width="1323" alt="image" src="https://github.com/user-attachments/assets/3dbf662f-f9dc-4db9-be42-e8356be3a39d" />
  
  <img width="1329" alt="image" src="https://github.com/user-attachments/assets/2e9a4b88-1925-4d2b-a5c9-4676e1a7b755" />
  
  <img width="1333" alt="image" src="https://github.com/user-attachments/assets/d03ce6b6-403b-45c9-b1a7-d1bcf7e9d005" />
  
  <img width="1323" alt="image" src="https://github.com/user-attachments/assets/a173a60b-4c1e-4872-abfd-309fe53612f4" />
  
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/7a78b700-bd1b-4cdd-ab90-ec429e7b26e4" />
  
  <img width="1327" alt="image" src="https://github.com/user-attachments/assets/8ae62549-2d58-479e-a53f-72cc0cda2460" />
  
  <img width="1327" alt="image" src="https://github.com/user-attachments/assets/290336f5-c08e-445d-85dd-e677f904fc5c" />
  
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/ec1b33ad-ed6c-4349-bd57-779b7c79e5ee" />
  
  <img width="1334" alt="image" src="https://github.com/user-attachments/assets/ed8f4b26-034b-491c-8993-c2ddfeae3ea1" />

### 5. 만족도가 높은 인프라시설이 많은 지역은 반려동물을 많이 키울것이다.
  <img width="1332" alt="image" src="https://github.com/user-attachments/assets/9e95cd92-197a-4e1b-99d5-b523715ba39b" />
  
  <img width="1324" alt="image" src="https://github.com/user-attachments/assets/1095d338-734c-41eb-9115-2034f314974d" />
  
  <img width="1329" alt="image" src="https://github.com/user-attachments/assets/23112b23-f05a-4708-af68-12a94fc8e910" />

### 6. 지역에 공원이 많을수록 반려동물 등록건수가 많은가?
  <img width="1329" alt="image" src="https://github.com/user-attachments/assets/d149a418-6ee6-48ed-b202-914b1af142d9" />
  
  <img width="1315" alt="image" src="https://github.com/user-attachments/assets/ec0737b7-cccf-4cbc-837b-a1ebad168675" />
  
  <img width="1336" alt="image" src="https://github.com/user-attachments/assets/469bf194-7446-4260-a4aa-b7b59e5dd493"/>

### 7. 서울시 반려동물 등록건수와 인프라 시설수와의 관계 분석
  <img width="1330" alt="image" src="https://github.com/user-attachments/assets/7b00deda-5bfb-4bad-a4e6-8ed8c65bf681" />
  
  <img width="1337" alt="image" src="https://github.com/user-attachments/assets/1213b129-3f25-4d22-b5ca-8dbe2891dab6" />

### 8. 과연 3대 지랄견으로 불리는 코카 스패니얼, 비글, 슈나우저는 유기율이 높을까?
  <img width="1333" alt="image" src="https://github.com/user-attachments/assets/f3753d71-2c74-49ca-a563-e1d6e475dcf5" />
  
  <img width="1328" alt="image" src="https://github.com/user-attachments/assets/c6f45b1e-fcb8-4de7-a4a4-523ba448dd5a" />

## 🌈 결론
### 서울시에서 반려동물을 키우기 좋은 자치구는 강남 3구입니다. 
