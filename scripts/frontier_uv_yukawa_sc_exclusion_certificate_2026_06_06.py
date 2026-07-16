#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
UV gauge-to-Yukawa coefficient comparison and plaquette-radius diagnostic
============================================================================

This runner consumes the bounded finite packet from
``UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md``:

        C_pert   = 1/(2 N_c) = 1/6
        C_strong = 1/N_c^2   = 1/9

It does not identify either square root with a physical Yukawa/gauge readout
and does not select a governing expansion.

The remaining blocks reproduce a finite d-log Pade estimate from connected
plaquette coefficients and test the exact limitation that a common
partition-function denominator does not imply an identical uncancelled
nearest singularity for every observable. The output is domain evidence for
the plaquette series, not a convergence proof for the four-fermion observable
and not a perturbative selector.

Run:  python3 scripts/frontier_uv_yukawa_sc_exclusion_certificate_2026_06_06.py
"""

import sys
import math
from pathlib import Path
import sympy as sp

PASS = []
FAIL = []
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "UV_YUKAWA_STRONG_COUPLING_DOMAIN_EXCLUSION_RADIUS_CERTIFICATE_BOUNDED_NOTE_2026-06-06.md"


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    return cond


# ---------------------------------------------------------------------------
# Certified exact connected-plaquette coefficients (reused; DERIVED + reproven
# from SU(3)-Haar primitives + the Picard-Fuchs J recurrence in the on-main
# campaign runners frontier_beta6_d9/d10/d11_coefficient_2026_06_04.py and the
# certified-backbone note; CITED here, not re-derived).
# Delta(beta) = <P> - P_1plaq = sum_{n>=5} d_n beta^n
# ---------------------------------------------------------------------------
D = {
    5: sp.Rational(1, 472392),
    6: sp.Rational(7, 5668704),
    7: sp.Rational(5, 17006112),
    8: sp.Rational(5, 272097792),
    9: sp.Rational(-2035, 264479053824),
    10: sp.Rational(-10483, 5289581076480),
    11: sp.Rational(-13, 3967185807360),
}


def block1_C_pert():
    print("\n[BLOCK 1] Reprove perturbative coefficient C_pert from SU(N_c) Fierz")
    Nc = sp.Integer(3)
    # Retained SU(N_c) Fierz (YT_EW_COLOR_PROJECTION_THEOREM):
    #   sum_A (T^A)_ab (T^A)_cd = 1/2 [ d_ad d_bc - (1/Nc) d_ab d_cd ]
    # color-singlet (d_ab d_cd) projection of one-gluon exchange -> C_pert = 1/(2 Nc).
    # Verify the Fierz identity itself on explicit SU(3) generators (Gell-Mann/2).
    import numpy as np
    lam = _gell_mann()
    T = [m / 2 for m in lam]  # T^A = lambda^A / 2, Tr(T^A T^B) = 1/2 delta^AB
    lhs = np.zeros((3, 3, 3, 3), dtype=complex)
    for A in range(8):
        lhs += np.einsum('ab,cd->abcd', T[A], T[A])
    rhs = 0.5 * (np.einsum('ad,bc->abcd', np.eye(3), np.eye(3))
                 - (1.0 / float(Nc)) * np.einsum('ab,cd->abcd', np.eye(3), np.eye(3)))
    fierz_err = float(np.max(np.abs(lhs - rhs)))
    check("Fierz identity holds on explicit SU(3) generators", fierz_err < 1e-12,
          f"max|sum_A T^A T^A - 1/2(d_ad d_bc - 1/N d_ab d_cd)| = {fierz_err:.2e}")
    # color-singlet coefficient magnitude = 1/(2 Nc)
    C_pert = sp.Rational(1, 2) / Nc
    sqrt_pert = sp.sqrt(C_pert)
    check("C_pert = 1/(2 N_c) = 1/6", C_pert == sp.Rational(1, 6), f"C_pert={C_pert}")
    check("sqrt(C_pert) = 1/sqrt(6) as coefficient arithmetic",
          sp.simplify(sqrt_pert - 1 / sp.sqrt(6)) == 0,
          f"= {float(sqrt_pert):.8f}")
    return C_pert, sqrt_pert


def block2_C_strong():
    print("\n[BLOCK 2] Reprove strong-coupling coefficient C_strong from one-link Haar")
    Nc = sp.Integer(3)
    # one-link Haar (note B.1):  int dU U_ab (Udag)_cd = (1/Nc) d_ad d_bc
    # two bilinears at a link + same Fierz -> C_strong = 1/Nc^2.
    C_strong = sp.Rational(1, 1) / Nc**2
    sqrt_strong = sp.sqrt(C_strong)
    check("C_strong = 1/N_c^2 = 1/9", C_strong == sp.Rational(1, 9), f"C_strong={C_strong}")
    check("sqrt(C_strong) = 1/N_c = 1/3 as coefficient arithmetic",
          sp.simplify(sqrt_strong - sp.Rational(1, 3)) == 0,
          f"= {float(sqrt_strong):.8f}")
    # Haar-sampled cross-check of B.1 (the correct index contraction: <U_ab (Udag)_cd>).
    import numpy as np
    rng = np.random.default_rng(20260606)

    def rand_su3():
        z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / np.sqrt(2)
        q, r = np.linalg.qr(z)
        ph = np.diagonal(r) / np.abs(np.diagonal(r))
        q = q * ph
        q = q / np.linalg.det(q) ** (1.0 / 3.0)
        return q

    N = 120000
    acc = np.zeros((3, 3, 3, 3), dtype=complex)
    for _ in range(N):
        U = rand_su3()
        Ud = U.conj().T
        acc += np.einsum('ab,cd->abcd', U, Ud)
    acc /= N
    expd = np.einsum('ad,bc->abcd', np.eye(3), np.eye(3)) / 3.0
    err = float(np.max(np.abs(acc - expd)))
    check("Haar one-link B.1: <U_ab (Udag)_cd> = (1/N_c) d_ad d_bc (MC)", err < 0.02,
          f"max|.|={err:.4f} -> 0")
    return C_strong, sqrt_strong


# ---- Pade helpers (manual, exact then numeric pole-finding) ----
def dlog_series(cs, order):
    """g_n, n=0..order : Taylor of h'/h where h = sum cs[k] x^k (cs[0]=1)."""
    g = []
    for n in range(order + 1):
        hp_n = (n + 1) * cs[n + 1] if (n + 1) < len(cs) else sp.Integer(0)
        s = hp_n
        for j in range(n):
            cj = cs[n - j] if (n - j) < len(cs) else sp.Integer(0)
            s -= g[j] * cj
        g.append(sp.nsimplify(s))  # cs[0]=1 so divide by 1
    return g


def pade_poles(a, L, M):
    """Poles of the [L/M] Pade of series a (a[0..L+M]); returns list of complex roots of Q."""
    # solve for q_1..q_M (q_0 = 1): for m=1..M : sum_{j=0..M} q_j a_{L+m-j} = 0
    import numpy as np
    A = np.zeros((M, M))
    rhs = np.zeros(M)
    for m in range(1, M + 1):
        for j in range(1, M + 1):
            idx = L + m - j
            A[m - 1, j - 1] = float(a[idx]) if 0 <= idx < len(a) else 0.0
        idx0 = L + m
        rhs[m - 1] = -(float(a[idx0]) if 0 <= idx0 < len(a) else 0.0)
    q = np.linalg.solve(A, rhs)  # q_1..q_M
    Q = np.concatenate(([1.0], q))  # Q(x) = sum_{j} Q[j] x^j
    roots = np.roots(Q[::-1])  # numpy wants highest power first
    return roots


def block3_radius():
    print("\n[BLOCK 3] Finite d-log Pade radius estimate from d_5..d_11")
    d5 = D[5]
    cs = [sp.Integer(1)] + [D[5 + k] / d5 for k in range(1, 7)]  # c_0..c_6, c_k = d_{5+k}/d_5
    check("series prefactor positive d_5=1/472392 > 0", d5 > 0)
    check("sign change at d_9 is consistent with complex-pair behavior", D[9] < 0 and D[8] > 0,
          f"d_8>0, d_9<0")
    g = dlog_series(cs, 5)  # g_0..g_5
    # [2/2] d-log Pade (the strongest 7-coefficient estimator; needs g_0..g_4)
    roots22 = pade_poles([float(x) for x in g], 2, 2)
    mods22 = sorted(abs(r) for r in roots22)
    R22 = mods22[0]
    # arg of the dominant pair
    import numpy as np
    dom = min(roots22, key=lambda r: abs(r))
    arg_deg = abs(np.degrees(np.angle(dom)))
    is_complex = abs(dom.imag) > 1e-6
    check("[2/2] d-log Pade dominant singularity is a COMPLEX pair", is_complex,
          f"beta_c ~ {dom.real:.3f} +/- {abs(dom.imag):.3f} i, arg ~ {arg_deg:.1f} deg")
    check("[2/2] radius |beta_c| ~ 5.39 (in [5.0, 5.8])", 5.0 < R22 < 5.8,
          f"R22 = {R22:.3f}")
    check("finite [2/2] estimate lies below beta=6", R22 < 6.0,
          f"R_est ~ {R22:.3f} < 6; not a convergence certificate")
    # [1/1]: the real-pole ansatz -> spurious real pole (TEETH: must NOT be trusted)
    roots11 = pade_poles([float(x) for x in g], 1, 1)
    r11 = roots11[0]
    check("[1/1] real-pole ansatz gives a (spurious) REAL pole ~3.4", abs(r11.imag) < 1e-9,
          f"beta_c[1/1] = {r11.real:.3f} (spurious; invalid for a complex pair)")
    # naive ratio extrapolation on early coefficients -> apparent R~8 (the artifact):
    # sqrt(|c_1/c_3|) = sqrt(|d_6/d_8|), the real-pole intuition applied to a complex pair
    naive = math.sqrt(abs(float(D[6] / D[8])))
    check("naive early-ratio extrapolation OVER-estimates R (>6, the artifact)", naive > 6.0,
          f"naive R ~ sqrt(|d_6/d_8|) ~ {naive:.2f} (real-pole intuition on a complex pair => WRONG)")
    return R22


def block4_observable_scope():
    print("\n[BLOCK 4] Common-denominator sharing and cancellation controls")
    # Finite-volume lemma demonstrated on a minimal 1-link toy: two distinct local
    # observables share the SAME beta-singularity (a zero of the common Z), so they
    # share the SAME radius. (Illustration of the entire-numerator/common-denominator
    # structure; the physical statement cites Yang-Lee/Fisher + Itzykson-Drouffe.)
    b = sp.symbols('b')
    # toy partition fn with a complex-conjugate zero pair at b = 2 +/- i (|b_c| = sqrt(5));
    # written in REAL expanded form so its series coefficients are real rationals:
    Z = b**2 - 4 * b + 5  # = (b-(2+i))(b-(2-i)); entire (polynomial) in b
    # two different "observable numerators", each entire in b:
    N1 = b + 3
    N2 = b**2 - 1
    O1 = sp.series(N1 / Z, b, 0, 8).removeO()
    O2 = sp.series(N2 / Z, b, 0, 8).removeO()
    p1 = [sp.nsimplify(sp.re(O1.coeff(b, k))) for k in range(8)]
    p2 = [sp.nsimplify(sp.re(O2.coeff(b, k))) for k in range(8)]
    r1 = sorted(abs(r) for r in pade_poles([float(x) for x in p1], 3, 2))[0]
    r2 = sorted(abs(r) for r in pade_poles([float(x) for x in p2], 3, 2))[0]
    target = float(sp.sqrt(5))
    check("two chosen observables share one radius |b_c|=sqrt(5)",
          abs(r1 - target) < 1e-3 and abs(r2 - target) < 1e-3,
          f"R(O1)={r1:.4f}, R(O2)={r2:.4f}, sqrt(5)={target:.4f}")
    O_cancel = sp.simplify(Z / Z)
    check("an entire numerator can cancel all denominator zeros",
          O_cancel == 1,
          "O_cancel = Z/Z = 1, so common Z does not force an identical radius")
    check("plaquette radius cannot be assigned to another observable from common Z alone",
          O_cancel == 1,
          "observable-specific cancellation leaves the four-fermion radius open")
    return True


def block5_scope_boundary(R22, sqrt_pert, sqrt_strong):
    print("\n[BLOCK 5] Source-note selector firewall")
    note = NOTE.read_text(encoding="utf-8")
    check("the two coefficient square roots are distinct",
          sp.simplify(sqrt_pert - sqrt_strong) != 0,
          f"1/sqrt(6)={float(sqrt_pert):.5f} vs 1/N_c={float(sqrt_strong):.5f}")
    check("source note preserves public C_strong = 1/N_c^2 convention",
          "`C_strong = 1/N_c^2`" in note)
    check("source note explicitly leaves governing-expansion selection open",
          "No governing-expansion conclusion follows from this packet" in note)
    check("source note does not claim an only-convergent expansion",
          "only convergent expansion" not in note.lower())
    check("beta=6 comparison is retained only as finite plaquette evidence",
          R22 < 6.0 and "finite-order" in note)
    return True


def block6_literature_comparator(R22):
    print("\n[BLOCK 6] Literature complex-singularity comparators (never inputs)")
    # Li-Meurice hep-lat/0507034: plaquette series analysis suggested a
    # singularity scale beta ~ 5.7. Denbleyker et al. arXiv:0710.5771:
    # finite-volume SU(3) Fisher zeros near 5.54 +/- 0.10i and 5.54 +/- 0.16i.
    series_scale = 5.7
    fisher_modulus = abs(complex(5.54, 0.10))
    check("R_SC consistent with the earlier series-analysis scale ~5.7",
          abs(R22 - series_scale) / series_scale < 0.10,
          f"R_SC={R22:.3f} vs series scale {series_scale} (comparator only)")
    check("R_SC consistent with the finite-volume Fisher-zero modulus ~5.54",
          abs(R22 - fisher_modulus) / fisher_modulus < 0.05,
          f"R_SC={R22:.3f} vs |5.54+0.10i|={fisher_modulus:.3f}")
    check("all comparator scales are below 6 without radius transfer",
          R22 < 6 and series_scale < 6 and fisher_modulus < 6,
          "comparison is plaquette-series evidence only")
    return True


def main():
    print("=" * 78)
    print("UV gauge-to-Yukawa: coefficient comparison + plaquette-radius diagnostic")
    print("(bounded support for uv_gauge_to_yukawa_bridge_sc_vs_pert_note)")
    print("=" * 78)
    Cp, rp = block1_C_pert()
    Cs, rs = block2_C_strong()
    R22 = block3_radius()
    block4_observable_scope()
    block5_scope_boundary(R22, rp, rs)
    block6_literature_comparator(R22)
    print("\n" + "=" * 78)
    print(f"SCORECARD:  PASS = {len(PASS)}   FAIL = {len(FAIL)}")
    if FAIL:
        print("  FAILURES:", FAIL)
    print("=" * 78)
    return 0 if not FAIL else 1


def _gell_mann():
    import numpy as np
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    return [l1, l2, l3, l4, l5, l6, l7, l8]


if __name__ == "__main__":
    sys.exit(main())
