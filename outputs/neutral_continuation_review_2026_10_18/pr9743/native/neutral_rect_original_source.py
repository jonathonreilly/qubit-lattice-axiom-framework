import numpy as np,json,time
from pathlib import Path
from neutral_rect_model import sector
from neutral_translation_model import orbit_op
p=Path('/private/tmp/neutral_rect_data');meta=json.loads((p/'ground.json').read_text());D=sector((3,3,4));data=tuple(np.load(p/(x+'.npy'),mmap_mode='r') for x in ['labels','signs','reps','sizes'])+(0,);H=orbit_op(sum(D['H'],[]),data);g=np.load(p/'ground.npy');E0=meta['energies'][0];start=time.time();terms=[]
for x in range(3):
 for y in range(3):
  for z in range(4):terms.append(D['project']((0,(1<<(12*x+4*y+z))^(1<<(12*x+4*y+(z+2)%4)),1)))
C=orbit_op(terms,data);src=C@g;mean=g@src;src-=mean*g;norm=np.linalg.norm(src);q=src/norm;prev=np.zeros_like(q);bp=0;aa=[];bb=[];steps=100
print('original source',mean,norm**2,flush=True)
for j in range(steps):
 v=H@q-E0*q-bp*prev;alpha=q@v;v-=alpha*q;v-=g*(g@v);beta=np.linalg.norm(v);aa.append(alpha)
 if j<steps-1:bb.append(beta)
 prev,q=q,v/beta;bp=beta
 if j%25==24:print('Cz Lanczos',j+1,'sec',time.time()-start,flush=True)
T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);es,U=np.linalg.eigh(T);weights=norm**2*U[0]**2;selected=np.argsort(weights)[-6:][::-1];vs=np.zeros((len(g),len(selected)));q=src/norm;prev=np.zeros_like(q);bp=0
for j in range(steps):
 vs+=q[:,None]*U[j,selected][None,:]
 if j==steps-1:break
 v=H@q-E0*q-bp*prev-aa[j]*q;v-=g*(g@v);prev,q=q,v/bb[j];bp=bb[j]
 if j%25==24:print('Cz reconstruct',j+1,'sec',time.time()-start,flush=True)
peaks=[]
for i,k in enumerate(selected):
 v=vs[:,i];v/=np.linalg.norm(v);hv=H@v;en=v@hv;res=np.linalg.norm(hv-en*v);peaks.append(dict(gap=float(en-E0),residual=float(res),source_weight=float((src@v)**2),accepted=bool(res<1e-7)))
out=dict(source='original Cz=sumZ_r Z_r+2z',mean=float(mean),variance=float(norm**2),peaks=peaks,seconds=time.time()-start,scope='Finite3x3x4 nativeH selectedplane+/q0; givenoriginalreadout, noempiricalidentification')
print(out,flush=True);(p/'original_source.json').write_text(json.dumps(out,indent=2)+'\n')
