# 1.导包
from utils.mysql_conn import db


class User(db.Model):
    __tablename__ = "user_tbl"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键自增id')
    account = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return self.id


class Group(db.Model):
    __tablename__ = "group_tbl"
    # __table_args__ = (
    #     db.ForeignKeyConstraint(['create_user_id', 'update_user_id'], [User.id, User.id]),
    # )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键自增id')
    group_name = db.Column(db.String(100), nullable=False)
    create_user_id = db.Column(db.Integer)
    # create_user = db.relationship(User, backref=db.backref('group_create_user'))
    create_time = db.Column(db.DateTime, default=db.func.now())
    update_user_id = db.Column(db.Integer)
    # update_user = db.relationship(User, backref=db.backref('group_update_user'), overlaps='')
    update_time = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return self.id


class Record(db.Model):
    __tablename__ = "record_tbl"
    # __table_args__ = (
    #     db.ForeignKeyConstraint(['create_user_id'], [User.id]),
    #     db.ForeignKeyConstraint(['group_id'], [Group.id]),
    # )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键自增id')
    group_id = db.Column(db.Integer, nullable=False)
    # group = db.relationship(Group, backref=db.backref('record_group'))
    role = db.Column(db.String(100), nullable=False)
    record = db.Column(db.Text)
    create_user_id = db.Column(db.Integer)
    # create_user = db.relationship(User, backref=db.backref('record_create_user'))
    create_time = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return self.id


class RelationDeep(db.Model):
    __tablename__ = "relation_deep_tbl"
    # __table_args__ = (
    #     db.ForeignKeyConstraint(['user_id'], [User.id]),
    # )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键自增id')
    user_id = db.Column(db.Integer)
    # create_user = db.relationship(User, backref=db.backref('relation_deep_user'))
    deep_num = db.Column(db.Integer)

    def __repr__(self):
        return self.id


