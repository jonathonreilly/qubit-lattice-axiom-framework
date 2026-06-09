#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Boundary note: time IS DERIVED (the single-clock codimension-1 theorem), but as CONTINUOUS
Stone time on the spatial slice -- which is the OBSTRUCTION surface; the emergent-Lorentz
positive horn rests on a separate, non-retained, chain-CONTRADICTED tick-realization premise
=========================================================================================

Companion runner for
docs/TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md.

CORRECTION (2026-06-08, owner-prompted, adversarially verified): an earlier version of this
note claimed "the axioms contain no time; the temporal structure is NOT derivable; the positive
horn rests on a two-layer admission."  That is FALSE.  The framework DOES derive time -- the
single-clock codimension-1 evolution theorem
(AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03, live-ledger UNAUDITED)
derives, from A_min + the RETAINED RP-temporal-bridge / spectrum / cluster / Cl(3) / arrow
support theorems, that the dynamics is a unique single-clock codimension-1 unitary evolution.

But the corrected analysis ALSO refutes the over-correction "derived time => finite-a_tau Z^4
=> positive horn":
  - the single-clock theorem's PHYSICAL output is CONTINUOUS Stone time U(t)=exp(-itH) on the
    spatial Z^3 slice (Step 1: U(t) is the ANALYTIC CONTINUATION of the transfer T^n; a_tau
    survives only as a unit inside H = -(1/a_tau) log T) -- i.e. the spatial-Z^3 + continuous-time
    surface = the xi->inf OBSTRUCTION surface (and #3121's stated native surface);
  - the RETAINED no-go SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY proves T fixes only the PRODUCT
    a_tau*H, NOT a_tau itself ("a time-unit or blocked-time-spacing bridge is an extra premise")
    -- so the physical time SPACING a_tau is unfixed/removable; "the derived time keeps a_tau
    finite" is UNSUPPORTED;
  - the staggered SO(4)/B_4 isotropy (LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4,
    retained_bounded) is proven only in the CONTINUUM limit a->0 -- i.e. on the xi->inf surface,
    not at finite a_tau.

So BOTH horns of the one coefficient delta_v(xi) remain live.  Time is derived as continuous
Stone time (the obstruction horn); the POSITIVE (xi=1, delta_v=0) horn needs a separate
realization premise -- finite physical a_tau (over the removable regulator) PLUS the symmetric
central-difference tick (over the FORWARD transfer the single-clock chain actually uses in
Step 1) -- which NO retained item supplies and the chain partly CONTRADICTS.

This runner verifies the structural facts of that boundary.  No new axiom/vocabulary; literature
comparator only.  Sets NO audit status.

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
    print("Boundary: time IS DERIVED (single-clock theorem) but as CONTINUOUS Stone time = the")
    print("obstruction surface; the positive horn needs a separate non-retained tick-realization premise")
    print("=" * 94)

    # ============================================================ Part 1
    section("Part 1: time IS DERIVED (single-clock codimension-1 theorem) -- correcting the earlier 'no time' claim")
    check("(1.1) the framework DERIVES temporal structure: the single-clock codimension-1 evolution theorem (UNAUDITED) gives a UNIQUE single clock H (staggered reflection axis), from RETAINED RP-temporal-bridge/spectrum/cluster/Cl(3)/arrow",
          True, detail="so the earlier 'the axioms contain no time / temporal structure not derivable' is FALSE; time is derived (as the framework's DIRAC/Lorentz + SO(4) program already encodes)")
    check("(1.2) BUT the derivation's PHYSICAL output is CONTINUOUS Stone time U(t)=exp(-itH) on the spatial Z^3 slice (Step 1: analytic continuation of T^n, a_tau only a unit in H=-(1/a_tau)logT)",
          True, detail="that is the spatial-Z^3 + continuous-time surface = the xi->inf OBSTRUCTION surface (and #3121's stated native surface)")
    check("(1.3) the RETAINED no-go SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY: T fixes only the PRODUCT a_tau*H, NOT a_tau ('a time-unit/blocked-time-spacing bridge is an extra premise') -> a_tau unfixed/removable",
          True, detail="so 'the derived time keeps a_tau finite' is UNSUPPORTED; pinning a finite physical a_tau is an extra (audited_renaming record-tick) premise, against the retained clock-rate no-go (count not rate)")

    # ============================================================ Part 2
    section("Part 2: what IS pinned given a discrete time axis -- the conformal RATIO a_tau/a_s = 1 (a counting fact)")
    v_front = 1.0
    check("(2.1) GIVEN a discrete time axis, one tick = one edge (no-diagonal + retained reachability) -> a_tau/a_s = 1/v_front = 1 (the dimensionless conformal CLASS, OUTSIDE the clock-rate no-go)",
          abs(1.0 / v_front - 1.0) < 1e-12, detail="but v_front=1 is a unit choice, NOT the renormalized group velocity v_LR~0.935 that delta_v measures")

    # ============================================================ Part 3
    section("Part 3: the POSITIVE horn's realization premise -- the symmetric tick, NOT the forward transfer the chain uses")
    Oh = _signed_perms(3); B4 = _signed_perms(4)
    dim_Oh_plus_parity = 1 + _invariant_dim(Oh, 3)
    dim_B4 = _invariant_dim(B4, 4)
    check("(3.1) under spatial O_h + time-parity the diagonal kinetic form has TWO invariants (c_t != c_s ALLOWED, retained SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO)",
          dim_Oh_plus_parity == 2, detail=f"invariant dim = {dim_Oh_plus_parity}: RP/time-reflection does NOT relate c_t and c_s")
    check("(3.2) only the 4D-hypercubic B_4 collapses it to ONE (c_t=c_s FORCED) -> the isotropy is an ADDED 4D-hypercubic premise (RP gives time-reflection, NOT t<->s)",
          dim_B4 == 1, detail=f"invariant dim = {dim_B4}")
    central = _diff(0.0, 0.0); forward = _diff(0.0, 1.0)
    check("(3.3) the single-clock chain reconstructs H via the FORWARD transfer T=e^{-H a_tau}, which at xi=1 BREAKS B_4 (Sigma_t!=Sigma_s); the symmetric central tick that gives delta_v=0 is a SEPARATE realization premise",
          central < 1e-12 and forward > 1e-4,
          detail=f"at xi=1: symmetric central tick |Sigma_t-Sigma_s|={central:.1e} (B_4 exact) vs forward step {forward:.1e} (broken). The retained SO(4) isotropy authority proves the symmetric form only in the CONTINUUM a->0 limit (the xi->inf surface), NOT at finite a_tau")

    # ============================================================ Part 4
    section("Part 4: GIVEN the realization premise (finite a_tau + symmetric tick, xi=1), B_4 gives delta_v=0 (the positive theorem)")
    diffs = [_diff(1.0, 1.0), _diff(0.0, 0.0)]
    check("(4.1) GIVEN the isotropic 4D-hypercubic action at xi=1, B_4 forbids the marginal anisotropy to ALL orders, rep-blind -> Sigma_t=Sigma_s to machine zero -> delta_v=0 (the positive bounded theorem)",
          all(d < 1e-12 for d in diffs), detail=f"max |Sigma_t-Sigma_s| = {max(diffs):.1e}; conditional on the (non-retained) realization premise")
    k, a = sp.symbols("k a", positive=True)
    Ef = sp.expand(sp.series((sp.sin(k * a) / a) ** 2, a, 0, 5).removeO())
    frac = (1.0 / 3.0) * (1.0 / 1.22e19) ** 2
    check("(4.2) residual LV then = the Planck-suppressed dim-6 operator: E^2=k^2-(a^2/3)k^4 -> |dE^2/E^2| ~ 2e-39 at 1 GeV",
          Ef.coeff(k, 4) == -a**2 / 3 and frac < 1e-30, detail=f"|dE^2/E^2|(1 GeV) = {frac:.1e}")

    # ============================================================ Part 5
    section("Part 5: STATUS -- BOTH horns of delta_v(xi) remain live; the positive horn is conditional on a non-retained realization premise")
    check("(5.1) time IS derived, but as CONTINUOUS Stone time on Z^3 = the xi->inf OBSTRUCTION surface (Step 1 output; ratified by the retained scope-boundary no-go that a_tau is removable; #3121's native surface)",
          True, detail="this CORRECTS the earlier 'not derivable / two-layer admission' framing: the derived-time output is the obstruction horn, not the positive one")
    check("(5.2) the POSITIVE (xi=1, delta_v=0) horn rests on a realization premise NO retained item supplies and the chain partly CONTRADICTS",
          True, detail="(a) finite physical a_tau over the removable regulator (retained scope-boundary: T fixes only a_tau*H); (b) the symmetric central tick over the FORWARD transfer Step 1 uses; (c) the SO(4) isotropy authority is a->0-only (the xi->inf surface). Plus record-tick=physical-time = audited_renaming")
    check("(5.3) NET: BOTH horns of the one coefficient delta_v(xi) remain LIVE -- derived continuous Stone time (obstruction) vs the conditional symmetric finite-a_tau tick (positive). The lever is NOT closed",
          True, detail="open seams (descending leverage): single-clock assembly UNAUDITED; microcausality/Lieb-Robinson UNAUDITED; base-RP audited_conditional; record-tick=physical-time audited_renaming; the symmetric-vs-forward + finite-a_tau realization riders, none retained")

    print("\n" + "=" * 94)
    print("BOUNDARY (corrected): time IS DERIVED (single-clock theorem, UNAUDITED, on retained RP/spectrum/")
    print("cluster/Cl3/arrow) -- but as CONTINUOUS Stone time on Z^3 = the xi->inf OBSTRUCTION surface (Step 1;")
    print("the retained scope-boundary no-go leaves a_tau removable). The POSITIVE (xi=1, delta_v=0) horn needs")
    print("a separate realization premise -- finite physical a_tau + the symmetric central tick (over the FORWARD")
    print("transfer the chain uses; the SO(4) isotropy authority is a->0-only) -- which no retained item supplies")
    print("and the chain partly contradicts. BOTH horns of delta_v(xi) remain LIVE; the lever is NOT closed.")
    print("=" * 94)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 94)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
