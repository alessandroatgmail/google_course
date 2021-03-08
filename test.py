import unittest
import os
from image_proc import process_imgs

class TestProcessImgs(unittest.TestCase):

    def test_init(self):
        source_dir = "img"
        dest_dir = "new_dir"
        pi = process_imgs(source_dir=source_dir, dest_dir=dest_dir)
        self.assertEqual(pi.status,-1)
        source_dir = "images"
        pi = process_imgs(source_dir=source_dir, dest_dir=dest_dir)
        self.assertEqual(pi.status,0)


if __name__ == '__main__':
    unittest.main()
