import numpy as np
from t72_pair_band2 import W_pair_sparse
print("small-m scan: (W-1)/(B/2m); NR + clock-alone + contact predicts -4 (=1+2<U>/M, <U>=-2B, M=2m)")
for m,lams,R in ((0.25,(0.15,0.3,0.45,0.6),400),(0.1,(0.06,0.12,0.18,0.24),900)):
    print(f"m={m}")
    for lam in lams:
        W,E0,d2=W_pair_sparse(lam,1.0,m,R,dK=0.02)
        B=2*m-E0
        print(f"  lam={lam:5.3f} B={B:9.6f} B/2m={B/(2*m):8.5f} kappa~{np.sqrt(m*B):.4f}  W={W:9.5f}  (W-1)/(B/2m)={(W-1)/(B/(2*m)):8.3f}")
