# 📑 기능 요약

---

## 📂 **data_preprocessing.py** 기능 요약

이 파일은 데이터 전처리 및 **FAISS** 인덱스 생성을 담당합니다.

### 주요 기능
1. **최신 JSON 파일 탐색**
   - 함수: `find_latest_json(directory='../car-scraper')`
   - 설명: 지정된 디렉터리에서 가장 최근에 생성된 JSON 파일을 찾아 반환합니다.

2. **FAISS 인덱스 생성 및 저장**
   - 설명: 사용자가 업로드한 JSON 데이터를 처리하여 FAISS 인덱스를 생성하고 저장합니다.
   - 사용 라이브러리: `faiss`, `numpy`, `pickle`

3. **SentenceTransformer 모델 로드**
   - 설명: 텍스트 데이터를 임베딩하기 위해 `sentence-transformers` 라이브러리의 모델을 사용합니다.

---

## 🔍 **search_engine.py** 기능 요약

이 파일은 사용자의 질의에 대해 **유사 차량 검색**을 수행합니다.

### 주요 기능
1. **FAISS 인덱스 및 메타데이터 로드**
   - 설명: 기존에 생성된 FAISS 인덱스와 메타데이터 파일을 로드합니다.

2. **SentenceTransformer 모델 로드**
   - 설명: `SentenceTransformer` 모델을 사용하여 사용자의 질의를 벡터화합니다.

3. **유사 차량 검색 함수**
   - 함수: `search_similar_cars(query, k=5)`
   - 설명: 사용자의 질의에 대한 유사한 차량을 검색하여 상위 `k`개 결과를 반환합니다.
   - 사용 라이브러리: `faiss`, `numpy`

---

## 🧩 **종합적인 워크플로우**
1. **data_preprocessing.py** 파일을 사용하여 데이터를 전처리하고 인덱스를 생성합니다.
2. **search_engine.py** 파일을 사용하여 사용자의 입력에 기반한 유사 차량을 검색합니다.
