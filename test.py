import os
from os.path import join, dirname

#dotenv_path = join(dirname(__file__) )
dotenv_path = join(dirname(__file__), '../.env')
print(str(dotenv_path))
