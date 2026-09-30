import numpy as np
rng = np.random.default_rng(11)
M = 4_000_000
A = (rng.normal(size=(M,3,3))+1j*rng.normal(size=(M,3,3)))/np.sqrt(2)
s = np.linalg.svd(A, compute_uv=False)
r2 = s[:,1]/s[:,0]; r3 = s[:,2]/s[:,0]
# joint probability P(r2<x, r3<y): fit C in  P = C x^6 y^2  in the regime y << x << 1
print("P(r2<x, r3<y)   measured      C = P/(x^6 y^2)")
Cs = []
for x,y in [(0.3,0.06),(0.25,0.04),(0.2,0.03),(0.15,0.02)]:
    P = np.mean((r2<x)&(r3<y)); C = P/(x**6*y**2); Cs.append(C)
    print(f"  x={x:<5} y={y:<5}  {P:.3e}   {C:.3g}")
C = np.median(Cs)
x, y = 3*7.4e-3, 3*7.5e-6
print(f"extrapolated P(r2<{x:.3g}, r3<{y:.3g}) ~ C x^6 y^2 = {C*x**6*y**2:.2e}  (C~{C:.3g}; small-x,y scaling law, not sampled)")
print(f"single-ratio: P(r3<{y:.3g}) ~ 18.4 y^2 = {18.4*y**2:.2e}")
