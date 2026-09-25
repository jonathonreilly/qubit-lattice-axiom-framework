#!/usr/bin/env python3
"""J:derive:deferred-20260924-stability:a1 -- worker w-macbookpro9927a-jbeaa (Claude Opus 5.5).

Owner-requested deferred-science recovery, batch 9 (U9-R2), first bounded pass.  Residual: the 'zero Hessian equality'
of the traceless anisotropy of the bond rates (block 88 T3; block 89 T2/T3): the cubic term of the path energy in both
supplied constraints.  Exact parts: sympy identities, exact rational lower sums and an exact rational remainder
constant.  Lines tagged [float] are numerical evidence only.

Model (landed notes): per site E(eps) = 36 beta eps^2 + E_sea(eps) - E_sea(0), E_sea = -<sqrt(Q_eps)>, zone average over
k in the 3D zone; a = s_x^2, b = s_y^2 + s_z^2, S = a + b, s_j = sin k_j.
  block 88 (fixed arithmetic mean): Q = (1+2eps)^2 a + (1-eps)^2 b;   block 89 (fixed mean log rate): Q = e^{4eps} a + e^{-2eps} b.
Run from the repository root."""
import hashlib, json, subprocess, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp

T0 = time.time()
RES = []
HERE = "probes/work/derive/deferred-20260924-stability/w-macbookpro9927a-jbeaa"


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"{tag} {'PASS' if ok else 'FAIL'}: {msg}", flush=True)


# ---------------------------------------------------------------- Q: frozen sources and landed notes
st = json.load(open(f"{HERE}/RECOVERY_STATUS.json"))
batch = json.load(open("probes/work/deferred-science-20260924/batch-09.json"))
man = {(str(s["pr"]), s["path"]): s["sha256"] for s in batch["sources"]}
bad = 0
for g in st["source_groups_inspected"]:
    blob = subprocess.run(["git", "show", f"{g['head']}:{g['path']}"], capture_output=True).stdout
    bad += hashlib.sha256(blob).hexdigest() != man[(str(g["pr"]), g["path"])]
same = all(subprocess.run(["git", "show", f"{st['origin_main_sha']}:{n['path']}"], capture_output=True).stdout ==
           subprocess.run(["git", "show", f"{st['batch_landed_commit']}:{n['path']}"], capture_output=True).stdout
           for n in st["canonical_notes"].values())
check("Q1", bad == 0 and len(st["source_groups_inspected"]) == 52 and same,
      f"52 frozen sources of PRs 8652/8657/8665/8678 match the manifest SHA256; blocks 84/85/88/89 identical at origin/main "
      f"{st['origin_main_sha'][:10]} and the landed commit")

# ---------------------------------------------------------------- S: exact identities
e = sp.symbols('epsilon', real=True)
a, b = sp.symbols('a b', positive=True)
u1, u2, u3 = sp.symbols('u1 u2 u3', nonnegative=True)
S = a + b
Ql = (1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b
Qg = sp.exp(4 * e) * a + sp.exp(-2 * e) * b


def coeffs(Q):
    ser = sp.expand(sp.series(sp.sqrt(Q), e, 0, 4).removeO())
    return [sp.simplify(ser.coeff(e, k)) for k in (1, 2, 3)]


def axis_sym(expr):
    """average over the three choices of the special axis: a = u_i, b = sum of the other two"""
    f = sp.Lambda((a, b), expr)
    return sp.simplify((f(u1, u2 + u3) + f(u2, u3 + u1) + f(u3, u1 + u2)) / 3)


s1, s2, s3 = u1 + u2 + u3, u1 * u2 + u2 * u3 + u3 * u1, u1 * u2 * u3
Su = s1
c1, c2, c3 = coeffs(Ql)
ok = sp.simplify(axis_sym(c1)) == 0
ok &= sp.simplify(2 * c2 - 9 * a * b / S ** sp.Rational(3, 2)) == 0
ok &= sp.simplify(c3 + sp.Rational(9, 2) * a * b * (2 * a - b) / S ** sp.Rational(5, 2)) == 0
ok &= sp.simplify(sp.diff(sp.sqrt(Ql), e, 2) - 9 * a * b / Ql ** sp.Rational(3, 2)) == 0
cub_lin = sp.simplify(axis_sym(c3) * Su ** sp.Rational(5, 2))
ok &= sp.expand(cub_lin + sp.Rational(3, 2) * (s1 * s2 - 9 * s3)) == 0
ok &= sp.expand(s1 * s2 - 9 * s3 - (u1 * (u2 - u3) ** 2 + u2 * (u3 - u1) ** 2 + u3 * (u1 - u2) ** 2)) == 0
check("S1", ok, "arithmetic mean: d2/de2 sqrt(Q) = 9ab/Q^(3/2) exactly; first-order cyclic sum 0; second order 9ab/S^(3/2) "
      "(block 88's chi_a); cubic -(9/2)ab(2a-b)/S^(5/2), axis-averaged -(3/2)(s1 s2 - 9 s3)/S^(5/2), "
      "s1 s2 - 9 s3 = sum_i u_i (u_j - u_k)^2 >= 0")
g1, g2, g3 = coeffs(Qg)
ok = sp.simplify(axis_sym(g1)) == 0
ok &= sp.simplify(axis_sym(2 * g2) - (axis_sym(9 * a * b / S ** sp.Rational(3, 2)) + 2 * sp.sqrt(Su))) == 0
cub_log = sp.expand(sp.simplify(axis_sym(g3) * Su ** sp.Rational(5, 2)))
ok &= sp.expand(cub_log - (s1 ** 3 + sp.Rational(9, 2) * s1 * s2 + sp.Rational(81, 2) * s3) / 3) == 0
check("S2", ok, "mean log rate: first order cancels; axis-averaged second order 9ab/S^(3/2) + 2 S^(1/2) (block 89's chi_a + 2J); "
      "cubic (s1^3 + 9 s1 s2/2 + 81 s3/2)/(3 S^(5/2)), every term >= 0")

# ---------------------------------------------------------------- R: remainder constant and rigorous lower bound
g4 = sp.diff(sp.sqrt(Ql), e, 4)
D1, D2 = 4 * a - 2 * b, 4 * a + b
Qp = sp.diff(Ql, e)
ok = sp.simplify(g4 + sp.Rational(27, 2) * a * b * (2 * D2 * Ql - sp.Rational(5, 2) * Qp ** 2) / Ql ** sp.Rational(7, 2)) == 0
e0 = Fr(1, 100)
m0, M0 = (1 - 2 * e0) ** 2, (1 + 2 * e0) ** 2
J_up = Fr(12248, 10000)                           # >= sqrt(3/2) >= <|s|> (Jensen: <S> = 3/2)
assert J_up * J_up >= Fr(3, 2)
K = Fr(162, 24) * M0 * J_up / (1 - 2 * e0) ** 7   # sup |F''''|/24 on |eps| <= e0, since m0^(7/2) = (1 - 2 e0)^7
worst = 0.0
rng = np.random.default_rng(7)
for _ in range(4000):
    av, bv, ev = rng.random(), rng.random(), (rng.random() * 2 - 1) * float(e0)
    Sv = av + bv
    val = abs(float(g4.subs({a: av, b: bv, e: ev})))
    worst = max(worst, val / (162 * float(M0) * Sv ** 0.5 / float(m0) ** 3.5))
check("R1", ok and worst <= 1.0, f"d4/de4 sqrt(Q) = -(27/2)ab(2D2 Q - (5/2)Q'^2)/Q^(7/2) exactly; bound 162 M0 |s|/m0^(7/2) on "
      f"|eps| <= 1/100 (sampled max ratio {worst:.3f}); remainder constant K = {float(K):.4f} (exact rational)")

mp.mp.dps = 50
n = 24
lo, hi = [], []
for j in range(n + 1):
    v = mp.sin(mp.pi * j / (2 * n)) ** 2
    f = Fr(int(mp.floor(v * 10 ** 30)), 10 ** 30)
    lo.append(max(Fr(0), f)); hi.append(min(Fr(1), f + Fr(1, 10 ** 30)))
box = [(lo[j], hi[j + 1]) for j in range(n)]


def gap(p, q):
    return max(Fr(0), p[0] - q[1], q[0] - p[1])


tot = Fr(0)
for i1 in range(n):
    for i2 in range(i1, n):
        for i3 in range(i2, n):
            B = (box[i1], box[i2], box[i3])
            N = B[0][0] * gap(B[1], B[2]) ** 2 + B[1][0] * gap(B[2], B[0]) ** 2 + B[2][0] * gap(B[0], B[1]) ** 2
            if N == 0:
                continue
            Sh = B[0][1] + B[1][1] + B[2][1]
            r = Fr(int(mp.ceil(mp.sqrt(mp.mpf(Sh.numerator) / Sh.denominator) * 10 ** 30)), 10 ** 30)
            tot += (6 if i1 < i2 < i3 else 1 if i1 == i2 == i3 else 3) * N / (Sh * Sh * r)
e3_lo = Fr(3, 2) * tot / n ** 3                   # e3 = (3/2)<sum u_i(u_j-u_k)^2/S^(5/2)> >= e3_lo
t = e3_lo / (2 * K)
eta = e3_lo ** 2 / (4 * K)
check("R2", e3_lo > 0 and t <= e0, f"exact lower sums on 24^3 boxes (u = sin^2 k monotone on [0, pi/2]): e3 >= {float(e3_lo):.5f}; "
      f"at eps = -e3_lo/(2K) = {-float(t):.5f}, E < E(0) whenever 0 < 36 beta - chi_a/2 < e3_lo^2/(4K) = {float(eta):.3e}, "
      f"i.e. beta in (chi_a/72, chi_a/72 + {float(eta / 36):.2e})")

# ---------------------------------------------------------------- N: numerical evidence [float]
kk = (np.arange(96) + 0.5) * (np.pi / 2) / 96
u = np.sin(kk) ** 2
U1, U2, U3 = np.meshgrid(u, u, u, indexing="ij")
A, Bb = U1, U2 + U3
Sg = A + Bb
S1, S2, S3 = Sg, U1 * U2 + U2 * U3 + U3 * U1, U1 * U2 * U3
e3_lin = 1.5 * np.mean((S1 * S2 - 9 * S3) / Sg ** 2.5)
e3_log = -np.mean((S1 ** 3 + 4.5 * S1 * S2 + 40.5 * S3) / (3 * Sg ** 2.5))
chi_a = 9 * np.mean(A * Bb / Sg ** 1.5)
Jf = np.mean(np.sqrt(Sg))


def Fl(x):
    return np.mean(np.sqrt((1 + 2 * x) ** 2 * A + (1 - x) ** 2 * Bb))


def Fg(x):
    return np.mean(np.sqrt(np.exp(4 * x) * A + np.exp(-2 * x) * Bb))


h = 0.01
fd_l = -(Fl(2 * h) - 2 * Fl(h) + 2 * Fl(-h) - Fl(-2 * h)) / (12 * h ** 3)
fd_g = -(Fg(2 * h) - 2 * Fg(h) + 2 * Fg(-h) - Fg(-2 * h)) / (12 * h ** 3)
check("N1", abs(fd_l - e3_lin) < 2e-3 and abs(fd_g - e3_log) < 2e-3 and e3_lo <= e3_lin,
      f"[float] e3 = {e3_lin:.6f} (arith.) and {e3_log:.6f} (log; E_sea''' = {6 * e3_log:.4f}); finite differences "
      f"{fd_l:.5f}, {fd_g:.5f}; chi_a = {chi_a:.6f}, <|s|> = {Jf:.6f}; thresholds {chi_a / 72:.6f}, {(chi_a + 2 * Jf) / 72:.6f}")
eps = np.linspace(-0.5, 1.0, 751)
F0 = Fl(0.0)
ratio = np.array([(Fl(x) - F0) / (36 * x * x) if abs(x) > 1e-9 else -1 for x in eps])
i = int(np.argmax(ratio))
check("N2", ratio[i] > chi_a / 72 and eps[i] < 0,
      f"[float] arithmetic-mean path on eps in [-1/2, 1]: min E < E(0) iff beta < {ratio[i]:.5f} (attained near eps = "
      f"{eps[i]:.2f}); planes end eps = -1/2 gives {ratio[0]:.5f}; quadratic threshold {chi_a / 72:.5f}")


def chit(q, n1=512):
    k1 = 2 * np.pi * (np.arange(n1) + 0.5) / n1
    m2 = (u[:, None] + u[None, :]).ravel()
    x, y = np.sin(k1)[:, None], np.sin(k1 + q)[:, None]
    fx, fy = x / np.sqrt(x ** 2 + m2), y / np.sqrt(y ** 2 + m2)
    with np.errstate(invalid="ignore", divide="ignore"):
        G = np.where(np.abs(x - y) > 1e-12, (fx - fy) / (x - y), m2 / (x ** 2 + m2) ** 1.5)
    return float(np.mean(np.sin(k1 + q / 2)[:, None] ** 2 * G))


c0, cpi = chit(0.0), chit(np.pi)
marg = [c0 + (cpi - c0) * (1 - np.cos(q)) / 2 - chit(q) for q in (0.5, np.pi / 2, 2.6, np.pi - 0.05)]
check("N3", abs(c0 - chi_a / 9) < 1e-4 and abs(cpi - 0.51274) < 2e-4 and min(marg) > 0,
      f"[float] single-axis response chi~(q) = <sin^2(k1+q/2) G(sin k1, sin(k1+q); m)>: chi~(0) = {c0:.5f} = chi_a/9, "
      f"chi~(pi) = {cpi:.5f} = chi/3; chord margins at q = 0.5, pi/2, 2.6, pi-0.05: " + ", ".join(f"{m:.4f}" for m in marg))

npass = sum(1 for _, x in RES if x)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass} ({time.time() - T0:.0f}s)")
if npass == len(RES):
    print("SUMMARY: PARTIAL batch 9 (U9-R2) first pass: the zero-Hessian equality of the traceless anisotropy is decided in "
          "both supplied constraints by an exact cubic term of definite sign; unexamined intermediate-q directions reduced "
          "to a chord inequality and left open")
    print("HIT: along block 88's fixed-mean traceless anisotropy of the bond rates (1+2e, 1-e, 1-e) the sea energy's cubic "
          "coefficient is exactly (3/2)<sum_i u_i(u_j-u_k)^2/|s|^5> > 0 (u_j = sin^2 k_j), and along block 89's fixed-mean-log "
          "path (e^2e, e^-e, e^-e) it is -<(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5)> < 0; the law cost 36 beta e^2 has no cubic "
          "part, so at each quadratic threshold (beta = chi_a/72, resp. (chi_a + 2<|s|>)/72) the uniform rates are not a local "
          "minimum along the path: they descend towards e < 0 (weaker special axis) in linear rates and e > 0 in log rates; "
          "in linear rates a path point lies below the uniform energy for all beta in (chi_a/72, chi_a/72 + 1.2e-5) "
          "(exact lower sums and remainder bound), and numerically up to beta = 0.0271 (near e = -0.37)")
else:
    print("SUMMARY: ROUTE FAILS AT " + ",".join(t for t, x in RES if not x))
