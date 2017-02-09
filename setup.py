from setuptools import setup
from setuptools import find_packages


setup(name='cleverhans',
      version='1.0.1',
      description='A library for benchmarking vulnerability to adversarial examples',
      author='Nicolas Papernot, Ian Goodfellow',
      author_email='cleverhans-dev@googlegroups.com',
      url='https://github.com/openai/cleverhans',
      license='MIT',
      install_requires=['keras', 'numpy', 'tensorflow'],
      extras_require={
        'tensorflow_gpu': ['tensorflow_gpu'],
      },
      packages=['cleverhans', 'tutorials'])
