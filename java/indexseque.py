def indexed_sequential_search(data, index, target):
    """index = list of (first_key_of_block, start_index)."""
    block_start = None
 
    for first_key, start in index:
        if target < first_key:
            break
        block_start = start
 
    if block_start is None:
        return -1
 
    # Sequential search inside the selected block
    for position in range(block_start, len(data)):
        if data[position] == target:
            return position
        if position + 1 < len(data) and data[position + 1] > target:
            break
    return -1
 
data = [3, 7, 12, 18, 25, 31, 40, 46, 52, 60]
index = [(3, 0), (18, 3), (40, 6), (60, 9)]
print(indexed_sequential_search(data, index, 31))
print(indexed_sequential_search(data, index, 7))
print(indexed_sequential_search(data, index, 45))
