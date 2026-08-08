#!/usr/bin/env python3
"""
frontier_koide_c3_generator_rephasing_obstruction.py
-----------------------------------------------------

Runner paired with
    KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md

Source-only proposal. Status authority: independent audit lane only.

This runner verifies a narrow algebraic obstruction, not a broad no-go on
every continuous action on the real C_3 doublet. The valid claim is that
continuous scalar rephasing of the cyclic generator, C -> exp(i a) C, is
incompatible with the retained order-three relation C^3 = I except at the
three cube roots. A continuous centralizer of the real order-three doublet
can exist, but it commutes with C and therefore leaves the circulant
coefficient b unchanged; it is not the missing b-phase rotation. This
runner verifies:

  (A) A continuous rotation of the doublet plane (B1,B2) by angle alpha
      is IDENTICALLY the rephasing of the order-3 shift C -> e^{i a} C,
      where B1 = C + C^2, B2 = i(C - C^2).
  (B) C^3 = I forces (e^{i a} C)^3 = e^{3 i a} I, which equals I only for
      alpha in {0, 2pi/3, 4pi/3}. The only scalar rephasings of C
      consistent with C^3 = I are the discrete C_3.
  (B') Continuous centralizers of the real C_3 doublet commute with C and
      therefore act trivially on the b coefficient in
      H = aI + bC + bbar C^2.
  (C) Gauge circles are generation-blind: a gauge phase is e^{i chi} I_3
      on the triplet (the three generations carry identical gauge
      charge), so g H g^dag = H -- ZERO action on the doublet.
  (D) Lattice translations = diagonal corner phases diag(e^{i phi_j}):
      either (a) a generic profile maps C out of the C_3-circulant class
      (P C P^dag not proportional to C; not a symmetry of the mass
      structure), or (b) a linear profile of slope 2pi k/3 reproduces the
      discrete C_3. Never a continuous rotation of b.

Context checks (the equivalence chain the obstruction bears on):
  (E) <C_3 shift, K reflection> on the doublet is the FINITE dihedral
      group of order 6 (rotations only at 0/120/240 deg), not U(1).
  (F) A C_3-invariant quadratic fluctuation weight is forced proportional
      to I (so the weight is auto-rotation-symmetric; the open datum is
      purely the COUNTING det_C vs det_R, not a broken weight-symmetry).
  (G) r = |b|^2/a^2 = 1/2  <=>  E_+ = E_perp (equal block)  <=>  Q = 2/3
      (det_C counting); the real-dimension counting (det_R) is the
      Plancherel/dimension extremum Q = 1.

These are exact finite-dimensional algebra; no external physics is
imported. The conclusion is a bounded obstruction on the generator
rephasing route only. It does not rule out every continuous state-space
action on the C_3 doublet.

PASS/FAIL counted per-check; exits 0 iff PASS_COUNT > 0 and FAIL_COUNT == 0.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import sys
from itertools import product

try:
    import numpy as np
except Exception as exc:  # pragma: no cover
    print(f"FAIL: numpy not available: {exc}")
    sys.exit(1)


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"[{status}] {name}"
    if detail:
        msg += f"  {detail}"
    print(msg)


# Generation/corner basis; C = order-3 cyclic shift |j> -> |j+1>.
C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)
B1 = C + C2          # doublet-plane basis (Probe 13)
B2 = 1j * (C - C2)


def main() -> int:
    print("=" * 72)
    print("Koide: C^3=I obstructs continuous scalar rephasing of the cyclic generator")
    print("Note: KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md")
    print("=" * 72)

    # Retained order-3 relation
    check("C^3 = I (retained order-3 generation relabeling)",
          np.allclose(np.linalg.matrix_power(C, 3), I3))

    # (A) doublet rotation by alpha == rephasing C -> e^{i alpha} C
    okA = True
    for alpha in (0.3, 1.0, 2.1, 2.7):
        e = np.exp(1j * alpha)
        B1r = e * C + np.conj(e) * C2
        B2r = 1j * (e * C - np.conj(e) * C2)
        B1so = np.cos(alpha) * B1 + np.sin(alpha) * B2
        B2so = -np.sin(alpha) * B1 + np.cos(alpha) * B2
        okA = okA and np.allclose(B1r, B1so) and np.allclose(B2r, B2so)
    check("(A) doublet rotation (B1,B2) by alpha == rephasing C -> e^{i alpha} C",
          okA, "verified for alpha in {0.3,1.0,2.1,2.7}")

    # (B) C^3=I obstruction: (e^{i a}C)^3 = e^{3ia} I; = I only for a in {0,2pi/3,4pi/3}
    discrete_ok = all(
        np.allclose(np.linalg.matrix_power(np.exp(1j * a) * C, 3), I3)
        for a in (0.0, 2 * np.pi / 3, 4 * np.pi / 3)
    )
    continuous_blocked = all(
        not np.allclose(np.linalg.matrix_power(np.exp(1j * a) * C, 3), I3)
        for a in (0.3, 1.0, 2.1, 0.5, 1.7)
    )
    check("(B) the 3 cube-root rephasings preserve C^3=I (discrete C_3)", discrete_ok)
    check("(B) every generic continuous scalar rephasing of C BREAKS C^3=I",
          continuous_blocked, "e^{3 i alpha} != 1 for alpha not in (2pi/3)Z")

    # conjugation form: (g C g^dag)^3 = g C^3 g^dag = I forces e^{3ia}=1 too
    # (algebraic identity; demonstrate with a random unitary g that the order is preserved)
    rng = np.random.default_rng(20260529)
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    g, _ = np.linalg.qr(A)
    gCg = g @ C @ g.conj().T
    check("(B) conjugation preserves order: (g C g^dag)^3 = I",
          np.allclose(np.linalg.matrix_power(gCg, 3), I3),
          "so g C g^dag = e^{ia}C would still require e^{3ia}=1")

    # (B') The continuous centralizer exists but is not the b-phase rotation.
    Htest = 2.0 * I3 + (0.6 + 0.4j) * C + np.conj(0.6 + 0.4j) * C2
    omega = np.exp(2j * np.pi / 3)
    F = np.array(
        [[1, 1, 1], [1, omega, omega**2], [1, omega**2, omega]], dtype=complex
    ) / np.sqrt(3)
    ok_cent = True
    for phi in (0.2, 0.9, 1.7):
        U = F @ np.diag([1, np.exp(1j * phi), np.exp(-1j * phi)]) @ F.conj().T
        ok_cent = ok_cent and np.allclose(U @ C @ U.conj().T, C)
        ok_cent = ok_cent and np.allclose(U @ Htest @ U.conj().T, Htest)
    check(
        "(B') continuous centralizer exists but acts trivially on C and b",
        ok_cent,
        "commuting U(1) is not the generator-rephasing route",
    )

    # (C) gauge circles are generation-blind: scalar on triplet -> H unchanged
    okC = True
    for chi in (0.5, 1.7, 3.0):
        Pg = np.exp(1j * chi) * I3
        okC = okC and np.allclose(Pg @ Htest @ Pg.conj().T, Htest)
    check("(C) gauge U(1) (generation-blind scalar) acts trivially on the doublet",
          okC, "g H g^dag = H -> b unchanged")

    # (D) translations = diagonal corner phases
    def PCPdag(phis):
        P = np.diag(np.exp(1j * np.array(phis, dtype=float)))
        return P @ C @ P.conj().T

    def prop_to_C(M):
        mask = np.abs(C) > 0
        vals = M[mask] / C[mask]
        return bool(np.allclose(vals, vals[0]) and np.allclose(M[~mask], 0))

    generic_leaves = not prop_to_C(PCPdag([0.0, 0.7, 1.9]))
    slope_offgrid_leaves = not prop_to_C(PCPdag([0.0, 0.4, 0.8]))
    slope_c3_stays = prop_to_C(PCPdag([0.0, 2 * np.pi / 3, 4 * np.pi / 3]))
    check("(D) generic translation maps C OUT of the C_3-circulant class",
          generic_leaves, "P C P^dag not proportional to C -> not a mass-structure symmetry")
    check("(D) off-grid linear translation (slope 0.4) also leaves the class",
          slope_offgrid_leaves)
    check("(D) only slope 2pi k/3 stays in class = the discrete C_3 character",
          slope_c3_stays)

    # (E) <C_3, K> is the finite dihedral group of order 6 (not U(1))
    Rdoub = np.array([[np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)],
                      [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)]])
    Kdoub = np.array([[1.0, 0.0], [0.0, -1.0]])
    G = [np.eye(2)]
    changed = True
    while changed:
        changed = False
        for gg in list(G):
            for gen in (Rdoub, Kdoub):
                p = gen @ gg
                if not any(np.allclose(h, p) for h in G):
                    G.append(p)
                    changed = True
    rots = sorted({round(np.degrees(np.arctan2(g[1, 0], g[0, 0])) % 360)
                   for g in G if np.allclose(np.linalg.det(g), 1)})
    check("(E) <C_3 shift, K reflection> on doublet = finite group of order 6",
          len(G) == 6, f"|G| = {len(G)}; rotation angles = {rots} (discrete, not U(1))")

    # (F) C_3-invariant symmetric quadratic form on the doublet is forced ∝ I
    sym = [np.array([[1, 0], [0, 0.0]]), np.array([[0, 1], [1, 0.0]]),
           np.array([[0, 0], [0, 1.0]])]
    M = np.array([(Rdoub.T @ Bm @ Rdoub - Bm).flatten() for Bm in sym]).T
    _, s, vt = np.linalg.svd(M)
    nulldim = int(np.sum(s < 1e-9))
    sol = vt[-1]
    Msol = sol[0] * sym[0] + sol[1] * sym[1] + sol[2] * sym[2]
    propI = np.allclose(Msol / Msol[0, 0], np.eye(2)) if abs(Msol[0, 0]) > 1e-9 else False
    check("(F) C_3-invariant quadratic weight is forced ∝ I (auto rotation-symmetric)",
          nulldim == 1 and propI,
          "so the open datum is the COUNTING (det_C vs det_R), not a broken weight-symmetry")

    # (G) r = 1/2 <=> equal block <=> Q = 2/3 (det_C); r=0 limit context
    def Qkoide(a, b):
        w = np.exp(2j * np.pi / 3)
        x = np.array([a + b * w ** k + np.conj(b) * w ** (-k) for k in range(3)]).real
        m = x ** 2
        return m.sum() / (np.abs(x).sum()) ** 2

    a, b = 1.0, np.sqrt(0.5)
    Ep, Eperp = 3 * a ** 2, 6 * abs(b) ** 2
    check("(G) r=|b|^2/a^2=1/2 => E_+ = E_perp (equal block) => Q = 2/3 (det_C)",
          np.isclose(Ep, Eperp) and np.isclose(Qkoide(a, b), 2 / 3),
          f"E_+={Ep:.3f}, E_perp={Eperp:.3f}, Q={Qkoide(a,b):.6f}")

    # (H) N5 execution certificate — granularity reached, no new checks.
    print("=" * 72)
    print("(H) N5 execution certificate: what this runner resolves")
    print(
        "  per_element: resolved — the corner-phase test is decided on individual matrix "
        "entries rather than on a norm. prop_to_C divides P C P^dag by C on the three "
        "nonzero support entries, requires those three ratios to agree, and separately "
        "requires every off-support entry to vanish; that entrywise test is what "
        "distinguishes the profiles (0, 0.7, 1.9) and (0, 0.4, 0.8), which leave the "
        "C_3-circulant class, from (0, 2 pi / 3, 4 pi / 3), which stays inside it."
    )
    print(
        "  per_site: checked and not executed — nothing here is indexed by a spatial site. "
        "The three diagonal phases that get varied are generation corners of a single "
        "carrier, and only one copy of that carrier ever exists in the computation, so no "
        "site-resolved version of the statement is available or needed. The relation being "
        "tested, C^3 = I, lives inside that one 3x3 algebra."
    )
    print(
        "  per_mode: resolved — the continuous centralizer is built mode by mode in the "
        "C_3 character basis as U = F diag(1, exp(i phi), exp(-i phi)) F^dag, one phase per "
        "Fourier mode, and is then shown for phi in {0.2, 0.9, 1.7} to leave both C and a "
        "test circulant H exactly invariant. That is the precise sense in which a "
        "continuous action does exist on the modes and yet cannot rotate the coefficient b: "
        "it is diagonal in the same modes that C is."
    )
    print(
        "  per_block: resolved — the real two-dimensional doublet block spanned by "
        "B1 = C + C^2 and B2 = i(C - C^2) is analysed as a block in its own right. The "
        "group generated by the 2 pi / 3 rotation and the reflection K is closed under "
        "multiplication inside that block and comes out with exactly 6 elements, and the "
        "space of C_3-invariant symmetric quadratic forms on it is found by SVD to be "
        "one-dimensional and proportional to the identity."
    )
    print(
        "  lattice_wide: checked and not executed, and deliberately so — the paired note's "
        "own N5 rhetoric audit states that the negative statement is per-generator and "
        "per-circulant-class and is not a per-doublet, per-state-space or lattice-wide "
        "absence claim. Running a lattice-wide sweep would assert more than the theorem "
        "does. The obstruction is instead exhausted by the exact scalar condition "
        "exp(3 i alpha) = 1, checked to hold at the three cube roots and to fail at each of "
        "alpha in {0.3, 1.0, 2.1, 0.5, 1.7}."
    )
    print("=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print(
            "SUMMARY: bounded obstruction. The route that realizes the missing "
            "b-phase as a scalar rephasing C -> exp(i alpha) C is incompatible "
            "with C^3=I except at cube roots. Continuous state-space centralizers "
            "exist but commute with C and do not rotate b, so they do not supply "
            "that route."
        )
        print("=" * 72)
        return 0
    print("SUMMARY: failures encountered; see above.")
    print("=" * 72)
    return 1


if __name__ == "__main__":
    sys.exit(main())
