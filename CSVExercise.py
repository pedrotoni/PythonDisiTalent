import csv
from operator import itemgetter


def top_10_revenue(csv_path):
    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        # skips the first line in csv
        next(csv_reader)
        product_revenue_dict = {}
        for line in csv_reader:
            product_revenue_dict[line['NAME']] = float(line['REVENUE'])
        # key=itemgetter(1) gets the second element of each tuple (revenue),
        # and then we sort the dictionary by the revenue values.
        sorted_dict = sorted(product_revenue_dict.items(), key=itemgetter(1), reverse=True)
        top10_revenue_dict = dict(sorted_dict[:-9])
        return top10_revenue_dict


def top_10_units_sold(csv_path):
    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        next(csv_reader)
        product_units_sold_dict = {}
        for line in csv_reader:
            product_units_sold_dict[line['NAME']] = int(line['UNITS_SOLD'])
        sorted_dict = sorted(product_units_sold_dict.items(), key=itemgetter(1), reverse=True)
        top_10_units_sold_dict = dict(sorted_dict[:-9])
        return top_10_units_sold_dict


def revenue_units_sold_per_category(csv_path):
    with open(csv_path, "r") as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        next(csv_reader)
        total_units_bakery, total_units_dairy, total_units_produce = 0, 0, 0
        total_revenue_bakery, total_revenue_dairy, total_revenue_produce = 0, 0, 0

        for line in csv_reader:
            if line['CATEGORY'] == 'DAIRY':
                total_units_dairy += int(line['UNITS_SOLD'])
                total_revenue_dairy += float(line['REVENUE'])
            elif line['CATEGORY'] == 'PRODUCE':
                total_units_produce += int(line['UNITS_SOLD'])
                total_revenue_produce += float(line['REVENUE'])
            else:
                total_units_bakery += int(line['UNITS_SOLD'])
                total_revenue_bakery += float(line['REVENUE'])

        data_per_category = {'Bakery': [total_revenue_bakery, total_units_bakery],
                             'Dairy': [total_revenue_dairy, total_units_dairy],
                             'Produce': [total_revenue_produce, total_units_produce]}

    return data_per_category


top_10_revenue = top_10_revenue("sales_data.csv")
top_10_units_sold = top_10_units_sold("sales_data.csv")

revenueRank = 1
print("TOP 10 PRODUCTS BY REVENUE")
for product_name, revenue in top_10_revenue.items():
    print(f"{revenueRank}.{product_name} - REVENUE: ${revenue:.2f}")
    revenueRank += 1
print("------------------------------")

unitsSoldRank = 1
print("TOP 10 PRODUCTS BY UNITS SOLD")
for product_name, units_sold in top_10_units_sold.items():
    print(f"{unitsSoldRank}.{product_name} - UNITS SOLD: {units_sold}")
    unitsSoldRank += 1
print("------------------------------")

data_per_category = revenue_units_sold_per_category("sales_data.csv")
for key, value in data_per_category.items():
    print(f"Category: {key} | Revenue: ${value[0]:.2f} | Units Sold: {value[1]}")
