from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in edu_inv/__init__.py
from edu_inv import __version__ as version

setup(
	name="edu_inv",
	version=version,
	description="Education Fee Invoice",
	author="IT Systematic",
	author_email="yasserelbana@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
