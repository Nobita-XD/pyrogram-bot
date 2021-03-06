import pathlib
from setuptools import setup
import re
import setuptools
#installing requirements
requirements = ["pyrogram==1.4.16", "py-tgcalls"]

with open("pyrogram_bot/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyrogram_bot",
    version=version,
    description="HELP FOR PyROGRAM",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrAbhiX/pyrogram-bot",
    author="ABHISHEK THAKUR",
    author_email="mrabhixd03ail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
