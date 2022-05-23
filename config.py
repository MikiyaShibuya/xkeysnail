# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.LEFT_META: Key.MUHENKAN,
    Key.LEFT_ALT: Key.RIGHT_META,
    Key.RIGHT_META: Key.HENKAN,
    Key.RIGHT_ALT: Key.LEFT_META,
})

define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.LEFT_CTRL],
    Key.HENKAN: [Key.HENKAN, Key.LEFT_CTRL],
})

define_keymap(None, {
    K('RSuper-h'): K('LEFT'),
    K('RSuper-j'): K('DOWN'),
    K('RSuper-k'): K('UP'),
    K('RSuper-l'): K('RIGHT'),
    K('Shift-RSuper-h'): K('Shift-LEFT'),
    K('Shift-RSuper-j'): K('Shift-DOWN'),
    K('Shift-RSuper-k'): K('Shift-UP'),
    K('Shift-RSuper-l'): K('Shift-RIGHT'),
    K('Shift-ESC'): K('Shift-GRAVE'),
})

