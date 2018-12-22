'''
LOW B三人组：
冒泡
选择
插入

NB三人组
快排
堆排
归并
'''


'''
冒泡排序：
    原理：序列按照索引顺序由下至上，以此数个比较，若下面的数比上面的数大，则交换位置
    关键点：1、趟数；2、每一趟都会逐渐缩小无序区域
'''

# def bubble_sort(l):
#     for i in range(len(l)-1):  # 总趟数
#         for j in range(len(l)-1-i):  # 每趟内部再进行排序
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return l
#
#
# if __name__ == '__main__':
#     l = [5,1,12,10,6,3,8,4]
#     print(bubble_sort(l))



'''
选择排序：
1、每次遍历，找出最小的数的索引；


'''

# def selection_sort(l):
#     for i in range(len(l)):
#         # 每一趟初始最小索引为无序区域第一个数
#         min_index = i
#         for j in range(i,len(l)):
#             if l[j]<l[min_index]:  # 每一趟会取出最小数的索引
#                 min_index=j
#         # 最小数与无序区域的第一个数交换位置
#         l[min_index],l[i]=l[i],l[min_index]
#     return l
#
#
# l = [5,1,12,10,6,3]
# print(selection_sort(l))


def partition(lst, left, right):
    '''
    以一次排序为例
    left=0
    right= len(lst)-1
    '''
    tmp = lst[left]  # 左侧第一个数
    while left < right:
        # 1、右侧指针从最右侧逐个左移动,本质上就是right值递减，直到对应的值小于p值
        while left < right and lst[right] >= tmp:
            right -= 1
        # 2、将找到小于p的值数移动到左侧第一位，对应的位置就空出来
        lst[left] = lst[right]

        # 3、指针移动到左侧，逐个右移，直到左侧的数大于7
        while left < right and lst[left] <= tmp:
            left += 1
        lst[right] = lst[left]

    lst[left] = tmp
    return left


def _quick_sort(lst, left, right):
    """快排"""
    if left < right:
        mid = partition(lst, left, right)
        _quick_sort(lst, left, mid - 1)
        _quick_sort(lst, mid + 1, right)



l = [5,7,4,6,3,1,2,9,8]

_quick_sort(l,0,len(l)-1)

print(l)