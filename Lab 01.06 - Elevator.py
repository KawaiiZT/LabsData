"""dOCSITRNG"""
class Elevator:
    """Docstring"""
    #init รับมาจาก elevator = Elevator(max_floor)
    def __init__(self, max_floor):
        """Docstring"""
        #ตั้งค่าเริ่มต้น current_floor ไว้ที่ 1
        self.current_floor = 1
 
        #self.max_floor = max_floor เปลี่ยนแปลงจาก ค่าที่รับเข้ามาตอนแรก
        self.max_floor = max_floor
 
    def go_to_floor(self, floor):
        """Docstring"""
        #ถ้ามีค่ามากกว่า 1 และน้อยกว่า max_floor ให้ค่า floor ที่รับเข้ามากลายเป็น currect_floor
        if 1 <= floor <= self.max_floor:
            self.current_floor = floor
        #ถ้า floor มีค่าน้อยกว่า 1 หรือ มากกว่า max_floor ให้ตอบว่า "Invalid Floor!"
        else:
            print("Invalid Floor!")
 
    def report_current_floor(self):
        """Docstring"""
        #รับค่ามาจาก def go_to_floor
        print(self.current_floor)
 
#ใส่ชั้นสูงสุด เป็น Constant เลยตัวใหญ่
MAX_FLOOR = int(input())
#ELEVATOR เป็นตัวเชื่อมต่อกับ Class Elevator
ELEVATOR = Elevator(MAX_FLOOR)
 
while True:
    #ใส่input ทั้งตัวเลขและอักษร
    inputfloor = input()
 
    #ใส่input Done = หยุด
    if inputfloor == "Done":
        break
 
    #นำ floor ที่ได้รับมาจาก input เชื่อมไปที่ ELEVATOR ที่เชื่อมต่อกับ Class Elevator
    try:
        floor = int(inputfloor)
        ELEVATOR.go_to_floor(floor)
 
    #ให้ยกเว้น ValueError ถ้าเป็นให้ตอบ Invalid Floor!
    except ValueError:
        print("Invalid Floor!")
 
#แสดงผลจากเมธอด .report_current_floor() เชื่อมไปที่ ELEVATOR ที่เชื่อมต่อกับ Class Elevator
ELEVATOR.report_current_floor()