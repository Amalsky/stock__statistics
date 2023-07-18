import csv
import statistics



   

def calculate_stock_statistics(file1,file2,closing_price_fieldname1,closing_price_fieldname2):
    copy_1 = file1
    copy_2 = file2
    
    def variance(csv_file, closing_price_fieldname):
         with open(csv_file) as csv_file:
            file = csv.DictReader(csv_file)
            closing_price_lis = []
            returns_lis = []
            for index, line in enumerate(file):
                if "," in line[closing_price_fieldname1]:
                    line = line[closing_price_fieldname].replace(",", "")
                else:
                    line = line[closing_price_fieldname]    
                previous_closing_price = line
                closing_price_lis.append(float(previous_closing_price))

                if index >= 1:
                    daily_returns = (float(line) / closing_price_lis[index - 1]) - 1
                    returns_lis.append(float(daily_returns))

            if len(returns_lis) < 2:
                raise ValueError("Insufficient data points to calculate variance")
            variance_value = statistics.variance(returns_lis)
            variance_decimal = format(variance_value, 'f')
            return float(variance_decimal) * 100


    closing_price_lis_1 = []
    returns_lis_1 = []
    closing_price_lis_2 = []
    returns_lis_2 = []
    with open(file1) as file1, open(file2) as file2:
        file_1 = csv.DictReader(file1)
        file_2 = csv.DictReader(file2)
        
        for index, line in enumerate(file_1):
            if "," in line[closing_price_fieldname1]:
                line = line[closing_price_fieldname1].replace(",", "")
            else:
                line = line[closing_price_fieldname1]    
            previous_closing_price = line
            closing_price_lis_1.append(float(previous_closing_price))

            if index >= 1:
                daily_returns = (float(line) / closing_price_lis_1[index - 1]) - 1
                returns_lis_1.append(float(daily_returns))
                
        for index, line in enumerate(file_2):
            if "," in line[closing_price_fieldname1]:
                line = line[closing_price_fieldname2].replace(",", "")
            else:
                line = line[closing_price_fieldname2] 
            if len(closing_price_lis_2) == len(closing_price_lis_1):
                break
            previous_closing_price = line
            closing_price_lis_2.append(float(previous_closing_price))

            if index >= 1:
                daily_returns = (float(line) / closing_price_lis_2[index - 1]) - 1
                returns_lis_2.append(float(daily_returns))
        covariance =statistics.covariance(returns_lis_1, returns_lis_2) 
        correlation = statistics.correlation(returns_lis_1, returns_lis_2)
        stock_1_variance = variance(copy_1,closing_price_fieldname1)  
        stock_2_variance = variance(copy_2,closing_price_fieldname2)  
    return {"covariance":covariance, "correlation":correlation, "variance":{"stock_1":stock_1_variance, "stock_2":stock_2_variance}}           
           
