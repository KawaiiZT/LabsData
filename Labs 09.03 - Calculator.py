"""Labs 09.03 - Calculator"""
def main(num):
    '''Labs 09.03 - Calculator'''
    if num == 1:
        print(1)
    else:
        total = 0
        for i in range(1, num+1):
            total += len(str(i))
    print(num+total)
main(int(input()))