import unittest
from math import isclose
from unittest.mock import patch, mock_open

from shadow.polyedr import Polyedr


class TestCharacteristic(unittest.TestCase):

    def test_fully_visible(self):
        content = """\
1.0\t0.0\t0.0\t0.0
8\t2\t8
-5.0\t-5.0\t0.0
5.0\t-5.0\t0.0
5.0\t5.0\t0.0
-5.0\t5.0\t0.0
2.0\t0.0\t1.0
3.0\t0.0\t1.0
3.0\t1.0\t1.0
2.0\t1.0\t1.0
4\t1    2    3    4
4\t5    6    7    8"""
        with patch('shadow.polyedr.open',
                   new=mock_open(read_data=content)):
            p = Polyedr('test')
        self.assertTrue(isclose(p.characteristic(), 0.0))

    def test_fully_invisible(self):
        content = """\
1.0\t0.0\t0.0\t0.0
8\t2\t8
-5.0\t-5.0\t0.0
5.0\t-5.0\t0.0
5.0\t5.0\t0.0
-5.0\t5.0\t0.0
2.0\t0.0\t-1.0
3.0\t0.0\t-1.0
3.0\t1.0\t-1.0
2.0\t1.0\t-1.0
4\t1    2    3    4
4\t5    6    7    8"""
        with patch('shadow.polyedr.open',
                   new=mock_open(read_data=content)):
            p = Polyedr('test')
        self.assertTrue(isclose(p.characteristic(), 0.0))

    def test_steep_angle(self):
        content = """\
1.0\t0.0\t0.0\t0.0
8\t2\t8
-5.0\t-5.0\t0.0
5.0\t-5.0\t0.0
5.0\t5.0\t0.0
-5.0\t5.0\t0.0
2.0\t0.0\t-1.0
2.0\t0.01\t-5.0
2.0\t1.0\t-5.0
2.0\t1.0\t-1.0
4\t1    2    3    4
4\t5    6    7    8"""
        with patch('shadow.polyedr.open',
                   new=mock_open(read_data=content)):
            p = Polyedr('test')
        self.assertTrue(isclose(p.characteristic(), 0.0))

    def test_far_from_line(self):
        content = """\
1.0\t0.0\t0.0\t0.0
8\t2\t8
8.0\t-5.0\t0.0
12.0\t-5.0\t0.0
12.0\t5.0\t0.0
8.0\t5.0\t0.0
7.0\t-0.5\t-0.01
13.0\t-0.5\t-0.01
13.0\t0.5\t-0.01
7.0\t0.5\t-0.01
4\t1    2    3    4
4\t5    6    7    8"""
        with patch('shadow.polyedr.open',
                   new=mock_open(read_data=content)):
            p = Polyedr('test')
        self.assertTrue(isclose(p.characteristic(), 0.0))

    def test_positive(self):
        content = """\
1.0\t0.0\t0.0\t0.0
8\t2\t8
-5.0\t-5.0\t0.0
5.0\t-5.0\t0.0
5.0\t5.0\t0.0
-5.0\t5.0\t0.0
-1.0\t-0.5\t-0.01
7.0\t-0.5\t-0.01
7.0\t0.5\t-0.01
-1.0\t0.5\t-0.01
4\t1    2    3    4
4\t5    6    7    8"""
        with patch('shadow.polyedr.open',
                   new=mock_open(read_data=content)):
            p = Polyedr('test')
        self.assertTrue(isclose(p.characteristic(), 12.0, abs_tol=1e-6))
