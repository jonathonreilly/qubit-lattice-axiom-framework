"""MILP search for positive immutable one-step transport certificates.
Only exactly reconstructed positive witnesses count as results. Solver failure
or an infeasibility report is not promoted to an impossibility theorem.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
HERE=Path(__file__).resolve().parent
D=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (1,-1))
def search_patch(state,N,base,shape):
 sites=tuple(product(range(N),repeat=3));idx={x:i for i,x in enumerate(sites)}
 def add(x,d):return tuple((a+b)%N for a,b in zip(x,d))
 patch=sorted({add(base,b) for b in product(*(range(n) for n in shape))});inside=set(patch)
 records=[x for x in patch if state[idx[x]]>=0];variables=[]
 for x in records:
  for y in sorted(({x}|{add(x,d) for d in D})&inside):variables.append((x,y))
 if not variables:return None
 rows=[];lo=[];hi=[]
 def constraint(coeff,lower,upper):rows.append(coeff);lo.append(lower);hi.append(upper)
 for x in records:constraint({i:1 for i,(a,b) in enumerate(variables) if a==x},1,1)
 for y in patch:constraint({i:1 for i,(a,b) in enumerate(variables) if b==y},0,1)
 def content_at(x,d):
  if x not in inside:return {},int(state[idx[x]]==d)
  return {i:1 for i,(a,b) in enumerate(variables) if b==x and state[idx[a]]==d},0
 for x in sites:
  for j in range(3):
   y=add(x,D[2*j])
   if x not in inside and y not in inside:continue
   a,ca=content_at(x,2*j);b,cb=content_at(y,2*j+1);coeff=a.copy()
   for key,value in b.items():coeff[key]=coeff.get(key,0)-value
   constraint(coeff,cb-ca,cb-ca)
 A=lil_matrix((len(rows),len(variables)),dtype=float)
 for i,row in enumerate(rows):
  for j,a in row.items():A[i,j]=a
 c=np.array([-int(state[idx[x]]!=state[idx[y]]) for x,y in variables],dtype=float)
 start=time.monotonic();result=milp(c,integrality=np.ones(len(c)),bounds=Bounds(0,1),constraints=LinearConstraint(A.tocsc(),lo,hi),options={'time_limit':2.0,'mip_rel_gap':0.0})
 receipt={'base':base,'shape':shape,'variables':len(c),'constraints':len(rows),'status':int(result.status),'message':result.message,'seconds':time.monotonic()-start,'objective':None if result.fun is None else float(result.fun)}
 if result.x is None or result.fun>-.5:return {'receipt':receipt,'witness':None}
 rounded=np.rint(result.x).astype(int);assert np.max(abs(result.x-rounded))<1e-7
 moves=[variables[i] for i,v in enumerate(rounded) if v];assert len(moves)==len(records)
 assert len({a for a,b in moves})==len(records) and len({b for a,b in moves})==len(records)
 final=list(state)
 for x in patch:final[idx[x]]=-1
 for x,y in moves:
  assert y==x or y in {add(x,d) for d in D};final[idx[y]]=state[idx[x]]
 assert final!=state and Counter(final)==Counter(state)
 assert all(v<0 or final[idx[add(x,D[v])]]==(v^1) for x,v in zip(sites,final))
 assert all(final[idx[x]]==state[idx[x]] for x in sites if x not in inside)
 # Return the concrete identity assignment: each initial occupied site names a record.
 witness={'moves':[{'record_initial_site':x,'destination':y,'content':int(state[idx[x]])} for x,y in moves if x!=y],'final_state':final,'new_vacancies':[x for x in sites if final[idx[x]]<0]}
 return {'receipt':receipt,'witness':witness}

def main():
 out=HERE/'patch_transport';out.mkdir(exist_ok=True);summaries=[]
 cases=[('pilot','N4_jam_extended_s21092102'),('screen','N4_jam_extended_s21092204'),('pilot','N4_empty_extended_s21092101')]
 for phase,name in cases:
  path=HERE/('paired_growth_'+phase)/(name+'.final.txt');state=list(map(int,path.read_text().split()));N=4;trials=[];witnesses=[]
  for shape in [(2,2,2),(3,2,2),(2,3,2),(2,2,3),(3,3,2),(3,2,3),(2,3,3),(3,3,3)]:
   found=False
   for base in product(range(N),repeat=3):
    result=search_patch(state,N,base,shape)
    if result is None:continue
    trials.append(result['receipt'])
    if result['witness'] is not None:witnesses.append(result);found=True;break
   if found:break
  output={'source_path':str(path),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'N':N,'trials':trials,'positive_witnesses':witnesses,'limits':'Only exact positive certificates are scientific conclusions; no search failure promoted to a universal negative.'}
  (out/(name+'.json')).write_text(json.dumps(output,indent=2)+'\n')
  brief={'case':name,'trials':len(trials),'found':bool(witnesses),'shape':witnesses[0]['receipt']['shape'] if witnesses else None,'moved_records':len(witnesses[0]['witness']['moves']) if witnesses else None};summaries.append(brief);print(json.dumps(brief),flush=True)
 (out/'SUMMARY.json').write_text(json.dumps({'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':summaries},indent=2)+'\n')
if __name__=='__main__':main()
