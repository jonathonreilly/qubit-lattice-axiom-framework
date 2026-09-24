#!/usr/bin/env python3
"""Delay of the rate field with the curvature member: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j6a3f
(claude-opus-5-5).

Objects (block 62, PR #8592; block 60, #8590; block 67, #8598): the second-order member F2 = -K wbar (u R1 + R2), the kinetic term
(1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2] with no rate of change of a rate, the coupling -e u; a slow packet's wave vector obeys
dk/dt = -E grad u (block 54). Exact parts: the full 7 x 7 pencil s^2 M + V solved over Q(s), rotation invariance, continuum kernel
identities. One floating-point control on a periodic box, labelled.
"""
from __future__ import annotations

import json
import subprocess
import sys

import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R = sp.Rational
NOTES = [
    ("b62", "aada579459", "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_"
     "FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["R_1 = -(p_i p_j h_ij - p^2 h), R_2 = -(1/4) p^2 h_ij h_ij + (1/2)(p_i h_ij)^2 - (1/2)(p_i h_ij p_j) h + (1/4) p^2 h^2, "
      "F_2 = -K wbar (u R_1 + R_2)",
      "(T4) With the kinetic term (1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2]"]),
    ("b67", "3bea45f6d8", "docs/ADMISSIBILITY_RULE_A_FORMATION_EVENT_IN_THE_CURVATURE_MEMBER_THE_LEDGER_CAN_ALWAYS_BE_KEPT_AND_THEN_THE_CLOCKS_"
     "FAR_FIELD_JUMPS_AT_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
     ["(b) With the ledger kept the monopole is unchanged and the dipole changes by `Q'(y − X̄)`",
      "Block 60 T5: for every kinetic term holding no rate of change of a rate, the rates and the isotropic lengths follow the content "
      "at the same label time."]),
    ("a1", "a5a9cf0861", "probes/work/derive/delay-of-the-rate-field-with-the-curvature-member/w-jonathonsmac4f50-j03c0/ATTEMPT.md",
     ["`u(k,t) = −e(k,t)/(4K w̄ p²) + α(α+3β) ë(k,t)/(K² w̄³ (α+β) p⁴)`"]),
]
TASK_Q = ["HIT if a packet's fall changes before the strains' wave arrives AND the change depends on the body's energy"]


def family_q() -> None:
    miss = []
    for tag, sha, path, qs in NOTES:
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict)
                 and t.get("id") == "J:derive:delay-of-the-rate-field-with-the-curvature-member:a2"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"blocks 62 and 67 (PR heads), attempt 1's law (ai/probes a5a9cf08) and the task quoted verbatim (6 lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


s = sp.Symbol("s")
hs = sp.symbols("h11 h22 h33 h12 h13 h23")
u = sp.Symbol("u")


def hmat(v):
    return sp.Matrix([[v[0], v[3], v[4]], [v[3], v[1], v[5]], [v[4], v[5], v[2]]])


def member(p, H):
    p2 = (p.T * p)[0]
    tr = H.trace()
    R1 = -((p.T * H * p)[0] - p2 * tr)
    ph = H * p
    R2 = -R(1, 4) * p2 * sum(H[i, j] ** 2 for i in range(3) for j in range(3)) + R(1, 2) * (ph.T * ph)[0] \
        - R(1, 2) * (p.T * H * p)[0] * tr + R(1, 4) * p2 * tr ** 2
    return R1, R2, p2


def pencil(pv, al, be, K, w):
    p = sp.Matrix(pv)
    H = hmat(hs)
    R1, R2, p2 = member(p, H)
    F2 = -K * w * (u * R1 + R2)
    xs = list(hs) + [u]
    dv = sp.symbols("d0:6")
    Hd = hmat(dv)
    T = (al * sum(Hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * Hd.trace() ** 2) / w
    M = sp.zeros(7, 7)
    for a in range(6):
        for b in range(6):
            M[a, b] = sp.diff(T, dv[a], dv[b])
    V = sp.Matrix(7, 7, lambda a, b: sp.diff(F2, xs[a], xs[b]))
    return M, V, p2


# ------------------------------------------------------------------------------------------------ A: the clock's transfer function
def family_a() -> None:
    ok = True
    n = 0
    for pv in ([0, 0, 1], [1, 2, 2], [R(1, 3), 1, 2], [R(2, 5), R(-1, 2), R(3, 4)]):
        for (al, be, K, w) in ((R(1), R(1, 2), R(1), R(1)), (R(2), R(-1, 3), R(3), R(1, 2)), (R(1, 4), R(1, 5), R(7, 3), R(2))):
            M, V, p2 = pencil(pv, al, be, K, w)
            A = s ** 2 * M + V
            b = sp.zeros(7, 1)
            b[6] = -1                                           # L = T - F2 - e u: (s^2 M + V) x = -e e_u
            dom = QQ.frac_field(s)
            x = DomainMatrix.from_Matrix(A).convert_to(dom).lu_solve(DomainMatrix.from_Matrix(b).convert_to(dom))
            Hs = sp.cancel(dom.to_sympy(x[6, 0].element))
            want = -1 / (4 * K * w * p2) + al * (al + 3 * be) * s ** 2 / (K ** 2 * w ** 3 * (al + be) * p2 ** 2)
            ok &= sp.simplify(Hs - want) == 0 and sp.denom(sp.together(Hs)).free_symbols == set()
            n += 1
    # every parameter symbolic, p = P z (rotation invariance, family O, carries it to every p)
    alS, beS, KS, wS, PS = sp.symbols("alpha beta K wbar P")
    M, V, p2 = pencil([0, 0, PS], alS, beS, KS, wS)
    b = sp.zeros(7, 1)
    b[6] = -1
    dom = QQ.frac_field(s, alS, beS, KS, wS, PS)
    x = DomainMatrix.from_Matrix(s ** 2 * M + V).convert_to(dom).lu_solve(DomainMatrix.from_Matrix(b).convert_to(dom))
    Hs = sp.cancel(dom.to_sympy(x[6, 0].element))
    want = -1 / (4 * KS * wS * p2) + alS * (alS + 3 * beS) * s ** 2 / (KS ** 2 * wS ** 3 * (alS + beS) * p2 ** 2)
    ok &= sp.simplify(Hs - want) == 0
    check("A", ok, f"the full 7 x 7 pencil (six strains and u, no mode split) solved over Q(s): symbolically in alpha, beta, K, wbar, P at "
          f"p = P z, and at {n} rational points (four wave vectors, three parameter sets): u/e = -1/(4K wbar p^2) + alpha(alpha + 3beta) s^2/"
          "(K^2 wbar^3 (alpha + beta) p^4), a polynomial in s - no pole, so no retarded part: the clock follows e and its second "
          "derivative at the same label time")


# ------------------------------------------------------------------------------------------------ O: rotation invariance of the member and the kinetic term
def family_o() -> None:
    a, b_, c = R(1, 3), R(-1, 2), R(1, 5)
    Aa = sp.Matrix([[0, -c, b_], [c, 0, -a], [-b_, a, 0]])
    Q = (sp.eye(3) - Aa) * (sp.eye(3) + Aa).inv()               # a rational rotation (Cayley)
    ok = sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3, 3) and Q.det() == 1
    p = sp.Matrix(sp.symbols("p1:4"))
    H = hmat(hs)
    R1, R2, _ = member(p, H)
    R1r, R2r, _ = member(Q * p, Q * H * Q.T)
    ok &= sp.expand(R1 - R1r) == 0 and sp.expand(R2 - R2r) == 0
    Hd = hmat(sp.symbols("d0:6"))
    Tk = lambda X: sum(X[i, j] ** 2 for i in range(3) for j in range(3)), lambda X: X.trace() ** 2
    ok &= sp.expand(Tk[0](Hd) - Tk[0](Q * Hd * Q.T)) == 0 and sp.expand(Tk[1](Hd) - Tk[1](Q * Hd * Q.T)) == 0
    check("O", ok, "R1, R2 and both kinetic invariants are unchanged under p -> Qp, h -> Q h Q^T for a rational rotation Q, so the "
          "transfer function depends on p only through p^2 (A's non-axis points are consistent with this)")


# ------------------------------------------------------------------------------------------------ K: the two kernels and a ledger-kept source
def family_k() -> dict:
    x, y, z = sp.symbols("x y z", real=True)
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
    G = 1 / (4 * sp.pi * r)                                     # 1/p^2
    B = -r / (8 * sp.pi)                                        # 1/p^4: Laplacian of B is -G
    ok = sp.simplify(lap(G)) == 0 and sp.simplify(lap(B) + G) == 0
    Dx, Dy, Dz = sp.symbols("D_x D_y D_z")
    D = sp.Matrix([Dx, Dy, Dz])
    X = sp.Matrix([x, y, z])
    grad = lambda f: sp.Matrix([sp.diff(f, v) for v in (x, y, z)])
    # a source with zero total and dipole D: kernel * source -> -D . grad(kernel) at large r
    dipB = -(D.T * grad(B))[0]
    ok &= sp.simplify(dipB - (D.T * X)[0] / (8 * sp.pi * r)) == 0            # u_B ~ C Ddd.rhat/(8 pi): no decay
    hessB = sp.Matrix(3, 3, lambda i, j: sp.diff(B, (x, y, z)[i], (x, y, z)[j]))
    ok &= sp.simplify(hessB + (sp.eye(3) - X * X.T / r ** 2) / (8 * sp.pi * r)) == sp.zeros(3, 3)
    mem = grad(dipB)                                            # grad(B * Delta e) for the jump of the source
    want = (D - X * (D.T * X)[0] / r ** 2) / (8 * sp.pi * r)
    ok &= sp.simplify(mem - want) == sp.zeros(3, 1)
    dipG = -(D.T * grad(G))[0]
    ok &= sp.simplify(dipG - (D.T * X)[0] / (4 * sp.pi * r ** 3)) == 0
    check("K", ok, "continuum kernels: G = 1/(4 pi r) for 1/p^2, B = -r/(8 pi) for 1/p^4 (lap B = -G); for a jump of the content with no "
          "monopole and dipole D (a ledger-kept event): Poisson part D.rhat/(4 pi r^2) (force ~ r^-3), B part D.rhat/(8 pi) with no decay "
          "(force ~ 1/r), and grad(B * Delta e) = (D - (D.rhat) rhat)/(8 pi r)")
    return {}


# ------------------------------------------------------------------------------------------------ F: floating-point control on a periodic box
def family_f() -> None:
    n = 96
    k = 2 * np.pi * np.fft.fftfreq(n)
    KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
    p2 = 4 * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2 + np.sin(KZ / 2) ** 2)
    p2[0, 0, 0] = 1.0
    src = np.zeros((n, n, n))
    src[1, 0, 0], src[-1, 0, 0] = 0.5, -0.5                      # zero total, dipole D = (1, 0, 0)
    sh = np.fft.fftn(src)
    Bk = sh / p2 ** 2
    Bk[0, 0, 0] = 0
    field = np.real(np.fft.ifftn(Bk))
    res = []
    for d in (8, 12, 16):
        # transverse point (0, d, 0): continuum grad_x of (B * src) is (D_x)/(8 pi d)
        gx = (field[1, d, 0] - field[-1, d, 0]) / 2
        res.append(gx * 8 * np.pi * d)
    xs = np.array([8, 12, 16]) / n
    slope, icpt = np.polyfit(xs, np.array(res), 1)
    ok = abs(icpt - 1) < 0.05 and slope < 0
    check("F", ok, "floating point, periodic 96^3 box, lattice kernel 1/p^4 with p^2 = sum 4 sin^2(k/2): the transverse gradient of B * "
          f"(dipole) at distance d, times 8 pi d, is {', '.join(f'{v:.3f}' for v in res)} at d = 8, 12, 16; the images of the long-range "
          f"kernel shift it linearly in d/L, and the line through the three points meets d/L = 0 at {icpt:.3f} (continuum value 1)")


def main() -> int:
    family_q()
    family_a()
    family_o()
    family_k()
    family_f()
    print("Delay of the rate field with the curvature member - checks; worker w-macbookpro9927a-j6a3f (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact: (1) solving block 62's full pencil without a mode split, the clock's transfer function is "
          "u/e = -1/(4K wbar p^2) + C s^2/p^4, C = alpha(alpha + 3beta)/(K^2 wbar^3 (alpha + beta)), a polynomial in s: no retarded part; "
          "(2) for a formation event that keeps the ledger (block 67: no monopole, dipole jump D = Q'(y - Xbar)), a slow packet at distance r "
          "feels at once the dipole force of the Poisson part (~ r^-3), and while the content is being rearranged the C-term's force "
          "~ E C Ddd/(8 pi r), which leaves a permanent displacement -(E C/m*)(D - (D.rhat)rhat)/(8 pi r): a memory falling only as 1/r, "
          "all before any transverse wave arrives")
    print("HIT: with block 62's kinetic term the curvature member's clock law is u = -e/(4K wbar p^2) + C ddot(e)/p^4 with no retarded part "
          "(re-derived from the full pencil); even a formation event that keeps the ledger moves every distant slow packet at once - "
          "through its dipole jump D = Q'(y - Xbar) - and leaves a permanent 1/r displacement -(E C/m*)(D - (D.rhat) rhat)/(8 pi r)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
