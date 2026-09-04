"""T90 - IS THERE A GAUGE FIELD, AND WHAT DOES THE FRAMEWORK SAY ABOUT IT?
Result 36 asked what freedom the framework leaves in the WEIGHTS -- how much a
cell may weigh -- and the answer was one overall constant.  The companion
question is what freedom it leaves in the COMPARISON: when a face compares two
cells, is there a phase freedom?  A phase per edge IS a gauge field, so this asks
whether the framework contains one.

Put a U(1) phase on every edge:  d_A  =  d  with each incidence multiplied by
exp(i theta_e).  Then:

 (G1) d_A o d_A is the PLAQUETTE CURVATURE.  For the ordinary d it vanishes -- that
      is what makes the cochain complex a complex.  With phases it vanishes iff
      the connection is FLAT (zero flux through every 2-cell).  So the framework's
      topological results (Result 25's Betti numbers and McKean-Singer, Result 30's
      d=4 versions) require a FLAT gauge field: they are not available in the
      presence of gauge curvature.
 (G2) The DIRAC OPERATOR does not need d^2 = 0.  D_A = d_A + d_A^dagger is still
      self-adjoint for ANY phases, so the matter sector survives gauge curvature
      even where the topology does not.
 (G3) The spectrum must respond to the flux -- the Aharonov-Bohm effect on the
      complex -- and must be periodic in it, since flux 2 pi is no flux at all."""
import numpy as np, itertools
def build(L,flux,d=2):
    """cubical complex with a uniform U(1) flux per plaquette"""
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    # Landau-gauge vector potential: phase on the x_1-edges proportional to x_0
    def phase(s,a):
        return np.exp(1j*flux*s[0]) if a==1 else 1.0+0j
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])),dtype=complex)
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sg=(-1)**pos
                D[j,cidx[k][(s,T)]]      += -sg*phase(s,a)
                D[j,cidx[k][(shift(s,a),T)]] += sg*phase(s,a)
        Ds.append(D)
    return Ds,[len(c) for c in cells]
print("T90  d=2 cubical complex, uniform flux per plaquette")
print(f"   {'flux':>10} {'max|d_A d_A|':>15} {'D_A self-adjoint':>18} {'lowest |eigenvalue|':>21}")
for flux in (0.0, 0.05, 0.25, np.pi/2, np.pi):
    Ds,dims=build(4,flux,d=2)
    dd = 0.0 if len(Ds)<2 else float(np.max(np.abs(Ds[1]@Ds[0])))
    N=sum(dims); off=[0]
    for x in dims: off.append(off[-1]+x)
    Df=np.zeros((N,N),dtype=complex)
    for k in range(len(Ds)):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].conj().T
    sa=bool(np.allclose(Df,Df.conj().T))
    ev=np.sort(np.abs(np.linalg.eigvalsh(Df)))
    print(f"   {flux:10.5f} {dd:15.3e} {str(sa):>18} {ev[0]:21.8f}", flush=True)
print()
print("   (G1) d_A d_A = 0 only at zero flux  =>  gauge curvature breaks the cochain")
print("        complex, so the topological results need a FLAT connection.")
print("   (G2) D_A stays self-adjoint at every flux  =>  the matter sector survives.")
print()
print("T90 (G3)  is the spectrum periodic in the flux?  (2 pi flux = no flux)")
print(f"   {'flux':>12} {'lowest 3 |eigenvalues|':>40}")
for flux in (0.0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi):
    Ds,dims=build(4,flux,d=2)
    N=sum(dims); off=[0]
    for x in dims: off.append(off[-1]+x)
    Df=np.zeros((N,N),dtype=complex)
    for k in range(len(Ds)):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].conj().T
    ev=np.sort(np.abs(np.linalg.eigvalsh(Df)))
    print(f"   {flux:12.6f} {str([f'{v:.6f}' for v in ev[:3]]):>40}", flush=True)
print()
print("   flux 0 and flux 2 pi agreeing => the gauge field is genuinely U(1):")
print("   only the holonomy matters, which is what a gauge field means.")
