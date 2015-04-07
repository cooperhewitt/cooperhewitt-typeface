from ufo2fdk import OTFCompiler
from ufo2fdk.makeotfParts import MakeOTFPartsCompiler
from robofab.world import OpenFont
from itertools import islice
import sys

family = "CooperHewitt"
weights = ["Thin", "Light", "Book", "Medium", "Semibold", "Bold", "Heavy"]
for w in islice( weights, 0, len(weights)-1 ):
    weights.append(w + "Italic")

for w in weights:
    font = OpenFont("files/{}-{}.ufo".format(family, w))
    compiler = OTFCompiler(savePartsNextToUFO = len(sys.argv)>1 and sys.argv[1] == "debug")
    reports = compiler.compile(font, family + "-" + w + ".otf", checkOutlines=False, autohint=True, releaseMode=True)

    print reports["autohint"]
    print reports["makeotf"]