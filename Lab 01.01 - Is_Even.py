"""Docstring"""
def main(numb):
    """Docstring"""
    if str(numb)[-1] in "02468":
        print(True)
    else:
        print(False)
main(int(input()))
