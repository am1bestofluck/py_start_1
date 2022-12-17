"""
GB Программист, "Знакомство с языком Python( семинары)", #1 
t1 Сообщает, выходной или нет 
t2 Строит таблицу истинности
t3 Сообщает квадрант точки на плоскости
t4 Считает расстояние между точками на плоскости
"""


__all__ = ['Point_2D','Break']
__version__ = "#1"
__author__ = "anton6733@gmail.com"


import os
import sys
from typing import Tuple


def validate_input(limits = (- sys.maxsize, sys.maxsize ) ) -> int:
    """~~~Харасим юзера.~~~ 
    Принимаем день недели с клавиатуры.
    
    wrong - основа костыля TryParse из шарпа
    msg - приглашение ко вводу
    tmp - буфер для инпута
    output- выводное значение
    """
    output: int
    tmp: str
    msg="Input number?"
    wrong=True
    while wrong:
        tmp = input(msg)
        if not tmp.isdigit():
            msg="Input number?"
            continue
        output = int( tmp)
        if output not in range( limits[0],limits[1]):
            msg="Between 1 and 7. Try again."
        else:
            wrong = False
    return output


def Break():
    input("Enter to proceed.")
    os.system('cls')


def t1(day_of_week_number: int = 0) -> bool:
    """Напишите программу, которая принимает на вход цифру, 
    обозначающую день недели, и проверяет,
    является ли этот день выходным.

    limits - границы допустимого ввода для проверки
    week_end_days - признак выходного
    """
    limits_week=( 1,8)
    week_end_days=( 6,7)
    day_of_week_number_m = day_of_week_number if ( 
        day_of_week_number in range(limits_week[0],limits_week[1])
        ) else validate_input(limits=limits_week)
    return True if day_of_week_number_m in week_end_days else False


def t2() -> None:
    """
    Напишите программу для. проверки истинности утверждения 
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    звучит как скрипт без ввода и вывода...
    x y z - шагаем по bool
    """
    print()
    x = y = z= (True,False)
    breaker=' | '
    
    for move_x in x:
        for move_y in y:
            for move_z in z:
                equation= not( move_x,move_y,move_z)== (not move_x 
                and not move_y and not move_z)
                print(f'not ({move_x}'.ljust(10,' '),end=' and ')
                print(f'{move_y}'.ljust(6,' '),end='and ')
                print(f'{move_z})'.ljust(7,' '),end=' == ')
                print(f'not {move_x}'.ljust(9,' '),end=' and ')
                print(f'not {move_y}'.ljust(9,' '),end=' and ')
                print(f'not {move_z}'.ljust(9,' '),end=' = ')
                print(equation)
    return None


def t3():
    return 't3'


def t4():
    return 't4'


class Point_2D:
    def __init__(self,ordinate:int,abscissa:int) -> None:
        pass

def main():

    def t1_decorated() -> None:
        print(t1.__doc__)
        print(t1())
        Break()
        return None

    def t2_decorated() -> None:
        print(t2.__doc__)
        print(t2())
        Break()
        return None

    def t3_decorated() -> None:
        print(t3.__doc__)
        print(t3())
        Break()
        return None

    def t4_decorated() -> None:
        print(t4.__doc__)
        print(t4())
        Break()
        return None

    if len( sys.argv ) >1:
        if "all" in sys.argv[1:]:
            t1_decorated()
            t2_decorated()
            t3_decorated()
            t4_decorated()
            sys.exit()
        for arg in sys.argv[1:]:
            if arg == 't1':
                t1_decorated()
            elif arg == 't2':
                t2_decorated()
            elif arg == 't3':
                t3_decorated()
            elif arg == 't4':
                t4_decorated()
            else:
                print( __doc__)
                break
    else:
        t1()
        t2()
        t3()
        t4()
        
"""



t3() Напишите программу, которая принимает на вход координаты 
точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).

t4() Напишите программу, которая принимает на вход координаты двух 
точек и находит расстояние между ними в 2D пространстве.

"""


if __name__=='__main__':
    main()