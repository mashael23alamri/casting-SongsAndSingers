# SONGS
Songs API designs company responsible for song creation and management, hiring singers for those songs.
This API is responsible for checking permissions and handling CRUD for singer and song model.

#Working App:
To view the production app it can be accessed from https://singersandsongs.herokuapp.com/ Currently there is a simple front end but it is not yet working. However, it can be used via the API endpoints mentioned in this readme.
![web](../master/page/img/web.jpg)

## let's start
### Installing Dependencies

1-Follow the instructions to install the latest version of Python [here](https://www.python.org/downloads/release/python-380/)
###### In this API I used a version Python 3.8.0

2-PIP Dependencies
install dependencies by naviging to the root directory of this project and running:

###### Frist:

```bash
pip3 freeze > requirements.txt
```
###### Secondly:

```bash
pip3 install -r requirements.txt
```
3-Virtual Enviornment
You have to work in a virtual environment when using Python for projects. This keeps your dependencies for each project separate and organized.

4-After installing the dependencies, execute the bash file config.py to set the user jwts, auth0 credentials and the remote database url.

#Local Development:

1-app.py
2-models.py
3-congfig.py
4-test_app.py


### Running the server
From within the root directory first ensure you are working using your created virtual environment.

To run the server(http://127.0.0.1:5000), execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
 -Note: You may get an error SSL: CERTIFICATE_VERIFY_FAILED,[You will find the solution here](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)


### To test the code:

go to the root directory of this project and , simply run the test_app.py by typing:
![web](../master/page/img/test.jpg)
## Best Practices for REST API Error Handling
-400: Bad Request.
-404: Resource Not Found.
-422: Unprocessable.
... etc.
[here](https://www.baeldung.com/rest-api-error-handling-best-practices)


### Hosting Instructions:
simply follow below steps to have the code ready to be deployed in the Heroku cloud service [here](https://classroom.udacity.com/nanodegrees/nd0044-connect/parts/faa5e5c6-65b5-4d89-b085-83273a34018a/modules/5a12cd8b-c106-4a27-bfc2-83fb5748d144/lessons/22de0129-9744-4580-894b-a9cfd1083375/concepts/ba5b80c9-aae9-42bd-98cf-9faddade53e6)
###Endpoints (APIs):
##### Note: Replace {token} with an actual one for the curl command to work:
There are three roles in the company,
1-Assistant Casting
Permissions:
 -Get/Singers
   curl http://127.0.0.1:5000/singers -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```bash
   {
  "singers": [
    {
      "age": 34,
      "gender": "female",
      "id": 2,
      "id_singer": 2,
      "name": "Lady Gaga"
    },
    {
      "age": 25,
      "gender": "female",
      "id": 3,
      "id_singer": 3,
      "name": "Justin Drew Bieber"
    },
    {
      "age": 32,
      "gender": "female",
      "id": 4,
      "id_singer": 7,
      "name": "Adele Laurie Blue Adkins"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 7,
      "id_singer": 10,
      "name": "Taylor Alison Swift"
    },
    {
      "age": 33,
      "gender": "male",
      "id": 8,
      "id_singer": 11,
      "name": "Jesse McCartney"
    },
    {
      "age": 31,
      "gender": "female",
      "id": 11,
      "id_singer": 13,
      "name": "Sean Kingston"
    },
    {
      "age": 31,
      "gender": "female",
      "id": 10,
      "id_singer": 13,
      "name": "Sean Kingston"
    },
    {
      "age": 34,
      "gender": "female",
      "id": 12,
      "id_singer": 6,
      "name": "Lady Gaga"
    },
    {
      "age": 42,
      "gender": "male",
      "id": 1,
      "id_singer": 1,
      "name": "Kanye west"
    },
    {
      "age": 27,
      "gender": "female",
      "id": 5,
      "id_singer": null,
      "name": "Demetria Devonne Lovato"
    }
  ],
  "status": 200,
  "success": true
}
```
 -GET/Songs
  curl http://127.0.0.1:5000/songs -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
 ```bash
 {
   "songs": [
     {
       "id": 1,
       "release_date": "Wed, 18 Dec 2019 13:17:17 GMT",
       "title": " I love it"
     },
     {
       "id": 3,
       "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
       "title": "  love yourself"
     },
     {
       "id": 4,
       "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
       "title": "  love yourself"
     },
     {
       "id": 5,
       "release_date": "Wed, 18 Dec 2019 13:17:17 GMT",
       "title": " 10,000 hours"
     },
     {
       "id": 6,
       "release_date": "Sat, 18 Dec 2010 13:17:17 GMT",
       "title": "  one time"
     },
     {
       "id": 7,
       "release_date": "Fri, 18 Dec 2015 13:17:17 GMT",
       "title": " Hello"
     },
     {
       "id": 9,
       "release_date": "Mon, 18 Dec 2017 13:17:17 GMT",
       "title": " wolves"
     },
     {
       "id": 11,
       "release_date": "Sat, 18 Dec 2004 13:17:17 GMT",
       "title": "  beautiful soul"
     },
     {
       "id": 12,
       "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
       "title": "  filthy blues"
     },
     {
       "id": 13,
       "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
       "title": "  beat it"
     },
     {
       "id": 10,
       "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
       "title": "love story"
     },
     {
       "id": 14,
       "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
       "title": "Rian on Me"
     },
     {
       "id": 2,
       "release_date": "Wed, 02 Oct 2019 09:22:00 GMT",
       "title": "Rain On Me"
     }
   ],
   "status": 200,
   "success": true
 }
 ```

 When using endpoints other than GET, the result will be
 ### EX:
  curl -X POST -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"name":"Celina", "age":23, "gender":"female", "id_singer":1}' http://127.0.0.1:5000/singers
 ```bash
 {
  "code": "unauthorized",
  "description": "Permission denied."
 }
 ```


2-Director Casting
Permissions:
-Get/Singers
  curl http://127.0.0.1:5000/singers -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```bash
  {
 "singers": [
   {
     "age": 34,
     "gender": "female",
     "id": 2,
     "id_singer": 2,
     "name": "Lady Gaga"
   },
   {
     "age": 25,
     "gender": "female",
     "id": 3,
     "id_singer": 3,
     "name": "Justin Drew Bieber"
   },
   {
     "age": 32,
     "gender": "female",
     "id": 4,
     "id_singer": 7,
     "name": "Adele Laurie Blue Adkins"
   },
   {
     "age": 30,
     "gender": "female",
     "id": 7,
     "id_singer": 10,
     "name": "Taylor Alison Swift"
   },
   {
     "age": 33,
     "gender": "male",
     "id": 8,
     "id_singer": 11,
     "name": "Jesse McCartney"
   },
   {
     "age": 31,
     "gender": "female",
     "id": 11,
     "id_singer": 13,
     "name": "Sean Kingston"
   },
   {
     "age": 31,
     "gender": "female",
     "id": 10,
     "id_singer": 13,
     "name": "Sean Kingston"
   },
   {
     "age": 34,
     "gender": "female",
     "id": 12,
     "id_singer": 6,
     "name": "Lady Gaga"
   },
   {
     "age": 42,
     "gender": "male",
     "id": 1,
     "id_singer": 1,
     "name": "Kanye west"
   },
   {
     "age": 27,
     "gender": "female",
     "id": 5,
     "id_singer": null,
     "name": "Demetria Devonne Lovato"
   }
 ],
 "status": 200,
 "success": true
}
```
-GET/Songs
 curl http://127.0.0.1:5000/songs -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
```bash
{
  "songs": [
    {
      "id": 1,
      "release_date": "Wed, 18 Dec 2019 13:17:17 GMT",
      "title": " I love it"
    },
    {
      "id": 3,
      "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
      "title": "  love yourself"
    },
    {
      "id": 4,
      "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
      "title": "  love yourself"
    },
    {
      "id": 5,
      "release_date": "Wed, 18 Dec 2019 13:17:17 GMT",
      "title": " 10,000 hours"
    },
    {
      "id": 6,
      "release_date": "Sat, 18 Dec 2010 13:17:17 GMT",
      "title": "  one time"
    },
    {
      "id": 7,
      "release_date": "Fri, 18 Dec 2015 13:17:17 GMT",
      "title": " Hello"
    },
    {
      "id": 9,
      "release_date": "Mon, 18 Dec 2017 13:17:17 GMT",
      "title": " wolves"
    },
    {
      "id": 11,
      "release_date": "Sat, 18 Dec 2004 13:17:17 GMT",
      "title": "  beautiful soul"
    },
    {
      "id": 12,
      "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
      "title": "  filthy blues"
    },
    {
      "id": 13,
      "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
      "title": "  beat it"
    },
    {
      "id": 10,
      "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
      "title": "love story"
    },
    {
      "id": 14,
      "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
      "title": "Rian on Me"
    },
    {
      "id": 2,
      "release_date": "Wed, 02 Oct 2019 09:22:00 GMT",
      "title": "Rain On Me"
    }
  ],
  "status": 200,
  "success": true
}
```
 -Post/Singer
  curl -X POST -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"name":"Celina", "age":23, "gender":"female", "id_singer":1}' http://127.0.0.1:5000/singers
 ```bash
 {
  "singers": [
    {
      "age": 23,
      "gender": "female",
      "id": 14,
      "id_singer": 1,
      "name": "Celina"
    }
  ],
  "status": 200,
  "success": true
}
```
 -Patch/Singer
 curl -X PATCH -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"name":"Celina", "age":26, "gender":"female", "id_singer":1}' http://127.0.0.1:5000/singers/1
 ```bash
 {
   "singers": [
     {
       "age": 26,
       "gender": "female",
       "id": 1,
       "id_singer": 1,
       "name": "Celina"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -Patch/Songs
 curl -X PATCH -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"title":"good for you", "release_date":"20120618 10:00:09 PM"}' http://127.0.0.1:5000/songs/1
 ```bash
 {
   "songs": [
     {
       "id": 1,
       "release_date": "Mon, 18 Jun 2012 22:00:09 GMT",
       "title": "good for you"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -Delete/Singer
  curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {token}" http://127.0.0.1:5000/singers/5
 ```bash
 {
   "delete": "5",
   "status": 200,
   "success": true
 }
```

 When using endpoints Delete/Songs or Post/Songs, the result will be
 ### EX:
 curl -X POST -H "Authorization: Bearer{token}" -H "Content-Type: application/json" -d '{"title":"good for you", "release_date":"20120618 10:34:09 AM"}' http://127.0.0.1:5000/songs
 ```bash
 {
   "code": "unauthorized",
   "description": "Permission denied."
 }


3-Executive Producer
Permissions:
 -Get/songs
 curl http://127.0.0.1:5000/songs -H "Authorization: Bearer {token}" -H "Content-Type: application/json"

 ```bash
 {
   "songs": [
     {
       "id": 3,
       "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
       "title": "  love yourself"
     },
     {
       "id": 4,
       "release_date": "Sun, 18 Dec 2016 13:17:17 GMT",
       "title": "  love yourself"
     },
     {
       "id": 5,
       "release_date": "Wed, 18 Dec 2019 13:17:17 GMT",
       "title": " 10,000 hours"
     },
     {
       "id": 6,
       "release_date": "Sat, 18 Dec 2010 13:17:17 GMT",
       "title": "  one time"
     },
     {
       "id": 7,
       "release_date": "Fri, 18 Dec 2015 13:17:17 GMT",
       "title": " Hello"
     },
     {
       "id": 9,
       "release_date": "Mon, 18 Dec 2017 13:17:17 GMT",
       "title": " wolves"
     },
     {
       "id": 11,
       "release_date": "Sat, 18 Dec 2004 13:17:17 GMT",
       "title": "  beautiful soul"
     },
     {
       "id": 12,
       "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
       "title": "  filthy blues"
     },
     {
       "id": 13,
       "release_date": "Wed, 18 Dec 2013 13:17:17 GMT",
       "title": "  beat it"
     },
     {
       "id": 10,
       "release_date": "Wed, 06 Oct 2021 08:22:00 GMT",
       "title": "love story"
     },
     {
       "id": 14,
       "release_date": "Thu, 01 Oct 2020 04:22:00 GMT",
       "title": "Rian on Me"
     },
     {
       "id": 2,
       "release_date": "Wed, 02 Oct 2019 09:22:00 GMT",
       "title": "Rain On Me"
     },
     {
       "id": 1,
       "release_date": "Mon, 18 Jun 2012 22:00:09 GMT",
       "title": "good for you"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -GET/Singers
 curl http://127.0.0.1:5000/songs -H "Authorization: Bearer {token}" -H "Content-Type: application/json"
 ```bash
 {
   "singers": [
     {
       "age": 34,
       "gender": "female",
       "id": 2,
       "id_singer": 2,
       "name": "Lady Gaga"
     },
     {
       "age": 25,
       "gender": "female",
       "id": 3,
       "id_singer": 3,
       "name": "Justin Drew Bieber"
     },
     {
       "age": 32,
       "gender": "female",
       "id": 4,
       "id_singer": 7,
       "name": "Adele Laurie Blue Adkins"
     },
     {
       "age": 30,
       "gender": "female",
       "id": 7,
       "id_singer": 10,
       "name": "Taylor Alison Swift"
     },
     {
       "age": 33,
       "gender": "male",
       "id": 8,
       "id_singer": 11,
       "name": "Jesse McCartney"
     },
     {
       "age": 31,
       "gender": "female",
       "id": 11,
       "id_singer": 13,
       "name": "Sean Kingston"
     },
     {
       "age": 31,
       "gender": "female",
       "id": 10,
       "id_singer": 13,
       "name": "Sean Kingston"
     },
     {
       "age": 34,
       "gender": "female",
       "id": 12,
       "id_singer": 6,
       "name": "Lady Gaga"
     },
     {
       "age": 27,
       "gender": "female",
       "id": 5,
       "id_singer": null,
       "name": "Demetria Devonne Lovato"
     },
     {
       "age": 23,
       "gender": "female",
       "id": 13,
       "id_singer": 1,
       "name": "Celina"
     },
     {
       "age": 23,
       "gender": "female",
       "id": 14,
       "id_singer": 1,
       "name": "Celina"
     },
     {
       "age": 23,
       "gender": "female",
       "id": 15,
       "id_singer": 1,
       "name": "Celina"
     },
     {
       "age": 26,
       "gender": "female",
       "id": 1,
       "id_singer": 1,
       "name": "Celina"
     }
   ],
   "status": 200,
   "success": true
 }
```
 _Post/Singers
 curl -X POST -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"name":"Shakira", "age":43, "gender":"female", "id_singer":3}' http://127.0.0.1:5000/singers
 ```bash
 {
   "singers": [
     {
       "age": 43,
       "gender": "female",
       "id": 16,
       "id_singer": 3,
       "name": "Shakira"
     }
   ],
   "status": 200,
   "success": true
 }
```
 _Post/Songs
 curl -X POST -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"title":"Loca", "release_date":"20120618 10:34:09 AM"}' http://127.0.0.1:5000/songs
 ```bash
 {
   "songs": [
     {
       "id": 15,
       "release_date": "Mon, 18 Jun 2012 10:34:09 GMT",
       "title": "Loca"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -Patch/Singers
 curl -X PATCH -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"name":"Shakira", "age":44, "gender":"female", "id_singer":1}' http://127.0.0.1:5000/singers/1
 ```bash
 {
   "singers": [
     {
       "age": 44,
       "gender": "female",
       "id": 1,
       "id_singer": 1,
       "name": "Shakira"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -Patch/Songs
 curl -X PATCH -H "Authorization: Bearer {token}" -H "Content-Type: application/json" -d '{"title":"Loca", "release_date":"20220518 7:00:09 PM"}' http://127.0.0.1:5000/songs/1
 ```bash
 {
   "songs": [
     {
       "id": 1,
       "release_date": "Wed, 18 May 2022 19:00:09 GMT",
       "title": "Loca"
     }
   ],
   "status": 200,
   "success": true
 }
```
 -Delete/Singers
 curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {token}" http://127.0.0.1:5000/singers/4
 ```bash
 {
   "delete": "4",
   "status": 200,
   "success": true
 }
```
 -Delete/Songs
 curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer {token}" http://127.0.0.1:5000/songs/1
 ```bash
 {
   "delete": "1",
   "status": 200,
   "success": true
 }
```

### Authentication:

1-"assistant_casting":

 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpsYWh6ajhZM2twd2wzYjZZNE0yQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jYXBzdG9uZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzMzFiMjQzYWNkMGUwMDNhMWEwYWU1IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk3ODk1NzM5LCJleHAiOjE1OTc5NDYxMzksImF6cCI6Im8zWUpybVQ3VkRnTmRYVUp4TGNtOUZRM0ZPR3NoVzJaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6c2luZ2VycyIsImdldDpzb25ncyJdfQ.sqJ2FhekzIfhrpA9r6JiJAwPX9vk34gRSFbw-X7wEeI_NIxtsYb9QbK8Riq739l0pfkwCR4U0-cZ8fSnmXr7hjTUWcl3tUbJX6sq2t9qaqwseFVBC1jZJlRpR2NB6nuggqd8dHkEdwFnd43JnOtmu4kCRNIN3RkYbG60RQzXxGdxw1lqTbBSVNDMtcSJSsPrE51K89kluRA4FHCCId87pVv0FyU-CnZLaLUfZw8XnUWirLnaIp3jy1TUMl_v5cuGcTzRzQQnJ8iYYntG6QlQsUP6i5BFl2I4WNNzvZyqJhgGt60V4E_SeSdHopKlHjuERZhgvNH5hxQvn_E5cDGSPQ

2-"director_casting":

  eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpsYWh6ajhZM2twd2wzYjZZNE0yQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jYXBzdG9uZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNjljOWNmZTQ1MjcwMDZkOTMxNDgxIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk3ODk1ODMxLCJleHAiOjE1OTc5NDYyMzEsImF6cCI6Im8zWUpybVQ3VkRnTmRYVUp4TGNtOUZRM0ZPR3NoVzJaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6c2luZ2VycyIsImdldDpzaW5nZXJzIiwiZ2V0OnNvbmdzIiwicGF0Y2g6c2luZ2VycyIsInBhdGNoOnNvbmdzIiwicG9zdDpzaW5nZXJzIl19.HOjYR6FKxnbsCYGI0L_BL9gyJe_SZWgfP9VnVMyFJqzdqJmcF0o59u-nXkZkp0xVl_8OGipbxBtEt3_4wg-RgNW_Fes5_04lN0N0fAzFECETTEMbOyGmDI3OqHrhKQGwJYQ2MTR6Zf0_jLQ2X80iKGgd_Xzznykfjo0GjyIzd_6_hQm3Xo0NKFE4-1sqzBNXnPlKU8r9vVad5LQYRntgLLx6Fp2nsMzaxxBMyerxZB6bBh_CJHv32l-_oT8hjGeP1-9cUkb3pSgaLBf35zghwCnO_C2_EJvSZqvDc_jinKa9SC-LkqTTDdAMJ81u_F0qBFcWYDXPVVUk__MTs1-WGw

3-"executive_producer":

 eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpsYWh6ajhZM2twd2wzYjZZNE0yQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1jYXBzdG9uZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzMzFjZjA2OGRlOTkwMDM3NDcxMTI4IiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiaWF0IjoxNTk3ODk1ODk5LCJleHAiOjE1OTc5NDYyOTksImF6cCI6Im8zWUpybVQ3VkRnTmRYVUp4TGNtOUZRM0ZPR3NoVzJaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6c2luZ2VycyIsImRlbGV0ZTpzb25ncyIsImdldDpzaW5nZXJzIiwiZ2V0OnNvbmdzIiwicGF0Y2g6c2luZ2VycyIsInBhdGNoOnNvbmdzIiwicG9zdDpzaW5nZXJzIiwicG9zdDpzb25ncyJdfQ.FYNEPxs5FXYShlLZeL-632bhQ7COPyeAzD6OHrMlVdgAdkvWX7aIKDUARV5ASb7a-PFu0C6c2bg5EHEvfzmIWMcEjBA-tn_Rzt06cOl8TS2wKgi6YrYJ1s5kMBLQK52brV76vfdaIifdqI0j2eTLwU7MUPKUxICY5pkfG_kTyYRswiiA8qmIEWIvp0FunFFOnyFiwp7O93sutToQHa9YOUIHD_-0lhLHv7vGG0ZWgn3ktb0VKnXTuNHSZBnVXlCou5DnFkQFSCZmJtQ2cv96Gbkj940IJI4yJGFc4BLyoYX2Gb5tbRhn0IPs7gkAnp721JsZMxwMQwH2P8U177HPwg

### References
1- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

2- [SSL: CERTIFICATE_VERIFY_FAILED](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)

3- [https://jwt.io/](https://jwt.io/)

4- [sql](https://www.w3schools.com/sql/default.asp)

5- [SQLAlchemy](https://www.sqlalchemy.org/)

6- [heroku](https://www.heroku.com)

7- [Best Practices for REST API Error Handling](https://www.baeldung.com/rest-api-error-handling-best-practices)
