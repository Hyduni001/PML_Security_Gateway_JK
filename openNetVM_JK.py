from multiprocessing import Process
import subprocess
import os
import  sys
import  tty, termios
import time    
import signal
import psutil
processes = dict()
def killProc(pid):
    baseProc = psutil.Process(pid)
    childrenProcList = baseProc.children(recursive=True)
    for proc in childrenProcList:
        os.kill(proc.pid, signal.SIGINT)
        # if (len(proc.children(recursive=True)) == 0):
            # os.kill(pid, signal.SIGINT)
        # else:
            # killProc(proc.pid)
def choose_nf(nf_name, service_id, nexthop_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/%s ; ./go.sh %d -d %d "%(nf_name,service_id, nexthop_id)
    os.system(cmd1)
    print("nf ok")

def choose_nf_router(service_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/nf_router ; ./go.sh %d  -f ./route.conf " % (service_id)
    devnull = open('/dev/null', 'w')
    p=subprocess.Popen(cmd1, stdout=devnull, shell=True)
    print("nf_router ok")
    return p.pid
def choose_firewall(service_id, nexthop_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/firewall ; ./go.sh %d -d %d -f ./rules.json " % (service_id, nexthop_id)
    os.system(cmd1)
    print("firewall ok")

def choose_bridge(service_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/bridge ; ./go.sh %d " % (service_id)
    os.system(cmd1)
    print("bridge ok")

def start_nf_router(service_id):
    pid = choose_nf_router(service_id)
    processes[service_id]=pid
    
def stop_nf(service_id):
    pid = processes[service_id]
    killProc(pid)
if __name__ == '__main__':
    
    linux_pid = None
    while True:
		fd=sys.stdin.fileno()
		old_settings=termios.tcgetattr(fd)
		#old_settings[3]= old_settings[3] & ~termios.ICANON & ~termios.ECHO  
		try:
			tty.setraw(fd)
			ch=sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
                if ch=='o':
                   pid=int(raw_input('please input pid you want to create: '))
                   linux_pid = start_nf_router(pid)
                if ch=='i':
                   pid=int(raw_input('please input pid you want to kill: '))
                   stop_nf(pid)
                if ch=='e':
                   os._exit(0)




