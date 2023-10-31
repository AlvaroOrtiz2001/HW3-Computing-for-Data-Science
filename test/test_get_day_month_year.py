import pytest
from hw3 import get_day_month_year

def test_get_day_month_year():
    test_dates = [
        datetime.date(2021, 1, 10), 
        datetime.date(2022, 2, 20),
        datetime.date(2023, 3, 30)
    ]
    
    result_df = get_day_month_year(test_dates)
    
    # Check the shape of the DataFrame
    assert result_df.shape == (3, 3)  # 3 rows and 3 columns
    
    # Check the values in each column
    assert all(result_df['day'] == [10, 20, 30])
    assert all(result_df['month'] == [1, 2, 3])
    assert all(result_df['year'] == [2021, 2022, 2023])