import json
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
