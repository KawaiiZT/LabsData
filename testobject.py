class Student:
    def __init__(self, in_id, in_name, in_add):
        #attr
        self.id = in_id
        self.name = in_name
        self.address = in_add
    def show_detail(self):
        #method
        print("ID : ", self.id) 
        print("Name : ", self.name)
        print("Address : ", self.address)

    def set_name(self, new_name):
        self.name = new_name

std1 = Student("66070069", "Trisit Charoenparipat", "Bangkok")
std1.show_detail()

std2 = Student("660700xx", "Ji", "Banggog")
std2.set_name("TTTT")
std2.show_detail()
        