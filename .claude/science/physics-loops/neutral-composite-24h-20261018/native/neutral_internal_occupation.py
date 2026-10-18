"""Internal rung excitations in the exact selected32site full-H stationary state."""
from pathlib import Path
import numpy as np,json
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer,mul
P=Path(__file__).resolve().parent;D=basis((2,2,8));s=np.load(P/'stationary_2x2x8_plus.npz');gfull=s['vectors'][:,0];e0=float(s['values'][0]);st=[]
for axis in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[axis]==0)
 st.append(D['reduce_term'](m,m if axis==1 else 0,1))
labels=[]
for t in st:labels.append(float(gfull@apply(gfull,*np.array([t],np.int64).T.copy())))
assert all(abs(abs(x)-1)<1e-8 for x in labels)
signs=[int(round(x)) for x in labels];R=reducer(len(D['free']),st,signs);j=np.arange(R['dimension'],dtype=np.int64);r=np.zeros_like(j)
for k,f in enumerate(R['free']):r|=((j>>k)&1)<<f
cs=[((0,0,1),1),(st[0],signs[0]),(st[1],signs[1]),(mul(*st),signs[0]*signs[1])];g=np.zeros(len(j))
for (f,z,c),sg in cs:
 parity=np.zeros_like(j)
 for b in range(len(D['free'])):
  if z>>b&1:parity^=(r>>b)&1
 g+=sg*c*(1-2*parity)*gfull[r^f]/2
norm=float(g@g);assert abs(norm-1)<1e-8;g/=np.sqrt(norm);del s,gfull,j,r
terms=np.array([R['reduce'](t) for t in D['terms']],np.int64);H=lambda v:apply(v,*terms.T.copy());gres=float(np.linalg.norm(H(g)-e0*g));assert gres<1e-8
rows=[];ground_columns=[]
for zz in range(8):
 chosen=[R['reduce'](t) for t,(i,j,a) in zip(D['terms'],D['bonds']) if a!=2 and D['sites'][i][2]==zz]
 terms=np.array(chosen,np.int64).T.copy()
 hg=apply(g,*terms);h2g=apply(hg,*terms)
 pg=(h2g-2*np.sqrt(2)*hg)/16;pe=(h2g+2*np.sqrt(2)*hg)/16
 ground_columns.append(pg)
 rows.append(dict(rung=zz,transverse_energy=float(g@hg),ground_internal_probability=float(g@pg),zero_internal_probability=float(1-g@pg-g@pe),upper_internal_probability=float(g@pe),projector_norm_check=float(pg@pg-g@pg)))
means=np.array([g@v for v in ground_columns]);cov=np.array(ground_columns)@np.array(ground_columns).T-np.outer(means,means)
assert max(abs(r['projector_norm_check']) for r in rows)<1e-10
result=dict(rows=rows,internal_ground_covariance=cov.tolist(),initial_residual=gres,scope='Fixed selected plane sector exact finite eigenstate. Probabilities of local internal h eigenspaces, not real particles or a ground-sector certificate. Frozen npz eigenstate input.')
(P/'neutral_internal_occupation.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
