import setuptools

setuptools.setup(
    name='lmj.perceptron',
    version='0.1',
    namespace_packages=['lmj'],
    packages=setuptools.find_packages(),
    ext_modules=[setuptools.Extension('lmj.pursuit._correlate', sources=['lmj/pursuit/correlate.c'])],
    author='Leif Johnson',
    author_email='leif@leifjohnson.net',
    description='A library of perceptron implementations ',
    long_description=open('README.md').read(),
    license='MIT',
    keywords=('perceptron '
              'averaged-perceptron '
              'machine-learning'),
    url='http://github.com/lmjohns3/py-perceptron',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
    )
