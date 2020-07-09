import unittest
import random

from srchalgo import srchs


class TestBase(unittest.TestCase):
    # --- 탐색 리스트 기본 설정 ---
    min_val = 1
    max_val = 1_000_000
    # ------

    # 검색 대상
    tgtarr = None
    # 검색 값
    srchval = None
    # 검색 값의 인덱스
    ansidx = None

    @classmethod
    def setUpClass(cls):
        # 검색 대상 설정
        TestBase.tgtarr \
            = tuple(i for i in range(TestBase.min_val, TestBase.max_val + 1))
        # 검색 값 설정
        TestBase.srchval = random.randint(TestBase.min_val, TestBase.max_val)
        # 검색 값의 인덱스
        TestBase.ansidx = TestBase.tgtarr.index(TestBase.srchval)

    def test_linear_search(self):
        fn = srchs.linear_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_iterative_binary_search(self):
        fn = srchs.iterative_binary_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_recursive_binary_search(self):
        fn = srchs.recursive_binary_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_jump_search(self):
        fn = srchs.jump_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_interpolation_search(self):
        fn = srchs.interpolation_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_exponential_search(self):
        fn = srchs.exponential_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)

    def test_fibonacci_search(self):
        fn = srchs.fibonacci_search

        chkidx = fn(TestBase.tgtarr, TestBase.srchval)
        self.assertEqual(chkidx, TestBase.ansidx)
        chkidx = fn(TestBase.tgtarr, TestBase.max_val + 1)
        self.assertEqual(chkidx, -1)


if __name__ == "__main__":
    unittest.main()
