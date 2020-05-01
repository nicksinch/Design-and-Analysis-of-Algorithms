# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

# Given a number n, the task is to find n’th Ugly number.

# Efficinet approach using dynamic programming resulting in O(N) time complexity
# and O(N) space

def find_nth_ugly_number(n):
    ugly = n * [0]
    ugly[0] = 1

    idx_two = idx_three = idx_five = 0

    next_multiple_of_two = 2
    next_multiple_of_three = 3
    next_multiple_of_five = 5

    for i in range(1, n):
        ugly[i] = min(next_multiple_of_two,
                        next_multiple_of_three,
                        next_multiple_of_five)

        if ugly[i] == next_multiple_of_two:
            idx_two += 1
            next_multiple_of_two = ugly[idx_two] * 2
        if ugly[i] == next_multiple_of_three:
            idx_three += 1
            next_multiple_of_two = ugly[idx_three] * 3
        if ugly[i] == next_multiple_of_five:
            idx_five += 1
            next_multiple_of_five = ugly[idx_five] * 5

    return ugly[-1]


print(find_nth_ugly_number(10))



