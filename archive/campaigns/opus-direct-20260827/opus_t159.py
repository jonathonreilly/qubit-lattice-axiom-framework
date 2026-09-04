"""T159 - DOES THE FULL AXIOM-DERIVED RULE GIVE  |lambda|^2 = m^2 + c^2 k^2 ?

R95 handled the curl channel alone: omega = |k|/3, a light cone.  The other two
channels are still there.  At k = 0 the symbol is (alpha + beta/3) I -- a constant
offset -- so the natural question is whether the FULL symbol's eigenvalue
magnitude assembles into the relativistic invariant

        |lambda(k)|^2  =  m^2 + c^2 |k|^2 + O(k^4),    m = alpha + beta/3,  c = delta/3

which is the structure the campaign previously obtained (R2/R5) by ASSUMING a
Kahler-Dirac operator on Z^4.  Getting it here would mean it follows from the
axioms instead.

There is also a selection question hiding in the beta channel.  Expanding,
   sum_a cos(k_a) e_a e_a^T = I - (1/2) diag(k_a^2)
so beta injects an ANISOTROPIC O(k^2) term, while alpha's contribution
   sum_a cos(k_a) = 3 - |k|^2/2
is isotropic.  If emergent isotropy is required, beta may be forced to zero --
which would narrow the rule further, from four parameters to three.

Measure both: (i) the fit of |lambda|^2 to m^2 + c^2 k^2, and (ii) the anisotropy
as a function of beta, cleanly this time (beta varied with alpha and delta FIXED)."""
import numpy as np
E=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.])]
def cross_mat(u): return np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
def symbol(k,al,be,de):
    c=np.cos(k); s=np.sin(k)
    M=al*2*c.sum()*np.eye(3,dtype=complex)
    M=M+be*2*sum(c[a]*np.outer(E[a],E[a]) for a in range(3))
    M=M+de*2j*sum(s[a]*cross_mat(E[a]) for a in range(3))
    return M/6.0
dirs={'(1,0,0)':np.array([1.,0,0]),'(1,1,0)':np.array([1.,1,0])/np.sqrt(2),
      '(1,1,1)':np.array([1.,1,1])/np.sqrt(3)}
print("T159  does the full rule give the relativistic invariant?")
al,be,de=0.5,0.0,1.0
m=al+be/3; c=de/3
print(f"   alpha={al}, beta={be}, delta={de}  ->  predicted m = alpha+beta/3 = {m:.6f},  c = delta/3 = {c:.6f}")
print()
print(f"   {'|k|':>8} " + "  ".join(f"{n+' : |lam|^2':>22}" for n in dirs) + f" {'m^2+c^2k^2':>14}")
for kmag in (0.02,0.05,0.1,0.2,0.4):
    row=[]
    for u in dirs.values():
        w=np.linalg.eigvals(symbol(kmag*u,al,be,de))
        row.append(max(abs(w))**2)
    print(f"   {kmag:8.3f} " + "  ".join(f"{v:22.10f}" for v in row) + f" {m*m+c*c*kmag*kmag:14.10f}")
print()
print("   residual (|lam|^2 - m^2 - c^2 k^2)/k^4, should approach a constant:")
print(f"   {'|k|':>8} " + "  ".join(f"{n:>16}" for n in dirs))
for kmag in (0.05,0.025,0.0125,0.00625):
    row=[]
    for u in dirs.values():
        w=np.linalg.eigvals(symbol(kmag*u,al,be,de))
        row.append((max(abs(w))**2-m*m-c*c*kmag**2)/kmag**4)
    print(f"   {kmag:8.5f} " + "  ".join(f"{v:16.6f}" for v in row))
print()
print("   (ii) anisotropy of |lambda| vs beta, at alpha=0.5, delta=1 fixed")
print(f"   {'beta':>8} " + "  ".join(f"{'|k|=%g'%k:>14}" for k in (0.05,0.1,0.2,0.4)))
for be2 in (0.0,0.05,0.1,0.2,0.5):
    row=[]
    for kmag in (0.05,0.1,0.2,0.4):
        vals=[max(abs(np.linalg.eigvals(symbol(kmag*u,al,be2,de)))) for u in dirs.values()]
        row.append((max(vals)-min(vals))/np.mean(vals))
    print(f"   {be2:8.2f} " + "  ".join(f"{v:14.3e}" for v in row))
print()
print("   anisotropy growing linearly with beta and vanishing at beta=0 means")
print("   emergent isotropy SELECTS beta = 0, narrowing the rule to three parameters.")
