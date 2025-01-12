import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import glob
import os

# 📂 최신 JSON 파일 탐색 함수
def find_latest_json(directory='/shared-data'):
    json_files = glob.glob(os.path.join(directory, '*.json'))
    if not json_files:
        raise FileNotFoundError("❌ JSON 파일을 찾을 수 없습니다.")
    latest_file = max(json_files, key=os.path.getctime)
    print(f"✅ 최신 JSON 파일: {latest_file}")
    return latest_file

# 데이터 전처리 및 FAISS 인덱스 생성
def create_faiss_index(model_name='sentence-transformers/all-MiniLM-L6-v2'):
    # 최신 JSON 파일 로드
    data_path = find_latest_json()

    with open(data_path, 'r', encoding='utf-8') as f:
        cars_data = json.load(f)

    # 모델 로드
    try:
        model = SentenceTransformer(model_name)
        print("✅ 모델 로드 완료!")
    except Exception as e:
        print(f"❌ 모델 로드 실패: {e}")

    # Embedding 생성
    car_embeddings = []
    car_metadata = []

    for category, cars in cars_data.items():
        for car in cars:
            description = f"{car['title']} {car['year']} {car['fuel']} {car['km']} {car['price']} {car['sellerName']} {car['location']}"
            embedding = model.encode(description)
            car_embeddings.append(embedding)
            car_metadata.append(car)

    # FAISS 인덱스 생성
    d = len(car_embeddings[0])
    index = faiss.IndexFlatL2(d)
    index.add(np.array(car_embeddings))

    # 파일 저장
    with open('car_embeddings.pkl', 'wb') as f:
        pickle.dump(car_embeddings, f)
    with open('car_metadata.pkl', 'wb') as f:
        pickle.dump(car_metadata, f)
    faiss.write_index(index, 'car_faiss_index.idx')

    print(f"✅ FAISS 인덱스 생성 완료: {index.ntotal} 개의 차량 벡터가 추가되었습니다.")

if __name__ == "__main__":
    create_faiss_index()