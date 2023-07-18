# Stock Statistics Calculator

This script, `calculate_stock_statistics.py`, is a Python program that calculates various statistics related to the stock market. It reads data from two CSV files containing stock market information and computes the covariance, correlation, and variance for the provided closing price fields of two stocks.

## Requirements

- Python 3.x
- CSV files containing historical stock market data
- The `csv` module (included in Python standard library)
- The `statistics` module (included in Python standard library)

## Usage

```python
python calculate_stock_statistics.py
```

## Function Explanation

### calculate_stock_statistics(file1, file2, closing_price_fieldname1, closing_price_fieldname2)

This function takes four arguments:

- `file1`: The path to the first CSV file containing historical stock market data for stock 1.
- `file2`: The path to the second CSV file containing historical stock market data for stock 2.
- `closing_price_fieldname1`: The field name in `file1` representing the closing prices of stock 1.
- `closing_price_fieldname2`: The field name in `file2` representing the closing prices of stock 2.

It calculates the following statistics:

1. Covariance between the daily returns of the two stocks.
2. Correlation between the daily returns of the two stocks.
3. Variance of the daily returns for each stock.

## How the Function Works

1. The function `calculate_stock_statistics` first defines a nested function `variance(csv_file, closing_price_fieldname)` to calculate the variance of daily returns for a given CSV file and closing price field name.

2. The function opens both CSV files and reads them using the `csv.DictReader` to parse the data.

3. It calculates the daily returns for each stock by computing the percentage change between consecutive closing prices.

4. The daily returns are stored in separate lists (`returns_lis_1` and `returns_lis_2`) for each stock.

5. The function computes the covariance and correlation between the two sets of daily returns (`returns_lis_1` and `returns_lis_2`) using the `statistics.covariance` and `statistics.correlation` functions, respectively.

6. To calculate the variance of each stock, the function calls the nested `variance` function twice, once for each stock.

7. The calculated statistics are then returned as a dictionary with the following keys:
   - `"covariance"`: The covariance between the daily returns of stock 1 and stock 2.
   - `"correlation"`: The correlation between the daily returns of stock 1 and stock 2.
   - `"variance"`: A dictionary containing the variance of each stock with keys `"stock_1"` and `"stock_2"`.

## Example Usage

```python
covariance_and_variance = calculate_stock_statistics(
    "NIFTY 50-18-07-2022-to-18-07-2023.csv",
    "NIFTY BANK-18-07-2022-to-18-07-2023.csv",
    "Close ",
    "Close "
)

print(covariance_and_variance)
```

## Note

- Ensure that the provided CSV files are correctly formatted with the closing price field matching the specified field names (`closing_price_fieldname1` and `closing_price_fieldname2`).

- In case of insufficient data points (less than 2), the function raises a `ValueError` with the message "Insufficient data points to calculate variance."

- The function returns the covariance as well as the variance multiplied by 100 to represent percentages.
