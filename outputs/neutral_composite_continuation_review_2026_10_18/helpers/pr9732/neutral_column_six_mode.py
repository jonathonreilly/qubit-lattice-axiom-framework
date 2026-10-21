"""Four-defect translation fibers in the + row/column-X symmetry quotient; includes native rectangle term."""
from pathlib import Path
import numpy as np,json
from scipy.linalg import eigh
from scipy.optimize import brentq

def graph(n,mx=0,my=0):
 def bit(x,y):return 1<<((x%n)*n+y%n)
 def rect(x,a,y,b):return bit(x,y)^bit(a,y)^bit(x,b)^bit(a,b)
 shapes=[(a,b) for a in range(1,n//2+1) for b in range(1,n//2+1) if not (2*a==n and mx%2) and not (2*b==n and my%2)];ix={s:i for i,s in enumerate(shapes)}
 sizes=np.array([n*n/((2 if a*2==n else 1)*(2 if b*2==n else 1)) for a,b in shapes])
 masks=[rect(x,x+2,y,y+1) for x in range(n) for y in range(n)]+[rect(x,x+1,y,y+2) for x in range(n) for y in range(n)]
 H=np.zeros((len(shapes),len(shapes)),dtype=complex)
 for i,(a,b) in enumerate(shapes):
  s=rect(0,a,0,b)
  for m in masks:
   d=s^m
   if d.bit_count()!=4:continue
   points=[]
   while d:
    bitval=d&-d;k=bitval.bit_length()-1;points.append((k//n,k%n));d-=bitval
   xs=sorted(set(x for x,y in points));ys=sorted(set(y for x,y in points))
   assert len(xs)==len(ys)==2
   da=xs[1]-xs[0];db=ys[1]-ys[0];key=(min(da,n-da),min(db,n-db))
   if key not in ix:continue
   j=ix[key];cx=(xs[0] if da<=n/2 else xs[1])+key[0]/2;cy=(ys[0] if db<=n/2 else ys[1])+key[1]/2
   phase=np.exp(2j*np.pi*(mx*(cx-a/2)+my*(cy-b/2))/n)
   H[j,i]-=phase*np.sqrt(sizes[i]/sizes[j])
 assert np.max(np.abs(H-H.T.conj()))<1e-12
 source=np.zeros(len(shapes));source[ix[1,2]]=source[ix[2,1]]=-1
 # Every defect costs8K6 in isolation; adjacent pairs save4K6 each.
 diag=np.array([32-4*(2*(a==1)+2*(b==1)) for a,b in shapes])
 return H,diag,source,shapes
rows=[];gamma=51/64;delta=8*gamma
for n in [12,20,40,60]:
 H,d,s,shapes=graph(n);active=set(np.flatnonzero(s));front=list(active)
 while front:
  i=front.pop()
  for j in np.flatnonzero(H[:,i]):
   if j not in active:active.add(j);front.append(j)
 ids=sorted(active);B=H[np.ix_(ids,ids)]+np.diag(gamma*(d[ids]-24));e,u=eigh(B);weights=np.abs(s[ids]@u)**2
 rows.append(dict(n=n,complete_q0_shapes=len(shapes),source_component=len(ids),upper=float(e[-1]),upper_weight=float(weights[-1]),lower=float(e[0]),source_norm2=float(s@s),symmetry_error=float(np.max(np.abs(H-H.T.conj())))))
 print(rows[-1],flush=True)
def g(e):return (e-np.sign(e)*np.sqrt(e*e-16))/8
E=brentq(lambda e:e-delta-8*g(e)-8*g(e-delta),delta+4+1e-10,delta+20)
ga,gb=g(E),g(E-delta);Z=1/(1+2*(2*ga)**2/(1-(2*ga)**2)+2*(2*gb)**2/(1-(2*gb)**2));weight=16*ga*ga*Z
curvature=Z*(-16*ga**3/(1-4*ga*ga)-ga-gb-4*gb**3/(1-4*gb*gb))
out=dict(upper_q_squared_curvature=float(curvature),physical_readout_weight_over_t_squared=float((63/20)**2*weight),gamma=gamma,delta=delta,upper=float(E),upper_binding=float(E-delta-4),source_weight=float(weight),lower_threshold=float(4*np.sqrt(2)-4),rows=rows,scope='Order-six column operator/source component; unknown common single-plaquette mass correction excluded; no exact native pole')
qchecks=[]
for mx,my in [(1,0),(1,1),(2,0)]:
 n=60;H,d,s,shapes=graph(n,mx,my);active=set(np.flatnonzero(s));front=list(active)
 while front:
  i=front.pop()
  for j in np.flatnonzero(np.abs(H[:,i])>1e-12):
   if j not in active:active.add(j);front.append(j)
 ids=sorted(active);ev=eigh(H[np.ix_(ids,ids)]+np.diag(gamma*(d[ids]-24)),eigvals_only=True)[-1]
 qx,qy=2*np.pi*mx/n,2*np.pi*my/n;ax,ay=2*np.cos(qx/2),2*np.cos(qy/2);bx,by=2*np.cos(qx),2*np.cos(qy)
 def gbfun(e,b):return (e-np.sqrt(e*e-4*b*b))/(2*b*b)
 pred=brentq(lambda e:e-delta-ay*ay*gbfun(e,bx)-ax*ax*gbfun(e,by)-ay*ay*gbfun(e-delta,ay)-ax*ax*gbfun(e-delta,ax),delta+2*max(ax,ay)+1e-10,delta+20)
 assert abs(ev-pred)<2e-5
 qchecks.append(dict(mx=mx,my=my,n=n,native_coefficient_finite=float(ev),halfline_prediction=float(pred)))
out['momentum_checks']=qchecks
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
