import datetime
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from todo.models import Base, Board, State, Task, User


class TestDatabaseRelationship:

    def test_uncommitted_add(self, session, task):
        session.add(task)
        session.commit()
        db_task = session.query(Task).filter_by(
            description='service road bike').first()
        assert db_task is task

    def test_uncommitted_add2(self, session, task):
        session.add(task)
        session.commit()
        db_task = session.query(Task).filter_by(
            description='service road bike').first()
        assert db_task is task

    def test_empty_db(self, session):
        result = session.query(Task).filter_by(
            description='service road bike').all()
        assert result == []

    def test_task_author(self, session, task, user):
        task.author = user
        session.add(task)
        session.commit()

        # when
        db_task = session.query(Task).filter_by(
            description='service road bike').first()

        # then
        assert db_task.author == user

    def test_lists_same_name_on_same_board(self, session, board, master):
        session.add(master)
        session.commit()
        with pytest.raises(IntegrityError):
            duplicate = State(name='master', board=board)
            session.add(duplicate)
            session.commit()

    def test_lists_same_name_on_different_boards(self, session, board, master):
        # given
        session.add(master)
        session.commit()

        new_board = Board(title='new board')
        duplicate = State(name='master', board=new_board)
        session.add(duplicate)
        session.commit()

        # when
        db_states = session.query(State).filter_by(name='master').all()

        # then
        assert len(db_states) == 2
        assert master in db_states
        assert duplicate in db_states

    def test_note_author(self, session, hit, user):
        # given
        hit.author = user
        session.add(hit)
        session.commit()

        # when
        db_note = session.query(State).filter_by(name='hit').first()

        # then
        assert db_note.author == user

    def test_add_task_to_note(self, session, hit, task):
        # given
        task.note = hit
        session.add(task)
        session.commit()

        # when
        db_state = session.query(State).filter_by(name='hit').first()

        # then
        assert task in db_state.tasks

    def test_remove_task_from_note(self, session, hit, task):
        # given
        hit.tasks.append(task)
        session.add(hit)
        session.commit()

        # when
        hit.tasks.remove(task)
        session.add(hit)  # should this be automated?

        # then
        result = session.query(State).filter_by(name='hit').first()
        assert task not in result.tasks

    def test_move_task_to_another_note(self, session, hit, master, task):
        # given
        hit.tasks.append(task)
        session.add(hit)
        session.commit()
        assert task in hit.tasks
        assert task not in master.tasks

        # when
        task.state = master
        session.add(task)
        session.commit()

        # then
        db_hit = session.query(State).filter_by(name='hit').first()
        assert task not in db_hit.tasks

        db_master = session.query(State).filter_by(name='master').first()
        assert task in db_master.tasks
