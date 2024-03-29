from setuptools import setup, find_packages
import sys, os, io

# List all of your Python package dependencies in the
# requirements.txt file

def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\\n")
        return stream.read()

readme = readfile("README.rst", split=True)[3:]  # skip title
# For requirements not hosted on PyPi place listings
# into the 'requirements.txt' file.
#requires = readfile("requirements.txt")
requires = [
    # minimal requirements listing
    "opencmiss.zinc >= 3.3",  # not yet on pypi - need manual install from opencmiss.org
    "opencmiss.zincwidgets >= 2.0.3"
]
license = readfile("LICENSE")

setup(
    name=u'mapclientplugins.smoothfitstep',
    version='0.1.0',
    description='',
    long_description='\n'.join(readme) + license,
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Programming Language :: Python",
    ],
    author=u'Richard Christie',
    author_email='',
    url='',
    license='GPL',
    packages=find_packages(exclude=['ez_setup',]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    )
