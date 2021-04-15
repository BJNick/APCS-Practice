"""
Mykyta S.
stocks_exam.py
Contains classes StockIndex and StockIndices for the CS30 OOP test
"""


def recursive_merge_sort(unsorted_list, compare):
    """Implements a recursive merge sort that returns the sorted list"""

    # If empty or just one element return same list
    if len(unsorted_list) == 0 or len(unsorted_list) == 1:
        return unsorted_list[:]

    # Sort the two halves
    middle = len(unsorted_list) // 2
    first_half = recursive_merge_sort(unsorted_list[:middle], compare)
    second_half = recursive_merge_sort(unsorted_list[middle:], compare)

    # Index the minimum elements in each list
    min_first_half = 0
    min_second_half = 0

    # Merge the elements together in a new list
    sorted_list = []
    for i in range(len(unsorted_list)):
        if min_second_half >= len(second_half) or \
                (min_first_half < len(first_half) and
                 compare(first_half[min_first_half],
                         second_half[min_second_half])):

            sorted_list.append(first_half[min_first_half])
            min_first_half += 1
        else:
            sorted_list.append(second_half[min_second_half])
            min_second_half += 1

    return sorted_list


class StockIndex:

    # Initialize the variables, convert to float
    def __init__(self, index_name, index_level, etf_name, etf_price, country):
        self.index_name = index_name
        self.index_level = float(index_level)
        self.etf_name = etf_name
        self.etf_price = float(etf_price)
        self.country = country

    # Converts all variables to str
    def __str__(self):
        return f"""
Index Name: {self.index_name}
Index Level: {self.index_level}
ETF Name: {self.etf_name}
ETF Price: {self.etf_price}
Index Country: {self.country}""".strip()


class StockIndices:

    # Loads the table from the file
    def __init__(self, filename):
        self.stock_list = []

        with open(filename) as file:
            for index, line in enumerate(file):
                # Skip the first line
                if index == 0:
                    continue
                # Append each data entry to the list
                data = line.split(",")
                self.stock_list.append(StockIndex(*data))

    # Sorts the list by the index name
    def sort_by_index_name(self):
        self.stock_list = recursive_merge_sort(self.stock_list,
                                   lambda a, b: a.index_name <= b.index_name)

    # Searches the list for the needed stock
    def search_by_index_name(self, index_name):
        for stock in self.stock_list:
            if stock.index_name == index_name:
                return stock
        return None

    # Finds the average ETF price
    def calculate_etf_avg(self):
        total = 0
        for stock in self.stock_list:
            total += stock.etf_price
        return total / len(self.stock_list)

    # Prints each stock in the list (just the Index Name)
    def __str__(self):
        string = ""
        for s in self.stock_list:
            string += s.index_name + ", "
        return string.removesuffix(", ")


if __name__ == "__main__":
    # Tests the program
    stock_db = StockIndices("indexdata.csv")

    print("Unsorted List: ", stock_db)

    stock_db.sort_by_index_name()

    print("Sorted list: ", stock_db)

    print()

    print("ETF Price Average:", stock_db.calculate_etf_avg())

    print()

    print(stock_db.search_by_index_name("SPX"))
