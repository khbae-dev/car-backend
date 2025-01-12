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

# 데이터 전처리 및 인덱스 생성 함수
def create_faiss_index():
    # 최신 JSON 파일 로드
    latest_json = find_latest_json()
    with open(latest_json, 'r', encoding='utf-8') as f:
        car_data = json.load(f)

    # 모델 로드
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # 차량 데이터를 임베딩
    car_titles = [car['title'] for car in car_data]
    embeddings = model.encode(car_titles)

    # FAISS 인덱스 생성
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    # 인덱스 저장
    faiss.write_index(index, 'car_faiss_index.idx')
    print("✅ FAISS 인덱스가 생성되었습니다.")

    # 메타데이터 저장
    with open('car_metadata.pkl', 'wb') as f:
        pickle.dump(car_data, f)
    print("✅ 메타데이터가 저장되었습니다.")

if __name__ == "__main__":
    create_faiss_index()