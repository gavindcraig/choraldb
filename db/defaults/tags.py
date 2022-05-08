from ..models import TagCategories, TagLabels
from flask_sqlalchemy import SQLAlchemy


def def_cats(db: SQLAlchemy):
    """Default tag categories"""
    cats = ['Lectionary',
            'Season',
            'Part of Liturgy',
            'Characteristics',
            'Occasion',
            ]
    for cg in cats:
        db.session.add(TagCategories(category=cg))
    db.session.commit()


def def_lit_tags(db: SQLAlchemy):
    """Default tags for parts of liturgy"""
    tags = ['Introit',
            'Offertory',
            'Communion', ]
    for t in tags:
        db.session.add(TagLabels(label=t, category_id=3))
    db.session.commit()


def def_char_tags(db: SQLAlchemy):
    """Default tags for musical characteristics"""
    tags = ['Soft',
            'Slow',
            'Fast',
            'Loud', ]
    for t in tags:
        db.session.add(TagLabels(label=t, category_id=4))
    db.session.commit()


def def_occ_tags(db: SQLAlchemy):
    """Default tags for occasions"""
    tags = ['Baptism',
            'Confirmation',
            'Matrimony',
            'Funeral',
            'Dedication Festival',
            'Secular',
            'Patriotic']
    for t in tags:
        db.session.add(TagLabels(label=t, category_id=5))
    db.session.commit()
