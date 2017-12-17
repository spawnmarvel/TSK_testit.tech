"""This is a test module where several methods are defined"""
# magic methods
__name__ = "Test"
__revision__ = "1.2.1"
__func__ = "test_enumerator()"



li = [1, 2, 8, 79]


def test_enumerator(li):
    
    for i, item in enumerate(li):
        print("index " + str(i) + " item " + str(item))

# test_enumerator(li)



   
