# -*- coding: utf-8 -*-

import sqlite3
import CommonConfigProcessor
import CommonDBProcessor
from flask import Flask
from flask import jsonify
from flask import make_response
from flask_httpauth import HTTPBasicAuth

###############################################################################


class DBHandler(CommonDBProcessor.CommonDBProcessor):
    """数据库操作"""

    def __init__(self, database):
        super(DBHandler, self).__init__(database)

    def get_asset(self):
        query = "SELECT * FROM asset"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_unknown(self):
        query = "SELECT * FROM unknown"
        self.cursor.execute(query)
        return self.cursor.fetchall()

##############################################################################


app = Flask(__name__)

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == confprocessor.get_username():
        return confprocessor.get_password()
    else: return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'results': 'Unauthorized access'}), 401)

@app.route('/', methods=['GET'])
def index():
    """Introduction of platform"""
    port = confprocessor.get_port()
    return u'''<html><head><title>欢迎使用资产责任人关系查询平台</title></head>
               <body><h1>本平台开放以下能力</h1>
               <ul>
               <li>查询能力：[get] https://x.x.x.x:%d/query</li>
               </ul>
               </body></html>
            ''' %(port)

@app.route('/query', methods=['GET'])
def query():
    """Introduction of query function"""
    port = confprocessor.get_port()
    return u'''<html><head><title>查询能力</title></head>
               <body><h1>【查询】能力提供以下API</h1>
               <ul>
               <li>资产责任人关系：[get] https://x.x.x.x:%d/query/relationship</li>
               </ul>
               </body></html>
            ''' %(port)

@app.route('/query/relationship', methods=['GET'])
@auth.login_required
def relationship():
    """Query all asset"""
    asset = DBHandler('relation.db').get_asset()
    results = []
    if asset:
        for ip, admin, description in asset:
            results.append(
                {'ip': ip, 'admin': admin, 'description': description})
    return jsonify({'results': results})

##############################################################################


if __name__ == '__main__':
    confprocessor = CommonConfigProcessor.CommonConfigProcessor(
        'config_relation.txt')
    app.run(
        host='0.0.0.0', port=confprocessor.get_port(), ssl_context='adhoc')

