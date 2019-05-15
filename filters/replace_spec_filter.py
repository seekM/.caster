# -*- coding: utf-8 -*-

from dragonfly import Text, Key

from castervoice.lib.actions import Text
from castervoice.lib.dfplus.merge.mergepair import MergeInf
from castervoice.lib.dfplus.state.short import R
from castervoice.lib import control

def replace_spec(rule, target, replacement):
    if target in rule.mapping_actual().keys():
        action = rule.mapping_actual()[target]
        del rule.mapping_actual()[target]
        rule.mapping_actual()[replacement] = action


def replace_spec_scenario(mp):
    if mp.time == MergeInf.BOOT:
        if mp.rule1 is not None:
            replace_spec(mp.rule1, "numb <wnKK>", "number <wnKK>")
            replace_spec(mp.rule1, "word number <wn>", "word digit <wn>")
        replace_spec(mp.rule2, "numb <wnKK>", "number <wnKK>")
        replace_spec(mp.rule2, "word number <wn>", "word digit <wn>")

def update_carrot(rule):
    if "carrot" in rule.mapping_actual().keys():
        rule.mapping_actual()["carrot"] = R(Text("^") + Text("^") + Key("left") + Key("delete"))

def fix_carrot_german_windows10_scenario(mp):
    if mp.time == MergeInf.BOOT:
        if mp.rule1 is not None :
            update_carrot(mp.rule1)
        update_carrot(mp.rule2)

control.nexus().merger.add_filter(replace_spec_scenario)
control.nexus().merger.add_filter(fix_carrot_german_windows10_scenario)