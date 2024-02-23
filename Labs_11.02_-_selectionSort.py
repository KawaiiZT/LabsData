"""Labs 11.02 - selectionSort()"""
def selectionsort(lst, last):
    """Labs 11.02 - selectionSort()"""
    cur = 0
    compare = 0

    while cur < last:
        smallest = cur
        walker = cur + 1

        while walker <= last:
            # เปรียบเทียบค่าของ walker กับค่าของ smallest
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1
            compare += 1

        # สลับค่าของ elements ที่ current และ smallest
        lst[cur], lst[smallest] = lst[smallest], lst[cur]
        cur += 1

        print(lst)

    print("Comparison times: {}".format(compare))
selectionsort(list(map(int, input().strip("[]").split(", "))), int(input()))
