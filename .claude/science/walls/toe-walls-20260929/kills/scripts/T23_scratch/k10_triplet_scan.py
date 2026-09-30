import sys, numpy as np
sys.argv=['x']
exec(open('k8_local_lifts_L6.py').read().split('if __name__')[0])
for name in ('C2d','C4z','C3','C2z'):
    for eps in (1,-1):
        l,a,K,k=search(name,eps,30,'triplet',seed=11)
        print(f"{name:4s} eps={eps:+d}: intertwiner dim {k}, best triplet-preserving unitary residual over 30 starts = {l:.3e}",flush=True)
