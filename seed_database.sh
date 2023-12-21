   #!/bin/bash

   rm db.sqlite3
   rm -rf ./triad/migrations
   python3 manage.py migrate
   python3 manage.py makemigrations triad
   python3 manage.py migrate triad
   python3 manage.py loaddata users types ingredients
