import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import geometry,dense_terms
sites,bonds=geometry((3,2,1));n=len(sites);terms=[]
for i,j,a in bonds:
 mask=(1<<i)|(1<<j);terms.append((mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
H=dense_terms(terms,1<<n);ix=sites.index((1,0,0));et=[t for t,(i,j,a) in zip(terms,bonds) if ix in (i,j)]
e=dense_terms(et,1<<n)/2;C=2*e@e-len(et)*np.eye(1<<n)/2
E,U=np.linalg.eigh(H);A=U.T@C@U;B=U.T@H@U
rows=[]
for beta in [.1,.5,1,2]:
 def mean(J):
  p=np.exp(-beta*J*(E-E.min()));p/=p.sum();return np.dot(p,np.diag(A))
 p=np.exp(-beta*(E-E.min()));p/=p.sum()
 cov=np.dot(p,np.diag(A)*E)-np.dot(p,np.diag(A))*np.dot(p,E)
 # H(lambda)=(1-lambda)H; derivative +beta covariance at fixed beta.
 h=1e-5;fd=(mean(1-h)-mean(1+h))/(2*h)
 D=E[None,:]-E[:,None];weights=(p[:,None]-p[None,:])*A*B.T
 response=np.sum(weights/(D-(.7+.2j)))
 assert abs(response)<1e-12
 assert abs(fd-beta*cov)<1e-8
 rows.append(dict(beta=beta,isothermal_derivative=float(beta*cov),finite_difference=float(fd),retarded_absolute=float(abs(response))))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
