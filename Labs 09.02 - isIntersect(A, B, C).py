"""Labs 09.02 - isIntersect(A, B, C)"""
import json as j
def isintersect():
    """Labs 09.02 - isIntersect(A, B, C)"""
    aaa = j.loads(input())
    bbb = j.loads(input())
    ccc = j.loads(input())
    for i in aaa:
        if i in bbb and i in ccc:
            print(True)
            break
        else:
            print(False)
            break
isintersect()