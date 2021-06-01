import pytest
from pytest_mock import MockerFixture
import src.code


@pytest.mark.parametrize(("a", "b"), [
    ("a", "b")
])
def test_show_arg_and_result_spy(mocker: MockerFixture, a, b) -> None:
    spy = mocker.spy(src.code, "get_result")
    assert src.code.show_arg_and_result(a, b) == 'a: a, b: b, external result: see you'
    assert spy.call_count == 1
    assert spy.spy_return == "see you"


@pytest.mark.parametrize(("a", "b"), [
    ("a", "b")
])
def test_show_arg_and_result_mock(mocker: MockerFixture, a, b) -> None:
    mock = mocker.patch("src.code.get_result", return_value="hi")
    assert src.code.show_arg_and_result(a, b) == 'a: a, b: b, external result: hi'
    assert mock.call_count == 1
    assert mock.return_value == "hi"
