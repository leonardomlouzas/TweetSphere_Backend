python -m venv venv;
source venv/bin/activate;
pip install --upgrade pip;
pip install -r requirements-dev.txt;
pip install -e .;
docker-compose build;
docker-compose up;