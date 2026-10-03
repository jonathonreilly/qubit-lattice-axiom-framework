"""Coordinator check of lane A42.
(1) The sign-twist mover C': X0 -> -X0 prod_N Z, Z0 -> Y0 prod_N Z is a valid automorphism (F2 symplectic check),
    is covariant under the sign-twist action (odd rotations act as the half-turn about x) and NOT under full soldering,
    and spreads (support growth under iteration).
(2) Axis soldering: the onsite half-turn about w=(1,1,1)/sqrt3 commutes with the whole image group (D3).
(3) The 12-element tetrahedral group (Pauli flips + cyclic relabelling) acts irreducibly on Bloch vectors.
"""
import numpy as np, itertools
N6=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def add(a,b): return tuple(i+j for i,j in zip(a,b))
# Pauli strings as dict site->(x,z) bits over F2
IMG={ 'X': {(0,0,0):(1,0), **{n:(0,1) for n in N6}},   # X0 -> X0 prod Z_N   (sign dropped)
      'Z': {(0,0,0):(1,1), **{n:(0,1) for n in N6}} }  # Z0 -> Y0 prod Z_N
def apply(P):
    out={}
    for site,(x,z) in P.items():
        for letter,bit in (('X',x),('Z',z)):
            if bit:
                for d,(xx,zz) in IMG[letter].items():
                    s=add(site,d); a,b=out.get(s,(0,0)); out[s]=((a+xx)%2,(b+zz)%2)
    return {s:v for s,v in out.items() if v!=(0,0)}
def symp(P,Q):  # 0 if commute, 1 if anticommute
    t=0
    for s,(x,z) in P.items():
        if s in Q: xx,zz=Q[s]; t+= x*zz+z*xx
    return t%2
# (1a) validity: images of single-site Paulis at sites within distance 2 keep their commutation relations
sites=[(0,0,0)]+N6+[add(a,b) for a in N6 for b in N6]
sites=list(set(sites)); ok=True
for s1 in sites:
    for s2 in sites:
        for L1 in ((1,0),(0,1),(1,1)):
            for L2 in ((1,0),(0,1),(1,1)):
                P={(0,0,0):L1}; Q={tuple(np.subtract(s2,s1)):L2}
                if symp(apply(P),apply(Q))!=symp(P,Q): ok=False
print("(1a) valid automorphism (commutation relations kept):", ok)
# (1b) covariance at the level of images of X0, Z0 (signs included): sign twist r=diag(1,s,s); full: r=g
def sgnperm(M): return round(np.linalg.det(np.abs(M)))
R=[]
for p in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3));
        for i in range(3): M[i,p[i]]=sg[i]
        if np.linalg.det(M)>0.5: R.append(M)
# Bloch-level images: C(X0) = -X0 * Zstar, C(Z0) = Y0 * Zstar, C(Y0) = Z0 (derived: Y = iXZ). Zstar = prod_N Z (rotation-invariant set).
# Represent an operator at site 0 as Bloch vector v (sum v_a sigma_a) times (Zstar)^e. C acts linearly on site-0 Bloch vectors:
#   sigma_x -> -sigma_x Zstar ; sigma_y -> sigma_z ; sigma_z -> sigma_y Zstar
def C_onsite(v):  # returns (vector part with Zstar, vector part without Zstar)
    with_z=np.array([-v[0],0,v[2]]); without=np.array([0,0,v[1]]); return with_z, without
def T(r, v_with, v_without):  # rotation with onsite Bloch action r; Zstar -> (r_zz)^6 Zstar = Zstar when r maps z to +-z
    return r@v_with, r@v_without
def covariant(action):
    for g in R:
        r=action(g)
        if not np.allclose(np.abs(r[2]),[0,0,1]) and not np.allclose(np.abs(r[:,2]),[0,0,1]):
            return False  # Zstar would not map to itself
        for v in np.eye(3):
            a=C_onsite(r@v); b=T(r,*C_onsite(v))
            if not (np.allclose(a[0],b[0]) and np.allclose(a[1],b[1])): return False
    return True
twist=lambda g: np.diag([1,sgnperm(g),sgnperm(g)]).astype(float)
full=lambda g: g
print("(1b) covariant under sign twist:", covariant(twist), "| under full soldering:", covariant(full))
# (1c) spreading
P={(0,0,0):(1,0)}; sizes=[]
for t in range(6): P=apply(P); sizes.append(len(P))
print("(1c) support sizes of C'^t(X0), t=1..6:", sizes)
# (2) axis soldering image: s(g)*abs(g); onsite half-turn about w commutes with all
w=np.ones(3)/np.sqrt(3); Rw=2*np.outer(w,w)-np.eye(3)
axis=[sgnperm(g)*np.abs(g) for g in R]
print("(2) half-turn about w commutes with all 24 axis-soldering images:", all(np.allclose(Rw@A,A@Rw) for A in axis),
      "| image group size:", len({tuple(np.round(A,6).ravel()) for A in axis}))
# (3) tetrahedral group: Pauli flips diag(+-1,+-1,+-1) with det 1, plus cyclic relabelling
flips=[np.diag(d).astype(float) for d in itertools.product([1,-1],repeat=3) if np.prod(d)==1]
cyc=np.array([[0,0,1],[1,0,0],[0,1,0]],float)
Tg=[f@np.linalg.matrix_power(cyc,k) for f in flips for k in range(3)]
# commutant dimension via averaging basis
basis=[np.eye(3)[:,[i]]@np.eye(3)[[j],:] for i in range(3) for j in range(3)]
avg=[sum(g@b@g.T for g in Tg)/len(Tg) for b in basis]
rank=np.linalg.matrix_rank(np.array([a.ravel() for a in avg]))
print("(3) tetrahedral group size", len({tuple(np.round(g,6).ravel()) for g in Tg}), "| commutant dimension:", rank)
