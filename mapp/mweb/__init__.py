from flask import Blueprint

web = Blueprint('web', __package__)

from mapp.mweb import book
from . import auth
from . import drift
from . import gift
from . import main
from . import wish


