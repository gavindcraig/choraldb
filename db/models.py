from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class TagLabels(db.Model):
    """Labels for the tags"""
    id = db.Column(db.Integer,
                   primary_key=True)
    label = db.Column(db.String(64),
                      nullable=False)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('tag_categories.id'),
                            nullable=False)

    def __repr__(self):
        return '<Tag Label %r>' % self.id  # TODO: CATEGORY AND LABEL


class TagCategories(db.Model):
    """Categories for each tag label"""
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), nullable=False, unique=True)

    def __repr__(self):
        return '<Tag Category %r>' % self.category


class Tags(db.Model):
    """The actual tags"""
    id = db.Column(db.Integer, primary_key=True)
    work_id = db.Column(db.Integer,
                        db.ForeignKey('works.id'),
                        nullable=True)
    movement_id = db.Column(db.Integer,
                            db.ForeignKey('movements.id'),
                            nullable=True)
    label = db.Column(db.Integer,
                      db.ForeignKey('tag_labels.id'),
                      nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.id


class Works(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(256),
                      nullable=True)  # TODO: DEFAULT TO TEXT START OR NULL
    # library_id = db.Column()  # TODO
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.id'),
                        nullable=True)  # TODO
    composer_id = db.Column(db.Integer,
                            db.ForeignKey('people.id'),
                            nullable=True)
    arranger_id = db.Column(db.Integer,
                            db.ForeignKey('people.id'),
                            nullable=True)
    editor_id = db.Column(db.Integer,
                          db.ForeignKey('people.id'),
                          nullable=True)
    # publisher_id = db.Column()  # TODO
    product_no = db.Column(db.String(16),
                           nullable=True)
    voicing = db.Column(db.String(64),
                        nullable=True)
    key_start = db.Column(db.String(32),
                          nullable=True)
    key_end = db.Column(db.String(32),
                        nullable=True)
    page_no = db.Column(db.Integer,
                        nullable=True)
    len_pages = db.Column(db.Integer,
                          default=0)  # TODO: ADD DEFAULT VALUE
    len_duration = db.Column(db.Interval,
                             nullable=True)
    imslp_url = db.Column(db.String(256),
                          nullable=True)
    cpdl_url = db.Column(db.String(256),
                         nullable=True)
    text = db.Column(db.String(12287),
                     nullable=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('people.id'),
                          nullable=True)
    text_source = db.Column(db.String(1024),
                            nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    quantity = db.Column(db.Integer,
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Work %r>' % self.id


class Movements(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    work_id = db.Column(db.Integer,
                        db.ForeignKey('works.id'),
                        nullable=False)
    title = db.Column(db.String(256),
                      nullable=True)  # TODO: DEFAULT TO TEXT START OR NULL
    voicing = db.Column(db.String(64),
                        nullable=True)
    key_start = db.Column(db.String(32),
                          nullable=True)
    key_end = db.Column(db.String(32),
                        nullable=True)
    page_no = db.Column(db.Integer,
                        nullable=True)
    len_pages = db.Column(db.Integer,
                          default=0)  # TODO: ADD DEFAULT VALUE
    len_duration = db.Column(db.Interval,
                             nullable=True)
    text = db.Column(db.String(12287),
                     nullable=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('people.id'),
                          nullable=True)
    text_source = db.Column(db.String(1024),
                            nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Movement %r>' % self.id


class Books(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(256),
                      nullable=True)  # TODO: DEFAULT TO TEXT START OR NULL
    # library_id = db.Column()  # TODO
    editor_id = db.Column(db.Integer,
                          db.ForeignKey('people.id'),
                          nullable=True)
    # publisher_id = db.Column()  # TODO
    product_no = db.Column(db.String(16),
                           nullable=True)
    composer_id = db.Column(db.Integer,
                            db.ForeignKey('people.id'),
                            nullable=True)
    arranger_id = db.Column(db.Integer,
                            db.ForeignKey('people.id'),
                            nullable=True)
    author_id = db.Column(db.Integer,
                          db.ForeignKey('people.id'),
                          nullable=True)
    text_source = db.Column(db.String(1024),
                            nullable=True)
    len_pages = db.Column(db.Integer,
                          default=0)  # TODO: ADD DEFAULT VALUE
    imslp_url = db.Column(db.String(256),
                          nullable=True)
    cpdl_url = db.Column(db.String(256),
                         nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    quantity = db.Column(db.Integer,
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Work %r>' % self.id


class Libraries(db.Model):
    """Physical collections of scores"""
    id = db.Column(db.Integer,
                   primary_key=True)
    contents = db.Column(db.String(256),
                         nullable=False)
    location = db.Column(db.String(256),
                         nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Library %r>' % self.id


class People(db.Model):
    """All people (composers, editors, etc.)"""
    id = db.Column(db.Integer,
                   primary_key=True)
    name_full = db.Column(db.String(256),
                          nullable=False)
    birth_date = db.Column(db.Date,
                           nullable=True)
    birth_place = db.Column(db.String(256),
                            nullable=True)
    death_date = db.Column(db.Date,
                           nullable=True)
    death_place = db.Column(db.String(256),
                            nullable=True)
    wiki_url = db.Column(db.String(1024),
                         nullable=True)
    imslp_url = db.Column(db.String(1024),
                          nullable=True)
    cpdl_url = db.Column(db.String(1024),
                         nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Person %r>' % self.id


class Publishers(db.Model):
    """Information on publishing companies"""
    id = db.Column(db.Integer,
                   primary_key=True)
    co_name = db.Column(db.String(256),
                        nullable=False)
    city = db.Column(db.String(256),
                     nullable=True)
    url = db.Column(db.String(1024),
                    nullable=True)
    comments = db.Column(db.String(1024),
                         nullable=True)
    date_added = db.Column(db.Date,
                           default=datetime.now,
                           nullable=False)
    date_modified = db.Column(db.Date,
                              onupdate=datetime.now,
                              nullable=True)

    def __repr__(self):
        return '<Publisher %r>' % self.id


class Instruments(db.Model):
    """Instrument names for orchestration tags"""
    id = db.Column(db.Integer,
                   primary_key=True)
    abbreviation = db.Column(db.String(8),
                             nullable=True)
    name_full = db.Column(db.String(64),
                          nullable=False)

    def __repr__(self):
        return '<Instrument %r>' % self.id


class Orchestration(db.Model):
    """Tags for orchestration of accompaniment"""
    id = db.Column(db.Integer,
                   primary_key=True)
    work_id = db.Column(db.Integer,
                        db.ForeignKey('works.id'),
                        nullable=True)
    movement_id = db.Column(db.Integer,
                            db.ForeignKey('movements.id'),
                            nullable=True)
    instrument_id = db.Column(db.Integer,
                              db.ForeignKey('instruments.id'),
                              nullable=False)

    def __repr__(self):
        return '<Orchestration Tag %r>' % self.id
