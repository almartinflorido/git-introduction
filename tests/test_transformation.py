import os
import unittest

import pyimaging.io as io
import pyimaging.visualization as visualization
import pyimaging.transformation as transformation

data_test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'data')


class TestTransformation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup class method')
        assert os.path.exists(os.path.join(data_test_dir, 'lenna.png'))

    @classmethod
    def tearDownClass(cls):
        print('teardown method')

    def test_scale_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        original_rows, original_cols, _ = lenna_image.shape
        scaled_lenna = transformation.scale(lenna_image, 1.5, 1.5)
        scaled_rows, scaled_cols, _ = scaled_lenna.shape
        self.assertEqual(scaled_cols, original_cols * 1.5)
        self.assertEqual(scaled_rows, original_rows * 1.5)
        # visualization.visualize_image('lenna', lenna_image, wait=False)
        # visualization.visualize_image('scaled lenna', scaled_lenna, wait=True)

    def test_translate_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        translated_lenna = transformation.translation(lenna_image, 100, 50)
        # visualization.visualize_image('translated lenna', translated_lenna, wait=True)

    def test_rotate_image(self):
        lenna_image = io.load_image(os.path.join(data_test_dir, 'lenna.png'))
        self.assertIsNotNone(lenna_image,' The image is None')
        rotated_lenna = transformation.rotation(lenna_image, 90)
        # visualization.visualize_image('rotated lenna', rotated_lenna, wait=True)
        