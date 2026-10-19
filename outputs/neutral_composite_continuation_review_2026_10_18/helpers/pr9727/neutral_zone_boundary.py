import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_scalar_explicit_basis import basis
from neutral_kink_core import band
rows=[]
for L in [6,8,10,12,14,16,20]:
 H1,H2,H3,states,src=band(L,third=True);U,labels,zeros=basis(L,L//2,states);A=U.conj().T@(H2@U);vals,vec=np.linalg.eigh(A)
 powers=[8**j for j in range(L)];lookup={st:i for i,st in enumerate(states)};dst=[];qs=[]
 for st in states:
  ds=[st//p%8 for p in powers];ref=[ds[(-j)%L] for j in range(L)]
  dst.append(lookup[sum(x*p for x,p in zip(ref,powers))]);qs.append((-1)**sum((x&3).bit_count() for x in ds))
 RU=np.zeros_like(U);RU[np.array(dst)]=U;QU=np.array(qs)[:,None]*U
 par=np.array([(-1)**(ell-1) for kind,ell in labels]);symerr=max(np.linalg.norm(RU-U*par),np.linalg.norm(RU+QU))
 assert symerr<2e-11
 assert np.linalg.norm(H1@U)<2e-11 and np.linalg.norm(H3@U)<2e-11
 source=np.zeros(len(labels));source[0]=1
 row=dict(L=L,labels=labels,H1norm=float(np.linalg.norm(H1@U)),H3norm=float(np.linalg.norm(H3@U)),H2=np.round(A.real,12).tolist(),imaginary_error=float(np.linalg.norm(A.imag)),reflection_checkerboard_error=float(symerr),energies=vals.tolist(),source_weights=abs(vec[0,:])**2)
 row['source_weights']=row['source_weights'].tolist();rows.append(row);print(row,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
