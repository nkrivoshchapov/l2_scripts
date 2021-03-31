import os, sys, subprocess, time, random, ntpath
rank = int(sys.argv[1])
proc=14

from distutils.dir_util import copy_tree
from shutil import rmtree
try:
    rmtree("/dev/shm/g16sse")
except:
    pass
copy_tree("./g16sse", "/dev/shm/g16sse")
from shutil import copy2
copy2("./Mg16.x", "/dev/shm/")
try:
    rmtree("/dev/shm/scratch")
except:
    pass
os.mkdir("/dev/shm/scratch")

def runcalc(file):
    try:
        jfile = open(file,"r")
    except:
        return 0
    jlines = jfile.readlines()
    jfile.close()
    for line in reversed(jlines):
        if line.startswith("%nprocshared") or line.startswith("%RWF") or line.startswith("%rwf"):
            jlines.remove(line)
    jlines.insert(0,"%nprocshared="+str(proc)+"\n")
    tempfile = "temp"+str(rank)+"_"+str(random.randint(1,100000))
    jlines.insert(0, "%RWF="+tempfile+",50GB\n")
    jfile = open(file,"w")
    jfile.write("".join(jlines))
    jfile.close()
    p = subprocess.Popen("/dev/shm//Mg16.x " + file, shell = True)
    print("Started Gaussian calc of " + file)
    while p.poll() == None:
        time.sleep(4)
    try:
        os.remove("/dev/shm/"+tempfile+".rwf")
    except:
        pass
    copy2("/dev/shm/inpfile.log", "./"+file.replace(".gjf",".log"))
    return 0

docalc = open("do_calc.dat","r").readlines()
print("Script started on rank " +str(rank)+"\n")
print("We have "+str(rank)+" rank and "+str(len(docalc))+" files\n")
runcalc(docalc[rank % len(docalc)].replace("\n",""))

sys.exit(0)
