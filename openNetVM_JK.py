from multiprocessing import Process
import subprocess

def choose_nf(nf_name, service_id, nexthop_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/%s ; ./go.sh %d -d %d "%(nf_name,service_id, nexthop_id)
    subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    print("nf ok")

def choose_nf_router(service_id, rule_file):
    cmd1 = "cd /home/hyd/openNetVM/examples/nr_router ; ./go.sh %d  -f %s " % (service_id, rule_file)
    subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    print("nf_router ok")

def choose_firewall(service_id, nexthop_id, rule_file):
    cmd1 = "cd /home/hyd/openNetVM/examples/firewall ; ./go.sh %d -d %d -f %s " % (service_id, nexthop_id, rule_file)
    subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    print("firewall ok")

def choose_bridge(service_id):
    cmd1 = "cd /home/hyd/openNetVM/examples/bridge ; ./go.sh %d " % (service_id)
    subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    print("bridge ok")

def start_nf_router(service_id, rule_file):
    p = "p%d" % service_id
    p = Process(target=choose_nf_router, args=(service_id, rule_file) )
    p.start()

def stop_nf(service_id):
    p = "p%d" % service_id
    p.terminate()



