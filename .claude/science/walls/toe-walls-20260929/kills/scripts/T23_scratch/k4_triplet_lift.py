#!/usr/bin/env python3
"""K4: range<=1 unitary local lifts A P_g (A D' = eps D A) that PRESERVE the hw=1 triplet subspace (no leakage).
Report best residual and, if exact, the permutation/phase pattern of the triplet action."""
import sys, numpy as np
sys.argv=[sys.argv[0]]+sys.argv[1:]
exec(open('k3_label_lift.py').read().split('if __name__')[0])
name=sys.argv[1]; eps=int(sys.argv[2]); nt=int(sys.argv[3])
l,A,Kf=attempt(name,eps,ntry=nt,mode='triplet',seed=7)
T=Kf[np.ix_(triplet,triplet)]
print(f"{name} eps={eps:+d} triplet-preserving lift: best loss {l:.3e}")
if l<1e-12:
    print("  |triplet block|:\n",np.round(np.abs(T),3))
    print("  monomial lift?",all((np.abs(A[i])>1e-8).sum()==1 for i in range(N)), " max row support",max((np.abs(A[i])>1e-8).sum() for i in range(N)))
