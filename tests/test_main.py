#!/usr/bin/env python3
"""Test fhprint
"""
from __future__ import annotations

import sys
from io import StringIO
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))


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


def test_meterpreter():
	result = StringIO()
	metPrint("none", file=result)
	metPrint("heading", ll=LogCode.HEADING, file=result)
	metPrint("debug", ll=LogCode.DEBUG, file=result)
	metPrint("info", ll=LogCode.INFO, file=result)
	metPrint("success", ll=LogCode.OK, file=result)
	metPrint("warning", ll=LogCode.WARNING, file=result)
	metPrint("error", ll=LogCode.ERROR, file=result)
	metPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/meterpreter.txt").read_text(encoding="utf-8")


def test_fH():
	result = StringIO()
	fhPrint("none", file=result)
	fhPrint("heading", ll=LogCode.HEADING, file=result)
	fhPrint("debug", ll=LogCode.DEBUG, file=result)
	fhPrint("info", ll=LogCode.INFO, file=result)
	fhPrint("success", ll=LogCode.OK, file=result)
	fhPrint("warning", ll=LogCode.WARNING, file=result)
	fhPrint("error", ll=LogCode.ERROR, file=result)
	fhPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/fh.txt").read_text(encoding="utf-8")


def test_fHNF():
	result = StringIO()
	fhnfPrint("none", file=result)
	fhnfPrint("heading", ll=LogCode.HEADING, file=result)
	fhnfPrint("debug", ll=LogCode.DEBUG, file=result)
	fhnfPrint("info", ll=LogCode.INFO, file=result)
	fhnfPrint("success", ll=LogCode.OK, file=result)
	fhnfPrint("warning", ll=LogCode.WARNING, file=result)
	fhnfPrint("error", ll=LogCode.ERROR, file=result)
	fhnfPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/fhnf.txt").read_text(encoding="utf-8")


def test_python():
	result = StringIO()
	pythonPrint("none", file=result)
	pythonPrint("heading", ll=LogCode.HEADING, file=result)
	pythonPrint("debug", ll=LogCode.DEBUG, file=result)
	pythonPrint("info", ll=LogCode.INFO, file=result)
	pythonPrint("success", ll=LogCode.OK, file=result)
	pythonPrint("warning", ll=LogCode.WARNING, file=result)
	pythonPrint("error", ll=LogCode.ERROR, file=result)
	pythonPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/python.txt").read_text(encoding="utf-8")


def test_colorLog():
	result = StringIO()
	colorlogPrint("none", file=result)
	colorlogPrint("heading", ll=LogCode.HEADING, file=result)
	colorlogPrint("debug", ll=LogCode.DEBUG, file=result)
	colorlogPrint("info", ll=LogCode.INFO, file=result)
	colorlogPrint("success", ll=LogCode.OK, file=result)
	colorlogPrint("warning", ll=LogCode.WARNING, file=result)
	colorlogPrint("error", ll=LogCode.ERROR, file=result)
	colorlogPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/colorLog.txt").read_text(encoding="utf-8")


def test_printTags():
	result = StringIO()
	printtagsPrint("none", file=result)
	printtagsPrint("heading", ll=LogCode.HEADING, file=result)
	printtagsPrint("debug", ll=LogCode.DEBUG, file=result)
	printtagsPrint("info", ll=LogCode.INFO, file=result)
	printtagsPrint("success", ll=LogCode.OK, file=result)
	printtagsPrint("warning", ll=LogCode.WARNING, file=result)
	printtagsPrint("error", ll=LogCode.ERROR, file=result)
	printtagsPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/printTags.txt").read_text(encoding="utf-8")


def test_xa():
	result = StringIO()
	xaPrint("none", file=result)
	xaPrint("heading", ll=LogCode.HEADING, file=result)
	xaPrint("debug", ll=LogCode.DEBUG, file=result)
	xaPrint("info", ll=LogCode.INFO, file=result)
	xaPrint("success", ll=LogCode.OK, file=result)
	xaPrint("warning", ll=LogCode.WARNING, file=result)
	xaPrint("error", ll=LogCode.ERROR, file=result)
	xaPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/xa.txt").read_text(encoding="utf-8")


def test_lamu():
	result = StringIO()
	lamuPrint("none", file=result)
	lamuPrint("heading", ll=LogCode.HEADING, file=result)
	lamuPrint("debug", ll=LogCode.DEBUG, file=result)
	lamuPrint("info", ll=LogCode.INFO, file=result)
	lamuPrint("success", ll=LogCode.OK, file=result)
	lamuPrint("warning", ll=LogCode.WARNING, file=result)
	lamuPrint("error", ll=LogCode.ERROR, file=result)
	lamuPrint("critical", ll=LogCode.CRITICAL, file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/lamu.txt").read_text(encoding="utf-8")


def test_custom():
	result = StringIO()
	customLogger = Logger({"a": "a {}", "b": "b {}", "c": "🐱 {}", "d": "🐲 {}"})
	customLogger.pprint("none", file=result)
	customLogger.pprint("letter a", ll="a", file=result)
	customLogger.pprint("letter b", ll="b", file=result)
	customLogger.pprint("cat", ll="c", file=result)
	customLogger.pprint("dragon", ll="d", file=result)
	assert result.getvalue() == Path(f"{THISDIR}/data/custom.txt").read_text(encoding="utf-8")
