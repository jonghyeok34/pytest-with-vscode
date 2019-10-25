0. directory
    ```
    - .vscode
        - settings.json
    - app
        - services
    - tests
        - services
    - venv
    - requirements.txt
    ```

1. setting.json 설정 
    ```javascript
    {
	    
	    "python.pythonPath": "./venv/bin/python", // python path
	    "python.venvPath": "venv", // virtual env path
	    "python.testing.pytestPath": "./venv/bin/py.test", // pytest path
	    "python.linting.flake8Enabled": true,
	    "python.linting.enabled": true,
	    "python.testing.unittestEnabled": false,
	    "python.testing.nosetestsEnabled": false,
	    "python.testing.pytestEnabled": true,
	    "extensions.autoUpdate": false,
	    "python.testing.pytestArgs": [
	        "."
	    ],
	}

    ```

2. virtual env 설정
    - virtual env 생성

    ```console
    foo@bar:/path$ python3 -m venv venv
    ```

    - virtual env activate
    ```console
    foo@bar:/path$ source venv/bin/activate
    ``` 

    - 
    ```console
    (venv) foo@bar:/path$ pip install -r requirements.
    ```
    requirements.txt에는 pytest 포함
    ```
    pytest
    ``` 
    - reload 
    ctrl+shif+p --> Developer Reload Window

    - virtual env 자동 설정
        - 자동 설정이 되지 않을 경우
        

3. setting 설정 (http://doc.pytest.org/en/latest/goodpractices.html)
    - file tree
    ```
    - .vscode
        - settings.json
    - app
        - services
    - tests
        - services
    - venv
    - requirements.txt
    - setting.py
    ```

    - setting.py
    PROJECTNAME = 저장될 이름
    ```python
    from setuptools import setup, find_packages

    setup(name="PROJECTNAME", packages=find_packages())
    ```

    - project module 생성
    ```
    (venv) foo@bar:/path$ pip install --editable .
    ```

    - window reload
    ctrl+shif+p --> Developer Reload Window