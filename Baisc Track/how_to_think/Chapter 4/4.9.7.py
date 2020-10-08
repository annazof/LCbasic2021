
def sum_to(n):
    """
    Sum to
    :param n: up to which number
    :return: sum
    """
    count=0
    for i in range(n+1):
        count+=i
    return count

print(sum_to(10))