#!/usr/bin/env python3
"""T28 Test D: lattice-native finite step (6 quarter-turns, SU(2) lift) as the one-tick kernel. See PREREG.md."""
import numpy as np
out=[]
def P(*a):
    s=" ".join(str(x) for x in a); print(s); out.append(s)
th=np.pi/2   # rotation angle; SU(2) eigenphases +-th/2
P("spin j   C_2      chi_j      lambda_j=chi/(2j+1)   tau_j = 2(-ln lambda)/C_2")
ok=True
for j2 in range(1,7):
    j=j2/2; c2=j*(j+1)
    chi=np.sin((j2+1)*th/2)/np.sin(th/2)
    lam=chi/(j2+1)
    tau = 2*(-np.log(lam))/c2 if lam>0 else float('nan')
    P(f"{j:5.1f}  {c2:6.3f}  {chi:8.4f}  {lam:12.5f}          {tau:8.4f}" + ("   <-- NEGATIVE eigenvalue" if lam<0 else ""))
    if lam<0: ok=False
# lazy step: hold with probability p
P("\nLazy version: K = p*delta + (1-p)*K6.  lambda_j(p) = p + (1-p) lambda_j.  Smallest p making all lambda_j>=0 for j<=6:")
lams=[np.sin((j2+1)*th/2)/np.sin(th/2)/(j2+1) for j2 in range(1,13)]
pmin=max(0.0, max(-l/(1-l) for l in lams if l<1))
P(f"   p_min = {pmin:.4f}; tau_1/2(p=p_min) = {2*(-np.log(pmin+(1-pmin)*lams[0]))/0.75:.4f}, tau_1(p=p_min) = {2*(-np.log(pmin+(1-pmin)*lams[1]))/2.0:.4f}")
P("   tau_{1/2}(p) as p varies:", ", ".join(f"p={p:.1f}:{2*(-np.log(p+(1-p)*lams[0]))/0.75:.3f}" for p in (0,0.2,0.5,0.8)))
P("READING D:", "PASS" if ok else "FAIL (negative eigenvalues: the bare native step is not a positive kernel; any repair adds a holding probability p = a free rate)")
open("testD_output.txt","w").write("\n".join(out)+"\n")
