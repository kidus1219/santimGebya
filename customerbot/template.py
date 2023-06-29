from .const import P_H, MAIN_HOST
GATE = {
    'text': """
This is core gate
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Register", "contact"]],
        [["Help"], ["About"]],
    ],
    'menu_button': ["Profile", f'{MAIN_HOST}/core/{P_H}/login/'],
    'state': 0
}

ACCEPT_PASSWORD = {
    'text': """
Enter your pin
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Cancel"]],
    ],
    'state': 2
}

CONFIRM_PASSWORD = {
    'text': f"""
Are you sure to make<b> {P_H} </b>your password? 
""",
    'keyboard_type': "inline",
    'keyboard': [
        [["Yes i am sure", "callback", "yes"], ["No let me change", "callback", "no"]],
    ],
    'state': 21
}

HOME = {
    'text': """
This is home
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Stores"]],
        [["Profile", "webapp", f"{MAIN_HOST}/core/{P_H}/profile/"], ["My Orders", "webapp", f"{MAIN_HOST}/core/{P_H}/orders/"]],
        [["Help"], ["About"]],
        [["Logout", "webapp", f"{MAIN_HOST}/core/{P_H}/logout/"]],
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
    'state': 3
}

ABOUT = {
    'text': """
This is ABOUT
""",
    'keyboard_type': "reply",
    'keyboard': [
        [["Back"]],
    ],
    'state': 4
}

STORE = {
    'text': """
This is store
""",
    'keyboard_type': "reply",
    'state': 5
}


WAITING_ORDER = {
    'text': f"""
╭──────────────────
│  Order {P_H}
│╭──────────────────
││<code>
││{P_H}
││</code>
│╰──────────────────
│  <b>PLEASE WAIT...</b>
│  <code>The restaurant is checking your order</code>
╰──────────────────
""",
    'keyboard_type': None,
    'state': None  # do something here
}