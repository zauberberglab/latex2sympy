from setuptools import setup, find_packages

setup(
    name="latex2sympy2",
    version="1.5.0",
    description='Convert latex to sympy with ANTLR and support Matrix, Linear Algebra and CAS function.',
    packages=find_packages(exclude=('tests')),
    py_modules=['asciimath_printer', 'latex2sympy2'],
    install_requires=[
        'sympy==1.4',
        'antlr4-python3-runtime>=4.7.2'
    ],
    # The project's main homepage.
    url='opconty - Overview',
    # Author details
    author='gaolijun',
    author_email='gao.gzhou@gmail.com',
    # Choose your license
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    py_modules=["nicelogger"],
    install_requires=['colorama']
)
