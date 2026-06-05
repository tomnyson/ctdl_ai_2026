
foods = [
    ("Com", 250),
    ("Trung", 150),
    ("Ga", 300),
    ("Sua", 120),
    ("canh", 100),
    ("Rau", 80)
]

target_kcal = 500
def backtrack(start, currentMeal, currentKcal):
    # b1: chọn
    if currentKcal == target_kcal:
        results.append(currentMeal.copy())
        return
    # prunning => bỏ khi khỏa đk
    if currentKcal > target_kcal or start >= len(foods):
        return
    # b2 khám phá

    name, kcal = foods[start]
    currentMeal.append((name, kcal))
    backtrack(start+1, currentMeal, currentKcal+kcal)

    # b3 -> bỏ chọn quay lui

    currentMeal.pop()

    backtrack(start+1, currentMeal, currentKcal)

    return results


results = []
backtrack(0, [], 0)

print("Các lựa chọn có tổng kcal =", target_kcal)

for i, choice in enumerate(results, 1):
    total = sum(kcal for _, kcal in choice)
    names = [name for name, _ in choice]
    print(f"Cách {i}: {names} - Tổng kcal: {total}")

