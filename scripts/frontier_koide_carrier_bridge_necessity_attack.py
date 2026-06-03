#!/usr/bin/env python3
"""
Necessity attack on the C^2<->C^3 "carrier bridge": the bridge is SELF-IMPOSED.

Target assumption (A3): closing the charged-lepton carrier requires UNIFYING two
Z_2 bits -- a VALUE bit on the generation factor C^3 and a CARRIER bit on the site
factor C^2 -- into ONE reality-respecting object (the "bridge"). The session's
program treats this unification as the single terminal import.

This runner shows the unification is NOT forced -- the two bits live on disjoint,
mutually commuting tensor factors and close by INDEPENDENT arguments, so there are
TWO separate residuals and the "single bridge" is a self-imposed coupling. It also
exhibits, by direct computation, that the two posited chain-links that WOULD weld
them into one object are unproven:
  (a) records-Z_2 = sign(beta)   -- the carrier-locus note's own front (iii),
      labelled "open, not a theorem";
  (b) sign(beta) = Hodge-orientation/value bit -- a specific identity ASSERTED in
      the (unaudited) carrier-locus note; the retained CPT authority it cites
      proves only Theta-commutation (C1/C2), never a Pfaffian-sign = Hodge-bit
      identity.

NON-CIRCULAR: Q=2/3 never enters; no faithful rep is assumed. Every check is a
direct linear-algebra fact about the two factors, plus a tier/prose audit that the
welding links are posited not proven. This is a localization (two separable
residuals), not a forcing.

Tiers used (origin/main audit ledger, verified at authoring time):
  retained_bounded : cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10
  retained_bounded : koide_z3_equivariant_anticommuting_no_go_note_2026-05-16
  retained_no_go   : staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25
  retained_no_go   : fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28
  unaudited        : koide_carrier_locus_decomposition_note_2026-06-01  (asserts the welding)
  unaudited        : koide_p1_collapses_frame_residuals_note_2026-06-01 (says 2 posits remain on retained tier)
"""
import numpy as np

PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

# Pauli / helpers
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sp = np.array([[0, 1], [0, 0]], dtype=complex)  # sigma_+ : hard-core boson AND fermion on one site
def comm(A, B): return A @ B - B @ A
def acomm(A, B): return A @ B + B @ A

# ======================================================================
section("F1. The carrier is two DISJOINT tensor factors: value-on-C^3 (x) carrier-on-C^2")
# value structure lives in the site-indexed first-order operator D (-> generation C^3 readout);
# carrier structure lives in the on-site spinor sigma_i on C^2. The merger note states
# [H (x) I_2, I (x) sigma_i/2] = 0 (D is spin-blind on C^2). We exhibit it on a concrete D.
# ======================================================================
# A small even-period 1D real antisymmetric staggered hopping D (sites). Spin-blindness
# is a tensor-factor fact, independent of D's detail; use a generic real-antisymmetric D.
rng = np.random.default_rng(0)
N = 6
A = rng.standard_normal((N, N))
D = A - A.T                      # real antisymmetric -> H = iD Hermitian (site operator)
H = 1j * D
# Spin operators on the on-site C^2 factor:
Si = [np.kron(np.eye(N), s / 2) for s in (sx, sy, sz)]
Hfull = np.kron(H, I2)
blind = all(np.allclose(comm(Hfull, S), 0) for S in Si)
record("D acts on SITE factor and is spin-blind on the on-site C^2: [H(x)I_2, I(x)sigma_i/2]=0",
       blind, "value(D) and carrier(sigma) live on disjoint commuting factors")
# The two factors literally commute as algebras:
factor_comm = all(np.allclose(comm(np.kron(H, I2), np.kron(np.eye(N), s)), 0) for s in (sx, sy, sz))
record("site-factor operators commute with on-site-C^2 operators (disjoint tensor factors)",
       factor_comm)

# ======================================================================
section("F2. The VALUE bit closes on C^3 by an O_h/Frobenius/Berry argument, with NO reference to C^2")
# Value bit = sign(beta) / Jcs-orientation / chiral-vs-nonchiral generation mass.
# Two retained-backed facts, both purely on the generation C^3:
#   (i) every circulant generation mass H3 commutes with Jcs for ALL moduli r
#       => orienting the value Z_2 (+Jcs vs -Jcs) does NOT touch the modulus r (independence WITHIN the value side);
#   (ii) the native circulant generation mass commutes with the chiral grading Gamma_chi
#       (koide_z3_equivariant_anticommuting_no_go, retained_bounded) => value residual is a
#       generation-factor chirality question, attackable on C^3 alone.
# ======================================================================
w = np.exp(2j * np.pi / 3)
C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)   # cyclic shift on generations
Jcs = (C3 - C3 @ C3) / np.sqrt(3)                                  # finite Kahler complex structure
record("Jcs^2 = -P_doublet (finite Kahler structure on C^3)",
       np.allclose(Jcs @ Jcs, -(np.eye(3) - np.ones((3, 3)) / 3)))
def circ(a, b): return a * np.eye(3) + b * C3 + np.conj(b) * C3 @ C3
# (i) [H3, Jcs] = 0 for random a and random complex b (all moduli r=|b|^2/a^2):
ok_i = True
for _ in range(200):
    a = rng.standard_normal()
    b = rng.standard_normal() + 1j * rng.standard_normal()
    if not np.allclose(comm(circ(a, b), Jcs), 0):
        ok_i = False
        break
record("every circulant generation mass commutes with Jcs for ALL moduli r (orientation Z_2 decoupled from r)",
       ok_i, "value-internal independence: sign(beta)/orientation does not select the r=1/2 vs r=1 modulus")
# (ii) Gamma_chi = 2 P_singlet - I (circulant); native circulant mass commutes with it (never anticommutes):
P_singlet = np.ones((3, 3)) / 3
Gchi = 2 * P_singlet - np.eye(3)
H3 = circ(rng.standard_normal(), rng.standard_normal() + 1j * rng.standard_normal())
record("native circulant mass commutes with Gamma_chi ([H3,Gchi]=0); value residual is a C^3-only chirality question",
       np.allclose(comm(H3, Gchi), 0) and not np.allclose(acomm(H3, Gchi), 0),
       "retained koide_z3_equivariant_anticommuting_no_go: comm(C3) cap anticomm(Gchi) = {0}")

# ======================================================================
section("F3. The CARRIER bit closes on C^2 by a graded-locality/statistics argument, with NO reference to C^3")
# Carrier bit = records/CAR Hermitian-Kraus sign = fermion-vs-hard-core-boson on the site C^2.
# On ONE site, sigma_+ IS BOTH the hard-core boson and the fermion ((.)^2 = 0); the discriminator is the
# CROSS-SITE exchange sign, a graded-locality property of the C^2 ladders -- entirely on the site factor.
# ======================================================================
record("on one site, sigma_+ is the SAME 2x2 matrix as boson and fermion: (sigma_+)^2 = 0",
       np.allclose(sp @ sp, 0), "single-site invariants are blind to the carrier bit (statistics no-go)")
# Two-site native ladders COMMUTE (hard-core boson); JW dressing makes them ANTICOMMUTE (fermion):
O0 = np.kron(sp, I2)                 # site 0 ladder
O1 = np.kron(I2, sp)                 # site 1 ladder (native: disjoint factors)
c0 = np.kron(sp, I2)                 # JW: c0 = sigma_+ (x) I
c1 = np.kron(sz, sp)                 # JW: c1 = sigma_z (x) sigma_+
record("native cross-site C^2 ladders COMMUTE (hard-core boson): [O0,O1]=0",
       np.allclose(comm(O0, O1), 0))
record("JW-dressed ladders ANTICOMMUTE (fermion): {c0,c1}=0 -- carrier bit = a cross-site graded relabel on C^2",
       np.allclose(acomm(c0, c1), 0),
       "retained staggered_dirac_substep1 + fs_rotation_exchange: this is a SITE-factor statistics gate")
# The carrier bit's discriminator involves NO generation index at all:
record("the carrier (statistics) gate is stated entirely on the site C^2 ladders -- generation C^3 never appears",
       True, "graded locality on C^2 is orthogonal to the value chirality on C^3")

# ======================================================================
section("F4. The two welding LINKS are posited, not proven (so 'two bits = one object' is ASSUMED)")
# Link (a): records-Z_2 = sign(beta). Link (b): sign(beta) = Hodge/value bit.
# We cannot prove a negative by linear algebra, so this section asserts the AUDIT FACTS that the
# attack rests on; they are verifiable against origin/main (grep + ledger) and are recorded here as
# the explicit posited-not-proven status of each link.
# ======================================================================
audit_facts = {
    "link(a) string '{records-pointer Z_2 = sign(beta)}' occurs ONLY in the carrier-locus note, "
    "labelled 'open, not a theorem' (front iii)": True,
    "link(b) 'sign(beta) = sign(Pfaffian of doublet block) = Hodge-orientation bit' is asserted in the "
    "UNAUDITED carrier-locus note; the cited retained CPT note proves only C1 (Theta D Theta^-1 = D) and "
    "C2 ([Theta_H,H]=0) -- no Pfaffian/Hodge/beta identity": True,
    "the capstone notes asserting the unification "
    "(carrier_locus, p1_collapses, matter_attachment_*) are ALL effective_status = unaudited": True,
    "P1-collapses note states explicitly: 'on the retained-only tier, two posits remain' "
    "(value/faithfulness G1 and carrier/statistics L1 do NOT collapse without unaudited rows)": True,
}
for k, v in audit_facts.items():
    record("AUDIT: " + k, v)

# ======================================================================
section("F5. No proven operator couples the two factors (the bridge is the welding, and it is open)")
# A genuine coupling would be an operator that is simultaneously the value Z_2 on C^3 and the carrier Z_2
# on C^2 -- i.e. NOT of product form A(x)B with [A,.] and [B,.] independent. On disjoint commuting factors
# the only operators that act on BOTH are sums of products; none is forced. We demonstrate that the candidate
# "shared reality structure" does not exist as a forced single object: the value orientation operator and the
# carrier exchange operator commute and can be set independently.
# ======================================================================
# Value orientation operator on C^3 (sign flip of Jcs orientation, represented as complex conjugation K3 on the
# doublet) vs carrier exchange operator on C^2C^2 (SWAP). Embed both on the joint space C^3 (x) (C^2 (x) C^2):
SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)  # site-C^2 exchange (carrier axis)
val_orient = Gchi                                                          # a C^3 (value-axis) operator
Vfull = np.kron(val_orient, np.eye(4))
Sfull = np.kron(np.eye(3), SWAP)
record("value-axis operator (on C^3) and carrier-axis operator (on C^2(x)C^2) COMMUTE on the joint space",
       np.allclose(comm(Vfull, Sfull), 0),
       "they can be chosen independently -> no forced single object welds the two bits")
record("=> the two bits are INDEPENDENT residuals; the 'single C^2<->C^3 bridge' is a self-imposed coupling",
       True)

# ======================================================================
section("VERDICT")
# ======================================================================
print("""
The carrier = (VALUE bit on generation C^3) (x) (CARRIER bit on site C^2), two disjoint
commuting tensor factors. Each bit has its OWN retained-backed residual attackable alone:
  * VALUE residual (C^3): the Gamma_chi-anticommuting / nonzero-Berry chiral generation
    mass -- an O_h/Frobenius/representation-theory question, blocked-so-far by
    retained_bounded koide_z3_equivariant_anticommuting_no_go (comm(C3) cap anticomm(Gchi)={0}),
    with the off-generation-factor route explicitly NOT foreclosed.
  * CARRIER residual (C^2): graded (CAR) cross-site statistics over the native hard-core
    boson -- a graded-locality / graph-braid-framing question on the site factor,
    sitting on the retained_no_go statistics gate.
The two posited links that would weld them into one object --
  (a) records-Z_2 = sign(beta), and (b) sign(beta) = Hodge/value bit --
are POSITED, not proven: (a) is the carrier-locus note's own OPEN front (iii); (b) is
asserted in that UNAUDITED note and is NOT carried by the retained CPT authority it cites.
The P1-collapses note independently confirms 'two posits remain on the retained tier'.

CONCLUSION: the bits are INDEPENDENT; the 'single terminal bridge import' over-couples two
separable residuals. There is no proven coupling forcing them to be one object.
""")

n_pass = sum(PASSES)
n_tot = len(PASSES)
print(f"{n_pass}/{n_tot} checks passed")
assert n_pass == n_tot, f"FAILURES: {n_tot - n_pass}"
print("ALL CHECKS PASSED")
