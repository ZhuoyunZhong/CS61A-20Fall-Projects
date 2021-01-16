test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> piggy_points(0)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(1)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(2)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(3)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(13)
          10
          >>> # ban indexing
          >>> test.check('hog.py', 'piggy_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          >>> # check pi is not changed
          >>> FIRST_101_DIGITS_OF_PI == 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(44)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(37)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(40)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(24)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(46)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(99)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(10)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(47)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(67)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(92)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(9)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(25)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(75)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(82)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(88)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(41)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(42)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(93)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(99)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(73)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(83)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(34)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(4)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(53)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(19)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(1)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(85)
          3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
