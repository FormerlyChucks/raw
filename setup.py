from setuptools import setup

setup(name='raw',
      version='0.0.6',
      description='Ruqqus API Wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/ithinkimokay/raw',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      packages=['raw'],
      zip_safe=False,
      keywords='Ruqqus API RAW',
      install_requires=['requests'],
      include_package_data=True
      )
