def find_insertion_index(result, target_number) :
    for i in range(len(result)) :
        # 결과 배열 원소가 주어진 원소보다 커지는 위치를 반환
        if result[i] > target_number :
            return i
    # 결과 배열이 비었거나 끝까지 돌았으나 주어진 원소가 여전히 크다면 제일 마지막에 위치
    return len(result)

def insertion_sort(array) :
    result = []
    while array :
        # 주어진 배열에서 첫번째 원소를 뺌
        target_number = array.pop(0)
        # 결과 배열에서 삽입할 위치를 구함
        insertion_index = find_insertion_index(result, target_number)
        # 결과 배열에서 해당 인덱스에 해당 원소 삽입
        result.insert(insertion_index, target_number)
    return result

array = [3,8,1,4]
print(insertion_sort(array))
