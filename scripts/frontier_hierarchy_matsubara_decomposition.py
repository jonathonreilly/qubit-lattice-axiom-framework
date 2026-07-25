#!/usr/bin/env python3
"""
Hierarchy Matsubara decomposition on the minimal APBC hypercube.

This script derives and verifies an exact closed-form temporal-mode
decomposition for the hierarchy determinant on the L_s = 2 APBC hypercube.

Key result:
  On the minimal spatial APBC block the two-site antiperiodic shift obeys
  T_i^2 = -Id, so each spatial hop operator satisfies A_i^2 = -Id exactly.
  That operator identity -- not a sampled momentum statement -- is what
  reduces the full Lt-dependent determinant to a temporal Matsubara product:

    |det(D + m)| = prod_omega [m^2 + u0^2 (3 + sin^2 omega)]^4

  where omega = (2n+1) pi / Lt are the APBC temporal momenta.

Part 0 supplies the general-L_t derivation of that product. The spatial
operators B and eta4 are extracted structurally from build_dirac_4d_apbc and
the reconstruction is checked exactly; the Clifford relations are integer
identities; the temporal factorization is the antiperiodic-circulant
diagonalization, verified symbolically for L_t = 2..16; and the exponent 4 is
obtained -- not inserted -- from a single symbolic characteristic-polynomial
factorization in (theta, u0, m) that covers every L_t at once.

This gives exact formulas for:
  - determinant magnitude
  - free-energy density difference
  - condensate density

The remaining theorem is then no longer "what is the determinant?" but
"which temporal averaging of this exact formula is the physical EWSB order
parameter?"
"""

from __future__ import annotations

import math
import sys
import time

import numpy as np
import sympy as sp

np.set_printoptions(precision=10, linewidth=120, suppress=True)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", fail_detail: str = ""):
    """Record a check.

    `detail` is the short evidence line printed on success. `fail_detail`
    carries the verbose per-point diagnostics and is printed only when the
    check does not pass, so a clean run stays inside the audit-packet
    rendering budget without losing any diagnostic power.
    """
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")
    if not condition and fail_detail:
        print(fail_detail)


def build_dirac_4d_apbc(Ls: int, Lt: int, u0: float, mass: float = 0.0):
    n = Ls**3 * Lt
    D = np.zeros((n, n), dtype=complex)

    def idx(x0: int, x1: int, x2: int, t: int) -> int:
        return (((x0 % Ls) * Ls + (x1 % Ls)) * Ls + (x2 % Ls)) * Lt + (t % Lt)

    for x0 in range(Ls):
        for x1 in range(Ls):
            for x2 in range(Ls):
                for t in range(Lt):
                    i = idx(x0, x1, x2, t)
                    D[i, i] += mass

                    eta = 1.0
                    xf = (x0 + 1) % Ls
                    sign = -1.0 if x0 + 1 >= Ls else 1.0
                    D[i, idx(xf, x1, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x0 - 1) % Ls
                    sign = -1.0 if x0 - 1 < 0 else 1.0
                    D[i, idx(xb, x1, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** x0
                    xf = (x1 + 1) % Ls
                    sign = -1.0 if x1 + 1 >= Ls else 1.0
                    D[i, idx(x0, xf, x2, t)] += u0 * eta * sign / 2.0
                    xb = (x1 - 1) % Ls
                    sign = -1.0 if x1 - 1 < 0 else 1.0
                    D[i, idx(x0, xb, x2, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1)
                    xf = (x2 + 1) % Ls
                    sign = -1.0 if x2 + 1 >= Ls else 1.0
                    D[i, idx(x0, x1, xf, t)] += u0 * eta * sign / 2.0
                    xb = (x2 - 1) % Ls
                    sign = -1.0 if x2 - 1 < 0 else 1.0
                    D[i, idx(x0, x1, xb, t)] -= u0 * eta * sign / 2.0

                    eta = (-1.0) ** (x0 + x1 + x2)
                    tf = (t + 1) % Lt
                    sign = -1.0 if t + 1 >= Lt else 1.0
                    D[i, idx(x0, x1, x2, tf)] += u0 * eta * sign / 2.0
                    tb = (t - 1) % Lt
                    sign = -1.0 if t - 1 < 0 else 1.0
                    D[i, idx(x0, x1, x2, tb)] -= u0 * eta * sign / 2.0
    return D


def temporal_modes(Lt: int):
    return np.array([(2 * n + 1) * math.pi / Lt for n in range(Lt)], dtype=float)


def exact_det_formula(Lt: int, u0: float, mass: float) -> float:
    omegas = temporal_modes(Lt)
    vals = [mass**2 + u0**2 * (3.0 + math.sin(w) ** 2) for w in omegas]
    prod = 1.0
    for v in vals:
        prod *= v**4
    return prod


def exact_free_energy_density(Lt: int, u0: float, mass: float) -> float:
    omegas = temporal_modes(Lt)
    return (1.0 / (2.0 * Lt)) * sum(
        math.log1p(mass**2 / (u0**2 * (3.0 + math.sin(w) ** 2))) for w in omegas
    )


def exact_condensate_density(Lt: int, u0: float, mass: float) -> float:
    omegas = temporal_modes(Lt)
    return (mass / Lt) * sum(
        1.0 / (mass**2 + u0**2 * (3.0 + math.sin(w) ** 2)) for w in omegas
    )


NS = 8  # 2^3 spatial sites of the L_s = 2 hypercube
EXTRACT_LT = [2, 3, 4, 5, 6, 8]
SPECTRUM_LT = list(range(2, 17))


def extract_operators(Lt: int):
    """Read B, eta4, S out of the matrix `build_dirac_4d_apbc` actually builds.

    The flat layout is idx(x0,x1,x2,t) = (((x0)*2 + x1)*2 + x2)*Lt + t, i.e.
    (8 spatial) (x) (Lt temporal) in numpy.kron(spatial, temporal) order.
    Nothing here is written down from the algebra: the same-t entries give
    B, the different-t entries give eta4 (x) S, and the relative sign of each
    spatial block against the reference block gives eta4's diagonal.
    """
    D0 = build_dirac_4d_apbc(2, Lt, 1.0, 0.0)
    same_t = [
        np.array([[D0[a * Lt + t, b * Lt + t] for b in range(NS)] for a in range(NS)])
        for t in range(Lt)
    ]
    t_dev = max(float(np.max(np.abs(same_t[t] - same_t[0]))) for t in range(Lt))
    B = same_t[0]

    diff_t = D0.copy()
    for a in range(NS):
        for b in range(NS):
            for t in range(Lt):
                diff_t[a * Lt + t, b * Lt + t] = 0.0
    off_dev = 0.0
    for a in range(NS):
        for b in range(NS):
            if a != b:
                blk = diff_t[a * Lt:(a + 1) * Lt, b * Lt:(b + 1) * Lt]
                off_dev = max(off_dev, float(np.max(np.abs(blk))))
    blocks = [diff_t[a * Lt:(a + 1) * Lt, a * Lt:(a + 1) * Lt] for a in range(NS)]
    S = blocks[0]
    pivot = np.unravel_index(np.argmax(np.abs(S)), S.shape)
    signs = [blocks[a][pivot] / S[pivot] for a in range(NS)]
    ratio_dev = max(float(np.max(np.abs(blocks[a] - signs[a] * S))) for a in range(NS))
    imag_dev = max(float(np.max(np.abs(M.imag))) for M in (B, S, np.array(signs)))

    Bi = np.rint(B.real).astype(np.int64)
    eta = np.rint(np.real(np.array(signs))).astype(np.int64)
    int_dev = max(float(np.max(np.abs(B.real - Bi))),
                  float(np.max(np.abs(np.real(np.array(signs)) - eta))))
    return {
        "B": Bi, "eta": eta, "S": S.real, "t_dev": t_dev, "off_dev": off_dev,
        "ratio_dev": ratio_dev, "imag_dev": imag_dev, "int_dev": int_dev,
    }


def shift_from_S(S: np.ndarray) -> np.ndarray:
    """Signed cyclic shift T read off the forward entries of the extracted S."""
    Lt = S.shape[0]
    T = np.zeros((Lt, Lt), dtype=np.int64)
    for t in range(Lt):
        T[t, (t + 1) % Lt] = int(np.sign(S[t, (t + 1) % Lt]))
    return T


def direction_hops(B: np.ndarray):
    """Split B into the three single-coordinate hops, by coordinate pairs."""
    hops = []
    for bit in (4, 2, 1):  # x0, x1, x2 in the (((x0)*2+x1)*2+x2) packing
        A = np.zeros((NS, NS), dtype=np.int64)
        for a in range(NS):
            A[a, a ^ bit] = B[a, a ^ bit]
        hops.append(A)
    return hops


def part0a_structural_extraction():
    print("\nPART 0: GENERAL-L_t DERIVATION FROM THE MATRIX")
    print(f"0A structural extraction from build_dirac_4d_apbc, Lt in {EXTRACT_LT}")
    ex = {Lt: extract_operators(Lt) for Lt in EXTRACT_LT}
    ref = ex[EXTRACT_LT[0]]
    b_dev = max(float(np.max(np.abs(ex[Lt]["B"] - ref["B"]))) for Lt in EXTRACT_LT)
    e_dev = max(float(np.max(np.abs(ex[Lt]["eta"] - ref["eta"]))) for Lt in EXTRACT_LT)
    check("same-t 8x8 block is t-independent and Lt-independent, giving B_ext",
          max(ex[Lt]["t_dev"] for Lt in EXTRACT_LT) == 0.0 and b_dev == 0.0
          and max(ex[Lt]["imag_dev"] + ex[Lt]["int_dev"] for Lt in EXTRACT_LT) == 0.0,
          "max dev over t, over Lt, and from integer values all = 0.0")
    check("different-t part is spatial-block-diagonal and equals kron(eta4_ext, S_ext)",
          max(ex[Lt]["off_dev"] + ex[Lt]["ratio_dev"] for Lt in EXTRACT_LT) == 0.0
          and e_dev == 0.0,
          "off-block max = 0.0, block-vs-reference ratio max dev = 0.0")
    coord = np.array([(-1) ** (((a >> 2) & 1) + ((a >> 1) & 1) + (a & 1)) for a in range(NS)])
    check("eta4_ext read off the blocks equals diag((-1)^(x0+x1+x2))",
          bool(np.array_equal(ref["eta"], coord)),
          f"read {ref['eta'].tolist()}")

    u0s, ms = [0.6, 1.0, 1.7], [0.0, 0.37]
    worst, rejector, rows = 0.0, math.inf, []
    for Lt in EXTRACT_LT:
        Bm, Em, Sm = ex[Lt]["B"], np.diag(ex[Lt]["eta"]), ex[Lt]["S"]
        for u0 in u0s:
            for m in ms:
                D = build_dirac_4d_apbc(2, Lt, u0, m)
                base = m * np.eye(NS * Lt) + u0 * np.kron(Bm, np.eye(Lt))
                dev = float(np.max(np.abs(D - (base + u0 * np.kron(Em, Sm)))))
                rej = float(np.max(np.abs(D - (base + u0 * np.kron(np.eye(NS), Sm)))))
                worst, rejector = max(worst, dev), min(rejector, rej)
                rows.append(f"    Lt={Lt} u0={u0} m={m}: dev={dev:.3e} rejector={rej:.3e}")
    npts = len(EXTRACT_LT) * len(u0s) * len(ms)
    check("m*Id + u0*kron(B_ext,Id) + u0*kron(eta4_ext,S_ext) == build_dirac_4d_apbc",
          worst == 0.0,
          f"{npts} points, u0 in {u0s} x m in {ms}, max abs dev = {worst!r}",
          "\n".join(rows))
    check("rejector: replacing eta4_ext by the identity does not reproduce the matrix",
          rejector > 0.0,
          f"smallest max abs dev over the {npts} points = {rejector:.2e}",
          "\n".join(rows))
    return ref


def part0b_clifford(ref):
    print("0B exact Clifford relations on the extracted operators (integer arithmetic)")
    B, eta = ref["B"], np.diag(ref["eta"])
    Id = np.eye(NS, dtype=np.int64)
    A = direction_hops(B)
    check("A_1+A_2+A_3 == B_ext, A_i^2 == -Id_8, and A_iA_j+A_jA_i == 0 for i != j",
          np.max(np.abs(A[0] + A[1] + A[2] - B)) == 0
          and all(np.max(np.abs(a @ a + Id)) == 0 for a in A)
          and all(np.max(np.abs(A[i] @ A[j] + A[j] @ A[i])) == 0
                  for i in range(3) for j in range(i + 1, 3)),
          "all seven deviations = 0; the 2-site antiperiodic ring gives T_i^2 = -Id")
    check("B_ext^2 == -3*Id_8 and trace(B_ext) == 0",
          np.max(np.abs(B @ B + 3 * Id)) == 0 and int(np.trace(B)) == 0)
    check("eta4_ext^2 == Id_8 and trace(eta4_ext) == 0",
          np.max(np.abs(eta @ eta - Id)) == 0 and int(np.trace(eta)) == 0)
    check("B_ext*eta4_ext + eta4_ext*B_ext == 0",
          np.max(np.abs(B @ eta + eta @ B)) == 0)


def part0c_temporal_spectrum():
    print(f"0C temporal spectrum, symbolic and exact, Lt = {SPECTRUM_LT[0]}..{SPECTRUM_LT[-1]}")
    lam, z = sp.Symbol("lam"), sp.Symbol("z")
    rec_dev, cp_ok, sf_ok, root_ok, ev_ok, rows = 0.0, True, True, True, True, []
    for Lt in SPECTRUM_LT:
        S = extract_operators(Lt)["S"]
        T = shift_from_S(S)
        rec_dev = max(rec_dev, float(np.max(np.abs(T @ T.T - np.eye(Lt)))),
                      float(np.max(np.abs(0.5 * (T - T.T) - S))))
        Tsym = sp.Matrix(T.tolist())
        cp_ok &= Tsym.charpoly(lam) == sp.Poly(lam**Lt + 1, lam)
        p = sp.Poly(lam**Lt + 1, lam)
        sf_ok &= sp.gcd(p, p.diff(lam)) == sp.Poly(1, lam)
        root_ok &= all(sp.exp(sp.I * (2 * n + 1) * sp.pi / Lt) ** Lt + 1 == 0
                       for n in range(Lt))
        v = sp.Matrix([z**t for t in range(Lt)])
        Ssym = sp.Matrix([[sp.Rational(int(round(2 * S[i, j])), 2) for j in range(Lt)]
                          for i in range(Lt)])
        r1 = [sp.rem(sp.expand(e), z**Lt + 1, z) for e in (Tsym * v - z * v)]
        r2 = [sp.rem(sp.expand(sp.cancel(z * e)), z**Lt + 1, z)
              for e in (Ssym * v - ((z - 1 / z) / 2) * v)]
        this_ev = all(e == 0 for e in r1) and all(e == 0 for e in r2)
        ev_ok &= this_ev
        rows.append(f"    Lt={Lt} charpoly={Tsym.charpoly(lam).as_expr()} "
                    f"shift_dev={float(np.max(np.abs(0.5 * (T - T.T) - S)))} eigvec={this_ev}")
    check("T_ext read off S_ext is a signed cyclic shift with (1/2)(T-T^-1) == S_ext",
          rec_dev == 0.0,
          f"{len(SPECTRUM_LT)} values of Lt, max abs dev = {rec_dev!r}", "\n".join(rows))
    check("charpoly(T_ext) == lam^Lt + 1 exactly for every Lt in the range",
          cp_ok, fail_detail="\n".join(rows))
    check("lam^Lt + 1 is squarefree, so its Lt roots exp(i(2n+1)pi/Lt) are distinct",
          sf_ok and root_ok,
          "gcd(p, p') == 1 and all Lt roots annihilate p, for every Lt")
    check("S_ext v(z) == ((z-1/z)/2) v(z) on the T_ext eigenvector v(z) = [1,z,..,z^(Lt-1)]",
          ev_ok,
          "residues reduced mod z^Lt + 1 vanish for every Lt; z^Lt = -1 closes the ring",
          "\n".join(rows))
    w = sp.Symbol("w", real=True)
    check("(z - 1/z)/2 == i*sin(omega) at z = exp(i*omega), so S -> i sin(omega)",
          sp.simplify((sp.exp(sp.I * w) - sp.exp(-sp.I * w)) / 2 - sp.I * sp.sin(w)) == 0)
    flat = [Lt for Lt in SPECTRUM_LT
            if all(sp.simplify(sp.sin(sp.Rational(2 * n + 1, Lt) * sp.pi) ** 2 - 1) == 0
                   for n in range(Lt))]
    check("Lt = 2 is the only APBC extent whose temporal modes all have sin^2 omega = 1",
          flat == [2],
          f"exact over Lt = {SPECTRUM_LT[0]}..{SPECTRUM_LT[-1]}; maximal-gap extents = {flat}")


def part0d_symbolic_multiplicity(ref):
    print("0D symbolic multiplicity-four theorem in (theta, u0, m): one computation, every Lt")
    t_start = time.time()
    theta = sp.Symbol("theta", real=True)
    u0 = sp.Symbol("u0", positive=True)
    m = sp.Symbol("m", real=True)
    lam = sp.Symbol("lam")
    K = u0 * (sp.Matrix(ref["B"].tolist())
              + sp.I * sp.sin(theta) * sp.Matrix(np.diag(ref["eta"]).tolist()))
    c = 3 + sp.sin(theta) ** 2
    check("K(theta)^2 == -u0^2*(3 + sin^2 theta)*Id_8 and trace K(theta) == 0",
          sp.simplify(K**2 + u0**2 * c * sp.eye(NS)) == sp.zeros(NS, NS)
          and sp.simplify(K.trace()) == 0,
          "traceless, square a negative multiple of Id_8, so the spectrum is +-i*sqrt(c)")
    const, factors = sp.factor_list(K.charpoly(lam).as_expr())
    mult = {sp.simplify(f - (lam**2 + u0**2 * c)) == 0: k for f, k in factors}.get(True)
    check("charpoly(K) factors as (lam^2 + u0^2*(3 + sin^2 theta))^mult with mult == 4",
          const == 1 and len(factors) == 1 and mult == 4,
          f"factor_list returned multiplicity {mult}; tracelessness forces the 4+4 split")

    det_expr = (m * sp.eye(NS) + K).det()
    pt = {theta: sp.Rational(3, 10), u0: sp.Rational(11, 10), m: sp.Rational(1, 2)}

    def residual(cand):
        d = sp.expand(det_expr - sp.expand(cand))
        return d, abs(complex(sp.N(d.subs(pt))))

    d4, _ = residual((m**2 + u0**2 * c) ** 4)
    check("det(m*Id_8 + K(theta)) == (m^2 + u0^2*(3 + sin^2 theta))^4",
          d4 == 0, "symbolic identity in theta, u0, m; holds for every temporal mode")
    for label, cand in (
        ("exponent 3", (m**2 + u0**2 * c) ** 3),
        ("exponent 5", (m**2 + u0**2 * c) ** 5),
        ("2 + sin^2 theta in place of 3 + sin^2 theta", (m**2 + u0**2 * (2 + sp.sin(theta) ** 2)) ** 4),
    ):
        d, val = residual(cand)
        check(f"rejector: {label} does not reproduce the block determinant",
              d != 0 and val > 1e-6,
              f"residual at (theta,u0,m) = (0.3,1.1,0.5) is {val:.4g}")
    print(f"  symbolic section wall time = {time.time() - t_start:.1f} s")
    return sp.lambdify((theta, u0, m), (m**2 + u0**2 * c) ** 4, "math")


def part0e_close_the_loop(block_det):
    print("0E closing the loop to the runner's own exact_det_formula")
    Lts, u0s, ms = [2, 4, 6, 8], [0.6, 0.9, 1.2], [0.0, 0.1, 0.5]
    max_rel, rows = 0.0, []
    for Lt in Lts:
        for u0 in u0s:
            for m in ms:
                prod = 1.0
                for w in temporal_modes(Lt):
                    prod *= block_det(w, u0, m)
                ref = exact_det_formula(Lt, u0, m)
                rel = abs(prod - ref) / ref
                max_rel = max(max_rel, rel)
                rows.append(f"    Lt={Lt} u0={u0} m={m}: rel={rel:.3e}")
    check("prod_n [symbolic block det at omega_n] == exact_det_formula",
          max_rel < 1e-13,
          f"Lt in {Lts} x u0 in {u0s} x m in {ms}, {len(rows)} points, max rel dev = {max_rel:.1e}",
          "\n".join(rows))


def test_closed_form_determinant():
    print("\nPART 1: CLOSED-FORM DETERMINANT")

    Ls = 2
    Lts, u0s, ms = [2, 4, 6, 8], [0.6, 0.9, 1.2], [0.0, 0.1, 0.5]
    max_rel, rows = 0.0, []
    for Lt in Lts:
        for u0 in u0s:
            for m in ms:
                D = build_dirac_4d_apbc(Ls, Lt, u0, m)
                direct = abs(np.linalg.det(D))
                exact = exact_det_formula(Lt, u0, m)
                rel = abs(direct - exact) / exact
                max_rel = max(max_rel, rel)
                rows.append(f"    Lt={Lt}, u0={u0:.1f}, m={m:.1f}: direct={direct:.8e}, "
                            f"exact={exact:.8e}, rel={rel:.2e}")
    check("exact Matsubara determinant formula matches direct determinant",
          max_rel < 1e-10,
          f"Lt in {Lts} x u0 in {u0s} x m in {ms}, {len(rows)} points, "
          f"max rel dev = {max_rel:.2e}",
          "\n".join(rows))


def test_closed_form_intensive_observables():
    print("\nPART 2: CLOSED-FORM FREE-ENERGY AND CONDENSATE DENSITIES")

    Ls = 2
    u0 = 0.9
    Lts, ms = [2, 4, 6, 8, 10], [1e-3, 1e-2, 0.1]
    max_f = 0.0
    max_c = 0.0
    rows = []
    for Lt in Lts:
        D0 = build_dirac_4d_apbc(Ls, Lt, u0, 0.0)
        ld0 = np.linalg.slogdet(D0)[1]
        n = Ls**3 * Lt
        for m in ms:
            Dm = build_dirac_4d_apbc(Ls, Lt, u0, m)
            ldm = np.linalg.slogdet(Dm)[1]
            direct_f = (ldm - ld0) / n
            exact_f = exact_free_energy_density(Lt, u0, m)
            direct_c = float(np.trace(np.linalg.inv(Dm)).real / n)
            exact_c = exact_condensate_density(Lt, u0, m)
            err_f = abs(direct_f - exact_f)
            err_c = abs(direct_c - exact_c)
            max_f = max(max_f, err_f)
            max_c = max(max_c, err_c)
            rows.append(f"    Lt={Lt}, m={m:g}: f_direct={direct_f:.10e}, f_exact={exact_f:.10e}, "
                        f"c_direct={direct_c:.10e}, c_exact={exact_c:.10e}")
    print(f"  grid: Lt in {Lts} x u0 = {u0} x m in {ms}, {len(rows)} points; "
          "log|det| taken with slogdet")
    check("exact free-energy density formula matches direct computation",
          max_f < 1e-12, f"max abs dev = {max_f:.2e}", "\n".join(rows))
    check("exact condensate density formula matches direct computation",
          max_c < 1e-12, f"max abs dev = {max_c:.2e}", "\n".join(rows))


def test_uv_endpoint_interpretation():
    print("\nPART 3: UV ENDPOINT INTERPRETATION")

    u0 = 0.9
    mass = 1e-2

    cond2 = exact_condensate_density(2, u0, mass)
    cond10 = exact_condensate_density(10, u0, mass)
    ratio = cond10 / cond2
    root4 = ratio ** (-1 / 4)
    root16 = ratio ** (-1 / 16)
    alpha_bare = 1.0 / (4.0 * math.pi)
    m_planck = 1.2209e19
    hierarchy_u0 = 0.5934 ** 0.25
    alpha_lm = alpha_bare / hierarchy_u0
    c_obs = 246.22 / (m_planck * alpha_lm**16)

    print(f"  u0={u0}, m={mass:g}: cond(Lt=2)={cond2:.8f}, cond(Lt=10)={cond10:.8f}, "
          f"R={ratio:.8f}")
    print(f"  C_obs={c_obs:.8f}, R^(-1/4)={root4:.8f}, R^(-1/16)={root16:.8f}")

    check("dimension-4 compression is closer to the observed hierarchy prefactor "
          "than 16th-root compression",
          abs(root4 - c_obs) < abs(root16 - c_obs),
          f"|root4-C_obs|={abs(root4-c_obs):.6f}, |root16-C_obs|={abs(root16-c_obs):.6f}")


def main():
    print("Hierarchy Matsubara decomposition")
    ref = part0a_structural_extraction()
    part0b_clifford(ref)
    part0c_temporal_spectrum()
    block_det = part0d_symbolic_multiplicity(ref)
    part0e_close_the_loop(block_det)
    test_closed_form_determinant()
    test_closed_form_intensive_observables()
    test_uv_endpoint_interpretation()
    print(f"\nSCORECARD: {PASS_COUNT} pass, {FAIL_COUNT} fail out of {PASS_COUNT + FAIL_COUNT}")
    sys.exit(1 if FAIL_COUNT else 0)


if __name__ == "__main__":
    main()
