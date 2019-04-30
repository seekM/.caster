"""
__author__ = 'LexiconCode'
Command-module for Slack
"""
#---------------------------------------------------------------------------

from dragonfly import (Dictation, Grammar, MappingRule, Repeat)

from castervoice.lib import control, settings
from castervoice.lib.actions import Key, Text
from castervoice.lib.context import AppContext
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R

class SlackRule(MergeRule):
    pronunciation = "Slack"

    mapping = {
        "(up | hoch)":
            R(Key("a-up")),
        "(down | runter)":
            R(Key("a-down")),
        "(next message | naechste nachricht)":
            R(Key("as-up")),
        "(previous message | vorherige nachricht)":
            R(Key("as-down")),
        "edit":
            R(Key("up")),
        "(new line | neue zeile)":
            R(Key("s-enter")),
        "(bold | fett)":
            R(Text("**") + Key("left")),
        "(emphasize | hervorheben)":
            R(Text("__") + Key("left")),
        "(search | suche)":
            R(Key("c-f")),
        "(block quote | zitat)":
            R(Text("> ")),
        "(mention | erwaehnen)":
            R(Text("@")),
        "(short code | kurzer code)":
            R(Text("```") + Key("left")),
        "(insert code | code einfuegen)":
            R(Text("```") + Key("backspace") + Text("```") + 
              Key("s-enter") + Key("s-enter") + 
              Text("```") + Key("backspace") + Key("backspace") + Text("```") + Text("```") + Key("backspace") + Key("backspace") + Key("backspace")+ 
              Key("up")), 
    }
    
#---------------------------------------------------------------------------

context = AppContext(executable="slack")
grammar = Grammar("slack", context=context)

rule = SlackRule(name="slack")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()