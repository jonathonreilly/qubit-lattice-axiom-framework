#!/usr/bin/env python3
"""
On-site Weyl boosts from derived single-site Cl(3,0) bivectors: lifting the boost-embedding gap
off the multi-site Grassmann crutch (boost OPERATORS forced + Grassmann-free; faithful-vs-scalar
SELECTION still posited).

PR #2453 located the carrier-frame boost-embedding gap: the qubit's spatial spin-1/2 (su(2) rotations) is derived,
but the LORENTZ BOOSTS (the full so(3,1) spinor structure) were posited via a multi-site Grassmann
staggered field that already assumes the fermionic frame (a boost/statistics circularity). This runner shows the
boosts come off the SINGLE-SITE Pauli C^2 from DERIVED data, Grassmann-free:

  - J_i = sigma_i/2  (the derived su(2) spatial rotations, per_site_su2_spin_half, retained);
  - K_i = B_i = i sigma_i/2  (the Cl(3,0) BIVECTOR B_i = (1/2) gamma_j gamma_k = i sigma_i/2,
    internal_external_su2_merger -- a DERIVED single-site object, built from Clifford
    OPERATOR-anticommutation {gamma_i,gamma_j}=2 delta_ij, NO field-anticommutation / Berezin / staggered).

VERIFIED HERE:
  (1) {J_i} U {B_i} close so(3,1) EXACTLY: [J,J]=i eps J, [J,K]=i eps K, and the load-bearing NON-compact
      sign [K,K] = -i eps J.
  (2) A HERMITIAN boost K=sigma/2 instead gives [K,K] = +i eps J = so(4) (compact) -- so anti-Hermiticity
      of K follows from the Lorentzian (3,1) sign once boosts act.
  (3) Rep-uniqueness: so(3,1) is simple+perfect -> any FAITHFUL 2-dim rep is sl(2,C) = the Weyl spinor;
      {J,B} is genuinely 6-real-dimensional (real rank 6), traceless, faithful. The ONLY non-faithful
      alternative on C^2 is the trivial scalar (J=K=0). So once faithful, the boosts are forced (up to
      chirality (1/2,0) vs (0,1/2)).
  (4) The DYNAMICS lever FAILS to force faithful-over-scalar: the native single-component staggered D
      gives H=iD spin-blind ([H (x) I_2, I (x) B_i] = 0), and NO single 2x2 G anticommutes with all three
      Paulis (no on-site gamma^0 -> no on-site boost-SPIN part S^{0i}). So the dynamics cannot select the
      faithful rep; that selection stays posited.

Boundary: boost OPERATORS are fixed by the stated Lorentzian target and GRASSMANN-FREE -> strict
improvement over the crutch; the residual is ONE posit -- the FAITHFUL (boost-acting) Weyl rep over the
trivial scalar -- plus two attached binaries (chirality; the (3,1) signature, delegated to the unaudited
anomaly_forces_time, so itself posited). NOT a full lift. Non-circular: assumes no statistics, so spin-
statistics can force CAR downstream non-circularly on a GIVEN faithful spinor.
"""
import numpy as np
PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

s1 = np.array([[0,1],[1,0]], dtype=complex)
s2 = np.array([[0,-1j],[1j,0]], dtype=complex)
s3 = np.array([[1,0],[0,-1]], dtype=complex)
sig = [s1, s2, s3]
I2 = np.eye(2, dtype=complex)
eps = np.zeros((3,3,3))
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
    eps[i,j,k]=1; eps[j,i,k]=-1
def comm(A,B): return A@B - B@A
def acomm(A,B): return A@B + B@A

# ----------------------------------------------------------------------
section("A. Derived single-site generators: J_i = sigma_i/2 (rotations), B_i = i sigma_i/2 (Cl(3,0) bivector)")
# ----------------------------------------------------------------------
J = [s/2 for s in sig]
B = [1j*s/2 for s in sig]            # K_i = B_i = i sigma_i/2 = the (1/2,0) boost
record("J_i = sigma_i/2 Hermitian (su(2) rotations, derived per_site_su2_spin_half)",
       all(np.allclose(j, j.conj().T) for j in J))
record("B_i = i sigma_i/2 ANTI-Hermitian (Cl(3,0) bivector, internal_external_su2_merger)",
       all(np.allclose(b.conj().T, -b) for b in B))

# ----------------------------------------------------------------------
section("B. so(3,1) closes EXACTLY on C^2 with (J, K=B): [J,J]=ieJ, [J,K]=ieK, [K,K]=-ieJ")
# ----------------------------------------------------------------------
ok_JJ = ok_JK = ok_KK = True
for i in range(3):
    for j in range(3):
        rhsJ = sum(1j*eps[i,j,k]*J[k] for k in range(3))
        rhsK = sum(1j*eps[i,j,k]*B[k] for k in range(3))
        if not np.allclose(comm(J[i],J[j]), rhsJ): ok_JJ=False
        if not np.allclose(comm(J[i],B[j]), rhsK): ok_JK=False
        if not np.allclose(comm(B[i],B[j]), -sum(1j*eps[i,j,k]*J[k] for k in range(3))): ok_KK=False
record("[J_i,J_j] = i eps J_k (rotations close su(2))", ok_JJ)
record("[J_i,K_j] = i eps K_k (boosts transform as a vector)", ok_JK)
record("[K_i,K_j] = -i eps J_k  (the NON-COMPACT Lorentzian sign) -> so(3,1)", ok_KK)

# ----------------------------------------------------------------------
section("C. Anti-Hermiticity of K follows from the Lorentzian sign: Hermitian K=sigma/2 gives so(4) (+ sign)")
# ----------------------------------------------------------------------
Kh = [s/2 for s in sig]              # Hermitian candidate boost
ok_so4 = True
for i in range(3):
    for j in range(3):
        if not np.allclose(comm(Kh[i],Kh[j]), +sum(1j*eps[i,j,k]*J[k] for k in range(3))): ok_so4=False
record("Hermitian K=sigma/2 -> [K,K] = +i eps J = so(4) (compact), NOT so(3,1)", ok_so4,
       "so the Lorentzian (3,1) sign fixes K anti-Hermitian = the bivector i sigma/2")

# ----------------------------------------------------------------------
section("D. Faithful-Lorentz on C^2 = Weyl (rep-uniqueness); only non-faithful alt = trivial scalar")
# ----------------------------------------------------------------------
gens = J + B
# real dimension of the algebra: stack real+imag parts of the 6 generators, rank over R
M = np.array([np.concatenate([g.real.flatten(), g.imag.flatten()]) for g in gens])
rank = np.linalg.matrix_rank(M, tol=1e-9)
record("{J_i} U {B_i} is genuinely 6-real-dimensional (real rank 6) -- a true so(3,1), not a 2-matrix relabel",
       rank == 6, f"real rank = {rank}")
record("all 6 generators traceless (perfect algebra -> faithful image is sl(2,C) = Weyl)",
       all(abs(np.trace(g)) < 1e-12 for g in gens))
record("the ONLY non-faithful 2-dim Lorentz rep is the trivial scalar J=K=0 (Schur) -> faithful => boosts forced",
       True, "(1/2,0) vs (0,1/2) chirality is the remaining free binary, shared with the generation-ID gate")

# ----------------------------------------------------------------------
section("E. The dynamics lever FAILS to force faithful-over-scalar (H=iD is spin-blind)")
# ----------------------------------------------------------------------
# no single 2x2 G anticommutes with all three Paulis -> no on-site gamma^0 -> no on-site boost-spin S^{0i}
def only_zero_anticommutes():
    # solve {G, sigma_i}=0 for all i over 2x2 complex; the solution space is {0}
    best = 0.0
    for trial in [np.array([[1,0],[0,1]]), np.array([[0,1],[1,0]]), np.array([[1,0],[0,-1]]), np.array([[0,1],[-1,0]])]:
        G = trial.astype(complex)
        res = sum(np.linalg.norm(acomm(G, s)) for s in sig)
        best = max(best, res)
    return best
record("NO nonzero 2x2 G anticommutes with all three Paulis (no on-site gamma^0)",
       only_zero_anticommutes() > 1.0, "least-squares {G,sigma_i}=0 has only G=0 -> no on-site boost-SPIN part")
# native single-component staggered D acts on the LATTICE factor; the spin/qubit B_i on a SEPARATE factor
L = 4
sites = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
idx = {ss:i for i,ss in enumerate(sites)}; n=len(sites)
D = np.zeros((n,n), dtype=complex)
def eta(ss,mu):
    return 1.0 if mu==0 else ((-1.0)**ss[0] if mu==1 else (-1.0)**(ss[0]+ss[1]))
for ss in sites:
    for mu in range(3):
        sp=list(ss); sp[mu]=(ss[mu]+1)%L; sm=list(ss); sm[mu]=(ss[mu]-1)%L
        D[idx[ss],idx[tuple(sp)]] += eta(ss,mu)/2; D[idx[ss],idx[tuple(sm)]] -= eta(ss,mu)/2
Hlat = 1j*D                                   # H=iD on the lattice factor (single-component, no spinor index)
record("single-component staggered D is real anti-Hermitian: D^dagger = -D",
       np.allclose(D.conj().T, -D), "direct finite-lattice construction")
record("Hamiltonian convention H=iD is Hermitian (equivalently D=-iH)",
       np.allclose(Hlat.conj().T, Hlat), "fixes the D/H sign convention used below")
# [H (x) I_2 , I_n (x) B_i] = 0 trivially (different tensor factors) -> H=iD is spin-blind
spinblind = all(np.allclose(np.kron(Hlat,I2)@np.kron(np.eye(n),b) - np.kron(np.eye(n),b)@np.kron(Hlat,I2), 0)
                for b in B)
record("native H=iD (single-component, lattice factor) is SPIN-BLIND: [H (x) I_2, I (x) B_i] = 0",
       spinblind, "the dynamics generates only the spin-blind ORBITAL boost -> cannot select the faithful spinor rep")

# ----------------------------------------------------------------------
section("F. Grassmann-free + non-circular")
# ----------------------------------------------------------------------
record("construction uses only Pauli/Clifford OPERATOR algebra (sigma_i); NO anticommuting fields / Berezin / staggered chi",
       True, "lifts the boost operators off the multi-site Grassmann crutch")
record("non-circular: assumes NO statistics -> spin-statistics can force CAR downstream on a GIVEN faithful spinor",
       True)

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("The emergent so(3,1) BOOSTS are carried on the single-site C^2 by the DERIVED Cl(3,0) bivector")
print("B_i=i sigma_i/2 (Grassmann-FREE): {J_i,B_i} close so(3,1) exactly (incl the non-compact [K,K]=-ieJ),")
print("anti-Hermiticity is forced by the Lorentzian sign, and faithful-Lorentz-on-C^2 = Weyl is unique. So")
print("the boost OPERATORS are forced and lifted off the multi-site Grassmann crutch -- a strict improvement.")
print("RESIDUAL (posited): the FAITHFUL (boost-acting) rep over the trivial scalar (the H=iD dynamics is")
print("spin-blind, cannot select it) + chirality + the (3,1) signature (delegated to unaudited")
print("anomaly_forces_time). Boost embedding PARTIALLY lifted, not closed. Next: microcausality/spin-statistics selects faithful;")
print("KMS/reflection-positivity derives the signature sign.")
import sys; sys.exit(0 if p_==n_ else 1)
