from dragonfly import (AppContext, Dictation, Grammar, IntegerRef, Key, MappingRule,
                       Pause, Repeat, Text)
from dragonfly.actions.action_mimic import Mimic

from castervoice.lib import control, settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R


class FileDialogueRule(MergeRule):
    pronunciation = "file dialogue"

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
            R(Key("c-l, tab:3")),
        "center pane":
            R(Key("c-l, tab:4")),
        "sort":
            R(Key("c-l, tab:5")),
        "organize":
            R(Key("c-l, tab:2")),
        "(dateiname | filename)":
            R(Key("c-l, tab:6")),
        "(dateityp | file type)":
            R(Key("c-l, tab:7")),
    }
    extras = [IntegerRefST("n", 1, 10)]
    defaults = {
        "n": 1,
    }

dialogue_names = [
    "open",
    "ffnen",
    "speichern",
    "select",
]

context = AppContext(title="save")
for name in dialogue_names:
    context = context | AppContext(title=name)

grammar = Grammar("FileDialogue", context=context)
rule = FileDialogueRule()
gfilter.run_on(rule)
grammar.add_rule(FileDialogueRule(name="filedialogue"))
grammar.load()
