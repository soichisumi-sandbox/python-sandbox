import os


def show_arg_and_result(a, b):
    return f'a: {a}, b: {b}, external result: {get_result()}'


def get_result():
    return "see you"


class Yo:
    member_a = 'A'
    member_5 = 5
    __hidden = 10
    _hidden = "10"


