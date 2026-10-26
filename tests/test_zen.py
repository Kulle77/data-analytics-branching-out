# pylint: disable-all
import unittest

ZEN_TEXT = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

with open("zen.txt", "r") as f:
    zen = f.read().strip()

class TestZen(unittest.TestCase):
    def test_zen_txt_has_02_or_more_lines(self):
        self.assertGreaterEqual(len(zen.splitlines()), 2)

    def test_zen_txt_has_16_or_more_lines(self):
        self.assertGreaterEqual(len(zen.splitlines()), 16)

    def test_zen_txt_has_all_lines(self):
        self.assertEqual(len(zen.splitlines()), len(ZEN_TEXT.splitlines()))

    def test_zen_txt_matches_original(self):
        # Strip leading/trailing whitespace from each line before comparison
        zen_lines = [line.strip() for line in ZEN_TEXT.splitlines()]
        content_lines = [line.strip() for line in zen.splitlines()]
        self.assertEqual(content_lines, zen_lines)
