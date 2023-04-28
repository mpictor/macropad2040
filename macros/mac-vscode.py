from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.mouse import Mouse

# COLOR    LABEL    KEY SEQUENCE
# 1st row ----------
JmpDef =  (0x004000, 'JmpDef', [Keycode.F12])
OpenLnk = (0x200000, 'OpenLnk', [Keycode.ALT,{'buttons':Mouse.LEFT_BUTTON}])
FoldL1 =  (0x00a000, 'FoldL1', [Keycode.F16])
# 2nd row ----------
Refs =    (0x200000, 'Refs',   [Keycode.SHIFT,Keycode.F16])
Impls =   (0x202000, 'Impls',  [Keycode.CONTROL,Keycode.F16])
FoldL2 =  (0x002020, 'FoldL2', [Keycode.F17])
# 3rd row ----------
QOpen =   (0x101000, 'QOpen',  [Keycode.COMMAND,'p'])
Cmds =    (0x201010, 'Cmds',   [Keycode.F1])
Unfold=   (0x100020, 'Unfold', [Keycode.SHIFT,Keycode.F17])
# 4th row ----------
TstPkg =  (0x102040, 'TstPkg', [Keycode.CONTROL,Keycode.F18])
TstAt =   (0x204010, 'Tst @',  [Keycode.F18])
DbgAt =   (0x401020, 'Dbg @',  [Keycode.SHIFT,Keycode.F18])
# Encoder button ---
#(0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab

app = {
    'name' : 'Mac VSCode',
    'macros' : [
        JmpDef, OpenLnk, FoldL1,
        Refs,   Impls,   FoldL2,
        QOpen,  Cmds,    Unfold,
        TstPkg, TstAt,   DbgAt
    ]
}

#   * vscode - code [DEFAULT]
#     * find all refs (shift-alt-f12)
#     * jump to def (F12)
#     * find all impls
#     * find/replace/next
#     * fold, unfold levels (ctrl-k ctrl-1, f16)
#     * open file (option-click)
#     * focus terminal


# unicode??

# [opn crsr] [save/test] []
# [jmp  def] [all refs] [all impl]
# [  find  ] [  repl ] [  next  ]
# [  fold  ] [ unfld?] []



# "f16":            "editor.foldLevel1",
# "shift+f16":      "references-view.findReferences",
# "ctrl+f16":       "references-view.findImplementations"
# "ctrl+s":         "workbench.action.files.save"
# "alt+p":          "workbench.action.quickOpen"
# "shift+alt+p":    "workbench.action.showCommands"
# "alt+f16":        "go.test.cursor"
# "shift+alt+f16":  "go.debug.cursor"


## skip
# "ctrl+/":         "editor.action.commentLine",
# "insert":         "git.stageSelectedRanges",
# "shift+delete":   "editor.action.clipboardCutAction"

### term
# "home":           "workbench.action.terminal.sendSequence"               # "args": { "text": "\u0001" }, //send ctrl-a
# "end":            "workbench.action.terminal.sendSequence"                 # "name":  "ctrl-e", "args": { "text": "\u0005" }, //send ctrl-e
# "alt+left":       "workbench.action.terminal.sendSequence",           # "name":  "ctrl <=", "args": { "text": "\u001b[1;5D" },
# "alt+right":      "workbench.action.terminal.sendSequence",          # "name": "ctrl-rightarrow", "args": { "text": "\u001b[1;5E" },
# "shift+cmd+c":    "workbench.action.terminal.sendSequence",        # "name": "ctrl-c", "args": { "text": "\u0003" },
# "ctrl+c":         "workbench.action.terminal.sendSequence",
# "shift+right":    "workbench.action.terminal.focusNext",
# "shift+left":     "workbench.action.terminal.focusPrevious",
