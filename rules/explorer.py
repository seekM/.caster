from dragonfly import (Grammar, MappingRule, Dictation, IntegerRef,
                       Repeat, Pause)

from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.context import AppContext
from castervoice.lib.actions import (Key, Text)


class IERule(MergeRule):
    pronunciation = "explorer"

    mapping = {
        "get up [<n>]":
            R(Key("a-up"))*Repeat(extra="n"),
        "get back [<n>]":
            R(Key("a-left"))*Repeat(extra="n"),
        "get forward [<n>]":
            R(Key("a-right"))*Repeat(extra="n"),
        "new folder":
            R(Key("cs-n")),
        "address bar":
            R(Key("c-l")),
        "search":
            R(Key("c-l, tab")),
        "left pane":
            R(Key("c-l, tab:2")),
        "center pane":
            R(Key("c-l, tab:3")),
        "sort":
            R(Key("c-l, tab:4")),
    }
    extras = [IntegerRefST("n", 1, 10)]
    defaults = {
        "n": 1,
    }


#---------------------------------------------------------------------------

context = AppContext(executable="explorer")
grammar = Grammar("Windows Explorer", context=context)

rule = IERule(name="explorer")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()