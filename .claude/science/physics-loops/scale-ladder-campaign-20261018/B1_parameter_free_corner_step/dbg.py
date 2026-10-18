exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
Tb1=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/Tb1.npy')
blb=blocks_from(Tb1)
G=Hk(blon,kst)+0.37*Lam+0.23*Hk(blli,kst)
w,V=np.linalg.eigh(G); print(np.round(w,4))
T0=Hk(blb,kst); print("T(k*) hermitian",np.allclose(T0,T0.conj().T),"T^2",np.allclose(T0@T0,2*np.eye(12)), "commutes with G", np.allclose(T0@G,G@T0))
for i in range(11):
    if abs(w[i+1]-w[i])<1e-8 and (i==0 or abs(w[i]-w[i-1])>1e-8) and (i+2>11 or abs(w[i+2]-w[i])>1e-8):
        Psi=V[:,i:i+2]; print("doublet",round(w[i],4),"T on it", np.round(Psi.conj().T@T0@Psi,4))
        for e in np.eye(3):
            d=(Hk(blb,kst+1e-6*e)-Hk(blb,kst-1e-6*e))/2e-6; print("   dT proj",np.round(Psi.conj().T@d@Psi,4).tolist())
