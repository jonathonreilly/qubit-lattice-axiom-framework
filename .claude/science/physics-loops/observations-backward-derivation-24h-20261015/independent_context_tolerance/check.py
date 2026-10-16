import numpy as np, math,json,subprocess,time,sys,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
def qmul(q,r):return np.r_[q[0]*r[0]-q[1:]@r[1:],q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def qedge(a,b):return np.r_[math.sqrt((1+a@b)/2),np.cross(a,b)/math.sqrt(2*(1+a@b))]
for N in [4,5,11,23]:
 for beta in [.00001,.47,1.56]:
  for sign in [-1,1]:
   pts=[np.array([math.sin(beta)*math.cos(2*math.pi*j/N),sign*math.sin(beta)*math.sin(2*math.pi*j/N),sign*math.cos(beta)]) for j in range(N)]
   z=np.array([0.,0,1]);x=np.array([1.,0,0]);path=[z,x]+pts+[pts[0],x,z];q=np.array([1.,0,0,0]);W=np.zeros(3)
   for a,b in zip(path,path[1:]):q=qmul(qedge(a,b),q);W+=np.cross(a,b)
   gam=-math.pi+N*math.atan(math.cos(beta)*math.tan(math.pi/N))
   ck('connector '+str((N,beta,sign)),len(path)-1==N+4 and min(a@b for a,b in zip(path,path[1:]))>=-1e-14 and np.linalg.norm(q-[math.cos(gam),0,0,-math.sin(gam)])<1e-12)
   ck('cross '+str((N,beta,sign)),np.linalg.norm(W-[0,0,sign*N*math.sin(beta)**2*math.sin(2*math.pi/N)])<1e-12)
# Disk tangent is exact, including near S=1; phase continuity is local.
for S in [.001,.2,.8,.999]:
 v=1-S*S+1j*S*math.sqrt(1-S*S)
 ck('sharp phase disk '+str(S),abs(abs(v-1)-S)<1e-14 and abs(np.angle(v)-math.asin(S))<1e-14)
# Quaternion norm equals operator norm for differences of SU(2) matrices.
rng=np.random.default_rng(419)
for j in range(100):
 a=rng.normal(size=3);a/=np.linalg.norm(a);b=rng.normal(size=3);b/=np.linalg.norm(b)
 ap=a+.02*rng.normal(size=3);ap/=np.linalg.norm(ap);bp=b+.02*rng.normal(size=3);bp/=np.linalg.norm(bp)
 eta=min(1+a@b,1+ap@bp);ea=np.linalg.norm(ap-a);eb=np.linalg.norm(bp-b)
 ck('quaternion Lipschitz '+str(j),np.linalg.norm(qedge(ap,bp)-qedge(a,b))<=math.sqrt(2)*(ea+eb)/math.sqrt(eta)+1e-13)
cmd=[sys.executable,'-B',str(p/'probe_context_tolerance_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);ck('exact full output reproduction',json.loads(r.stdout)==json.loads((p/'CONTEXT_TOLERANCE_CONTROLS_v1.json').read_text()))
h=json.loads((o/'frozen_sources.json').read_text());ck('all frozen sources unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==v for n,v in h.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'checks passed')
