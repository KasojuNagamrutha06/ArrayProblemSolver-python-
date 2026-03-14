class ArrayProblemSolver:

    # Sorting using Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    # Binary Search (array must be sorted)
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # Find pairs with given sum
    def pair_sum(self, arr, target):
        seen = set()
        pairs = []
        for num in arr:
            if target - num in seen:
                pairs.append((num, target - num))
            seen.add(num)
        return pairs


# Main Program
if __name__ == "__main__":
    solver = ArrayProblemSolver()

    arr = list(map(int, input("Enter array elements: ").split()))
    
    # Sorting
    sorted_arr = solver.quick_sort(arr)
    print("Sorted Array:", sorted_arr)

    # Searching
    key = int(input("Enter element to search: "))
    index = solver.binary_search(sorted_arr, key)
    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")

    # Pair Sum
    target = int(input("Enter target sum: "))
    print("Pairs with given sum:", solver.pair_sum(arr, target))
