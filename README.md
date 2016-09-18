# flask-nginx-uwsgi-fabric
All we need for flask app is "$ fab go" (python fabric3 for distribution script)

---

## useage
```bash
  $ virtualenv venv
  $ source venv/bin/activate
  $ (venv) pip install -r requirements.txt
  $ fab go
```

## env
- Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Script, PyMySQL
- uwsgi, nginx
- python3, fabric3
- tested on AWS ubuntu 14.04 LTS
