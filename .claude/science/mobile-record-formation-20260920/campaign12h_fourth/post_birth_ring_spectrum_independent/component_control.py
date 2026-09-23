from pathlib import Path
import ast,hashlib,json,itertools,math
from collections import deque
import numpy as np
import sympy as sp
D=Path(__file__).resolve().parent;p=D/'ring_control.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='b082190bf88df120577cf9337a4edee200e1306a96bcd05d8bcfedd4978e5bf9'
ns={'np':np,'sp':sp,'math':math,'itertools':itertools}
exec(compile(ast.Module(body=[n for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef)],type_ignores=[]),str(p),'exec'),ns)
charge_hops=ns['charge_hops'];states_P=ns['states_P'];physical_hops=ns['physical_hops'];valid=ns['valid'];make_form=ns['make_form']
rows=[]
for L in range(3,8):
 ps=states_P(L);ix={q:i for i,q in enumerate(ps)};adj={}
 def inv(q,f):
  occ=[x for x,c in enumerate(q) if c];return (f+occ.index(q.index(-1)))%L
 for q in ps:
  for f in range(L):
   s=(q,f);adj[s]=set()
   for t,e,de in charge_hops(q):
    for r,g,dg in charge_hops(t):
     if r not in ix or r==q:continue
     df=(de if e==2*L-1 else 0)+(dg if g==2*L-1 else 0)
     z=(r,(f+df)%L);assert inv(*s)==inv(*z);adj[s].add(z)
 unseen=set(adj);comps=[]
 while unseen:
  root=next(iter(unseen));todo=[root];seen={root};unseen.remove(root)
  while todo:
   s=todo.pop()
   for z in adj[s]:
    if z not in seen:seen.add(z);unseen.remove(z);todo.append(z)
  comps.append((len(seen),sorted({inv(*s) for s in seen})))
 assert len(comps)==L and all(n==len(ps) and len(I)==1 for n,I in comps)
 rows.append({'L':L,'states_in_flux_mod_L_control':len(adj),'components':sorted(comps)})

birth=[]
for L in (3,4):
 for coh in (False,True):
  v=make_form(L,{0:sp.Integer(1)},coh);channels=[]
  for e in range(2*L):
   for c in (1,-1):
    result={}
    for s,coef in v.items():
     for mid in physical_hops(s):
      a=e;b=(e+1)%(2*L)
      if mid[0][a] or mid[0][b]:continue
      q=list(mid[0]);q[a]=c;q[b]=-c;E=list(mid[1]);E[e]+=c;z=(tuple(q),tuple(E))
      assert valid(*z) and all(q[x] for x in range(0,2*L,2))
      result[z]=result.get(z,0)+coef
    norm=sp.simplify(sum(sp.conjugate(a)*a for a in result.values()))
    if norm:
     channels.append({'edge':e,'charge_at_tail':c,'norm_squared':str(norm),'output_record_counts':sorted({sum(x!=0 for x in s[0]) for s in result})})
  total=sum(sp.sympify(x['norm_squared']) for x in channels)
  assert total==(0 if L==3 else 4)
  birth.append({'L':L,'coherent_initial_mark':coh,'subsequent_resolved_total_loss_over_kappa_at_this_state':str(total),'nonzero_channels':channels})
out={'finite_flux_quotient_connectivity':rows,'initial_subsequent_birth_controls':birth,'scope':'The quotient check corroborates the analytic integer-winding invariant and connectivity proof. The birth control only evaluates the initial operator loss, not a later waiting law or completion probability.'}
(D/'COMPONENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
