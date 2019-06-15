from flask import Blueprint

web = Blueprint('web', __package__)

from mapp.mweb import book


