#!/usr/bin/env python3
"""
Clock-exchange site-preference no-go: no S-invariant linear selector can
prefer one named site-clock over its exchanged partner on the finite two-clock
witness. This does not rule out an S-invariant diagonal quotient or other
one-clock reduction theorem.

Shape mirrors the framework's axis-label no-gos (W-transport invariance => cannot select an
axis). Here the symmetry is the clock-swap S preserving the lattice placement and one-site
algebras on a finite two-clock witness. Deterministic, finite matrices, no RNG.
Sets no audit status (audit lane only).
"""
import numpy as np
from pathlib import Path

NOTE_PATH = Path("docs/N5_SINGLE_GENERATOR_CLOCK_EXCHANGE_INVARIANCE_NARROW_NO_GO_NOTE_2026-06-17.md")
EXPECTED_SUMMARY = "TOTAL: PASS=12 FAIL=0"

PASS=0; FAIL=0
def ck(n,ok):
    global PASS,FAIL; PASS+=ok; FAIL+=(not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}")

I2=np.eye(2,dtype=complex); sz=np.array([[1,0],[0,-1]],complex)
G1=np.kron(sz,I2); G2=np.kron(I2,sz)                      # two independent commuting clocks
# S = SWAP on C^2 (x) C^2 : exchange of two equivalent qubit sites
S=np.zeros((4,4),complex)
for i in range(2):
    for j in range(2):
        S[2*j+i, 2*i+j]=1
def conj(U,X): return U@X@U.conj().T

print("BLOCK [SOURCE BOUNDARY]:")
note_text = NOTE_PATH.read_text(encoding="utf-8")
ck("note states site-preference obstruction only", "site-preference obstruction only" in note_text)
ck("note does not close every S-invariant one-clock reduction", "does **not** prove all `S`-invariant one-clock reductions impossible" in note_text)
ck("note leaves diagonal or quotient-style reduction outside this row", "does **not** close a diagonal or quotient-style reduction" in note_text)

print("BLOCK [CLOCK-EXCHANGE SYMMETRY S] (S = site-swap preserving lattice placement and one-site algebra):")
ck("S unitary, S^2 = I", np.allclose(S@S.conj().T,np.eye(4)) and np.allclose(S@S,np.eye(4)))
ck("S exchanges the two clocks: S G1 S^dag = G2 and S G2 S^dag = G1",
   np.allclose(conj(S,G1),G2) and np.allclose(conj(S,G2),G1))
ck("S fixes the symmetric direction H_sum=G1+G2; negates antisym G1-G2 (true exchange)",
   np.allclose(conj(S,G1+G2),G1+G2) and np.allclose(conj(S,G1-G2),-(G1-G2)))

print("\nBLOCK [S-INVARIANT SELECTORS CANNOT DISTINGUISH G1,G2]:")
# Lemma: any S-invariant linear functional Phi (Phi(S X S^dag)=Phi(X)) has Phi(G1)=Phi(G2),
# since G2 = S G1 S^dag. Demonstrate with S-invariant readouts; contrast an S-breaking one.
def Sinv_funcs():
    # representative S-invariant functionals (Record-style: symmetric/additive/spectral)
    Msym=G1+G2                         # an S-invariant weight operator
    return {
      "Tr(X)            (additive trace)" : lambda X: np.trace(X),
      "Tr(X^2)          (spectral, sym)"  : lambda X: np.trace(X@X),
      "Tr(X.(G1+G2))    (S-invariant wt)" : lambda X: np.trace(X@Msym),
    }
for name,phi in Sinv_funcs().items():
    eq=np.allclose(phi(G1),phi(G2))
    ck(f"S-invariant {name}: Phi(G1)==Phi(G2) (cannot select one clock)", eq)
# an S-BREAKING functional (site-A projector weight) DOES distinguish -- i.e. selection REQUIRES breaking S
PA=np.kron(np.array([[1,0],[0,0]],complex),I2)            # "read site A only" -- breaks site-exchange
ck("S-breaking Tr(X.P_A): Phi(G1)!=Phi(G2)  => selecting a clock REQUIRES breaking S",
   not np.allclose(np.trace(G1@PA),np.trace(G2@PA)))
ck("...and P_A indeed breaks S ([P_A,S]!=0)", not np.allclose(PA@S-S@PA,0))

print("\nBLOCK [SUM-CLOCK BOUNDARY: H_sum does not reproduce retained G1 evolution]:")
def expm_h(A):
    w,V=np.linalg.eigh(A); return V@np.diag(np.exp(-1j*w))@V.conj().T
U10=expm_h(G1)                                            # the off-diagonal evolution exp(-i G1)
gaps=[np.linalg.norm(U10-expm_h(r*(G1+G2))) for r in np.linspace(0,2*np.pi,2000)]
ck(f"exp(-iG1) NOT on the sum-clock orbit exp(-ir(G1+G2)) (min gap {min(gaps):.3f}>0.05)", min(gaps)>0.05)
print("   => If G1 is retained as physical, H_sum alone does not reproduce it.")
print("      This is not a proof against a separate S-invariant diagonal quotient theorem.")

print("\nCONCLUSION (clock-exchange site-preference no-go, scoped):")
print(" Every clock-exchange(S)-INVARIANT linear selector assigns G1,G2 equal status, so it cannot")
print(" prefer one named site-clock over the other. A site-preferred clock selector requires an")
print(" S-breaking readout/preferred-site ingredient. The broader N5 one-clock reduction problem")
print(" remains open to a separate diagonal quotient, superselection, or dynamics theorem.")
summary = f"TOTAL: PASS={PASS} FAIL={FAIL}"
print(f"\n{summary}")
if summary != EXPECTED_SUMMARY:
    print(f"EXPECTED_SUMMARY mismatch: {EXPECTED_SUMMARY}")
    raise SystemExit(1)
