from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='vega-mysql',
    version='0.1.0',
    author='jinland',
    author_email='jinland@bommaru.com',
    description='Library for using MySQL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jinland-bommaru/mysql.git',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.10',
    install_requires=[
        'PyMySQL >= 1.0.2',
        'sshtunnel >= 0.4.0',
    ],
    package_data={"vega_mysql": ["*.txt"]},
    include_package_data=True,
)