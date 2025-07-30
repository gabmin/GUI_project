# 🍚 오늘은 뭐 먹지? 🍛

#### Rokey 심화반 GUI 프로젝트

#### PyQt5와 OpenAI API를 활용한 이미지 태그 자동화 시스템 구축

</br>

## 🧾 주제 및 선정 배경

음식 재료 이미지를 분석해서 해당 재료로 무슨 요리를 해먹을 수 있을지 레시피를 알려주는 시스템.
오늘은 뭐 먹을지 고민될 때, 냉장고의 있는 재료로 만들 수 있는 메뉴를 추천해준다.

<br/>

## 🎥 시연 영상

![시연영상](https://blog.kakaocdn.net/dna/vAPq4/btsPDbR85ou/AAAAAAAAAAAAAAAAAAAAACRICrJ7x1VKEuYBMbMS7KkN6UupKAOuPkKP5iAfWOJI/img.gif?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1753973999&allow_ip=&allow_referer=&signature=y8zA4Y3sXWZXI5SM6Sb8N1X6wvs%3D)

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
└── recipe_log.db
```

</br>

## 📚 예시 시나리오

```
1. 이미지 업로드 버튼을 클릭
2. 음식 재료 이미지 등록
3. 분석하기 버튼을 클릭
4. OpenAI API를 통해 이미지 분석 진행
5. 분석한 결과를 JSON 데이터로 파싱
5. 파싱한 데이터를 화면에 출력
6. 검색 결과를 DB에 저장
```

<br/>

## 📜 회고

처음에는 사진을 업로드해서 관상을 통해 운세를 점처보는 프로그램을 기획하고 기능 구현까지 진행하였지만, GPT내부의 정책(외모 기반으로 성격·운명을 판단하는 AI 서비스는 윤리적인 문제 때문에 직접적으로 지원하지 않음)으로 인해 불가피하게 주제를 변경하게 되었습니다. 이를 통해 기획과 사전 조사에 대한 중요성을 다시 깨달을 수 있었던 좋은 경험이었습니다.
