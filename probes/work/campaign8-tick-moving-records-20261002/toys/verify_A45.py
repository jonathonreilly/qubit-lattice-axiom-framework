"""Coordinator check of the core step of A45's lemma F: under full soldering, a half-turn C about an axis through a site
maps any Pauli monomial A to C(A) that COMMUTES with A (pairs of swapped sites contribute anticommutations in pairs;
fixed sites contribute none). Controls: a half-turn that is NOT soldered on fixed sites (extra quarter phase) breaks it.
Work in GF(2) symplectic form on a 5x5x5 window, half-turn about the z axis through the centre (soldered action: conjugation by sigma_z)."""
import numpy as np, itertools
rng=np.random.default_rng(7)
L=5; c=2
sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}; N=len(sites)
def C2z(s): return (2*c-s[0], 2*c-s[1], s[2])
perm=np.array([idx[C2z(s)] for s in sites])
def image(x,z):           # soldered: conj by sigma_z keeps X->-X, Z->Z (signs irrelevant mod 2) => bits unchanged, sites permuted
    x2=np.zeros(N,int); z2=np.zeros(N,int); x2[perm]=x; z2[perm]=z; return x2,z2
def image_bad(x,z):       # control: fixed sites get an extra quarter turn about z: X->Y (x stays, z flips with x)
    x2,z2=image(x,z); fixed=perm==np.arange(N); z2=z2.copy(); z2[fixed]=(z2[fixed]+x2[fixed])%2; return x2,z2
def symp(a,b): return (np.dot(a[0],b[1])+np.dot(a[1],b[0]))%2
anti=0; anti_bad=0; T=3000
for _ in range(T):
    x=rng.integers(0,2,N); z=rng.integers(0,2,N)
    anti+=symp((x,z),image(x,z)); anti_bad+=symp((x,z),image_bad(x,z))
print(f"soldered half-turn: {anti}/{T} monomials anticommute with their image (lemma F core step expects 0)")
print(f"control (extra quarter phase on fixed sites): {anti_bad}/{T} anticommute (expected ~half)")
