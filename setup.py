from setuptools import setup

setup(
	name="latex2sympy",
	packages=['gen'],
	py_modules=['asciimath_printer', 'latex2sympy'],
	install_requires=[
		'sympy==1.4',
		'antlr4-python3-runtime>=4.7.2'
	]
)