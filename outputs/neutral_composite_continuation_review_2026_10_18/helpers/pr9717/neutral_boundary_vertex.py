"""Derive the existing boundary bond's neutral-sector coupling; no added term."""
from pathlib import Path
import numpy as np,json
from scipy.sparse.linalg import LinearOperator,eigsh
from neutral_rung_model import h,Ds
P=Path(__file__).resolve().parent
H=np.kron(h,np.eye(8))+np.kron(np.eye(8),h)-sum(np.kron(d,d) for d in Ds);n=len(H);d=n//2;a=np.arange(d);b=n-1-a
Ws={};Es={};Us={}
for s in [1,-1]:
 W=np.zeros((n,d));W[a,np.arange(d)]=1/np.sqrt(2);W[b,np.arange(d)]=s/np.sqrt(2)
 E,U=np.linalg.eigh(W.T@H@W);Ws[s]=W;Es[s]=E;Us[s]=W@U
left=[Us[-1].T@np.kron(np.eye(8),D)@Us[1] for D in Ds]
right=[Us[-1].T@np.kron(D,np.eye(8))@Us[1] for D in Ds]
V=-sum(np.kron(A,B) for A,B in zip(left,right))
plus=(Es[1][:,None]+Es[1][None,:]).ravel();minus=(Es[-1][:,None]+Es[-1][None,:]).ravel();E0=plus[0];v=V[:,0]
den=minus-E0;second=-float(np.sum(v*v/den));mix=float(np.sum(v*v/den**2));rows=[]
for lam in [.01,.05,.1,.25,.5,1.]:
 def mv(x):return np.r_[plus*x[:d*d]+lam*V.T@x[d*d:],minus*x[d*d:]+lam*V@x[:d*d]]
 op=LinearOperator((2*d*d,2*d*d),matvec=mv,dtype=float)
 e,u=eigsh(op,k=1,which='SA',tol=1e-12,v0=np.random.default_rng(18).normal(size=2*d*d));g=u[:,0]
 rows.append(dict(boundary_multiplier=lam,energy=float(e[0]),second_order_energy=float(E0+lam**2*second),second_order_error=float(e[0]-E0-lam**2*second),residual=float(np.linalg.norm(mv(g)-e[0]*g)),odd_odd_weight=float(g[d*d:]@g[d*d:]),product_ground_weight=float(g[0]**2)))
# Exact elimination of the odd-odd block at full native strength.
e=float(rows[-1]['energy']);gp=g[:d*d];gm=g[d*d:];pred=(V@gp)/(e-minus)
reconstruction_error=float(np.linalg.norm(pred-gm))
Sigma=lambda x:V.T@((V@x)/(e-minus))
feshbach_residual=float(np.linalg.norm(plus*gp+Sigma(gp)-e*gp))
u=gp/np.linalg.norm(gp);minus_sigma_derivative=float(np.sum((V@u)**2/(e-minus)**2))
normalization_prediction=1/(1+minus_sigma_derivative)
assert reconstruction_error<1e-9 and feshbach_residual<1e-9
assert abs(normalization_prediction-float(gp@gp))<1e-9
column=V.T@(v/(e-minus));offdiag=np.linalg.norm(column[1:])
feshbach=dict(odd_reconstruction_error=reconstruction_error,neutral_equation_residual=feshbach_residual,neutral_sector_weight=float(gp@gp),weight_from_energy_derivative=normalization_prediction,minus_self_energy_derivative=minus_sigma_derivative,product_ground_column_diagonal=float(column[0]),product_ground_column_offdiagonal_norm=float(offdiag))
# Exact neutral-neutral first-order blocks vanish, despite a nonzero native V.
block=max(np.max(abs(Us[1].T@np.kron(np.eye(8),D)@Us[1])) for D in Ds)
assert block<1e-12
assert abs(rows[-1]['energy']-json.loads((P/'tube_results/tube_4.json').read_text())['initial_energy'])<1e-8
# Source vertex for an existing region energy observable, without adding it to H.
energies,modes=eigsh(op,k=16,which='SA',tol=1e-11,v0=np.random.default_rng(19).normal(size=2*d*d))
ix=np.argsort(energies);energies=energies[ix];modes=modes[:,ix];g0=modes[:,0]
OLp=np.repeat(Es[1],d);OLm=np.repeat(Es[-1],d);vertex_rows=[]
for k in range(1,len(energies)):
 f=modes[:,k];pf=f[:d*d];pi=g0[:d*d]
 direct=float(np.dot(pf,OLp*pi)+np.dot(f[d*d:],OLm*g0[d*d:]))
 bare=float(np.dot(pf,OLp*pi))
 ri=(V@pi)/(energies[0]-minus);rf=(V@pf)/(energies[k]-minus)
 induced=float(np.dot(rf,OLm*ri));dressed=bare+induced
 assert abs(direct-dressed)<1e-8
 if abs(direct)>1e-7:
  vertex_rows.append(dict(gap=float(energies[k]-energies[0]),direct_native_energy_matrix_element=direct,bare_P_contribution=bare,induced_Q_contribution=induced,dressed_error=abs(direct-dressed),eigen_residual=float(np.linalg.norm(op@f-energies[k]*f))))
assert vertex_rows
out=dict(source_vertex_rows=vertex_rows,feshbach=feshbach,half_rungs=2,physical_qubits=16,uncoupled_energy=float(E0),charged_half_gap=float(Es[-1][0]-Es[1][0]),first_order_even_block_error=float(block),native_boundary_norm=4.,product_source_weight=float(v@v),second_order_energy_coefficient=second,second_order_odd_weight_coefficient=mix,rows=rows,scope='Exact finite native cut interaction. Lambda labels a diagnostic interpolation only; original H has lambda1. No weak-coupling assumption at lambda1, new mediator, universal coupling or 3D limit.')
(P/'neutral_boundary_vertex.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
