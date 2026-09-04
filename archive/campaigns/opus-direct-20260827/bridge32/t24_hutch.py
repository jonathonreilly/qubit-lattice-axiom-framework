"""T24 - what a Hutchinson/Chebyshev estimator would have cost here, computed exactly.

dW/ds_e needs the matrix elements F(B)_{a,a+delta} for the ~31 offsets inside a
Kuhn simplex star.  A Rademacher probe z estimates F(B)_{ab} by z_b (F(B) z)_a,
whose per-probe variance is  sum_c F(B)_{ac}^2 - F(B)_{ab}^2.  On the flat lattice
F(B)_{ac} = phi(a-c) and Parseval gives  sum_c phi(c)^2 = N^-1 sum_k F(lambda_k)^2,
while the target is phi(delta) = N^-1 sum_k F(lambda_k) e^{i k.delta}.
So the per-probe relative sigma is sqrt(sum_k F^2 / N) / |phi(delta)| exactly."""
import numpy as np
L=32; N=L**4
n=np.arange(L); m=2*(1-np.cos(2*np.pi*n/L))
K1=np.array([2*np.pi*n/L])
print(f"T24  L={L}, N={N}, improved operator, m=0 (zero mode deflated)")
print(f"{'tau0':>6} {'sig/|phi(0)|':>13} {'probes for 1%':>14} {'sig/|phi(nn)|':>14} "
      f"{'probes for 1%':>14}")
lam=(m[:,None,None,None]+m[None,:,None,None]+m[None,None,:,None]+m[None,None,None,:])
mu=lam+lam*lam/24.0; mup=1+lam/12.0
ph=np.exp(1j*2*np.pi*n/L)                       # phase for a unit offset in one direction
for tau0 in (2.7,4.0,6.0,8.0):
    F=np.where(mu>1e-12,np.exp(-tau0*mu)*mup/np.where(mu>1e-12,mu,1.0),0.0)
    F=F.copy(); F[0,0,0,0]=0.0
    s2=float((F**2).sum())/N
    phi0=float(F.sum())/N
    phinn=float(np.real((F*ph[:,None,None,None]).sum()))/N
    for tgt,nm in ((phi0,'onsite'),(phinn,'nn')):
        pass
    r0=np.sqrt(s2)/abs(phi0); rn=np.sqrt(s2)/abs(phinn)
    print(f"{tau0:6.2f} {r0:13.1f} {(r0/0.01)**2:14.3e} {rn:14.1f} {(rn/0.01)**2:14.3e}")
print()
print("HONEST QUALIFICATION.  dW/ds_e is identical for all L^3 spatial translates of an")
print("edge, so a single probe already delivers L^3 = %d independent samples of it;" % L**3)
print("that cuts the probe count by L^3 and the subsequent 15L-point fit by another")
print("~n_fit/(1-corr^2).  With common random numbers across the background subtraction")
print("(needed: the signal is only ~3%% of dW) B could be reached to ~1%% with O(10) probes.")
print("So Hutchinson was not hopeless -- but the translation symmetry that rescues it is")
print("exactly the symmetry that makes the problem EXACTLY solvable:")
print(f"  {L**3} eigendecompositions of tridiagonal {L}x{L} blocks = {L**3*L**3:.2e} flops,")
print("  seconds of wall time, validated against a dense N x N reference to 2e-13 (T06).")
print("  Stochastic estimation would have bought nothing and cost accuracy.")
