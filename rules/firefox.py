#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Firefox

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


class FirefoxRule(MergeRule):
    pronunciation = "fire fox"

    mapping = {
        "new tab [<n>]":
            R(Key("c-t"))*Repeat(extra="n"),
        "reopen tab [<n>]":
            R(Key("cs-t"))*Repeat(extra="n"),
        "show history":
            R(Key("c-h")),
        "show downloads":
            R(Key("c-j")),
        "show bookmarks":
            R(Key("c-b")),
        "[add] bookmark":
            R(Key("c-d")),
        "cancel bookmark": # Call this after "[add] bookmark" if you want to cancel
            R(Key("a-b")),
        "delete bookmark": # Call if you are on a page you have bookmarked before
            R(Key("c-d") + Pause("200") + Key("a-e")),
        "full screen":
            R(Key("f11")),
        "zoom in [<n>]":
            R(Key("c-plus/20"))*Repeat(extra="n"),
        "zoom out [<n>]":
            R(Key("c-minus/20"))*Repeat(extra="n"),

        # the following commands requires the vim vixen extension
        "scroll down [<n>]":
            R(Key("c-f"))*Repeat(extra="n"),
        "scroll down half [<n>]":
            R(Key("c-d"))*Repeat(extra="n"),
        "scroll up [<n>]":
            R(Key("c-b"))*Repeat(extra="n"),
        "scroll up half [<n>]":
            R(Key("c-u"))*Repeat(extra="n"),
        "scroll top":
            R(Key("g") + Key("g")),
        "scroll bottom":
            R(Key("G")),
        "reload":
            R(Key("r")),
        "toggle pin":
            R(Key("z") + Key("p")),
        "(loesche pin | delete pin)":
            R(Key("!") + Key("d")),
        "history back [<n>]":
            R(Key("H"))*Repeat(extra="n"),
        "history forward [<n>]":
            R(Key("L"))*Repeat(extra="n"),
        "parent [<n>]":
            R(Key("g") + Key("u"))*Repeat(extra="n"),
        "root":
            R(Key("g") + Key("U")),
        "link": # opens in new tab
            R(Key("F")),
        "link here":
            R(Key("f")),
        "mark <letter>":
            R(Key("m") +  Text("%(letter)s")),
        "jump <letter>":
            R(Key("'") +  Text("%(letter)s")),
        "focus input":
            R(Text("gi")),
        "copy url": # copy URL in current tab
            R(Text("y")),
        "clipboard tab": # open clipboard's URL in current tab
            R(Text("p")),
        "clipboard new tab": # open clipboard's URL in new tab
            R(Text("P")),
        "toggle": # enables / disables add on
            R(Key("s-escape")),

        # from nav: next / prior / close tab
    }
    extras = [
        IntegerRefST("n", 1, 100),
        alphanumeric.get_alphabet_choice("letter"),
    ]
    defaults = {"n": 1}


#---------------------------------------------------------------------------

context = AppContext(executable="firefox")
grammar = Grammar("firefox", context=context)

rule = FirefoxRule(name="firefox")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
