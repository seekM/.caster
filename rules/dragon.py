from dragonfly import (Grammar, Playback, Key, Dictation, Function)

from castervoice.lib import control
from castervoice.lib import utilities, settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

_NEXUS = control.nexus()


def fix_dragon_double(nexus):
    try:
        lr = nexus.history[len(nexus.history) - 1]
        lu = " ".join(lr)
        Key("left/5:" + str(len(lu)) + ", del").execute()
    except Exception:
        utilities.simple_log(False)


class DragonRule(MergeRule):
    pronunciation = "dragon"

    mapping = {
        "reboot dragon":
            R(Function(utilities.reboot), rdescript="Reboot Dragon Naturallyspeaking"),
    }

    extras = [
        Dictation("text"),
        Dictation("mim"),
        IntegerRefST("n", 1, 1000),
    ]
    defaults = {"n": 1, "mim": ""}


#---------------------------------------------------------------------------

grammar = Grammar("Dragon Naturallyspeaking")

rule = DragonRule(name="dragon")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
