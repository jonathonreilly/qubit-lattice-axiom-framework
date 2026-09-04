"""T82 - is the surviving 2-fold the CHIRALITY grading?
T81: with a symmetry-free curved metric every level of D^2 has multiplicity 2.
The natural reading is the D <-> -D pairing, but that should be checked rather
than assumed, because the Kahler-Dirac operator carries a natural grading -- EVEN
versus ODD form degree -- which is its chirality, and which is what makes the
index theorem work (Result 25's McKean-Singer).

Check: build the grading operator G = (-1)^(form degree), confirm it ANTICOMMUTES
with D (that is what makes it a chirality), and confirm that the +-pairs of D
eigenvalues are exchanged by it.  If so the residual 2-fold is chirality and
carries no flavour information, which is what Result 35 assumed."""
import numpy as np, itertools
L=3; d=4
sites=list(itertools.product(range(L),repeat=d))
cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
for s in sites:
    for k in range(d+1):
        for S in itertools.combinations(range(d),k):
            cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
def shift(s,a):
    t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
rng=np.random.default_rng(3)
RAND={s:1.0+0.35*rng.random(4) for s in sites}
W=[]
for k in range(d+1):
    w=np.zeros(len(cells[k]))
    for (s,S),i in cidx[k].items():
        g=RAND[s]; vol=float(np.prod(np.sqrt(g)))
        w[i]=vol/np.prod([g[a] for a in S]) if S else vol
    W.append(w)
Ds=[]
for k in range(d):
    D=np.zeros((len(cells[k+1]),len(cells[k])))
    for (s,S),j in cidx[k+1].items():
        for pos,a in enumerate(S):
            T=tuple(x for x in S if x!=a); sgn=(-1)**pos
            D[j,cidx[k][(s,T)]]+=-sgn; D[j,cidx[k][(shift(s,a),T)]]+=sgn
    Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
dims=[len(c) for c in cells]; N=sum(dims); off=[0]
for k in range(d+1): off.append(off[-1]+dims[k])
Df=np.zeros((N,N)); G=np.zeros(N)
for k in range(d+1): G[off[k]:off[k+1]]=(-1)**k
for k in range(d):
    Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
    Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
Gm=np.diag(G)
print(f"T82  symmetry-free curved metric, cochain dim {N}")
print(f"   G = (-1)^degree ;  G^2 = I : {bool(np.allclose(Gm@Gm,np.eye(N)))}")
print(f"   {{G, D}} = 0  (chirality anticommutes with the operator): "
      f"{bool(np.allclose(Gm@Df+Df@Gm,0,atol=1e-10))}")
ev=np.linalg.eigvalsh(Df)
pos=np.sort(ev[ev>1e-8]); neg=np.sort(-ev[ev<-1e-8])
print(f"   spectrum of D: {int(np.sum(np.abs(ev)<1e-8))} zero modes, "
      f"{len(pos)} positive, {len(neg)} negative")
print(f"   positive and negative parts identical: "
      f"{bool(np.allclose(pos,neg,atol=1e-9))}   max|diff| = {float(np.max(np.abs(pos-neg))):.2e}")
d2=np.sort(pos**2)
lv=[]
for z in d2:
    if lv and abs(z-lv[-1][0])<1e-7*max(z,1.0): lv[-1][1]+=1; lv[-1][0]=z
    else: lv.append([z,1])
print(f"   multiplicities of D^2 restricted to POSITIVE D eigenvalues only: "
      f"{[m for _,m in lv[:12]]}")
print()
print("   all 1 there => the 2-fold in Result 35 is exactly the +- pairing, i.e.")
print("   chirality, and carries no flavour information.  Result 35's reading holds.")
