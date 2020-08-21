#!/usr/bin/env python3


def finish_off_list(target, start, remaining):
    for i in range(start, len(remaining)):
        target.append(remaining[i])

def merge_lists(*args):
    args = args[0]
    list1, list2 = args if len(args) > 1 else (args, [])
    i = 0
    j = 0
    returning = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            returning.append(list1[i])
            i+=1
        else :
            returning.append(list2[j])
            j+=1

    finish_off_list(returning, i, list1)
    finish_off_list(returning, j, list2)

    return returning


def merge_lists_in_place(list1, left_start, left_end, right_start, right_end):
    if list1[left_end] <= list1[right_start]:
        return
    else:
        while left_start < left_end and right_start < right_end:
            if list1[left_start] <= list1[right_start]:
                left_start += 1
            else:
                temp = list1[right_start]


def merge_sort_in_place(list1):
    merge_sort_in_place_helper(list1, 0, len(list1) - 1)
    return list1


def merge_sort_in_place_helper(list1, start, end):
    if end - start < 1:
        return start, end
    half = (end - start) // 2 + start
    left_start, left_end = merge_sort_in_place_helper(list1, start, half)
    right_start, right_end = merge_sort_in_place_helper(list1, half + 1, end)

    left_sorted = list1[left_start:left_end + 1]
    right_sorted = list1[right_start:right_end + 1]

    list1[left_start:right_end + 1] = merge_lists((left_sorted, right_sorted))

    return start, end


def merge_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        half = len(list1) // 2
        left = merge_sort(list1[:half])
        right = merge_sort(list1[half:])
        return merge_lists((left, right))


if __name__ == '__main__':
    temp = [1,32,32,413,12,5,134,1,23,3]
    merge_sort_in_place(temp, 0, len(temp)-1)
    print(temp)