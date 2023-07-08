# Translation API using deep learning

A simple web server that can run translation jobs quickly. This server can easily be extended to translate more languages, or add more options. Using FastAPI, we'll create a web server that exposes a /translate route and a /results route. Clients will post their translation request to the /translate route, and get the translation results from /results. The server will use a sqlite database to store the translations. On the backend, we'll use async and a pretrained deep learning language model to run the translation job.

## File overview:

- `requirements.txt` - packages you'll need to install
- `languages.txt` - list of languages that are supported for translation
- `main.py` - defines the web server routes
- `models.py` - defines database models
- `tasks.py` - runs our backend tasks, including the translation

## Installation

To follow this project, please install the following locally:

- Python 3.8+
- The packages defined in `requirements.txt`

## Run the Project

To run the server locally, run `uvicorn main:app --reload`.

## Data

During this project, we'll download a pretrained language model.

## Docker containerization

- `docker build -t dlapi .` to build the container.
- `docker run -d --name dlapi -p 80:80 dlapi` to run the container.
- `docker ps` to view the container information.
- Run `docker logs` to see logs from the container. You should see `Uvicorn running on http://0.0.0.0:80`. If you don't see this, wait a bit and try running `docker logs` again.
- Visit `127.0.0.1` or `localhost` to see the API server. Visit `localhost/docs` to see API docs.
- Run `docker stop dlapi` to stop the container.
- Run `docker rm dlapi` to remove the container.
