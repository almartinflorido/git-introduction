from setuptools import setup, find_packages
import sys, os.path


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("./requirements.txt")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyimaging'))
import pyimaging
setup(name='pyimaging',
      version= pyimaging.__version__,
      install_requires=[install_reqs],
      description='A module to manage images.',
      url='https://github.com/almartinflorido/git-introduction',
      author='developers',
      python_requires='>=3.6,<4',
      packages = find_packages(exclude=("test"))
)