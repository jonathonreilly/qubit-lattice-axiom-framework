#!/usr/bin/env python3
"""The zero-field floor sharpened, attempt 1: checks for ATTEMPT.md (worker w-macbookpro9927a-ja8d2, claude-opus-5-5).

Setting (block 92 on its PR branch, head 3e26092f3c): the sphere ferromagnet prod_edges e^{beta s.s'} on block 90's bilayer
torus, zero field; D = sum_u c_u L_u (c_u = e^{ik.x_u}, L_u the rotation of s_u about e2, L s = e2 x s = (s3, 0, -s1));
A = sum_u conj(c_u) s_u (a complex 3-vector), m = V^-1 sum_u s_u, M^2 = <|m|^2>, u(k) = V^-1 <|A_1|^2>.

Claim: with F = (m x A)_2 = A_1 m_3 - A_3 m_1 (attempt a2's choice) and the weight w = |m|^2 INSIDE Cauchy-Schwarz,
    |<DF>|^2 = beta^2 |<F DH>|^2 <= beta^2 <|F|^2/w> <w|DH|^2>,
where the extra term of the second integration by parts, <(Dbar w) DH>, is -2/V <F DH>, i.e. again <DF>. The algebra closes:
    u(k) >= (4/9) M^2 / (beta E(k) + 4/(3V))      (linear in M^2; an equality at beta = 0 for every V).
Everything below is exact (sympy, fractions) except family M, a floating Monte Carlo control that is not a proof.
"""
from __future__ import annotations

import itertools
import math
import subprocess
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ----------------------------------------------------------------------------------------------------------------------
# Family S: the derivation identities on a symbolic configuration (a bilayer of two 3-rings with rungs, V = 6)

def family_s() -> None:
    I = sp.I
    V = 6
    # unit phases (rational points), equal across each rung; the identities need only |c_u| = 1
    ph = [sp.Rational(1), sp.Rational(3, 5) + I * sp.Rational(4, 5), sp.Rational(-7, 25) + I * sp.Rational(24, 25)]
    c = ph + ph
    X = sp.symbols("x0:6", real=True); Y = sp.symbols("y0:6", real=True); Z = sp.symbols("z0:6", real=True)
    edges = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5)]

    def Dop(f, cc):   # sum_u cc_u L_u f with L s = (s3, 0, -s1): z d/dx - x d/dz
        return sp.expand(sum(cc[u] * (Z[u] * sp.diff(f, X[u]) - X[u] * sp.diff(f, Z[u])) for u in range(V)))

    cb = [sp.conjugate(x) for x in c]
    A1 = sum(cb[u] * X[u] for u in range(V)); A2 = sum(cb[u] * Y[u] for u in range(V)); A3 = sum(cb[u] * Z[u] for u in range(V))
    A1b = sum(c[u] * X[u] for u in range(V)); A3b = sum(c[u] * Z[u] for u in range(V))
    m1, m2, m3 = (sum(v) / V for v in (X, Y, Z))
    F = A1 * m3 - A3 * m1
    w = m1 ** 2 + m2 ** 2 + m3 ** 2
    H = sum(X[a] * X[b] + Y[a] * Y[b] + Z[a] * Z[b] for a, b in edges)
    z = lambda e: sp.simplify(sp.expand(e)) == 0
    ids = {
        "D A1 = V m3": z(Dop(A1, c) - V * m3),
        "D A3 = -V m1": z(Dop(A3, c) + V * m1),
        "D A2 = 0": z(Dop(A2, c)),
        "D m3 = -conj(A1)/V": z(Dop(m3, c) + A1b / V),
        "D m1 = conj(A3)/V": z(Dop(m1, c) - A3b / V),
        "D F = V(m1^2+m3^2) - (|A1|^2+|A3|^2)/V": z(Dop(F, c) - (V * (m1 ** 2 + m3 ** 2) - (A1 * A1b + A3 * A3b) / V)),
        "Dbar w = -2F/V": z(Dop(w, cb) + 2 * F / V),
        "Dbar D H = -sum|c_u-c_v|^2 (x x' + z z')": z(Dop(Dop(H, c), cb)
                                                      + sum(sp.expand((c[a] - c[b]) * (cb[a] - cb[b])) * (X[a] * X[b] + Z[a] * Z[b])
                                                            for a, b in edges)),
        "F = (m x A)_2": z(F - (m3 * A1 - m1 * A3)),
    }
    # |m x A|^2 = |m|^2 |A|^2 - |m.A|^2 for real m and complex A (componentwise symbols)
    mr = sp.symbols("n1:4", real=True); ar = sp.symbols("p1:4", real=True); ai = sp.symbols("q1:4", real=True)
    Av = [ar[i] + I * ai[i] for i in range(3)]
    cr = [mr[1] * Av[2] - mr[2] * Av[1], mr[2] * Av[0] - mr[0] * Av[2], mr[0] * Av[1] - mr[1] * Av[0]]
    lhs = sum(sp.expand(v * sp.conjugate(v)) for v in cr)
    rhs = sum(x * x for x in mr) * sum(sp.expand(v * sp.conjugate(v)) for v in Av) - sp.expand(
        sum(mr[i] * Av[i] for i in range(3)) * sp.conjugate(sum(mr[i] * Av[i] for i in range(3))))
    ids["|m x A|^2 = |m|^2|A|^2 - |m.A|^2"] = z(lhs - rhs)
    bad = [k for k, v in ids.items() if not v]
    check("S1", not bad, "derivation identities on a symbolic bilayer (two 3-rings, 3 rungs, unit rational phases, rungs "
          "joining equal phases): D A1 = V m3, D A3 = -V m1, D A2 = 0, D m3 = -conj(A1)/V, D m1 = conj(A3)/V, "
          "D F = V(m1^2+m3^2) - (|A1|^2+|A3|^2)/V, Dbar|m|^2 = -2F/V, Dbar D H = -sum_edges |c_u-c_v|^2 (x x' + z z') "
          f"(rungs drop out), |m x A|^2 = |m|^2|A|^2 - |m.A|^2 {bad if bad else ''}")


# ----------------------------------------------------------------------------------------------------------------------
# Family R: the rotation average (Schur): a rotation-invariant law gives E|Y_2|^2 = E|Y|^2/3; checked on the octahedral group

def family_r() -> None:
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if M.det() == 1:
                mats.append(M)
    y = sp.Matrix(sp.symbols("y1:4")) + sp.I * sp.Matrix(sp.symbols("w1:4"))
    avg = sp.zeros(3, 3)
    for M in mats:
        v = M * y
        avg += v * v.H
    avg = (avg / len(mats)).applyfunc(sp.expand)
    tr = sp.expand(sum(avg[i, i] for i in range(3)))
    ok = len(mats) == 24 and all(sp.expand(avg[i, j] - (tr / 3 if i == j else 0)) == 0 for i in range(3) for j in range(3))
    check("R1", ok, "the average of (Ry)(Ry)^dag over the 24 proper rotations of the cube is (|y|^2/3) I for a symbolic "
          "complex y: an invariant law gives E|Y_i|^2 = E|Y|^2/3, applied to Y = n x A and to A itself")


# ----------------------------------------------------------------------------------------------------------------------
# Family A: the algebra of the floor, and the first (block-92 F) instance

def family_a() -> None:
    V, E, beta, a, u = sp.symbols("V E beta a u", positive=True)
    X = 2 * (V * a - u)                                      # <DF> for F = (m x A)_2, a = M^2/3
    # |<DF>|^2 <= beta^2 <|F|^2/w> <w|DH|^2> <= beta^2 (V u) (beta^-1 V E (3a) - 2 X/(beta^2 V))
    rhs = sp.expand(beta ** 2 * (V * u) * (V * E * 3 * a / beta - 2 * X / (beta ** 2 * V)))
    ineq = sp.expand(rhs - X ** 2)                           # >= 0
    target = sp.expand(4 * V * a * ((3 * beta * V * E + 4) * u - 4 * V * a) / 4)
    # rhs - X^2 = V a [ (3 beta V E + 4) u - 4 V a ]
    ok1 = sp.simplify(ineq - V * a * ((3 * beta * V * E + 4) * u - 4 * V * a)) == 0
    floor = 4 * V * a / (3 * beta * V * E + 4)
    ok2 = sp.simplify(floor - sp.Rational(4, 3) * a / (beta * E + sp.Rational(4, 3) / V)) == 0
    # block 92's F = A1 m3 with w = m3^2: <DF> = V a - u, <|F|^2/w> = V u, <w> = a
    X1 = V * a - u
    ineq1 = sp.expand(beta ** 2 * (V * u) * (V * E * a / beta - 2 * X1 / (beta ** 2 * V)) - X1 ** 2)
    ok3 = sp.simplify(ineq1 - (beta * V ** 2 * E * a * u + u ** 2 - V ** 2 * a ** 2)) == 0
    # from u^2 + beta V^2 E a u - V^2 a^2 >= 0: u >= 2 V a/(beta V E + sqrt(beta^2 V^2 E^2 + 4)) >= a/(beta E + 1/V)
    root = 2 * V * a / (beta * V * E + sp.sqrt(beta ** 2 * V ** 2 * E ** 2 + 4))
    ok4 = sp.simplify(root ** 2 + beta * V ** 2 * E * a * root - V ** 2 * a ** 2) == 0
    ok5 = sp.simplify(sp.sqrt(beta ** 2 * V ** 2 * E ** 2 + 4) ** 2 - (beta * V * E + 2) ** 2 + 4 * beta * V * E) == 0
    check("A1", ok1 and ok2 and ok3 and ok4 and ok5,
          "algebra: with X = <DF> = 2(Va - u), beta^2 (Vu)(V E 3a/beta - 2X/(beta^2 V)) - X^2 = V a[(3 beta V E + 4)u - 4Va], "
          "so u >= 4Va/(3 beta V E + 4) = (4/9) M^2/(beta E + 4/(3V)); block 92's F with w = m3^2 gives "
          "u^2 + beta V^2 E a u - V^2 a^2 >= 0, whose root is >= a/(beta E + 1/V) = (M^2/3)/(beta E + 1/V) "
          "(sqrt(b^2+4) <= b + 2)")


# ----------------------------------------------------------------------------------------------------------------------
# Family Z: beta = 0, where the floor is an equality for every V

def family_z() -> None:
    ok = True
    for Vn in (2, 6, 16, 128, 1000):
        u0 = Fr(1, 3)                          # independent uniform spins: <s^1 s^1'> = delta/3, |c_u| = 1
        M2 = Fr(1, Vn)                         # <|m|^2> = V^-2 sum_u <|s_u|^2>
        new = Fr(4, 9) * M2 / (Fr(4, 3) / Vn)
        old = (M2 / 3) ** 2 / (Fr(2, 3) / Vn)
        ok &= new == u0 and old < u0
    check("Z1", ok, "beta = 0 (independent spins): u(k) = 1/3 and M^2 = 1/V exactly, and the new floor (4/9)M^2/(4/(3V)) "
          "equals 1/3 for V = 2, 6, 16, 128, 1000: the ratio (4/9)/(4/3) of the constants cannot be raised; block 92's "
          "floor there is 1/(6V)")


# ----------------------------------------------------------------------------------------------------------------------
# Family P: consequences in 3+1 and on planes

def harmonic(n):
    return sum(Fr(1, j) for j in range(1, n + 1))


def family_p() -> None:
    b0 = 0.5905
    rows = []
    for beta in (1, 2, 3, 6):
        f = 1 - b0 / beta
        rows.append((beta, (f / 3) ** 2, 4 * (f / 3) ** 2, 4 * f / 9))
    old_ok = [round(r[1], 4) for r in rows] == [0.0186, 0.0552, 0.0717, 0.0903]
    # planes: shell count sum_{k != 0} |k|^-2 >= (N/pi^2) H_{L/2-1}, exact for L = 4..24 (block 92's family D range)
    shell_ok = True
    for L in range(4, 26, 2):
        tot = Fr(0)
        for n1 in range(-L // 2 + 1, L // 2 + 1):
            for n2 in range(-L // 2 + 1, L // 2 + 1):
                if n1 or n2:
                    tot += Fr(1, n1 * n1 + n2 * n2)
        # sum |k|^-2 = (L^2/(4 pi^2)) sum |n|^-2 >= (L^2/pi^2) H  <=>  sum |n|^-2 >= 4 H
        shell_ok &= tot >= 4 * harmonic(L // 2 - 1)
    # algebra of the plane bound: c M^2 (N/pi^2) H/(beta + 1/(6 pi^2)) <= 2N/3 with c = 4/9
    Mq, N, Hs, beta, pi = sp.symbols("M2 N H beta pi", positive=True)
    Mmax = sp.solve(sp.Eq(sp.Rational(4, 9) * Mq * (N / pi ** 2) * Hs / (beta + 1 / (6 * pi ** 2)), 2 * N / 3), Mq)[0]
    alg_ok = sp.simplify(Mmax - sp.Rational(3, 2) * (pi ** 2 * beta + sp.Rational(1, 6)) / Hs) == 0
    # where it bites (M^2 < 1): H_{L/2-1} > (3/2)(pi^2 beta + 1/6), with pi^2 < 98697/10000
    bite = {}
    for bt in (Fr(1, 10), Fr(3, 10)):
        need = Fr(3, 2) * (Fr(98697, 10000) * bt + Fr(1, 6))
        n, h = 0, Fr(0)
        while h <= need:
            n += 1
            h += Fr(1, n)
        bite[bt] = 2 * (n + 1)
    check("P1", old_ok and shell_ok and alg_ok,
          "3+1: E(k)R(k) >= (4/9)M^2 >= (4/9)(1 - beta_0/beta) in the limit: "
          + ", ".join(f"{r[3]:.4f}" for r in rows) + " at beta = 1, 2, 3, 6 (block 92: "
          + ", ".join(f"{r[1]:.4f}" for r in rows) + "; a2's M^4 floor: " + ", ".join(f"{r[2]:.4f}" for r in rows)
          + "); planes: shell count exact for even L = 4..24, and the sum rule gives M^2 <= (3/2)(pi^2 beta + 1/6)/H_{L/2-1} "
          f"(block 92: M^4 <= (6 pi^2 beta + 1/2)/H), below 1 from L = {bite[Fr(1, 10)]} at beta = 0.1 and "
          f"L = {bite[Fr(3, 10)]} at beta = 0.3")


# ----------------------------------------------------------------------------------------------------------------------
# Family M: executed control (floating Monte Carlo; evidence, not proof)

def mc(d, L, beta, sweeps, seed):
    rng = np.random.default_rng(seed)
    N = L ** d; V = 2 * N
    coords = np.array(np.unravel_index(np.arange(N), (L,) * d)).T
    nbr = np.zeros((V, 2 * d + 1), dtype=int)
    for u in range(V):
        lay, x = divmod(u, N)
        col = 0
        for j in range(d):
            for s in (1, -1):
                cc = coords[x].copy(); cc[j] = (cc[j] + s) % L
                nbr[u, col] = lay * N + np.ravel_multi_index(tuple(cc), (L,) * d); col += 1
        nbr[u, col] = (1 - lay) * N + x
    S = rng.normal(size=(V, 3)); S /= np.linalg.norm(S, axis=1)[:, None]
    k = np.zeros(d); k[0] = 2 * np.pi / L
    phase = np.exp(-1j * (np.concatenate([coords, coords]) @ k))
    us, ms = [], []
    for sw in range(sweeps):
        for u in rng.permutation(V):
            h = beta * S[nbr[u]].sum(axis=0); hn = np.linalg.norm(h)
            a = h / hn; x = rng.random(); ct = 1 + np.log(x + (1 - x) * np.exp(-2 * hn)) / hn
            t1 = np.cross(a, [1, 0, 0] if abs(a[0]) < .9 else [0, 1, 0]); t1 /= np.linalg.norm(t1); t2 = np.cross(a, t1)
            phi = 2 * np.pi * rng.random(); st = math.sqrt(max(0.0, 1 - ct * ct))
            S[u] = ct * a + st * (math.cos(phi) * t1 + math.sin(phi) * t2)
        if sw >= sweeps // 5:
            A = phase @ S; m = S.mean(axis=0)
            us.append(np.mean(np.abs(A) ** 2) / V); ms.append(m @ m)
    return V, 2 - 2 * math.cos(2 * math.pi / L), float(np.mean(us)), float(np.mean(ms))


def family_m() -> None:
    rows = []
    for d, L, beta in ((3, 4, 1.0), (2, 8, 1.0)):
        V, E, u, M2 = mc(d, L, beta, 500, 7)
        rows.append((d, L, beta, u, M2, (4 / 9) * M2 / (beta * E + 4 / (3 * V)), (M2 / 3) ** 2 / (beta * E + 2 / (3 * V))))
    check("M1", all(r[3] > r[5] > r[6] for r in rows), "executed (floating heat bath, 500 sweeps, not a proof): "
          + "; ".join(f"d={r[0]} L={r[1]} beta={r[2]}: u={r[3]:.3f}, M^2={r[4]:.3f}, new floor {r[5]:.3f}, block 92 {r[6]:.4f}"
                      for r in rows))


# ----------------------------------------------------------------------------------------------------------------------
# Family Q: sources

B92 = "3e26092f3c43921e0096c930dad5a8ad1362d4b6"
N92 = ("docs/ADMISSIBILITY_RULE_THE_ZERO_FIELD_BOUND_ON_THE_FORMATION_BILAYER_A_HELD_SOURCES_KERNEL_WITHOUT_A_FIELD_IN_3PLUS1_"
       "AND_NO_MEMORY_ON_PLANES_BOUNDED_THEOREM_NOTE_2026-09-23.md")
A2 = "probes/work/derive/the-zero-field-floor-sharpened/w-jonathonsmac4f50-je12b/ATTEMPT.md"


def family_q() -> None:
    t = subprocess.run(["git", "show", f"{B92}:{N92}"], capture_output=True, text=True).stdout
    a2 = subprocess.run(["git", "show", f"origin/ai/probes:{A2}"], capture_output=True, text=True).stdout
    need92 = ["`u(k) ≥ (M²/3)² / (βE(k) + 2/(3V))`", "`F = A m³`", "`⟨D̄DH⟩ ≤ Σ_{edges}|c_u − c_v|² = V E(k)`",
              "Block 91's response is `R̂(k) = βu(k)`", "`M⁴ ≤ (6π²β + 1/2)/H_{L/2−1}`"]
    needa2 = ["(C) is not proved here.", "weighting the measure by `|m|²` breaks the integration by parts",
              "Take `F = A₁ m₃ − A₃ m₁ = (m × A)₂`."]
    bad = [q[:30] for q in need92 if q not in t] + [q[:30] for q in needa2 if q not in a2]
    check("Q", not bad, f"block 92 at its branch head {B92[:10]} (T1's floor, F = A m^3, the stiffness sum, R = beta u, the "
          "plane bound M^4 <= ...); attempt a2 on ai/probes ('(C) is not proved here', 'weighting the measure by |m|^2 breaks "
          f"the integration by parts', its F = (m x A)_2) {bad if bad else ''}")


def main() -> None:
    t0 = time.time()
    family_q()
    family_s()
    family_r()
    family_a()
    family_z()
    family_p()
    family_m()
    print("\n".join(OUT))
    print(f"TOTAL: PASS={len(OUT) - len(FAILS)} FAIL={len(FAILS)}  ({time.time() - t0:.0f} s)")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return
    print("SUMMARY: PROVED (zero field, finite volume, every beta >= 0, every k != 0, any rung coupling): "
          "u(k) >= (4/9) M^2 / (beta E(k) + 4/(3V)) on block 90's bilayer, linear in M^2. Route: the weight w = |m|^2 sits inside "
          "Cauchy-Schwarz, not in the measure; the second integration by parts produces <(Dbar w) DH> = -(2/V)<F DH>, "
          "which is again <DF>, and the algebra closes with no remainder. Equality at beta = 0 for every V. Consequences: "
          "in 3+1 E(k)R(k) >= (4/9)M^2 >= (4/9)(1 - beta_L/beta) up to 4/(3 beta V) (limit (4/9)(1 - beta_0/beta), against "
          "block 92's ((1 - beta_0/beta)/3)^2); on planes M^2 <= (3/2)(pi^2 beta + 1/6)/H_{L/2-1}. The coefficient 4/9 in "
          "front of beta E is not shown to be best.")
    print("HIT: at zero field on block 90's formation bilayer, for every finite volume, beta >= 0 and k != 0, "
          "u(k) >= (4/9) M^2/(beta E(k) + 4/(3V)) - linear in M^2 and an equality at beta = 0; hence a held source's response "
          "in 3+1 is at least (4/9)(1 - beta_0/beta) of the inverse lattice Laplacian, and on planes "
          "M^2 <= (3/2)(pi^2 beta + 1/6)/H_{L/2-1}")


if __name__ == "__main__":
    main()
