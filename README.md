# pytest vscode 에서 사용하기( WSL/ virtual env 같이 사용 할 시)

0. remote wsl 다운 후 wsl로 시작
   - ![](/img/0-1.png)
   - ![](/img/0-2.png)
   - ![](/img/0-3.png)

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
       "python.testing.pytestEnabled": true,
       "python.testing.pytestArgs": [
            "-v",
            "-p",
            "no:cacheprovider",
            "test_*.py",
            "-s"
        ]
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

   - [requirements.txt]

   ```
   pytest
   ```

   - install pytest

   ```console
   (venv) foo@bar:/path$ pip install -r requirements.txt
   ```

   - reload

     - <kbd>ctrl</kbd>+<kbd>shif</kbd>+<kbd>p</kbd>
     - Developer: Reload Window

   - 재실행 할 경우 virtual env 자동 실행이 된다.
     - 자동 실행이 되지 않을 경우
     - virtual env activate
     ```console
     foo@bar:/path$ source venv/bin/activate
     ```

3. 해당 에러 해결 해야함.
    - 

    ```
    ModuleNotFoundError: No module named 'app'
    ```

    1. 방법 1 = setup.py 설정
        setting 설정 (http://doc.pytest.org/en/latest/goodpractices.html)

        - file tree

        ```
            - .vscode
                - settings.json
            - app
                - services
                - __init__.py
            - tests
                - services
                - __init__.py
            - setup.py
            
        ```

        - setup.py

        ```python
        from setuptools import setup, find_packages

        setup(name="PROJECTNAME", packages=find_packages())
        ```

        PROJECTNAME = 저장될 이름

        - project module 생성
        해당 디렉토리에 경로 패키지 install:

        ```console
        (venv) foo@bar:/path/app$ pip install -e .
        ```

        - file tree

        ```
        - .vscode
            - settings.json
        - app
            - services
            - setup.py
        - tests
            - services
        - venv
        - PROJECTNAME
            - dependency_links.txt
            - PKG-INFO
            - SOURCES.txt
            - top_level.txt
        - requirements.txt
        ```

    2. 방법 2 = .bashrc 설정

    
        - 해당 디렉토리 찾기
        
        ```
        (venv) foo@bar:/path/$ pwd
        /path
        ```
        - bashrc 수정
        ```console
        (venv) foo@bar:/path/$ cd ~
        (venv) foo@bar:~$ vim .bashrc 
        ```

        - 해당 디렉토리의 app 경로 추가후 bashrc 실행
        ```vim
        export PYTHONPATH="/path/app"
        ```
        ```
        (venv) foo@bar:~$ source .bashrc 
        ```
    
   - reload
     - <kbd>ctrl</kbd>+<kbd>shif</kbd>+<kbd>p</kbd>
     - Developer: Reload Window

    

4. pytest.ini 설정 - 해당 mark 등록(https://docs.pytest.org/en/latest/mark.html)

   - warning 메시지 없애기

   ```
   is this a typo?  You can register custom marks to avoid this warning
   ```

   - file 구조

   ```
    - .vscode
        - settings.json
    - app
        - services
    - tests
        - services
            -test_calc_service.py
    - venv
    - requirements.txt
    - setup.py
    - pytest.ini
   ```

   - pytest.ini 파일 ( service) python test 파일에 등록된 mark 이름과 설명

   ```ini
   [pytest]
   markers =
       service: default service
   ```

   - test_calc_service.py

   ```python
   @pytest.mark.service
   def test_add1():

       number = 1
       assert calc_service.add1(number) == 2
   ```


5. output 보기
   - ![](/img/1.png)
   - ![](/img/2.png)
   - ![](/img/3.png)
