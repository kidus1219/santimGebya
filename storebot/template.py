from .const import P_H, MAIN_HOST
GATE = {
    'text': """
You are not registered
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Help"], ["About"]],
    ],
    'state': 0
}

HOME = {
    'text': """
This is home
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Profile", "webapp", f"{MAIN_HOST}/store/profile/{P_H}/"], ["Cashier", "webapp", f"{MAIN_HOST}/store/cashier/{P_H}/"]],
        [["Help"], ["About"]],
    ],
    'state': 1
}

HELP = {
    'text': """
This is HELP
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]],
    ],
    'state': 2
}

ABOUT = {
    'text': """
This is ABOUT
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]],
    ],
    'state': 3
}