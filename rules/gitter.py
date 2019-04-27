"""
__author__ = 'LexiconCode'
Command-module for Gitter
Official Site "https://gitter.im/"
"""
#---------------------------------------------------------------------------

from dragonfly import Dictation, Grammar, MappingRule

from castervoice.lib import control, settings
from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

class GitterRule(MergeRule):
    pronunciation = "Gitter"

    mapping = {
        "(rooms | raeume)":
            R(Key("cs-1") + Key("right")),
        "(search | suche)":
            R(Key("cs-1") + Key("cs-2")),
        "chat":
            R(Key("escape") + Key("cs-c")),
        "edit":
            R(Key("up")),
        "(send | senden)":
            R(Key("s-enter"))
        # TODO: Exit by clicking top left, then down etc... (probabyl works only in full mode or sikuli)
    }
    extras = [
        Dictation("text"),
    ]
    Defaults = {}
    
#---------------------------------------------------------------------------

context = AppContext(executable="gitter")
grammar = Grammar("gitter", context=context)

rule = GitterRule(name="gitter")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()