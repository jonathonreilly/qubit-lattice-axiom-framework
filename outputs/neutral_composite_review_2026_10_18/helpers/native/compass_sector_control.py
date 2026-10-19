"""Full-H versus symmetry-sector checks with all signs on eight sites."""
import itertools,json
from pathlib import Path
import numpy as np
from compass_sector_basis import basis,dense_terms,isometry
shape=(2,2,2);d=basis(shape);full=[]
for i,j,a in d['bonds']:
 mask=(1<<i)|(1<<j);full.append((mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
H=dense_terms(full,256);spectra=[];errors=[]
for signs in itertools.product([0,1],repeat=3):
 d=basis(shape,list(signs[:2]),list(signs[2:]));U=isometry(d);h=dense_terms(d['terms'],d['dimension'])
 err=np.linalg.norm(H@U-U@h);assert err<1e-12
 assert np.linalg.norm(U.T@U-np.eye(d['dimension']))<1e-12
 spectra.extend(np.linalg.eigvalsh(h));errors.append(err)
assert np.max(abs(np.sort(spectra)-np.linalg.eigvalsh(H)))<1e-12
out=dict(shape=shape,sectors=8,dimension_each=32,max_intertwiner_error=max(errors),spectrum_error=float(np.max(abs(np.sort(spectra)-np.linalg.eigvalsh(H)))),larger_sector_dimension=basis((3,3,3))['dimension'],scope='Exact symmetry coordinates checked against full open8-site Hamiltonian; no sector identified as global ground')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
