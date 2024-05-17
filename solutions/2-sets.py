m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_numbers = sum(len(array) for array in m)

total_sum = sum(sum(array) for array in m)

average_number = total_sum / total_numbers

merged_array = tuple(set.union(*m))
