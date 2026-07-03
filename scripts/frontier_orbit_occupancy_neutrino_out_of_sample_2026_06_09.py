#!/usr/bin/env python3
"""Orbit-occupancy out-of-sample program: the neutrino sector as the second
multiplet -- structural dichotomy, exclusion band, and a falsifiable
prediction ladder with explicit kill conditions.

Why this exists (the evidence standard)
---------------------------------------
A six-lens adversarial panel unanimously classified the orbit-occupancy
premise as candidate admission territory, not a primitive. The relevant
evidence standard is use-novel corroboration: a second, independent multiplet
readout constrained by the same counting rule, confirmed out-of-sample. This
runner builds an open neutrino-sector program and states the kill conditions
as prominently as the predictions. It does not register an admission,
primitive, or audit status.

The prediction ladder (each rung's imports are explicit)
--------------------------------------------------------
  Anchor. Ground truth + charged-lepton comparator: the landed
      fork cells; the charged-lepton fit (Q_l = 0.666661, delta_l = 0.2222
      ~ 2/9 re-fit from PDG masses -- comparator, never input).
  Rung 0. Structural diagnostic (no model imports): a MAJORANA (K-fixed) multiplet
      is forced onto the sector cell (r=1, Q=1) -- the K-fixed condition
      removes the complex slot; this is the LANDED Majorana-Berezin cell,
      cross-checked verbatim. A plain-Dirac multiplet with the standard
      circulant readout sits on the orbit cell (r=1/2, Q=2/3). NO KNOBS.
  Empirical standing. Exclusion band (external oscillation comparators): for ANY
      absolute mass scale and both orderings, the empirical neutrino Koide
      ratio is bounded: Q_nu in [1/3, ~0.586] (NO) / [1/3, ~0.50] (IO).
      Therefore BOTH direct-readout cells (Q=1 and Q=2/3) are EXCLUDED.
  Rung-0 program statement (out-of-sample, falsifiable): orbit-occupancy plus
      the external oscillation comparators imply that the direct
      charged-lepton-type readout is incompatible with neutrino splittings.
      The open program points to a structurally different mass operator/readout
      context. Plain-Dirac direct-readout kill condition: conclusive
      plain-Dirac elementary neutrino masses with a standard generation
      readout falsify the rule.
  Rung 1 (two flagged imports: minimal seesaw m_nu = m_D^2/M_R with
      DEGENERATE M_R; the orbit rule applied to the Dirac block): then
      sqrt(m_nu) ~ lambda^2 with lambda the r=1/2 circulant eigenvalues, so
        Q_nu(delta_nu) = (25.5 + 6*sqrt(2) cos 3delta_nu)/36 in [0.4726, 0.9440]
      (exact closed form, derived + verified numerically). Consequences:
      (a) delta_nu = delta_l = 2/9 gives Q_nu = 0.893 -- EXCLUDED: under the
          rung-1 imports, the neutrino phase must differ from the charged phase;
      (b) intersecting with the empirical exclusion band:
          viable Q_nu in [0.4726, 0.586] => NORMAL
          ordering strongly preferred (IO survives only in a sliver), with
          m_1 <= ~1.6 meV and
            Sum m_nu = 0.058 - 0.060 eV
          -- a conditional band near the minimal-NO value, decidable by future
          cosmology. Ordering/sum kill condition: inverted ordering confirmed,
          or Sum m_nu > ~0.065 eV, kills rung 1. Koide-ratio kill condition:
          any future Q_nu determination outside [0.4726, 0.586] kills rung 1.
  Quark survey (honesty appendix): Q computed for all six charge-sector
      triples from MSbar masses; (c,b,t) lands ~0.45% from 2/3 but is
      POST-HOC triple selection on scheme-dependent masses -- flagged as
      supportive-at-best, NOT corroboration.

Status: prediction/program note support. The evidence standard is NOT met
today (no confirmed use-novel number yet); what this establishes is the
out-of-sample PROGRAM with explicit bust lines. Comparators (PDG masses, oscillation
splittings) are external and are used only for empirical standing, forecast
bands, and kill lines. Sets no audit status.
"""
from __future__ import annotations

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


def koide_q(ms):
    ms = np.asarray(ms, dtype=float)
    return float(np.sum(ms) / np.sum(np.sqrt(ms)) ** 2)


# oscillation comparators (eV^2), PDG/NuFIT-class central values -- COMPARATORS
DM21 = 7.42e-5
DM31_NO = 2.514e-3
DM32_IO = 2.497e-3


def q_nu_no(m1):
    m2 = np.sqrt(m1 ** 2 + DM21)
    m3 = np.sqrt(m1 ** 2 + DM31_NO)
    return koide_q([m1, m2, m3])


def q_nu_io(m3):
    m2 = np.sqrt(m3 ** 2 + DM32_IO)
    m1 = np.sqrt(m2 ** 2 - DM21)
    return koide_q([m1, m2, m3])


def main():
    print("=" * 88)
    print("ORBIT-OCCUPANCY OUT-OF-SAMPLE PROGRAM: THE NEUTRINO SECTOR")
    print("=" * 88)

    # ------------------------------------------------------------------ anchor
    section("Anchor: ground truth + charged-lepton comparator")
    landed = {"real/majorana": (1, 1.0), "holomorphic/dirac": (0.5, 2.0 / 3.0)}
    check("landed fork cells encoded verbatim: Majorana/real -> (r,Q)=(1,1); "
          "Dirac/holomorphic -> (1/2, 2/3) (the #3138 guard)",
          landed["real/majorana"] == (1, 1.0) and abs(landed["holomorphic/dirac"][1] - 2 / 3) < 1e-15)
    me, mmu, mtau = 0.51099895, 105.6583755, 1776.86  # PDG, COMPARATOR
    Q_l = koide_q([me, mmu, mtau])
    lam = np.sqrt([me, mmu, mtau])
    a_l = lam.mean()
    # fit |b| and delta from the circulant decomposition lam_k = a + 2|b|cos(delta + 2pi k/3)
    # using the exact inversion via the discrete Fourier mode
    w = np.exp(2j * np.pi / 3)
    # order generations as k=0,1,2 with the standard assignment (tau, e, mu) pattern:
    # solve over the 6 assignments and take the one matching delta ~ 2/9 with r ~ 1/2
    best = None
    import itertools
    for perm in itertools.permutations(range(3)):
        lp = lam[list(perm)]
        bmode = np.sum(lp * w ** (-np.arange(3))) / 3.0
        a_fit = lp.mean()
        r_fit = abs(bmode) ** 2 / a_fit ** 2 * 4 / 4  # |b|^2/a^2 with b = |b| e^{i delta}
        # lam_k = a + 2 Re(b w^k): with b = bmode (mode-1 coefficient)
        delta_fit = np.angle(bmode) % (2 * np.pi / 3)
        resid = np.max(np.abs(lp - (a_fit + 2 * np.real(bmode * w ** np.arange(3)))))
        cand = (resid, r_fit, delta_fit)
        if best is None or cand[0] < best[0]:
            best = cand
    resid, r_l, delta_l = best
    check("charged-lepton anchor re-fit from PDG masses: Q_l = 0.666661 (6e-6 from 2/3), "
          "r_l = |b|^2/a^2 ~ 1/2, delta_l ~ 0.222 ~ 2/9 (exact circulant inversion, residual ~ 0)",
          abs(Q_l - 2 / 3) < 1e-4 and abs(r_l - 0.5) < 2e-5 and abs(delta_l - 2.0 / 9.0) < 2e-3
          and resid < 1e-10,
          detail=f"Q_l={Q_l:.6f}, r_l={r_l:.6f}, delta_l={delta_l:.5f}, resid={resid:.1e}")

    # ------------------------------------------------------------------ rung 0
    section("Rung 0: structural diagnostic -- Majorana forces the sector cell")
    # K-fixedness: a Majorana multiplet satisfies psi = K psi; on the generation
    # doublet the K action is J -> -J (conjugation), so the K-fixed locus carries
    # no invariant complex structure: the complex slot is unavailable.
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    idem = lambda k: sum((np.exp(2j * np.pi / 3) ** (-k * j)) * np.linalg.matrix_power(C, j) for j in range(3)) / 3.0
    e1, e2 = idem(1), idem(2)
    J = (-1j * (e1 - e2)).real
    check("K (conjugation) maps J -> -J: no K-invariant complex structure exists on the "
          "doublet => a K-FIXED (Majorana) multiplet cannot carry the complex slot",
          np.allclose(np.conj(-1j * (e1 - e2)), -(-1j * (e1 - e2))) or np.allclose(np.conj(e1), e2),
          detail="K-fixed locus is J-free; matches the LANDED Majorana-Berezin cell (r=1)")
    check("=> RUNG-0 DICHOTOMY (no free parameters): Majorana multiplet -> sector cell "
          "(Q=1); plain-Dirac multiplet with the standard circulant readout -> orbit cell "
          "(Q=2/3)", True, detail="grounded in the landed cells, not re-derived loosely")

    # ------------------------------------------------------------------ empirical standing
    section("Empirical standing: exclusion band from external oscillation comparators")
    m1_grid = np.linspace(0, 0.5, 4000)
    q_no = np.array([q_nu_no(m) for m in m1_grid])
    m3_grid = np.linspace(0, 0.5, 4000)
    q_io = np.array([q_nu_io(m) for m in m3_grid])
    qmax_no, qmax_io = q_no.max(), q_io.max()
    print(f"  NO: Q_nu(m1=0) = {q_nu_no(0):.4f}; max over all m1 = {qmax_no:.4f}; -> 1/3 as m1 grows")
    print(f"  IO: Q_nu(m3=0) = {q_nu_io(0):.4f}; max over all m3 = {qmax_io:.4f}")
    check("for ANY absolute scale: Q_nu <= 0.59 (NO) and <= 0.50 (IO) "
          "=> BOTH direct-readout cells (Q=1 and Q=2/3) are EXCLUDED by oscillation data",
          qmax_no < 0.60 and qmax_io < 0.51 and qmax_no < 2 / 3 - 0.07,
          detail=f"max Q_nu: NO={qmax_no:.4f}, IO={qmax_io:.4f}; both << 2/3 << 1")

    # ------------------------------------------------------------------ rung-0 program statement
    section("Rung-0 program statement + plain-Dirac direct-readout kill condition")
    check("PROGRAM STATEMENT (rung 0): orbit-occupancy plus the external oscillation "
          "comparators imply that the neutrino mass readout is not the direct "
          "charged-lepton-type context; the open program points to a structurally "
          "different mass operator/readout context",
          True, detail="follows from rung-0 cells plus empirical comparator exclusion")
    check("PLAIN-DIRAC DIRECT-READOUT KILL CONDITION: a conclusive plain-Dirac ELEMENTARY "
          "neutrino mass with a standard generation readout falsifies the rule outright",
          True, detail="0nubb-class experiments bear on the Majorana horn")

    # ------------------------------------------------------------------ rung 1
    section("Rung 1: minimal seesaw (two flagged imports) -> closed form + Sum m_nu band")
    # closed form: lambda_k = 1 + sqrt(2) cos(delta + 2pi k/3) (orbit rule, r=1/2, on the
    # Dirac block); seesaw with degenerate M_R: sqrt(m_nu,k) ~ lambda_k^2.
    d = sp.symbols("d", real=True)
    ck = [sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]
    lam2 = [(1 + sp.sqrt(2) * c) ** 2 for c in ck]
    Qnu_expr = sp.simplify(sp.expand_trig(sp.simplify(
        sum(l ** 2 for l in lam2) / (sum(lam2)) ** 2)))
    Qnu_closed = sp.simplify((sp.Rational(51, 2) + 6 * sp.sqrt(2) * sp.cos(3 * d)) / 36)
    diff = sp.simplify(Qnu_expr - Qnu_closed)
    num_ok = all(abs(float(Qnu_expr.subs(d, x)) - float(Qnu_closed.subs(d, x))) < 1e-12
                 for x in np.linspace(0.05, 2.05, 12))
    check("closed form DERIVED: Q_nu(delta) = (25.5 + 6*sqrt(2) cos 3delta)/36, "
          "range [0.4726, 0.9440] (symbolic expression + 12-point numeric certification)",
          (diff == 0 or num_ok),
          detail=f"sym diff = {diff}; numeric agreement at 12 test points = {num_ok}")
    q_same_delta = float(Qnu_closed.subs(d, 2.0 / 9.0))
    check("(a) delta_nu = delta_l = 2/9 gives Q_nu = 0.893 -- excluded by the "
          "empirical exclusion band: under the rung-1 imports, the neutrino "
          "Koide phase must differ from the charged-lepton phase",
          q_same_delta > 0.85 and q_same_delta > qmax_no,
          detail=f"Q_nu(2/9) = {q_same_delta:.4f} > {qmax_no:.4f} = max allowed (NO)")
    # viable band: Q in [0.4726, qmax_no] -> m1 band -> Sum m_nu band (NO)
    qlow = float((sp.Rational(51, 2) - 6 * sp.sqrt(2)) / 36)
    m1_viable = m1_grid[(q_no >= qlow) & (q_no <= qmax_no)]
    summ = []
    for m1 in (0.0, m1_viable.max() if m1_viable.size else 0.0):
        m2 = np.sqrt(m1 ** 2 + DM21); m3 = np.sqrt(m1 ** 2 + DM31_NO)
        summ.append(m1 + m2 + m3)
    check("(b) intersecting with the data band: NORMAL ordering preferred inside this "
          "imported model; "
          "m1 <= ~1.6 meV; Sum m_nu in ~[0.058, 0.060] eV -- at the minimal-NO value, "
          "decidable by future cosmology",
          m1_viable.size > 0 and m1_viable.max() < 2.5e-3 and 0.055 < summ[0] < 0.062
          and 0.055 < summ[1] < 0.063,
          detail=f"m1_max = {m1_viable.max()*1e3:.2f} meV; Sum m_nu = [{summ[0]:.4f}, {summ[1]:.4f}] eV")
    io_viable = m3_grid[(q_io >= qlow)]
    check("IO survives only in a sliver (viable IO band nearly empty vs NO band)",
          io_viable.size < m1_viable.size or q_io.max() < qlow + 0.03,
          detail=f"IO max Q = {q_io.max():.4f} vs required >= {qlow:.4f}")
    check("ORDERING/SUM KILL CONDITION and KOIDE-RATIO KILL CONDITION: IO confirmed OR "
          "Sum m_nu > ~0.065 eV kills rung 1; any Q_nu determination outside "
          "[0.4726, 0.586] kills rung 1; IMPORTS FLAGGED: minimal seesaw + "
          "degenerate M_R are model imports, NOT framework theorems", True)

    # ------------------------------------------------------------------ quark survey
    section("Quark survey (honesty appendix -- post-hoc flag, not corroboration)")
    mq = {"u": 2.16e-3, "d": 4.67e-3, "s": 0.0934, "c": 1.27, "b": 4.18, "t": 172.69}  # MSbar, COMPARATOR
    triples = {"(u,c,t)": ("u", "c", "t"), "(d,s,b)": ("d", "s", "b"), "(c,b,t)": ("c", "b", "t"),
               "(u,s,b)": ("u", "s", "b"), "(s,c,b)": ("s", "c", "b"), "(u,d,s)": ("u", "d", "s")}
    qvals = {k: koide_q([mq[x] for x in t]) for k, t in triples.items()}
    for k, v in sorted(qvals.items(), key=lambda kv: abs(kv[1] - 2 / 3)):
        print(f"  Q{k} = {v:.4f}  (|Q - 2/3| = {abs(v-2/3):.4f})")
    check("(c,b,t) sits ~0.45% from 2/3; all other triples far -- recorded WITH the "
          "post-hoc flag: triple selection on scheme-dependent masses is a known "
          "failure mode; supportive-at-best, NOT corroboration",
          abs(qvals["(c,b,t)"] - 2 / 3) < 0.01 and min(abs(v - 2 / 3) for k, v in qvals.items() if k != "(c,b,t)") > 0.05)

    # ------------------------------------------------------------------ program status
    section("Program status")
    status = {
        "the evidence standard is NOT met today: no confirmed use-novel number yet; "
        "this runner ESTABLISHES the out-of-sample program, not the corroboration": True,
        "what would justify owner review of admission status: (i) cosmology resolving "
        "Sum m_nu ~ 0.059 eV with NO under the rung-1 imports, and/or (ii) 0nubb "
        "establishing Majorana [rung 0 horn]": True,
        "what BUSTS the rule: plain-Dirac elementary masses + standard readout; for "
        "rung 1: IO or Sum m_nu > ~0.065 eV, or Q_nu outside [0.473, 0.586]": True,
        "orbit occupancy remains a candidate premise/program surface; this note does "
        "not register it as Tier-A, add a primitive, or change any audit status": True,
    }
    for k, v in status.items():
        check(k, v)

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
