#!/usr/bin/python3
def lenim(x):
        k = 0
        for i in x:
                k += 1
        return k

def safe_print_list(my_list=[], x=0):
        count = 0
        try:
                for i in range(0, x):
                        print(my_list[i], end="")
                        count += 1
        except:
                pass
        print()
        return count
