"""T158 - DOES THE AXIOMS' OWN RULE PROPAGATE RELATIVISTICALLY?

R92/93/94 narrowed the admissibility rule, using only axiom content, to
     v_out(x) = (1/6)[ alpha V + beta N + delta C ](x)
     V = sum_i v(x+n_i),  N = sum_i (n_i.v(x+n_i)) n_i,  C = sum_i n_i x v(x+n_i)
with alpha in [-1/3,1] and the gradient channel bounded by max|gamma_0| = 1-alpha
(or sqrt((1+3a)(1-a)) below alpha=0).

The rule is a linear operator on the lattice spin field, so its SYMBOL is
computable by Fourier transform with no added premise -- in particular without
supplying a record-formation rule, which the axioms explicitly leave downstream.
Symbols of the three channels:

   V -> 2 sum_a cos(k_a) I
   N -> 2 sum_a cos(k_a) e_a e_a^T
   C -> 2i sum_a sin(k_a) [e_a]_x

The CURL channel is the only one carrying sin(k_a) -- a FIRST-ORDER derivative.
Since [k]_x has eigenvalues 0, +-i|k|, the curl term alone gives a dispersion
LINEAR in |k|: a light cone, from axiom content.

Three things to measure, each of which could fail:
  (1) is the small-k dispersion of the curl channel linear in |k| and ISOTROPIC?
  (2) the N channel expands as I - (1/2)diag(k_a^2), which is NOT isotropic at
      O(k^2) -- so how much anisotropy does beta inject, and is beta forced small?
  (3) at what k does lattice anisotropy become O(1)? (the usual Brillouin effect)"""
import numpy as np, itertools
E=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.])]
def cross_mat(u): return np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
def symbol(k,al,be,de):
    c=np.array([np.cos(k[a]) for a in range(3)]); s=np.array([np.sin(k[a]) for a in range(3)])
    M=al*2*c.sum()*np.eye(3,dtype=complex)
    M=M+be*2*sum(c[a]*np.outer(E[a],E[a]) for a in range(3))
    M=M+de*2j*sum(s[a]*cross_mat(E[a]) for a in range(3))
    return M/6.0
print("T158  dispersion of the axiom-derived admissibility rule")
print()
print("(1) CURL channel alone (alpha=beta=0, delta=1): eigenvalues vs |k| and direction")
print(f"   {'|k|':>8} " + "  ".join(f"{nm:>22}" for nm in ("k along (1,0,0)","k along (1,1,0)/r2","k along (1,1,1)/r3")))
dirs=[np.array([1.,0,0]),np.array([1.,1,0])/np.sqrt(2),np.array([1.,1,1])/np.sqrt(3)]
for kmag in (0.02,0.05,0.1,0.2,0.4,0.8):
    row=[]
    for u in dirs:
        w=np.linalg.eigvals(symbol(kmag*u,0,0,1))
        row.append(max(abs(w.imag)) if max(abs(w.imag))>max(abs(w.real)) else max(abs(w)))
    print(f"   {kmag:8.3f} " + "  ".join(f"{v:22.8f}" for v in row))
print()
print("   ratio to |k| (constant => LINEAR dispersion; equal across columns => ISOTROPIC)")
print(f"   {'|k|':>8} " + "  ".join(f"{nm:>22}" for nm in ("(1,0,0)","(1,1,0)","(1,1,1)")))
for kmag in (0.02,0.05,0.1,0.2,0.4,0.8):
    row=[]
    for u in dirs:
        w=np.linalg.eigvals(symbol(kmag*u,0,0,1)); row.append(max(abs(w))/kmag)
    print(f"   {kmag:8.3f} " + "  ".join(f"{v:22.8f}" for v in row))
print()
print("(2) anisotropy injected by the N channel (beta), measured as the spread of")
print("    the largest eigenvalue over directions at fixed |k|")
print(f"   {'beta':>8} {'|k|=0.05':>14} {'|k|=0.2':>14} {'|k|=0.5':>14}")
for be in (0.0,0.1,0.3,1.0):
    row=[]
    for kmag in (0.05,0.2,0.5):
        vals=[max(abs(np.linalg.eigvals(symbol(kmag*u,0.5,be,1)))) for u in dirs]
        row.append((max(vals)-min(vals))/max(np.mean(vals),1e-300))
    print(f"   {be:8.2f} " + "  ".join(f"{v:14.3e}" for v in row))
print()
print("(3) where does lattice anisotropy of the CURL channel reach 1%?")
for kmag in np.linspace(0.05,3.0,60):
    vals=[max(abs(np.linalg.eigvals(symbol(kmag*u,0,0,1)))) for u in dirs]
    sp=(max(vals)-min(vals))/max(np.mean(vals),1e-300)
    if sp>0.01:
        print(f"   |k| = {kmag:.3f}  (wavelength {2*np.pi/kmag:.1f} lattice units)"); break
