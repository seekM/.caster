#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for HexChat

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Dictation, Repeat, Pause)

from castervoice.lib import control, alphanumeric
from castervoice.lib import settings
from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class HexChatRule(MergeRule):
    pronunciation = "hex chat"

    mapping = {
        "network list":
            R(Key("c-s")),

        # from nav: next / prior tab
    }

#---------------------------------------------------------------------------

context = AppContext(executable="hexchat")
grammar = Grammar("hexchat", context=context)

rule = HexChatRule(name="hexchat")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()