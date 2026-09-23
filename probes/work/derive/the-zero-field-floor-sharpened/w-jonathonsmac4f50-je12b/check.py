#!/usr/bin/env python3
"""the-zero-field-floor-sharpened, attempt 2 (worker w-jonathonsmac4f50-je12b, claude-opus-5-5).

Exact claims: sympy / fractions. Section E is a Monte Carlo control (floating point, labelled [executed]).
Step labels refer to ATTEMPT.md.
"""
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

T0 = time.time()
NP = NF = 0


def ok(label, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        NF += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


# ---------------------------------------------------------------- Step 1: the derivation identities for F = A1 m3 - A3 m1
# symbolic configuration on V = 4 vertices, phases c_u = i^u (a wave vector pi/2 on a ring; |c_u| = 1)
V = 4
S = [[sp.Symbol(f"s{a}_{u}", real=True) for a in (1, 2, 3)] for u in range(V)]
c = [sp.I ** u for u in range(V)]
cb = [sp.conjugate(x) for x in c]


def D(f):
    """D = sum_u c_u L_u, L_u the rotation about e2 at u: L s1 = s3, L s3 = -s1, L s2 = 0 (block 92's convention)"""
    return sp.expand(sum(c[u] * (S[u][2] * sp.diff(f, S[u][0]) - S[u][0] * sp.diff(f, S[u][2])) for u in range(V)))


A = [sum(cb[u] * S[u][a] for u in range(V)) for a in range(3)]
Ab = [sum(c[u] * S[u][a] for u in range(V)) for a in range(3)]
m = [sum(S[u][a] for u in range(V)) / V for a in range(3)]
ok("1.1 D A1 = V m3, D A3 = -V m1, D A2 = 0, D m3 = -Abar1/V, D m1 = Abar3/V (block 92's conventions)",
   sp.simplify(D(A[0]) - V * m[2]) == 0 and sp.simplify(D(A[2]) + V * m[0]) == 0 and sp.simplify(D(A[1])) == 0
   and sp.simplify(D(m[2]) + Ab[0] / V) == 0 and sp.simplify(D(m[0]) - Ab[2] / V) == 0)
F = A[0] * m[2] - A[2] * m[0]
DF_claim = V * (m[0] ** 2 + m[2] ** 2) - (A[0] * Ab[0] + A[2] * Ab[2]) / V
ok("1.2 F = A1 m3 - A3 m1 = (m x A)_2 : DF = V(m1^2 + m3^2) - V^-1(|A1|^2 + |A3|^2) on a symbolic configuration", sp.simplify(D(F) - DF_claim) == 0)
F92 = A[0] * m[2]
ok("1.3 block 92's F = A1 m3 gives DF = V m3^2 - V^-1 |A1|^2 (reproduced)", sp.simplify(D(F92) - (V * m[2] ** 2 - A[0] * Ab[0] / V)) == 0)
# rotation-averaged expectations (zero field): <m_a^2> = M^2/3, <|A_a|^2> = V u  =>  <DF> = 2(V M^2/3 - u), block 92: V M^2/3 - u
# |F|^2 = |(A x m)_2|^2, rotation average = |A x m|^2 / 3 = (|m|^2 |A|^2 - |A.m|^2)/3 = |m|^2 |A_perp|^2 / 3
Ar = sp.symbols("ar1:4", real=True)
Ai = sp.symbols("ai1:4", real=True)
mv = sp.symbols("mv1:4", real=True)
Ac = [Ar[i] + sp.I * Ai[i] for i in range(3)]
cross = [Ac[1] * mv[2] - Ac[2] * mv[1], Ac[2] * mv[0] - Ac[0] * mv[2], Ac[0] * mv[1] - Ac[1] * mv[0]]
lhs = sum(sp.expand(x * sp.conjugate(x)) for x in cross)
m2 = sum(x * x for x in mv)
Adotm = sum(Ac[i] * mv[i] for i in range(3))
rhs = sp.expand(m2 * sum(sp.expand(x * sp.conjugate(x)) for x in Ac) - Adotm * sp.conjugate(Adotm))
ok("1.4 |A x m|^2 = |m|^2 |A|^2 - |A.m|^2 = |m|^2 |A_perp|^2 for complex A (A_perp the part of A orthogonal to m)", sp.simplify(lhs - rhs) == 0)
# rotation average of |X_2|^2 for a vector X: (1/3)|X|^2 (Haar average of a fixed component)
th, ph = sp.symbols("theta phi", real=True)
n = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
avg = sp.integrate(sp.integrate(n[1] ** 2 * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)) / (4 * sp.pi)
ok("1.5 the Haar average of one component squared is 1/3 of the length squared (n_2^2 over the sphere)", avg == sp.Rational(1, 3))

# ---------------------------------------------------------------- Step 2: the quadratic step and the improved floor
a_, x_, b_, Vs = sp.symbols("a x b V", positive=True)  # a = M^2/3, x = u(k), b = beta E(k)
ident = (b_ / 4 + 2 * a_ / Vs) * x_ - a_ ** 2 - ((b_ / 4) * x_ - (a_ - x_ / Vs) ** 2 + x_ ** 2 / Vs ** 2)
ok("2.1 (bE/4 + 2a/V) x - a^2 = (bE/4) x - (a - x/V)^2 + x^2/V^2: from 4(a - x/V)^2 <= bE x follows x >= 4a^2/(bE + 8a/V)", sp.simplify(ident) == 0)
new = 4 * a_ ** 2 / (b_ + 8 * a_ / Vs)
old = a_ ** 2 / (b_ + 2 * a_ / Vs)
ok("2.2 the new floor is 4 x block 92's up to the finite-volume term: new/old -> 4 as V -> oo, and new >= old for every a <= 1/3, V >= 1",
   sp.limit(new / old, Vs, sp.oo) == 4 and sp.simplify(sp.factor(new - old).subs({a_: sp.Rational(1, 3), Vs: 1, b_: 1})) > 0
   and sp.simplify(sp.numer(sp.together(new - old)) - 3 * a_ ** 2 * b_ * Vs ** 2) == 0)
ok("2.3 the floor 4a^2/(bE + 8a/V) is increasing in a, so M^2 >= 1 - beta_L/beta may be inserted", sp.simplify(sp.diff(new, a_)) .equals(
   sp.simplify(4 * a_ * (2 * b_ + 8 * a_ / Vs) / (b_ + 8 * a_ / Vs) ** 2)) and True)
# 3+1: R = beta u >= 4((1 - beta_L/beta)/3)^2/(E + 8/(3 beta V)); limit 4/9 of the inverse Laplacian
b0 = sp.Rational(5905, 10000)
floors_old = [((1 - b0 / sp.Integer(bb)) / 3) ** 2 for bb in (1, 2, 3, 6)]
floors_new = [4 * f for f in floors_old]
ok("2.4 in 3+1 the E(k)R(k) floor becomes 4((1 - beta_0/beta)/3)^2: 0.0745, 0.2207, 0.2867, 0.3613 at beta = 1, 2, 3, 6 (block 92's own values 0.0186, 0.0552, 0.0717, 0.0903 reproduced), limit 4/9",
   [round(float(f), 4) for f in floors_new] == [0.0745, 0.2207, 0.2867, 0.3613] and [round(float(f), 4) for f in floors_old] == [0.0186, 0.0552, 0.0717, 0.0903],
   f"{[round(float(f), 4) for f in floors_new]}")
b4, b6 = Fr(18239, 35840), Fr(27735979, 51891840)
ok("2.5 finite tori (block 90's exact beta_4, beta_6): at beta = 1 the zero-field floors 4((1 - beta_L)/3)^2 are exact rationals",
   4 * ((1 - b4) / 3) ** 2 == Fr(4, 9) * (1 - b4) ** 2 and 4 * ((1 - b6) / 3) ** 2 == Fr(4, 9) * (1 - b6) ** 2,
   f"L=4: {4 * ((1 - b4) / 3) ** 2} ~ {float(4 * ((1 - b4) / 3) ** 2):.4f}; L=6: {float(4 * ((1 - b6) / 3) ** 2):.4f}")

# ---------------------------------------------------------------- Step 3: the linear bound is equivalent to one correlation inequality
# with <|F|^2> = (1/3) E[|m|^2 |A_perp|^2]; if E[|m|^2 |A_perp|^2] <= M^2 E|A_perp|^2 <= M^2 * 3 V u, then 4 V^2 (a - x/V)^2 <= beta * M^2 V x * V E
lin = sp.solve(sp.Eq(4 * (a_ - x_ / Vs) ** 2, b_ * 3 * a_ * x_), x_)
ident2 = (3 * b_ * a_ / 4 + 2 * a_ / Vs) * x_ - a_ ** 2 - ((3 * b_ * a_ / 4) * x_ - (a_ - x_ / Vs) ** 2 + x_ ** 2 / Vs ** 2)
ok("3.1 given (C) E[|m|^2 |A_perp|^2] <= M^2 E|A_perp|^2: 4(a - x/V)^2 <= 3 a bE x, hence x >= a/((3/4) bE + 2/V) = (4/9) M^2/(beta E + 8/(3V)): M^2 to the FIRST power",
   sp.simplify(ident2) == 0 and sp.simplify(a_ ** 2 / (3 * b_ * a_ / 4 + 2 * a_ / Vs) - sp.Rational(4, 3) * a_ / (b_ + sp.Rational(8, 3) / Vs)) == 0)

print(f"exact part done in {time.time() - T0:.1f} s")

# ---------------------------------------------------------------- E: Monte Carlo on block 90's bilayer (floating point, evidence)
rng = np.random.default_rng(20260923)


def bilayer_mc(L, beta, sweeps, therm):
    """O(3) spins on two copies of (Z/L)^3 (nearest-neighbour bonds) plus one rung per site; weight exp(beta s.s') on every edge.
    Checkerboard heat bath on the bipartition parity(x) + layer."""
    s = rng.normal(size=(2, L, L, L, 3))
    s /= np.linalg.norm(s, axis=-1, keepdims=True)
    s[:] = np.array([0, 0, 1.0])  # ordered start
    X, Y, Z = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
    par = (X + Y + Z) % 2
    masks = [np.stack([par == q, par != q]) for q in (0, 1)]  # colour q: layer 0 with parity q, layer 1 with parity 1-q
    kx = 2 * np.pi / L
    ph = np.exp(-1j * kx * X)
    out = []
    for sw in range(sweeps + therm):
        for mk in masks:
            h = np.zeros_like(s)
            for ax in (1, 2, 3):
                h += np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax)
            h += s[::-1]  # rung partner
            hn = np.linalg.norm(h, axis=-1)
            bh = beta * hn
            U = rng.random(hn.shape)
            ct = 1 + np.log1p(-U * (1 - np.exp(-2 * bh))) / bh
            ct = np.clip(ct, -1, 1)
            phi = 2 * np.pi * rng.random(hn.shape)
            e3 = h / hn[..., None]
            tmp = np.where(np.abs(e3[..., :1]) < 0.9, np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
            e1 = np.cross(e3, tmp)
            e1 /= np.linalg.norm(e1, axis=-1, keepdims=True)
            e2 = np.cross(e3, e1)
            st = np.sqrt(1 - ct ** 2)
            new = ct[..., None] * e3 + (st * np.cos(phi))[..., None] * e1 + (st * np.sin(phi))[..., None] * e2
            s = np.where(mk[..., None], new, s)
        if sw >= therm:
            Vv = 2 * L ** 3
            mvec = s.reshape(-1, 3).sum(0) / Vv
            Avec = np.einsum("lxyz,lxyza->a", np.broadcast_to(ph, (2, L, L, L)), s)
            mh = mvec / np.linalg.norm(mvec)
            Aperp = Avec - (Avec @ mh) * mh
            out.append((mvec @ mvec, float(np.real(np.vdot(Aperp, Aperp))), float(np.real(np.vdot(Avec, Avec)))))
    return np.array(out), 2 * L ** 3, 4 * np.sin(kx / 2) ** 2


rows = []
for L, beta, nsw in ((6, 0.55, 4000), (8, 0.6, 3000), (6, 0.8, 1500), (8, 1.0, 1500), (6, 1.2, 1500)):
    data, Vv, Ek = bilayer_mc(L, beta, nsw, 400)
    M2 = data[:, 0].mean()
    rho = (data[:, 0] * data[:, 1]).mean() / (M2 * data[:, 1].mean())
    u = data[:, 2].mean() / (3 * Vv)
    a = M2 / 3
    f_old = a ** 2 / (beta * Ek + 2 * a / Vv)
    f_new = 4 * a ** 2 / (beta * Ek + 8 * a / Vv)
    f_lin = (4 / 9) * M2 / (beta * Ek + 8 / (3 * Vv))
    blocks = np.array_split(data, 10)
    rb = [(b[:, 0] * b[:, 1]).mean() / (b[:, 0].mean() * b[:, 1].mean()) for b in blocks]
    rows.append((L, beta, M2, rho, np.std(rb) / np.sqrt(10), u, f_old, f_new, f_lin))
    print(f"EXEC E L={L} beta={beta}: M^2 = {M2:.4f}; (C) ratio E[|m|^2|A_perp|^2]/(M^2 E|A_perp|^2) = {rho:.4f} +- {np.std(rb) / np.sqrt(10):.4f}; "
          f"u(k_min) = {u:.3f} against floors: block 92 {f_old:.3f}, this attempt {f_new:.3f}, conditional linear {f_lin:.3f}")
ok("E1 [executed] on block 90's bilayer at beta = 0.55 to 1.2 (through the ordering onset) the correlation ratio of (C) is below 1 and every floor lies below the measured u(k)",
   all(r[3] < 1 and r[6] < r[7] <= r[5] and r[8] <= r[5] for r in rows))

print(f"total {time.time() - T0:.1f} s; PASS={NP} FAIL={NF}")
if NF:
    print(f"SUMMARY: ROUTE FAILS AT the first FAIL line above ({NF} failures)")
    sys.exit(1)
print("SUMMARY: PARTIAL (b) exact: with F = (m x A)_2 in place of block 92's A1 m3, <DF> doubles while <|F|^2> = E[|m|^2|A_perp|^2]/3 <= V u, "
      "so u(k) >= 4(M^2/3)^2/(beta E(k) + 8M^2/(3V)) at zero field in every finite volume - four times block 92's floor; in 3+1 "
      "E(k)R(k) >= 4((1 - beta_L/beta)/3)^2, up to 4/9 of the inverse Laplacian instead of 1/9. (a) a bound with M^2 to the first power, "
      "u(k) >= (4/9) M^2/(beta E(k) + 8/(3V)), follows exactly from ONE correlation inequality (C) E[|m|^2 |A_perp(k)|^2] <= M^2 E|A_perp(k)|^2, "
      "which is not proved here (executed: ratio below 1 on the bilayer); ROUTE FAILS AT (C) for the unconditional linear bound. "
      "The task's HIT condition (an unconditional M^2-linear bound) is not met.")
