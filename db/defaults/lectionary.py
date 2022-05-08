from flask_sqlalchemy import SQLAlchemy
from ..models import TagLabels
from dataclasses import dataclass, field
from roman import toRoman


@dataclass
class Observance:
    season: str = None
    week: int = None
    title: str = None
    form: str = None
    year: str = None
    variable: bool = True

    def __str__(self) -> str:
        if self.year:
            return self.str_year()
        else:
            return self.str_no_year

    def str_year(self):
        if self.title:
            return '{0} {1}'.format(self.title,
                                    self.year)
        else:
            return self.form.format(self.season,
                                    toRoman(self.week),
                                    self.year)

    def str_no_year(self):
        if self.title:
            return self.title
        else:
            return self.form.format(self.season,
                                    toRoman(self.week))


@dataclass
class Season:
    title: str
    weeks: int
    form: str
    alt: dict = field(default_factory=dict)
    observances: list = field(default_factory=list)
    variable: bool = True

    def __post_init__(self) -> None:
        if self.variable:
            year = ['A', 'B', 'C']
        else:
            year = ['ABC']
        for w in range(self.weeks):
            for y in year:
                self.create_obs(w+1, y)

    def create_obs(self, w, y):
        """Create an observance and add it to self.observances"""
        try:
            alt_title = self.alt[w]
        except KeyError:
            alt_title = None
        obs = Observance(season=self.title,
                         week=w,
                         year=y,
                         variable=self.variable,
                         form=self.form,
                         title=alt_title,
                         )

        self.observances.append(obs)


def def_tec_lect(db: SQLAlchemy):
    """Default tags for the RCL as used by the Episcopal Church"""
    advent = Season(title='Advent',
                    weeks=4,
                    form='{0} {1} {2}',
                    alt={3: 'Gaudete'})
    christmastide = Season(title='Christmas',
                           weeks=2,
                           form='{1} after {0}',
                           variable=False)
    epiphanytide = Season(title='Epiphany',
                          weeks=9,
                          form='{1} after {0} {2}',
                          alt={9: 'Last after Epiphany'})
    lent = Season(title='Lent',
                  weeks=5,
                  form='{0} {1} {2}',
                  alt={4: 'Laetare'})
    easter = Season(title='Easter',
                    weeks=8,
                    form='{0} {1} {2}',
                    alt={1: 'Easter Day',
                         2: 'Low Sunday',
                         4: 'Shepherd Sunday',
                         8: 'Whisunday'})
    whitsun = Season(title='Pentecost',
                     weeks=29,
                     form='Proper {1} {2}',
                     alt={29: 'Christ the King'})

    lectionary = (advent.observances +
                  list('Christmas') +
                  christmastide.observances +
                  list('Epiphany') +
                  epiphanytide.observances +
                  lent.observances +
                  ['Maundy Thursday',
                   'Good Friday',
                   'Holy Saturday'] +
                  easter.observances +
                  ['Trinity Sunday A',
                   'Trinity Sunday B',
                   'Trinity Sunday C'] +
                  whitsun.observances +
                  ['St. Andrew',
                   'St. Thomas',
                   'St. Stephen',
                   'St. John',
                   'Holy Innocents',
                   'Confession of St. Peter',
                   'Conversion of St. Paul',
                   'The Presentation',
                   'St. Matthias',
                   'St. Joseph',
                   'The Annunciation',
                   'St. Mark',
                   'Ss. Phillip and James',
                   'The Visitation',
                   'St. Barnabas',
                   'Nativity of St. John Baptist',
                   'Ss.Peter and Paul',
                   'American Independence Day',
                   'St. Mary Magdalene',
                   'St. James',
                   'The Transfiguration',
                   'St. Mary the Virgin',
                   'St. Bartholomew',
                   'Holy Cross',
                   'St. Matthew',
                   'Michaelmas',
                   'St. Luke',
                   'St. James of Jerusalem',
                   'Ss. Simon and Jude',
                   "All Saints' A",
                   "All Saints' B",
                   "All Saints' C",
                   'Thanksgiving Day A',
                   'Thanksgiving Day B',
                   'Thanksgiving Day C']
                  )

    for o in lectionary:
        db.session.add(TagLabels(label=str(o), category_id=1))
    seasons = ['Advent',
               'Christmastide',
               'Epiphanytide',
               'Lent',
               'Eastertide',
               'Whitsuntide']
    for s in seasons:
        db.session.add(TagLabels(label=s, category_id=2))
    db.session.commit()
