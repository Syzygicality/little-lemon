# little-lemon
The capstone project for Meta's Back-End Developer Certificate. Although, the instructions called for using mysqlclient, this Capstone project uses mysql-connector-python instead, as it was much easier to use when working in a GitHub Codespace.

For peer reviewers:

Once you have cloned this repo, please activate your virtual environment. Afterwards:
- cd workspace/littlelemon/
- pip install -r requirements.txt

Visit 127.0.0.1:8000/restaurant/ to view static content

Additionally, test the following API endpoints in your REST client:
- 127.0.0.1:8000/auth/token/login
- 127.0.0.1:8000/auth/users/
- 127.0.0.1:8000/auth/users/me/
- 127.0.0.1:8000/auth/token/logout
- 127.0.0.1:8000/restaurant/menu
- 127.0.0.1:8000/restaurant/menu/(insert primary key of item)
- 127.0.0.1:8000/restaurant/booking/tables

Thank you, and have a nice day!