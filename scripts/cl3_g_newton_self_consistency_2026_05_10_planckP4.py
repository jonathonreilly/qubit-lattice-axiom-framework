"""Supplied dimensional family, action-depth identities, finite Green diagnostic.
No ledger input, retained-status test, physical closure or non-derivability proof.
"""
import math
import numpy as np
import sympy as sp

_results=[]
def report(name, ok, detail=""):
    ok=bool(ok)
    _results.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")

def lattice_green_function_z3(r, L=64):
    """Compute the zero-mean finite periodic pseudoinverse at (r,0,0).

    This finite torus diagnostic does not establish a large-distance limit.

    Implementation: discretized 3D Fourier transform on L^3 grid. We
    compute the inverse of the discrete Laplacian eigenvalues
    sigma(k) = 2 (3 - cos k_1 - cos k_2 - cos k_3) and evaluate at
    distance r along an axis.
    """
    import numpy as np

    # FFT-based Green function on L^3 with k-zero point removed
    n = L
    k = np.fft.fftfreq(n) * 2 * np.pi  # k in [-pi, pi)
    k1, k2, k3 = np.meshgrid(k, k, k, indexing='ij')
    sigma = 2 * (3 - np.cos(k1) - np.cos(k2) - np.cos(k3))
    # Avoid division by zero at k = 0
    sigma_safe = np.where(sigma > 1e-12, sigma, 1.0)
    Ghat = np.where(sigma > 1e-12, 1.0 / sigma_safe, 0.0)
    # Inverse FFT to get G(x, 0)
    G = np.fft.ifftn(Ghat).real
    # Distance r along x-axis
    return float(G[r, 0, 0])


def main():
    _results.clear()
    p,q,r,s=sp.symbols('p q r s', real=True)
    equations=(p+q+2*s-3,r+s+1,-q-s+2)
    solution=sp.linsolve(equations,(p,q,r,s))
    expected=sp.FiniteSet((1-s,2-s,-1-s,s))
    report("complete real-exponent dimensional family", solution==expected, str(solution))
    candidates=[(a,b,c,d) for a in range(-3,4) for b in range(-3,4)
                for c in range(-3,4) for d in range(-3,4)
                if (a+b+2*d,c+d,-b-d)==(3,-1,-2)]
    report("finite box matches family, not uniqueness", set(candidates)==
           {(1-j,2-j,-1-j,j) for j in (-1,0,1,2)}, str(candidates))
    report("explicit nonunique dimensional forms", all(
        tuple(e.subs(dict(zip((p,q,r,s),v))) for e in equations)==(0,0,0)
        for v in ((1,2,-1,0),(0,1,-2,1),(2,3,0,-1))))
    anchor=1.054571817e-34*299792458/(2.176434e-8)**2
    report("rounded supplied Planck-anchor consistency only",
           abs(anchor-6.67430e-11)/6.67430e-11<1e-3, str(anchor))
    ratios=[4*math.pi*4*lattice_green_function_z3(4,L) for L in (16,24,32,48)]
    for L,x in zip((16,24,32,48),ratios):
        report(f"finite torus positive ratio L={L}",x>0,str(x))
    report("finite sequence increases",all(x<y for x,y in zip(ratios,ratios[1:])))
    report("largest finite ratio in historical bound",.6<ratios[-1]<1.05)
    f=sp.symbols('f',positive=True)
    depth=f/(1+sp.sqrt(1-f))
    report("stated square-root depth rationalization",
           sp.simplify(depth-(1-sp.sqrt(1-f)))==0)
    report("stated square-root leading order one and next coefficient",
           sp.limit(depth/f,f,0,dir='+')==sp.Rational(1,2) and
           sp.limit((depth-f/2)/f**2,f,0,dir='+')==sp.Rational(1,8))
    geometric=sp.sqrt(2*f+f**2)-f
    report("geometric spent-delay order one-half",
           sp.limit(geometric/sp.sqrt(f),f,0,dir='+')==sp.sqrt(2))
    report("model square-root and valley-linear exact depths",
           sp.simplify(1-(1-sp.sqrt(f))-sp.sqrt(f))==0 and
           sp.simplify(1-(1-f)-f)==0)
    # Equal site densities do not imply equal density matrices.
    psi=sp.Matrix([1,1])/sp.sqrt(2)
    pure=psi*psi.T; mixed=sp.eye(2)/2
    report("pure and mixed can share site density",pure.diagonal()==mixed.diagonal()
           and pure!=mixed)
    print(f"TOTAL: PASS={sum(_results)}, FAIL={len(_results)-sum(_results)}")
    print("Scope: exact supplied identities and finite diagnostics; composition obligations remain open.")
    return 0 if all(_results) else 1

if __name__=='__main__':
    raise SystemExit(main())
