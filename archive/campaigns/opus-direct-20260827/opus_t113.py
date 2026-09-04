"""T113 - DOES THE FRAMEWORK'S OWN ACTION PREFER ANISOTROPY?  (the generation lane)
Result 49 established what the generation sector needs: the repo's note
GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING proves S_3 must break to any
proper subgroup, and says it "does not derive the breaking".  Result 49 found
that DIRECTIONAL INEQUIVALENCE supplies it -- and that flat anisotropy suffices,
curvature is not needed.

The question that turns that into a derivation: does the framework's OWN ACTION
prefer an anisotropic geometry, or an isotropic one?  If isotropic, the breaking
has to come from initial conditions or from matter, and the generation sector
gets nothing for free.  If anisotropic, S_3 breaks by itself.

Test on a flat 4-torus with independent side lengths (a_0,a_1,a_2,a_3) at FIXED
4-volume.  Two actions are relevant:
  (i)  the Regge action  -- but a flat torus has ZERO deficit at every hinge for
       any side lengths, so S_Regge = 0 identically: gravity alone is indifferent.
       (Worth confirming rather than assuming.)
  (ii) the OPERATOR's action -- the matter sector's vacuum energy, which is the
       one quantity in this campaign that is well-defined and convergent
       (Result 38: dW/dVol converges to 0.7% between lattice sizes).
So the real question is whether the MATTER vacuum energy prefers isotropy."""
import numpy as np, itertools
def spec_torus(L,sides,d=4,full=True):
    """cubical cochain operator on a flat torus with side lengths 'sides'."""
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    g=np.array(sides)**2
    vol=float(np.prod(np.sqrt(g)))
    W=[]
    for k in range(d+1):
        w=np.zeros(len(cells[k]))
        for (s,S),i in cidx[k].items():
            w[i]=vol/np.prod([g[a] for a in S]) if S else vol
        W.append(w)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sg=(-1)**pos
                D[j,cidx[k][(s,T)]]+=-sg; D[j,cidx[k][(shift(s,a),T)]]+=sg
        Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for x in dims: off.append(off[-1]+x)
    Df=np.zeros((N,N))
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    ev=np.abs(np.linalg.eigvalsh(Df))
    return ev, vol*L**d
def W_action(L,sides,m):
    ev,vol=spec_torus(L,sides)
    return float(np.sum(np.log(ev+m))), vol
print("T113  does the matter vacuum energy prefer ISOTROPY or ANISOTROPY?")
print("      flat 4-torus, side lengths varied at FIXED 4-volume")
L=3; m=0.6
def sides_at_fixed_vol(t):
    """one-parameter anisotropy: stretch dir 0 by e^{3t}, shrink 1,2,3 by e^{-t}"""
    s=np.array([np.exp(3*t),np.exp(-t),np.exp(-t),np.exp(-t)])
    return s/np.prod(s)**0.25
print(f"   {'t (anisotropy)':>16} {'sides':>34} {'volume':>10} {'W':>14} {'W - W(0)':>13}")
W0=None
for t in (-0.20,-0.10,-0.05,0.0,0.05,0.10,0.20):
    s=sides_at_fixed_vol(t)
    Wv,vol=W_action(L,s,m)
    if W0 is None and t==0.0: W0=Wv
    print(f"   {t:16.3f} {str([f'{x:.4f}' for x in s]):>34} {vol:10.5f} {Wv:14.6f} "
          f"{(Wv-W0 if W0 is not None else float('nan')):13.6f}", flush=True)
print()
print("   W minimised at t=0 => the matter vacuum energy PREFERS ISOTROPY, and the")
print("   generation sector's S_3 breaking must come from elsewhere (initial data,")
print("   or matter inhomogeneity).")
print("   W maximised at t=0, or monotone => it prefers ANISOTROPY, and the S_3")
print("   breaking the generation gate needs is supplied by the framework's own")
print("   dynamics.")
print()
print("   control: the Regge action on a FLAT torus must be identically zero for")
print("   ANY side lengths (no deficits), i.e. gravity alone is indifferent here.")
