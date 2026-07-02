#!/usr/bin/env python3
"""Product-grading eta sector selection bridge (signed-gravity, eta-half).

Companion runner for
docs/SIGNED_GRAVITY_PRODUCT_GRADING_ETA_SECTOR_SELECTION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md

Verifies, in exact finite dimensions:

  [R]  the real Majorana Cl(3,1) representation (retained extension's
       epsilon = -1 cell): generator squares, all anticommutators,
       gamma_5^2 = -I, gamma_5 skew, eps = i gamma_5 a Hermitian
       involution with tr(eps) = 0.
  [T1] sector swap carries orientation reversal:
       e4 eps e4^{-1} = -eps  and  e4 (e1 e2 e3) e4^{-1} = -(e1 e2 e3).
  [T2] sector selection: the boundary block I (x) A(a) (x) eps
       restricted to the eps = +/-1 sectors carries +/-A(a); opposite
       counting asymmetries eta = +/-2; labels chi_{+/-} = +/-1; the
       orientation-image eta flip on a random unitary conjugate.
  [T3] quantized label table on the spectrally-truncated twisted tower
       for the exact half-integer cutoff family Lambda in Z>=0+1/2,
       with the proposal's branch conditions (gap failure at a = 0;
       eta = 0 at a = 1/2; chi = -1 on (1/2, 1)), the exact floor
       formula and the equivalent generic Lambda=m+r formula
       eta=1_{r>=a}-1_{r>=1-a}, plus explicit non-half-integer
       counterexample cutoffs.
  [T4] coexistence: D_tot Hermitian; [D_gen, C3] = 0; {D_gen-part,
       Gamma_prod} = 0; [D_bdy-part, Gamma_prod] = 0; [N, eps] = 0;
       {e4, eps} = 0; {e1, eps} = 0.
  [F]  falsifiers: full-anticommuting grading forces eta = 0; index
       truncation manufactures a spurious label at a = 1/2; untwisted
       a = 0 yields no label (bulk-vanishing consistency).

Deterministic, numpy only, runtime seconds.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""

from __future__ import annotations

import sys

import numpy as np

PASS = 0
FAIL = 0
DELTA = 1e-8


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        s = "PASS"
    else:
        FAIL += 1
        s = "FAIL"
    print(f"  [{s}] [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 76)
    print(title)
    print("-" * 76)


def eta_h(lam: np.ndarray, delta: float = DELTA) -> tuple[int, int]:
    """Counting spectral asymmetry and zero-window count (repo convention)."""
    eta = int(np.sum(lam > delta) - np.sum(lam < -delta))
    h = int(np.sum(np.abs(lam) <= delta))
    return eta, h


def tower_spectral(a: float, lam_max: float) -> np.ndarray:
    """Twisted tower {n + a} with SPECTRAL truncation |n + a| <= lam_max."""
    n = np.arange(-int(lam_max + 2), int(lam_max + 2) + 1)
    lam = n + a
    return lam[np.abs(lam) <= lam_max]


def eta_formula_positive(a: float, lam_max: float) -> int:
    """Closed-form eta for a in (0, 1/2) on the spectral cutoff."""
    return int(np.floor(lam_max - a) + 1 - np.floor(lam_max + a))


def frac_part(x: float) -> float:
    return float(x - np.floor(x))


def eta_formula_positive_twist(a: float, lam_max: float) -> int:
    """Exact eta for 0 < a < 1/2 and Lambda=m+r."""
    r = frac_part(lam_max)
    return int(r + 1.0e-12 >= a) - int(r + 1.0e-12 >= 1.0 - a)


def label(lam: np.ndarray) -> str:
    e, h = eta_h(lam)
    if h > 0:
        return "UNDEF(gap)"
    if e == 0:
        return "UNDEF(eta=0)"
    return "+1" if e > 0 else "-1"


def main() -> int:
    print("=" * 76)
    print("PRODUCT-GRADING ETA SECTOR SELECTION BRIDGE (signed-gravity, eta-half)")
    print("the [+1, -1] source labels derived from the retained Cl(3,1) grading")
    print("plus ONE twist datum -- no sign axiom")
    print("=" * 76)

    # =======================================================================
    section("[R] real Majorana Cl(3,1) representation (retained extension)")
    # =======================================================================
    s1 = np.array([[0.0, 1.0], [1.0, 0.0]])
    s3 = np.diag([1.0, -1.0])
    is2 = np.array([[0.0, 1.0], [-1.0, 0.0]])
    I2 = np.eye(2)
    e1 = np.kron(s1, s1)
    e2 = np.kron(s1, s3)
    e3 = np.kron(s3, I2)
    e4 = np.kron(is2, I2)
    gens = [e1, e2, e3, e4]
    sq_ok = all(np.allclose(g @ g, s * np.eye(4))
                for g, s in zip(gens, (1, 1, 1, -1)))
    check("R", "generator squares: e_i^2 = +I (i<=3), e_4^2 = -I", sq_ok)
    anti_ok = all(np.allclose(gens[i] @ gens[j] + gens[j] @ gens[i], 0)
                  for i in range(4) for j in range(i + 1, 4))
    check("R", "all generator pairs anticommute", anti_ok)
    check("R", "representation is real (Majorana cell of the retained "
               "Cl(3)->Cl(3,1) extension)",
          all(np.isrealobj(g) for g in gens))
    g5 = e1 @ e2 @ e3 @ e4
    check("R", "gamma_5^2 = -I (real Cl(3,1) volume element)",
          np.allclose(g5 @ g5, -np.eye(4)))
    check("R", "gamma_5 skew (orthogonal with square -I)",
          np.allclose(g5.T, -g5))
    eps = 1j * g5
    check("R", "eps = i gamma_5: Hermitian involution with tr(eps) = 0",
          np.allclose(eps @ eps, np.eye(4))
          and np.allclose(eps.conj().T, eps)
          and abs(np.trace(eps)) < 1e-12)

    # =======================================================================
    section("[T1] sector swap carries orientation reversal (retained algebra)")
    # =======================================================================
    e4inv = -e4  # e4^2 = -I
    check("T1", "e_4 eps e_4^{-1} = -eps (the eps-sectors are exchanged by "
                "the retained odd generator)",
          np.allclose(e4 @ eps @ e4inv, -eps))
    vol3 = e1 @ e2 @ e3
    check("T1", "e_4 (e1 e2 e3) e_4^{-1} = -(e1 e2 e3) (the exchange "
                "reverses the boundary volume element)",
          np.allclose(e4 @ vol3 @ e4inv, -vol3))

    # =======================================================================
    section("[T2] sector selection derives the opposite label pair")
    # =======================================================================
    a, lam_max = 0.3, 20.5
    tow = tower_spectral(a, lam_max)
    NY = len(tow)
    Aa = np.diag(tow.astype(complex))
    bdy = np.kron(Aa, eps)  # boundary block on H_Y (x) S
    Gam_S = eps             # grading on the spinor slot
    check("T2", "boundary block commutes with the grading "
                "(sector selection, not mirror)",
          np.allclose(bdy @ np.kron(np.eye(NY), Gam_S)
                      - np.kron(np.eye(NY), Gam_S) @ bdy, 0))
    w, V = np.linalg.eigh(eps)
    Pp = V[:, w > 0.5]
    Pm = V[:, w < -0.5]
    blk_p = np.kron(np.eye(NY), Pp).conj().T @ bdy @ np.kron(np.eye(NY), Pp)
    blk_m = np.kron(np.eye(NY), Pm).conj().T @ bdy @ np.kron(np.eye(NY), Pm)
    lam_p = np.linalg.eigvalsh(blk_p)
    lam_m = np.linalg.eigvalsh(blk_m)
    ep_, hp_ = eta_h(lam_p)
    em_, hm_ = eta_h(lam_m)
    check("T2", "eps = +1 sector carries +A(a): eta = +2, h = 0",
          ep_ == 2 and hp_ == 0, f"eta_+ = {ep_:+d}")
    check("T2", "eps = -1 sector carries -A(a): eta = -2, h = 0",
          em_ == -2 and hm_ == 0, f"eta_- = {em_:+d}")
    check("T2", "derived label pair (chi_+, chi_-) = (+1, -1) from ONE "
                "twist datum",
          np.sign(ep_) == 1 and np.sign(em_) == -1)
    rng = np.random.default_rng(7)
    U = np.linalg.qr(rng.standard_normal((NY, NY)))[0]
    lam_img = np.linalg.eigvalsh(-U @ np.diag(tow) @ U.T)
    e_img, _ = eta_h(lam_img)
    e_orig, _ = eta_h(tow)
    check("T2", "orientation image: eta(-U A U^dag) = -eta(A) exactly",
          e_img == -e_orig, f"{e_orig:+d} -> {e_img:+d}")

    # =======================================================================
    section("[T3] half-integer-cutoff labels + the proposal's branch conditions")
    # =======================================================================
    table = {0.0: "UNDEF(gap)", 0.1: "+1", 0.3: "+1", 0.49: "+1",
             0.5: "UNDEF(eta=0)", 0.7: "-1", 0.9: "-1",
             -0.1: "-1", -0.3: "-1"}
    ok_all = True
    for aa, expect in table.items():
        got = label(tower_spectral(aa, lam_max))
        if got != expect:
            ok_all = False
            print(f"    MISMATCH a={aa}: got {got}, expect {expect}")
    check("T3", "label table over a in {0, +/-0.1, +/-0.3, 0.49, 0.5, "
                "0.7, 0.9} at Lambda = 20.5 matches exactly (chi "
                "quantized; branch conditions fail exactly at a = 0 "
                "and a = 1/2)", ok_all)
    e0, h0 = eta_h(tower_spectral(0.0, lam_max))
    check("T3", "a = 0 (untwisted): h_delta = 1, label undefined "
                "(gap branch condition fails)", h0 == 1)
    e5, h5 = eta_h(tower_spectral(0.5, lam_max))
    check("T3", "a = 1/2: spectrum reflection-symmetric, eta_delta = 0, "
                "label undefined", e5 == 0 and h5 == 0)
    formula_ok = True
    for LL in (0.5, 1.5, 2.5, 20.5, 20.25, 20.75):
        for aa in (0.1, 0.3, 0.49):
            e_direct, _ = eta_h(tower_spectral(aa, LL))
            floor_formula = eta_formula_positive(aa, LL)
            indicator_formula = eta_formula_positive_twist(aa, LL)
            if e_direct != floor_formula or floor_formula != indicator_formula:
                formula_ok = False
                print(f"    FLOOR MISMATCH Lambda={LL}, a={aa}: "
                      f"direct={e_direct}, floor={floor_formula}, "
                      f"indicator={indicator_formula}")
    check("T3", "closed floor/fractional formula for eta matches direct "
                "spectral counts on tested cutoffs",
          formula_ok)
    half_integer_ok = True
    for LL in (0.5, 1.5, 2.5, 7.5, 20.5):
        for aa in (0.1, 0.25, 0.49):
            ep, hp = eta_h(tower_spectral(aa, LL))
            en, hn = eta_h(tower_spectral(-aa, LL))
            half_integer_ok = half_integer_ok and ep == 1 and hp == 0 and en == -1 and hn == 0
    check("T3", "uniform half-integer cutoff family Lambda in Z>=0+1/2 "
                "gives chi=+1 on (0,1/2) and chi=-1 on (-1/2,0) "
                "for sampled twists",
          half_integer_ok)
    counterexamples_ok = (
        eta_h(tower_spectral(0.30, 20.25))[0] == 0
        and eta_h(tower_spectral(0.30, 20.75))[0] == 0
        and eta_h(tower_spectral(-0.30, 20.25))[0] == 0
        and eta_h(tower_spectral(-0.30, 20.75))[0] == 0
    )
    check("T3", "non-half-integer cutoffs Lambda=20.25 and 20.75 are "
                "excluded by explicit counterexamples at |a|=0.30",
          counterexamples_ok)

    # =======================================================================
    section("[T4] coexistence with the Koide-side anticommutation "
            "(escape hatch II realized)")
    # =======================================================================
    Dg = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]], dtype=float)
    G = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float)
    C3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=float)
    N12 = e1 @ e2
    check("T4", "[N, eps] = 0 (even element commutes with the volume "
                "grading)", np.allclose(N12 @ eps - eps @ N12, 0))
    check("T4", "{e_4, eps} = 0 and {e_1, eps} = 0 (odd elements "
                "anticommute with eps)",
          np.allclose(e4 @ eps + eps @ e4, 0)
          and np.allclose(e1 @ eps + eps @ e1, 0))
    check("T4", "[D_gen, C_3] = 0 (C_3-equivariance of the generation "
                "block)", np.allclose(Dg @ C3 - C3 @ Dg, 0))
    check("T4", "{D_gen, G} = 0 (L4-form anticommuting pair on the "
                "generation factor)", np.allclose(Dg @ G + G @ Dg, 0))
    genpart = np.kron(np.kron(Dg, np.eye(NY)), N12).astype(complex)
    bdypart = np.kron(np.kron(np.eye(3), Aa), eps)
    Dtot = genpart + bdypart
    Gam = np.kron(np.kron(G, np.eye(NY)), eps)
    check("T4", "D_tot Hermitian (sym (x) sym + Hermitian, parts commute)",
          np.allclose(Dtot.conj().T, Dtot))
    check("T4", "{D_gen-part, Gamma_prod} = 0 (Koide-side anticommutation "
                "survives on the product)",
          np.allclose(genpart @ Gam + Gam @ genpart, 0))
    check("T4", "[D_bdy-part, Gamma_prod] = 0 (sector selection on the "
                "boundary factor)",
          np.allclose(bdypart @ Gam - Gam @ bdypart, 0))
    check("T4", "the two parts of D_tot commute ([N, eps] = 0 transfers)",
          np.allclose(genpart @ bdypart - bdypart @ genpart, 0))
    check("T4", "Gamma_prod is an involution", np.allclose(Gam @ Gam,
          np.eye(Gam.shape[0])))

    # =======================================================================
    section("[F] falsifiers")
    # =======================================================================
    # (F1) a grading anticommuting with the WHOLE boundary operator
    # forces a mirror spectrum and eta = 0.
    Dmir = np.kron(Aa, s1.astype(complex))  # anticommutes with I (x) s3
    Gmir = np.kron(np.eye(NY), s3.astype(complex))
    lam_mir = np.linalg.eigvalsh(Dmir)
    e_mir, _ = eta_h(lam_mir)
    check("F", "(F1) full-anticommuting grading forces eta = 0 (mirror "
               "spectrum) -- the grading MUST commute with the boundary "
               "block; sector selection is the only route to nonzero eta",
          np.allclose(Dmir @ Gmir + Gmir @ Dmir, 0) and e_mir == 0,
          f"eta(mirror) = {e_mir:+d}")
    # (F2) index truncation manufactures a spurious label at a = 1/2.
    n_idx = np.arange(-20, 21)
    e_idx, _ = eta_h(n_idx + 0.5)
    check("F", "(F2) INDEX truncation at a = 1/2 fakes eta = +1 where "
               "spectral truncation gives 0 -- the truncation convention "
               "is load-bearing",
          e_idx == 1 and e5 == 0,
          f"index-cutoff eta = {e_idx:+d}, spectral-cutoff eta = {e5:+d}")
    # (F3) untwisted surface: no label (consistency with the retained
    # bulk-vanishing row).
    check("F", "(F3) a = 0 carries no label (h_delta = 1): consistent "
               "with the retained eta_APS = 0 bulk-vanishing row -- a "
               "nonzero label REQUIRES the twist datum",
          h0 == 1 and e0 == 0)

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
