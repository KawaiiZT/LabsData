"""Labs 11.04 - Seats Number (Insertion Sort)"""
import json as j
def insertionsort(lst, last):
    """Labs 11.04 - Seats Number (Insertion Sort)"""
    #กำหนดตัวแปร cur เพื่อ check index ปัจจุบันที่กำลังจะถูกเรียงลำดับในแต่ละครั้ง
    cur = 1
    compare = 0

    #ใช้ while loop จนกว่า cur = last
    while cur <= last:
        #นำข้อมูลที่เรียงลำดับไว้ที่ hold
        hold = lst[cur]
        walker = cur - 1
        #ลูป while ภายใน เพื่อทำ compare และ เรียงเลขเพิ่ม
        while walker >= 0:
            #เพิ่มค่า compare
            compare += 1
            #เลื่อนข้อมูลที่ walker ไปทางขวา
            if is_current_smaller(hold, lst[walker]):
                lst[walker+1] = lst[walker]
                #ลดค่า walker ลงไป 1
                walker -= 1
            else:
                break
        lst[walker+1] = hold
        cur += 1
        print(lst)
    print("Comparison times: {}".format(compare))

def is_current_smaller(current, walker):
    """Check if it's current smaller"""
    if current[0] == walker[0]:
        return int(current[1:]) < int(walker[1:])
    else:
        return current[0] < walker[0]
 
insertionsort(j.loads(input().replace("'", '"')), int(input()))
