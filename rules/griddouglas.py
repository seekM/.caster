"""
Command-module for DouglasGrid

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


def send_input(n, n2, action, nexus):
    s = nexus.comm.get_com("grids")
    s.move_mouse(int(n), int(n2))
    s.kill()
    grids.wait_for_death(settings.DOUGLAS_TITLE)
    int_a = int(action)
    if int_a == 0:
        Mouse("left").execute()
    elif int_a == 1:
        Mouse("right").execute()


class GridControlRule(MergeRule):

    mapping = {
        "<n> [by] <n2> [<action>]":
            R(Function(send_input, nexus=_NEXUS), rdescript="Douglas Grid: Action"),
        "exit | escape | cancel":
            R(Function(kill, nexus=_NEXUS), rdescript="Exit Douglas Grid"),
    }
    extras = [
        IntegerRefST("n", 0, 300),
        IntegerRefST("n2", 0, 300),
        Choice("action", {
            "kick": 0,
            "psychic": 1,
        }),
    ]
    defaults = {
        "action": 0,
    }


#---------------------------------------------------------------------------

context = AppContext(title="douglasgrid")
grammar = Grammar("douglasgrid", context=context)

rule = GridControlRule(name="Douglas")
gfilter.run_on(rule)
grammar.add_rule(rule)
grammar.load()
