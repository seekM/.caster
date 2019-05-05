"""
Command-module for RainbowGrid

"""

from dragonfly import (Grammar, Function, Playback, Choice, MappingRule, Mouse)

from castervoice.asynch.mouse import grids
from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.context import AppContext

_NEXUS = control.nexus()


def kill(nexus):
    nexus.comm.get_com("grids").kill()


def send_input(pre, color, n, action, nexus):
    s = nexus.comm.get_com("grids")
    s.move_mouse(int(pre), int(color), int(n))
    s.kill()
    grids.wait_for_death(settings.RAINBOW_TITLE)
    int_a = int(action)
    if int_a == 0:
        Mouse("left").execute()
    elif int_a == 1:
        Mouse("right").execute()


class GridControlRule(MergeRule):

    mapping = {
        "[<pre>] <color> <n> [<action>]":
            R(Function(send_input, nexus=_NEXUS), rdescript="Rainbow: Rainbow Grid: Action"),
        "exit | escape | cancel":
            R(Function(kill, nexus=_NEXUS), rdescript="Rainbow: Exit Rainbow Grid"),
    }
    extras = [
        IntegerRefST("pre", 0, 9),
        Choice(
            "color", {
                "(red | rot)": 0,
                "(orange | tan | brown | braun)": 1,
                "(yellow | gelb)": 2,
                "(green | gruen)": 3,
                "(blue | blau)": 4,
                "(purple | lila)": 5
            }),
        Choice("action", {
            "kick": 0,
            "psychic": 1,
        }),
        IntegerRefST("n", 0, 100),
    ]
    defaults = {
        "pre": 0,
        "action": 0,
    }

#---------------------------------------------------------------------------

context = AppContext(title="rainbowgrid")
grammar = Grammar("rainbowgrid", context=context)

rule = GridControlRule(name="rainbow")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
