#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Notepad++
"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar)

from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

class NPPRule(MergeRule):
    pronunciation = "notepad plus plus"

    mapping = {
        "(line | zeile) <n>":
            R(Key("c-g") + Text("%(n)d") + Key("enter")),
        "(save | speichern)":
            R(Key("c-s")),
        "(save as | speichern als)":
            R(Key("ca-s")),        
    }
    extras = [
        IntegerRefST("n", 1, 1000)
    ]
    defaults = {"n": 1}

#---------------------------------------------------------------------------

context = AppContext(executable="notepad++")
grammar = Grammar("Notepad++", context=context)

rule = NPPRule(name="notepad plus plus")
grammar.add_rule(rule)
grammar.load()