"""Kill-round check on attack Test 1: can its pre-registered FAIL reading ever occur?
FAIL = ||[H_A,H]|| = 0 in a CONNECTED chain.  Draw random connected nearest-neighbour Hamiltonians on L=6
(random nonzero ZZ, XX, field terms) and record ||[H_A,H]||, ||[H_B,H]|| and the kinematic N5 conditions.
Also: the N5 note's own falsifier (sigma_x sigma_x coupling breaks commutation) is the same computation."""
import numpy as np
L=6
I2=np.eye(2);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.]).astype(complex)
def op(mats):
    out=mats[0]
    for m in mats[1:]: out=np.kron(out,m)
    return out
def site(a,j):
    m=[I2]*L;m[j]=a;return op(m)
def two(a,j,b,k):
    m=[I2]*L;m[j]=a;m[k]=b;return op(m)
rng=np.random.default_rng(5)
Id=np.eye(2**L)
HA=Id+site(X,0);HB=Id+site(X,L-1)
kin=np.linalg.norm(HA@HB-HB@HA)
mins=[]
for t in range(200):
    H=np.zeros((2**L,2**L),complex)
    for j in range(L-1):
        for P in (X,Y,Z):
            H+=rng.normal()*two(P,j,P,j+1)
    for j in range(L):
        H+=rng.normal()*site(X,j)+rng.normal()*site(Z,j)
    c=max(np.linalg.norm(HA@H-H@HA),np.linalg.norm(HB@H-H@HB))
    mins.append(c)
print("kinematic ||[H_A,H_B]|| =",kin)
print("random CONNECTED laws (n=200): min over laws of max(||[H_A,H]||,||[H_B,H]||) =",min(mins),"; any zero:",any(m<1e-9 for m in mins))
# decoupled world (two isolated end sites + rest): kinematic conditions identical, commutation holds
H=np.zeros((2**L,2**L),complex)
for j in range(1,L-2):
    H+=two(Z,j,Z,j+1)
for j in range(L): H+=site(X,j)
print("decoupled ends: ||[H_A,H]|| =",np.linalg.norm(HA@H-H@HA)," ||[H_B,H]|| =",np.linalg.norm(HB@H-H@HB))
