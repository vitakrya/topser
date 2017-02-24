from unittest import TestCase

import topser


class TestPont(TestCase):
    def test_is_string(self):
        s = topser.pont()
        self.assertTrue(isinstance(s, str))