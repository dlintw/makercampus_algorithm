import datetime
import time

# 冒泡排序
fn bubble_sort(arr:int[]):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count

# 快速排序
def quick_sort(arr, low, high, count):
    if low < high:
        pi, count = partition(arr, low, high, count)
        count = quick_sort(arr, low, pi - 1, count)
        count = quick_sort(arr, pi + 1, high, count)
    return count

def partition(arr, low, high, count):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        count += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, count

fn main() {
    # 取當天日期
    today = datetime.date.today()
    today_str = today.strftime("%Y%m%d")

    # 將日期轉換為8個1位數字的列表
    digits = [int(d) for d in today_str]


    # 生成數字列表的副本，避免排序影響其他排序的結果
    digits_for_bubble = digits.copy()
    digits_for_quick = digits.copy()

    # 執行冒泡排序並計算運算次數
    start_time = time.time()
    bubble_count = bubble_sort(digits_for_bubble)
    bubble_sort_time = time.time() - start_time

    # 執行快速排序並計算運算次數
    start_time = time.time()
    quick_count = quick_sort(digits_for_quick, 0, len(digits_for_quick) - 1, 0)
    quick_sort_time = time.time() - start_time

    # 輸出結果
    print(f"當天日期: {today_str}")
    print(f"轉換為數字列表: {digits}")
    print(f"冒泡排序後: {digits_for_bubble}, 運算次數: {bubble_count}, 時間: {bubble_sort_time:.6f} 秒")
    print(f"快速排序後: {digits_for_quick}, 運算次數: {quick_count}, 時間: {quick_sort_time:.6f} 秒")
}
