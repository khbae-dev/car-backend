import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# FAISS 인덱스 및 메타데이터 로드
index = faiss.read_index('car_faiss_index.idx')
with open('car_metadata.pkl', 'rb') as f:
    car_metadata = pickle.load(f)

# 모델 로드
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 검색 함수
def search_similar_cars(query, k=5):
    query_embedding = model.encode(query)
    D, I = index.search(np.array([query_embedding]), k)
    results = [car_metadata[i] for i in I[0]]
    return results

# 검색 테스트
if __name__ == "__main__":
    query = "2022년식 SUV 경유 차량"
    similar_cars = search_similar_cars(query)
    print(query)

    print("\n✅ 검색 결과:")
    for car in similar_cars:
        print(car)