__author__ = "smrati.katiyar@gmail.com"

from flask.blueprints import Blueprint
from flask import request,jsonify

wr = Blueprint('hello', __name__, url_prefix='/hello/v1.0')

@wr.route('/test',methods=['GET'])
def test():
	return jsonify({'status':'success'})