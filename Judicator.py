import os
import time
import subprocess
import tempfile
import py_compile

filelist = os.listdir("/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs")
truetext = open("/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/Cancernipok.py","r").read()

for filename in filelist:

    filelist = os.listdir("/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs")

    filepath = "/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs/"+filename
    filetext = open(filepath,"r").read()

    statinfo = os.stat(filepath)
    filesize = statinfo.st_size

    truestatinfo = os.stat("/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/Cancernipok.py")
    truesize = truestatinfo.st_size

    if filesize != truesize:
        os.remove(filepath)
        continue

    elif filetext == truetext:
        os.remove(filepath)
        continue

    for checkfile in filelist:
        checkpath = "/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/TechnoCoreAIs/"+checkfile
        if checkpath != filepath:
            checktext = open(checkpath,"r").read()

            if filetext == checktext:
                os.remove(checkpath)
                continue
            continue
        continue
    testcode = subprocess.Popen(["python",filepath])
    testcode.terminate()
    if testcode.poll() and testcode.returncode != 0:
        os.remove(filepath)

    bashSort = "diff Cancernipok.py {0}".format(filepath)

    process = subprocess.Popen(bashSort.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    time.sleep(.05)
    try:
        process.terminate()
    except OSError:
        pass
    print output

    filediff = tempfile.NamedTemporaryFile("w", dir="/Users/jadtayl/Desktop/Advanced-Programming/TechnoCoreExperiment/Differences", delete=False)

    filediff.write(output)
    filediff.close()

    diffname = "Differences/diff"+filename

    os.rename(filediff.name,diffname)

    continue
