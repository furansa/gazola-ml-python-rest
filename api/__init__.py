import os
import sys

# Not sure if this is the best approach to solve package name resolution during
# tests execution, but solves by now
sys.path.append(os.getcwd())
