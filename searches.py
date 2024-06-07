def simple_search(list, target):
    steps = 0
    for index, element in enumerate(list):
        steps += 1
        if element == target:
            # Return the index and steps taken if found
            return index, steps
    # Return -1 and steps taken if the target is not found in the list
    return -1, steps

def binary_search(list, target):
    steps = 0
    low, high = 0, len(list) - 1

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if list[mid] == target:
            # Return the index and steps taken if found
            return mid, steps
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    # Return -1 and steps taken if the target is not in the list
    return -1, steps

target_name = "John"
names = ["Alice", "Bob", "John", "Kate", "Mike"]

index_simple, steps_simple = simple_search(names, target_name)
print(f"Simple Search: Found {target_name} at index {index_simple} in {steps_simple} steps")

index_binary, steps_binary = binary_search(sorted(names), target_name)
print(f"Binary Search: Found {target_name} at index {index_binary} in {steps_binary} steps")