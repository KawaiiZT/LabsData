"""Docstring"""
import json
def main():
    """Docstring"""
    my_list = json.loads(input())
    lmx = 0
    lmn = 0
    lavg = 0
    for i in my_list:
        if i > lmx:
            lmx = i
        if lmn == 0 or i < lmn:
            lmn = i
        lavg += i
    lavg = round(lavg/len(my_list), 2)
    print("(%s, %s, %s)" %(lmx, lmn, lavg))
main()
