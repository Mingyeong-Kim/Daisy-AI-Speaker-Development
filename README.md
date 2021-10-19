# Daisy AI Speaker Development

- **프로젝트 기간: 2020.05 - 2020.06(8주, 팀)**
- **프로젝트 개요: 시카고 공공자전거(Divvy) 이용 데이터를 기반으로한 영어 질의응답 AI 스피커 개발**
- **사용기술: python(visual studio code), sqlite3(DB), Google API Client Library, PyAudio 0.2.11(Microphone), PyPI Library**
- **역할: 팀장, SW 프로그래머(programmer), 데이터베이스 구축 및 연결, 음성인식, TTS,STT 로직 코드 구현**


## 프로젝트 목표
- 영어 또는 한국어 음성으로 특정 데이터에 대한 질의응답이 가능한 무료 오픈소스 기기(AI Speaker)를 개발하는 것을 목표로 했습니다.
- The goal of this project will be to create a free and opensource device that can perform ad_hoc data qaureies(SQL) via voice in English or Korean. 


## 프로젝트 과정 및 내용
- **프로젝트 개요(Project Outline)**
<img width="500"  height="300" src="https://user-images.githubusercontent.com/65681568/137986387-da792c15-503e-409f-a9c1-66da58155ea6.PNG">

- **프로그램 로직(Program logic)**
<img width="600"  height="350" src="https://user-images.githubusercontent.com/65681568/137985791-d138313c-136c-44ab-93bd-e58c9be79766.PNG">


1. 필요 라이브러리 및 API 설정
   1-1.필요한 프로그램 설치(Prepare Requirements tools)
   
    * (1)	python 3.7(visual studio code)

    * (2)	PyAudio 0.2.11(Microphone) 
        – pip install pyaudio
    
    * (3)	PocketSphinx 
        – recognizer_instance.recognize_sphinx
    
    * (4)	Google API Client Library for Python 
        - recognizer_instance.recognize_google_cloud
        - pip install google-api-python-client
    
    * (5) FLAC encoder(voice file)
        - sudo apt-get install flac

    1-2. install SpeechRecognition
        - pip install SpeechRecognition

    1-3. download python library (from PyPI)

    1-4. python setup.py install
    
2. 데이터 베이스 생성 및 데이터 저장
   - 데이터(Data): 시카고 공공자전거 이용 데이터(Divvy data 2015_Q2)
 
3. 마이크 음성인식 설정 및 테스트
   - 음성인식 코드 구현
   - Microphone 변수(parameter) 조절  
   - 음성인식이 가장 잘되는 요건 및 변수설정 찾기

4. STT,TTS 로직 코드 구현
   - 인식된 문장(질문)을 바탕으로 얻고자하는 정보(대답) 추출을 위한 SQL쿼리로 변경해주는 코드 구현(Speech to Text)
   - 사용자가 얻고자 하는 답변을 영어 문장으로 구현하여 음성으로 전달하는 코드 구현(Text To Speech)
   - 예시 문장과 답변을 설정하여 코드를 구현함

5. 프로그램 테스트

## 프로젝트 결과
- 6개 질문에 대한 Q&A speaker 프로그램 로직 코드 완성

**추후 보완점**
- 외부의 소음이나 다양한 사람의 발음을 인식하지 못하는 경우가 있음
- 다양한 질문에 대한 STT,TTS 로직 코드 구현 필요


