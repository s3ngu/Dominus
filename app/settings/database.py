from os import read
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import false
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def init_app(app: Flask):
    from environs import Env
    env = Env()
    env.read_env()
    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    ma.init_app(app)
    app.db = db
    from app.models.users_model import UsersModel
    from app.models.notices_model import NoticesModel
    from app.models.homes_model import HomesModel
    from app.models.poll_options_model import PollOptionsModel
    from app.models.polls_votes_model import PollsVotesModel
    from app.models.polls_model import PollsModel
    from app.models.events_categories_model import EventsCategoriesModel
    from app.models.events_invitations_model import EventsInvitationsModel
    from app.models.events_model import EventsModel
