# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.RIGHT_ALT: Key.HENKAN,
    Key.LEFT_META: Key.RIGHT_ALT,
})

define_multipurpose_modmap({
    Key.LEFT_ALT: [Key.HENKAN, Key.LEFT_CTRL],
    # Key.LEFT_META: [Key.LEFT_CTRL, Key.LEFT_META]
})

define_keymap(None, {
    K('Alt-h'): K('LEFT'),
    K('Alt-j'): K('DOWN'),
    K('Alt-k'): K('UP'),
    K('Alt-l'): K('RIGHT'),
    K('Shift-ESC'): K('Shift-GRAVE'),
})

