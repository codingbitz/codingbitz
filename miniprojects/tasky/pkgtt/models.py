from pkgtt import db
from datetime import datetime, date
from sqlalchemy.types import Date
ts_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(ts_1)


# Creating model table for our CRUD database

class Blearn(db.Model):
    __table__name = 'blearn'
    learn_id = db.Column(db.Integer, primary_key=True)
    learn_date = db.Column(db.String(50), nullable=False)
    learn_start_time = db.Column(db.String(50), nullable=False)
    learn_end_time = db.Column(db.String(50), nullable=True)
    area_of_study = db.Column(db.String(200), nullable=False)
    sub_area = db.Column(db.String(200), nullable=False)
    completion_status = db.Column(db.String(100), nullable=False)
    learning_src = db.Column(db.String(1000), nullable=False)
    brief_desc = db.Column(db.String(3000), nullable=False)
    comments = db.Column(db.String(3000), nullable=False)
    code_practice_link = db.Column(db.String(3000), nullable=False)
    audit_ts = db.Column(db.String(50), default=ts_1)

    def __init__(self, learn_date, learn_start_time, learn_end_time, area_of_study, sub_area, completion_status,
                 learning_src, brief_desc, comments, code_practice_link):
        self.learn_date = learn_date
        self.learn_start_time = learn_start_time
        self.learn_end_time = learn_end_time
        self.area_of_study = area_of_study
        self.sub_area = sub_area
        self.completion_status = completion_status
        self.learning_src = learning_src
        self.brief_desc = brief_desc
        self.comments = comments
        self.code_practice_link = code_practice_link

    def __repr__(self):
        return '<Learning details %r %r %r %r %r %r %r %r %r %r>' % (self.learn_date,
                                                                     self.learn_start_time,
                                                                     self.learn_end_time,
                                                                     self.area_of_study,
                                                                     self.sub_area,
                                                                     self.completion_status,
                                                                     self.learning_src,
                                                                     self.brief_desc,
                                                                     self.comments,
                                                                     self.code_practice_link)