import os
from pathlib import Path


ROOT = Path(__file__).parent
for file in os.listdir(ROOT):
    if file.startswith("input-"):
        print(file)
        with ROOT.joinpath(file).open("r") as reader:
            print(reader.read())
