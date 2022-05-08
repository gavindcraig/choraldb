from flask_sqlalchemy import SQLAlchemy
from .defaults.instruments import def_instruments
from .defaults.lectionary import def_tec_lect
from .defaults.tags import def_cats, def_char_tags, def_lit_tags, def_occ_tags


def yesno(prompt: str):
    y = ['yes', 'y', 'yep', 'true', 't']
    n = ['no', 'n', 'nope', 'false', 'f']

    while True:
        ans = input(prompt + '\n')
        if ans.lower() in y:
            return True
        elif ans.lower() in n:
            return False
        else:
            print('Please type [Y]es or [N]o')


def setup_all(db: SQLAlchemy):
    if yesno('Add default tag categories?'):
        def_cats(db)
        if yesno('Add default tags?'):
            def_lit_tags(db)
            def_char_tags(db)
            def_occ_tags(db)
        if yesno('Add default Episcopal lectionary tags?'):
            def_tec_lect(db)
    if yesno('Add default instrument list?'):
        def_instruments(db)
