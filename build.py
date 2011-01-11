#!/usr/bin/env python

import sys
import subprocess
import inspect
import os.path

from support import gencode
        
if __name__ == "__main__":
    try:
        from support import config
        pythonexe = config.interpreters.python
    except ImportError as ex:
        pythonexe = sys.executable
        
    gencodepy = inspect.getsourcefile(gencode)
    
    arguments = [pythonexe, gencodepy]
    arguments.extend(sys.argv[1:])
    
    #returncode = subprocess.call(arguments, executable = pythonexe)
    #sys.exit(returncode)
    
    os.execv(pythonexe, arguments)
        
    
