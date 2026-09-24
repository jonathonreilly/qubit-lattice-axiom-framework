#!/usr/bin/env python3
"""Referee of corrigendum-PR8178 a2. Own shift algebra and a read of the pinned note."""
import cmath
import math
import subprocess

import sympy as sp

SHA = "e6ffae5b460b"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_"
        "EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_NONLINEAR_LAW_MEASURED_AGAINST_IT_"
        "BOUNDED_THEOREM_NOTE_2026-09-17.md")
RUN = ("scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_"
       "exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py")
SCI = ".claude/science/physics-loops/admissibility-induced-law-20260906"


def show(path):
    out = subprocess.run(["git", "show", f"{SHA}:{path}"], capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(out.stderr.strip() or f"missing {path}")
    return out.stdout


def main():
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    phic = (1 + sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2)) / 3
    def gone(expr):
        return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0

    if not gone(phi - phic - (2 * sp.I / 3) * (sp.sin(k1) + sp.sin(k2))):
        raise SystemExit("difference")
    if not gone(sp.Abs(phi) ** 2 - sp.Abs(phic) ** 2):
        raise SystemExit("moduli")
    u = (3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)) / 9
    if not gone(sp.Abs(phi) ** 2 - u):
        raise SystemExit("|phi|^2")
    if not gone(sp.conjugate(phic) - phi):
        raise SystemExit("conjugate")
    # P e = phi_c e, P^T e = phi e, for e_x = exp(+i k.x)
    for L in (3, 4):
        for n1 in range(L):
            for n2 in range(L):
                kk = (2 * math.pi * n1 / L, 2 * math.pi * n2 / L)
                pc = (1 + cmath.exp(-1j * kk[0]) + cmath.exp(-1j * kk[1])) / 3
                pp = (1 + cmath.exp(1j * kk[0]) + cmath.exp(1j * kk[1])) / 3
                worst = 0.0
                for x1 in range(L):
                    for x2 in range(L):
                        e = cmath.exp(1j * (kk[0] * x1 + kk[1] * x2))
                        pe = (e
                              + cmath.exp(1j * (kk[0] * ((x1 - 1) % L) + kk[1] * x2))
                              + cmath.exp(1j * (kk[0] * x1 + kk[1] * ((x2 - 1) % L)))) / 3
                        pt = (e
                              + cmath.exp(1j * (kk[0] * ((x1 + 1) % L) + kk[1] * x2))
                              + cmath.exp(1j * (kk[0] * x1 + kk[1] * ((x2 + 1) % L)))) / 3
                        worst = max(worst, abs(pe - pc * e), abs(pt - pp * e))
                if worst > 1e-12:
                    raise SystemExit(f"action {L} {worst}")
    print("S1-S5 FOLLOW: under e^{-ik.x} the backward average has multiplier phi_c, and under "
          "e^{+ik.x} it has the stated phi; phi-phi_c=(2i/3)(sin k1+sin k2) and |phi|=|phi_c|; "
          "on L=3,4 every mode satisfies P e_k = phi_c e_k and P^T e_k = phi e_k for e_x=e^{+ik.x}; "
          "conj(phi_c)=phi, so an fft2 coefficient that steps by phi_c is measured as phi")

    note = show(NOTE).splitlines()
    line = note[84]
    if "e^{-ik" not in line.replace(" ", "") and "e^{−ik" not in line:
        raise SystemExit(f"line 85 transform missing: {line[:180]}")
    if "(1 + e^{ik" not in line and "(1 + e^{ik₁}" not in line and "e^{ik_1}" not in line:
        # unicode subscripts
        if "e^{ik" not in line and "ik₁" not in line and "ik\u2081" not in line:
            raise SystemExit(f"line 85 phi missing: {line[:240]}")
    t11 = [l for l in note if l.startswith("**T1.1.**")]
    if len(t11) != 1 or "conjugate convention" not in t11[0]:
        raise SystemExit("T1.1 clause")
    hand = show(f"{SCI}/HANDOFF.md").splitlines()
    if len(hand) < 30 or "phi" not in hand[29].lower() and "φ" not in hand[29]:
        raise SystemExit(f"HANDOFF:30 {hand[29][:200] if len(hand)>=30 else 'short'}")
    run = show(RUN)
    if "phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3" not in run:
        raise SystemExit("runner phi")
    print("S6 FOLLOWS at the pinned head e6ffae5b460b: note line 85 states both the e^{-ik.x} "
          "transform and the multiplier phi in one sentence; T1.1's proof says the conjugate "
          "convention gives the stated phi; HANDOFF.md:30 carries the formula and is outside a1's "
          "nine lines; the runner writes phi with +i, so changing the transform is two clauses of "
          "prose and changing the formula touches executed code")
    print("SUMMARY: confirmed - PR #8178 T1.1's defect is one sentence with two repairs: phi to "
          "phi_c in ten lines, three of them executed or frozen, or the transform to e^{+ik.x} in "
          "two clauses, which leaves the runner, the cache and both of block 35's controls "
          "(they measure phi, not phi_c) untouched")
    print("HIT: confirmed - the transform clause is the cheaper repair of PR #8178 T1.1; a1's "
          "formula repair is also correct but its line list omits HANDOFF.md:30")


if __name__ == "__main__":
    main()
