import os
import unittest

import pyimaging.io as io
import pyimaging.filter as filter
import pyimaging.visualization as visualization

data_test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data')


class TestFilter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup class method')
        assert os.path.exists(os.path.join(data_test_dir, 'lenna.png'))

    @classmethod
    def tearDownClass(cls):
        print('teardown method')

    def test_sharper_filter(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        filter_image = filter.sharpen(lenna_image)
        self.assertIsNotNone(filter_image,' The filtered image is None')
        visualization.visualize_image('sharpen filter', filter_image)

    def test_shepia_filter(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        filter_image = filter.shepia(lenna_image)
        self.assertIsNotNone(filter_image,' The filtered image is None')
        visualization.visualize_image('shepia filter', filter_image)

    def test_gaussian_blur_filter(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        filter_image = filter.gaussian_blur(lenna_image)
        self.assertIsNotNone(filter_image,' The filtered image is None')
        visualization.visualize_image('gaussian blur filter', filter_image)

    def test_emboss_filter(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        filter_image = filter.emboss(lenna_image)
        self.assertIsNotNone(filter_image,' The filtered image is None')
        visualization.visualize_image('emboss filter', filter_image)
