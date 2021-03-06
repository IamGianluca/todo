from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.schema import UniqueConstraint


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64))
    email = Column(String(120), unique=True, nullable=False)
    tasks = relationship('Task', back_populates='assignee')

    def __repr__(self):
        return '<User(username={}, email={})>'.format(self.username,
                                                      self.email)


class Board(db.Model):
    __tablename__ = 'board'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    states = relationship('State', back_populates='board')

    def __repr__(self):
        return '<Board(title={}, states={})>'.\
                format(self.title, self.states)


class State(db.Model):
    __tablename__ = 'state'

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    board_id = Column(Integer, ForeignKey('board.id'))
    board = relationship('Board', back_populates='states')
    tasks = relationship('Task', back_populates='state')
    __table_args__ = (UniqueConstraint('board_id', 'name'), )

    def __repr__(self):
        return '<State(name={}, board={})>'.format(self.name, self.board.title)


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    description = Column(Text)
    state_id = Column(Integer, ForeignKey('state.id'))
    state = relationship('State', back_populates='tasks')
    user_id = Column(Integer, ForeignKey('user.id'))
    assignee = relationship('User', back_populates='tasks')
    deadline = Column(Date)

    def as_dict(self):
        return {
            'id': self.id,
            'description': self.description
        }

    def __repr__(self):
        return '<Task(description={}, state={}, deadline={})>'.format(
            self.description, self.state, self.deadline)
