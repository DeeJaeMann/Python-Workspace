def simple_search(list, target, index, step=1):
    if list[index] == target:
        return index, step
    elif index == 0:
        return -1, step
    else:
        return simple_search(list, target, index - 1, step + 1)


def binary_search(list, target, low, high, step=1):
    if low > high:
        return -1, step
    else:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid, step
        elif list[mid] < target:
            return binary_search(list, target, mid + 1, high, step + 1)
        else:
            return binary_search(list, target, low, mid - 1, step + 1)


target_name = "John"
names = ["Alice", "Bob", "John", "Kate", "Mike"]

index_simple, steps_simple = simple_search(names, target_name, len(names) - 1)
print(
    f"Simple Recurisive Search: Found {target_name} at index {index_simple} in {steps_simple} steps")

index_binary, steps_binary = binary_search(
    names, target_name, 0, len(names) - 1)
print(
    f"Binary Recursive Search: Found {target_name} at index {index_binary} in {steps_binary} steps")
