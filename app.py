import os
import sys
import ssl
from flask import Flask, request, abort, jsonify, render_template
from models import setup_db, Singer, Song, db
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
from flask_migrate import Migrate


DEFAULT_OFFSET = 1
DEFAULT_LIMIT = 30
#get a list of paginated questions#
def paginate_results(request, selection):
      offset = request.args.get('offset', DEFAULT_OFFSET, type=int)
      limit = request.args.get('limit', DEFAULT_LIMIT, type=int)
      start =  (offset - 1) * limit
      end = start + limit

      formatted_selection = [item.format() for item in selection]
      paginated_selection = formatted_selection[start:end]

      return paginated_selection

#--------------------------------------------------------------------------------------#
def create_app(test_config=None):
    #create and configure the app#
    app = Flask(__name__, template_folder='page')
    setup_db(app)
    migrate = Migrate(app, db)
    CORS(app)
#--------------------------------------------------------------------------------------#
    #headers#
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
#--------------------------------------------------------------------------------------#
    #route to index page#
    @app.route('/')
    def index():
     return render_template('index.html')

#--------------------------------------------------------------------------------------#
    #route get/singers#
    @app.route('/singers', methods=['GET'])
    #require the 'get:singers' permission#
    @requires_auth('get:singers')
    #get singers#
    def get_singers(token):
       #query all singers#
       selection = Singer.query.all()
       singers_paginated = paginate_results(request, selection)

       if len(singers_paginated) == 0:
         abort(404,
            {
              'message': 'no singers found in database.'
            })

       return jsonify({
        'success': True,
        'status': 200,
        'singers': singers_paginated
    })

#--------------------------------------------------------------------------------------#
    #route get/songs#
    @app.route('/songs', methods=['GET'])
    #require the 'get:songs' permission#
    @requires_auth('get:songs')
    #get songs#
    def get_songs(token):
      #query all songs#
      selection = Song.query.all()
      songs_paginated = paginate_results(request, selection)

      if len(songs_paginated) == 0:
        abort(404,
         {'message': 'no songs found in database.'}
         )

      return jsonify({
        'success': True,
        'status': 200,
        'songs': songs_paginated
    })

#--------------------------------------------------------------------------------------#
#Now, create a post of singers and songs#
#--------------------------------------------------------------------------------------#
    #route post/singers post#
    @app.route('/singers', methods=['POST'])
    #require the 'post:singers'' permission#
    @requires_auth('post:singers')
    def create_singer(token):
          body = request.json
          name = body.get('name', None)
          age = body.get('age', None)
          gender = body.get('gender', None)
          idsinger = body.get('id_singer', None)

          #make sure there are no missing fields#
          if any(arg is None for arg in [name, age, gender, idsinger]) or '' in [name, age, gender, idsinger]:

          #abort 400 if any fields are missing#
             abort(400, 'name, age and gender and idsinger are required fields :( Please fill it out ^ـ^')

          #create a new Singer and insert#
          new_singer = Singer(name=name, age=age, gender=gender, id_singer=idsinger )
          new_singer.insert()

          #returns the Singer who was created a little while ago#
          return jsonify({
          'success': True,
          'status': 200,
          'singers': [Singer.query.get(new_singer.id).format()]

    })

#--------------------------------------------------------------------------------------#
    #route post/songs post#
    @app.route('/songs', methods=['POST'])
    #require the 'post:songs' permission#
    @requires_auth('post:songs')
    def create_song(token):
      body = request.json
      title = body.get('title', None)
      release_date = body.get('release_date', None)

      #make sure there are no missing fields#
      if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
        #abort 400 if any fields are missing#
        abort(400, 'title and release_date are required fields :( Please fill it out ^ـ^')

      #create a new Song and insert#
      new_song = Song(title=title, release_date=release_date)
      new_song.insert()

      #returns the Song who was created a little while ago#
      return jsonify({
         'success': True,
         'status': 200,
         'songs': [Song.query.get(new_song.id).format()]
    })
#--------------------------------------------------------------------------------------#
#Now, create a delete of singers and songs#
#--------------------------------------------------------------------------------------#
    #route delete/singerid#
    @app.route('/singers/<singerid>', methods=['DELETE'])
    #require the 'delete:singerid' permission#
    @requires_auth('delete:singers')
    #get delete singer#
    def delete_singer(token, singerid):
         singer = Singer.query.get(singerid)

         #abort 404 if the singer was not found#
         if singer is None:
          abort(404)

         #delete the singer#
         singer.delete()

         return jsonify({
          'success': True,
          'status': 200,
          'delete': singerid
    })

#--------------------------------------------------------------------------------------#
    #route delete/songid#
    @app.route('/songs/<songid>', methods=['DELETE'])
    #require the 'delete:songs' permission#
    @requires_auth('delete:songs')
    #get delete song#
    def delete_song(token, songid):
        song = Song.query.get(songid)

        #abort 404 if the Song was not found#
        if song is None:
         abort(404)

        #delete the Song#
        song.delete()

        return jsonify({
         'success': True,
         'status': 200,
         'delete': songid
    })

#--------------------------------------------------------------------------------------#
#Now, create a patch of singers and songs#
#--------------------------------------------------------------------------------------#
    #route /singers id patch#
    @app.route('/singers/<singerid>', methods=['PATCH'])
    #require the 'patch:singers' permission#
    @requires_auth('patch:singers')
    #get patch singer#
    def update_singer(token, singerid):
       singer = Singer.query.get(singerid)

       #abort 404 if the Singer was not found#
       if singer is None:
         abort(404)

       body = request.json
       name = body.get('name', None)
       age = body.get('age', None)
       gender = body.get('gender', None)
       idsinger = body.get('id_singer', None)

       #make sure there are no missing fields#
       if any(arg is None for arg in [name, age, gender, idsinger]) or '' in [name, age, gender, idsinger]:
         #abort 400 if any fields are missing#
         abort(400, 'name, age and gender are required fields.')

       #update the Singer with the requested fields#
       singer.name = name
       singer.age = age
       singer.gender = gender
       singer.id_singer = idsinger
       singer.update()
       #return the updated Singer#
       return jsonify({
         'success': True,
         'status': 200,
         'singers': [Singer.query.get(singerid).format()]
    })

#--------------------------------------------------------------------------------------#
    #route /song id patch#
    @app.route('/songs/<songid>', methods=['PATCH'])
    #require the 'patch:songs' permission#
    @requires_auth('patch:songs')
    #get patch song#
    def update_song(token, songid):
       song = Song.query.get(songid)
       #abort 404 if the Song was not found#
       if song is None:
         abort(404)

       body = request.json
       title = body.get('title', None)
       release_date = body.get('release_date', None)

       #make sure there are no missing fields#
       if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
        #abort 400 if any fields are missing#
        abort(400, 'title and release_date are required fields.')

       #update the Song with the requested fields#
       song.title = title
       song.release_date = release_date
       song.update()

       #return the updated Song#
       return jsonify({
        'success': True,
        'status': 200,
        'songs': [Song.query.get(songid).format()]
    })
#--------------------------------------------------------------------------------------#
#Now, Error Handling#
#--------------------------------------------------------------------------------------#
    #bad request#
    #errorhandler whenCheck the body request and status code 400#
    @app.errorhandler(400)
    def bad_request(error):
      return jsonify({
        "success": False,
        "error": 400,
        "message": str(error)
    }), 400
#--------------------------------------------------------------------------------------#
    #not found#
    #errorhandler when resource not found and status code 404#
    @app.errorhandler(404)
    def not_found_error(error):
      return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found."
    }), 404
#--------------------------------------------------------------------------------------#
    #unprocessable entity#
    #errorhandler when unprocessable and status code 422#
    @app.errorhandler(422)
    def unprocessable(error):
      return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable."
    }), 422
#--------------------------------------------------------------------------------------#
    #implement error handler for AuthError#
    #errorhandler#
    @app.errorhandler(AuthError)
    def handle_auth_error(e):
      #receive the raised authorization error and propagates it as response#
      response = jsonify(e.error)
      response.status_code = e.status_code
      return response

    return app


app = create_app()

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
