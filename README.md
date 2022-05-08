# URL Shortener
This application is a simple, minimalistic URL shortener that utilizes a package named Pyshorteners and TinyURL API. Just enter a URL into the field and submit, and it will return a JSON data containing the shortened version of the URL.

There are two endpoints:
* `/encode/<link-id>`: After clicking submit, the page will automatically redirect you to the JSON page with the ID of the link in the URL.
* `/decode/<link-id>`: replacing `<url-id` with the ID of the link you want to decode will give a JSON response containing the original url of the shortened version.

## Setup
1. Clone this repo into your local machine.
```
git clone https://github.com/jennytoc/url-shortener.git
```
2. Create a virtual environment.
```
python -m venv .venv
```
3. Activate the virtual environment
```
source .venv/bin/activate
```
4. Install requirements.txt.
```
pip install -r requirements.txt
```
* If terminal command fails, you may need to use `pip3 install -r requirements.txt` instead
5. Create a database. This application is using Postgresql.
```
createdb url_proj_db
```
* If you get an error like this: `Is the server running locally and accepting connections on that socket?` Run this command:
```
sudo service postgresql start
```
6. Migrate the models into your database.
```
python3 manage.py makemigrations
```
7. Run the migrate command.
```
python3 manage.py migrate
```
8. Finally, startup the server.
```
python3 manage.py runserver
```
9. Enter this into your browser to take you to the application.
```
http://127.0.0.1:8000/
```