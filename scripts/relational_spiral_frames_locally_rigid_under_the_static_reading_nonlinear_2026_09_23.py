#!/usr/bin/env python3
"""Relational spiral frames are locally rigid under the static reading:
every static stationary record near a spiral is a rotated spiral, up to a
free axis at each core corner.

Open PR 8691 found spiral records b(x) = R_z(theta . x) b0 stationary under
its covariant unsoldered rule, and under the static reading each core site
is the unique covariant completion of its back-neighbours and of its forward
neighbours.  Open PR 8717 showed linear rigidity for the static reading.
This runner lifts it to the full nonlinear system on 4- and 5-boxes:
  * the full static system (values b on the used sites, a back axis and a
    forward axis at each core site; unit lengths, axes orthogonal to the
    value, b(x - e_i) = R_nb(-theta_i) b(x), b(x + e_i) = R_nf(theta_i) b(x))
    linearised at the spiral has nullity exactly 5;
  * five exact kernel vectors: the phase, the two tilts, and a turn of the
    back axis at one core corner and of the forward axis at the other;
  * exact nonlinear families through the spiral realise all five: rational
    rotations of the whole record, and rational turns of the corner axes
    with the corner's outer neighbours rotated along;
  * a smooth 5-parameter family of solutions whose tangent space is the
    whole kernel forces, by the implicit function theorem, every solution
    near the spiral to lie in that family.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * the spiral, angles (3/5, 4/5), (5/13, 12/13), (8/17, 15/17) and the
    static relations of open PR 8691; the Rodrigues formula
    R_n(a) v = cos a v + sin a (n x v) + (1 - cos a)(n . v) n;
  * boxes: core sites have all coordinates in 1..L-2; used sites are the
    core sites and their six neighbours;
  * exact arithmetic: Fractions; ranks modulo the prime 2^61 - 1 bound the
    rational rank from below, so exact independent kernel vectors fix the
    rational nullity.

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


def spiral(x):
    c, s = phase(x)
    return (c, s, Fr(0))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def rot(n, c, s, v):
    """Rodrigues: rotation about unit n with (cos, sin) = (c, s)."""
    nxv, nv = cross(n, v), dot(n, v)
    return tuple(c * v[t] + s * nxv[t] + (1 - c) * nv * n[t] for t in range(3))


def nb(x, i, d):
    return tuple(x[j] + (d if j == i else 0) for j in range(3))


def boxes(L):
    core = [x for x in product(range(L), repeat=3) if all(1 <= c <= L - 2 for c in x)]
    used = sorted(set(core) | {nb(x, i, d) for x in core for i in range(3) for d in (-1, 1)})
    return core, used


def static_rows(L):
    """The full static system linearised at the spiral: unknowns db (used), dnb and dnf (core)."""
    core, used = boxes(L)
    bi = {x: 3 * k for k, x in enumerate(used)}
    nbi = {x: 3 * len(used) + 3 * k for k, x in enumerate(core)}
    nfi = {x: 3 * len(used) + 3 * len(core) + 3 * k for k, x in enumerate(core)}
    nv = 3 * len(used) + 6 * len(core)
    rows = []

    def add(r, k, v):
        r[k] = r.get(k, Fr(0)) + v

    for x in used:
        b = spiral(x)
        rows.append({bi[x] + t: 2 * b[t] for t in range(3) if b[t]})
    for x in core:
        b, n = spiral(x), Z3
        for ni in (nbi, nfi):
            rows.append({ni[x] + 2: Fr(2)})
            r = {}
            for t in range(3):
                add(r, ni[x] + t, b[t])
                add(r, bi[x] + t, n[t])
            rows.append(r)
        for i, (c, s) in enumerate(CS):
            for d, ni, sa in ((-1, nbi, -s), (1, nfi, s)):
                y = nb(x, i, d)
                for comp in range(3):
                    r = {}
                    add(r, bi[y] + comp, Fr(1))
                    add(r, bi[x] + comp, -c)
                    e0, e1 = [(1, 2), (2, 0), (0, 1)][comp]
                    add(r, ni[x] + e0, -sa * b[e1])
                    add(r, ni[x] + e1, sa * b[e0])
                    add(r, bi[x] + e1, -sa * n[e0])
                    add(r, bi[x] + e0, sa * n[e1])
                    for t in range(3):
                        add(r, ni[x] + t, -(1 - c) * b[t] * n[comp])
                        add(r, bi[x] + t, -(1 - c) * n[t] * n[comp])
                    rows.append(r)
    return core, used, bi, nbi, nfi, nv, rows


def kernel_vectors(core, used, bi, nbi, nfi, nv, L):
    """Phase, tilts about x and y, and the two corner-axis turns, written directly."""
    out = []
    for w in ((Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0))):
        v = [Fr(0)] * nv
        for x in used:
            for t, q in enumerate(cross(w, spiral(x))):
                v[bi[x] + t] = q
        for x in core:
            for t, q in enumerate(cross(w, Z3)):
                v[nbi[x] + t] = v[nfi[x] + t] = q
        out.append(v)
    for corner, ni, d in (((1, 1, 1), nbi, -1), ((L - 2,) * 3, nfi, 1)):
        v = [Fr(0)] * nv
        turn = cross(spiral(corner), Z3)
        for t in range(3):
            v[ni[corner] + t] = turn[t]
        for i, (c, s) in enumerate(CS):
            v[bi[nb(corner, i, d)] + 2] = d * s
        out.append(v)
    return out


print("A. the full static system, linearised at the spiral")
lin = []
for L in (4, 5):
    core, used, bi, nbi, nfi, nv, rows = static_rows(L)
    nullity = nv - rank_mod([[modq(r.get(k, Fr(0))) for k in range(nv)] for r in rows], nv)
    kv = kernel_vectors(core, used, bi, nbi, nfi, nv, L)
    exact = all(sum(val * v[k] for k, val in r.items()) == 0 for v in kv for r in rows)
    rk = rank_mod([[modq(q) for q in v] for v in kv], nv)
    lin.append((L, nv, len(rows), nullity, rk, exact))
check("nullity exactly 5 on 4- and 5-boxes: phase, two tilts, and the two corner-axis turns",
      all(r[3] == 5 and r[4] == 5 and r[5] for r in lin),
      "; ".join(f"L={r[0]}: {r[1]} unknowns, {r[2]} equations, nullity {r[3]} = rank of 5 exact kernel vectors {r[4]}"
                for r in lin))

print("B. exact nonlinear families through the spiral")


def satisfies(L, val, axb, axf):
    """Every static relation and constraint holds exactly for values val and axes axb, axf."""
    core, used = boxes(L)
    ok = all(dot(val[x], val[x]) == 1 for x in used)
    for x in core:
        ok = ok and dot(axb[x], axb[x]) == 1 and dot(axf[x], axf[x]) == 1
        ok = ok and dot(axb[x], val[x]) == 0 and dot(axf[x], val[x]) == 0
        for i, (c, s) in enumerate(CS):
            ok = ok and val[nb(x, i, -1)] == rot(axb[x], c, -s, val[x]) and val[nb(x, i, 1)] == rot(axf[x], c, s, val[x])
    return ok


fam = []
for L in (4, 5):
    core, used = boxes(L)
    base = ({x: spiral(x) for x in used}, {x: Z3 for x in core}, {x: Z3 for x in core})
    ok_base = satisfies(L, *base)
    rotated = []
    for axis in ((Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(1))):
        Q = lambda v: rot(axis, Fr(3, 5), Fr(4, 5), v)
        rotated.append(satisfies(L, {x: Q(v) for x, v in base[0].items()}, {x: Q(v) for x, v in base[1].items()},
                                 {x: Q(v) for x, v in base[2].items()}))
    corners = []
    for corner, d in (((1, 1, 1), -1), ((L - 2,) * 3, 1)):
        val, axb, axf = dict(base[0]), dict(base[1]), dict(base[2])
        new_axis = rot(spiral(corner), Fr(5, 13), Fr(12, 13), Z3)
        if d < 0:
            axb[corner] = new_axis
        else:
            axf[corner] = new_axis
        for i, (c, s) in enumerate(CS):
            val[nb(corner, i, d)] = rot(new_axis, c, d * s, val[corner])
        moved = sum(1 for x in used if val[x] != base[0][x])
        corners.append(satisfies(L, val, axb, axf) and moved == 3)
    fam.append((L, ok_base, rotated, corners))
check("rotations of the whole record and turns of either corner axis are exact nonlinear solutions",
      all(r[1] and all(r[2]) and all(r[3]) for r in fam),
      "rotations by (3/5, 4/5) about x, y and z; corner axes turned by (5/13, 12/13), each moving exactly the "
      "corner's three outer neighbours; exact on the 4- and 5-boxes")

print("C. local rigidity")


def d_rot(n0, n1, c, s, v):
    """First-order change of R_n(a) v when the axis moves from n0 to n0 + e n1 (Rodrigues, term by term)."""
    n1xv = cross(n1, v)
    return tuple(s * n1xv[t] + (1 - c) * (dot(n1, v) * n0[t] + dot(n0, v) * n1[t]) for t in range(3))


tangent_ok = []
for L in (4, 5):
    core, used, bi, nbi, nfi, nv, rows = static_rows(L)
    kv = kernel_vectors(core, used, bi, nbi, nfi, nv, L)
    for k, (corner, ni, d) in enumerate((((1, 1, 1), nbi, -1), ((L - 2,) * 3, nfi, 1))):
        b0 = spiral(corner)
        n1 = cross(b0, Z3)
        t = [Fr(0)] * nv
        for q in range(3):
            t[ni[corner] + q] = n1[q]
        for i, (c, s_) in enumerate(CS):
            dv = d_rot(Z3, n1, c, d * s_, b0)
            for q in range(3):
                t[bi[nb(corner, i, d)] + q] = dv[q]
        tangent_ok.append(t == kv[3 + k])
    for k, w in enumerate(((Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)))):
        t = [Fr(0)] * nv
        for x in used:
            for q, val in enumerate(cross(w, spiral(x))):
                t[bi[x] + q] = val
        for x in core:
            for q, val in enumerate(cross(w, Z3)):
                t[nbi[x] + q] = t[nfi[x] + q] = val
        tangent_ok.append(t == kv[k])
check("the families' tangent vectors at the spiral are the five kernel vectors, so the family fills the kernel",
      len(tangent_ok) == 10 and all(tangent_ok) and all(r[3] == 5 and r[4] == 5 for r in lin),
      "a corner-axis turn moves the axis by b x z and each outer neighbour by d s_i z (first-order Rodrigues); "
      "rotations move values and axes by w x b and w x z; with the linearisation of rank n - 5 the implicit "
      "function theorem makes the nearby solution set a 5-dimensional manifold, which the family fills")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
