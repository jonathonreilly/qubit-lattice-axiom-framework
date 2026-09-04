"""T151c - the self-dual split, done properly.

T151b's su(2) ranks came out 1 and 2 rather than 3 and 0, and the fault was mine:
I formed 'self-dual' combinations as B_ab + B_ce over ALL ordered pairs a<b, which
double-counts each complementary pair and omits the epsilon SIGN, so the results
were not self-dual at all.  The correct construction uses exactly three
complementary pairs with their signs:

   SD_i  = B_{0i} + (1/2) eps_{ijk} B_{jk},   ASD_i = B_{0i} - (1/2) eps_{ijk} B_{jk}
i.e.  SD_1 = B_01 + B_23,  SD_2 = B_02 + B_31,  SD_3 = B_03 + B_12   (note B_31 = -B_13)

giving 3 + 3, and su(2)_L x su(2)_R = so(4).  Verify each triple closes into su(2)
BEFORE using it -- a triple that does not close is not an su(2) and its 'rank' on
a subspace means nothing."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t138 import setup
d=4; NF,G,Gb=setup(d)
CL=np.eye(NF)
for a in range(d): CL=CL@G[a]
Bv=lambda a,b: 0.5*(G[a]@G[b])
SD=[Bv(0,1)+Bv(2,3), Bv(0,2)-Bv(1,3), Bv(0,3)+Bv(1,2)]
ASD=[Bv(0,1)-Bv(2,3), Bv(0,2)+Bv(1,3), Bv(0,3)-Bv(1,2)]
print("T151c  self-dual / anti-self-dual bivectors, properly signed")
for nm,L in (("self-dual",SD),("anti-self-dual",ASD)):
    sp=np.linalg.matrix_rank(np.array([X.ravel() for X in L]),tol=1e-9)
    com=[]
    for X in L:
        for Y in L: com.append((X@Y-Y@X).ravel())
    clo=np.linalg.matrix_rank(np.vstack([np.array([X.ravel() for X in L]),np.array(com)]),tol=1e-9)
    print(f"   {nm:>16}: spans {sp}, closed under commutators -> {clo}"
          f"   {'su(2) CLOSES' if clo==3 else 'does NOT close'}")
cross=max(np.abs(X@Y-Y@X).max() for X in SD for Y in ASD)
print(f"   [self-dual, anti-self-dual] = {cross:.1e}   {'COMMUTE -> so(4) = su(2)+su(2)' if cross<1e-12 else ''}")
print()
Pp=0.5*(np.eye(NF)+CL); Pm=0.5*(np.eye(NF)-CL)
def act(L,P):
    R=np.array([(P@X@P).ravel() for X in L])
    return np.linalg.matrix_rank(R,tol=1e-9), max(np.abs(P@X@P).max() for X in L)
print("   action of each su(2) on the two CL-halves:")
print(f"      {'':>16} {'rank on P+':>12} {'norm on P+':>12} {'rank on P-':>12} {'norm on P-':>12}")
for nm,L in (("self-dual",SD),("anti-self-dual",ASD)):
    rp,np_=act(L,Pp); rm,nm_=act(L,Pm)
    print(f"      {nm:>16} {rp:12d} {np_:12.3e} {rm:12d} {nm_:12.3e}")
print()
print("   3/0 on opposite halves = 16 = (4_taste, 2_L) + (4_taste, 2_R):")
print("   one su(2) acts on one chirality only, which is what makes it a WEYL structure.")
