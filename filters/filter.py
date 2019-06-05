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
            replace_spec(mp.rule1, "quotes", "(quotes|zit)")
            replace_spec(mp.rule1, "thin quotes", "(small quotes |zit klei)")
            replace_spec(mp.rule1, "pipe (sim | symbol)", "(rohr | pipe symbol)")
            replace_spec(mp.rule1, "long pipe (sim | symbol)", "(lang rohr | long pipe symbol)")
            replace_spec(mp.rule1, "comma", "(comma|komm)")
            replace_spec(mp.rule1, "shift right click", "test")
            replace_spec(mp.rule1, "curse <direction> [<direction2>] [<nnavi500>] [<dokick>]", "(curse|maus) <direction> [<direction2>] [<nnavi500>] [<dokick>]")
            replace_spec(mp.rule1, "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)]", "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>)]")
            replace_spec(mp.rule1, "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)", "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>)")
            replace_spec(mp.rule1, "(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel) <textnv> [brunt]", "(<capitalization> <spacing> | <capitalization> | <spacing>) <textnv>")
   
        replace_spec(mp.rule2, "numb <wnKK>", "number <wnKK>")
        replace_spec(mp.rule2, "word number <wn>", "word digit <wn>")
        replace_spec(mp.rule2, "quotes", "(quotes|zit)")
        replace_spec(mp.rule2, "thin quotes", "(small quotes |zit klei)")
        replace_spec(mp.rule2, "pipe (sim | symbol)", "(rohr | pipe symbol)")
        replace_spec(mp.rule2, "long pipe (sim | symbol)", "(lang rohr | long pipe symbol)")
        replace_spec(mp.rule2, "comma", "(comma|komm)")
        replace_spec(mp.rule2, "shift right click", "test")
        replace_spec(mp.rule2, "curse <direction> [<direction2>] [<nnavi500>] [<dokick>]", "(curse|haus) <direction> [<direction2>] [<nnavi500>] [<dokick>]")
        replace_spec(mp.rule2, "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)]", "spark [<nnavi500>] [(<capitalization> <spacing> | <capitalization> | <spacing>)]")
        replace_spec(mp.rule2, "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel)", "set [<big>] format (<capitalization> <spacing> | <capitalization> | <spacing>)")
        replace_spec(mp.rule2, "(<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel) <textnv> [brunt]", "(<capitalization> <spacing> | <capitalization> | <spacing>) <textnv>")
 
def update_carrot(rule):
    if "carrot" in rule.mapping_actual().keys():
        rule.mapping_actual()["carrot"] = R(Key("caret") + Key("left") + Key("delete"))

def fix_carrot_german_windows10_scenario(mp):
    if mp.time == MergeInf.BOOT:
        if mp.rule1 is not None :
            update_carrot(mp.rule1)   
        update_carrot(mp.rule2)

control.nexus().merger.add_filter(replace_spec_scenario)
control.nexus().merger.add_filter(fix_carrot_german_windows10_scenario)