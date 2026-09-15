from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json
R=Path(__file__).parent;idx=json.loads((R/'8074-recovered-object-inventory.json').read_text());bind={}
def read(p):
 x=next(x for x in idx if x['original_relative_path']==p);bind[p]=x['sha256'];return json.loads((R/'forensic'/x['sha256']).read_text())
saved=read('native-fresh-pivot-width-run/RESULT.json');computed=[];S=2**192
for orbit in range(5):
 hist=read(f'native-compression-twelve-to24-run-111c/ORBIT_{orbit}/HISTORY.json')['history'];assert len(hist)==24;seen=set()
 for row,h in enumerate(hist):
  i=h['index'];support={i} if i>=396 else {6*(i//6)+(i%6)//2,6*(i//6)+(i%6)//2+3};fresh=sorted(support-seen);seen|=support
  if not fresh:continue
  l,u=h['r'];a=isqrt(l*S);b=isqrt(u*S);b+=b*b<u*S;assert a>0;f=1 if i>=396 else 2
  low=S*S//(f*b);high=(S*S+f*a-1)//(f*a);lb=F((u-l)*S,f*2*u*b)
  x={'orbit':orbit,'row':row,'index':i,'fresh_raw':fresh,'half':i<396,'divisor_failure':False,'forced_lower':low,'forced_upper':high,'width':high-low,'threshold':S//2**39,'must_fail_width':high-low>S//2**39,'exact_image_width_lower_bound':str(lb),'exact_image_lower_exceeds_threshold':lb>F(1,2**39)};computed.append(x)
assert computed==saved['rows'];assert len(computed)==78
bad=[x for x in computed if x['must_fail_width']];assert len(bad)==53
first=[min(x['row']+1 for x in bad if x['orbit']==i) for i in range(5)];assert first==[7,8,8,8,9]
(R/'fresh-width-control.json').write_text(json.dumps({'status':'PASS','rows':78,'blockers':53,'first_fresh_obstruction':first,'bindings':bind,'scope':'Exact independent support/endpoint replay from saved pivot intervals; no primary or numerical worker executed.'},indent=2)+'\n');print('PASS 78 fresh width rows, 53 blockers')
