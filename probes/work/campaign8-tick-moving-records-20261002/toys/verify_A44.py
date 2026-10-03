"""Coordinator check of A44's Klein duality:
(1) V_x = (i s1)^x1 (i s2)^x2 (i s3)^x3;  V_x^dag (i s_a) V_{x+e_a} = scalar * 1 with KS-type signs (pi flux);
(2) on an a-bond, sigma.sigma -> 2 s^a s^a - sigma.sigma and the compass term s^a s^a is unchanged (D = 0 map H(J,K) -> H(-J, K+2J))."""
import numpy as np, itertools
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]).astype(complex)]
I2=np.eye(2)
def V(x):
    M=I2.copy()
    for a in range(3): M=M@np.linalg.matrix_power(1j*s[a],x[a]%4)
    return M
ok=True; signs={}
for x in itertools.product(range(4),repeat=3):
    for a in range(3):
        y=list(x); y[a]+=1
        M=V(x).conj().T@(1j*s[a])@V(y)
        c=M[0,0]
        if not np.allclose(M,c*I2): ok=False
        signs[(x,a)]=c
print("(1) V_x^dag (i s_a) V_{x+e_a} is a scalar on every bond:", ok)
# plaquette flux: product of the four bond scalars around each elementary square (xy, yz, zx) relative to the uniform (-1)^... convention
def bond(x,a): return signs[(tuple(v%4 for v in x),a)]
flux=set()
for x in itertools.product(range(2),repeat=3):
    for a,b in [(0,1),(1,2),(2,0)]:
        ea=[0,0,0]; ea[a]=1; eb=[0,0,0]; eb[b]=1
        xa=[x[i]+ea[i] for i in range(3)]; xb=[x[i]+eb[i] for i in range(3)]
        p=bond(x,a)*bond(xa,b)/bond(xb,a)/bond(x,b)
        flux.add(np.round(p,8))
print("    plaquette products of the dual hopping:", flux, "(-1 = pi flux on every face)")
# (2) bond map
def rot(x,v): return V(x).conj().T@v@V(x)
x=(0,0,0); 
for a in range(3):
    y=[0,0,0]; y[a]=1
    SS=sum(np.kron(s[b],s[b]) for b in range(3)); SSd=sum(np.kron(rot(x,s[b]),rot(tuple(y),s[b])) for b in range(3))
    Ka=np.kron(s[a],s[a]); Kad=np.kron(rot(x,s[a]),rot(tuple(y),s[a]))
    print(f"(2) bond {a}: sigma.sigma -> 2 s^a s^a - sigma.sigma:", np.allclose(SSd,2*Ka-SS), "| compass unchanged:", np.allclose(Kad,Ka))
