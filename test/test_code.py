import pytest
from pytest_mock import MockerFixture
from src import code


@pytest.mark.parametrize(("a", "b"), [
    ("a", "b")
])
def test_show_arg_and_result_spy(mocker: MockerFixture, a, b) -> None:
    spy = mocker.spy(code, "get_result")
    assert code.show_arg_and_result(a, b) == 'a: a, b: b, external result: spy here'
    assert spy.call_count == 1
    assert spy.spy_return == "spy here"


@pytest.mark.parametrize(("a", "b"), [
    ("a", "b")
])
def test_show_arg_and_result_mock(mocker: MockerFixture, a, b) -> None:
    mock = mocker.patch("src.code.get_result", return_value="hi")
    assert code.show_arg_and_result(a, b) == 'a: a, b: b, external result: hi'
    assert mock.call_count == 1
    assert mock.return_value == "hi"


def test_class_member():
    c = code.Yo
    assert c.member_a == 'A'
    assert c.member_5 == 5

    for k, v in vars(c).items():
        print(f'k: {k}, v: {v}')
