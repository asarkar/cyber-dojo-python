from leap_years import is_leap_year


def test_year_not_divisible_by_4_in_common_year() -> None:
    assert not is_leap_year(2015)


def test_year_divisible_by_2_not_divisible_by_4_in_common_year() -> None:
    assert not is_leap_year(1970)


def test_year_divisible_by_4_not_divisible_by_100_in_leap_year() -> None:
    assert is_leap_year(1996)


def test_year_divisible_by_4_and_5_is_still_a_leap_year() -> None:
    assert is_leap_year(1960)


def test_year_divisible_by_100_not_divisible_by_400_in_common_year() -> None:
    assert not is_leap_year(2100)


def test_year_divisible_by_100_but_not_by_3_is_still_not_a_leap_year() -> None:
    assert not is_leap_year(1900)


def test_year_divisible_by_400_is_leap_year() -> None:
    assert is_leap_year(2000)


def test_year_divisible_by_400_but_not_by_125_is_still_a_leap_year() -> None:
    assert is_leap_year(2400)


def test_year_divisible_by_200_not_divisible_by_400_in_common_year() -> None:
    assert not is_leap_year(1800)
