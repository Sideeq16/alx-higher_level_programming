#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            el_1 = my_list_1[i]
            el_2 = my_list_2[i]

            if not isinstance(el_1, (int, float)) or not
            isinstance(el_2, (int, float)):
                raise TypeError("wrong type")
            if el_2 == 0:
                raise ZeroDivisionError("division by 0")
            division_result = el_1 / el_2
            result.append(division_result)
        except IndexError:
            print("out of range")
            break
        except TypeError as e:
            print(e)
            result.append(0)
        except ZeroDivisionError as e:
            print(e)
            result.append(0)
    return result
