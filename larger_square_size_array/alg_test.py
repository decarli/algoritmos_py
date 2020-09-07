import unittest
from larger_square_size_array import alg_v1

class TestarCoun(unittest.TestCase):
    def test(self):
        for case in use_cases:
            total = alg_v1.count(case["values"])
            self.assertEqual(case["total"], total)


if __name__ == '__main__':
    unittest.main()

use_cases = [
    {
    "total": 1,
    "values":
        [
            [1,0,0],
            [1,0,0],
            [1,1,0]
        ]
    },
    {
    "total": 2,
    "values":
        [
            [1,0,0],
            [1,1,0],
            [1,1,0]
        ]
    },
    {"total": 2,
    "values":
        [
            [1,1,1],
            [1,1,0],
            [1,1,0]
        ]
    },
    {"total": 3,
    "values":
        [
            [1,1,1],
            [1,1,1],
            [1,1,1]
        ]
     },
    {"total": 2,
    "values":
        [
            [0,0,0],
            [0,1,1],
            [0,1,1]
        ]
    },
    {"total": 2,
    "values":
        [
            [0,1,1],
            [0,1,1],
            [0,1,0]
        ]
    },
    {"total": 4,
    "values":
        [
            [0,1,1,0,1,1],
            [0,1,1,1,1,1],
            [0,1,1,1,1,1],
            [0,1,1,1,1,1],
            [0,1,1,1,1,1],
            [0,1,1,1,1,0]
        ]
    }

]