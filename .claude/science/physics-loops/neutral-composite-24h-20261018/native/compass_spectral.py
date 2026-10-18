"""Krylov spectral measures of native composite; finite tori, supplied ground state."""
from pathlib import Path
import itertools,json,numpy as np
from scipy.linalg import eigh_tridiagonal
from compass_scalar import operator
P=Path(__file__).resolve().parent;rows=[]
for shape in [(3,2,2),(4,2,2)]:
 sites=list(itertools.product(*(range(x) for x in shape)));idx={x:i for i,x in enumerate(sites)};bonds=[]
 for x,i in idx.items():
  for a in range(3):
   y=list(x);y[a]=(y[a]+1)%shape[a];bonds.append((i,idx[tuple(y)],a,1.))
 H=operator(shape,bonds);saved=np.load(P/('ground_'+'x'.join(map(str,shape))+'.npz'));G=saved['vectors'];E=float(saved['energy'])
 for qx in [0.,2*np.pi/shape[0]]:
  terms=[]
  for x in sites:
   for a in range(3):
    l=list(x);r=list(x);l[a]=(l[a]-1)%shape[a];r[a]=(r[a]+1)%shape[a];terms.append((idx[tuple(l)],idx[tuple(r)],a,np.exp(1j*qx*x[0])))
  C=operator(shape,terms);alllines=[];controls=[];totalweight=0.
  for gi in range(G.shape[1]):
   v=C@G[:,gi];v-=G@(G.conj().T@v);weight=float(np.vdot(v,v).real)/G.shape[1];totalweight+=weight
   if weight<1e-16:continue
   v/=np.linalg.norm(v);basis=[];aa=[];bb=[];prev=np.zeros_like(v);beta=0.
   for step in range(128):
    basis.append(v.copy());w=H@v-E*v-beta*prev;alpha=float(np.vdot(v,w).real);w-=alpha*v
    B=np.array(basis).T
    for repeat in range(2):w-=B@(B.conj().T@w);w-=G@(G.conj().T@w)
    bn=float(np.linalg.norm(w));aa.append(alpha)
    if len(aa) in [32,64,128] or bn<1e-10:
     ev,U=eigh_tridiagonal(np.array(aa),np.array(bb));ww=U[0]**2
     controls.append(dict(ground=gi,steps=len(aa),weight_sum=float(ww.sum()),mean=float(ww@ev),resolvent_imag=[float(np.sum(ww*(.1/(ev**2+.1**2)))),float(np.sum(ww*(.5/(ev**2+.5**2))))]))
    if bn<1e-10 or step==127:break
    bb.append(bn);prev=v;v=w/bn;beta=bn
   alllines.extend(dict(delta=float(en),weight=float(weight*z)) for en,z in zip(ev,ww) if z>1e-12)
  row=dict(shape=shape,qx=qx,ground_vectors=G.shape[1],weight_per_site=totalweight/len(sites),quadrature_lines=alllines,controls=controls)
  print(shape,qx,'weight/site',row['weight_per_site'],'strong lines',sorted(alllines,key=lambda x:-x['weight'])[:4],flush=True);rows.append(row)
(P/'compass_spectral.json').write_text(json.dumps(dict(scope='Finite-torus Krylov quadrature, supplied low-energy eigenspace, no thermodynamic particle claim',rows=rows),indent=2)+'\n')
