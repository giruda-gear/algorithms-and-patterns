import pytest
from solutions.delivery_message import delivery_message


@pytest.mark.parametrize(
    "scenario, timestamps, messages, k, expected_result",
    [
        (
            "all_messages_delivered",
            [1, 2, 3, 4],
            ["A", "B", "C", "D"],
            5,
            [True, True, True, True],
        ),
        (
            "some_messages_delivered",
            [1, 2, 5, 6],
            ["A", "B", "A", "B"],
            5,
            [True, True, False, False],
        ),
        (
            "no_messages_delivered",
            [1, 3, 5, 7],
            ["A", "B", "A", "B"],
            2,
            [True, True, True, True],
        ),
        ("empty_input_lists", [], [], 2, []),
        (
            "large_k_value",
            [1, 10, 20, 30],
            ["A", "B", "C", "D"],
            100,
            [True, True, True, True],
        ),
        (
            "messages_repeating_within_k_seconds",
            [1, 4, 5, 10, 11, 14],
            ["hello", "bye", "bye", "hello", "bye", "hello"],
            5,
            [True, True, False, True, True, False],
        ),
        (
            "messages_repeating_within_k_seconds 2",
            [2, 5, 8, 12, 15, 20],
            ["apple", "banana", "apple", "banana", "apple", "banana"],
            7,
            [True, True, False, True, True, True],
        ),
    ],
)
def test_delivery_message(scenario, timestamps, messages, k, expected_result):
    assert delivery_message(timestamps, messages, k) == expected_result
