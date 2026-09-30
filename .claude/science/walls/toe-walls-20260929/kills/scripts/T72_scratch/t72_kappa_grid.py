import numpy as np
from t72_kappa_scan import W_of
ks=[-3,-2,-1.5,-1,-0.5,0,0.5]
print("W_pair-1 (timed) on a kappa grid; blank = bound level lost/merged")
print("lam   "+"  ".join(f"k={k:5.1f}" for k in ks))
for lam in (0.2,0.3,0.45,0.6):
    row=[]
    for k in ks:
        try:
            W,E0=W_of(lam,k); row.append(f"{W-1:+8.3f}" if (2-E0)>1e-3 else "   n/a  ")
        except Exception as e: row.append("   err  ")
    print(f"{lam:4.2f}  "+"  ".join(row))
