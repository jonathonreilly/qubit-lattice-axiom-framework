"""Dense six-site scaling control; supports algebra, not physical calibration."""
import itertools,json,numpy as np
from pathlib import Path
from compass_sector_basis import geometry,dense_terms
sites,bonds=geometry((3,2,1));idx={x:i for i,x in enumerate(sites)};terms=[];local=[];center=idx[(1,0,0)]
for i,j,a in bonds:
 mask=(1<<i)|(1<<j);term=(mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1);terms.append(term)
 if center in [i,j]:local.append(term)
H=dense_terms(terms,64);e=dense_terms(local,64)/2;C=2*e@e-len(local)/2*np.eye(64)
en,U=np.linalg.eigh(H);g=U[:,0];delta=en-en[0];vC=U.T@C@g;ve=U.T@e@g
rows=[];reference={}
for J in [1.,.1,3.,10.]:
 row={'J':J}
 for name,va,vb,a,b in [('CC',vC,vC,0,0),('Ce',vC,ve,0,1),('ee',ve,ve,1,1)]:
  z=J*(1.2+.2j);D=J*delta;value=np.sum(2*D*va*vb*J**(a+b)/(D*D-z*z))
  scaled=value/J**(a+b-1)
  if J==1:reference[name]=scaled
  assert abs(scaled-reference[name])<1e-12
  row[name]=[float(value.real),float(value.imag)]
 rows.append(row)
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows,scope='Fixed dimensionless state, frequency and regulator rescaled with J; no observed clock/ruler/mass identification'),indent=2)+'\n');print(rows)
