#! /usr/bin/python3  # 确保程序能在Linux系统中直接执行
import random
import time
from sort_algorithm import selection_sort, bubble_sort, optimized_bubble_sort, cocktail_sort, insertion_sort, shell_sort, quick_sort

# 生成10000项的 -1000 到 1000 随机数组
nums = [random.randint(-1000, 1000) for i in range(10000)]


def cal_run_time(name_of_function, name):
    """计算程序运行时间

    :param name_of_function: 排序方法
    :param name: 对排序数组的描述--排序数组的中文名字，方便辨别
    """
    # 开始计时
    print(f"开始进行 {name} ......")
    start_time = time.perf_counter()
    # 执行程序
    res = name_of_function(nums[::])  # 通过nums[::]传入nums的复件，对nums[::]进行排序，不会影响到nums
    # 结束计时
    end_time = time.perf_counter()
    print(res)
    print(f"耗时{end_time - start_time}\n")


if __name__ == "__main__":

    # 存在一个问题，在依次选择排序方法对数组进行排序时，除了第一个排序方法
    # 是对无序数组进行排序，后面的方法处理的都是已经排序好的数组
    # 如何解决？？？

    # names = {"选择排序": selection_sort,
    #          "冒泡排序": bubble_sort,
    #          "优化的冒泡排序": optimized_bubble_sort,
    #          "鸡尾酒排序": cocktail_sort,
    #          "插入排序": insertion_sort,
    #          "希尔排序": shell_sort,
    #          "快速排序": quick_sort
    #          }
    #
    # print(f"未经排序的数组：\n{nums}\n")
    # for k, v in names.items():
    #     cal_run_time(v, k)

    print(nums)
    cal_run_time(quick_sort, "快速排序")

