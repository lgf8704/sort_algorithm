"""几种简单的排序算法
1 - 选择排序 -- selection sort
2 - 冒泡排序 -- bubble sort
3 - 改进的冒泡排序 -- optimized bubble sort
4 - 鸡尾酒排序 -- cocktail sort
5 - 插入排序 -- insertion sort
6 - 快速排序 -- quick sort
"""
import random


def selection_sort(nums):
    """
    过程简单描述：
首先，找到数组中最小的那个元素，
其次，将它和数组的第一个元素交换位置(如果第一个元素就是最小元素那么它就和自己交换)。
再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。
如此往复，直到将整个数组排序。这种方法我们称之为选择排序。

    :param array: 待排序数组
    """

    N = len(nums)
    for i in range(N):
        # 从第i + 1个元素开始，与第i个元素比较，找到最小值，并将其与第一个元素交换(i, i + 1为下标）
        for j in range(i + 1, N):
            if nums[j] < nums[i]:
                # 交换，让较大的靠后
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def bubble_sort(nums):
    """每一次两两进行比较，每进行一个循环，都有一个大数沉底
    第一个元素与第二个元素比较，如果第一个比第二个大，则交换他们的位置。
    接着继续比较第二个与第三个元素，如果第二个比第三个大，则交换他们的位置….

    我们对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，
    这样一趟比较交换下来之后，排在最右的元素就会是最大的数。

    除去最右的元素，我们对剩余的元素做同样的工作，如此重复下去，直到排序完成。

    :param array: 待排序数组
    """

    N = len(nums)
    for i in range(N - 1):
        flag = True
        for j in range(N - i - 1):
            # 后一项小于前一项，交换
            if nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                flag = False
        if flag:
            break

    return nums


def optimized_bubble_sort(nums):

    N = len(nums)

    for i in range(N - 1):
        flag = True
        for j in range(N - i - 1):
            # 后一项小于前一项，交换
            if nums[j + 1] < nums[j]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                flag = False
        # 判断是否有交换
        if flag:
            break
    return nums


def cocktail_sort(nums):
    """双向冒泡排序
    同样可以通过flag来优化
    :param nums: 待排序数组
    """

    N = len(nums)
    left = 0
    right = N - 1

    while left < right:
        # 从左向右移动
        flag = True
        for i in range(left, right):
            if nums[i + 1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # 交换数值
                flag = False

        right -= 1  # nums[right]已排序完成
        # 从右向左移动
        for j in range(right, left, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                flag = False
        left += 1  # nums[left]已排序完成

        if flag:
            break
    return nums


def insertion_sort(nums):

    """插入排序 -- 将数组分成两个部分，左边的为有序数组，右边的为无序数组，依次
    遍历右边数组的元素，插入到左边的有序数组中去
    1、从数组第2个元素开始抽取元素。

    2、把它与左边第一个元素比较，如果左边第一个元素比它大，
    则继续与左边第二个元素比较下去，直到遇到不比它大的元素，然后插到这个元素的右边。

    3、继续选取第3，4，….n个元素,重复步骤 2 ，选择适当的位置插入。

    :param nums: 待排序数组
    :return: 返回排序好的数组
    """
    right = 1  # 将第一个元素视为有序数组，从第二个元素开始，插入到有序数组中去
    N = len(nums)

    while right < N:
        # 已排好序的数组是nums[:right]，其最后一个元素是nums[right - 1]
        left = right - 1  # 从有序元素的最后一个元素开始比较
        # 指针向前移动，依次比较，找到需要插入的位置
        while left >= 0:
            if nums[right] < nums[left]:
                left -= 1
            else:
                break
        # 找到了nums[right]需要插入的位置left，nums[left + 1:right]的元素向右移动一个位置
        i = right - 1
        # 将需要排序的元素nums[right]的数值存储起来
        temp = nums[right]
        while i > left:
            nums[i + 1] = nums[i]
            i -= 1
        nums[left + 1] = temp

        right += 1  # 下一个无序元素

    return nums


def shell_sort(nums):
    """1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。
    它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

    :param nums:
    :return:
    """
    gap = len(nums) // 2
    while gap > 0:
        # 数组被分成gap组
        for i in range(gap, len(nums)):
            # 排序

            left = i - gap
            right = left + gap
            while right < len(nums):
                if nums[right] < nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]
                right += gap

        gap //= 2
    return nums


def quick_sort(nums, left=0, right=None):

    """在数组中选择一个元素作为中间元素，将大于中间元素的元素放在中间元素的右边，小的放左边
    利用递归的方式对左边和右边的数组进行排序，直到数组的个数等于1。

    :param nums: 待排序数组
    :param left: 数组的左边界
    :param right: 数组的右边界
    :return: 返回排好序的数组
    """
    if right is None:
        right = len(nums) - 1

    # 递归结束条件，数组长度不大于1
    if len(nums[left:right + 1]) <= 1:
        return nums

    # 随机产生比较元素的位置
    mid = random.randint(left, right)
    # 将找到的元素调到数组尾部
    nums[mid], nums[right] = nums[right], nums[mid]
    # 将最后一个元素设为比较元素
    mid = right
    i, j = left, left

    while j < right:
        if nums[j] < nums[mid]:
            if j > i:
                nums[j], nums[i] = nums[i], nums[j]
            i += 1
        j += 1

    if mid != i:
        nums[mid], nums[i] = nums[i], nums[mid]
        mid = i

    quick_sort(nums, left, mid - 1)
    quick_sort(nums, mid + 1, right)

    return nums

