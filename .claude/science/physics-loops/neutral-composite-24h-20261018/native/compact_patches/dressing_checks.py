from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh
P=Path(__file__).resolve().parent
r=json.loads((P/'boundary_response_32.json').read_text())['rows'][0]
G=np.array(r['centered_gram']);K=np.array(r['centered_H']);Q=np.array(r['centered_H2']);n=len(G);columns=[];defects=[]
for i in range(2):
 c=np.zeros(n);c[i]=1;columns.append(c)
for i in range(2):
 d=np.array([2. if name.startswith(r['labels'][i]+':native-boundary-') else 0. for name in r['labels']]);columns.append(d)
 defect=np.sqrt(max(0,Q[i,i]-2*K[i]@d+d@G@d));bound=(1+abs(r['source_means'][i]))*r['reference_residual'];assert defect<=bound+1e-8
 defects.append(dict(patch=r['labels'][i],native_action_defect=float(defect),reference_residual_bound=float(bound)))
C=np.column_stack(columns);g=C.T@G@C;k=C.T@K@C;q=C.T@Q@C
sv,W=eigh(g);keep=sv>1e-10*max(sv);W=W[:,keep]/np.sqrt(sv[keep]);en,c=eigh(W.T@k@W);c=W@c
res=np.sqrt(np.maximum(0,np.diag(c.T@q@c)-en**2))
out=dict(defects=defects,coherent_native_first_step_energies=en.tolist(),full_H_residuals=res.tolist(),scope='Exact reference-error identity and original-H boundary coefficients; no added interaction or stable-size certificate')
(P/'dressing_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
