def all_elements_true(tup):
    return all(tup)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
print("Are all elements of tuple1 true?", all_elements_true(tuple1))
print("Are all elements of tuple2 true?", all_elements_true(tuple2))