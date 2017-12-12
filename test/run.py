li = [1, 2, 8, 79]
it = iter(li)
# print(it)



def test_unpacking(a_list):
    iterator = iter(a_list)
    a, b, c, d = iterator
    print(" {} {} {} {} ".format(a, b, c, d))

def test_enumerator(li):
    for i, item in enumerate(li):
        print("index " + str(i) + " item " + str(item))

def test_iterator(a_iter): 
    """___"""
    try:
        print(a_iter.__next__())
        print(a_iter.__next__())
        print(a_iter.__next__())
    except StopIteration:
        print("No more elements! ")
    except AttributeError:
        print("Object has no attribute __next__ ")

test_unpacking(li)
# test_enumerator(li)
# test_iterator(it)
# test_iterator(li)




   
