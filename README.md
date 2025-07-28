# 재미로 보는 관상 테스트

#### Rokey 심화반 GUI 프로젝트

#### PyQt5와 OpenAI API를 활용한 이미지 태그 자동화 시스템 구축

</br>

## 🧾 주제 및 선정 배경

이미지를 분석하여 관상을 통한 운세를 점처볼 수 있는 프로그램
간단하게 사진으로 이미지를 분석해서 데이터를 저장하는 시스템을 재밌게 풀어보고자 해당 주제를 선정

</br>

## 🛠️ 사용 기술

- Python3, PyQt5
- OpenAI API
- SQLite3
- dotenv

</br>

## 🔀 전체 흐름

1. 이미지 업로드
2. 이미지 분석 요청
3. 분석 결과를 JSON 형식으로 파싱
4. 파싱한 데이터를 화면에 출력
5. 데이터 DB 저장

</br>

## ⚙️ 시스템 구성도 (Architecture)

```
[ 사용자 ]
   ↓
[ PyQt5 GUI ]
   ↓
[ 이미지 + 프롬프트 ]
   ↓
[ GPT API 호출 ]
   ↓
[ 결과 출력 및 저장 ]   →   [ SQLite DB ]
```

</br>

## 🗂️ 디렉토리 구조

```
project/
├── gui/
│   └── main_app.py
├── api/
│   └── openai_api.py
├── utils/
│   └── config.py
│   └── db_handler.py
│   └── file_handler.py
├── main.py
├── .env
└── image_log.db
```

</br>

## 📚 예시 시나리오

```
1. 내 사진을 업로드
2. 분석하기 버튼을 클릭
3. OpenAI API를 통해 이미지 분석 진행
4. 분석한 결과를 필터링하여 필요한 JSON 데이터만 추출
5. JSON 데이터로 파싱하여 재물운, 연애운, 건강운, 전체 요약으로 나눠 화면에 출력
6. 검색 결과를 DB에 저장
```
