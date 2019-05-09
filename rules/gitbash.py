#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for git

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Mimic, Function)

from castervoice.lib import control
from castervoice.lib import settings
from castervoice.lib.dfplus.additions import IntegerRefST
from castervoice.lib.dfplus.merge import gfilter
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib.context import AppContext
from castervoice.lib.actions import (Key, Text)
from castervoice.lib.dfplus.merge.ccrmerger import CCRMerger

class GitBashRule(MergeRule):
    pronunciation = "git bash"
    mwith = CCRMerger.CORE
    mapping = {
    
        # Compare to https://github.com/seekM/docs/blob/master/git.md
        
        # Basics
        # ======
    
        "get (initialize|initialisieren)":
            R(Text("git init") + Key("enter")),
        
        "get (status|zustand)":
            R(Text("git status") + Key("enter")),
        "get (status briefly|zustand kurz)":
            R(Text("git status --short") + Key("enter")),
        
        "get (append file|datei hinzufuegen)":
            Text("git add "),
        "get (append directory|ordner hinzufuegen)":
            R(Text("git add .") + Key("enter")),
        "get (append all|alle hinzufuegen)":
            R(Text("git add -A") + Key("enter")),
                
        "get difference file":
            Text("git diff "),
        "get difference":
            R(Text("git diff") + Key("enter")),
        "get difference staged": 
            R(Text("git diff --staged") + Key("enter")),
        
        "get commit":
            R(Text("git commit") + Key("enter")),
        "get commit message":
            R(Text("git commit --message \"\"") + Key("left")), # message
            
        "get (remove|entfernen)":
            R(Text("git rm ")), # file
        "get remove force":
            R(Text("git rm --force ")), # file
            
        "get (rename|umbenennen)":
            R(Text("git mv ")), # file1 file2
            
        "get unmodify file":
            R(Text("git checkout -- ")), # file           
        "get (unstage file|datei rueckgaengig)":
            R(Text("git reset HEAD ")), # file   
        "get reset repository":
            R(Text("git reset --hard") + Key("enter")),  
        "get (redo commit|commit wiederholen)":
            R(Text("git commit --amend --message \"\"") + Key("left")), # message         
          
        # Branches
        # ========
            
        "get branch":
            R(Text("git branch ")), # branch
            
        "get (switch|checkout)":
            R(Text("git checkout ")), # branch
        
        "get branch (delete|entfernen)":
            R(Text("git branch --delete ")), # branch
        "get branch (delete|entfernen) force":
            R(Text("git branch --delete -- force ")), # branch
            
        "get branch (combine|kombiniert)":
            R(Text("git checkout -b ")), # branch
              
        "get (reset branch|branch zuruecksetzen)":
            R(Text("git reset --hard ")), # branch
            
        # Merging
        # =======
        
        "get (merge|vereinen)":
            R(Text("git merge ")), # branch
            
        "get (show merged|zeige vereinigt)":
            R(Text("git branch --merged") + Key("enter")),
        
        "get (show not merged|zeige nicht vereinigt)":
            R(Text("git branch --no--merged") + Key("enter")),
        
        "get (logging|aufzeichnung) graph":
            R(Text("git loggraph")),
        "get (logging|aufzeichnung) patch <n>":
            R(Text("git log --patch -%(n)s") + Key("enter")), # number
        "get (logging|aufzeichnung) statistic":
            R(Text("git log --stat") + Key("enter")),
            
        # Remotes
        # =======
        
        "get (clone|kopieren)":
            R(Text("git clone ")), # url
        "get append remote":
            R(Text("git remote add ")), # remote_repository(e.g. upstream) url
        "get (show|zeige) remotes":
            R(Text("git remote --verbose") + Key("enter")),
            
        "get (show|zeige) remote branches":
            R(Text("git branch --remote") + Key("enter")),
        "get fetch remote":
            R(Text("git fetch ")), # remote_repository
        "get push new branch":
            R(Text("git push --set-upstream ")), # remote_repository branch
        "get push branch":
            R(Text("git push ")), # remote_repository branch
            
        "get (tracking|verfolgungs) branch": 
             R(Text("git checkout --branch ")), # branch remote_repository/branch
        "get (show tracking|zeige verfolgungs) branches": 
             R(Text("git branch --verbose --verbose") + Key("enter")),
        "get (delete|entferne) remote branch": 
             R(Text("git push  --delete ") + Key("left:10")), # remote_repository branch
            
        # Rebasing
        # ========
        
        "get base": 
             R(Text("git rebase ")), # branch              
             
        # Miscellaneous
        # =============
                
        "get (stash|versteck)":
            R(Text("git stash save --message \"\"") + Key("left")),
        "get (stash|versteck) include untracked":
            R(Text("git stash save --include-untracked --message \"\"") + Key("left")),
        "get (stash|versteck) list show":
            R(Text("git stash list") + Key("enter")),
        
        #"get (stash apply|versteck anwenden) [<n>]":
        #    R(Text("git stash apply stash@{%(n)s}")), # @,{,} don't work at the moment
        #"get (stash apply|versteck anwenden) [<n>] file":
        #    R(Text("git checkout stash@{%(n)s} -- ")), # file # @,{,} don't work at the moment
        #"get (stash|versteck) drop [<n>]":
        #    R(Text("git stash drop stash@{%(n)s}")), # @,{,} don't work at the moment
        
        "get (stash apply|versteck anwenden)":
            R(Text("git stash apply")),
        "get (dropping stash|versteck verwerfen)":
            R(Text("git stash drop")),
        "get (search|suche)": 
             R(Text("git grep --line-number ")), # searchterm       
             
        # Other
        # =====    
            
        "CD up":
            R(Text("cd ..") + Key("enter")),
        "CD":
            R(Text("cd ") + Key("enter")),
        "list":
            R(Text("ls") + Key("enter")),
        "make directory":
            R(Text("mkdir ")),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}


#---------------------------------------------------------------------------

context = AppContext(executable="\\sh.exe") | \
          AppContext(executable="\\bash.exe") | \
          AppContext(executable="\\cmd.exe") | \
          AppContext(executable="\\mintty.exe")

control.nexus().merger.add_app_rule(GitBashRule(), context)
