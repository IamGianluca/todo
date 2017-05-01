import datetime
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from todo.models import Base, Board, State, Task, User


class TestDatabaseRelationship:

    def test_add(self, session, task):
        """The ORM object and the one retrieved from the database, after
        changes have been made permanent in the database, should be the same
        object.
        """
        session.add(task)
        session.commit()
        db_task = session.query(Task).filter_by(
            description='service road bike').first()
        assert db_task is task

    def test_add2(self, session, task):
        """Make sure the finalizer part of the *session* fixture was run, after
        the previous automated test.
        """
        session.add(task)
        session.commit()
        db_task = session.query(Task).filter_by(
            description='service road bike').first()
        assert db_task is task

    def test_empty_db(self, session):
        """The databases shouldn't include any record since in the *session*
        fixture's finalizer all tables are dropped.
        """
        result = session.query(Task).filter_by(
            description='service road bike').all()
        assert result == []

    def test_assign_author_to_task(self, session, task, user):
        """If a *User* object is assigned to a task and the *Task* object is
        made persistent, retrieving the same record from the database should
        guarantee the two *User* objects point to the same address in memory.
        """
        # given
        task.author = user
        session.add(task)
        session.commit()

        # when
        db_task = session.query(Task).filter_by(
            description='service road bike').first()

        # then
        assert db_task.author == user

    def test_lists_same_name_on_same_board(self, session, board, master):
        """An *IntegrityError* should be raised when trying to add to a *Board*
        a *State* with the same name of an existing one.
        """
        session.add(master)
        session.commit()
        with pytest.raises(IntegrityError):
            duplicate = State(name='master', board=board)
            session.add(duplicate)
            session.commit()

    def test_lists_same_name_on_different_boards(self, session, board, master):
        """It should be possible to create a *State* with identical name of
        another *State* but in a different *Board*.
        """
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

    def test_assign_author_to_board(self, session, hit, user):
        """If a *User* object is assigned to a board and the *Board* object is
        made persistent, retrieving the same record from the database should
        guarantee the two *User* objects point to the same address in memory.
        """
        # given
        hit.author = user
        session.add(hit)
        session.commit()

        # when
        db_state = session.query(State).filter_by(name='hit').first()

        # then
        assert db_state.author == user

    def test_add_task_to_state(self, session, hit, task):
        """If a *Task* object is assigned to a state and the relationship is
        made persistent in the database, retrieving the same record from the
        database should guarantee that the Task object is included in the list
        of tasks belonging to that board.
        """
        # given
        task.state = hit
        session.add(task)
        session.commit()

        # when
        db_state = session.query(State).filter_by(name='hit').first()

        # then
        assert task in db_state.tasks

    def test_remove_task_from_state(self, session, hit, task):
        """If task is removed from a state, and then chances are made permanent
        in the database, the *State* object retrieved from the database
        shouldn't include the given task in the list of task belonding to that
        state.
        """
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

    def test_assigning_a_list_to_task_state(self, session, hit, master, task):
        """The *Task* *state* attribute shouldn't be assigned to a list."""
        with pytest.raises(AttributeError):
            task.state = [hit, master]

    def test_assigning_multiple_states_to_task(self, session, hit, master,
                                               task):
        """A *Task* can't belong to more than one *State* at the same time. If
        a task is moved from one state to another, the previous state shouldn't
        hold any reference to that task.
        """
        # NOTE: in the *task* fixture, the default *State* is the hit list.
        # given 
        task.state = master
        session.add(task)
        session.commit()

        # when
        db_hit = session.query(State).filter_by(name='hit').first()
        db_master = session.query(State).filter_by(name='master').first()

        # then
        assert task not in db_hit.tasks
        assert task in db_master.tasks

    def test_move_task_to_another_state(self, session, hit, master, task):
        """If a *Task* is re-assigned to a new *State*, the database and the Python
        representation of the current environment should match.
        """
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
