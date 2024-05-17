a = [[1, 2, 3], [4, 5, 6]]

dict_list = [
    dict((f"k{key+1}", value) for key, value in enumerate(values))
    for values in a
]
