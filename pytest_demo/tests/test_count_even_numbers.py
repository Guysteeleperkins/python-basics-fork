from src.list_utils import count_even_numbers


def test_returns_zero_for_empty_list():
    # Arrange
    test_input = []
    expected_output = 0
    # Act
    actual_output = count_even_numbers(test_input)
    # Assert
    assert actual_output == expected_output


def test_returns_zero_for_list_with_value_one():
    # Arrange
    test_input = [1]
    expected_output = 0
    # Act
    actual_output = count_even_numbers(test_input)
    # Assert
    assert actual_output == expected_output


def test_returns_one_for_list_with_value_two():
    # Arrange
    test_input = [2]
    expected_output = 1
    # Act
    actual_output = count_even_numbers(test_input)
    # Assert
    assert actual_output == expected_output
