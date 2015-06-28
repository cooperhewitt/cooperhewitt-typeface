from ufo2fdk import OTFCompiler
from ufo2fdk.makeotfParts import MakeOTFPartsCompiler
from robofab.world import OpenFont
import sys

family = "CooperHewitt"
weights = ["Thin", "Light", "Book", "Medium", "Semibold", "Bold", "Heavy"]
for w in weights[0:]:
    weights.append(w + "Italic")

for w in weights:
    font = OpenFont("files/{}-{}.ufo".format(family, w))
    compiler = OTFCompiler(savePartsNextToUFO = len(sys.argv)>1 and sys.argv[1] == "debug")
    reports = compiler.compile(font, family + "-" + w + ".otf", checkOutlines=False, autohint=True, releaseMode=True)

    print reports["autohint"]
    print reports["makeotf"]