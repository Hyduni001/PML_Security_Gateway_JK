import json

rules_dict = None

def check_rules():
    with open("rules.json", "r") as fid:
        rules_dict = json.load(fid)
    print(rules_dict)
    return rules_dict

def add_rule(name, source_ip, depth,action):
    with open("rules.json", "r") as fid:
        rules_dict = json.load(fid)
    rules_dict[name]['ip'] = source_ip
    rules_dict[name]['depth'] = depth
    rules_dict[name]['action']= action
    with open("rules.json", "w") as fid:
        json.dump(rules_dict, fid)
    print(rules_dict)
    return 0

def del_rule(name):
    with open("rules.json", "r") as fid:
        rules_dict = json.load(fid)
    del rules_dict[name]
    with open("rules.json", "w") as fid:
        json.dump(rules_dict, fid)
    print(rules_dict)
    return 0





if __name__ == '__main__':
  rules_dict = None
  with open("rules.json","r") as fid:
     rules_dict = json.load(fid)
     print(rules_dict['rule3']['action'])
  rules_dict['rule3']['action']=1-rules_dict['rule3']['action']
  with open("rules.json","w") as fid:
     json.dump(rules_dict,fid)
  del rules_dict['rule3']
  print(rules_dict)
  rules_dict['rule3']=1
  print(rules_dict)

