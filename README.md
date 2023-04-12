# Class for autotests flask python apps

## Install
```bash
$ pip install tester_flask
```

## Usage in tests

```python
from flask import Flask
from tester_flask import TestFlask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return "Flask OK"


@app.route('/redirect', methods=['POST'])
def redirect_page():
    return redirect(url_for('main_page'))


class TestFlaskApp(TestFlask):

    def setUp(self):
        TestFlask.setUp(self, app)

    def test_app(self):
        assert self.simple_view('main_page').status_code == 200
        assert self.param_post('main_page', {'hello': 1}, {'one': 1}).status_code == 200

        response = self.simple_post('redirect_page', {'one': 1}, follow=False)
        assert self.final_url(response) == self.get_url('main_page')

```

## Development
```
$ git clone git@github.com:vb64/test.helper.flask.git
$ cd test.helper.flask
```

With Python 2.7
```
$ make setup PYTHON_BIN="/path/to/python2.7 -m virtualenv"
```

With Python 3
```
$ make setup PYTHON_BIN="/path/to/python3.7 -m venv"
```

Then
```
$ make tests
```
