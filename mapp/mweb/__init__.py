from flask import Blueprint, render_template

web = Blueprint('web', __package__)


@web.errorhandler(404)
def not_found(e):
    return render_template('404.html')

from mapp.mweb import book
from . import auth
from . import drift
from . import gift
from . import main
from . import wish


