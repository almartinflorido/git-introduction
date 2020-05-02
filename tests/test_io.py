import os
import unittest
import tempfile

import pyimaging.io as io

data_test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data')


class TestIO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup class method')
        assert os.path.exists(os.path.join(data_test_dir, 'lenna.png'))

    @classmethod
    def tearDownClass(cls):
        print('teardown method')

    def test_io_read_color_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        self.assertTrue(len(lenna_image.shape) == 3, 'The image doesnt have dimensions')
        self.assertTrue(lenna_image.shape[2] == 3, 'The image is not a color image')

    def test_io_read_grayscale_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'), color=False)
        self.assertIsNotNone(lenna_image, ' The image is None')
        self.assertTrue(len(lenna_image.shape) == 2, 'The image have dimension')

    def test_io_write_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        temp_file = tempfile.NamedTemporaryFile().name + '.png'
        io.write_image(temp_file, lenna_image)
        self.assertTrue(os.path.exists(temp_file))
        temp_lenna_image =io.load_image(temp_file)
        self.assertIsNotNone(temp_lenna_image,' The image is None')
        self.assertTrue(len(temp_lenna_image.shape) == 3, 'The image doesnt have dimensions')
        self.assertTrue(temp_lenna_image.shape[2] == 3, 'The image is not a color image')