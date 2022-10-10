def sort_string(char_list):
    if len(char_list) <= 1:
        return char_list
    mid = len(char_list) // 2
    left, right = sort_string(char_list[:mid]), sort_string(char_list[mid:])
    return "".join(merge(left, right, char_list.copy()))


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[right_cursor + left_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    sorted_first_string = sort_string([char.lower() for char in first_string])
    sorted_second_string = sort_string(
        [char.lower() for char in second_string]
    )

    return sorted_first_string == sorted_second_string
