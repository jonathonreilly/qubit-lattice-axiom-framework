import sys, numpy as np
sys.argv=['x']
exec(open('k8_local_lifts_L6.py').read().split('if __name__')[0])
def support(a): return [int((np.abs(a[:,pr])>1e-6).sum()) for pr in range(8)]
print("== validation: unrestricted unitary lifts, several random starts")
for name,eps in (('E',1),('C2d',1),('C4z',1),('C3',1)):
    for seed in range(3):
        l,a,K,k=search(name,eps,1,'free',seed=seed)
        T=K[np.ix_(triplet,triplet)]; leak=np.linalg.norm(K[np.ix_(rest,triplet)])
        print(f"{name:4s} eps={eps:+d} seed{seed}: loss={l:.1e} row supports per parity={support(a) if l<1e-10 else '-'}  leakage triplet->rest={leak:.3f}")
