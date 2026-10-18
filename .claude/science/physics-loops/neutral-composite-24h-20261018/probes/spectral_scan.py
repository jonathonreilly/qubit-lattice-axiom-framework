"""Exposed development scan; supplied corner bands, no added interaction."""
from pathlib import Path
import itertools,json,time
import numpy as np
from scipy.special import expit
ROOT=Path(__file__).resolve().parents[5]
d=json.loads((ROOT/'data/collective_corner_response/candidate.json').read_text())
dec=lambda x:np.array(x['real'])+1j*np.array(x['imag'])
sh=np.array(d['shifts']);bl=dec(d['blocks']);M=dec(d['mass_matrix']);mu=d['chemical_potential_development_value']
def bands(k):return np.linalg.eigh(np.einsum('ks,sij->kij',np.exp(1j*k@sh.T),bl))
def stats(e,eo,V,T,qnorm):
 de=eo[:,:,None]-e[:,None,:];pop=expit((mu-e)/T)[:,None,:]-expit((mu-eo)/T)[:,:,None]
 w=pop*abs(V)**2/len(e);good=(de>1e-9)&(w>1e-24)
 x=de[good];w=w[good];total=w.sum()
 if total<1e-24:return {'weight':float(total)}
 order=np.argsort(x);x=x[order];w=w[order];p=w/total;c=np.r_[0,np.cumsum(p)]
 mean=np.dot(p,x);var=np.dot(p,(x-mean)**2)
 def window(width):
  j=np.searchsorted(x,x+width,side='right');a=c[j]-c[:-1];i=int(np.argmax(a));return {'fraction':float(a[i]),'lo':float(x[i]),'width':float(width)}
 return {'weight':float(total),'mean':float(mean),'std':float(np.sqrt(var)),'relative_width':float(np.sqrt(var)/mean),'min_transition':float(x[0]),'max_transition':float(x[-1]),'low_energy_fraction':float(p[x<.2].sum()),'window_fixed_001':window(.01),'window_005q':window(.05*qnorm),'transitions':len(x)}
rows=[];t=time.time()
for N in [4,8,12,16,20,24]:
 k=2*np.pi/N*(np.array(list(itertools.product(range(N),repeat=3)))+.5)
 e,U=bands(k)
 for direction in [[1,0,0],[1,1,1]]:
  p=2*np.pi/N*np.array(direction);pn=np.linalg.norm(p)
  for channel,mat,shift in [('density',np.eye(12),p),('mass',M,p+np.pi)]:
   eo,Uo=bands(k+shift);V=Uo.conj().transpose(0,2,1)@mat@U
   for T in [.03,.01]:
    row={'N':N,'direction':direction,'qnorm':pn,'channel':channel,'T':T,**stats(e,eo,V,T,pn)};rows.append(row)
    print(N,direction,channel,T,round(row['weight'],6),round(row.get('relative_width',0),5),row.get('window_005q'),flush=True)
 # conserved density control
 V=U.conj().transpose(0,2,1)@U
 assert stats(e,e,V,.03,1)['weight']<1e-24
out={'status':'development_only','mu_supplied':mu,'rows':rows,'elapsed_seconds':time.time()-t,'density_q0_control':'pass','interaction_added':False}
Path(__file__).with_name('spectral_scan.json').write_text(json.dumps(out,indent=2)+'\n')
