import numpy as np, math,json,subprocess,sys,time,hashlib
from pathlib import Path
p=Path(__file__).resolve().parent.parent;o=Path(__file__).resolve().parent
rows=[]
def ck(n,c):
 assert c,n
 rows.append(n)
def mul(q,r):return np.r_[q[0]*r[0]-q[1:]@r[1:],q[0]*r[1:]+r[0]*q[1:]+np.cross(q[1:],r[1:])]
def path(beta,N,rot):
 pts=[rot@np.array([math.sin(beta)*math.cos(j*2*math.pi/N),math.sin(beta)*math.sin(j*2*math.pi/N),math.cos(beta)]) for j in range(N)]
 return [np.array([0.,0,1])]+pts+[pts[0],np.array([0.,0,1])]
def transport(pts,n,k):
 q=np.array([1.,0,0,0]);W=np.zeros(3)
 for a,b in zip(pts,pts[1:]):
  v=np.cross(a,b);c=a@b;pair=np.r_[math.sqrt((1+c)/2),v/math.sqrt(2*(1+c))];angle=k*(n@v)/2
  twist=np.r_[math.cos(angle),a*math.sin(angle)]
  q=mul(mul(pair,twist),q);W+=v
 return q,W
n=np.array([.31,-.27,.83]);k=-.63
for N in [3,5,7,12,31]:
 for beta in [.01,.38,.9,1.3,math.pi/2-1e-4]:
  gam=-math.pi+N*math.atan(math.cos(beta)*math.tan(math.pi/N))
  bb=math.acos(math.tan((math.pi+gam/2)/N)/math.tan(math.pi/N))
  A=path(beta,N,np.eye(3));B=path(bb,N,np.eye(3))+path(bb,N,np.diag([1,-1,-1]))[1:]
  qa,wa=transport(A,n,0);qb,wb=transport(B,n,0);va,_=transport(A,n,k);vb,_=transport(B,n,k)
  W=N*math.sin(beta)**2*math.sin(2*math.pi/N)
  ck('full reference '+str((N,beta)),np.linalg.norm(qa-qb)<1e-9 and np.linalg.norm(qa-np.array([math.cos(gam),0,0,-math.sin(gam)]))<1e-9)
  ck('W '+str((N,beta)),np.linalg.norm(wa-[0,0,W])<1e-12 and np.linalg.norm(wb)<1e-12)
  ck('context '+str((N,beta)),np.linalg.norm(vb-qb)<1e-9 and np.linalg.norm(va-np.array([math.cos(gam-k*n[2]*W/2),0,0,-math.sin(gam-k*n[2]*W/2)]))<1e-9)
  rev,_=transport(list(reversed(A)),n,k)
  ck('reverse '+str((N,beta)),np.linalg.norm(mul(rev,va)-[1,0,0,0])<1e-9)
# Characteristic-function series at negative sinc: distinguishes coherence/visibility.
x=4.;series=sum((-1.)**j*x**(2*j)/math.factorial(2*j+1) for j in range(30))
ck('signed coherence is negative',abs(series-math.sin(x)/x)<1e-14 and series<0)
cmd=[sys.executable,'-B',str(p/'probe_context_echo_v1.py')];start=time.monotonic();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(o/'reproduction.stdout').write_text(r.stdout);(o/'reproduction.stderr').write_text(r.stderr);(o/'reproduction_receipt.json').write_text(json.dumps({'command':cmd,'timeout_seconds':120,'elapsed_seconds':time.monotonic()-start,'returncode':r.returncode},indent=2))
ck('author succeeds',r.returncode==0);ck('published JSON reproduced',json.loads(r.stdout)==json.loads((p/'CONTEXT_ECHO_CONTROLS_v1.json').read_text()))
f=json.loads((o/'frozen_sources.json').read_text());ck('frozen unchanged',all(hashlib.sha256((p/n).read_bytes()).hexdigest()==h for n,h in f.items()))
(o/'results.json').write_text(json.dumps({'passed':len(rows),'checks':rows},indent=2));print(len(rows),'checks passed')
