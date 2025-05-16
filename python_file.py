from flask import Flask
import datetime

from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")
add_user("Silent", "Den", 42, "safety auditor", "integrated safety auditor of the ship", "module_3", "silent_den@mars.org")
add_user("Green", "Mel", 50, "doctor", "therapist", "module_1", "green_mel@mars.org")
add_user("Morgan", "Dexter", 35, "engineer", "engineer worker", "module_2", "morgan_dexter@mars.org")


def add_job(team_leader, job, work_size, collaborators, start_date, is_finished, end_date=datetime.datetime.now()):
    job_ = Jobs()
    job_.team_leader = team_leader
    job_.job = job
    job_.work_size = work_size
    job_.collaborators = collaborators
    job_.start_date = start_date
    job_.is_finished = is_finished
    if is_finished:
        job_.end_date = end_date
    db_sess = db_session.create_session()
    user_ = db_sess.query(User).filter(User.id == team_leader).first()
    job_.leader = user_
    user_.jobs_.append(job_)
    db_sess.add(job_)
    db_sess.commit()


add_job(1, "deployment of residential modules 1 and 2", 15, "2, 3", datetime.datetime.now(), False)


def main():
    app.run()


if __name__ == '__main__':
    main()