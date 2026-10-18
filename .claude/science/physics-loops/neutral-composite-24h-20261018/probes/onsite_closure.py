"""All onsite neutral bilinear eigenoperators for supplied hopping matrices, numerical rank."""
from pathlib import Path
import numpy as np,json
R=Path(__file__).resolve().parents[5];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);I=np.eye(12)
B0=bl[np.all(sh==0,axis=1)][0];L0=np.kron(I,B0)-np.kron(B0.T,I);e,U=np.linalg.eigh(L0)
groups=[]
for i,x in enumerate(e):
 if not groups or abs(x-e[groups[-1][0]])>1e-8:groups.append([i])
 else:groups[-1].append(i)
rows=[]
for q in [np.zeros(3),np.array([.1,0,0]),np.array([.3,0,0]),np.array([np.pi/2,0,0]),np.ones(3)*np.pi,np.ones(3)*.1]:
 Ks=[np.exp(1j*np.dot(s,q))*np.kron(I,b)-np.kron(b.T,I) for s,b in zip(sh,bl) if np.any(s)]
 C=np.concatenate(Ks,axis=0);G=C.conj().T@C;found=[];mins=[]
 for inds in groups:
  V=U[:,inds];gg=V.conj().T@G@V;g,W=np.linalg.eigh(gg);mins.append(float(g.min()))
  keep=g<1e-12
  if keep.any():
   for v in (V@W[:,keep]).T:
    M=v.reshape(12,12,order='F');freq=float(e[inds].mean());res=np.linalg.norm(C@v)
    found.append({'omega':freq,'residual':float(res),'trace_abs':float(abs(np.trace(M)))})
 row={'q':q.tolist(),'modes':found,'minimum_squared_leakage_across_onsite_eigenfrequency_groups':min(mins),'frequency_groups':len(groups)};rows.append(row);print(row,flush=True)
Path(__file__).with_name('onsite_closure.json').write_text(json.dumps({'scope':'All144 onsite orbital bilinears; numerical frequency grouping1e-8, Gram kernel threshold1e-12; not extended operators','rows':rows},indent=2)+'\n')
