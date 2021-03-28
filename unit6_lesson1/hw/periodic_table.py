"""
Mykyta S.
periodic_table.py
Contains the complete Periodic Table assignment
"""

def recursive_merge_sort(list, compare):
    """Implements a recursive merge sort that returns the sorted list"""

    # If empty or just one element return same list
    if len(list) == 0 or len(list) == 1:
        return list[:]

    # Sort the two halves
    middle = len(list) // 2
    first_half = recursive_merge_sort(list[:middle], compare)
    second_half = recursive_merge_sort(list[middle:], compare)

    # Index the minimum elements in each list
    min_first_half = 0
    min_second_half = 0

    # Merge the elements together in a new list
    sorted = []
    for i in range(len(list)):
        if min_second_half >= len(second_half) or \
                (min_first_half < len(first_half) and
            compare(first_half[min_first_half], second_half[min_second_half])):

            sorted.append(first_half[min_first_half])
            min_first_half += 1
        else:
            sorted.append(second_half[min_second_half])
            min_second_half += 1

    return sorted


class Element:
    """Describes a chemical element with its properties"""

    # Element data as follows:
    # Atomic #, Symbol, Period, Element name, Atomic Mass,
    # Melting Point (?C), Boiling Point (?C), Density (g/cm3)

    def __init__(self, data):
        self.atomicN, self.symbol, self.period, self.name, self.mass, \
        self.melting_p, self.boiling_p, self.density = data

    def __str__(self):
        return "{2} [{0}], #{1} mass={3}"\
            .format(self.symbol, self.atomicN,
                    str.capitalize(self.name), self.mass)

    # Methods to compare various values for sorting
    def compare_atomic_mass(self, other):
        if other.mass == "NoDATA":
            return True
        if self.mass == "NoDATA":
            return False
        return float(self.mass) <= float(other.mass)

    def compare_atomic_number(self, other):
        return int(self.atomicN) <= int(other.atomicN)

    def compare_name(self, other):
        return self.name <= other.name


class PeriodicTable:

    def __init__(self):
        self.elements = list()
        # Read the table data from file
        with open("periodic_table_data.csv") as f:
            first_line = False
            for line in f:
                if not first_line:
                    first_line = True
                    continue
                data = line.replace("\n", "").split(sep=",")
                element = Element(data)
                self.elements.append(element)

    def search_by_atomic_number(self, N):
        if N < 0 or N >= len(self.elements):
            return None
        # Subtract 1 because zero is hydrogen
        return self.elements[N-1]

    def sort_by_atomic_mass(self):
        # Do the merge sort using the compare_atomic_mass() function
        return recursive_merge_sort(self.elements, Element.compare_atomic_mass)

    def sort_in_alphabetical_order(self):
        # Do the merge sort using the compare_name() function
        return recursive_merge_sort(self.elements, Element.compare_name)

    def count_elements_in_period(self, period):
        count = 0
        for e in self.elements:
            if int(e.period) == period:
                count += 1
        return count

    def __str__(self):
        string = ""
        current_period = 1
        period_size = self.count_elements_in_period(current_period)
        column_count = 1
        for e in self.elements:
            if current_period < int(e.period):
                current_period += 1
                period_size = self.count_elements_in_period(current_period)
                string += "\n"
                column_count = 1
            if column_count == 19:
                string += "\n"
            string += e.symbol + " " * (4-len(e.symbol))
            if column_count == 2 and period_size == 8:
                string += " " * (4 * (16 - (period_size - 2)))
            column_count += 1
        return string


if __name__ == "__main__":

    # Test the code
    pt = PeriodicTable()

    # Regular order
    for e in pt.elements[:5]:
        print(e)

    print()

    # Ordered by mass (#19 before #18)
    sorted_by_mass = pt.sort_by_atomic_mass()
    for e in sorted_by_mass[15:20]:
        print(e)

    print()

    # Ordered in alphabetical order
    sorted_alphabetical = pt.sort_in_alphabetical_order()
    for e in sorted_alphabetical[:5]:
        print(e)

    print()

    # Search by an atomic number
    print(pt.search_by_atomic_number(100))
    print(pt.search_by_atomic_number(256))

    print()

    # Print the periodic table
    print(pt)