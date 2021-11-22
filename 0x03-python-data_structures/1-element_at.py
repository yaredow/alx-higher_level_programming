#!/usr/bin/python3


def element_at(my_list, idx):
    for _ in my_list:
        if idx < 0 or idx > (len(my_list) - 1):
            retunr None
        else:
            return (my_list[idx])
