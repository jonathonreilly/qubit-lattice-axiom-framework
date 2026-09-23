#!/usr/bin/env python3
"""Relational spiral frames: linearly rigid on the lattice, flexible on boxes,
and amplified by the sweep.

Open PR 8691 found spiral records b(x) = R_z(theta . x) b0 stationary under
a covariant unsoldered sweep rule: each site's value v and its three
back-neighbours lie on one great circle, with axis n(x), and
b(x - e_i) = R_n(x)(-theta_i) b(x) for Pythagorean angles
(cos, sin) = (3/5, 4/5), (5/13, 12/13), (8/17, 15/17).  It left rigidity
open.  Linearising that stationarity at a spiral:
  * in-plane: a phase psi with psi(x - e_i) = psi(x): only the constant;
  * out-of-plane: with a = -(vertical part of the value) and beta = the
    axis tilt along z x b0, a(x - e_i) = c_i a(x) - s_i beta(x); every w
    gives the exact solution a = prod_j (c_j - w s_j)^(-x_j), beta = w a.
On an L-box the linear solutions are exactly the phase and the span of
these modes (nullity 3L - 3, checked for L = 3, 4, 5 on the full
linearisation with exact rational solutions and a modular rank bound).  A
mode has a real wavevector only if |c_j - w s_j| = 1 for all j; each such
circle is |w|^2 - 2 cot(theta_j) Re w = 1, so two meet only at w = +-i,
whose modes are the two global tilts.  Bounded deformations on Z^3 are
therefore global.  Along the sweep a mode grows by 1/|c_j - w s_j| per
step: 5/3, 13/5, 17/8 at w = 0 and 5, 13, 34 at w = 1/2.  On a 6-box the
sweep rebuilds a mode from its back boundary exactly and stops at a
generic change of one boundary value.  Under the static reading, where
each core site completes from its back-neighbours and from its forward
neighbours, the out-of-plane solutions on 4-, 5- and 6-boxes are the two
global tilts and a free axis at each of the two core corners: the
static reading is rigid on boxes.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * the spiral, the angles and the stationarity relations of open PR 8691;
  * boxes: sites with all coordinates in 0..L-1; interior sites (all
    coordinates >= 1) carry the relations; their back-neighbours are the
    box sites used;
  * exact arithmetic: rational solutions verified with Fractions; ranks
    modulo the prime 2^61 - 1 bound the rational rank from below, so exact
    independent solutions fix the rational nullity.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


PR = 2**61 - 1
CS = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17))]
Z3 = (Fr(0), Fr(0), Fr(1))


def modq(q):
    return (q.numerator % PR) * pow(q.denominator % PR, PR - 2, PR) % PR


def rank_mod(rows, ncols):
    rows = [r[:] for r in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] % PR), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], PR - 2, PR)
        rows[r] = [v * inv % PR for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % PR for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def phase(x):
    """(cos, sin) of theta . x by complex multiplication."""
    z = (Fr(1), Fr(0))
    for (c, s), k in zip(CS, x):
        step = (c, s) if k >= 0 else (c, -s)
        for _ in range(abs(k)):
            z = cmul(z, step)
    return z


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def box(L):
    I = [x for x in product(range(L), repeat=3) if all(c >= 1 for c in x)]
    S = sorted(set(I) | {tuple(x[j] - (j == i) for j in range(3)) for x in I for i in range(3)})
    return I, S


def full_rows(L):
    """Linearised stationarity of open PR 8691's sweep relations at the spiral, unknowns db (on S) and dn (on I)."""
    I, S = box(L)
    bi = {x: 3 * k for k, x in enumerate(S)}
    ni = {x: 3 * len(S) + 3 * k for k, x in enumerate(I)}
    nv = 3 * len(S) + 3 * len(I)
    rows = []

    def add(r, k, v):
        r[k] = r.get(k, Fr(0)) + v

    for x in S:
        cz, sz = phase(x)
        b = (cz, sz, Fr(0))
        r = {}
        for t in range(3):
            add(r, bi[x] + t, 2 * b[t])
        rows.append(r)
    for x in I:
        cz, sz = phase(x)
        b, n = (cz, sz, Fr(0)), Z3
        r = {}
        for t in range(3):
            add(r, ni[x] + t, 2 * n[t])
        rows.append(r)
        r = {}
        for t in range(3):
            add(r, ni[x] + t, b[t])
            add(r, bi[x] + t, n[t])
        rows.append(r)
        for i, (c, s) in enumerate(CS):
            prev = tuple(x[j] - (j == i) for j in range(3))
            for comp in range(3):
                r = {}
                add(r, bi[prev] + comp, Fr(1))
                add(r, bi[x] + comp, -c)
                e0, e1 = [(1, 2), (2, 0), (0, 1)][comp]
                add(r, ni[x] + e0, s * b[e1])
                add(r, ni[x] + e1, -s * b[e0])
                add(r, bi[x] + e1, s * n[e0])
                add(r, bi[x] + e0, -s * n[e1])
                for t in range(3):
                    add(r, ni[x] + t, -(1 - c) * b[t] * n[comp])
                    add(r, bi[x] + t, -(1 - c) * n[t] * n[comp])
                rows.append(r)
    return I, S, bi, ni, nv, rows


def lift(I, S, bi, ni, nv, a, beta, psi):
    """Full perturbation from (a, beta) out of plane and psi in plane: db = psi t0 - a z, dn = a b0 + beta t0."""
    v = [Fr(0)] * nv
    for x in S:
        cz, sz = phase(x)
        t0 = (-sz, cz, Fr(0))
        p = psi.get(x, Fr(0))
        for t, val in enumerate((p * t0[0], p * t0[1], -a.get(x, Fr(0)))):
            v[bi[x] + t] = val
    for x in I:
        cz, sz = phase(x)
        b0, t0 = (cz, sz, Fr(0)), (-sz, cz, Fr(0))
        for t in range(3):
            v[ni[x] + t] = a[x] * b0[t] + beta[x] * t0[t]
    return v


def mode(w, S, I):
    a = {}
    for x in S:
        val = Fr(1)
        for (c, s), k in zip(CS, x):
            val /= (c - w * s) ** k
        a[x] = val
    return a, {x: w * a[x] for x in I}


print("A. the linearisation and its solutions on boxes")
WS = [Fr(k, 7) for k in range(-12, 13)]
rows_out = []
for L in (3, 4, 5):
    I, S, bi, ni, nv, rows = full_rows(L)
    dense = [[modq(r.get(k, Fr(0))) for k in range(nv)] for r in rows]
    nullity_p = nv - rank_mod(dense, nv)
    sols = [lift(I, S, bi, ni, nv, {x: Fr(0) for x in S}, {x: Fr(0) for x in I}, {x: Fr(1) for x in S})]
    for w in WS:
        a, beta = mode(w, S, I)
        sols.append(lift(I, S, bi, ni, nv, a, beta, {}))
    exact = all(sum(val * v[k] for k, val in r.items()) == 0 for v in sols for r in rows)
    indep = rank_mod([[modq(q) for q in v] for v in sols], nv)
    rows_out.append((L, nullity_p, indep, exact))
check("on L-boxes the solutions are the phase and the exponential modes: nullity 3L - 3 for L = 3, 4, 5",
      all(r[3] and r[1] == r[2] == 3 * r[0] - 3 for r in rows_out),
      "; ".join(f"L={r[0]}: nullity {r[1]} = rank of {len(WS) + 1} exact solutions {r[2]}" for r in rows_out))

print("B. bounded deformations on Z^3")
circle_ok = all(Fr(c, 1) ** 2 / s ** 2 - 1 / s ** 2 == -1 for c, s in CS)
pairs_ok = all(CS[i][0] / CS[i][1] != CS[j][0] / CS[j][1] for i in range(3) for j in range(i + 1, 3))
unit_at_i = all((c ** 2 + s ** 2) == 1 for c, s in CS)
check("each neutral circle |c_j - w s_j| = 1 is |w|^2 - 2 cot(theta_j) Re w = 1; distinct circles meet only at w = +-i",
      circle_ok and pairs_ok and unit_at_i,
      "cot^2 - csc^2 = -1 for all three angles; the cotangents 3/4, 5/12, 8/15 differ, so Re w = 0 and |w| = 1")
I, S = box(4)
tilt_x = {x: -phase(x)[1] for x in S}, {x: -phase(x)[0] for x in I}
tilt_y = {x: phase(x)[0] for x in S}, {x: -phase(x)[1] for x in I}
rel = lambda a, beta: all(a[tuple(x[j] - (j == i) for j in range(3))] == c * a[x] - s * beta[x]
                          for x in I for i, (c, s) in enumerate(CS))
check("the w = +-i modes are the global tilts about the x and y axes",
      rel(*tilt_x) and rel(*tilt_y),
      "a = -sin(theta . x), beta = -cos(theta . x) about x; a = cos, beta = -sin about y; exact on the 4-box")

print("C. the sweep")
growth = {w: [1 / abs(c - w * s) for c, s in CS] for w in (Fr(0), Fr(1, 2), Fr(3))}
unique = all(CS[i][1] * CS[j][0] - CS[i][0] * CS[j][1] != 0 for i in range(3) for j in range(i + 1, 3))
check("a consistent back-boundary perturbation propagates uniquely as its mode; modes grow, decay or (at w = +-i) stay level",
      unique and growth[Fr(0)] == [Fr(5, 3), Fr(13, 5), Fr(17, 8)] and growth[Fr(1, 2)] == [5, 13, 34]
      and all(g < 1 for g in growth[Fr(3)]),
      "forward factors per step: w = 0: 5/3, 13/5, 17/8; w = 1/2: 5, 13, 34; w = 3: 5/9, 13/31, 17/37")



def sweep(a_back, I):
    """Forward propagation: each interior site from its back-neighbours along e1, e2; None where e3 disagrees."""
    a, beta = dict(a_back), {}
    (c1, s1), (c2, s2), (c3, s3) = CS
    for x in sorted(I, key=sum):
        y1, y2, y3 = (tuple(x[j] - (j == i) for j in range(3)) for i in range(3))
        det = -c1 * s2 + c2 * s1
        ax = (-s2 * a[y1] + s1 * a[y2]) / det
        bx = (c1 * a[y2] - c2 * a[y1]) / det
        if a[y3] != c3 * ax - s3 * bx:
            return None, x
        a[x], beta[x] = ax, bx
    return (a, beta), None


I6, S6 = box(6)
back = [x for x in S6 if x not in set(I6)]
m_a, m_beta = mode(Fr(1, 2), S6, I6)
prop, _ = sweep({x: m_a[x] for x in back}, I6)
kick = dict((x, m_a[x]) for x in back)
kick[(0, 1, 1)] += Fr(1, 1000)
stop, where = sweep(kick, I6)
corner = m_a[(5, 5, 5)] / m_a[(1, 1, 1)]
check("on the 6-box the sweep rebuilds the w = 1/2 mode from its back boundary; one generic boundary change stops it",
      prop is not None and prop[0] == m_a and prop[1] == m_beta and stop is None and where == (1, 1, 1)
      and corner == (5 * 13 * 34) ** 4,
      f"{len(back)} boundary values; interior grows by (5*13*34)^4 from (1,1,1) to (5,5,5); "
      f"the changed value at (0,1,1) breaks the third relation at (1,1,1)")

print("D. the static reading")


def nb(x, i, d):
    return tuple(x[j] + (d if j == i else 0) for j in range(3))


def static_rows(L):
    """Core sites complete from their back-neighbours (axis tilt beta_b) and from their forward ones (beta_f)."""
    core = [x for x in product(range(L), repeat=3) if all(1 <= c <= L - 2 for c in x)]
    used = sorted(set(core) | {nb(x, i, d) for x in core for i in range(3) for d in (-1, 1)})
    ai = {x: k for k, x in enumerate(used)}
    bb = {x: len(used) + k for k, x in enumerate(core)}
    bf = {x: len(used) + len(core) + k for k, x in enumerate(core)}
    rows = []
    for x in core:
        for i, (c, s) in enumerate(CS):
            rows.append({ai[nb(x, i, -1)]: Fr(1), ai[x]: -c, bb[x]: s})
            rows.append({ai[nb(x, i, 1)]: Fr(1), ai[x]: -c, bf[x]: -s})
    return core, used, ai, bb, bf, len(used) + 2 * len(core), rows


static_out = []
for L in (4, 5, 6):
    core, used, ai, bb, bf, nv, rows = static_rows(L)
    nullity_p = nv - rank_mod([[modq(r.get(k, Fr(0))) for k in range(nv)] for r in rows], nv)
    sols = []
    for a_of, b_of in ((lambda x: -phase(x)[1], lambda x: -phase(x)[0]), (lambda x: phase(x)[0], lambda x: -phase(x)[1])):
        v = [Fr(0)] * nv
        for x in used:
            v[ai[x]] = a_of(x)
        for x in core:
            v[bb[x]] = v[bf[x]] = b_of(x)
        sols.append(v)
    lo, hi = (1, 1, 1), (L - 2,) * 3
    v = [Fr(0)] * nv
    v[bb[lo]] = Fr(1)
    for i, (c, s) in enumerate(CS):
        v[ai[nb(lo, i, -1)]] = -s
    sols.append(v)
    v = [Fr(0)] * nv
    v[bf[hi]] = Fr(1)
    for i, (c, s) in enumerate(CS):
        v[ai[nb(hi, i, 1)]] = s
    sols.append(v)
    exact = all(sum(val * w_[k] for k, val in r.items()) == 0 for w_ in sols for r in rows)
    indep = rank_mod([[modq(q) for q in w_] for w_ in sols], nv)
    on_core = [any(w_[ai[x]] != 0 for x in core) for w_ in sols]
    static_out.append((L, nullity_p, indep, exact, on_core))
check("the static reading is rigid on boxes: the global tilts and a free axis at each core corner, nothing else",
      all(r[3] and r[1] == r[2] == 4 and r[4] == [True, True, False, False] for r in static_out),
      "; ".join(f"L={r[0]}: nullity {r[1]} = rank of 4 exact solutions {r[2]}" for r in static_out)
      + "; only the two tilts move core sites")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
