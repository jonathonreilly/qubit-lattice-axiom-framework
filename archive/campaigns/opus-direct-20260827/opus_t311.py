"""
T311 - which operator gives the packet's tau0 = 0.04297 a^2?

T310 verified tau0 = a^2/(16 pi^2 I) with I = 0.15493339 to 8 digits by three
independent routes -- but that is the NAIVE d=4 Laplacian and gives
tau0 = 0.040873, 4.9% below the packet's 0.04297. R135 used the framework's own
(Kuhn simplicial) operator, and R132 an improved one, so the discrepancy should
trace to the operator. Test the candidates; whichever reproduces 0.04297
identifies the provenance, and if none does, the packet's number needs a source.
"""
import numpy as np
TARGET=0.04297
def tau0_from(lamfun,L=64):
    k=2*np.pi*np.arange(L)/L
    K=np.meshgrid(k,k,k,k,indexing='ij')
    lam=lamfun(K).ravel(); lam=lam[lam>1e-12]
    I=np.sum(1.0/lam)/L**4
    return 1/(16*np.pi**2*I), I
cands={
 "naive              sum 2(1-cos k)":
    lambda K: sum(2*(1-np.cos(k)) for k in K),
 "Symanzik improved  (4/3)c1 - (1/12)c2":
    lambda K: sum((4.0/3.0)*2*(1-np.cos(k)) - (1.0/12.0)*2*(1-np.cos(2*k)) for k in K),
 "hypercubic w/ diag (Kuhn-like, +1/2 body diags)":
    lambda K: sum(2*(1-np.cos(k)) for k in K)
             + 0.5*sum(2*(1-np.cos(K[i]+K[j])) + 2*(1-np.cos(K[i]-K[j]))
                       for i in range(4) for j in range(i+1,4)),
 "nearest+next-nearest equal weight":
    lambda K: sum(2*(1-np.cos(k)) for k in K)
             + sum(2*(1-np.cos(K[i]+K[j])) + 2*(1-np.cos(K[i]-K[j]))
                   for i in range(4) for j in range(i+1,4)),
}
print(f"target (packet R152): tau0 = {TARGET} a^2\n")
print("  operator                                         I           tau0      dev")
for nm,f in cands.items():
    t,I=tau0_from(f)
    print(f"  {nm:46s} {I:.7f}   {t:.6f}   {t/TARGET-1:+7.2%}")
print("\n  ell_P = sqrt(2 pi tau0) for each (R195: N=6):")
for nm,f in cands.items():
    t,_=tau0_from(f)
    print(f"    {nm:46s} ell_P = {np.sqrt(2*np.pi*t):.4f} a")
print(f"    {'packet 0.04297':46s} ell_P = {np.sqrt(2*np.pi*TARGET):.4f} a")
