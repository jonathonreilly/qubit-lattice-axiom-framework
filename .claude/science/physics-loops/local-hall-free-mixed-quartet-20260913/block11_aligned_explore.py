from block11_explore import *
rows=[]
for b,zeta,mu in [(.4,.7,.2),(.8,.6,.5),(.2,.9,.3)]:
 R=np.sqrt(1-mu*mu);x=np.arccos(R*np.cos(b));z=np.arccos(1+zeta-R)
 def hh(k):return H(k,b,zeta,mu*np.sin(b))+mu*np.cos(b)*np.kron(tau[0],sig[2])
 for sx in [-1,1]:
  for sz in [-1,1]:
   k=np.array([sx*x,0,sz*z]);e,U=np.linalg.eigh(hh(k));u=U[:,1:3];v=[u.conj().T@derivative(k,b,zeta,0,i)@u for i in range(3)];J=np.array([[np.trace(a@s).real/2 for a in v] for s in sig]);expected=np.diag([R*R,1,R*R*np.sin(b)**2*np.sin(z)**2/np.sin(x)**2]);rows.append(dict(b=b,zeta=zeta,mu=mu,node=k.tolist(),energies=e.tolist(),metric=(J.T@J).tolist(),metric_error=float(np.linalg.norm(J.T@J-expected)),det=float(np.linalg.det(J)),spectator_gap_expected=float(2*np.sin(x))))
print(json.dumps(rows,indent=2));(P/'BLOCK11_ALIGNED_EXPLORATION.json').write_text(json.dumps(rows,indent=2)+'\n')
