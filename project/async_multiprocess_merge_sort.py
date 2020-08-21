#!/usr/bin/env python3

from multiprocessing import Pool
import merge_sort
import time
from random import randint
import asyncio


async def multiprocess_merge_sort(list1, processes):
    tic = time.perf_counter()
    sublists = []
    for i in range(processes):
        sublists.append(list1[i::(processes * 2)])

    with Pool(processes) as p:
        sublists = p.map(merge_sort.merge_sort_in_place, sublists)

        while len(sublists) > 1:
            # want groupings of 2 to merge
            # if odd then add empty list to end to get around tuple pairs
            if len(sublists) % 2 == 1:
                sublists.append([])
            temp = [(sublists[i], sublists[i + 1]) for i in range(0, len(sublists), 2)]
            sublists = list(p.map(merge_sort.merge_lists, temp))
    return sublists[0], time.perf_counter() - tic


def make_list(size):
    result = []
    for i in range(int(size)):
        result.append(randint(0, 1000))
    return result


if __name__ == '__main__':
    for i in range(5):
        size = 10 ** i

        big_list = make_list(size)
        processes = 10

        multi_task = asyncio.create_task(multiprocess_merge_sort(big_list, processes))
        single_task = asyncio.create_task(merge_sort.merge_sort_in_place(big_list))

        [await task for task in [multi_task, single_task]]

        print(f"\nTesting with list size of {size}")
        print(f"Parrallel merge sort on {processes} cores took:   {multi_task.result()[1]}s")
        print(f"Single core merge sort took:             {single_task.result()[1]}s")
        print()
