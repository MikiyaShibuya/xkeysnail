# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.RIGHT_ALT: Key.HIRAGANA,
    Key.RIGHT_META: Key.LEFT_META,
    # Key.LEFT_META: Key.RIGHT_ALT,
    Key.LEFT_META: Key.RIGHT_META,
})

define_multipurpose_modmap({
    Key.LEFT_ALT: [Key.HENKAN, Key.LEFT_CTRL],
    # Key.RIGHT_META: [Key.LEFT_CTRL, Key.LEFT_META]
})

define_keymap(None, {
    K('RSuper-h'): K('LEFT'),
    K('RSuper-j'): K('DOWN'),
    K('RSuper-k'): K('UP'),
    K('RSuper-l'): K('RIGHT'),
    K('Shift-ESC'): K('Shift-GRAVE'),
})

