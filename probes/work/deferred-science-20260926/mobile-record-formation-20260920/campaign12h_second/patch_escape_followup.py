"""Bounded constructive continuation from the verified larger-patch move."""
from pathlib import Path
from collections import deque
import importlib.util,json,hashlib
HERE=Path(__file__).resolve().parent
p=HERE/'paired_record_growth_validate.py';spec=importlib.util.spec_from_file_location('validation',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
source=HERE/'patch_transport/N4_jam_extended_s21092204.json';data=json.loads(source.read_text());start=data['positive_witnesses'][0]['witness']['final_state'];word=m.word(start)
seen={word:None};queue=deque([word]);end=None;birth=None;explored=0
while queue and explored<500:
 w=queue.popleft();channels=m.python_channels([int(a)-1 for a in w]);explored+=1
 births=[(key,value) for key,value in channels.items() if key[0]=='B']
 if births:birth=births[0];end=w;break
 for key,value in channels.items():
  if value not in seen:seen[value]=(w,key);queue.append(value)
steps=[]
if end is not None:
 node=end
 while seen[node] is not None:
  parent,key=seen[node];steps.append({'channel':key,'before':parent,'after':node});node=parent
 steps.reverse();steps.append({'channel':birth[0],'before':end,'after':birth[1]})
 assert all(m.valid([int(a)-1 for a in step['after']]) for step in steps)
 assert '0' not in steps[-1]['after']
result={'input_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'author_channel_implementation_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'found_full_packing':end is not None,'explored':explored,'seen':len(seen),'unexplored_queue':len(queue),'cap':500,'steps_after_patch_move':steps,'scope':'Finite exact positive path if found; no general reachability conclusion.'}
(HERE/'patch_transport/ESCAPE_FOLLOWUP.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='steps_after_patch_move'}))
