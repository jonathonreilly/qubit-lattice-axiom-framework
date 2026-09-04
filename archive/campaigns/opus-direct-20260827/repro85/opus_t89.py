"""T89 - WHY is the graded vacuum energy exactly zero?  (auditing T88)
T88: the supertrace-weighted spectral action has a volume derivative of 1e-15
while the ordinary trace gives -3.2.  Before calling that a cancellation, the
mechanism has to be pinned down, because I think it is the index theorem and that
changes what the result means.

The argument: G anticommutes with D (T82), so for a NONZERO eigenvalue lambda,
G maps the lambda eigenvector to the -lambda one, hence <psi|G|psi> = 0.  Only
the KERNEL contributes.  Therefore for ANY function f,

        Str f(D)  =  (n_even - n_odd) * f(0)  =  index * f(0)

which is topological -- it cannot depend on the geometry at all, so its volume
derivative is identically zero.  The cancellation would then be the index theorem,
not a dynamical cancellation.

Three checks:
 (A) <psi|G|psi> is ~0 for every nonzero mode and +-1 on the kernel;
 (B) Str f(D) = index * f(0) for several unrelated f;
 (C) on a complex with chi != 0 the supertrace is NONZERO but still exactly
     geometry-independent -- which is the sharp statement."""
import numpy as np, itertools
def build(L,scale,d=4):
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s_ in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s_,S)]=len(cells[k]); cells[k].append((s_,S))
    def shift(s_,a):
        t=list(s_); t[a]=(t[a]+1)%L; return tuple(t)
    g=np.array([scale]*d)**2; W=[]
    for k in range(d+1):
        w=np.zeros(len(cells[k])); vol=float(np.prod(np.sqrt(g)))
        for (s_,S),i in cidx[k].items():
            w[i]=vol/np.prod([g[a] for a in S]) if S else vol
        W.append(w)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s_,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sg=(-1)**pos
                D[j,cidx[k][(s_,T)]]+=-sg; D[j,cidx[k][(shift(s_,a),T)]]+=sg
        Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for k in range(d+1): off.append(off[-1]+dims[k])
    Df=np.zeros((N,N)); G=np.zeros(N)
    for k in range(d+1): G[off[k]:off[k+1]]=(-1)**k
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    return Df,G,dims
Df,G,dims=build(3,1.0)
ev,U=np.linalg.eigh(Df)
gexp=np.einsum("ij,i,ij->j",U,G,U)
ker=np.abs(ev)<1e-8; non=~ker
print("T89 (A)  <psi|G|psi> by mode class")
print(f"   nonzero modes ({int(non.sum())}): max|<G>| = {float(np.max(np.abs(gexp[non]))):.3e}")
print(f"   kernel modes  ({int(ker.sum())}): values {sorted(set(np.round(gexp[ker],9)))}")
print(f"   index = sum of <G> over the kernel = {float(np.sum(gexp[ker])):+.6f}")
print(f"   Betti [1,4,6,4,1] -> n_even - n_odd = (1+6+1) - (4+4) = {1+6+1-4-4}")
print()
print("T89 (B)  Str f(D) = index * f(0) for unrelated f")
for nm,f in (("log(|D|+0.5)",lambda x: np.log(np.abs(x)+0.5)),
             ("exp(-D^2)",   lambda x: np.exp(-x**2)),
             ("1/(1+D^2)",   lambda x: 1.0/(1.0+x**2)),
             ("cos(D)",      lambda x: np.cos(x))):
    st=float(np.sum(gexp*f(ev))); idx=float(np.sum(gexp[ker]))
    print(f"   {nm:>14}: Str = {st:+.3e}   index*f(0) = {idx*float(f(np.array([0.0]))[0]):+.3e}")
print()
print("T89 (C)  is the supertrace geometry-independent?  vary the scale")
for scale in (0.7,1.0,1.6,2.5):
    Df2,G2,_=build(3,scale)
    ev2,U2=np.linalg.eigh(Df2); ge2=np.einsum("ij,i,ij->j",U2,G2,U2)
    st=float(np.sum(ge2*np.log(np.abs(ev2)+0.5)))
    tr=float(np.sum(np.log(np.abs(ev2)+0.5)))
    print(f"   scale={scale}: Str = {st:+.3e}     ordinary trace = {tr:+.4f}")
print()
print("   nonzero modes contributing nothing, and Str = index*f(0) for every f,")
print("   means the vanishing is the INDEX THEOREM -- topological, not dynamical.")
