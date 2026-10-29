"""Independent patch resolvent/support-algebra tests; not an actual YM matrix."""
import math,json,os,re,resource,subprocess,time
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss
START=time.monotonic();checks=[];resources=[]
def guard(where):
 cp=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5);mt=re.search(r'System-wide memory free percentage:\s*(\d+)%',cp.stdout);assert cp.returncode==0 and mt,'RESOURCE memory'
 r={'where':where,'rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'free':int(mt.group(1)),'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'elapsed':time.monotonic()-START,'threads':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']}};resources.append(r)
 assert r['rss']<2_000_000_000 and r['free']>=50 and max(r['load'])<20 and r['nice']>=10 and r['elapsed']<=60 and set(r['threads'].values())=={'1'},('RESOURCE',r)
def gate(name,yes,detail=None):
 checks.append({'name':name,'passed':bool(yes),'detail':detail});assert yes,name
def rotation(axis,angle):
 a=np.asarray(axis,dtype=float);a/=np.linalg.norm(a);x,y,z=a
 return expm(angle*np.array([[0,-z,y],[z,0,-x],[-y,x,0]]))
N=30;D=3;R=5;beta=4.5;size=N*D;eye=np.eye(size)
boxes=[set(range(6*j,6*j+6)) for j in range(5)]
def thick(S,r):return { (v+d)%N for v in S for d in range(-r,r+1)}
def blockids(S):return frozenset(v//6 for v in S)
def scalar(S):return [D*v+c for v in sorted(S) for c in range(D)]
phase=.2*np.sin(.17*np.arange(N))
def build(z):
 K=np.zeros((size,size));rot=[]
 for i in range(N):
  O=rotation([1,.3+math.sin(i),.2+math.cos(.4*i)],.11*i)
  onsite=O@np.diag([1.5+.08*math.sin(z[(i-1)%N]),1.9+.07*math.cos(z[i]),2.35+.06*math.sin(z[(i+1)%N])])@O.T
  K[D*i:D*i+D,D*i:D*i+D]+=onsite
 for i in range(N):
  j=(i+1)%N;w=.09+.013*math.cos(.31*i+z[i]);O=rotation([math.sin(.6*i+.2),math.cos(.43*i-.1),.7+.03*i],.19+.07*i+z[i]);rot.append(O)
  ii=slice(D*i,D*i+D);jj=slice(D*j,D*j+D)
  K[ii,ii]+=w*np.eye(D);K[jj,jj]+=w*np.eye(D);K[ii,jj]-=w*O;K[jj,ii]-=w*O.T
 return K,rot
def atoms(K,a):
 P=[];res=[]
 for q in boxes:
  om=thick(q,R);read=thick(om,1);inside=scalar(om);cols=scalar(q);outside=sorted(set(range(size))-set(inside));lookup={v:i for i,v in enumerate(inside)}
  inverse=np.linalg.solve(K[np.ix_(inside,inside)]+a*np.eye(len(inside)),np.eye(len(inside))[:,[lookup[c] for c in cols]])
  Pq=np.zeros_like(K);Pq[np.ix_(inside,cols)]=inverse
  Rq=np.zeros_like(K);Rq[np.ix_(outside,cols)]=-K[np.ix_(outside,inside)]@inverse
  support=blockids(read);P.append((support,Pq));res.append((support,Rq))
 return P,res
def norms(A):
 out=np.zeros(size);inc=np.zeros(5);incoming=np.zeros(size)
 for S,a in A:
  w=math.exp(beta*len(S));absolute=np.abs(a)*w;out+=absolute.sum(axis=1);incoming+=absolute.sum(axis=0)
  for v in S:inc[v]+=absolute.sum()
 return {'row':float(max(out)),'column':float(max(incoming)),'M':float(max(max(out),max(incoming))),'B':float(max(inc))}
def joined(A,B):
 out=[]
 for S,a in A:
  for T,b in B:
   c=a@b
   if np.max(np.abs(c))>0:
    assert S&T
    out.append((S|T,c))
 return out
guard('start');K,transport=build(phase);eig,Q=np.linalg.eigh(K)
gate('real positive covariant precision',min(eig)>1.4,float(min(eig)))
hol=np.eye(D)
for t in transport:hol=hol@t
gate('nontrivial winding retained',np.linalg.norm(hol-np.eye(D))>.2,float(np.linalg.norm(hol-np.eye(D))))
gate('noncommuting colour transports',np.linalg.norm(transport[1]@transport[7]-transport[7]@transport[1])>.01)
details=[]
for a in (0.,.3,2.,20.):
 pa,ra=atoms(K,a);P=sum(x for S,x in pa);res=sum(x for S,x in ra);pn=norms(pa);rn=norms(ra)
 error=float(np.max(np.abs((K+a*eye)@P-(eye-res))))
 gate('patch identity a='+str(a),error<=5e-12,error)
 gate('absolute weighted residual a='+str(a),rn['M']<.5,rn)
 G=np.linalg.solve(K+a*eye,eye);recon=P@np.linalg.solve(eye-res,eye)
 gate('right-ordered inverse a='+str(a),np.max(np.abs(G-recon))<=5e-12,float(np.max(np.abs(G-recon))))
 products=joined(pa,ra);prod=norms(products)
 gate('marked product incidence a='+str(a),prod['B']<=pn['B']*rn['M']+pn['M']*rn['B']+5e-12,{'actual':prod['B'],'bound':pn['B']*rn['M']+pn['M']*rn['B']})
 trunc=np.zeros_like(K);power=eye.copy()
 for order in range(4):
  trunc+=P@power;power=power@res
  err=float(np.max(np.abs(G-trunc)));bound=pn['M']*rn['M']**(order+1)/(1-rn['M'])
  gate('Neumann remainder a='+str(a)+' n='+str(order),err<=bound+5e-12,{'error':err,'bound':bound})
 details.append({'a':a,'P':pn,'R':rn})
 if a==0:
  wrongsign=float(np.max(np.abs(P@np.linalg.solve(eye+res,eye)-G)))
  wrongorder=float(np.max(np.abs(np.linalg.solve(eye-res,P)-G)))
  gate('wrong residual sign rejected',wrongsign>1e-10,wrongsign)
  gate('wrong noncommuting order rejected',wrongorder>1e-10,wrongorder)
 guard('resolvent a='+str(a))
# Coefficient just outside the inverse's coordinate patch changes its matrix.
z=phase.copy();z[24]+=.4;K2,_=build(z);pa,_=atoms(K,0);pb,_=atoms(K2,0);remote=float(np.max(np.abs(pa[0][1]-pb[0][1])))
gate('patch read collar coefficient matters',remote>1e-10,remote)
# Independent Stieltjes integral and Jacobi trace integral, without logdet LU.
x,w=leggauss(64);C=np.zeros_like(K);trace=0.;c=4.
for xx,ww in zip(x,w):
 t=(xx+1)*math.pi/4;a=math.tan(t)**2
 C+=ww/2/(math.cos(t)**2)*np.linalg.solve(K+a*eye,eye)
 theta=(xx+1)/2;trace+=ww/2*np.trace(np.linalg.solve((1-theta)*c*eye+theta*K,K-c*eye))
spectral=(Q*(eig**-.5))@Q.T
sqrerr=float(np.max(np.abs(C-spectral)));logdet=float(np.log(eig).sum());trace_det=float(size*math.log(c)+trace)
gate('Stieltjes square root',sqrerr<=2e-10,sqrerr)
gate('full scalar determinant homotopy',abs(trace_det-logdet)<=2e-10,{'trace':trace_det,'spectral':logdet})
wrongcolour=3*float(np.log(np.linalg.eigvalsh(K[::3,::3])).sum())
gate('three identical colour determinants rejected',abs(wrongcolour-logdet)>1e-10,{'full':logdet,'wrong':wrongcolour})
# Exact marked-product counterexample: many leaves feed several centres,
# then each centre's diagonal atom reads a remote common vertex v.
n=m=256;b0=4.;actual=n*m*math.exp(3*b0);wrong=(n+m)*math.exp(4*b0);correct=(n+n*m)*math.exp(4*b0)
gate('column omission fails marked-incidence bound',actual>wrong,{'actual_at_remote':actual,'row_only_wrong_bound':wrong,'correct_global_bound':correct,'n':n,'m':m,'beta':b0})
gate('remote mark cannot be omitted',actual>n*math.exp(4*b0),{'actual':actual,'root_only_bound':n*math.exp(4*b0)})
# The connector's cardinality differs even at the same endpoint separation.
connector=set(range(9));endpoint_label={0,8};filled_box_support=set(range(18))
gate('support-size and filled-box cost retained',len(connector)==9 and len(endpoint_label)==2 and len(filled_box_support)==2*len(connector))
guard('completion')
print(json.dumps({'checks':checks,'patch_norms':details,'resources':resources,'scope':'Generic matrix/support mechanism diagnostic. Base actual Yang-Mills precision is the separately reviewed CB input; this test does not identify this covariant cycle matrix with it.'},indent=2))
