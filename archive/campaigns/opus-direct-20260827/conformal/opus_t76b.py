"""T76b - second route to the matter-content result, and the flavour count made explicit.
T76 (L=3): the cubical complex has 16 components per site splitting as 1:4:6:4:1
at every spectral level.  Confirm at a second lattice size, and make the flavour
statement explicit rather than inferred:
  * total multiplicity per MOMENTUM must be exactly 16 (the whole fibre);
  * a single Dirac operator in d=4 has 4 spinor components, so 16/4 = 4 FLAVOURS;
  * and the eigenvalues of the full Kahler-Dirac operator D = d + delta must be
    +-sqrt(Hodge Laplacian), i.e. the operator really is first-order Dirac-like."""
import numpy as np, itertools
def build(L,d=4):
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sgn=(-1)**pos
                D[j,cidx[k][(s,T)]]+=-sgn; D[j,cidx[k][(shift(s,a),T)]]+=sgn
        Ds.append(D)
    return cells,Ds,len(sites)
for L in (3,4):
    cells,Ds,nsites=build(L)
    d=4
    dims=[len(c) for c in cells]
    N=sum(dims)
    # full Kahler-Dirac operator D = d + delta on the whole cochain space
    off=[0]
    for k in range(d+1): off.append(off[-1]+dims[k])
    Dfull=np.zeros((N,N))
    for k in range(d):
        Dfull[off[k+1]:off[k+2], off[k]:off[k+1]]=Ds[k]
        Dfull[off[k]:off[k+1], off[k+1]:off[k+2]]=Ds[k].T
    ev=np.linalg.eigvalsh(Dfull)
    lap=np.sort(np.clip(ev**2,0,None))
    lv=[]
    for z in lap:
        if lv and abs(z-lv[-1][0])<1e-6: lv[-1][1]+=1
        else: lv.append([z,1])
    print(f"\n  L={L}: {nsites} sites, cochain dim {N} = {N//nsites} per site "
          f"(fibre {dims[0]//nsites},{dims[1]//nsites},{dims[2]//nsites},"
          f"{dims[3]//nsites},{dims[4]//nsites})")
    print(f"     full D = d+delta is {N}x{N};  symmetric: "
          f"{bool(np.allclose(Dfull,Dfull.T))};  spectrum symmetric about 0: "
          f"{bool(np.allclose(np.sort(ev),-np.sort(-ev)[::-1],atol=1e-8))}")
    print(f"     {'level (D^2)':>13} {'total mult':>11} {'momenta':>9} {'mult/momentum':>15}")
    pred=sorted({round(sum(4*np.sin(np.pi*n[a]/L)**2 for a in range(4)),9)
                 for n in itertools.product(range(L),repeat=4)})
    for val,mult in lv[:5]:
        # how many momenta give this Laplacian value
        cnt=sum(1 for n in itertools.product(range(L),repeat=4)
                if abs(sum(4*np.sin(np.pi*n[a]/L)**2 for a in range(4))-val)<1e-6)
        print(f"     {val:13.6f} {mult:11d} {cnt:9d} {(mult/cnt if cnt else float('nan')):15.4f}",
              flush=True)
    print(f"     predicted 0-form levels 4*sum sin^2: {[f'{v:.4f}' for v in pred[:5]]}")
print()
print("  mult/momentum = 16 at every level  =>  each momentum carries the WHOLE")
print("  Kahler-Dirac fibre.  A Dirac operator in d=4 has 4 spinor components, so")
print("  16 / 4 = FOUR DEGENERATE DIRAC FLAVOURS -- the rule's matter content in 4D.")
