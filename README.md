http://45.118.133.192/home

With reference to: https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1

Read the docs!

Before running the app script, 
set the environment variable to the script file:

On Mac:`export FLASK_APP=SCRIPT_NAME.py`
On Windows:`set FLASK_APP=SCRIPT_NAME.py`

To run the app script: `flask run`

In debug mode, you don't have to close and re-start the web server to see the changes in the code.

Setting debug environment variable:
`export FLASK_DEBUG=1`

Alternatively, add in the following python code in SCRIPT_NAME.py:

```
if __name__ == "__main__":
    app.run(debug=True)

```

And use `python3 SCRIPT_NAME.py`

```
def home():
    return render_template("home.html", posts=posts)
```

The first `posts` in front of the "=" is used in the html files.

In HTML files, `{}` for code, `{{}}` for text.

To reduce repeating code in html, use inheritance.

bootstrap formatting: https://getbootstrap.com/docs/4.3/getting-started/introduction/#starter-template

`pip install flask-wtf`

`pip install email_validator`

cyber security, attack on websites

create the datebase, run the following in terminal:

```
from SCRIPT_NAME.py import db
db.create_all()
```

add date to datebase using command line:

```
from SCRIPT_NAME.py import User, Post
user_1 = User(username="Geralt", email="gor@witcher.com", password="silver")
db.session.add(user_1)
db.session.commit()
```

Command lines for SQLAlchemy:

```
User.query.add()
User.query.first()
User.query.filter_by(username="...").all()
User.query.filter_by(username="...").first()
```

```
>>>user = User.query.filter_by(username="...").first()
>>>user
User(...)
>>>user.id
1
>>>user.posts
[] (no posts for this user now)
>>> post_1 = Post(title="blog1", content="helloworld", user_id=user.id)
>>> post_2 = Post(title="blog2", content="hi again", user_id=user.id)
>>> db.session.add(post_1)
>>> db.session.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('blog1', '2020-05-02 07:25:53.398008'), Post('blog2', '2020-05-02 07:25:53.402143')]
>>> for post in user.posts:
...     print(post)
... 
Post('blog1', '2020-05-02 07:25:53.398008')
Post('blog2', '2020-05-02 07:25:53.402143')
>>> post.user_id
1
```

`backref` enables accessing attributes in "User" from "Post":
```
>>> post.author
User('Geralt', 'gor@witcher.com', 'default.jpg')
```

See the first 8 minutes for "circular import" problem: https://www.youtube.com/watch?v=44PvX0Yv368&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=5.

After refactoring the code, the current (simplified) structure is:
```
.
├── README.md
├── __pycache__
│   ├── flaskblog.cpython-37.pyc
│   └── forms.cpython-37.pyc
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── email_validator
│   ├── flask
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python -> python3
│   └── python3 -> /opt/anaconda3/bin/python3
├── flaskblog
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── htmltemp.html
├── include
├── lib
│   └── python3.7
│       └── site-packages
│              ......
│           (ignored 2000+ lines of site package directories)
│ 
├── pyvenv.cfg
├── run.py
```

To create the datebase after refactoring code:

```
from flashblog import db
from flashblog.models import User, Post
db.create_all()
```

After re-creating datebase, you can see the `site.db` is added in the `flaskblog` directory
as shown by the (simplified) structure tree:

```
.
├── README.md
├── __pycache__
│   ├── flaskblog.cpython-37.pyc
│   └── forms.cpython-37.pyc
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── email_validator
│   ├── flask
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python -> python3
│   └── python3 -> /opt/anaconda3/bin/python3
├── flaskblog
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── site.db
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── htmltemp.html
├── include
├── lib
│   └── python3.7
│       └── site-packages
│              ......
│           (ignored 2000+ lines of site package directories)
│ 
├── pyvenv.cfg
├── run.py

322 directories, 2343 files
```

Encrypt passwords:


`pip install flask-bcrypt`


```buildoutcfg
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash("testing")
```

Pagination:

```buildoutcfg
posts = Post.query.paginate(per_page=5)
```

Use environment variable to save passwords:

```buildoutcfg
nano .zprofile
export EMAIL_USER=""
export EMAIL_PASS=""
```

Restructure code using `Blueprint`:


```
.
├── README.md
├── __pycache__
│   ├── flaskblog.cpython-37.pyc
│   └── forms.cpython-37.pyc
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── email_validator
│   ├── flask
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python -> python3
│   ├── python3 -> /opt/anaconda3/bin/python3
│   └── wheel
├── flaskblog
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── config.cpython-37.pyc
│   │   └── models.cpython-37.pyc
│   ├── config.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   └── routes.cpython-37.pyc
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── forms.cpython-37.pyc
│   │   │   └── routes.cpython-37.pyc
│   │   ├── forms.py
│   │   └── routes.py
│   ├── site.db
│   ├── static
│   │   ├── main.css
│   │   └── profile_pics
│   │       ├── 2633c06f6bb51952.jpg
│   │       ├── 2e32b4c96a8d8f10.jpg
│   │       ├── 6248bbdcf193157d.png
│   │       ├── 7798432669b8b3ac.jpg
│   │       ├── 81e2a9a1c9f772ed.png
│   │       ├── 85ed1b444539873d.png
│   │       ├── b26b2b21cfb25d55.png
│   │       ├── b6e1c53325f88b74.png
│   │       └── default.jpg
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-37.pyc
│       │   ├── forms.cpython-37.pyc
│       │   ├── routes.cpython-37.pyc
│       │   └── utils.cpython-37.pyc
│       ├── forms.py
│       ├── routes.py
│       └── utils.py
├── htmltemp.html
├── include
├── pyvenv.cfg
└── run.py
```



### Setting up linux server:

1. Update:

    `apt update && apt upgrade`

2. Setting host name:

    Setting in system 
    
    `hostnamectl set-hostname SERVER HOSTNAME`
    
    Setting in host file:
    
    `nano /etc/hosts`
    
    Under local IP address, add in server IP address and IP name.
    
    ```
    LOCAL IP    LOCAL HOSTNAME
    SERVER IP   SERVER HOSTNAME 
    ```

3. add a user:
    
    `adduser USERNAME`
    
    `adduser USERNAME sudo`
    
    to check whether a use exists: https://linuxize.com/post/how-to-list-users-in-linux/
    
4. logout and log back in as new user:

    ```
    exit
    ssh USERNAME@IP
    ```
   
5. Setting up SSH keybase authentication:
    
    on linux server:
    
    `mkdir .ssh`
    
    on local machine:
    
    `ssh-keygen -b 4096`
    
    ``scp ~/.ssh/id_rsa.pub USERNAME@IP:~/.ssh/SAVED_FILE_NAME``

    After these, you should be able to see SAVED_FILE_NAME folded on you server by running `ls .ssh`.

6. Setting permissions:

    `sudo chmod 700 ~/.ssh/`
    
    `sudo chmod 600 ~/.ssh/*`
    
7. Then you can logout and log back in using ssh (without password)

8. Disallow route login using SSH:

    `sudo nano /etc/ssh/sshd_config`
    
    change to `PermitRootLogin yes` to `PermitRootLogin no`
    
    Find `PasswordAuthentication yes`, uncomment it, and change it to `PasswordAuthentication no`
    
    Then restart the server: `sudo systemctl restart sshd`
    
9. Setting up firewall:

    Install ufw: `sudo apt install ufw`
    
    `sudo ufw default allow outgoing`
    
    `sudo ufw default deny incoming`
    
    `sudo ufw allow ssh` (port 22 is ssh)
    
    `sudo ufw allow 5000`
    
    Implement all the settings above: `sudo ufw enable`
    
    Check the firewall status: `sudo ufw status`
    
generating `requirements.txt`: `pip freeze > requirements.txt`

transfer local repository to cloud server: `scp -r LOCAL_DIRECTORY USERNAME@IP:~/`

Setting up `.py` environment:

`sudo apt install python3-pip`

`sudo apt install python3-venv`

Then set up a virtual environment on Linux server:

```buildoutcfg
python3 -m venv flask/blog/venv
cd ~/flask/blog
```

And activate it: `source venv/bin/activate`

install dependencies from `requirements.txt`: `pip install -r requirements.txt`

create a config file:

`sudo touch /etc/config.json`

`sudo nano /etc/config.json`

edit the `config.py` file:

`sudo nano flaskblog/config.py`

in the file, add in:

```buildoutcfg
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

```

and change all the `os.environ.get()` to `config.get()`

Use `flask run` on server:

`export FLASK_APP=run.py`

`flask run --host=0.0.0.0`

Then you can see the webpage at `IP:5000`

Use `nginx` and `gunicorn` to host website and handle traffic.

`sudo apt install nginx`

`pip install gunicorn`


Configure:

`cd`

`sudo rm /etc/nginx/sites-enabled/default`

`sudo nano /etc/nginx/sites-enalbled/flaskblog`

Edit the config file for `nginx`:

```buildoutcfg
server {
    listen 80;
    server_name YOUR_IP_OR_DOMAIN;

    location /static {
        alias /home/YOUR_USER/YOUR_PROJECT/flaskblog/static;
    }

    location / {
        proxy_pass http://localhost:8000;
        include /etc/nginx/proxy_params;
        proxy_redirect off;
    }
}
```

and then:

`sudo ufw allow http/tcp`

`sudo ufw delete allow 5000`

`sudo ufw enable`

`sudo systemctl restart nginx`

*Take note, the operation sequence is important. You have to edit the configuration file for `nginx` first, and then edit firewall settings.*

The number of workers is (2 x num_cores) +1

number of cores: `nproc --all`

locate wo working directory: `cd ~/flask/blog`

`gunicorn -w 3 run:app`

Use `supervise` to constantly monitor `gunicorn`:

`sudo apt install supervisor`

`sudo nano /etc/supervisor/conf.d/flaskblog.conf`

edit the config file:

```buildoutcfg

[program:flaskblog]
directory=/home/YOUR_USER/YOUR_PROJECT
command=/home/YOUR_USER/YOUR_PROJECT/venv/bin/gunicorn -w 3 run:app
user=YOUR_USER
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/flaskblog/flaskblog.err.log
stdout_logfile=/var/log/flaskblog/flaskblog.out.log
```

create log files: 

`sudo mkdir -p /var/log/flaskblog`  (`-p` creates any the directories in the chain if none of them exists)

`sudo touch /var/log/flaskblog/flaskblog.err.log`

`sudo touch /var/log/flaskblog/flaskblog.out.log`

restart `supervisor`: `sudo supervisorctl reload`

and then everything should work!
