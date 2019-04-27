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
        "(address bar | adressleiste)":
            R(Key("c-l"), rdescript="Explorer: Address Bar"),
        "(new folder | neuer ordner)":
            R(Key("cs-n"), rdescript="Explorer: New Folder"),
        # "new file": sikuli # annahme: menue zu sehen
        "(show | file | folder) properties":
            R(Key("a-enter"), rdescript="Explorer: Properties Dialog"),
        "get up":                            
            R(Key("a-up"), rdescript="Explorer: Navigate up"),
        "get back":
            R(Key("a-left"), rdescript="Explorer: Navigate back"),
        "get forward":
            R(Key("a-right"), rdescript="Explorer: Navigate forward"),
    }
    extras = [
        Dictation("text"),
        IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1}


#---------------------------------------------------------------------------

context = AppContext(executable="explorer")
grammar = Grammar("Windows Explorer", context=context)

if settings.SETTINGS["apps"]["explorer"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(IERule())
    else:
        rule = IERule(name="explorer")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
