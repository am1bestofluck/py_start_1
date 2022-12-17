"""
GB Программист, "Знакомство с языком Python( семинары)", #1 
t1 Сообщает, выходной или нет 
t2 Строит таблицу истинности
t3 Сообщает квадрант точки на плоскости
t4 Считает расстояние между точками на плоскости
"""

from __future__ import annotations


__all__ = ['Point_2D', 'Break', 'validate_input']
__version__ = "#1"
__author__ = "anton6733@gmail.com"


import math
import os
import sys
from typing import Tuple


class Point_2D:
    """Класс для точки на двухмерной оси координат
    """

    def __init__( self, abscissa: int, ordinate: int) -> None:
        """Определяет позицию точки на плоскости

        abscissa - координата по  оси OX
        ordinate - координата по оси OY
        """
        if not isinstance(abscissa,int):
            ordinate=validate_input()
        if not isinstance(ordinate,int):
            ordinate=validate_input()
        self.location = ( abscissa, ordinate)
        return None 

    def GetQuadrant( self) -> str:
        """Переводим систему координат на русский язык"""
        if self.location[0] == 0:
            return "Точка лежит на оси OX"
        if self.location[1] == 0:
            return "Точка лежит на оси OY"
        if self.location[0] > 0:
            return "1" if self.location[1] > 0 else "4"
        else:
            return "2" if self.location[1] > 0 else "3"
    
    def GetDistance( point_1: Point_2D , point_2: Point_2D ) -> float:
        """Определяем расстояние между двумя точками"""
        return round( ndigits=2, number =
            math.sqrt(
            ( point_1.location[0] - point_2.location[0] )**2
            + ( point_1.location[1] - point_2.location[1])**2
            ))


def validate_input(limits: Tuple[int,]=(- sys.maxsize, sys.maxsize ), 
    accepts_zero = True, short_note: str = "") -> int:
    """~~~Харасим юзера.~~~ 
    
    wrong - основа костыля TryParse из шарпа
    msg - приглашение ко вводу
    tmp - буфер для инпута
    output - выводное значение
    multiplier - костыль для отрицательных инпутов
    accepts_zero - если False - ноль не пропускаем
    short_note - описание задачи вызова
    """
    if short_note:
        print( short_note)
    output: int
    tmp: str
    msg = "Input number?"
    wrong = True
    while wrong:
        tmp = input(msg)
        multiplier = -1 if tmp.startswith( '-') else 1
        tmp=tmp.removeprefix( '-')
        if not tmp.isdigit():
            msg="Input number?"
            continue
        output = int( tmp) * multiplier
        if output not in range( limits[0],limits[1]):
            msg = f"Between {limits[0]} and {limits[1]-1}. Try again."
        elif not accepts_zero and output == 0:
            msg =" Zero is not accepted. Try again"
        else:
            wrong = False
    return output


def Break():
    """Чистим консоль, чтобы не переполнять внимание :'D"""
    input("Enter to proceed.")
    os.system('cls')


def t1( day_of_week_number: int = 0) -> bool:
    """Напишите программу, которая принимает на вход цифру, 
    обозначающую день недели, и проверяет,
    является ли этот день выходным.

    limits - границы допустимого ввода для проверки
    week_end_days - признак выходного
    """
    limits_week = ( 1,8)
    week_end_days = ( 6,7)
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
    
    for move_x in x:
        for move_y in y:
            for move_z in z:
                equation= not( move_x,move_y,move_z) == (not move_x 
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
    """Напишите программу, которая принимает на вход координаты 

    точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 

    плоскости, в которой находится эта точка (или на какой оси 

    она находится).
    """
    point_1=Point_2D( 
        abscissa=validate_input( accepts_zero = False,
        short_note = "Input x coordinate"),
        ordinate=validate_input( accepts_zero = False,
        short_note = "Input y coordinate"))
    print( point_1.GetQuadrant())


def t4():
    """
    Напишите программу, которая принимает на вход координаты двух

    точек и находит расстояние между ними в 2D пространстве.
    """
    here=Point_2D( 
        abscissa=validate_input( short_note = "Input x coordinate (1)"),
        ordinate=validate_input( short_note = "Input y coordinate (1)"))
    there=Point_2D( 
        abscissa=validate_input( short_note = "Input x coordinate (2)"),
        ordinate=validate_input( short_note = "Input y coordinate (2)"))
    print( Point_2D.GetDistance( point_1 = here, point_2= there))


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
        t1_decorated()
        t2_decorated()
        t3_decorated()
        t4_decorated()
        

if __name__=='__main__':
    main()