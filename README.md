### Installation Steps

Follow these steps to set up the Dockerized Django application:

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>

2.**Build and Run Docker:**
  ```bash
  docker-compose up --build

3.**Access the Application:**
 
 Open your web browser or postman(recommended) and go to http://127.0.0.1:8000/ or http://0.0.0.0:8000/ to access the application.


4:**Postman Collection:**
  ```json
      {
	"info": {
		"_postman_id": "e2c7c355-98a8-40b1-b517-e6533ee978fe",
		"name": "Social Media",
		"description": "API collection for a social media app",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "25173500"
	},
	"item": [
		{
			"name": "Register User",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"fullname\": \"new user\",\n    \"email\": \"newuser@gmail.com\",\n    \"password\":\"password123\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/register/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"register",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "User Login",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"email\":\"newuser@gmail.com\",\n    \"password\":\"password123\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/login/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"login",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Search Name",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDAwMDEyLCJpYXQiOjE3MTc5OTk3MTIsImp0aSI6IjVlMTUwNGFmYWFjMTRhNThhZGVmZDE3NWNkYzdmYmJkIiwidXNlcl9pZCI6OH0.hF41eEFgAS9T7CdFjFlzpplRJz2Qk_wUj0NWFYeu8Dg",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/search?name=user",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"search"
					],
					"query": [
						{
							"key": "name",
							"value": "user"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "Search Email",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "Send Friend Request",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDAwNDQ4LCJpYXQiOjE3MTgwMDAxNDgsImp0aSI6IjcyMTg0M2EzMWE1YTRlM2NhMjM4YzMwZjdiMTJjNTNhIiwidXNlcl9pZCI6OH0.pN6qA4oexIqjdbfbyXxBtUttH1Es4N7MKXOLPjYzqec",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDAwMDEyLCJpYXQiOjE3MTc5OTk3MTIsImp0aSI6IjVlMTUwNGFmYWFjMTRhNThhZGVmZDE3NWNkYzdmYmJkIiwidXNlcl9pZCI6OH0.hF41eEFgAS9T7CdFjFlzpplRJz2Qk_wUj0NWFYeu8Dg"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"sender\":8,\n    \"receiver\": 3\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/friends/send/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"friends",
						"send",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Accept Friend Request",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDAzMjY2LCJpYXQiOjE3MTgwMDI5NjYsImp0aSI6IjIwODIzYzBhZGMyNDQzODQ4N2NlYjNhYTllMDJmODQzIiwidXNlcl9pZCI6OH0.XSqzvgLGbmV9hAgCl89tMLhz9D8v9MtZtmY1nPvq88Q",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDAwNDQ4LCJpYXQiOjE3MTgwMDAxNDgsImp0aSI6IjcyMTg0M2EzMWE1YTRlM2NhMjM4YzMwZjdiMTJjNTNhIiwidXNlcl9pZCI6OH0.pN6qA4oexIqjdbfbyXxBtUttH1Es4N7MKXOLPjYzqec"
					},
					{
						"key": "Content-Type",
						"value": "application/json"
					}
				],
				"body": {
					"mode": "raw",
					"raw": ""
				},
				"url": {
					"raw": "http://127.0.0.1:8000/friends/accept/9/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"friends",
						"accept",
						"9",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Reject Friend Request",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDA5OTU2LCJpYXQiOjE3MTgwMDk2NTYsImp0aSI6Ijc2NzNkMGMzZDVkYTQ2OWY4MmY1ODdkNTNhMGE2YzIyIiwidXNlcl9pZCI6OH0.501jgJpC4qBzJWaN9fbQTKBq6y9V628cd1at--Nib9E",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/friends/reject/10/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"friends",
						"reject",
						"10",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Pending Request",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDA5OTU2LCJpYXQiOjE3MTgwMDk2NTYsImp0aSI6Ijc2NzNkMGMzZDVkYTQ2OWY4MmY1ODdkNTNhMGE2YzIyIiwidXNlcl9pZCI6OH0.501jgJpC4qBzJWaN9fbQTKBq6y9V628cd1at--Nib9E",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/friends/pending/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"friends",
						"pending",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "List Friends",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MDA5OTU2LCJpYXQiOjE3MTgwMDk2NTYsImp0aSI6Ijc2NzNkMGMzZDVkYTQ2OWY4MmY1ODdkNTNhMGE2YzIyIiwidXNlcl9pZCI6OH0.501jgJpC4qBzJWaN9fbQTKBq6y9V628cd1at--Nib9E",
							"type": "string"
						}
					]
				},
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/friends/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"friends",
						""
					]
				}
			},
			"response": []
		}
	]
}
