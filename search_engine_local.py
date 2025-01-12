import pickle

# 중고차 메타데이터 로드
with open('car_metadata.pkl', 'rb') as f:
    car_metadata = pickle.load(f)

# 검색 함수
def search_similar_cars(query):
    # 쿼리에서 숫자 추출
    try:
        budget_limit = int(''.join(filter(str.isdigit, query)))
    except ValueError:
        print("❌ 잘못된 입력입니다. 숫자를 입력해주세요.")
        return []

    # 예산 이하 차량 필터링
    filtered_cars = [car for car in car_metadata if car['price'] <= (budget_limit/3)]

    if not filtered_cars:
        print("❌ 예산에 맞는 차량이 없습니다.")
        return []

    return filtered_cars

# 테스트
if __name__ == "__main__":
    query = input("연봉을 입력하세요 (만원 단위): ")
    cars = search_similar_cars(query)
    for car in cars:
        print(f"{car['title']} | {car['price']}{car['unit']} | {car['km']}km | {car['year']} | {car['fuel']}")