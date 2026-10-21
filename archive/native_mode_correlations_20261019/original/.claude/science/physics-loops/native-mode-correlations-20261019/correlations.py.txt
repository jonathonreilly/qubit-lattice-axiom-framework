"""Anchored native ZZ-bond covariances; no probability or internal-radius interpretation."""
from pathlib import Path
import json
import numpy as np
from compass_sector_basis import basis
from compass_sector_solve import apply
AUDIT_TIMEOUT_SEC = 600
P=Path(__file__).resolve().parent

OUT=P.parents[3]/'outputs/native_mode_correlations_20261019'
OUT.mkdir(parents=True,exist_ok=True)

def measure(E,V,poles):
 d=basis((3,3,3));idx={p:i for i,p in enumerate(d['sites'])}
 # Choose the first returned level with numerically nonzero compact-source weight.
 weights=np.array(poles['normalized_probe_weights'])
 groups=[]
 for i in range(len(E)):
  if not groups or abs(E[i]-E[groups[-1][0]])>=1e-8:groups.append([i])
  else:groups[-1].append(i)
 group=np.array(next(g for g in groups if E[g[0]]-E[0]>1e-8 and weights[:,g].sum(axis=1).max()>1e-8));first=group[0]
 out={'gap':float(E[first]-E[0]),'returned_group_indices':group.tolist(),'scope':'Anchored bond covariance in the ground and uniform mixture of returned eigenvectors. Neither an internal size nor degeneracy completeness is inferred.','states':{}}
 def act(v,p):
  q=(p[0],p[1],(p[2]+1)%3);mask=(1<<idx[p])|(1<<idx[q]);t=np.array([d['reduce_term'](0,mask,1)],dtype=np.int64)
  return apply(v,*t.T.copy())
 for name,cols in [('ground',[0]),('returned_mode_mixture',group)]:
  means=np.zeros(27);pairs=np.zeros(27)
  for col in cols:
   v=V[:,col];av=act(v,(0,0,0))
   for i,p in enumerate(d['sites']):
    bv=act(v,p);means[i]+=float(v@bv)/len(cols);pairs[i]+=float(av@bv)/len(cols)
  covariance=pairs-means[0]*means
  assert abs(covariance[0]-(1-means[0]**2))<1e-10
  out['states'][name]={'mean_bonds':means.tolist(),'anchor_covariance':covariance.tolist(),'anchor_variance':float(covariance[0]),'mean_spread':float(np.ptp(means))}
 out['coordinates']=d['sites'];out['excess_covariance']=(np.array(out['states']['returned_mode_mixture']['anchor_covariance'])-out['states']['ground']['anchor_covariance']).tolist()
 (OUT/'correlations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
 # Called by the eigensolver before its in-memory states are released.
 return out
