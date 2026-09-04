"""T105 - DOES CURVATURE SUPPLY THE GENERATION SECTOR'S MISSING SYMMETRY BREAKING?
docs/GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING_NARROW_THEOREM_NOTE_2026-05-23
proves exactly what the generation gate needs:

    preserved S_3      -> mass matrix has only 2 distinct eigenvalues (FORCED
                          degeneracy, carried by the 2-dim irrep E)
    any proper subgroup -> 3 distinct

so the minimal input is  S_3 -> (any proper subgroup)  -- and the note states it
"does not derive the breaking".  That is the open question.

This campaign found a framework-internal mechanism that lifts degeneracies:
CURVATURE (Results 34, 35), which splits them completely with no intermediate
structure.  Result 35 recorded that as a NEGATIVE, because it gives no three-fold
structure of its own.  But for THIS purpose complete splitting is exactly what is
wanted -- the generation sector already HAS three states and needs them made
distinct.

Test on the 4-torus, where S_3 acts by permuting three of the four directions:
  (a) FLAT               -> the three spatial modes are degenerate (3-fold)
  (b) CURVED, S_3-SYMMETRIC (same profile in each of the three directions)
                         -> does the degeneracy survive?  The note's theorem says
                            a preserved S_3 forces it.
  (c) CURVED, S_3-BREAKING (different amplitudes per direction)
                         -> 3 distinct?
  (d) FLAT but ANISOTROPIC (a constant metric, no curvature) -> controls for
      'is it the curvature, or merely the anisotropy?'"""
import numpy as np, itertools
d=4
def spec0(L,gfun):
    """0-form (vertex) Laplacian of the cubical complex with a diagonal metric"""
    sites=list(itertools.product(range(L),repeat=d)); sid={s:i for i,s in enumerate(sites)}
    N=len(sites); K=np.zeros((N,N)); M=np.zeros(N)
    for s in sites:
        g=gfun(s); vol=float(np.prod(np.sqrt(g)))
        M[sid[s]]+=vol
        for a in range(d):
            t=list(s); t[a]=(t[a]+1)%L; t=tuple(t)
            gt=gfun(t); w=0.5*(vol/g[a]+float(np.prod(np.sqrt(gt)))/gt[a])
            K[sid[s],sid[s]]+=w; K[sid[t],sid[t]]+=w
            K[sid[s],sid[t]]-=w; K[sid[t],sid[s]]-=w
    A=np.diag(1.0/np.sqrt(M))@K@np.diag(1.0/np.sqrt(M))
    return np.sort(np.clip(np.linalg.eigvalsh(A),0,None))
def levels(e,n=4,tol=1e-7):
    nz=e[e>1e-9]; out=[]
    for z in nz:
        if out and abs(z-out[-1][0])<tol*max(1.0,abs(z)): out[-1][1]+=1; out[-1][0]=z
        else: out.append([z,1])
    return out[:n]
L=4; A0=0.35
cases={
 "(a) FLAT":                      lambda s: np.ones(d),
 "(b) CURVED, S3-SYMMETRIC":      lambda s: np.array([1.0,
                                      1.0+A0*np.cos(2*np.pi*s[1]/L),
                                      1.0+A0*np.cos(2*np.pi*s[2]/L),
                                      1.0+A0*np.cos(2*np.pi*s[3]/L)]),
 "(c) CURVED, S3-BREAKING":       lambda s: np.array([1.0,
                                      1.0+0.45*np.cos(2*np.pi*s[1]/L),
                                      1.0+0.25*np.cos(2*np.pi*s[2]/L),
                                      1.0+0.10*np.cos(2*np.pi*s[3]/L)]),
 "(d) FLAT but ANISOTROPIC":      lambda s: np.array([1.0,1.21,1.44,1.69]),
}
print("T105  does curvature break S_3 in the generation sector?")
print("      (S_3 permutes the three spatial directions of the 4-torus)")
print(f"   {'case':>28} {'first levels (value x multiplicity)':>52}")
for nm,g in cases.items():
    e=spec0(L,g); lv=levels(e)
    print(f"   {nm:>28} {str([f'{v:.6f}x{c}' for v,c in lv]):>52}", flush=True)
print()
print("   Reading against the repo's theorem:")
print("     (a) flat: the three spatial modes are degenerate -- the S_3 3-fold.")
print("     (b) S_3-symmetric curvature must PRESERVE the degeneracy if S_3 really")
print("         is what forces it.")
print("     (c) S_3-breaking curvature must give THREE DISTINCT values -- which is")
print("         the 'any proper subgroup' row of the note's table.")
print("     (d) separates curvature from mere anisotropy: a constant metric is FLAT,")
print("         so if (d) also splits, the mechanism is anisotropy, not curvature.")
