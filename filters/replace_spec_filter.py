# -*- coding: utf-8 -*-

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
            #replace_spec(mp.rule1, "[<big>] arch", "[<big>] air")
        replace_spec(mp.rule2, "numb <wnKK>", "number <wnKK>")
        replace_spec(mp.rule2, "word number <wn>", "word digit <wn>")


def get_filter():
    return replace_spec_scenario