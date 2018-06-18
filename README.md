# Proj_i02





## Installation Instructions

1. Install [python] 2.7.10 or above, [git], [virtualenv], in your computer, if you don't have it already.

2. Get the source code on your machine via git.

    ```shell
    git clone https://github.com/ncs-jss/Proj_i02.git

    ```

3. Create a python virtual environment and install python dependencies.

    ```shell
    cd Proj_i02
    virtualenv venv
    source venv/bin/activate  # run this command everytime before working on project
    pip install requirements.txt
    ```

4. That's it. Now you can run development server at [http://127.0.0.1:8000]

    ```
    python manage.py runserver
    ```