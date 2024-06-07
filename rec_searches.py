def simple_search(list, target, index, step = 1):
    if list[index] == target:
        return index, step
    elif index == 0:
        return -1, step
    else:
        return simple_search(list, target, index - 1, step + 1)
    
target_name = "John"
names = ["Alice", "Bob", "John", "Kate", "Mike"]

index_simple, steps_simple = simple_search(names, target_name, len(names) - 1)
print(f"Simple Recurisive Search: Found {target_name} at index {index_simple} in {steps_simple} steps")
        