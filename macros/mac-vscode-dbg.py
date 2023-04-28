from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
#from adafruit_hid.mouse import Mouse

# COLOR    LABEL    KEY SEQUENCE
# 1st row ----------
SOver = (0x200020, 'S Over',  [Keycode.F10])
SInto = (0x000020, 'S Into',  [Keycode.F11])
SOut  = (0x004000, 'S Out',   [Keycode.SHIFT,Keycode.F11])
Cont  = (0x004000, 'Cont',    [Keycode.F5])
ReSt  = (0x204000, 'Restart', [Keycode.COMMAND,Keycode.SHIFT,Keycode.F5])
Stop  = (0x500000, 'Stop',    [Keycode.SHIFT,Keycode.F5,])
_O_ = (0x000000, '', [])

# Encoder button ---
#(0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab

app = {                    
    'name' : 'Dbg VSCode-M', 
    'macros' : [           
        SOver, SInto, SOut,
        _O_  , _O_,   _O_,
        Cont,  _O_,   ReSt,
        _O_  , Stop
    ]
}
