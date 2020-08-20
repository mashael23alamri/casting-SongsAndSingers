import os
import json
import unittest
from app import create_app, paginate_results
from config import bearer_tokens
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from models import setup_db, Singer, Song


#bearer_tokens#
assistant_casting = {'Authorization': bearer_tokens['assistant_casting']}
director_casting = {'Authorization':  bearer_tokens['director_casting']}
executive_producer = {'Authorization': bearer_tokens['executive_producer']}


#this class represponseents the casting agency test case#
class CastingAgency(unittest.TestCase):
 #define test variables and initialize app#
 def setUp(self):
    self.app = create_app()
    self.client = self.app.test_client
    self.database_name = "capstone_test"
    self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
    setup_db(self.app, self.database_path)

    self.new_singer = {
      'name': 'John Doe',
      'age': 20,
      'gender': 'Male'
    }

    self.new_singer_2 = {
      'name': 'Nate',
      'age': 20,
      'gender': 'Male'
    }

    self.update_singer = {
      'name': 'Claire',
      'age': 20,
      'gender': 'Female'
    }

    self.new_song = {
      'title': 'Avengers 2',
      'release_date': '2021-10-1 04:22'
    }

    self.new_song_2 = {
      'title': 'Avengers 4',
      'release_date': '2021-10-1 04:22'
    }

    self.update_song = {
      'title': 'Toy Story 12',
      'release_date': '2021-10-1 04:22'
    }

    #binds the app to the current context#
    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)

      #create all tables#
      self.db.create_all()

 def tearDown(self):
    pass
#--------------------------------------------------------------------------------------#
#Now, success behavior tests#
#--------------------------------------------------------------------------------------#

 #test get singers#
 def test_get_singers (self):
    response = self.client().get('/singers', headers=assistant_casting )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertTrue(len(data['singers']) >= 0)
 #--------------------------------------------------------------------------------------#
 #test get songs#
 def test_get_songs (self):
    response = self.client().get('/songs', headers=assistant_casting )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['songs']))
 #--------------------------------------------------------------------------------------#
 #test create singers#
 def test_create_singers (self):
    response = self.client().post('/singers', json=self.new_singer, headers=director_casting )
    data = json.loads(response.data)
 #--------------------------------------------------------------------------------------#
 #test create songs#
 def test_create_songs (self):
    response = self.client().post('/songs', json=self.new_song, headers=executive_producer )
    data = json.loads(response.data)
 #--------------------------------------------------------------------------------------#
 #test update singers#
 def test_update_singers (self):
    self.client().post('/singers', json=self.new_singer, headers=executive_producer )
    response = self.client().patch('/singers/', json=self.update_singer, headers=executive_producer )
    data = json.loads(response.data)
 #--------------------------------------------------------------------------------------#
 #test update songs#
 def test_update_songs (self):
    self.client().post('/songs', json=self.new_song, headers=director_casting )
    response = self.client().patch('/songs/', json=self.update_song, headers=director_casting )
    data = json.loads(response.data)

 #--------------------------------------------------------------------------------------#
 #test delete singers#
 def test_delete_singers (self):
    self.client().post('/singers', json=self.new_singer, headers=executive_producer )
    self.client().post('/singers', json=self.new_singer_2, headers=executive_producer )
    response = self.client().delete('/singers/5', headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['delete'], '5')
 #--------------------------------------------------------------------------------------#
 #test delete songs#
 def test_delete_songs (self):
    self.client().post('/songs ', json=self.new_song, headers=executive_producer )
    self.client().post('/songs ', json=self.new_song_2, headers=executive_producer )
    response = self.client().delete('/songs/6', headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(data['delete'], '6')
 #--------------------------------------------------------------------------------------#
   #Error behavior tests#
 #--------------------------------------------------------------------------------------#
 def test_401_get_singers (self):
    response = self.client().get('/singers')
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)
 #--------------------------------------------------------------------------------------#
 def test_401_get_songs (self):
     response = self.client().get('/songs')
     data = json.loads(response.data)
     self.assertEqual(response.status_code, 401)
 #--------------------------------------------------------------------------------------#
 def test_401_create_singers (self):
    response = self.client().post('/singers', json=self.new_singer)
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)
 #--------------------------------------------------------------------------------------#
 def test_401_create_songs (self):
    response = self.client().post('/songs', json=self.new_song)
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 401)
 #--------------------------------------------------------------------------------------#
 def test_404_update_singers (self):
    response = self.client().patch('/singers/1000', json=self.update_singer, headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)
 #--------------------------------------------------------------------------------------#
 def test_404_update_songs (self):
    response = self.client().patch('/songs/1000', json=self.update_song, headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------#
 def test_404_delete_singers (self):
    response = self.client().delete('/singers/1000', headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)
#--------------------------------------------------------------------------------------#
 def test_404_delete_songs(self):
    response = self.client().delete('/songs/1000', headers=executive_producer )
    data = json.loads(response.data)
    self.assertEqual(response.status_code, 404)



 if __name__ == "__main__":
  unittest.main()
