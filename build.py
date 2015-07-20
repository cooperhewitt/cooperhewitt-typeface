from __future__ import print_function
from ufo2fdk import OTFCompiler
from robofab.world import OpenFont
import sys

family = "CooperHewitt"
weights = ["Thin", "Light", "Book", "Medium", "Semibold", "Bold", "Heavy"]
for w in weights[:]:
    weights.append(w + "Italic")

for w in weights:
    font = OpenFont("files/{}-{}.ufo".format(family, w))
    compiler = OTFCompiler(savePartsNextToUFO = len(sys.argv)>1 and sys.argv[1] == "debug")
    reports = compiler.compile(font, "{}-{}.otf".format(family, w), checkOutlines=False, autohint=True, releaseMode=True)

    print(reports["autohint"])
    print(reports["makeotf"])
