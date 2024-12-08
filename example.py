from collections.abc import Sequence, Callable
from typing import TypeVar

from example_types import CountriesType

x: list[int] = [1, 2, 3]

one: int
two: int
three: int

one, two, three = x

#1. Union - bad solution

def combine(a: int | str,b: int | str) -> int | str:
    return a + b

r1 = combine(1, 2) # int, 3
r2 = combine("1", "2") # str , "12"
#r3 = combine(1, "2") # TypeError
r4: int = combine("1", "2")

#2 Two dedicated functions (DRY) bad solution
def combine_no(a: int,b: int) -> int:
    return a + b

def combine_txt(a: str,b: str) -> str:
    return a + b

# 3. Generic types

# T = TypeVar("T", bound= [int, str]) # to tez dobre
T = TypeVar("T",str, int)

def combine_(a: T, b: T) -> list[T]:
    return [a , b]

res1 = combine_(1, 2)
res2 = combine_("ala", "ola")



def yolo():
    ...
U= TypeVar('U')

def magic(data: Sequence[U]) -> U:
    return data[0]

v = magic((1, 2, 3))
v2 = magic((1, 2))



#dict
countries: dict[str , str] = {
    "poland": "warsaw",
    "germany": "berlin"
}

counttries_2: CountriesType ={
    "europe":{
        "poland": "warsaw",
        "germany": "berlin"

    },
    "asia":{
        "china": "beijing"
    }
}


def my_max(*args: int):
    return max(args)

x_yolo = my_max(1 ,2 , 3, 4, 5)

T = TypeVar("T")

def sentence(cb: Callable[[T],T] ,txt: T) -> T:
    return cb(txt)

sentence( lambda x: x.upper(), "ala ma kota")