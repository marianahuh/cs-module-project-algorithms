'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):  # xor/bitwise operator
    result = 0
    # iterate through the arrary
    for i in arr:
        # xor will return 0 for same element and cancel out. otherwise retrun 1
        result ^= i
    return result

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
