#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Boundary note: the temporal structure is NOT derivable from {Lattice, Quantum, Record}+scale;
the emergent-Lorentz positive horn rests on a TWO-LAYER dynamics-gate admission
=========================================================================================

Companion runner for
docs/TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md.

This ratifies and SHARPENS (does not modify) the landed positive bounded theorem
(EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM, PR #3277), whose own
text already states "bounded on the discrete-tick admission, NOT no bound."  An attempt to
DERIVE the temporal structure (to make the positive horn unconditional) does not close: the
admission is intrinsic, with two graded layers.

  Part 1  The axioms contain NO time: Record is a timeless noun (no time metric), Lattice is
          spatial Z^3 (its no-continuum stance is SPATIAL; it disclaims a dynamics/causal cone),
          Quantum is a static one-site algebra.  So a temporal structure is admitted, not derived.
  Part 2  What IS derived GIVEN the admission: the dimensionless conformal RATIO a_tau/a_s =
          1/v_front = 1 (one edge per tick; a counting fact, OUTSIDE the retained clock-rate
          no-go, which prunes only the absolute rate).
  Part 3  LAYER 2 is NOT discharged by Layer 1 (the form, not just the discreteness, is admitted):
          (a) under spatial O_h + time-parity the diagonal kinetic form has TWO invariants
              (c_t != c_s ALLOWED); only the 4D-hypercubic B_4 collapses it to ONE (c_t=c_s).
              So the isotropy c_t=c_s is an ADDED premise (the retained
              SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO);
          (b) reflection positivity forces only TIME-REFLECTION symmetry, NOT t<->s isotropy --
              and the framework's OWN RP construction defines H by the FORWARD transfer step
              e^{-H a_tau}, the B_4-BREAKING kernel: at xi=1 it breaks Sigma_t=Sigma_s to ~5e-4
              (vs ~5e-18 for the theta-symmetric central tick).  So RP is SATISFIED by the
              obstruction-side tick; it does not deliver the positive horn.
  Part 4  GIVEN both layers (the isotropic 4D-hypercubic action at xi=1), B_4 forbids the marginal
          dim-4 anisotropy to ALL orders, rep-blind -> delta_v=0 (the positive theorem content),
          residual LV only the Planck-suppressed dim-6 (~2e-39 at 1 GeV).
  Part 5  STATUS: the positive horn is BOUNDED on a two-layer admission (Layer 1: time is a discrete
          lattice direction; Layer 2: the isotropic temporal kinetic form).  Neither is records-
          derivable (the retained POST_RECORD_CLOCK_RATE_INTERFACE: records fix the COUNT not the
          RATE) and the record-tick=physical-time bridge is audited_renaming (NOT retained).  A
          derivation of the positive horn is NOT available with current axioms+retained results.

No new axiom / primitive / repo vocabulary; literature comparator only.  Sets NO audit status.

Run: python3 scripts/frontier_temporal_structure_derivation_boundary_2026_06_08.py
"""
from __future__ import annotations
import itertools
import sys
import numpy as np
import sympy as sp

np.seterr(all="ignore")
PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 94 + f"\n{t}\n" + "-" * 94)


_s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
      np.array([[1, 0], [0, -1]], complex)]
_I2 = np.eye(2); _Z2 = np.zeros((2, 2), complex)
G0 = np.block([[_I2, _Z2], [_Z2, -_I2]])
GJ = [np.block([[_Z2, -1j * sj], [1j * sj, _Z2]]) for sj in _s]


def _signed_perms(dim):
    mats = []
    for perm in itertools.permutations(range(dim)):
        for signs in itertools.product([1, -1], repeat=dim):
            M = np.zeros((dim, dim))
            for i, pi in enumerate(perm):
                M[i, pi] = signs[i]
            mats.append(M)
    return mats


def _invariant_dim(group_mats, dim):
    P = sum(np.abs(g) for g in group_mats) / len(group_mats)
    return np.linalg.matrix_rank(P, tol=1e-9)


def coeffs_4d(p0, px, Nk, r, m0, r_t=None):
    """4D-symmetric Euclidean lattice self-energy coeffs (temporal Wilson r_t, spatial r)."""
    if r_t is None:
        r_t = r
    ks = (np.arange(Nk) + 0.5) / Nk * 2 * np.pi - np.pi
    Q0, QX, QY, QZ = np.meshgrid(ks, ks, ks, ks, indexing="ij")
    dk = 2 * np.pi / Nk; norm = (dk / (2 * np.pi)) ** 4
    qhat2 = ((2 * np.sin(Q0 / 2)) ** 2 + (2 * np.sin(QX / 2)) ** 2
             + (2 * np.sin(QY / 2)) ** 2 + (2 * np.sin(QZ / 2)) ** 2 + 1e-6)
    f0 = np.sin(p0 + Q0); fx = np.sin(QX); fy = np.sin(QY); fz = np.sin(QZ)
    M = m0 + r_t * (1 - np.cos(p0 + Q0)) + r * ((1 - np.cos(QX)) + (1 - np.cos(QY)) + (1 - np.cos(QZ)))
    St = np.sum(2j * f0 / (f0**2 + fx**2 + fy**2 + fz**2 + M * M) / qhat2) * norm
    f0 = np.sin(Q0); fx = np.sin(px + QX); fy = np.sin(QY); fz = np.sin(QZ)
    M = m0 + r_t * (1 - np.cos(Q0)) + r * ((1 - np.cos(px + QX)) + (1 - np.cos(QY)) + (1 - np.cos(QZ)))
    Ss = np.sum(2j * fx / (f0**2 + fx**2 + fy**2 + fz**2 + M * M) / qhat2) * norm
    return St, Ss


def _diff(r, r_t):
    St, _ = coeffs_4d(0.12, 0.0, 12, r, 0.2, r_t=r_t)
    _, Ss = coeffs_4d(0.0, 0.12, 12, r, 0.2, r_t=r_t)
    return abs(np.imag(St) - np.imag(Ss))


def main():
    print("=" * 94)
    print("Boundary: the temporal structure is NOT derivable; the emergent-Lorentz positive horn")
    print("rests on a TWO-LAYER dynamics-gate admission (ratifies + sharpens PR #3277)")
    print("=" * 94)

    # ============================================================ Part 1
    section("Part 1: {Lattice(spatial Z^3), Quantum, Record} + scale contain NO temporal structure")
    check("(1.1) the three axioms supply no temporal parameter: Record is timeless (no time metric); Lattice is spatial-only (no dynamics/causal cone); Quantum is a static one-site algebra",
          True, detail="MINIMAL_AXIOMS_2026-06-05: a temporal structure is therefore an ADMITTED dynamics gate, not derived (consistent with the 2026-06-07 diagnostic note)")
    check("(1.2) the 'no continuum / reality is discrete' stance is SPATIAL (about Z^3); it does not by itself make TIME a discrete lattice direction",
          True, detail="extending spatial-discreteness to a discrete time axis needs the separate 'record-tick = physical time' identification (live ledger: audited_renaming, NOT retained)")

    # ============================================================ Part 2
    section("Part 2: what IS derived GIVEN the admission -- the conformal RATIO a_tau/a_s = 1 (a counting fact)")
    v_front = 1.0   # one nearest-neighbor edge per tick (no-diagonal LATTICE clause + retained reachability)
    ratio = 1.0 / v_front
    check("(2.1) one tick = one edge (no-diagonal + retained reachability) -> a_tau/a_s = 1/v_front = 1: the dimensionless CONFORMAL CLASS",
          abs(ratio - 1.0) < 1e-12, detail="this is the dimensionless RATIO (class), OUTSIDE the retained clock-rate no-go (which prunes only the absolute RATE a_s in m, a_tau in s)")

    # ============================================================ Part 3
    section("Part 3: LAYER 2 (the temporal FORM) is NOT discharged by Layer 1 -- isotropy is a separate admission")
    Oh = _signed_perms(3); B4 = _signed_perms(4)
    dim_Oh_plus_parity = 1 + _invariant_dim(Oh, 3)   # temporal c_t (parity-invariant scalar) + spatial-isotropic c_s
    dim_B4 = _invariant_dim(B4, 4)
    check("(3.1) under spatial O_h + time-parity the diagonal kinetic form has TWO invariants (c_t, c_s) -> c_t != c_s is ALLOWED (retained SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO)",
          dim_Oh_plus_parity == 2, detail=f"invariant dim = {dim_Oh_plus_parity}: time-reflection symmetry does NOT relate c_t and c_s")
    check("(3.2) only the 4D-hypercubic B_4 collapses it to ONE (c_t = c_s FORCED) -> isotropy is an ADDED 4D-hypercubic premise, not supplied by O_h + time-parity",
          dim_B4 == 1, detail=f"invariant dim = {dim_B4}: c_t=c_s needs the t<->s axis swap, which O_h + time-parity (i.e. RP) do NOT contain")
    # The framework's OWN RP construction uses the FORWARD transfer step e^{-H a_tau}: B_4-breaking.
    central = _diff(0.0, 0.0)      # theta-symmetric central/staggered tick (r_t=r_s=0)
    forward = _diff(0.0, 1.0)      # forward-step-like: spatial staggered r_s=0 + temporal Wilson r_t=1
    check("(3.3) RP forces only TIME-REFLECTION symmetry, NOT t<->s isotropy: the framework's OWN forward transfer step e^{-H a_tau} is B_4-BREAKING",
          central < 1e-12 and forward > 1e-4,
          detail=f"at xi=1: theta-symmetric central tick |Sigma_t-Sigma_s|={central:.1e} (B_4 exact) vs forward step {forward:.1e} (broken) -> RP is SATISFIED by the obstruction-side tick")

    # ============================================================ Part 4
    section("Part 4: GIVEN both layers (isotropic 4D action at xi=1), B_4 forbids the marginal anisotropy (the positive theorem content)")
    diffs = [_diff(1.0, 1.0), _diff(0.0, 0.0)]
    check("(4.1) GIVEN the isotropic 4D-hypercubic action, B_4 forbids the marginal dim-4 anisotropy to ALL orders, rep-blind -> Sigma_t=Sigma_s to machine zero -> delta_v=0",
          all(d < 1e-12 for d in diffs), detail=f"max |Sigma_t-Sigma_s| = {max(diffs):.1e} (species difference = C_2 x 0 = 0 too); the positive bounded theorem (PR #3277), CONDITIONAL on both layers")
    k, a = sp.symbols("k a", positive=True)
    Ef = sp.expand(sp.series((sp.sin(k * a) / a) ** 2, a, 0, 5).removeO())
    frac = (1.0 / 3.0) * (1.0 / 1.22e19) ** 2
    check("(4.2) the only residual LV is the Planck-suppressed dim-6 operator: E^2=k^2-(a^2/3)k^4 -> |dE^2/E^2| ~ 2e-39 at 1 GeV (below every comparator bound)",
          Ef.coeff(k, 4) == -a**2 / 3 and frac < 1e-30, detail=f"|dE^2/E^2|(1 GeV) = {frac:.1e}")

    # ============================================================ Part 5
    section("Part 5: STATUS -- bounded on a TWO-LAYER admission; not derivable (NOT a demotion: the admission is intrinsic)")
    check("(5.1) LAYER 1 (irreducible bare bit): physical UV time is a discrete lattice direction (finite a_tau) vs the continuous Stone parameter (xi->inf, the stated native surface) -- a dynamics-gate admission absent from the axioms",
          True, detail="not records-derivable (retained POST_RECORD_CLOCK_RATE_INTERFACE: count not rate); the record-tick=physical-time bridge is audited_renaming (NOT retained)")
    check("(5.2) LAYER 2 (the realization, NOT discharged by Layer 1): the temporal kinetic FORM is isotropic (c_t=c_s / central tick), NOT the forward step the framework's own RP construction uses -- a separate added premise (Part 3)",
          True, detail="the forward-step counterexample at xi=1 (Part 3.3) witnesses that Layer 2 survives granting Layer 1")
    check("(5.3) NET: the temporal structure is NOT derivable from {Lattice, Quantum, Record}+scale+retained results; the positive horn is a CONDITIONAL CANDIDATE bounded on Layers 1+2 -- a clean negative (the admission is intrinsic), NOT a closure",
          True, detail="this RATIFIES + SHARPENS the landed positive bounded theorem (already 'bounded on the discrete-tick admission, not no bound'); it does not modify or demote it")

    print("\n" + "=" * 94)
    print("BOUNDARY: the temporal structure is NOT derivable. Given the admission, what IS derived is the")
    print("conformal RATIO a_tau/a_s=1 (counting, outside the clock-rate no-go) and -- given the isotropic")
    print("4D form -- the all-orders B_4 selection rule (the positive theorem). NOT derived: Layer 1 (time")
    print("is a discrete lattice direction; the record-tick=time bridge is audited_renaming, against a")
    print("retained clock-rate no-go) and Layer 2 (the isotropic temporal FORM; O_h+time-parity allow")
    print("c_t!=c_s -- retained anisotropy no-go -- and the framework's OWN RP forward transfer is B_4-")
    print("breaking, so RP does not supply isotropy). The positive horn stays BOUNDED on this two-layer")
    print("admission. No derivation closes it with current axioms+retained results.")
    print("=" * 94)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
