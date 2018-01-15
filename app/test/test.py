"""This is a test module where several methods are defined"""
# magic methods
__name__ = "Test"
__revision__ = "1.2.1"
__func__ = "test_enumerator()"









NUM_LIST = [1, 2, 8, 79]
rv = "Length of num list: {} ".format(len(NUM_LIST))
# print(rv)

def test_enumerator(numbr_list):
    """Test enumerate"""
    for i, item in enumerate(numbr_list):
        print("index " + str(i) + " item " + str(item))

def test_range():
    """Test range"""
    for item_x in range(6):
        print(item_x)

def test_zip():
    """test zip"""
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    for item_x in zipped:
        print(item_x)
        print(item_x[0])

def check_greeting(data_in):
    rv = ""
    input_hi = ["hi", "hello", "good day", "greetings", "how"]
    for x in input_hi:
        if x == data_in.lower():
            rv = "yes"
    return rv

print(check_greeting("hi"))
# test_zip()

# y = "128"
# print(type(y))
# x = int(y)
# print(type(x))
# test_zip()
# test_range()
# test_enumerator(NUM_LIST)
