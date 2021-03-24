"""
Mykyta S.
coding_test_q5.py
Answers question 5 - recursive harmonic sequence
"""


def harmonic_sequence_sum(n_terms):
    """Finds the sum of a harmonic sequence 1 + 1/2 + 1/3 + ... to n_terms"""
    if n_terms == 1:
        return 1
    else:
        return (1 / n_terms) + harmonic_sequence_sum(n_terms-1)



if __name__ == "__main__":

    # Test the function
    print(harmonic_sequence_sum(1))
    print(harmonic_sequence_sum(2))
    print(harmonic_sequence_sum(3))
    print(harmonic_sequence_sum(4))

    # Output:
    # 1
    # 1.5
    # 1.833333333333333
    # 2.083333333333333
