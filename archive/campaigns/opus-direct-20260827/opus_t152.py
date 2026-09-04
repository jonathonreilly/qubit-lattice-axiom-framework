"""T152 - DOES THE STANDARD MODEL GAUGE GROUP FIT INSIDE THE FRAMEWORK?

T151c settled the fibre exactly:  16 = (4_taste, 2_L) + (4_taste, 2_R), with
u(4) taste (16 hermitian generators, Cartan rank 4, eigenvalue multiplicities
(4,4,4,4)) acting inside each chirality half, and so(4) = su(2)_L + su(2)_R from
the Clifford bivectors acting on one half each (rank 3/0 and 0/3).

IMPORTANT READING NOTE, because this is exactly where numerology starts.  Those
su(2)'s are the LORENTZ groups -- Spin(4) = SU(2)_L x SU(2)_R -- not internal
symmetries.  So the fibre is '4 Dirac fermions carrying a u(4) index', which is
R76 restated, NOT a Pati-Salam (4,2,1).  The framework's ONLY internal symmetry
is u(4): T138 measured the commutant of the Gamma's at 16, and the commutant of
{Gamma} u {Gbar} at 1, so there is nothing else.

THE TOE QUESTION IS THEN SHARP AND PURELY ALGEBRAIC:
        does su(3) + su(2) + u(1)  embed in  u(4)?
Dimensions permit it (12 <= 16) and ranks match (4 = 4), so it must be settled by
computation, not by counting.  The obstruction, if there is one, is that the
CENTRALIZER of an su(3) inside u(4) is too small to hold an su(2).

Measure it: embed su(3) in u(4) the only way it goes (acting on 3 of the 4), and
compute the dimension of its centralizer."""
import numpy as np, itertools
# u(4) as 4x4 hermitian matrices; su(3) embedded on the first three components
def gell_mann():
    l=[]
    l.append(np.array([[0,1,0],[1,0,0],[0,0,0]],dtype=complex))
    l.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]],dtype=complex))
    l.append(np.array([[1,0,0],[0,-1,0],[0,0,0]],dtype=complex))
    l.append(np.array([[0,0,1],[0,0,0],[1,0,0]],dtype=complex))
    l.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]],dtype=complex))
    l.append(np.array([[0,0,0],[0,0,1],[0,1,0]],dtype=complex))
    l.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]],dtype=complex))
    l.append(np.diag([1,1,-2]).astype(complex)/np.sqrt(3))
    return l
SU3=[]
for g in gell_mann():
    M=np.zeros((4,4),dtype=complex); M[:3,:3]=g; SU3.append(M)
# a basis of u(4) hermitian generators
basis=[]
for i in range(4):
    E=np.zeros((4,4),dtype=complex); E[i,i]=1; basis.append(E)
for i in range(4):
    for j in range(i+1,4):
        A=np.zeros((4,4),dtype=complex); A[i,j]=1; A[j,i]=1; basis.append(A)
        B=np.zeros((4,4),dtype=complex); B[i,j]=-1j; B[j,i]=1j; basis.append(B)
print(f"T152  does su(3)+su(2)+u(1) fit inside u(4)?")
print(f"   u(4) hermitian basis: {len(basis)} generators   (dim u(4) = 16)")
rows=[]
for X in SU3:
    R=[]
    for Y in basis: R.append((X@Y-Y@X).ravel())
    rows.append(np.array(R))
A=np.hstack([r.reshape(len(basis),-1) for r in rows])
cent=len(basis)-np.linalg.matrix_rank(A,tol=1e-9)
print(f"   centralizer of the embedded su(3) inside u(4): dimension {cent}")
print(f"      (su(2) needs 3;  u(1) needs 1)")
print()
print(f"   dim su(3)+su(2)+u(1) = 8+3+1 = 12  <=  16 = dim u(4)   [dimension permits]")
print(f"   rank su(3)+su(2)+u(1) = 2+1+1 = 4  =   4 = rank u(4)   [rank permits]")
print(f"   BUT the centralizer of su(3) is {cent}-dimensional, so an su(2) commuting")
print(f"   with the su(3) {'DOES' if cent>=3 else 'DOES NOT'} fit.")
print()
print("   Verdict: the framework's entire internal symmetry is u(4).  If su(2) does")
print("   not fit in the centralizer of su(3), the Standard Model gauge group cannot")
print("   act on this fibre, and the SM needs a LARGER fibre than d=4 provides.")
