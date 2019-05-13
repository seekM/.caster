# -*- encoding: utf-8 -*-

# addition to castervoice/lib/ccr/core/numbers.py

from dragonfly import Function

from castervoice.lib import control, alphanumeric
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger
from castervoice.lib.actions import Key, Text, Mouse
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

def wort_zahl(wn):
    numbers_to_words = {
        0: "null",
        1: "eins",
        2: "zwei",
        3: "drei",
        4: "vier",
        5: u"fünf",
        6: "sechs",
        7: "sieben",
        8: "acht",
        9: "neun"
    }
    Text(numbers_to_words[int(wn)]).execute()

class Zahlen(MergeRule):
    pronunciation = "zahlen"

    mapping = {
        "wort ziffer <wn>":
            R(Function(wort_zahl, extra="wn")),
    }

    extras = [
        IntegerRefST("wn", 0, 10),
    ]
    defaults = {}

def get_rule():
    return Zahlen()