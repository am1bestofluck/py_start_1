<style>
binary_operators {
  color: orange;
}
keywords {
  color: blue;
}
keywords_bold {
    color: blue;
    font-weight: 700;
}
strings {
    color: green;

}
attention {
    color:cyan;
    font-weight: 700;
}
Classes {
    color:#00994c;
}
import
{
    color:#7f00ff;
}
NO
{
    text-decoration: line-through
}

</style>
# Code conventions  

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.  
  
## Таб или пробелы?  
> Spaces are the preferred indentation method.  

>Tabs should be used solely to remain consistent with code that is already indented with tabs. Python disallows mixing tabs and spaces for indentation. 

Отступ это четыре пробела.  
___
## Отступы  

<pre>многострочные конструкции нужно выделять (либо в вертикальные блоки,  
                                            штатными средствами редактора),
либо (
    выделять отступом и
    отдельной строкой):
вот так </pre>
<pre> Конструкция "if (" создаёт отступ, и этим может создать внешнюю путаницу с отступом для кода после объявления условий if.  

если (так 
        происходит)
    можно добавить отдельный отступ внутри условий если,
    чтобы явно отличать где начинаются операторы
Сам Python Enhancement Proposal (PEP) оставляет это на откуп пользователя.</pre>  
<pre>Скобку(
    закрывающую, многострочный,
    список аргументов
    )
можно(
    поставить как под первым не-пробельным( whitespace),
    символом так и в начале строки
).</pre>
___
## Длина строки    
\###############################################################################

**Не больше 79 знаков в строке.**
---  
\########################################################################  

Для многострочных блоков кода, например докстрингов, комментариев, много-  
уровневых блоков кода, длина строки не должна превышать 72 знака.  
Предпочитаемый способ разбиения строк- встроенный.  

Заворачиваем выражение в скобочку ({[ и оставляем её открытой в месте разрыва ]}).Лучше использовать скобки, а не бэкслэш.  
Бэкслэш _иногда_ можно применять. Например в конструкциях with:  

<pre><keywords_bold>with</keywords_bold> <keywords>open</keywords>(<strings>'/path/to/some/file/you/want/to/read'</strings>) <keywords>as</keywords> file_1, <attention>\</attention>
    <keywords>open</keywords>(<strings>'/path/to/some/file/being/written'</strings>, <strings>'w'</strings>) <keywords>as</keywords> file_2:  
     file_2<binary_operators>.</binary_operators>write(file_1<binary_operators>.</binary_operators>read())</pre>
В assert'ах тоже применяем бэкслеш.  
Независимо от метода переноса помним об отступах.  

**Придерживаясь регламента в этом вопросе, можем открывать несколько   
окон редактора без страданий.**   
## Линию разрывать до или после бинарного оператора*?
##### * Бинарный оператор создает новую переменную из двух других. Например =-*/  
Разрываем многоуровневый блок кода ДО оператора, сам оператор отделяем пробелом.  
<pre> чистая прибыль <binary_operators>=</binary_operators> ( 
    комиссия от заказов
    <binary_operators>+</binary_operators> взносы клиентов
    <binary_operators>-</binary_operators> (аренда <binary_operators>+</binary_operators> хозяйственные расходы)
    <binary_operators>-</binary_operators> налоги
    <binary_operators>-</binary_operators> зарплата
)</pre>

## Обрамление пустыми строками
<pre><br><br><binary_operators>Функции </binary_operators> <keywords>Головного_уровня</keywords> и <br><br>
<keywords>Классы</keywords> <Classes>Отделяются </Classes>
    <strings>"""двойной пустой строкой спереди и сзади."""</strings><br>
    <binary_operators>методы </binary_operators> <keywords>класса</keywords>
        отделяются одной строкой спереди и сзади<br><br><br></pre>
Можно _реже_ устанавливать дополнительные разрывы между логическими блоками, и наоборот убирать их для подчеркивания связности.

## Кодировки  
##### _улыбаемся и машем **большой студии**_  
Файлы **всегда** должны кодироваться в utf-8. Указывать кодировку не нужно.  
Пользуем ASCII символы, кроме обозначения имён и мест.
Если пользуем не-аски в качестве данных __почему в коде??__, то не пишем ересь типа ♥◘г╒╘▌╞┘╒♥z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘.. Не очень то и хотелось.  
Все имена только в аски, при этом лучше слова будут английские, если возможно. (ну как перевести слово 'borsch'?)
\* Кстати, шутка в том что борщ как раз так и переводится. Но это транскрипционный аналог.  
## Импорты
Импортируем каждый модуль отдельной строкой.
<pre><import>import</import> correct 
<import>import</import> way
<NO><import>import</import> bad, code</NO></pre>
Но можно импортировать функции из модуля одной строкой
<pre><import>from</import>  our_lib <import>import</import>  functions, right</pre>
Импорты собираем в одном месте. Вверху файла. После докстрингов. До глобальных переменных и констант.

Порядок импортирования:  
* стандартные библиотеки
* "relative third party imports" Т.е. тоже классные и сложные библиотеки, просто не от друзей Гвидо.
* библиотеки локального уровня, т.е. НАши :).

Уровни импортирования нужно разделять одинарной линией, можно даже написать комментарий что есть что...   
Рекомендуются абсолютные импорты..._никто не знает про venv_
Относительные импорты допускаются если абсолютное импортирование усложняет код. _конфликт версий?_
Импортируем кусочек модуля из полного, если это не вызывает конфликт имён.
<pre>
<import>from</import> myclass <import>import</import> MyClass
<import>from </import> foo.bar.yourclass <import>import</import> YourClass
a=MyClass
b=YourClass</pre>
Если конфликт всё же есть, импортируем так:
<pre>
<import>import</import> myclass
<import>import</import> foo.bar.yourclass
a=myclass.MyClass
b=foo.bar.yourclass.YourClass</pre>

> Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools.
## Module Level Dunder Names
##### ...или, "Мама, смотри, Я синьёр"
Модульные "х здесь навсегда" переменные 
<pre>'''This is the example module.

It does all and well.
'''
from __future__ import 
__version__ = '0.1'

__author__ = 'Cardinal Biggles'</pre>
вставляются после докстрингов, но перед импортами, КРОМЕ from \_\_future__ import- категории.   
## оффтоп. Что вообще такого особенного в future? C stackoverflow:
> Future statements are special -- they change how your Python module is parsed, which is why they must be at the top of the file. They give new -- or different -- meaning to words or symbols in your file. From the docs:
A future statement is a directive to the compiler that a particular module should be compiled using syntax or semantics that will be available in a specified future release of Python. The future statement is intended to ease migration to future versions of Python that introduce incompatible changes to the language. It allows use of the new features on a per-module basis before the release in which the feature becomes standard
## Кавычки
Всем всё равно. Но если в строке тоже есть кавычка, то внутренние и обрамляющие должны различаться, потому что бэкслэш усложняет чтение.  
**Но** внутри """троекратной строки""" кавычки используем "двойную кавычку, согласно pep257..._сколько их?_.
## Пустоты(whitespace) внутри выражений и  утверждений( присваиваний?)
|Не нужны вайтспейсы:  |пример|
|-|-|
после скобки  |Concat( first_string, second_string)
между запятой и закрывающей скобкой _зачем запятая?_ | Concat( first_string,)
сразу перед запятой, двоеточием, точкозапятой | if x == 4: print( x, y); x, y = y, x
перед скобкой обрамляющей аргументы функции| \_\_sum__( a, b)
перед скобкой среза |myDict['key']== myList[index]
чтобы выровнять ключи переменных| a = 1
с разной длиной названий |  long_name = 2

В целом **не** пользуем последовательность пробелов;  
Всегда оборачиваем бинарные операторы одним пробелом с каждой из сторон.  
<pre>
Для целей этой главы, бинарные операторы это:  
присвоение: <binary_operators>=</binary_operators>
дополненное присвоение: <binary_operators>+=</binary_operators>, <binary_operators>-=</binary_operators> и т.д.
операторы сравнения : <binary_operators>== < > != <> <= >= in, not in, is, is not </binary_operators> #запятые должны быть белыми, но там ТАКОЕ в коде странички :)
Boolean: <binary_operators>and</binary_operators>, <binary_operators>or</binary_operators>, <binary_operators>not</binary_operators></pre>
Если выражение содержит бинарные операторы разного уровня, лучше б.о. наинизшего приоритета обрамить пробелами:  

<pre>x <binary_operators>=</binary_operators> 2<binary_operators>*</binary_operators>a <binary_operators> + </binary_operators> 3<binary_operators>*</binary_operators>b
x <binary_operators>=</binary_operators> a <binary_operators>+</binary_operators> b
tmp <binary_operators> += </binary_operators>1
hyp_sqr<binary_operators> = </binary_operators>(a<binary_operators>*</binary_operators>a)<binary_operators> + </binary_operators>(b<binary_operators>*</binary_operators>b) </pre>
Function annotatation _примечания_ внутри скобок подчиняются обычным правилам скобок, а ожидаемый тип вывода **->** определяется как бинарный оператор  
Знак "=" для дефолтного значения аргументов пробелами не выделяется.
<pre>
<binary_operators>def</binary_operators> <keywords> pack_input</keywords>(firstString<binary_operators>=</binary_operators><strings>"Adam"</strings>, secondString<binary_operators>=</binary_operators><strings>"Smit"</strings>):
    <import>return</import> (firstString,secondString) </pre>