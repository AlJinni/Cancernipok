import subprocess
import os
import time
import tempfile
import py_compile

filelist = os.listdir("/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs")

selftext = open(__file__,"r").read()

for filename in filelist:
    newfile = "/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs/"+filename
    try:
        testcode = py_compile.compile(file=newfile, doraise=True)
    except py_compile.PyCompileError:
        os.remove(newfile)
        continue
    deletepath = "/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs/"+filename+"c"
    os.remove(deletepath)
    #newmed = tempfile.NamedTemporaryFile("w", dir="/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/Mediators", delete=False)

    #newmed.write(selftext)
    #newmed.close()

    #subprocess.Popen(["python", newmed.name])

#subprocess.Popen(["python", __file__])
