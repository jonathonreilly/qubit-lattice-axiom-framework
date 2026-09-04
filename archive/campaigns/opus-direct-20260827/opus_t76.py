"""T76 - THE FRAMEWORK'S MATTER CONTENT, on a CUBICAL complex.
T75 asked what matter the rule carries and answered a sharper question than the
one posed: the simplicial 4-torus has 1:15:50:60:24 = 150 cells per vertex, which
is NOT the Kahler-Dirac fibre.  The fibre C(d,k) = 1,4,6,4,1 is the CUBICAL cell
count -- a hypercube has exactly 1 vertex, 4 edges, 6 faces, 4 cubes and 1
hypercube per site, total 2^4 = 16.  So the CELL SHAPE fixes the matter content,
and the framework's own language (cells with volumes, faces with areas, and the
landed lane's hypercubic structure) points to cubical.

Build the cubical cochain complex on the 4-torus and check:
  (M1) cells per vertex = 1,4,6,4,1, total 16 = the Kahler-Dirac fibre;
  (M2) d o d = 0 and Betti = [1,4,6,4,1] -- it is still the 4-torus;
  (M3) the spectrum at each momentum splits across degrees as 1:4:6:4:1, which is
       what "the 16 components are 4 Dirac flavours x 4 spinor components" means;
  (M4) the 0-form Laplacian is the standard lattice one, 4 sum_a sin^2(k_a/2)."""
import numpy as np, itertools
L=3; d=4
sites=list(itertools.product(range(L),repeat=d)); sid={s:i for i,s in enumerate(sites)}
cells=[[] for _ in range(d+1)]; cidx=[{} for _ in range(d+1)]
for s in sites:
    for k in range(d+1):
        for S in itertools.combinations(range(d),k):
            cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
print("T76  CUBICAL complex on the 4-torus, L=%d" % L)
print(f"   cells by degree: {[len(c) for c in cells]}")
print(f"   per vertex     : {[len(c)//len(sites) for c in cells]}   total "
      f"{sum(len(c) for c in cells)//len(sites)}")
print(f"   (M1) matches the Kahler-Dirac fibre C(4,k) = [1,4,6,4,1], total 16: "
      f"{[len(c)//len(sites) for c in cells]==[1,4,6,4,1]}")
def shift(s,a):
    t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
def cob(k):
    D=np.zeros((len(cells[k+1]),len(cells[k])))
    for (s,S),j in cidx[k+1].items():
        for pos,a in enumerate(S):
            T=tuple(x for x in S if x!=a)
            sgn=(-1)**pos
            D[j,cidx[k][(s,T)]]        += -sgn
            D[j,cidx[k][(shift(s,a),T)]] += sgn
    return D
Ds=[cob(k) for k in range(d)]
mx=max(float(np.max(np.abs(Ds[k+1]@Ds[k]))) for k in range(d-1))
print(f"   (M2) max|d d| = {mx:.2e}")
ranks=[int(np.linalg.matrix_rank(D,tol=1e-8)) for D in Ds]
betti=[len(cells[k])-(ranks[k] if k<d else 0)-(ranks[k-1] if k>=1 else 0) for k in range(d+1)]
print(f"   (M2) Betti = {betti}   (T^4 requires [1,4,6,4,1])  "
      f"{'PASS' if betti==[1,4,6,4,1] else 'FAIL'}")
print()
print("   (M3)+(M4) spectra by degree")
print(f"   {'degree':>7} {'dim':>7} {'zero':>6} {'distinct nonzero levels (value x multiplicity)':>52}")
specs=[]
for k in range(d+1):
    Lk=np.zeros((len(cells[k]),len(cells[k])))
    if k<d: Lk=Lk+Ds[k].T@Ds[k]
    if k>=1: Lk=Lk+Ds[k-1]@Ds[k-1].T
    e=np.sort(np.clip(np.linalg.eigvalsh(Lk),0,None)); specs.append(e)
    nz=e[e>1e-8]; out=[]
    for z in nz:
        if out and abs(z-out[-1][0])<1e-6: out[-1][1]+=1
        else: out.append([z,1])
    print(f"   {k:7d} {len(cells[k]):7d} {int(np.sum(e<1e-8)):6d}   "
          f"{[f'{v:.5f}x{c}' for v,c in out[:4]]}", flush=True)
print()
print("   flat-lattice prediction for the 0-form Laplacian: 4*sum_a sin^2(pi n_a/L)")
pred=sorted({round(sum(4*np.sin(np.pi*n[a]/L)**2 for a in range(d)),9)
             for n in itertools.product(range(L),repeat=d)})
print(f"   predicted distinct values: {[f'{v:.5f}' for v in pred[:5]]}")
print()
print("   ratio of multiplicities across degrees at the FIRST nonzero level:")
firsts=[]
for k in range(d+1):
    nz=specs[k][specs[k]>1e-8]
    lvl=nz[0]; firsts.append((lvl,int(np.sum(np.abs(specs[k]-lvl)<1e-6))))
print(f"      {[f'{v:.5f} x{c}' for v,c in firsts]}")
base=firsts[0][1] if firsts[0][1] else 1
print(f"      multiplicity ratios: {[round(c/base,3) for _,c in firsts]}   want [1,4,6,4,1]")
