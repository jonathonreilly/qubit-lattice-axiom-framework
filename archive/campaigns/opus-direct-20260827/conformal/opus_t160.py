"""T160 - CORRECTING R95's FRAMING, AND AN ISOTROPY CRITERION THAT SELECTS beta.

TWO CORRECTIONS TO MYSELF FIRST.

(a) The symbol is HERMITIAN, not anti-hermitian.  i[e_a]_x is imaginary
    antisymmetric, hence hermitian, so the spectrum is REAL:
        lambda(k) = A(k) +- (delta/3)|sin k|,   A(k) = (2 alpha sum cos + ...)/6
    not A +- i(delta/3)|sin k| as I assumed in T159.  Verified directly:
    ||M M^dag - M^dag M|| = 0 and the eigenvalues came out real (0.51645, 0.49979,
    0.48313).  So the rule is a CONTRACTION -- a channel -- and its spectrum is a
    real splitting, NOT a frequency.  R95's numbers are all correct but the words
    'dispersion', 'omega' and 'light cone' overstate them: what is linear in |k|
    and isotropic is a SPECTRAL SPLITTING of a hermitian symbol.  Calling it a
    light cone requires a time identification the axioms do not supply, which R95
    flagged but then leaned on anyway.

(b) T159's closing line -- 'isotropy selects beta = 0' -- is FALSE on its own
    data: anisotropy was 8.9e-6 at beta=0 and 4.4e-6 at beta=0.05, i.e. LOWER.
    The beta channel partially CANCELS the curl channel's lattice anisotropy.

That cancellation is worth chasing, because it is a genuine selection criterion:
the leading anisotropy of the splitting is an O(k^2) direction-dependent term, and
if a single beta kills it for ALL directions at once, that beta is DERIVED.

The leading anisotropic pieces, by hand:
   curl:  |sin k| = |k| (1 - (1/6) sum_a k_a^4/|k|^2 ... )  -- anisotropic at O(k^2)
   N   :  sum_a cos(k_a) e_a e_a^T = I - (1/2) diag(k_a^2) -- anisotropic at O(k^2)
so a cancellation at O(k^2) is possible in principle.  Test it."""
import numpy as np
E=[np.array([1.,0,0]),np.array([0,1.,0]),np.array([0,0,1.])]
def cm(u): return np.array([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
def symbol(k,al,be,de):
    c=np.cos(k); s=np.sin(k)
    M=al*2*c.sum()*np.eye(3,dtype=complex)+be*2*sum(c[a]*np.outer(E[a],E[a]) for a in range(3))
    M=M+de*2j*sum(s[a]*cm(E[a]) for a in range(3))
    return M/6.0
def split(k,al,be,de):
    w=np.sort(np.linalg.eigvalsh(0.5*(symbol(k,al,be,de)+symbol(k,al,be,de).conj().T)))
    return w[-1]-w[0]          # the spectral splitting, basis-independent
print("T160  is there a beta that makes the splitting isotropic?")
print()
dirs=[np.array([1.,0,0]),np.array([1.,1,0])/np.sqrt(2),np.array([1.,1,1])/np.sqrt(3)]
def aniso(be,kmag,al=0.5,de=1.0):
    v=[split(kmag*u,al,be,de) for u in dirs]
    return (max(v)-min(v))/np.mean(v)
print(f"   {'beta':>9} " + "  ".join(f"{'|k|=%g'%k:>13}" for k in (0.1,0.2,0.4)))
for be in (-0.2,-0.1,0.0,0.05,0.1,0.2,0.4):
    print(f"   {be:9.3f} " + "  ".join(f"{aniso(be,k):13.3e}" for k in (0.1,0.2,0.4)))
print()
print("   minimising anisotropy over beta at each |k| (golden-section):")
def minimise(kmag):
    lo,hi=-1.0,1.0
    for _ in range(200):
        m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
        if aniso(m1,kmag)<aniso(m2,kmag): hi=m2
        else: lo=m1
    return 0.5*(lo+hi)
for kmag in (0.4,0.2,0.1,0.05):
    b=minimise(kmag)
    print(f"      |k|={kmag:5.3f}  ->  beta* = {b:+.6f}   residual anisotropy {aniso(b,kmag):.3e}")
print()
print("   a beta* converging to a fixed value as |k| -> 0 is a DERIVED coefficient:")
print("   emergent isotropy would then select it out of the CP-allowed region.")
