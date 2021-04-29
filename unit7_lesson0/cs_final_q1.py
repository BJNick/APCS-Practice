"""
Mykyta S.
cs_final_q1.py
Contains the data model for the real estate agency
"""


def selection_sort(properties):
    """Sorts the provided list by price using selection sort"""
    for sorted_length in range(len(properties) - 1):
        # Find min number
        min_index = sorted_length
        for i in range(sorted_length, len(properties)):
            if properties[min_index].price > properties[i].price:
                min_index = i
        # Swap it
        properties[sorted_length], properties[min_index] = \
            properties[min_index], properties[sorted_length]


class MLSProperty:

    # Initializes the variables for the property
    def __init__(self, address, price, customer_name, phone_number):
        self.address = address
        self.price = float(price)
        self.customer_name = customer_name
        self.phone_number = phone_number

    # Calculates the commission based on price
    def MyCommission(self):
        if self.price > 400000:
            total_commission = 0.03 * 400000 + 0.05 * (self.price - 400000)
        else:
            total_commission = 0.03 * self.price
        return total_commission

    # Formats all the variables in a string
    def __str__(self):
        return \
            f"""Address: {self.address}
List price: {self.price}
Customer name: {self.customer_name}
Customer phone: {self.phone_number}
Commission: {self.MyCommission()}\n"""


class MLSProperties:

    # Load data from file
    def __init__(self):
        self.properties = list()
        # Read the property data from file
        with open("mylistings.csv") as f:
            first_line = False
            for line in f:
                if not first_line:
                    first_line = True
                    continue
                data = line.replace("\n", "").split(sep=",")
                element = MLSProperty(*data)
                self.properties.append(element)

    # Search the list by customer name using linear search
    def search_by_customer_name(self, name):
        for p in self.properties:
            if p.customer_name == name:
                return p
        return None

    # Sorts the list by price using selection sort
    def sort_by_price(self):
        selection_sort(self.properties)

    # Print all list elements (shortened version)
    def __str__(self):
        string = ""
        for p in self.properties:
            string += f"{p.address} | {p.price} | " \
                      f"{p.customer_name} | {p.phone_number}"
            string += "\n"
        return string


if __name__ == "__main__":
    # Tests the methods of the class
    agency = MLSProperties()

    print("Sorted:\n")
    agency.sort_by_price()
    print(agency)

    print("Search for \"Ben Yee\":\n")
    found_property = agency.search_by_customer_name("Ben Yee")
    print(found_property)
