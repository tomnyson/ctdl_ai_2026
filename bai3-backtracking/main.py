def subsets_sum(nums, target):
    result= []
    def backtrack(start,path, current_sum):
    # TODO 1: Lưu path hiện tại vào result
        if current_sum == target:
            result.append(path.copy())
    # TODO 2: Duyệt các phần tử từ start đến cuối nums
        for i in range(start,len(nums)):
        # CHOOSE
            path.append(nums[i])
        # EXPLORE
            backtrack(i+1,path,current_sum + nums[i])

        # UNCHOOSE
            path.pop()

    backtrack(0, [], 0)
    return result


def subsets_sum_pruning(nums, target):
    result= []
    nums.sort()  # Sắp xếp để dễ dàng cắt tỉa
    def backtrack(start,path, current_sum):
    # TODO 1: Lưu path hiện tại vào result
        if current_sum == target:
            result.append(path.copy())
            return  # Dừng lại nếu đã tìm thấy một tập con hợp lệ
    # TODO 2: Duyệt các phần tử từ start đến cuối nums
        for i in range(start,len(nums)):
        # CHOOSE
            if current_sum + nums[i] > target:
                break  # Cắt tỉa nếu tổng vượt quá target
            path.append(nums[i])
        # EXPLORE
            backtrack(i+1,path,current_sum + nums[i])

        # UNCHOOSE
            path.pop()

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
      # Test
    nums = [2, 3, 6, 7, 1, 4]
    target = 7
    print("Các tập con có tổng bằng", target, ":")
    print(subsets_sum_pruning(nums, target))