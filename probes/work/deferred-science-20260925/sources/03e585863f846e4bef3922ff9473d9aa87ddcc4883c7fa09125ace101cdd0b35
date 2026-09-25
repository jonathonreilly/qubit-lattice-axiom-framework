"""Read-only personal46 evidence check; never imports or executes the primary."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict
import hashlib,json
D=Path(__file__).resolve().parent
data=json.loads((D/'attempt01/stdout.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert data['source_sha256']==sha(D/'current_noise_controls.py')==sha(D/'attempt01/source.py')
receipt=json.loads((D/'attempt01/EXECUTION.json').read_text())
assert receipt['exit_code']==0 and receipt['source_unchanged'] and receipt['stdout_sha256']==sha(D/'attempt01/stdout.json')
assert (D/'attempt01/stderr.txt').read_bytes()==b''
rows=defaultdict(list)
for row in data['primitive_rows']:rows[row['graph']].append(row)
summaries=[];total=0
for group in data['graph_summaries']:
 name=group['graph'];L=int(name[5:]) if name.startswith('torus') else None
 if L:
  xyz=list(product(range(L),repeat=3));A={i for i,v in enumerate(xyz) if sum(v)%2==0}
  edges=[]
  for u,v in combinations(range(len(xyz)),2):
   if sum(min(abs(x-y),L-abs(x-y)) for x,y in zip(xyz[u],xyz[v]))==1:edges.append((u,v) if u in A else (v,u))
  edges=sorted(edges)
 elif name=='path7':
  xyz=[(i,0,0) for i in range(7)];A={0,2,4,6};edges=sorted((i,i+1) if i in A else (i+1,i) for i in range(6))
 else:
  assert name=='K2_3';xyz=[(i,0,0) for i in range(5)];A={0,1};edges=[(a,b) for a in (0,1) for b in (2,3,4)]
 nv=len(xyz);assert group['vertices']==nv and group['A']==len(A) and group['edges']==[list(e) for e in edges]
 near={a:{b for x,b in edges if x==a} for a in A};degrees={a:len(bs) for a,bs in near.items()}
 assert group['A_degrees']==[[a,degrees[a]] for a in sorted(A)]
 fs=[[1]*nv,[int(i==0) for i in range(nv)],[x-2*y+3*z for x,y,z in xyz],[1 if i in A else -1 for i in range(nv)]]
 if L==4:fs.extend([[(1,0,-1,0)[x] for x,y,z in xyz],[(0,-1,0,1)[x] for x,y,z in xyz]])
 elif L==6:fs.extend([[(-1)**x for x,y,z in xyz],[0]*nv])
 else:fs.extend([[i%3 for i in range(nv)],[i%5 for i in range(nv)]])
 means=[0]*6;cov=[[0]*6 for _ in range(6)];qd=[0]*nv;ed=[0]*len(edges);seen=set();norms=Counter()
 for row in rows[name]:
  a,b,c,s=(row[k] for k in ('a','b','c','sigma'));assert s in (-1,1) and b in near[a] and c in near[a] and b!=c
  key=(a,b,c,s);assert key not in seen;seen.add(key);norms[a,b]+=1
  expected_q={a:s-1,b:-s,c:1};expected_q={k:v for k,v in expected_q.items() if v}
  deltaq=dict(row['delta_q']);assert len(deltaq)==len(row['delta_q']) and deltaq==expected_q
  deltaE=dict(row['delta_E']);assert len(deltaE)==len(row['delta_E']) and deltaE=={edges.index((a,b)):s,edges.index((a,c)):-1}
  div=[0]*nv
  for e,v in deltaE.items():u,w=edges[e];div[u]+=v;div[w]-=v;ed[e]+=v
  assert div==[deltaq.get(i,0) for i in range(nv)] and sum(div)==0
  q=[int(i in A)+div[i] for i in range(nv)]
  assert all(v in (-1,0,1) for v in q) and sum(q)==len(A) and sum(map(abs,q))==len(A)+2
  qd=[x+y for x,y in zip(qd,div)]
  ws=[sum(f[i]*v for i,v in deltaq.items()) for f in fs];assert ws==row['charge_tests']
  for i in range(6):
   means[i]+=ws[i]
   for j in range(6):cov[i][j]+=ws[i]*ws[j]
 expected={(a,b,c,s) for a,bs in near.items() for b in bs for c in bs if b!=c for s in (-1,1)}
 assert seen==expected and len(seen)==group['primitive_rows']==group['total_first_event_rate_in_kappa']
 assert means==group['initial_mean_slope_in_kappa'] and cov==group['initial_covariance_slope_in_kappa']
 assert qd==group['initial_charge_drift_in_kappa']
 current=[-v for v in ed];assert current==group['formation_current_in_kappa']==[2*(degrees[a]-1) for a,b in edges]
 assert group['mark_squared_norms']==[[a,b,norms[a,b],degrees[a]-1,2*(degrees[a]-1)] for a in sorted(A) for b in sorted(near[a])]
 formula_mean=[sum(2*(degrees[a]-1)*(f[b]-f[a]) for a,b in edges) for f in fs]
 formula_cov=[[sum(4*(degrees[a]-1)*(f[b]-f[a])*(g[b]-g[a]) for a,b in edges) for g in fs] for f in fs]
 assert means==formula_mean and cov==formula_cov
 if L in (4,6):
  Fourier=group['Fourier'];defect=1 if L==4 else 2
  assert Fourier==dict(allowed_k_in_pi=['1/2' if L==4 else '1','0','0'],full_initial_second_moment_slope_in_kappa=80*len(A)*defect,site_normalized_slope_in_kappa=40*defect,defect_sum=defect,imaginary_self_covariance=0)
 else:assert group['Fourier'] is None
 summaries.append(dict(graph=name,primitive_rows=len(seen),charge_mean=means,covariance=cov,
  formation_current_values=sorted(set(current)),charge_drift_values=sorted(set(qd)),Fourier=group['Fourier']))
 total+=len(seen)
assert total==data['primitive_count']==8480 and data['real_polarized_covariance_entries']==180 and data['all_assertions_passed']
print(json.dumps(dict(all_complete_primitive_rows_checked=total,polarized_covariance_entries=180,
 all_geometry_mark_norm_current_and_charge_arrays_checked=True,groups=summaries,
 mode='read-only reconstruction of own stored evidence; no independent authorship or finite-lag calculation'),indent=2))
