import re
import sys

from bs4 import BeautifulSoup
from markdown import markdown
from setuptools import setup

sys.setrecursionlimit(2000)

VERSION = re.compile("[^0-9.]").sub(
    "",
    (
        BeautifulSoup(markdown(open("changelog.md", "r").read()), "html.parser")
        .find_all(string=re.compile("v[.0-9]+"))[0]
        .split()[0]
    ),
)
with open("resources/VERSION", "w") as f:
    f.write(VERSION)


APP = ["wb_gui.py"]
DATA_FILES = [
    "src",
    "resources",
    "resources/params.json",
    "resources/VERSION",
    "resources/wb_logo.icns",
]
OPTIONS = {
    "includes": [
        "PySimpleGUI",
        "numpy",
    ],
    "excludes": [
        "*.csv",
        "csv_stats.py",
        "*.gif",
    ],
    "iconfile": "/Users/GFahmy/Documents/projects/weight_and_balance/resources/wb_logo.icns",
    "arch": "universal2",
}

setup(
    app=APP,
    version=VERSION,
    data_files=DATA_FILES,
    name="Weight And Balance",
    options={"py2app": OPTIONS},
    author="George Fahmy",
    description="WeightAndBalance",
    python_requires=">=3.12",
    long_description="""The WeightAndBalance app allows you to calculate and visual the
    weight and balance of your airplane.""",
)
