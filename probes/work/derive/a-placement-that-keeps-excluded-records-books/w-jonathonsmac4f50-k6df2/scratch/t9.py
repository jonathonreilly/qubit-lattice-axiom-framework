from fiber import *
N=8; m=(1,2)
K,H,H2,P=build(N,*m)
for comp in (0,1):
    Jf=build_J(N,K,comp,R=-1)
    print(comp,"free J: [H,Jf]=",abs(H@Jf-Jf@H).max())
    # eigenvalue check on plane waves: phi=e^{ik1 r} coin vector c; Jf phi = g phi (scalar) 
    k1=2*np.pi*np.array([1,3])/N; k2=K-k1
    g=0.5*(np.sin(2*k1[comp])+np.sin(2*k2[comp]))
    r=np.array([[rx,ry] for rx in range(N) for ry in range(N)])
    ph=np.exp(1j*(r@k1))
    for c in range(4):
        v=np.zeros(4*N*N,complex); v[c::4]=ph
        w=Jf@v
        print("  coin",c,"|Jf v - g v| =",np.linalg.norm(w-g*v), "g=",g)
