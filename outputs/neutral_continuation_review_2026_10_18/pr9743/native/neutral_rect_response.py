import numpy as np,json,time
from pathlib import Path
from neutral_rect_model import sector
from neutral_translation_model import orbit_op
p=Path('/private/tmp/neutral_rect_data');meta=json.loads((p/'ground.json').read_text());D=sector((3,3,4));data=tuple(np.load(p/(x+'.npy'),mmap_mode='r') for x in ['labels','signs','reps','sizes'])+(0,);H=orbit_op(sum(D['H'],[]),data);Hs=[orbit_op(x,data) for x in D['H']];g=np.load(p/'ground.npy');E0=meta['energies'][0];start=time.time();S=orbit_op(D['S'],data);s=S@g;s-=g*(g@s);b=Hs[2]@g-(Hs[0]@g+Hs[1]@g)/2;b-=g*(g@b);qsrc=np.zeros_like(g)
for A in Hs:
 ag=A@g;aag=A@ag;qsrc+=2*A@(H@ag)-E0*aag-H@aag
qmean=g@qsrc;qsrc-=g*qmean
observables=dict(energy_components=[float(g@(a@g)) for a in Hs],Q_mean=float(qmean),Q_variance=float(qsrc@qsrc),S_variance=float(s@s),B_variance=float(b@b),Q_S_connected=float(qsrc@s),Q_B_connected=float(qsrc@b));print(observables,flush=True);(p/'observables.json').write_text(json.dumps(observables,indent=2)+'\n');rows=[]
for name,src in [('plaquette',s),('directional',b)]:
 norm=np.linalg.norm(src);q=src/norm;prev=np.zeros_like(q);bp=0;aa=[];bb=[];steps=100
 for j in range(steps):
  v=H@q-E0*q-bp*prev;alpha=q@v;v-=alpha*q;v-=g*(g@v);beta=np.linalg.norm(v);aa.append(alpha)
  if j<steps-1:bb.append(beta)
  prev,q=q,v/beta;bp=beta
  if j%25==24:print(name,'Lanczos',j+1,'sec',time.time()-start,flush=True)
 T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);es,U=np.linalg.eigh(T);weights=norm**2*U[0]**2;selected=np.argsort(weights)[-6:][::-1];vs=np.zeros((len(g),len(selected)));q=src/norm;prev=np.zeros_like(q);bp=0
 for j in range(steps):
  vs+=q[:,None]*U[j,selected][None,:]
  if j==steps-1:break
  v=H@q-E0*q-bp*prev-aa[j]*q;v-=g*(g@v);prev,q=q,v/bb[j];bp=bb[j]
  if j%25==24:print(name,'reconstruct',j+1,'sec',time.time()-start,flush=True)
 peaks=[]
 for i,k in enumerate(selected):
  v=vs[:,i];v/=np.linalg.norm(v);hv=H@v;en=v@hv;res=np.linalg.norm(hv-en*v);peaks.append(dict(gap=float(en-E0),residual=float(res),source_weight=float((src@v)**2),Q_weight=float((qsrc@v)**2),accepted=bool(res<1e-7)))
 row=dict(source=name,variance=float(norm**2),peaks=peaks);rows.append(row);print(row,flush=True);(p/'response.json').write_text(json.dumps(dict(rows=rows,scope='Finite rectangular36site plane+/q0 sector; geometry breaks cubic symmetry, no scalar-irrep or infinitevolume claim',seconds=time.time()-start),indent=2)+'\n')
 del vs
