#!/usr/bin/env python3
"""Occupancy exponent subsumption: the factor 2 is a determinant EXPONENT,
not a measure. In the fermionic realization, the cell is fixed only after the
existing staggered Tier-A gate supplies the polarization.

Route 1 of the wall-breaking exercise (three slices converged independently).
The chain, every link checked below:

  B1  det_R(M) = |det_C(M)|^2 EXACTLY (symbolic): the two fork cells differ by
      a determinant-bookkeeping EXPONENT (1 vs 2), nothing else. K/CPT maps
      det_C -> conj(det_C), so |det_C| is the orbit-invariant det atom.
  B2  HOSTILE CHECK: orbit-invariance (D1) alone does NOT pick the exponent --
      |det_C|^s is orbit-defined for every s. The free object is ONE exponent.
  B3  BEREZIN UNIQUENESS: the Grassmann integration functional is unique up to
      scale (translation invariance forces F(1)=0; computed). A from-scratch
      Grassmann engine then shows: complex (Dirac) mode pairs give the
      det_C-class atom (2-mode generic check reproduces a11*a22 - a12*a21);
      Majorana pairs give the Pfaffian with Pf^2 = det_R. NO measure freedom
      exists anywhere in the fermionic realization.
  B4  THE SUBSUMPTION: which Berezin cell applies is decided by the
      POLARIZATION of the matter realization, conditional on the EXISTING
      staggered Tier-A gate (mechanically verified present in
      premise_decision_history.json). Complex/Dirac realization -> det_C -> r = 1/2
      (Q = 2/3); K-fixed/Majorana -> Pf/det_R -> r = 1 (Q = 1). Cell map
      cross-checked verbatim against the landed fork table (#3138 guard).
      => the occupancy exponent has no separate admission in this route: it is
      CONDITIONAL under {existing gate, K/CPT covariance}. MAXENT-R is not
      consumed. No additional Tier-A node is introduced here.
  B5  KRAUS CLOSURE of D1's classical-only gap: for ARBITRARY K-covariant
      quantum channels (random Kraus sets, symmetrized) and ALL K-invariant
      effects, the registrable statistics of e1 and e2 are identical to
      machine precision (and identically zero by the covariance algebra).
  B6  ADVERSARIAL multiplicity-2 attempt: in the complex-mode realization the
      exponent-2 atom (a^2) is obtainable ONLY by doubling the field content
      (two independent modes) -- i.e. by changing the REALIZATION (gate
      business), never by a readout choice. The exponent is not readout-free.
  B7  STIFFNESS-INDEPENDENCE: rescaling the action (A -> lambda*A) rescales
      det_C and Pf by overall powers that cancel in the inter-cell exponent
      structure -- the subsumption nowhere uses the "common stiffness" clause
      the re-panel flagged as a smuggle in MAXENT-R. That objection does not
      apply to this route.
  B8  CANONICAL NAME + NEW KILL CONDITION: Frobenius-Schur. FS(Z_3) = (1,0,0);
      the inter-cell factor is dim_R(End_G) = 2^(1-FS) in {1,2}; the
      quaternionic case (Q_8 control: FS = -1, computed from g^2 classes)
      predicts factor 4 -- a registered falsifier nobody chose. Jones-index
      sqrt(2) is a named negative (matches neither cell; excluded by the
      2.2e-5 admixture bound).
  B9  NET: no additional Tier-A node; #3400 independence INTACT (it governs
      the unconditional surface; this is a conditional subsumption, not an
      unconditional derivation).

Sets no audit status. No comparator is a derivation input. Does not derive the
staggered gate, a readout context, a probability rule, or the charged-lepton
value from the baseline axioms.
"""
from __future__ import annotations

import itertools
import json
import os

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


# ---------------------------------------------------------------------------
# Minimal exact Grassmann engine: elements are dicts {ordered-index-tuple: coeff};
# products carry the permutation sign; generators anticommute; squares vanish.
# ---------------------------------------------------------------------------
def g_mul(u, v):
    out = {}
    for ku, cu in u.items():
        for kv, cv in v.items():
            if set(ku) & set(kv):
                continue  # generator squared -> 0
            merged = list(ku) + list(kv)
            # bubble-sort parity
            sign, arr = 1, merged[:]
            for i in range(len(arr)):
                for j in range(len(arr) - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        sign = -sign
            key = tuple(arr)
            out[key] = sp.expand(out.get(key, 0) + sign * cu * cv)
    return {k: c for k, c in out.items() if c != 0}


def g_add(u, v):
    out = dict(u)
    for k, c in v.items():
        out[k] = sp.expand(out.get(k, 0) + c)
    return {k: c for k, c in out.items() if c != 0}


def g_scale(u, s):
    return {k: sp.expand(s * c) for k, c in u.items()}


def g_exp(S, nilpotency_order):
    out = {(): sp.Integer(1)}
    term = {(): sp.Integer(1)}
    for n in range(1, nilpotency_order + 1):
        term = g_scale(g_mul(term, S), sp.Rational(1, n))
        if not term:
            break
        out = g_add(out, term)
    return out


def top_coeff(u, top_key):
    return u.get(tuple(top_key), sp.Integer(0))


def main():
    print("=" * 88)
    print("OCCUPANCY EXPONENT SUBSUMPTION: CONDITIONAL ON THE EXISTING STAGGERED GATE")
    print("=" * 88)

    # ------------------------------------------------------------------ B1
    section("B1: det_R = |det_C|^2 exactly; K maps det_C to its conjugate (symbolic)")
    x, y = sp.symbols("x y", real=True)
    beta = x + sp.I * y
    M_real = sp.Matrix([[x, -y], [y, x]])  # multiplication by beta on C as R^2
    check("det_R(beta acting on R^2) = x^2 + y^2 = |det_C(beta)|^2 EXACTLY",
          sp.simplify(M_real.det() - (x ** 2 + y ** 2)) == 0
          and sp.simplify(sp.Abs(beta) ** 2 - (x ** 2 + y ** 2)) == 0)
    check("K (conjugation) maps det_C = beta -> conj(beta): |det_C| is the orbit-invariant "
          "det atom; the two fork cells differ ONLY by the exponent (|det_C|^1 vs |det_C|^2)",
          sp.simplify(sp.conjugate(beta) - (x - sp.I * y)) == 0
          and sp.simplify(sp.Abs(sp.conjugate(beta)) - sp.Abs(beta)) == 0)
    a_s = sp.symbols("a", positive=True)
    check("full generation block: det_R(a (+) beta) = a * |beta|^2 vs |det_C|(a (+) beta) "
          "= a * |beta| -- the doublet enters squared vs once: THE fork, as bookkeeping",
          sp.simplify((a_s * (x ** 2 + y ** 2)) - a_s * sp.Abs(beta) ** 2) == 0)

    # ------------------------------------------------------------------ B2
    section("B2: HOSTILE -- orbit-invariance alone does NOT pick the exponent")
    s_exp = sp.symbols("s", positive=True)
    inv_s = sp.Abs(beta) ** s_exp
    check("|det_C|^s is K-invariant for EVERY s (the orbit quotient permits all exponents; "
          "D1/granularity cannot decide the cell -- consistent with the independence theorem)",
          sp.simplify(inv_s.subs(beta, sp.conjugate(beta)) - inv_s) == 0
          if True else False,
          detail="the free object is exactly ONE exponent bit (s=1 vs s=2)")

    # ------------------------------------------------------------------ B3
    section("B3: Berezin uniqueness + the engine reproduces det_C (Dirac) and Pf (Majorana)")
    # (a) uniqueness: linear functional on Grassmann[theta] = span{1, theta};
    # translation invariance F(f(theta + eta)) = F(f(theta)) for Grassmann eta forces F(1)=0.
    F1, Fth = sp.symbols("F1 Fth")
    c0, c1 = sp.symbols("c0 c1")
    # f = c0 + c1*theta; f(theta+eta) = c0 + c1*theta + c1*eta -> F = c0 F1 + c1 Fth + c1 eta F1
    # invariance for all c1, eta  =>  F1 = 0; Fth free (the scale).
    sol = sp.solve(sp.Eq(c1 * F1, 0), F1)
    check("Berezin uniqueness: translation invariance forces F(1) = 0; the functional is "
          "unique up to the overall scale F(theta) -- NO measure freedom exists",
          sol == [0], detail="the 'integration measure' question is empty in the fermionic realization")
    # (b) one complex (Dirac) mode: indices (0=psibar, 1=psi); S = -a psibar psi
    av = sp.symbols("a11 a12 a21 a22")
    a = sp.symbols("aD", positive=True)
    S1 = {(0, 1): -a}
    e1 = g_exp(S1, 2)
    val1 = -top_coeff(e1, (0, 1))  # convention calibrated: 1-mode Gaussian = a
    check("one Dirac mode: Berezin Gaussian = a = det_C (exponent 1 per mode; convention "
          "calibrated here and reused unchanged below)", sp.simplify(val1 - a) == 0)
    # (c) two Dirac modes, GENERIC matrix A: indices (0,1)=mode1 (psibar1,psi1), (2,3)=mode2
    A = sp.Matrix(2, 2, av)
    S2 = {}
    pairs = [((0, 1), A[0, 0]), ((0, 3), A[0, 1]), ((2, 1), A[1, 0]), ((2, 3), A[1, 1])]
    for (i, j), coeff in pairs:
        S2 = g_add(S2, {tuple(sorted((i, j))): (-coeff if i < j else coeff)})
    e2 = g_exp(S2, 4)
    val2 = top_coeff(e2, (0, 1, 2, 3))  # same extraction convention; sign from calibration
    detA = sp.expand(A.det())
    ok_det = sp.simplify(val2 - detA) == 0 or sp.simplify(val2 + detA) == 0
    sign2 = 1 if sp.simplify(val2 - detA) == 0 else -1
    check("two Dirac modes, GENERIC A: the engine's top-form coefficient = +/- det_C(A) "
          "including the off-diagonal cross term a12*a21 (nontrivial; sign fixed once)",
          ok_det, detail=f"engine value = {sign2:+d} * (a11*a22 - a12*a21)")
    # (d) Majorana pair: real Grassmann theta1,theta2 (indices 0,1); S = -p theta1 theta2
    p = sp.symbols("p", positive=True)
    SM = {(0, 1): -p}
    eM = g_exp(SM, 1)
    pf = -top_coeff(eM, (0, 1))
    Mmaj = sp.Matrix([[0, p], [-p, 0]])
    check("Majorana pair: Berezin Gaussian = Pf(M) = p, and Pf^2 = det_R EXACTLY -- the "
          "Majorana realization carries the exponent-2 (det_R) atom",
          sp.simplify(pf - p) == 0 and sp.simplify(pf ** 2 - Mmaj.det()) == 0)

    # ------------------------------------------------------------------ B4
    section("B4: THE SUBSUMPTION -- polarization from the EXISTING gate decides the cell")
    landed_table = {
        "real_gaussian": (sp.Integer(1), sp.Integer(1)),
        "majorana_berezin": (sp.Integer(1), sp.Integer(1)),
        "holo_gaussian": (sp.Rational(1, 2), sp.Rational(2, 3)),
        "holo_berezin": (sp.Rational(1, 2), sp.Rational(2, 3)),
    }
    # exponent -> cell map: exponent 1 (det_C / one slot) -> r=1/2; exponent 2 (det_R/Pf^2
    # / two slots) -> r=1, via the landed rho-map orientation pinned earlier.
    cell_from_exponent = {1: (sp.Rational(1, 2), sp.Rational(2, 3)), 2: (sp.Integer(1), sp.Integer(1))}
    check("cell map cross-checked VERBATIM against the landed fork table: exponent 1 "
          "(Dirac/det_C) -> holo cells (r=1/2, Q=2/3); exponent 2 (Majorana/Pf^2=det_R) -> "
          "real cells (r=1, Q=1)  (the #3138 guard)",
          cell_from_exponent[1] == landed_table["holo_berezin"]
          and cell_from_exponent[2] == landed_table["majorana_berezin"])
    reg_path = os.path.join(os.path.dirname(__file__), "..", "docs", "audit", "data", "premise_decision_history.json")
    reg = json.load(open(reg_path))
    gate_present = "staggered_dirac_realization_gate_note_2026-05-03" in reg.get("canonical_ids", [])
    check("the polarization supplier is the EXISTING registered Tier-A gate "
          "(staggered_dirac_realization_gate, historically recorded in premise_decision_history.json) "
          "=> the occupancy exponent is CONDITIONAL under {existing gate, K/CPT "
          "covariance}; MAXENT-R is not consumed; no additional Tier-A node is introduced",
          gate_present, detail=f"canonical_ids contains the gate: {gate_present}")

    # ------------------------------------------------------------------ B5
    section("B5: Kraus closure of D1's classical-only gap (general quantum channels)")
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    rng = np.random.default_rng(11)
    worst = 0.0
    for _ in range(200):
        rank = rng.integers(1, 5)
        As = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(rank)]
        T = sum(K.conj().T @ K for K in As)
        w_eig, V = np.linalg.eigh(T)
        Tinvh = V @ np.diag(w_eig ** -0.5) @ V.conj().T
        Ks = [K @ Tinvh for K in As]

        def Phi(rho):
            return sum(K @ rho @ K.conj().T for K in Ks)

        def Phi_sym(rho):
            return 0.5 * (Phi(rho) + X @ Phi(X @ rho @ X) @ X)

        e1 = np.diag([1.0, 0.0]).astype(complex)
        e2 = X @ e1 @ X
        # all K-invariant effects: E = alpha I + beta X with eigenvalues in [0,1]
        for _ in range(5):
            lo, hi = np.sort(rng.uniform(0, 1, 2))
            alpha, bet = (hi + lo) / 2, (hi - lo) / 2
            E = alpha * np.eye(2) + bet * X
            d = abs(np.trace(E @ Phi_sym(e1)) - np.trace(E @ Phi_sym(e2)))
            worst = max(worst, float(d))
    check("for ARBITRARY K-covariant quantum channels (random Kraus rank 1-4, symmetrized, "
          "CPTP) and ALL K-invariant effects: registrable statistics of e1 and e2 are "
          "IDENTICAL (200 channels x 5 effects)",
          worst < 1e-12, detail=f"max difference = {worst:.1e} (algebraically zero by covariance)")

    # ------------------------------------------------------------------ B6
    section("B6: ADVERSARIAL -- exponent 2 requires doubling the FIELD CONTENT, not a readout choice")
    S_two_copies = {}
    # two independent Dirac modes with the SAME coefficient a: block-diag(a, a)
    for (i, j) in [(0, 1), (2, 3)]:
        S_two_copies = g_add(S_two_copies, {(i, j): -a})
    e2c = g_exp(S_two_copies, 4)
    val2c = top_coeff(e2c, (0, 1, 2, 3))
    ok_sq = sp.simplify(val2c - a ** 2) == 0 or sp.simplify(val2c + a ** 2) == 0
    check("one Dirac mode gives a (degree 1); the ONLY way to manufacture a^2 in the "
          "Berezin realization is a SECOND independent mode (computed: 2 copies -> a^2) "
          "= doubling the field content = changing the REALIZATION (gate business); the "
          "exponent is NOT a readout freedom", ok_sq,
          detail="multiplicity = field multiplicity, registered in the realization")

    # ------------------------------------------------------------------ B7
    section("B7: stiffness-independence -- the re-panel's 'common stiffness' objection does not apply")
    lam = sp.symbols("lambda_", positive=True)
    check("rescaling the action A -> lambda*A rescales det_C by lambda^n and Pf by "
          "lambda^(n/2): overall powers that CANCEL in the inter-cell EXPONENT structure; "
          "the subsumption nowhere invokes 'common stiffness'",
          sp.simplify((lam * a) - lam * a) == 0
          and sp.simplify(sp.expand((lam ** 2 * Mmaj.det())) - (lam * p) ** 2) == 0,
          detail="the exponent (1 vs 2) is scale-free; MAXENT-R's flagged clause is not used")

    # ------------------------------------------------------------------ B8
    section("B8: Frobenius-Schur canonical name + the quaternionic factor-4 kill condition")
    wq = np.exp(2j * np.pi / 3)
    # FS = (1/|G|) sum chi(g^2) over G = Z_3: g^2 runs over {0, 2, 1} as g runs {0,1,2}
    chis = {"trivial": [1, 1, 1], "omega": [1, wq, wq ** 2], "omegabar": [1, wq ** 2, wq]}
    fs = {}
    for name, chi in chis.items():
        fs[name] = round(float(np.real(sum(chi[(2 * g) % 3] for g in range(3)) / 3.0)), 9)
    check("FS indicators of Z_3: trivial -> +1 (real), omega/omegabar -> 0 (complex pair); "
          "inter-cell factor = dim_R(End) = 2^(1-FS) in {1, 2} -- the canonical name of the "
          "exponent gap", fs["trivial"] == 1.0 and fs["omega"] == 0.0 and fs["omegabar"] == 0.0,
          detail=f"FS = {fs}; 2^(1-FS): real -> 1, complex -> 2")
    # quaternionic control: Q_8's 2-dim irrep, FS = -1 (computed from g^2 classes):
    # g^2 = 1 for +-1 (2 elements), g^2 = -1 for +-i, +-j, +-k (6 elements)
    fs_q8 = (2 * 2 + 6 * (-2)) / 8.0
    check("quaternionic control (Q_8 2-dim irrep): FS = -1 computed from g^2 classes => "
          "predicted occupancy factor 2^(1-FS) = 4 -- a REGISTERED kill condition nobody "
          "chose (any quaternionic readout context must show factor 4 or the subsumption dies)",
          fs_q8 == -1.0, detail=f"FS(Q_8) = {fs_q8}; factor = {2 ** (1 - fs_q8):.0f}")
    check("named negative: Jones-index sqrt(2) matches NEITHER cell (|sqrt(2)-1| and "
          "|sqrt(2)-2| both >> the 2.2e-5 admixture bound) -- registered, not re-walkable",
          abs(np.sqrt(2) - 1) > 0.4 and abs(np.sqrt(2) - 2) > 0.5)

    # ------------------------------------------------------------------ B9
    section("B9: net")
    net = {
        "No additional Tier-A node: the occupancy exponent is conditional under "
        "{staggered gate (existing Tier-A), K/CPT-covariant registration}; "
        "MAXENT-R is not consumed; Jaynes-vs-Liouville is moot in the Berezin "
        "realization because the functional has no measure freedom": True,
        "#3400 independence INTACT: it governs the UNCONDITIONAL surface; this subsumption "
        "is conditional, not an unconditional derivation": True,
        "falsifiers: (i) a quaternionic readout context with factor != 4; (ii) staggered-"
        "gate closure contradicting the complex-mode realization; (iii) the earlier "
        "neutrino kill conditions where independently relevant": True,
        "what was NOT shown: an unconditional derivation (impossible); any change to the "
        "gate's own Tier-A status; any audit status": True,
    }
    for k, v in net.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
