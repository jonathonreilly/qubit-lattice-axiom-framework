from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,signal,time,math
signal.alarm(60);st=time.monotonic();r=Path(__file__).parent
# Exact dyadic Gaussian 4x4 fixture: all intermediates below2^53, dyadic denominators.
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def adj(a):return [[complex(x).conjugate() for x in row] for row in zip(*a)]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
h=[[(-1)**((i&j).bit_count())/2 for j in range(4)] for i in range(4)];u=[[h[i][j]*(1j)**i for j in range(4)] for i in range(4)];v=[[h[i][j]*(1j)**j for j in range(4)] for i in range(4)];assert mm(adj(u),u)==mm(adj(v),v)==eye(4)
s=[[int(i==j)*(i+1) for j in range(4)] for i in range(4)];x=mm(mm(u,s),adj(v));y=mm(mm(u,s),adj(u));z=mm(mm(v,s),adj(v));a=[[complex(i+j,(i-j)) for j in range(4)] for i in range(4)];b=[[complex(2*(i==j),j-i) for j in range(4)] for i in range(4)];c=[]
for bit in range(2):
 q=[[0]*4 for _ in range(4)]
 for n in range(4):
  if n>>bit&1:q[n^(1<<bit)][n]=(-1)**((n&((1<<bit)-1)).bit_count())
 c.extend([q,adj(q)])
def energy(x,a,b):return tr(mm(mm(adj(x),a),x))+tr(mm(mm(adj(x),x),list(map(list,zip(*b)))))-sum(tr(mm(mm(mm(adj(x),q),x),adj(q))) for q in c)
bar=lambda a:[[complex(x).conjugate() for x in row] for row in a]
delta=energy(x,a,b)-(energy(y,a,bar(a))+energy(z,bar(b),b))/2;square=0
for q in c:
 aa=mm(mm(adj(u),q),u);bb=mm(mm(adj(v),q),v);d=[[aa[i][j]-bb[i][j] for j in range(4)] for i in range(4)];square+=tr(mm(mm(mm(s,d),s),adj(d)))/2
assert delta==square and delta.real>0
wrong=energy(x,a,b)-(energy(y,a,a)+energy(z,bar(b),b))/2;assert wrong!=square
# L6 actual edge/face incidence, unlike canonical L4/L8 controls.
L=6;vs=list(product(range(L),repeat=3));idx={x:i for i,x in enumerate(vs)}
def step(x,a):y=list(x);y[a]=(y[a]+1)%L;return tuple(y)
def edge(x,a):return frozenset((x,step(x,a)))
faces=[]
for x in vs:
 for a,b in combinations(range(3),2):faces.append({edge(x,a),edge(x,b),edge(step(x,a),b),edge(step(x,b),a)})
ef={};inc={x:[] for x in vs}
for x in vs:
 for a in range(3):e=edge(x,a);ef[e]=set();inc[x].append((e,a));inc[step(x,a)].append((e,a))
for f,es in enumerate(faces):
 for e in es:ef[e].add(f)
counts=[[0,0] for _ in faces];pairs=[0,0]
for x in vs:
 for (e,a),(f,b) in combinations(inc[x],2):
  t=int(a==b);affected=ef[e]^ef[f];assert len(affected)==(8 if t else 6);pairs[t]+=1
  for k in affected:counts[k][t]+=1
assert pairs==[12*L**3,3*L**3] and all(x==[24,8] for x in counts)
# Exact constant implications, independent of acceptance receipt booleans.
thermal=F(3,50)-4*(F(30,8*32**2)+F(7,10*200));assert thermal==F(4013,128000)>F(3,100)
k=(F(3,50)-F(15,1024))/8;assert k==F(1161,204800) and F(3,2)/k==F(102400,387)
assert sum((F(105**j,math.factorial(j)) for j in range(201)),F(0))>48**24*31*4096
out={'scope':'Independent n4 complex dyadic weighted-SVD identity with actual wrong-conjugation alternative; L6 full incidence; rational constants. No canonical imports or physical state solve','svd_defect':str(delta),'wrong_conjugation':str(wrong),'L':L,'pairs':pairs,'all_faces_counts':[24,8],'thermal_margin':str(thermal),'ground_kappa_over_h':str(k),'seconds':time.monotonic()-st};(r/'control-structural.json').write_text(json.dumps(out,indent=2));print(out)
