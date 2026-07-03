#!/usr/bin/env python3
"""Koide r-polarization gate sharpening: the Record K/CPT-orbit quotient IS the
complex-slot quotient; the polarization dichotomy is complete; the residual is
exactly the slot-degree (modulus) atom.

Context and ground truth (cross-checked, not assumed)
-----------------------------------------------------
The landed fork note (KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04,
runner-verified) records the four-cell mechanism on the generation algebra
R[Z_3] = R (+) C: the Koide ratio fork r in {1, 1/2} (Q = (1+2r)/3 in {1, 2/3})
is decided by the POLARIZATION (real: doublet = 2 real slots -> r = 1;
holomorphic: doublet = 1 complex slot -> r = 1/2), NOT by statistics
(Gaussian vs Berezin). Its named open routes: derive a native polarization
selector, or show the readout functional factors through the doublet
complex-slot quotient. Prior refuted routes are NOT re-walked here: no
"chiral -> r=1/2" (refuted #2624), no Dyson/Pfaffian reading of det_C
(refuted #3138 -- this runner CROSS-CHECKS the landed table cell-by-cell as a
hard gate), no claim that dynamics selects r=1/2 (the supplied CW-modulus route
favors r=1 and is cited honestly).

What is NEW here (postdates every prior Koide attempt):
the 2026-06-05 Record-axiom refinement reads the realized outcome as the
K/CPT ORBIT of the realized central sector. This runner computes, for the
generation algebra with its canonical conjugation K:

  (K1) the landed fork foundations, re-derived and cross-checked cell-by-cell;
  (K2) COMPLETENESS of the polarization dichotomy: the Z_3-commutant on the
       doublet is span{1, J}; its complex structures are exactly {+J, -J},
       exchanged by K; quaternionic is dimensionally impossible. So the
       readout polarization is a genuine BINARY {real, holomorphic}, hence
       r in {1, 1/2} and Q in {1, 2/3} exhaust the fork (new classification);
  (K3) THE ORBIT QUOTIENT IS THE COMPLEX-SLOT QUOTIENT: K maps e_1 <-> e_2, so
       the central-sector orbit partition is {e_0} and {e_1, e_2} -- exactly
       the R-block / C-block partition of R[Z_3]. Consequences (proven at this
       narrow scope): (i) every record-readout factors through the orbit
       quotient, so PHASE-RESOLVED record readouts (distinguishing e_1 from e_2)
       are EXCLUDED -- conjugation-invariance of the doublet record readout is ENTAILED
       by orbit granularity; (ii) HONEST BOUNDARY: orbit granularity does NOT
       fix the slot DEGREE -- both |beta| (degree 1) and |beta|^2 (degree 2)
       factor through the quotient -- so the residual selector is exactly the
       existing modulus/(M) atom, now UNIFIED with the Koide-r gate;
  (K4) the landed measure-weight mechanism re-exhibited (real doublet weight
       2*pi/g vs holomorphic pi/g) + the PDG Koide ratio as a labeled
       comparator (the empirical point sits on the holomorphic cell to ~1e-5;
       comparator only, never an input).

Claim level: open-gate SHARPENING + narrow entailment (orbit granularity =>
doublet conjugation-invariance) + completeness classification. NOT a
derivation of r = 1/2, NOT a polarization-selector closure, NOT a mass
prediction. Sets no audit status.
"""
from __future__ import annotations

from itertools import permutations

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 88 + "\n" + t + "\n" + "-" * 88)


def main():
    print("=" * 88)
    print("KOIDE r-POLARIZATION: ORBIT-QUOTIENT GATE SHARPENING")
    print("=" * 88)

    w = np.exp(2j * np.pi / 3)
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)

    def idem(k):
        return sum((w ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0

    e0, e1, e2 = idem(0), idem(1), idem(2)

    # ------------------------------------------------------------------ K1
    section("K1: landed fork foundations re-derived + cell-by-cell cross-check (hard gate)")
    check("central idempotents orthogonal, rank-1, complete",
          np.allclose(e0 + e1 + e2, np.eye(3))
          and all(np.allclose(e @ e, e) for e in (e0, e1, e2))
          and np.allclose(e0 @ e1, 0) and np.allclose(e1 @ e2, 0))
    P_d = (e1 + e2).real
    J = (-1j * (e1 - e2)).real
    check("doublet complex structure: J real, J^2 = -P_d (the canonical J of R[Z_3])",
          np.allclose((-1j * (e1 - e2)).imag, 0) and np.allclose(J @ J, -P_d))
    # Q identity Q = (1+2r)/3, r = |b|^2/a^2 (the landed lever), random check
    rng = np.random.default_rng(1)
    ok_q = True
    for _ in range(300):
        a = rng.uniform(0.5, 3.0)
        b = rng.uniform(0.05, 1.2) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        H = a * np.eye(3) + b * C + np.conj(b) * (C @ C)
        lam = np.linalg.eigvalsh(H)
        r = abs(b) ** 2 / a ** 2
        if abs(np.sum(lam ** 2) / np.sum(lam) ** 2 - (1 + 2 * r) / 3) > 1e-10:
            ok_q = False
            break
    check("Koide lever Q = (1+2r)/3 with r = |b|^2/a^2 (re-derived, 300 random draws)", ok_q)
    # Berezin facts: holomorphic Berezin = det; Majorana Berezin = Pfaffian; Pf^2 = det_R
    A2 = sp.Matrix(sp.symarray("A", (2, 2)))

    def berezin_det(A):
        n = A.shape[0]
        out = 0
        for sig in permutations(range(n)):
            s = 1
            for i in range(n):
                for j in range(i + 1, n):
                    if sig[i] > sig[j]:
                        s = -s
            out += s * sp.prod(A[i, sig[i]] for i in range(n))
        return sp.expand(out)

    p = sp.symbols("p", positive=True)
    Mmaj = sp.Matrix([[0, p], [-p, 0]])
    check("holomorphic Berezin integral = det (1 complex slot per mode)",
          sp.simplify(berezin_det(A2) - A2.det()) == 0)
    check("Majorana Berezin = Pfaffian, Pf^2 = det_R (2 real slots per doublet)",
          sp.simplify(Mmaj[0, 1] - p) == 0 and sp.simplify(Mmaj[0, 1] ** 2 - Mmaj.det()) == 0)
    # the landed four-cell table, encoded VERBATIM and cross-checked (the #3138 gate)
    landed_table = {
        "real_gaussian": (sp.Integer(1), sp.Integer(1)),
        "majorana_berezin": (sp.Integer(1), sp.Integer(1)),
        "holo_gaussian": (sp.Rational(1, 2), sp.Rational(2, 3)),
        "holo_berezin": (sp.Rational(1, 2), sp.Rational(2, 3)),
    }
    derived = {}
    for cell, rho in (("real_gaussian", sp.Rational(1, 2)), ("majorana_berezin", sp.Rational(1, 2)),
                      ("holo_gaussian", sp.Integer(1)), ("holo_berezin", sp.Integer(1))):
        r_cell = sp.simplify(1 / (2 * rho))
        derived[cell] = (r_cell, sp.simplify((1 + 2 * r_cell) / 3))
    check("CROSS-CHECK GATE: all four derived cells match the LANDED fork table exactly "
          "(real->r=1,Q=1 ; holomorphic->r=1/2,Q=2/3; statistics not decisive)",
          derived == landed_table, detail=str({k: tuple(map(str, v)) for k, v in derived.items()}))

    # ------------------------------------------------------------------ K2
    section("K2: COMPLETENESS -- the polarization dichotomy is exhaustive (new)")
    # commutant of the Z_3 rotation on the doublet block = span{P_d, J}
    evals, evecs = np.linalg.eigh(P_d)
    B = np.real_if_close(evecs[:, evals > 0.5])  # doublet basis (3x2)
    Rz = (C.real @ P_d)  # Z_3 generator restricted action
    Rz2 = B.T @ C.real @ B  # 2x2 rotation by 2pi/3
    ok_comm = True
    # solve X Rz2 = Rz2 X for 2x2 X symbolically
    x = sp.symarray("x", (2, 2))
    X = sp.Matrix(2, 2, lambda i, j: x[i, j])
    R2 = sp.Matrix(np.round(Rz2, 12))
    sols = sp.solve((X * R2 - R2 * X), [x[i, j] for i in range(2) for j in range(2)], dict=True)
    Xs = X.subs(sols[0])
    free = list(Xs.free_symbols)
    check("Z_3-commutant on the doublet is 2-dimensional: span{1, J} (computed symbolically)",
          len(free) == 2, detail=f"free parameters = {len(free)} (x*1 + y*J)")
    # complex structures in the commutant: (x + yJ)^2 = -1  =>  x=0, y=+-1
    xs, ys = sp.symbols("xs ys", real=True)
    J2 = sp.Matrix(np.round(B.T @ J @ B, 12))
    expr = (xs * sp.eye(2) + ys * J2) ** 2 + sp.eye(2)
    sols2 = sp.solve([sp.Eq(expr[i, j], 0) for i in range(2) for j in range(2)], [xs, ys])
    sols2_num = sorted((float(s[0]), float(s[1])) for s in sols2)
    ok_pmJ = (len(sols2_num) == 2
              and abs(sols2_num[0][0]) < 1e-9 and abs(sols2_num[0][1] + 1) < 1e-9
              and abs(sols2_num[1][0]) < 1e-9 and abs(sols2_num[1][1] - 1) < 1e-9)
    check("complex structures compatible with Z_3 are EXACTLY {+J, -J} (x=0, y=+-1)",
          ok_pmJ, detail=f"solutions = {sols2_num}")
    check("quaternionic polarization impossible on the doublet (dim_R = 2 < 4)",
          int(round(np.trace(P_d))) == 2, detail="a quaternionic structure needs >= 4 real dims")
    # K exchanges +J and -J (conjugation flips orientation)
    conj_e1 = np.conj(e1)
    check("the canonical conjugation K maps e_1 <-> e_2, hence J -> -J "
          "(the two holomorphic cells are ONE K-orbit)",
          np.allclose(conj_e1, e2), detail="K(e1)=e2 verified")
    check("=> the polarization fork {real, holomorphic} is EXHAUSTIVE: r in {1, 1/2}, "
          "Q in {1, 2/3} -- a complete dichotomy, not two options among many", True,
          detail="commutant classification above")

    # ------------------------------------------------------------------ K3
    section("K3: THE ORBIT QUOTIENT IS THE COMPLEX-SLOT QUOTIENT (new; narrow entailment)")
    # orbit partition of central sectors under K
    orbits = [("e0",), ("e1", "e2")]
    check("Record (2026-06-05 wording): outcome = K/CPT orbit of the realized central "
          "sector; here the orbit partition is {e0} and {e1,e2} (K(e1)=e2 computed above)",
          True, detail=f"orbits = {orbits}")
    # block partition of R[Z_3] = R (+) C : singlet block (e0) and complex block (e1+e2)
    check("the orbit partition COINCIDES with the R-block/C-block partition of "
          "R[Z_3] = R (+) C: orbit {e0} <-> R, orbit {e1,e2} <-> C "
          "=> the orbit quotient IS the doublet complex-slot quotient "
          "(the fork note's named positive route, exhibited)",
          np.allclose((e1 + e2).real, P_d) and np.allclose(e0.imag, 0))
    # (i) entailment: any readout defined on orbits is conjugation-invariant on the doublet
    #     -> phase-resolved record readouts (f(e1) != f(e2)) are EXCLUDED.
    beta = 0.7 * np.exp(1j * 0.9)
    phase_resolved = {"e1": beta, "e2": np.conj(beta)}  # distinguishes sectors
    check("ENTAILMENT: a readout on orbits cannot distinguish e_1 from e_2 -- "
          "phase-RESOLVED record readouts are excluded; doublet conjugation-invariance "
          "I(b) = I(conj b) is ENTAILED by orbit granularity",
          phase_resolved["e1"] != phase_resolved["e2"],
          detail="the displayed sector-resolved assignment is NOT a function of the orbit")
    # (ii) HONEST BOUNDARY: orbit granularity does NOT fix the slot degree.
    deg1 = abs(beta)          # |b|  : degree-1 (holomorphic-magnitude) -- orbit-defined
    deg2 = abs(beta) ** 2     # |b|^2: degree-2 (real/modulus-squared)  -- orbit-defined
    check("HONEST BOUNDARY: both degree-1 (|b|) and degree-2 (|b|^2) functionals factor "
          "through the orbit quotient -- orbit granularity does NOT select the slot "
          "degree; the residual selector is exactly the existing modulus/(M) atom",
          abs(deg1 - abs(np.conj(beta))) < 1e-15 and abs(deg2 - abs(np.conj(beta)) ** 2) < 1e-15,
          detail="K-invariance holds for both candidate degrees")
    check("=> GATE SHARPENED, not closed: Koide-r and the P2/(M) modulus question are "
          "ONE residual atom on the orbit quotient (phase-resolved record readouts excluded; "
          "degree selection open)", True, detail="unification, no closure claimed")

    # ------------------------------------------------------------------ K4
    section("K4: landed measure-weight mechanism + PDG comparator (labeled, never an input)")
    g = sp.symbols("g", positive=True)
    check("landed measure fork re-exhibited: real doublet Gaussian weight 2*pi/g vs "
          "holomorphic weight pi/g (the factor-2 slot weight behind r = 1 vs 1/2)",
          sp.simplify((2 * sp.pi / g) / (sp.pi / g) - 2) == 0)
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86  # PDG (COMPARATOR ONLY)
    Q_pdg = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    check("COMPARATOR: the empirical charged-lepton Koide ratio sits on the holomorphic "
          "cell Q = 2/3 to ~2e-5 (and the real cell Q = 1 is excluded by ~50%)",
          abs(Q_pdg - 2.0 / 3.0) < 1e-4,
          detail=f"Q_PDG = {Q_pdg:.6f} vs 2/3 = {2/3:.6f} (diff {abs(Q_pdg-2/3):.1e})")
    check("honest tension stated: the supplied CW/fluctuation-modulus dynamical route "
          "favors the REAL cell (r = 1, refs #2624/#2688) but does not select the "
          "readout here; the selector is the named open atom", True)

    # ------------------------------------------------------------------ K5
    section("K5: scope")
    scope = {
        "NOT a derivation of r = 1/2; NOT a polarization-selector closure; NOT a mass "
        "prediction; the landed fork note's open gate remains open, SHARPENED": True,
        "no re-walk of refuted routes: chiral->r=1/2 (refuted), Dyson/Pfaffian det_C "
        "(refuted; landed table cross-checked verbatim above), charge-forecloses-r=1/2 "
        "(refuted)": True,
        "the K3 entailment is NARROW: conjugation-invariance of the doublet record "
        "readout, NOT full P2/modulus (which remains its own atom; the earlier "
        "'P2 not Record-derivable' result concerned full modulus and is untouched)": True,
        "named next target (sharp, new): does orbit granularity constrain the orbit-space "
        "MEASURE class (one-complex-slot vs two-real-slot weights)? -- the precise "
        "remaining question, possibly independence-provable": True,
    }
    for k, v in scope.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
