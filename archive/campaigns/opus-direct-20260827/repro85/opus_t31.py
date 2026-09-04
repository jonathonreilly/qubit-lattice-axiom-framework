"""T31 - THE GRAVITON KINETIC TERM IN 3+1 DIMENSIONS, done exactly.
T30 measured d^2W/dh^2(k) in 2D by brute force, but (i) its k=0 and k=pi points
carry <cos^2>=1 while the interior carries 1/2, so they must not be fitted with
the rest, and (ii) in 2D the Einstein-Hilbert term is topological, so a 2D k^2
coefficient is NOT the graviton kinetic term.  The test has to be run in d=4.

Method that makes d=4 cheap and exact: let the plane wave run along ONE axis.
The operator is then still translation invariant in the other d-1 directions, so
a partial Fourier transform block-diagonalises it: for each transverse momentum
p, what remains is a 1D chain of size L * 2^d.  W = sum_p log|det Q_p| is exact.
Validated first against T30's brute-force 2D numbers."""
import numpy as np, itertools
def carrier(D):
    B=[]
    for k in range(D+1): B+=[tuple(c) for c in itertools.combinations(range(D),k)]
    return B,{b:i for i,b in enumerate(B)}
def ops(D):
    B,IDX=carrier(D); NF=len(B)
    def epsm(a):
        M=np.zeros((NF,NF))
        for Sx in B:
            if a in Sx: continue
            T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
        return M
    def iota(a,gi):
        M=np.zeros((NF,NF))
        for Sx in B:
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
        return M
    return [epsm(a) for a in range(D)], iota, NF
def W(D, L, m0, E, n, h, WAVE=1):
    """log|det Q| with g = I + h cos(2 pi n x_WAVE / L) E, exact, via partial FT."""
    EPS, iota, NF = ops(D)
    prof=[float(np.cos(2*np.pi*n*x/L)) for x in range(L)]
    gi=[np.linalg.inv(np.eye(D)+h*prof[x]*E) for x in range(L)]
    GAM=[[EPS[a]+iota(a,gi[x]) for a in range(D)] for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]
    tot=0.0
    for pidx in itertools.product(range(L), repeat=D-1):
        p={a: 2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF, L*NF), dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+= m0*np.eye(NF)
            for a in trans:
                Q[i:i+NF,i:i+NF]+= 1j*np.sin(p[a])*GAM[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                Q[i:i+NF,j:j+NF]+= 0.25*sgn*(2*EPS[WAVE]+iota(WAVE,gi[x])+iota(WAVE,gi[y]))
        tot += float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def D2(D,L,m0,E,n,e=2e-3):
    return (W(D,L,m0,E,n,e)-2*W(D,L,m0,E,n,0.0)+W(D,L,m0,E,n,-e))/e**2
print("=== VALIDATION: d=2, L=12, m0=0.9, E=diag(1,-1)  vs T30's brute-force numbers")
E2=np.array([[1.,0.],[0.,-1.]])
T30={0:270.72987073,1:136.55828386,2:139.10320145,3:140.74799024,4:139.52720629,
     5:135.95599094,6:267.71334058}
for n in range(0,7):
    v=D2(2,12,0.9,E2,n)
    print(f"   n={n}  partial-FT={v:+.6f}   brute-force={T30[n]:+.6f}   diff={abs(v-T30[n]):.2e}", flush=True)
print()
print("=== d=4, m0=0.9, wave along x1, E=diag(0,1,0,-1) [TRANSVERSE to the wave]")
print("    (a transverse-traceless-type mode: E has no component along the wave axis)")
E4=np.zeros((4,4)); E4[2,2]=1.0; E4[3,3]=-1.0
for L in (8,10,12):
    rows=[]
    for n in range(1, L//2):            # interior only: <cos^2> = 1/2 throughout
        k=2*np.pi*n/L; d=D2(4,L,0.9,E4,n); rows.append((k,d))
        print(f"   L={L:2d} n={n} k={k:.6f} k^2={k*k:.6f}  d2W/dh2={d:+.8f}", flush=True)
    ks=np.array([r[0] for r in rows]); ds=np.array([r[1] for r in rows])
    if len(rows)>=3:
        c=np.polyfit(ks[:3]**2, ds[:3], 1)
        NV=L**4
        print(f"   L={L}: fit A={c[1]:+.6f}  B={c[0]:+.6f}   per site: A/V={c[1]/NV:+.8f}"
              f"  B/V={c[0]/NV:+.8f}   B!=0: {abs(c[0])>1e-6}", flush=True)
    print()
print("=== d=4 mass dependence of the induced coupling B/V  (L=10)")
for m0 in (0.4,0.7,1.0,1.6,2.4):
    rows=[(2*np.pi*n/10, D2(4,10,m0,E4,n)) for n in (1,2,3)]
    ks=np.array([r[0] for r in rows]); ds=np.array([r[1] for r in rows])
    c=np.polyfit(ks**2, ds, 1)
    print(f"   m0={m0}:  B/V={c[0]/10**4:+.8f}   A/V={c[1]/10**4:+.8f}", flush=True)
