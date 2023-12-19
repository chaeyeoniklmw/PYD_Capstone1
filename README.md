# pyd-capstone

## 프로젝트 소개
- 프로젝트 이름: 노인사고율 줄이기- 노인횡단 데이터를 통한 보호구역 지정
- 멤버: 김은혜, 김채연, 조유라 (11조)
- 주제 선정 이유:
  ![슬라이드7](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/50f007d7-3201-4a15-8af8-3262dffc46a8)
  ![슬라이드8](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/6209b189-3fcb-4570-8e14-6e2ed7a90ee1)
  ![슬라이드9](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/e1af1082-9d98-4018-adbe-5098dff3e315)

## 기존진도
1. 기존에는 2개년 데이터로 진행 (20, 21)
2. 기존에는 동대문구의 어떤동을 선정할지 고민 할 때 기존에 분석되어있는 통계자료를 통해 선정, 시각화 자체 역시 gui 툴을 이용해서 진행
   ![슬라이드20](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/7eccefa3-586f-4097-bada-585c4dfacbfd)
   ![슬라이드21](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/3e4f8232-4888-4071-ac8f-d1bbfee9c881)
   ![슬라이드22](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/9f651937-2288-42bf-ae57-61ef78e7c2bd)
   ![슬라이드23](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/ab2260f9-d9a4-4d61-bc27-1487033ada32)
   ![슬라이드24](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/550ebdb0-2ec5-4024-ad0c-289c7c2a77a2)
   ![슬라이드25](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/98bed2f2-a1c2-4dfc-880e-4743dcdb09a2)
   ![슬라이드26](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/80326ba0-158f-417e-9c8b-b78ce6cd92dc)
## 발전과제
1. 3개년 데이터로 발전 (19, 20, 21)
2. EDA를 통해 데이터를 좀 더 파악
   1) 두변수를 선정하여 알아보기 쉽게 시각화 진행하여 사고건수 관련해 가장 많은 수치를 가지는 변수
   2) 사고건수 대비 도로형태 분석, 사고발생장소 대비 도로형태 분석
   3) 동대문구 동으로 그룹화하여 가장 많은 사고가 나는 동 분석
      ![image](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/616d6b76-c9e6-40db-a13e-29f8f7cadeea)

   4) 사고 구간 폴리곤을 이용하여 표시
      ![image](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/6c124b42-869f-4b8d-b56a-4436a71387c1)

3. 시각화 역시 gui 툴이 가지고 있는 데이터를 이용해 folium, matplotlib등의 라이브러리를 이용하여 시각화

## 코드 실행하는 방법
실행위치: Google Colab
![image](https://github.com/chaeyeoniklmw/pyd-capstone/assets/129934881/7b2a64b5-16ad-4ba0-8d6f-7a35539c28eb)
1. 위 사진에 해당하는 데이터를 data 파일에서 찾아서 업로드 한다.
2. 한글폰트 조정이라고 주석이 달린 블럭을 먼저 돌린 후, 다시 런을 해야 한글폰트가 깨지지 않고 나온다.


### __Environment__
<img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=PyCharm&logoColor=white"><img src="https://img.shields.io/badge/googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white">

### __Development__
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### __Communication__
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"><img src="https://img.shields.io/badge/kakaotalk-FFCD00?style=for-the-badge&logo=kakaotalk&logoColor=white">
