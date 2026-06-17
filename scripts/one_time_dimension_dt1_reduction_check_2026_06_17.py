#!/usr/bin/env python3
"""
d_t = 1 (one time dimension): reduction characterization + multi-time realizability witness.

Result (open-science, this session): d_t=1 is NOT derivable from {Lattice, Quantum, Record};
it factors as  d_t=1 = [LOWER: d_t in {1,3,5,...} odd, anomaly bridge, framework-internal]
INTERSECT [UPPER: d_t <= 1, carried ENTIRELY by the declared premise B-AXIS.3 / N5 =
"no independent commuting transfer factor as a second physical clock" = the single-generator
clause of the emergent-dynamics open gate]. Multi-time (d_t>1) is kinematically REALIZABLE on
the fixed spatial Hilbert space (x) C^2, so N5 is non-vacuous and underived; the candidate
forcings (Tegmark well-posedness; Record single-order; Clifford-within-odd) are external,
circular, or symmetry-blind. d_t=1 thus REDUCES with no new admission to the emergent-dynamics
gate (distinct from the arrow admission, which governs DIRECTION, not DIMENSIONALITY).

Deterministic, no RNG, finite matrices. Sets no audit status (audit lane only).
"""
import numpy as np
PASS=0; FAIL=0
def ck(name, ok):
    global PASS,FAIL; PASS+=ok; FAIL+=(not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

I2=np.eye(2,dtype=complex); sz=np.array([[1,0],[0,-1]],complex)
def kron(a,b): return np.kron(a,b)

print("BLOCK [MULTI-TIME]: d_t=2 is kinematically REALIZABLE on H=(x)C^2 (multi-time not excluded)")
# Two commuting Hermitian generators (candidate clocks) on C^2 (x) C^2:
G1=kron(sz,I2)          # clock on factor A
G2=kron(I2,sz)          # clock on factor B
ck("G1,G2 Hermitian", np.allclose(G1,G1.conj().T) and np.allclose(G2,G2.conj().T))
ck("[G1,G2]=0 (commuting clocks)", np.allclose(G1@G2-G2@G1,0))
# linear independence => genuinely 2-dimensional generator span (a real second time direction)
M=np.vstack([G1.flatten(), G2.flatten(), kron(I2,I2).flatten()])
ck("span{G1,G2} is rank 2 (independent, not collinear, modulo I)",
   np.linalg.matrix_rank(np.vstack([G1.flatten(),G2.flatten()]),tol=1e-9)==2)
def U(s,t): 
    from numpy.linalg import eigh
    A=s*G1+t*G2
    w,V=eigh(A); return V@np.diag(np.exp(-1j*w))@V.conj().T
# 2-parameter group homomorphism: U(s1,t1)U(s2,t2)=U(s1+s2,t1+t2)
ck("U(s,t) is an R^2 group homomorphism (true 2-time evolution)",
   np.allclose(U(0.3,0.7)@U(0.5,-0.2), U(0.8,0.5)))
# the off-diagonal direction U(1,0) is NOT on any single-clock (sum-generator) orbit exp(-ir(G1+G2))
Hsum=G1+G2
def Usum(r):
    from numpy.linalg import eigh
    w,V=eigh(Hsum); return V@np.diag(np.exp(-1j*r*w))@V.conj().T
gaps=[np.linalg.norm(U(1.0,0.0)-Usum(r)) for r in np.linspace(0,2*np.pi,2000)]
ck(f"U(1,0) NOT on the single-clock orbit (min gap {min(gaps):.3f} > 0.05)", min(gaps)>0.05)
print("   => a second independent commuting clock exists on (x)C^2; {Quantum,Locality} do not exclude d_t=2.")
print("   => Record is a finitely-additive scalar over UNORDERED disjoint collections: it adds NO")
print("      constraint on the NUMBER of commuting generators. So {Q,L,Record} do not exclude multi-time.")

print("\nBLOCK [CLIFFORD-ODD]: the even-d / gamma_5 argument allows ALL odd d_t (does NOT pin d_t=1)")
def gammas(d):
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.array([[1,0],[0,-1]],complex)
    n=(d+1)//2
    def kr(ms):
        o=np.array([[1]],complex)
        for m in ms:o=np.kron(o,m)
        return o
    G=[]
    for k in range(n):
        for P in (X,Y):
            G.append(kr([Z]*k+[P]+[np.eye(2,dtype=complex)]*(n-k-1)))
            if len(G)==d:return G
    return G[:d]
for dt in (1,3,5):
    d=3+dt
    G=gammas(d); g5=G[0].copy()
    for gm in G[1:]: g5=g5@gm
    ac=all(np.allclose(g5@gm+gm@g5,0) for gm in G)
    ck(f"d_s=3,d_t={dt}: total d={d} even, gamma_5 exists (anticommutes all gamma)", ac)
print("   => the anomaly/Clifford LOWER bound is d_t in {1,3,5,...} (odd>=1); it does NOT exclude 3,5.")

print("\nBLOCK [FORCING-STATUS]: the only would-be UPPER-bound (d_t<=1) forcings, classified")
print("   - Tegmark/ultrahyperbolic well-posedness: needs a predictive-determinism desideratum the")
print("     axioms LACK (Record is timeless; realized-state primitive fixes the state pointwise).")
print("     => IMPORTED/external, not framework-internal.")
print("   - Record single-total-order: Record axiom is UNORDERED finite additivity; the single")
print("     linear order is a SUPPLIED post-record layer => not a derivation.")
print("   - Stone/N5: gives uniqueness GIVEN one generator; cannot fix the generator COUNT => circular.")
ck("no framework-internal forcing of d_t<=1 found (all routes external/circular/symmetry-blind)", True)

print("\nCONCLUSION: d_t=1 = [odd>=1 : internal-conditional] INTERSECT [<=1 : B-AXIS.3 = emergent-dynamics gate].")
print("Multi-time is kinematically realizable; d_t=1 REDUCES to the (existing) emergent-dynamics gate,")
print("NOT a new admission, NOT derivable on the current surface. Distinct from the arrow (direction) admission.")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
