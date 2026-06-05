import time
from collections import defaultdict

def has_duplicate_v1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


def has_duplicate_v2(arr):
    n = len(arr)
    seen = set()
    for i in range(n):
        if arr[i] in seen:
            return True
        seen.add(arr[i])
    return False

if __name__ == "__main__":
#     arr = list(range(100000))
#     arr.append(10000)
    
# #  cach 1 on2
# start = time.time()
# result_v1 = has_duplicate_v1(arr)
# time1 = time.time() - start
# print(f"Method 1: Has duplicate? {result_v1}, Time taken: {time1:.4f} seconds")
# # cach 2 on  # Add a duplicate
# start = time.time()
# result_v2 = has_duplicate_v2(arr)
# time2 = time.time() - start
# print(f"Method 2: Has duplicate? {result_v2}, Time taken: {time2:.4f} seconds")
# print(f"{time1/time2:.2f} times faster than method 1")

    feq = defaultdict(int)
    print(feq)
    arr = list(range(10))
    arr.append(5)
    for item in arr:
        feq[item] += 1
    print(list(feq.items()))   