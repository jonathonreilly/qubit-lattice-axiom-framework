exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
U=np.eye(12)-2*Ps[2]
W=lambda k: RL(k)@U
for k in (kst+np.array([0.3,-0.2,0.5]),np.array([1.,2.,-0.7])):
    M=W(k); print("unitary off-grid:",np.allclose(M@M.conj().T,np.eye(12)))
# node space at k*: eigenvalue 1
e,V=np.linalg.eig(W(kst)); idx=np.where(np.abs(np.angle(e))<1e-7)[0]
Q,_=np.linalg.qr(V[:,idx]); print("node dim",Q.shape[1])
# effective generator: H_eff(q) = i log W ~ first order: K_i = Q^dag (i dW_i W^-1) Q
W0=W(kst); h=1e-6
K=[Q.conj().T@(1j*((W(kst+h*e)-W(kst-h*e))/(2*h))@np.linalg.inv(W0))@Q for e in np.eye(3)]
for i in range(3): print("K%d herm"%i, np.allclose(K[i],K[i].conj().T,atol=1e-7), "eig", np.round(np.linalg.eigvalsh((K[i]+K[i].conj().T)/2),8))
Kh=[(k+k.conj().T)/2 for k in K]
# kernel common? project out the zero (flat) part
ev,Vv=np.linalg.eigh(sum(k@k for k in Kh)); print("sum K^2 eig",np.round(ev,8))
D=Vv[:,np.abs(ev)>1e-6]; Kd=[D.conj().T@k@D for k in Kh]
v2=np.trace(Kd[0]@Kd[0]).real/D.shape[1]
err=max(np.linalg.norm(a@b+b@a-(2*v2*np.eye(D.shape[1]) if i==j else 0)) for i,a in enumerate(Kd) for j,b in enumerate(Kd))
print("dispersing dim",D.shape[1],"Clifford residual",err,"v",np.sqrt(v2),"1/sqrt3",1/np.sqrt(3))
