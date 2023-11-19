# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны спискa
def numb_counter(numb):
    res = []
    length = len(numb)
    for i in range(length):
        left_index = (i - 1 + length) % length
        right_index = (i + 1) % length
        index_sum = numb[left_index] + numb[right_index]
        res.append(index_sum)

    return res


numb_list = [1, 21, 412, 5, 12, 566]
print(numb_list)
print(numb_counter(numb_list))
