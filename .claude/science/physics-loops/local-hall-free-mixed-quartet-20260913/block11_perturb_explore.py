from block11_explore import *
from scipy.optimize import root
b=.4;zeta=.7;m=.2;delta=.013
I4=np.eye(4)
def pert(k):
 return delta*(np.kron(tau[1],sig[2])+.31*np.kron(tau[2],sig[1])+(.4*np.cos(k[0])+.23*np.cos(k[1])+.17*np.cos(k[2]))*I4)
def hp(k):return H(k,b,zeta,m)+pert(k)
def reduced(k,ref):
 e,u=np.linalg.eigh(hp(k));P=u[:,1:3]@u[:,1:3].conj().T;v=P@ref;w,Q=np.linalg.eigh(v.conj().T@v);v=v@(Q/np.sqrt(w))@Q.conj().T
 h=v.conj().T@hp(k)@v
 return np.array([np.trace(h@s).real/2 for s in sig]),np.trace(h).real/2
rows=[]
for node in nodes(b,zeta,m):
 _,u=np.linalg.eigh(H(node,b,zeta,m));ref=u[:,1:3]
 sol=root(lambda k:reduced(k,ref)[0],node,tol=1e-11);d,mu=reduced(sol.x,ref)
 step=1e-5;jac=np.array([(reduced(sol.x+step*e,ref)[0]-reduced(sol.x-step*e,ref)[0])/(2*step) for e in np.eye(3)]).T;tilt=np.array([(reduced(sol.x+step*e,ref)[1]-reduced(sol.x-step*e,ref)[1])/(2*step) for e in np.eye(3)])
 rows.append(dict(success=bool(sol.success),node=sol.x.tolist(),residual=float(np.linalg.norm(d)),mu=mu,det=float(np.linalg.det(jac)),tilt=tilt.tolist(),type_I_norm=float(tilt@np.linalg.solve(jac.T@jac,tilt))))
print(json.dumps(dict(rows=rows,symmetry_errors=[float(np.linalg.norm(T@hp(k).conj()@T-hp(-k))) for k in [np.array([.1,.2,.3]),np.array([.4,-.7,1.1])]],PH_defect=float(np.linalg.norm(PH@hp(np.array([.1,.2,.3])).conj()@PH+hp(np.array([.1,.2,.3]))))),indent=2))
(P/'BLOCK11_PERTURB_EXPLORATION.json').write_text(json.dumps(rows,indent=2)+'\n')
