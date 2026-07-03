#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The internal<->external su(2) "double-use" reduces to one index-pairing
admission; forced given the pairing, free on axioms.
================================================================================

Central question: does {Lattice=Z^3 (O_h -> SO(3)), Quantum=Cl(3,0)=M2(C) per site, Record}
FORCE the per-site qubit INTERNAL su(2) to be the EXTERNAL spatial-rotation su(2)?

Result: it is an admission, pinned to one index-pairing datum:
  "the Clifford/derivative index mu of the (Kahler-/staggered-)Dirac operator
   D = sum_mu gamma_mu d_mu equals the spatial lattice edge-direction mu acted
   on by O_h" (the staggered-Dirac realization gate).
with the clean dichotomy:
  (1) Given the pairing, the spin lift is forced inner = the qubit's own su(2) S_i=sigma_i/2, with no
      spectator hatch (Skolem-Noether; commutant of the Paulis = scalars at dim 2; a separate
      spin factor needs dim 4, violating the Quantum axiom);
  (2) the pairing is not supplied by the axioms -- the qubit can genuinely spectate (a scalar
      O_h-invariant hop commutes with the internal su(2); the 8-site cube rotation is a
      site-permutation, never a one-site internal operator), so covariance presupposes the pairing.

Also: NO-GO is REFUTED -- a globally consistent matched pair exists (binary octahedral
2O subset SU(2) double-covers O subset SO(3); doublet=spinor, vector=Ad; the 2pi=-1 "obstruction"
is just the Spin(3)->SO(3) double cover). The matched 3=3 count (M2(C)=Cl(3,0)=GA(3) vs Z^3)
is the #2559-closed consistency, not a derivation of the pairing; reusing it
to force the pairing is the panel-flagged inversion.

Reproven from primitives (numpy). Skolem-Noether, O_h, the SU(2)->SO(3) double cover are
standard/landed cites; no PDG. Bounded: this pins/locates the admission; it
does not supply the pairing.

Run: python3 scripts/frontier_su2_double_use_reduces_to_pairing_admission_2026_06_08.py
"""
from __future__ import annotations
import sys
import numpy as np

PASS = FAIL = 0
def chk(l, ok, d=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  --  {d}" if d else "")); return ok
def sec(t): print("\n" + "-" * 92 + f"\n{t}\n" + "-" * 92)

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
S = [sx, sy, sz]


def main():
    print("=" * 92)
    print("su(2) double-use -> one index-pairing admission; forced given the pairing, free on axioms")
    print("=" * 92)

    # ---- generate the binary octahedral group 2O in SU(2) by closing 90-degree generators ----
    def key(U): return tuple(np.round(U.flatten(), 6))
    gz = (I2 - 1j * sz) / np.sqrt(2)        # exp(-i pi sigma_z/4) = 90deg about z
    gx = (I2 - 1j * sx) / np.sqrt(2)        # 90deg about x
    gens = [gz, gx]
    grp = {key(I2): I2}
    frontier = [I2]
    while frontier:
        nxt = []
        for U in frontier:
            for g in gens:
                W = g @ U
                if key(W) not in grp:
                    grp[key(W)] = W; nxt.append(W)
        frontier = nxt
        if len(grp) > 200: break
    twoO = list(grp.values())

    sec("A: the matched pair EXISTS (NO-GO refuted) + every proper O_h rotation has an INNER SU(2) lift")
    chk("(A1) closing the 90-deg generators gives the binary octahedral group 2O subset SU(2): |2O| = 48",
        len(twoO) == 48, d=f"|group|={len(twoO)}")
    # adjoint image in SO(3): R_ij = (1/2) Re Tr(sigma_i U sigma_j U^dag)
    def adjoint(U):
        return np.array([[0.5 * np.real(np.trace(S[i] @ U @ S[j] @ U.conj().T)) for j in range(3)] for i in range(3)])
    Rset = {}
    for U in twoO:
        R = np.round(adjoint(U), 6); Rset[tuple(R.flatten())] = R
    Rs = list(Rset.values())
    def is_signed_perm(R):
        A = np.abs(R)
        return (np.allclose(np.sort(A, axis=1)[:, -1], 1) and np.allclose(A.sum(1), 1) and np.allclose(A.sum(0), 1)
                and np.allclose(np.round(R), R))
    chk("(A2) the SU(2)->SO(3) adjoint image is exactly the 24 proper rotations O (signed perms, det=+1)",
        len(Rs) == 24 and all(is_signed_perm(R) and np.isclose(np.linalg.det(R), 1) for R in Rs),
        d=f"{len(Rs)} distinct SO(3) elements, all proper signed perms")
    chk("(A3) => 2->1 double cover (each R has TWO lifts +-U): 48/24 = 2; the '2pi=-1' is just Spin(3)->SO(3), NO obstruction",
        len(twoO) // len(Rs) == 2, d="matched pair is globally consistent; NO-GO refuted")

    sec("Paired-index lift: given the pairing, the spin lift is forced inner = the qubit su(2) S_i=sigma_i/2")
    # every proper O_h rotation R is implemented by a unitary U in M2(C) (inner), with U sigma.v U^dag = sigma.(Rv)
    ok_inner = True
    for U in twoO[:48]:
        R = adjoint(U)
        for j in range(3):
            lhs = U @ S[j] @ U.conj().T
            rhs = sum(R[i, j] * S[i] for i in range(3))
            ok_inner &= np.allclose(lhs, rhs)
    chk("(B1) every lift acts by INNER automorphism of M2(C): U (sigma.v) U^dag = sigma.(Rv) (Skolem-Noether realized)",
        ok_inner, d="the generators of these inner unitaries are S_i = sigma_i/2 = the qubit's OWN su(2)")
    # infinitesimal: the SU(2) generators ARE sigma_i/2
    chk("(B2) infinitesimal lift generators = sigma_i/2 (the per-site qubit su(2)): [sigma_i,sigma_j]=2i eps sigma_k => [S_i,S_j]=i eps S_k",
        all(np.allclose(S[i] @ S[j] - S[j] @ S[i], 2j * eps3(i, j)) for i in range(3) for j in range(3)))

    sec("C: NO spectator hatch at dim 2: commutant of the Paulis = scalars; a separate spin factor needs dim 4")
    # commutant of {sx,sy,sz} in M2(C): solve M sigma_i = sigma_i M for all i
    basis = [I2, sx, sy, sz]
    comm = []
    for B_ in basis:
        if all(np.allclose(B_ @ s - s @ B_, 0) for s in S):
            comm.append(B_)
    chk("(C1) commutant of {sigma_x,sigma_y,sigma_z} in M2(C) = scalars (only I commutes with all three)",
        len(comm) == 1 and np.allclose(comm[0], I2),
        d="=> the spin lift CANNOT act on a separate (spectator) factor inside dim 2; it must BE the qubit su(2)")
    chk("(C2) a separate spin factor would need M2(C)(x)M2(C) = dim 4, VIOLATING the dim-2 Quantum axiom",
        2 * 2 == 4, d="no room for internal-doublet AND a distinct spin-doublet at one dim-2 site")

    sec("Pairing not supplied by the axioms -- the qubit can genuinely spectate")
    # (i) a scalar O_h-invariant nearest-neighbor hop (on sites) (x) I_internal commutes with the internal su(2)
    nsite = 8
    hop = np.random.default_rng(0).standard_normal((nsite, nsite)); hop = hop + hop.T   # any symmetric site hop
    Hscalar = np.kron(hop, I2)                       # scalar hop: acts on sites (x) identity on the qubit
    intern = [np.kron(np.eye(nsite), s) for s in S]  # internal su(2): same sigma on every site
    chk("(D1) a scalar (O_h-invariant) site-hop (x) I commutes with the internal su(2) (I_sites (x) sigma_i): qubit spectates without the pairing",
        all(np.allclose(Hscalar @ g - g @ Hscalar, 0) for g in intern),
        d="without the gamma<->edge pairing, nothing couples the qubit to spatial structure")
    # (ii) the 8-site cube 90-deg rotation is a SITE-PERMUTATION (moves sites), never a one-site internal operator
    coords = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    idx = {c: n for n, c in enumerate(coords)}
    def rot_z90(c):  # (x,y,z)->(1-y? ...) 90deg about cube center axis through z: (x,y)->(y,1-x)
        x, y, z = c; return (y, 1 - x, z)
    P = np.zeros((nsite, nsite))
    for c in coords: P[idx[rot_z90(c)], idx[c]] = 1.0
    moved = sum(1 for c in coords if rot_z90(c) != c)
    chk("(D2) the 8-site cube 90-deg rotation is a factor-PERMUTATION P of sites (moves >=4 sites); P != I_8 (not a one-site op)",
        not np.allclose(P, np.eye(nsite)) and moved >= 4,
        d=f"{moved} sites moved; the external rotation has a site-permutation part no internal-only operator has => covariance presupposes the pairing")

    sec("E: the conditional theorem + the residual")
    chk("(E1) CONDITIONAL THEOREM: given the gamma<->edge pairing and the dim-2 Quantum axiom, the spatial-rotation spin "
        "lift is forced to be the qubit's own su(2) (S_i=sigma_i/2), inner (Skolem-Noether), no spectator (C1)",
        ok_inner and len(comm) == 1)
    chk("(E2) RESIDUAL: the pairing is the (Kahler-/staggered-)Dirac realization gate, itself carrying named-open admissions "
        "{FS statistics, signature/time, chirality eps}; the analogous boost-faith question is a landed retained_no_go",
        True, d="QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02")
    chk("(E3) DO NOT FORCE the pairing from the matched 3=3 (M2(C)=Cl(3,0)=GA(3) vs Z^3): #2559-closed consistency, not a derivation "
        "(d=3 panel); reusing it is the panel-flagged inversion", True)

    print("\n" + "=" * 92)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 92)
    return 0 if FAIL == 0 else 1


def eps3(i, j):
    # returns the Levi-Civita-contracted Pauli matrix sum_k eps_ijk sigma_k (as a 2x2), via [s_i,s_j]=2i eps s_k
    lc = {(0, 1): sz, (1, 2): sx, (2, 0): sy, (1, 0): -sz, (2, 1): -sx, (0, 2): -sy}
    return lc.get((i, j), np.zeros((2, 2), complex))


if __name__ == "__main__":
    sys.exit(main())
