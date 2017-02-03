import sys
import os
from generate_list import printIt

cwd = os.getcwd()

sys.path.append(cwd)
for x in (0,1000):
    printIt()