"""Large-window check of the Fano factor F(w)=Var/Mean for crowding rules (does s tend to 3?)  L=128, w up to 32."""
import numpy as np
from t62_variance import frozen_state, var_curve
L=128; ws=[1,2,4,8,12,16,24,32]
print("L=%d, 3 seeds; Fano factor F(w)=Var(N_w)/Mean(N_w); if F(w) tends to a constant then Var ~ w^3 (Poisson class)"%L)
print("rule                     density  " + "  ".join("w=%-3d"%w for w in ws) + "   s(16..32) local slope")
for name,A in (("A={0}",[0]),("A={0,1}",[0,1]),("A={0,1,2}",[0,1,2]),("A={0,1,2,3}",[0,1,2,3]),("A={0..4}",[0,1,2,3,4])):
    Fs=[];dens=[];sl=[]
    for sd in range(3):
        rng=np.random.default_rng(500+sd)
        occ,ne,ns=frozen_state(L,A,rng)
        vc=var_curve(occ,ws)
        Fs.append(vc[:,0]/vc[:,1]); dens.append(occ.mean())
        V=vc[:,0]; i16=ws.index(16); i32=ws.index(32)
        sl.append(np.log(V[i32]/V[i16])/np.log(2))
    F=np.mean(Fs,axis=0)
    print("%-24s %.3f    "%(name,np.mean(dens))+"  ".join("%.3f"%f for f in F)+"    %.2f"%np.mean(sl))
