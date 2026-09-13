from pathlib import Path
import json,numpy as np
P=Path(__file__).resolve().parent
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)];I=np.eye(2);tau=sig
S=[np.kron(I,s) for s in sig];T=np.kron(tau[0],I);PH=np.kron(I,sig[1])
def coeff(k,b,zeta,m):
 x,y,z=k;return -np.cos(x)*np.sin(b),np.sin(x)*np.cos(b),2+zeta-np.cos(x)*np.cos(b)-np.cos(y)-np.cos(z),-np.sin(x)*np.sin(b)
def H(k,b,zeta,m):
 a,b1,c,d=coeff(k,b,zeta,m);return np.sin(k[1])*S[1]+a*S[0]+b1*np.kron(tau[2],sig[0])+m*np.kron(tau[0],sig[0])+c*S[2]+d*np.kron(tau[2],sig[2])
def derivative(k,b,zeta,m,i):
 x,y,z=k
 if i==0:return np.sin(x)*np.sin(b)*S[0]+np.cos(x)*np.cos(b)*np.kron(tau[2],sig[0])+np.sin(x)*np.cos(b)*S[2]-np.cos(x)*np.sin(b)*np.kron(tau[2],sig[2])
 if i==1:return np.cos(y)*S[1]+np.sin(y)*S[2]
 return np.sin(z)*S[2]
def E2(k,b,zeta,m):
 a,b1,c,d=coeff(k,b,zeta,m);ss=np.sin(k[1])**2+a*a+b1*b1+m*m+c*c+d*d;split=2*np.sqrt((a*b1+c*d)**2+m*m*(a*a+d*d));return np.array([ss-split,ss+split])
def nodes(b,zeta,m):
 R=np.sqrt(1-m*m);x=np.arccos(np.cos(b)/R);z=np.arccos(1+zeta-R)
 return [np.array([sx*x,0,sz*z]) for sx in [-1,1] for sz in [-1,1]]
def curvature(k,b,zeta,m,i,j):
 e,U=np.linalg.eigh(H(k,b,zeta,m));a=U.conj().T@derivative(k,b,zeta,m,i)@U;bb=U.conj().T@derivative(k,b,zeta,m,j)@U
 return float(2*np.imag(np.sum(a[:2,2:]*bb[2:,:2].T/(e[:2,None]-e[None,2:])**2)))
if __name__=='__main__':
 rng=np.random.default_rng(11);b=.4;zeta=.7;m=.2;rows=[];errors=[]
 for trial in range(12):
  k=rng.uniform(-np.pi,np.pi,3);h=H(k,b,zeta,m);ev=np.linalg.eigvalsh(h);expected=np.sort(np.r_[np.sqrt(E2(k,b,zeta,m)),-np.sqrt(E2(k,b,zeta,m))]);errors.append(dict(spectral=float(max(abs(ev-expected))),TR=float(np.max(abs(T@h.conj()@T-H(-k,b,zeta,m)))),PHS=float(np.max(abs(PH@h.conj()@PH+h))),Hall_TR=max(abs(curvature(k,b,zeta,m,i,j)+curvature(-k,b,zeta,m,i,j)) for i,j in [(0,1),(0,2),(1,2)])))
 for k in nodes(b,zeta,m):
  e,U=np.linalg.eigh(H(k,b,zeta,m));u=U[:,np.argsort(abs(e))[:2]];linear=[u.conj().T@derivative(k,b,zeta,m,i)@u for i in range(3)];matrix=np.array([[np.trace(a@s).real/2 for a in linear] for s in sig]);g=matrix.T@matrix
  a,b1,c,d=coeff(k,b,zeta,m);R=np.sqrt(1-m*m);qx=2*np.sin(k[0])*R*np.exp(1j*b);qz=2*(c-1j*np.cos(k[0])*np.sin(b))*np.sin(k[2]);q=np.array([qx,0,qz]);analytic=(q.conj()[:,None]*q[None,:]).real/(4*np.sin(b)**2);analytic[1,1]=1
  rows.append(dict(node=k.tolist(),energies=e.tolist(),metric=g.tolist(),metric_formula_error=float(np.max(abs(g-analytic))),chirality=float(np.linalg.det(matrix)),expected_sign=int(np.sign(k[0]*k[2])),spectator_gap_expected=float(2*np.sin(b))))
 result=dict(parameters=dict(b=b,zeta=zeta,m=m),errors=errors,nodes=rows);(P/'BLOCK11_EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
