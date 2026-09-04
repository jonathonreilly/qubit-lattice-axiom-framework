"""T184 - WHAT IS THE dim-32 CONTINUUM TASTE ALGEBRA, AND DOES THE SM FIT?

T183 measured the Z^3+qubit CONTINUUM taste algebra at dimension 32, with the
method validated by reproducing u(4) = 16 for the staggered Z^4 control.  32 is not
a perfect square, so my 'u(6)' label in T183 was wrong -- it is not u(n) for any n.

A semisimple complex algebra is a direct sum of matrix blocks, dim = sum n_i^2, and
the number of blocks equals the dimension of its CENTRE.  So:
      32 = 16+16          two 4x4 blocks     centre 2
      32 = 16+4+4+4+4     one 4x4, four 2x2  centre 5
      32 = 4x8            eight 2x2 blocks   centre 8
Measure the centre and settle it.

WHY IT MATTERS.  R90/R116 concluded the Standard Model does not fit because the
available algebra was too small (u(4), centralizer of su(3) = 2 < 3; then u(2)).
If the continuum algebra is u(4) (+) u(4), embedding su(3) in ONE factor leaves a
centralizer of u(1) (+) u(4) = 17 dimensions, which HOLDS su(2) comfortably --
and the Standard Model gauge group WOULD fit.  That would reverse the campaign's
central matter-side negative, so it needs the algebra identified, not guessed."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def shift3(a,sg,p):
    M=np.zeros((8,8),dtype=complex)
    for r in R8:
        s=list(r)
        if sg>0:
            if r[a]==0: s[a]=1; ph=1.0
            else: s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else: s[a]=1; ph=np.exp(-1j*p[a])
        M[I8[tuple(s)],I8[r]]+=ph
    return M
D3=lambda p: sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),S[a]) for a in range(3))/2.0
def grads(Dfun,d,h=1e-5):
    G=[]
    for mu in range(d):
        e=np.zeros(d); e[mu]=h; G.append((Dfun(e)-Dfun(-e))/(2*h))
    return G
def comm_basis(mats,N):
    A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    k=int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
    return [Vt[len(s)-0-i-1].conj().reshape(N,N) for i in range(k)] if k else []
G=grads(D3,3)
B=comm_basis(G,16)
print("T184  identifying the dim-32 continuum taste algebra")
print(f"   commutant basis size: {len(B)}")
err=max(np.abs(X@G[a]-G[a]@X).max() for X in B for a in range(3))
print(f"   CONTROL every basis element commutes with every Gamma_mu: max {err:.1e}")
# centre of the algebra
cen=[]
M=[]
for X in B:
    if all(np.abs(X@Y-Y@X).max()<1e-8 for Y in B):
        v=np.concatenate([X.real.ravel(),X.imag.ravel()])
        M.append(v)
        if np.linalg.matrix_rank(np.array(M),tol=1e-8)>len(cen): cen.append(X)
        else: M.pop()
print(f"   dimension of the CENTRE: {len(cen)}")
print()
for blocks,desc in (((4,4),"u(4) (+) u(4)"),((4,2,2,2,2),"u(4) (+) 4 x u(2)"),
                    ((2,)*8,"8 x u(2)")):
    tot=sum(b*b for b in blocks)
    print(f"   {desc:>22}: dim {tot:3d}, centre {len(blocks)}"
          f"   {'<-- MATCHES' if tot==len(B) and len(blocks)==len(cen) else ''}")
print()
print("   does the Standard Model fit?  embed su(3) in the largest block:")
for blocks,desc in (((4,4),"u(4)+u(4)"),((4,2,2,2,2),"u(4)+4u(2)"),((2,)*8,"8u(2)")):
    if len(blocks)!=len(cen) or sum(b*b for b in blocks)!=len(B): continue
    big=max(blocks)
    if big<3:
        print(f"   {desc}: largest block is u({big}) -- cannot even hold su(3)")
    else:
        cent=1+sum(b*b for b in blocks if b!=big or blocks.count(big)>1)-(big*big if False else 0)
        rest=sum(b*b for b in blocks)-big*big
        print(f"   {desc}: su(3) in the u({big}) block leaves centralizer"
              f" u(1) + [other blocks] = {1+rest} dims  -> su(2) needs 3:"
              f" {'FITS' if 1+rest>=3 else 'does not fit'}")
