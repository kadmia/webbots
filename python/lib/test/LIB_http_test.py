import sys
sys.path.append("..")

import unittest
from LIB_http import *

class TestLib_http(unittest.TestCase):

  def setUp(self):
    pass

  def test_get_http(self):
    response = http_get('http://google.com')
    self.assertTrue(response['status'], 302)


if __name__ == '__main__':
      unittest.main()
