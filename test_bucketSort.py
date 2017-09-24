from bucketSort import Solution

def test_basic():

    test1_arr = [0.3432, 0.1233, 0.9884, 0.231, 0.564, 0.7843]
    test1_result = Solution().bucketSort(test1_arr)
    assert(test1_result == [0.1233, 0.231, 0.3432, 0.564, 0.7843, 0.9884])
    print('test_basic passed! result is ', test1_result)

if __name__ == '__main__':
    test_basic()