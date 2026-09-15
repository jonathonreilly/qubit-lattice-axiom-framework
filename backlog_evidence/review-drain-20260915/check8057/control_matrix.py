from pathlib import Path
from fractions import Fraction as F
import json,gzip,signal,time,itertools
signal.alarm(60);start=time.monotonic();r=Path(__file__).parent;raw=next((r/'8056/original/.claude').rglob('RAW_CANDIDATES'));data=json.loads((raw/'CUBE_INPUTS.json').read_text());trig=json.loads((raw/'TRIG_INPUTS.json').read_text())
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def conj(x):return x[0],-x[1]
def sub(x,y):return x[0]-y[0],x[1]-y[1]
def dot(a,b):return tuple(sum(x[i] for x in [mul(v,w) for v,w in zip(a,b)]) for i in (0,1))
def norm2(x):return x[0]**2+x[1]**2
v=list(itertools.product(range(2),repeat=3));edges=[(x,a) for x in v for a in range(3) if x[a]==0];records=[]
for job,rep in zip((0,4,8,12,16,20),(0,1,3,5,10,15)):
 with gzip.open(raw/f'job{job:02d}.jsonl.gz','rt') as f:row=json.loads(next(f))
 signs=dict(zip(edges,data['rows'][rep]['cube_signs']));c=[[0]*8 for _ in range(8)]
 for i,x in enumerate(v):
  for a in range(3):
   y=list(x);y[a]=0;c[i][i^(1<<(2-a))]=signs[tuple(y),a]
 d=[[(F(sum(c[i//2][k]*c[k][j//2] for k in range(8))+3*(i//2==j//2)) if i%2==j%2 else F(0),F(0)) for j in range(16)] for i in range(16)];radius=F(0)
 for a,t in enumerate(row['index']):
  g=trig['rows'][t];q=F(float.fromhex(g['q_hex']));radius+=max(abs(q-F(g['lower_numerator'],g['denominator'])),abs(q-F(g['upper_numerator'],g['denominator'])))
  for i,x in enumerate(v):
   j=i^(1<<(2-a));ai=(0,F(c[i][j]*(2*x[a]-1)))
   for s in (0,1):
    target=(1-s if a<2 else s);pa=(F(1),F(0)) if a==0 else ((F(0),F(2*s-1)) if a==1 else (F(1-2*s),F(0)));d[2*i+s][2*j+target]=mul(ai,(pa[0]*q,pa[1]*q))
 Q=[[(F(float.fromhex(z[0])),F(float.fromhex(z[1]))) for z in rr] for rr in row['vectors_hex']];lam=[F(float.fromhex(x)) for x in row['eigenvalues_hex']];cols=list(zip(*Q));res=gram=F(0)
 for i in range(16):
  for j in range(16):
   res+=norm2(sub(dot(d[i],cols[j]),(Q[i][j][0]*lam[j],Q[i][j][1]*lam[j])))
   gram+=norm2(sub(dot([conj(z) for z in cols[i]],cols[j]),(F(i==j),F(0))))
 cert=row['certificate'];assert F(cert['input_radius'])==radius;assert F(cert['residual'])**2>=res and F(cert['eta'])**2>=gram;assert F(cert['eigenvalue_radius'])==radius+2*F(cert['residual'])+4*max(map(abs,lam))*F(cert['eta'])
 rad=F(cert['eigenvalue_radius'])
 for x,(a,b) in zip(lam,cert['root_intervals']):assert 0<=F(a) and F(a)**2<=max(0,x-rad) and F(b)**2>=x+rad
 records.append({'rep':rep,'job':job,'index':row['index'],'exact_residual_and_gram_bounds':True,'all16_root_enclosures':True})
out={'scope':'Independent Fraction pair arithmetic, direct bit-action D16, six first-node certificates; no canonical helper imports or eigensolve','cases':records,'seconds':time.monotonic()-start};(r/'control-matrix.json').write_text(json.dumps(out,indent=2));print(out)
