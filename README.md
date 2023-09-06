# timestamp
Creating password reset tokens based on username and time stamp with different patterns

# installation
- git clone https://github.com/legend-of-bugs/timestamp.git
- cd timestamp
- pip install -r requirements.txt

# Usage
- python3 timestamp.py -u USERNAME1 -s SECONDS
- python3 timestamp.py -u USERNAME1,USERNAME2 -s SECONDS
  - USERNAME = your username or email (You can enter multiple usernames with `,` separator)
  - SECONDS = The amount of seconds you want the tool to create a hash for you based on the timestamp
 
# Change Pattern
- Open the `pattern.json` files and modify the patterns as you want and need
  - Note that the `$USERNAME` and `$TIMESTAMP` values are fixed and you should not change their letters
