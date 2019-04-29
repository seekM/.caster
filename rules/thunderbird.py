#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Thunderbird

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Dictation, Repeat)

from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class ThunderbirdRule(MergeRule):
    pronunciation = "thunderbird"

    mapping = {
        "(new message | neue nachricht)":
            R(Key("c-n")),
        "(reply | antworten)":
            R(Key("c-r")),
        "(reply all | allen antworten)":
            R(Key("cs-r")),
        "(forward message | nachricht weiterleiten)":
            R(Key("cs-r")),
        "(retrieve | abholen)":
            R(Key("s-f5")),
        "(expand | aufklappen)":
            R(Key("*")),
        "(collapse | einklappen)":
            R(Key("\\")),
        "(toggle read | gelesen | ungelesen)":
            R(Key("m")),
        "(no | kein) spam":
            R(Key("s-j")),
        "spam":
            R(Key("j")),
        "(toggle star | favorit)":
            R(Key("s")),
        "(next message | naechste nachricht)":
            R(Key("n")),
        "(previous message | vorherige nachricht)":
            R(Key("p")),
        "toggle pane":
            R(Key("f6")),
        "(next | naechster) tab":
            R(Key("c-tab")),
        "(previous | vorheriger) tab":
            R(Key("cs-tab")),
        "(attach file | datei anhaengen)":
            R(Key("cs-a")),
    }

#---------------------------------------------------------------------------

context = AppContext(executable="thunderbird")
grammar = Grammar("thunderbird", context=context)

rule = ThunderbirdRule(name="thunderbird")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
