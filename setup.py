#!/usr/bin/env python
# encoding: utf-8

# readme
import os
if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = ''

from setuptools import setup, find_packages

setup(name='MatrixScreener',
      version='0.2.1',
      description='Read and stitch ome.tifs from Leica LAS AF MatrixScreener Data exporter',
      author='Arve Seljebu',
      author_email='arve.seljebu@gmail.com',
      license='MIT',
      url='https://github.com/arve0/matrixscreener',
      packages=find_packages(),
      install_requires=['tifffile', 'numpy'],
      long_description=long_description)
