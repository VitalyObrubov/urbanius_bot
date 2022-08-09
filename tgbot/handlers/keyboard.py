from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, 
                     KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove)



def build_menu(keys: dict, columns: int):
    tg_keys = []
    keys_row = []       
    col = columns
    for key in keys:
        col-=1
        if type(keys[key]) == dict:
            btn_txt = keys[key]["label"]
            btn_type = keys[key]["type"]
        else:
            btn_txt = keys[key]
            btn_type = None
        if btn_type == "phone":
            keys_row.append(KeyboardButton(text=btn_txt,request_contact=True))
        else:
            keys_row.append(KeyboardButton(text=btn_txt))
        if col == 0:
            col = columns
            tg_keys.append(keys_row)
            keys_row = []
    if len(keys_row) > 0:
        tg_keys.append(keys_row)
    return tg_keys

def make_usual_keyboard(keys: dict, columns: int, header_buttons=None, footer_buttons=None):
    if len(keys) == 0:
        keyboard=ReplyKeyboardRemove()
    else:
        tg_keys = build_menu(keys, columns)
        if header_buttons:
            hed_bns = build_menu(header_buttons,len(header_buttons))
            tg_keys.insert(0,hed_bns[0])
        if footer_buttons:
            foot_bns = build_menu(footer_buttons,len(footer_buttons))
            tg_keys.append(foot_bns[0])
        keyboard = ReplyKeyboardMarkup(tg_keys, resize_keyboard=True)
    return keyboard

def build_menu_inline(keys: dict, columns: int):
    tg_keys = []
    keys_row = []       
    col = columns
    for key in keys:
        col-=1
        if type(keys[key]) == dict:
            btn_txt = keys[key]["label"]
            btn_type = keys[key]["type"]
        else:
            btn_txt = keys[key]
            btn_type = None
        if btn_type == "switch_inline":
            btn = InlineKeyboardButton(btn_txt, switch_inline_query_current_chat = "")
        else:
            btn = InlineKeyboardButton(btn_txt,callback_data=key)
        keys_row.append(btn)
        if col == 0:
            col = columns
            tg_keys.append(keys_row)
            keys_row = []
    if len(keys_row) > 0:
        tg_keys.append(keys_row)
    return tg_keys

def make_inline_keyboard(keys: dict, columns: int, header_buttons=None, footer_buttons=None):
    if len(keys) == 0:
        keyboard=InlineKeyboardMarkup([])
    else:
        tg_keys = build_menu_inline(keys, columns)
        if header_buttons:
            hed_bns = build_menu_inline(header_buttons,len(header_buttons))
            tg_keys.insert(0,hed_bns[0])
        if footer_buttons:
            foot_bns = build_menu_inline(footer_buttons,len(footer_buttons))
            tg_keys.append(foot_bns[0])
        keyboard = InlineKeyboardMarkup(tg_keys)
    return keyboard
    

def make_keyboard(keys: dict, type: str, columns: int, header_buttons=None, footer_buttons=None):

    if type == "usual":
        keyboard = make_usual_keyboard(keys, columns, header_buttons, footer_buttons)
    else:
        keyboard = make_inline_keyboard(keys, columns, header_buttons, footer_buttons)
    return keyboard


