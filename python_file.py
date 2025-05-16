from flask import Flask

from data import db_session
from data.users import User
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()

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
    db_sess.commit()


add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")
add_user("Silent", "Den", 42, "safety auditor", "integrated safety auditor of the ship", "module_3", "silent_den@mars.org")
add_user("Green", "Mel", 50, "doctor", "therapist", "module_1", "green_mel@mars.org")
add_user("Morgan", "Dexter", 35, "engineer", "engineer worker", "module_2", "morgan_dexter@mars.org")


def main():
    app.run()


if __name__ == '__main__':
    main()