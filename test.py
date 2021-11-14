#!/usr/bin/env python3
"""Test fhprint
"""
from __future__ import annotations

import sys
from io import StringIO
from pathlib import Path

from ansitoimg.render import ansiToSVG

result = StringIO()
oldStdout = sys.stdout
sys.stdout = result
THISDIR = str(Path(__file__).resolve().parent)

from fhprint import (
	LogCode,
	Logger,
	colorlogPrint,
	fhnfPrint,
	fhPrint,
	lamuPrint,
	metPrint,
	printtagsPrint,
	pythonPrint,
	xaPrint,
)

print("#########################")
print("#      Meterpreter      #")
print("#########################")
metPrint("none")
metPrint("heading", ll=LogCode.HEADING)
metPrint("debug", ll=LogCode.DEBUG)
metPrint("info", ll=LogCode.INFO)
metPrint("success", ll=LogCode.OK)
metPrint("warning", ll=LogCode.WARNING)
metPrint("error", ll=LogCode.ERROR)
metPrint("critical", ll=LogCode.CRITICAL)


print("#########################")
print("#          FH           #")
print("#########################")
fhPrint("none")
fhPrint("heading", ll=LogCode.HEADING)
fhPrint("debug", ll=LogCode.DEBUG)
fhPrint("info", ll=LogCode.INFO)
fhPrint("success", ll=LogCode.OK)
fhPrint("warning", ll=LogCode.WARNING)
fhPrint("error", ll=LogCode.ERROR)
fhPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#         FHNF          #")
print("#########################")
fhnfPrint("none")
fhnfPrint("heading", ll=LogCode.HEADING)
fhnfPrint("debug", ll=LogCode.DEBUG)
fhnfPrint("info", ll=LogCode.INFO)
fhnfPrint("success", ll=LogCode.OK)
fhnfPrint("warning", ll=LogCode.WARNING)
fhnfPrint("error", ll=LogCode.ERROR)
fhnfPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#        Python         #")
print("#########################")
pythonPrint("none")
pythonPrint("heading", ll=LogCode.HEADING)
pythonPrint("debug", ll=LogCode.DEBUG)
pythonPrint("info", ll=LogCode.INFO)
pythonPrint("success", ll=LogCode.OK)
pythonPrint("warning", ll=LogCode.WARNING)
pythonPrint("error", ll=LogCode.ERROR)
pythonPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#       ColorLog        #")
print("#########################")
colorlogPrint("none")
colorlogPrint("heading", ll=LogCode.HEADING)
colorlogPrint("debug", ll=LogCode.DEBUG)
colorlogPrint("info", ll=LogCode.INFO)
colorlogPrint("success", ll=LogCode.OK)
colorlogPrint("warning", ll=LogCode.WARNING)
colorlogPrint("error", ll=LogCode.ERROR)
colorlogPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#       PrintTags       #")
print("#########################")
printtagsPrint("none")
printtagsPrint("heading", ll=LogCode.HEADING)
printtagsPrint("debug", ll=LogCode.DEBUG)
printtagsPrint("info", ll=LogCode.INFO)
printtagsPrint("success", ll=LogCode.OK)
printtagsPrint("warning", ll=LogCode.WARNING)
printtagsPrint("error", ll=LogCode.ERROR)
printtagsPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#          Xa           #")
print("#########################")
xaPrint("none")
xaPrint("heading", ll=LogCode.HEADING)
xaPrint("debug", ll=LogCode.DEBUG)
xaPrint("info", ll=LogCode.INFO)
xaPrint("success", ll=LogCode.OK)
xaPrint("warning", ll=LogCode.WARNING)
xaPrint("error", ll=LogCode.ERROR)
xaPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#         Lamu          #")
print("#########################")
lamuPrint("none")
lamuPrint("heading", ll=LogCode.HEADING)
lamuPrint("debug", ll=LogCode.DEBUG)
lamuPrint("info", ll=LogCode.INFO)
lamuPrint("success", ll=LogCode.OK)
lamuPrint("warning", ll=LogCode.WARNING)
lamuPrint("error", ll=LogCode.ERROR)
lamuPrint("critical", ll=LogCode.CRITICAL)

print("#########################")
print("#        Custom         #")
print("#########################")
customLogger = Logger({"a": "a {}", "b": "b {}", "c": "🐱 {}", "d": "🐲 {}"})
customLogger.pprint("none")
customLogger.pprint("letter a", ll="a")
customLogger.pprint("letter b", ll="b")
customLogger.pprint("cat", ll="c")
customLogger.pprint("dragon", ll="d")


textStream = result.getvalue()
ansiToSVG(textStream, THISDIR + "/readme-assets/screenshots/screenshot-0.svg")
print(textStream, file=oldStdout)
