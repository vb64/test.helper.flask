# Class for autotests flask python apps
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/test.helper.flask/pep257.yml?label=Pep257&style=plastic&branch=main)](https://github.com/vb64/test.helper.flask/actions?query=workflow%3Apep257)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/test.helper.flask/py2.yml?label=Python%202.7&style=plastic&branch=main)](https://github.com/vb64/test.helper.flask/actions?query=workflow%3Apy2)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/vb64/test.helper.flask/py3.yml?label=Python%203.7-3.10&style=plastic&branch=main)](https://github.com/vb64/test.helper.flask/actions?query=workflow%3Apy3)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/7b91398bad9f4f3db99b727f3b225d6b)](https://app.codacy.com/gh/vb64/test.helper.flask/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7b91398bad9f4f3db99b727f3b225d6b)](https://app.codacy.com/gh/vb64/test.helper.flask/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

## Install
```bash
pip install tester_flask
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

```bash
git clone git@github.com:vb64/test.helper.flask.git
cd test.helper.flask
```

With Python 2

```bash
make setup2 PYTHON_BIN="/path/to/python2
```

With Python 3

```bash
make setup PYTHON_BIN="/path/to/python3
```

Then

```bash
make tests
```
