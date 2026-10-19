import numpy as np,json,math
rows=[]
for m in range(3,21):
 R=m+3;S={(x,y) for x in range(m) for y in range(m)}
 edges=[];pls=[]
 for x in range(R):
  for y in range(R):
   edges.extend([{(x,y),((x+1)%R,y)},{(x,y),(x,(y+1)%R)}])
   pls.append({(x,y),((x+1)%R,y),(x,(y+1)%R),((x+1)%R,(y+1)%R)})
 ei=[e for e in edges if e<=S];pi=[p for p in pls if p<=S]
 ec=[e for e in edges if e&S and not e<=S];pc=[p for p in pls if p&S and not p<=S]
 assert len(ei)==2*m*(m-1) and len(pi)==(m-1)**2
 assert len(ec)==len(pc)==4*m
 assert all(any(len(e&p)==1 for p in pi) for e in ei)
 D=10*m*(m-1)-4*(m-1)**2
 assert D==6*m*m-2*m-4
 rows.append(dict(m=m,internal_edges=len(ei),internal_plaquettes=len(pi),cross_edges=len(ec),cross_plaquettes=len(pc),D=D,boundary_error=72*m))
# Independent dense local matrix in Z basis, m=3.
m=3;N=m*m;idx=np.arange(1<<N);H=np.zeros((1<<N,1<<N));flat=np.ones(1<<N,dtype=bool)
for x in range(m-1):
 for y in range(m-1):
  bits=[x*m+y,(x+1)*m+y,x*m+y+1,(x+1)*m+y+1]
  parity=np.zeros(len(idx),dtype=int)
  for b in bits:parity^=(idx>>b)&1
  sign=1-2*parity;H[idx,idx]-=4*sign;flat &= sign==1
for x in range(m):
 for y in range(m):
  for a,b in [(x+1,y),(x,y+1)]:
   if a<m and b<m:H[idx,idx^((1<<(x*m+y))|(1<<(a*m+b))) ]-=5
sub=H[np.ix_(flat,flat)];assert np.max(np.abs(sub+16*np.eye(sum(flat))))==0
v=np.ones(len(idx))/np.sqrt(len(idx));assert abs(v@H@v+60)<1e-10
E=float(np.linalg.eigvalsh(H)[0]);assert E<=-60+1e-10
for m in range(32,10000):
 assert 5*m*m-74*m-4>=2*m*m
a=1/(20*math.sqrt(10))
assert abs(a*a/2-1/8000)<1e-18
for lam in [.001,.01,.1]:
 for delta in [10.**(-k) for k in range(1,12)]:
  lhs=lam*(1-lam)*delta+lam**4/(1024000*delta)
  lower=2*math.sqrt((1-lam)/1024000)*lam**2.5
  assert lhs>=lower*(1-1e-12)
print(json.dumps(dict(balance_coefficient=2/math.sqrt(1024000),status='pass',rows=rows,dense_m3_ground=E,flat_dimension=int(sum(flat)),flat_energy=-16,all_X_trial=-60)))
