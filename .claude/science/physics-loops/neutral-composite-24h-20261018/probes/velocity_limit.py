"""Leading intraband density spectrum at small q, finite T; development only."""
from pathlib import Path
import numpy as np,json,itertools
from scipy.special import expit
R=Path(__file__).resolve().parents[5];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);mu=d['chemical_potential_development_value'];rows=[]
for N in [12,24,36]:
 k=2*np.pi/N*(np.array(list(itertools.product(range(N),repeat=3)))+.5)
 phase=np.exp(1j*k@sh.T);h=np.einsum('ks,sij->kij',phase,bl);e,U=np.linalg.eigh(h)
 for direction in [np.array([1.,0,0]),np.ones(3)/np.sqrt(3)]:
  dh=np.einsum('ks,sij->kij',phase*(1j*(sh@direction))[None,:],bl)
  v=np.einsum('kij,kij->kj',U.conj(),dh@U).real
  for T in [.03,.01]:
   f=expit((mu-e)/T);w=f*(1-f)/T*np.maximum(v,0)/len(k);good=w>1e-20;x=v[good];ww=w[good];total=ww.sum();p=ww/total;mean=np.dot(p,x);std=np.sqrt(np.dot(p,(x-mean)**2));order=np.argsort(x);x=x[order];p=p[order];cs=np.r_[0,np.cumsum(p)]
   widths={}
   for delta in [.05,.01,.002]:
    j=np.searchsorted(x,x+delta,side='right');mass=cs[j]-cs[:-1];i=mass.argmax();widths[str(delta)]={'max_fraction':float(mass[i]),'start':float(x[i])}
   row={'N':N,'direction':direction.tolist(),'T':T,'positive_weight_over_q':float(total),'mean_velocity':float(mean),'std_velocity':float(std),'relative_width':float(std/mean),'windows':widths};rows.append(row);print(row,flush=True)
Path(__file__).with_name('velocity_limit.json').write_text(json.dumps({'scope':'Supplied grand canonical finite-temperature states; leading intraband response; no scalar or observed speed identified','rows':rows},indent=2)+'\n')
