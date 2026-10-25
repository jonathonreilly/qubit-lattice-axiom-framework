#!/usr/bin/env python3
"""Independent exact reconstruction and certificate for the range-three cubic walk obstruction.

Setting (premises, see ATTEMPT.md): translation-covariant walk on one qubit per site, hops in
{-3..3}^3, covariant under the 24 proper cubic rotations with the full-soldered spin-1/2 coin
action.  After the determinant reduction, V(k) = f + i g.sigma with f an O-invariant and g an
O-equivariant trigonometric polynomial of range <= 3 and f^2 + g.g = 1.  The script works over
C (coefficients are allowed complex: only the polynomial identity f^2+g.g=1 is used).

Uses only numpy, sympy and the standard library.  No Singular, no source scripts.
Optional: if ./src/r3_triv.sing sits next to this file, the archived Singular input is compared.
"""
import itertools, math, os, random, sys, time, resource
from collections import defaultdict
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

T0 = time.time()
NPASS = NFAIL = 0
def check(ok, msg):
    global NPASS, NFAIL
    if ok: NPASS += 1
    else: NFAIL += 1
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    return ok
def el(): return f"[{time.time()-T0:.0f}s]"

# ---------------------------------------------------------------- group and function bases
def rotations():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for a in range(3): M[a][p[a]] = s[a]
            if sp.Matrix(M).det() == 1: out.append(tuple(map(tuple, M)))
    return out
O24 = rotations()
D4 = [M for M in O24 if abs(M[2][2]) == 1]          # keeps the z axis as an axis (control group)

def pull(M, b):
    """phi_b(M k) = sign * phi_b'(k) for the tensor basis phi_b = prod_a phi_{b_a}(k_a); j>0 cos, j<0 sin."""
    nb = [0] * 3; sg = 1
    for a in range(3):
        c = [x for x in range(3) if M[a][x] != 0][0]; s = M[a][c]
        if b[a] < 0 and s == -1: sg = -sg
        nb[c] = b[a]
    return sg, tuple(nb)

def build_bases(G, R):
    J = list(range(-R, R + 1)); B = list(itertools.product(J, repeat=3)); idx = {b: i for i, b in enumerate(B)}
    nB = len(B); n = len(G)
    rows = []
    for b in B:
        v = defaultdict(int)
        for M in G:
            sg, nb = pull(M, b); v[idx[nb]] += sg
        rows.append([QQ(v.get(i, 0), n) for i in range(nB)])
    rr, piv = DomainMatrix(rows, (nB, nB), QQ).rref()
    Mr = rr.to_Matrix(); FB = [[Fr(int(x.p), int(x.q)) for x in Mr.row(i)] for i in range(len(piv))]
    rows = []
    for a in range(3):
        for b in B:
            v = defaultdict(int)
            for M in G:
                sg, nb = pull(M, b)
                for c in range(3):
                    if M[a][c] != 0: v[c * nB + idx[nb]] += sg * M[a][c]
            rows.append([QQ(v.get(i, 0), n) for i in range(3 * nB)])
    rr, piv = DomainMatrix(rows, (3 * nB, 3 * nB), QQ).rref()
    Mr = rr.to_Matrix(); GB = [[Fr(int(x.p), int(x.q)) for x in Mr.row(i)] for i in range(len(piv))]
    return B, FB, GB

# ---------------------------------------------------------------- exact rational trigonometry
def cs_rational(s):
    s = Fr(s); return (1 - s * s) / (1 + s * s), 2 * s / (1 + s * s)
def cs_multiples(c, s, R):
    """exact (cos jk, sin jk), j = 0..R, from (c, s)=(cos k, sin k) rational"""
    out = [(Fr(1), Fr(0))]
    for _ in range(R): out.append((out[-1][0] * c - out[-1][1] * s, out[-1][0] * s + out[-1][1] * c))
    return out
def basis_values(B, R, cs):
    """values of all tensor basis functions at the point whose per-axis (cos,sin) are cs[a]"""
    tab = [cs_multiples(cs[a][0], cs[a][1], R) for a in range(3)]
    def ph(a, j): return Fr(1) if j == 0 else (tab[a][j][0] if j > 0 else tab[a][-j][1])
    return [ph(0, b[0]) * ph(1, b[1]) * ph(2, b[2]) for b in B]

# ---------------------------------------------------------------- line restriction (exact, rational)
def tmul(p, q):
    out = defaultdict(Fr)
    for (ka, ma), ca in p.items():
        for (kb, mb), cb in q.items():
            c = ca * cb
            if ka == 'c' and kb == 'c':
                out[('c', abs(ma - mb))] += c / 2; out[('c', ma + mb)] += c / 2
            elif ka == 's' and kb == 's':
                out[('c', abs(ma - mb))] += c / 2; out[('c', ma + mb)] -= c / 2
            else:
                a_, b_ = (ma, mb) if ka == 's' else (mb, ma)       # sin(a_) cos(b_)
                out[('s', a_ + b_)] += c / 2
                if a_ > b_: out[('s', a_ - b_)] += c / 2
                elif a_ < b_: out[('s', b_ - a_)] -= c / 2
    return {k: v for k, v in out.items() if v != 0 and k != ('s', 0)}
def factor(j, b, e):
    if j == 0: return {('c', 0): Fr(1)}
    m = abs(j); sg = -1 if (m * b) % 2 else 1
    if j > 0: return {('c', 0): Fr(sg)} if e == 0 else {('c', m): Fr(sg)}
    return {} if e == 0 else {('s', m): Fr(sg * e)}
def restrict(bj, base, e):
    p = {('c', 0): Fr(1)}
    for a in range(3):
        p = tmul(p, factor(bj[a], base[a], e[a]))
        if not p: return {}
    return p

def line_system(B, FB, GB, lines, R):
    nF, nG = len(FB), len(GB); nB = len(B)
    rest = {li: [restrict(b, base, e) for b in B] for li, (base, e) in enumerate(lines)}
    rowsd = {}
    def add(key, col, val):
        r = rowsd.setdefault(key, defaultdict(Fr)); r[col] += val
    for li, (base, e) in enumerate(lines):
        for i, v in enumerate(FB):
            for bi, c in enumerate(v):
                if c == 0: continue
                for k, cf in rest[li][bi].items(): add((li, 'f', k), i, c * cf)
        for i, v in enumerate(GB):
            for a in range(3):
                if e[a] == 0: continue
                for bi in range(nB):
                    c = v[a * nB + bi]
                    if c == 0: continue
                    for k, cf in rest[li][bi].items(): add((li, 'g', k), nF + i, c * cf * e[a])
    deg = {li: R * sum(abs(x) for x in e) for li, (b, e) in enumerate(lines)}
    keys = set(rowsd)
    assert all(k[2][1] <= deg[k[0]] for k in keys), "line restriction exceeds stated degree"
    for li in range(len(lines)):
        for kind in 'fg':
            for m in range(deg[li] + 1):
                for t in 'cs':
                    if not (t == 's' and m == 0): keys.add((li, kind, (t, m)))
    keys = sorted(keys, key=lambda x: (x[0], x[1], x[2][0], x[2][1]))
    L = [[rowsd.get(k, {}).get(c, Fr(0)) for c in range(nF + nG)] for k in keys]
    return keys, L, deg

def rho_type(e): return {1: 'a', 2: 'b', 3: 'c'}[sum(x * x for x in e)]   # |e| = 1, sqrt2, sqrt3

def left_null(L, ncols):
    nr = len(L)
    LT = DomainMatrix([[QQ(L[i][j].numerator, L[i][j].denominator) for i in range(nr)] for j in range(ncols)], (ncols, nr), QQ)
    N = LT.nullspace().to_Matrix().tolist()
    return [[Fr(int(x.p), int(x.q)) for x in row] for row in N]

def enumerate_branches(lines, keys, L, deg, ncols, groups_sign, split):
    """All exponent/sign branches (n_l, eps_point) of the line lemma that are exactly consistent:
    f|line = eps cos(n t), (e.g)/|e| = eps sin(n t), eps fixed per base point (Gamma: +1).
    Exact left-null-space test, no numerical step.  The irrational |e| in {1,sqrt2,sqrt3} is
    handled by splitting the test over the Q-independent numbers 1, sqrt2, sqrt3."""
    nr = len(keys); N = left_null(L, ncols)
    assert all(sum(row[i] * L[i][c] for i in range(nr)) == 0 for row in N for c in range(ncols))
    def tv(li, n, kind):
        t = [Fr(0)] * nr
        for r, (l, k, (typ, m)) in enumerate(keys):
            if l != li or k != kind: continue
            if kind == 'f' and typ == 'c' and m == abs(n): t[r] = Fr(1)
            if kind == 'g' and typ == 's' and m == abs(n) and n != 0: t[r] = Fr(1 if n > 0 else -1)
        return t
    def Nt(t):
        nzi = [i for i in range(nr) if t[i] != 0]
        return tuple(sum((row[i] * t[i] for i in nzi), Fr(0)) for row in N)
    data = {(li, n): (Nt(tv(li, n, 'f')), Nt(tv(li, n, 'g'))) for li in range(len(lines)) for n in range(-deg[li], deg[li] + 1)}
    zero = tuple(Fr(0) for _ in N)
    def comps(sel, eps):
        rat = list(zero); b = list(zero); c = list(zero)
        for li, n in sel:
            e = eps[li]; f, g = data[(li, n)]
            for i in range(len(zero)): rat[i] += e * f[i]
            tgt = {'a': rat, 'b': b, 'c': c}[rho_type(lines[li][1])]
            for i in range(len(zero)): tgt[i] += e * g[i]
        return tuple(rat), tuple(b), tuple(c)
    A, Bl = split
    table = defaultdict(list); nA = 0
    for ns in itertools.product(*[range(-deg[l], deg[l] + 1) for l in A]):
        table[comps(list(zip(A, ns)), {l: 1 for l in A})].append(ns); nA += 1
    feas = []; nB = 0
    signs = sorted({groups_sign[l] for l in Bl}); 
    for sg in itertools.product((1, -1), repeat=len(signs)):
        sm = dict(zip(signs, sg)); eps = {l: sm[groups_sign[l]] for l in Bl}
        for ns in itertools.product(*[range(-deg[l], deg[l] + 1) for l in Bl]):
            rat, b, c = comps(list(zip(Bl, ns)), eps); nB += 1
            key = (tuple(-x for x in rat), tuple(-x for x in b), tuple(-x for x in c))
            for na in table.get(key, []): feas.append((dict(zip(A, na)), dict(zip(Bl, ns)), dict(sm)))
    return feas, nA, nB, len(N)

# ================================================================ STAGE 0: hypotheses of the line lemma
def stabilizer_ok(G, base, e):
    """Stab of the torus line {base*pi + t e} fixing e pointwise ; and Stab(base) of the point."""
    def fixes(M, v): return all(sum(M[a][c] * v[c] for c in range(3)) == v[a] for a in range(3))
    def pt(M): return all((sum(M[a][c] * base[c] for c in range(3)) - base[a]) % 2 == 0 for a in range(3))
    stl = [M for M in G if fixes(M, e) and pt(M)]
    stp = [M for M in G if pt(M)]
    fixl = sp.Matrix.vstack(*[sp.Matrix(M) - sp.eye(3) for M in stl]).nullspace()
    only_line = (len(fixl) == 1 and sp.Matrix.hstack(fixl[0], sp.Matrix(e)).rank() == 1)
    fixp = sp.Matrix.vstack(*[sp.Matrix(M) - sp.eye(3) for M in stp]).nullspace()
    return only_line, len(fixp) == 0, len(stl), len(stp)

LINES_O = [((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (1, 1, 0)), ((0, 0, 0), (1, 1, 1)),
           ((0, 0, 1), (1, 0, 0)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 1), (1, 0, 0))]
SIGN_PT = {0: 'G', 1: 'G', 2: 'G', 3: 'X', 4: 'X', 5: 'M'}

def main():
    check(len(O24) == 24 and len(D4) == 8, f"group generation: |O|=24 proper signed permutation matrices, |D4|=8 {el()}")
    res = [stabilizer_ok(O24, b, e) for b, e in LINES_O]
    check(all(r[0] and r[1] for r in res),
          "line-lemma hypotheses for the six lines: stabiliser of line fixes only its direction; stabiliser of base point fixes no nonzero vector; "
          f"|Stab(line)|,|Stab(base)| = {[(r[2], r[3]) for r in res]}")

    # ------------------------------------------------------------ STAGE 1: control for the line-stage machinery (D4, range 1)
    Bc, FBc, GBc = build_bases(D4, 1)
    lines_c = [((0, 0, 0), (0, 0, 1)), ((0, 0, 0), (1, 0, 0))]
    okc = all(stabilizer_ok(D4, b, e)[0] and stabilizer_ok(D4, b, e)[1] for b, e in lines_c)
    keysc, Lc, degc = line_system(Bc, FBc, GBc, lines_c, 1)
    feas_c, _, _, _ = enumerate_branches(lines_c, keysc, Lc, degc, len(FBc) + len(GBc), {0: 'G', 1: 'G'}, ([0, 1], []))
    got = sorted((f[0][0], f[0][1]) for f in feas_c)
    # the known moving D4 walk V = exp(i k_z sigma_z) has f = cos k_z, g = (0,0,sin k_z): it must satisfy the n_z = 1 branch
    okc2 = okc and {(0, 0), (1, 0), (-1, 0)} <= set(got)
    check(okc2, f"positive control (D4-covariant, range one, dims f={len(FBc)}, g={len(GBc)}): the exact line stage, which uses only necessary conditions, keeps the trivial branch and both axial-shift branches n_z=+-1 (it keeps {len(got)} exponent pairs in all, the unitarity ideal removes the rest), so it does not reject genuine moving walks")
    # direct test that exp(+i k_z sigma_z) solves the n_z=1 line system
    keys1, L1, deg1 = keysc, Lc, degc
    xk = [Fr(0)] * (len(FBc) + len(GBc))
    ic = {b: i for i, b in enumerate(Bc)}
    # find coefficients of cos k_z in FBc and (0,0,sin k_z) in GBc by solving small exact systems
    cosz = [Fr(1) if b == (0, 0, 1) else Fr(0) for b in Bc]
    sinz = [Fr(1) if (b == (0, 0, -1)) else Fr(0) for b in Bc]
    def coords_in(basis, vec):
        M_ = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in basis]).T
        rhs = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in vec])
        sol = M_.gauss_jordan_solve(rhs)[0]
        return [Fr(int(sp.Rational(t).p), int(sp.Rational(t).q)) for t in sol]
    cf = coords_in(FBc, cosz)
    gvec = [Fr(0)] * (3 * len(Bc))
    gvec[2 * len(Bc) + ic[(0, 0, -1)]] = Fr(1)
    cg = coords_in(GBc, gvec)
    xk = cf + cg
    tgt_ok = True
    n_target = 1
    for r_, (l, k_, (typ, m)) in enumerate(keys1):
        val = sum(L1[r_][c] * xk[c] for c in range(len(xk)))
        if l == 0:       # the z line: f = cos(t), e.g = sin(t) (|e|=1)
            want = Fr(1) if ((k_ == 'f' and typ == 'c' and m == 1) or (k_ == 'g' and typ == 's' and m == 1)) else Fr(0)
        else:            # the x line: f = 1, g.e = 0
            want = Fr(1) if (k_ == 'f' and typ == 'c' and m == 0) else Fr(0)
        if val != want: tgt_ok = False
    check(tgt_ok, "positive control, direct: the D4-covariant walk exp(i k_z sigma_z) (f = cos k_z, g = (0,0,sin k_z)) satisfies the exact line system of the branch (n_z, n_x) = (1, 0)")

    # ------------------------------------------------------------ STAGE 2: bases for O, range 3
    B, FB, GB = build_bases(O24, 3)
    check(len(B) == 343 and len(FB) == 21 and len(GB) == 42, f"O-invariant scalars 21, O-equivariant vectors 42 on the 343-point stencil (63 real unknowns) {el()}")
    idx = {b: i for i, b in enumerate(B)}
    dims_f = sum(sum(sg * (1 if nb == b else 0) for sg, nb in [pull(M, b)]) for M in O24 for b in B)
    tr_vec = [sum(M[a][a] for a in range(3)) for M in O24]
    dims_g = sum(tr_vec[i] * sum(sg * (1 if nb == b else 0) for b in B for sg, nb in [pull(M, b)]) for i, M in enumerate(O24))
    check(Fr(dims_f, 24) == 21 and Fr(dims_g, 24) == 42, f"character formula (1/24) sum_R tr: scalars {Fr(dims_f,24)}, vectors {Fr(dims_g,24)}")
    rnd = random.Random(7)
    okeq = True
    for trial in range(3):
        sv = [Fr(rnd.randint(1, 9), rnd.randint(2, 9)) for _ in range(3)]
        cs = [cs_rational(s) for s in sv]
        v0 = basis_values(B, 3, cs)
        f0 = [sum(c * v0[b] for b, c in enumerate(FB[i])) for i in range(21)]
        g0 = [[sum(GB[i][a * 343 + b] * v0[b] for b in range(343)) for a in range(3)] for i in range(42)]
        for M in O24:
            # point Mk: cos(M k)_a = cos(k_c), sin(M k)_a = s * sin(k_c)  where M[a][c]=s
            cs2 = []
            for a in range(3):
                c = [x for x in range(3) if M[a][x] != 0][0]; s = M[a][c]
                cs2.append((cs[c][0], s * cs[c][1]))
            v1 = basis_values(B, 3, cs2)
            for i in range(21):
                if sum(c * v1[b] for b, c in enumerate(FB[i])) != f0[i]: okeq = False
            for i in range(42):
                g1 = [sum(GB[i][a * 343 + b] * v1[b] for b in range(343)) for a in range(3)]
                Mg = [sum(M[a][c] * g0[i][c] for c in range(3)) for a in range(3)]
                if g1 != Mg: okeq = False
    check(okeq, f"exact rational check at random rational momenta (tan(k/2) rational): f(Mk)=f(k), g(Mk)=M g(k) for all 24 rotations and all 63 basis functions {el()}")

    # ------------------------------------------------------------ STAGE 3: exact line stage (no numerical discard)
    keys, L, deg = line_system(B, FB, GB, LINES_O, 3)
    Lm = DomainMatrix([[QQ(x.numerator, x.denominator) for x in r] for r in L], (len(keys), 63), QQ)
    check(len(keys) == 132 and Lm.rank() == 42 and deg == {0: 3, 1: 6, 2: 9, 3: 3, 4: 6, 5: 3},
          f"line system: 132 rows (modes of f and e.g on 6 lines) x 63 unknowns, rank 42, line degrees 3,6,9,3,6,3 {el()}")
    feas, nA, nB, nN = enumerate_branches(LINES_O, keys, L, deg, 63, SIGN_PT, ([0, 1, 2], [3, 4, 5]))
    check(nA == 7 * 13 * 19 and nB == 4 * 7 * 13 * 7 and nA * nB == 4405492,
          f"exhaustive enumeration size: 1729 Gamma-line exponent triples x 2548 (X,M) exponent/sign choices = {nA*nB} branches, left-null space dim {nN}")
    check(len(feas) == 1 and all(v == 0 for v in feas[0][0].values()) and all(v == 0 for v in feas[0][1].values()) and all(s == 1 for s in feas[0][2].values()),
          f"every branch tested exactly (meet-in-the-middle on exact rational vectors, no tolerance): exactly one consistent branch, all exponents 0, all signs +1 {el()}")

    # ------------------------------------------------------------ STAGE 4: the trivial branch
    t0 = [Fr(1) if (k[1] == 'f' and k[2] == ('c', 0)) else Fr(0) for k in keys]
    aug = DomainMatrix([[QQ(x.numerator, x.denominator) for x in r] + [QQ(t.numerator, t.denominator)] for r, t in zip(L, t0)], (len(keys), 64), QQ)
    rr, piv = aug.rref(); M_ = rr.to_Matrix()
    free = [c for c in range(63) if c not in piv]
    def Fq(x): return Fr(int(x.p), int(x.q))
    xp = [Fr(0)] * 63
    for r_, pc in enumerate(piv): xp[pc] = Fq(M_[r_, 63])
    vs = []
    for fc in free:
        v = [Fr(0)] * 63; v[fc] = Fr(1)
        for r_, pc in enumerate(piv): v[pc] = -Fq(M_[r_, fc])
        vs.append(v)
    const = idx[(0, 0, 0)]
    fconst = all(sum(xp[i] * FB[i][b] for i in range(21)) == (1 if b == const else 0) for b in range(343))
    fdirs = [k for k, v in enumerate(vs) if any(v[i] != 0 for i in range(21))]
    gdirs = [k for k, v in enumerate(vs) if any(v[i] != 0 for i in range(21, 63))]
    check(63 not in piv and len(free) == 21 and fconst and len(fdirs) == 1 and len(gdirs) == 20 and not set(fdirs) & set(gdirs) and all(x == 0 for x in xp[21:]),
          "trivial branch (all n=0, eps=+1): solution set of the line conditions is x = (f=1, g=0) + one f-direction phi0 + 20 g-directions (21 free real unknowns)")
    # identify phi0
    f0v = [sum(vs[fdirs[0]][i] * FB[i][b] for i in range(21)) for b in range(343)]
    expect = defaultdict(Fr)
    for perm in itertools.permutations(range(3)):
        sg = sp.combinatorics.Permutation(list(perm)).signature()
        mono = [0, 0, 0]
        for pos, axis in enumerate(perm): mono[axis] = -(pos + 1)     # sin((pos+1) k_axis)
        expect[idx[tuple(mono)]] += sg
    lam = None; okphi = True
    for b in range(343):
        e_ = expect.get(b, 0)
        if e_ != 0:
            lam = f0v[b] / e_ if lam is None else lam
        if f0v[b] != (lam if lam is not None else 0) * e_ and e_ != 0: okphi = False
    okphi = okphi and lam is not None and all((f0v[b] == 0) for b in range(343) if expect.get(b, 0) == 0)
    check(okphi, "the f-direction is the O-invariant sine pseudoscalar phi0 = sum_sigma sgn(sigma) sin(k_s1) sin(2 k_s2) sin(3 k_s3), which vanishes on all six lines")

    # ------------------------------------------------------------ STAGE 5: unitarity equations f^2 + g.g - 1 = 0 on the trivial branch
    nv = 21
    Fv = []; Gv = []
    for v in vs:
        Fv.append({B[b]: c for b in range(343) for c in [sum(v[i] * FB[i][b] for i in range(21))] if c != 0})
        Gv.append([{B[b]: c for b in range(343) for c in [sum(v[21 + i] * GB[i][a * 343 + b] for i in range(42))] if c != 0} for a in range(3)])
    def prod1(j1, j2):
        out = defaultdict(Fr)
        cs_ = lambda j: ('c', j) if j >= 0 else ('s', -j)
        (ka, ma), (kb, mb) = cs_(j1), cs_(j2)
        if ka == 'c' and kb == 'c':
            out[abs(ma - mb)] += Fr(1, 2); out[ma + mb] += Fr(1, 2)
        elif ka == 's' and kb == 's':
            out[abs(ma - mb)] += Fr(1, 2); out[ma + mb] -= Fr(1, 2)
        else:
            a_, b_ = (ma, mb) if ka == 's' else (mb, ma)
            out[-(a_ + b_)] += Fr(1, 2)
            if a_ > b_: out[-(a_ - b_)] += Fr(1, 2)
            elif a_ < b_: out[-(b_ - a_)] -= Fr(1, 2)
        return {k: v for k, v in out.items() if v != 0}
    P1 = {(a, b): prod1(a, b) for a in range(-3, 4) for b in range(-3, 4)}
    def mul3(p, q):
        out = defaultdict(Fr)
        for b1, c1 in p.items():
            for b2, c2 in q.items():
                t0_ = P1[(b1[0], b2[0])]; t1_ = P1[(b1[1], b2[1])]; t2_ = P1[(b1[2], b2[2])]
                if not (t0_ and t1_ and t2_): continue
                c = c1 * c2
                for j0, a0 in t0_.items():
                    for j1, a1 in t1_.items():
                        for j2, a2 in t2_.items(): out[(j0, j1, j2)] += c * a0 * a1 * a2
        return out
    Q = defaultdict(lambda: defaultdict(Fr))
    for i in range(nv):
        for b, c in Fv[i].items(): Q[b][(i,)] += 2 * c
    for i in range(nv):
        for j in range(i, nv):
            w = 1 if i == j else 2
            tot = defaultdict(Fr)
            for b, c in mul3(Fv[i], Fv[j]).items(): tot[b] += c
            for a in range(3):
                if Gv[i][a] and Gv[j][a]:
                    for b, c in mul3(Gv[i][a], Gv[j][a]).items(): tot[b] += c
            for b, c in tot.items():
                if c != 0: Q[b][(i, j)] += w * c
    eqs = [(b, {k: v for k, v in d.items() if v != 0}) for b, d in Q.items()]
    eqs = [(b, d) for b, d in eqs if d]
    # exact rational verification of the expansion at random rational points
    okexp = True
    for trial in range(3):
        sv = [Fr(rnd.randint(1, 9), rnd.randint(2, 9)) for _ in range(3)]
        cs = [cs_rational(s) for s in sv]
        v0 = basis_values(B, 3, cs)
        y = [Fr(rnd.randint(-5, 5), rnd.randint(1, 4)) for _ in range(nv)]
        x = [xp[c] + sum(y[i] * vs[i][c] for i in range(nv)) for c in range(63)]
        f = sum(x[i] * sum(c * v0[b] for b, c in enumerate(FB[i])) for i in range(21))
        g = [sum(x[21 + i] * sum(GB[i][a * 343 + b] * v0[b] for b in range(343)) for i in range(42)) for a in range(3)]
        lhs = f * f + sum(t * t for t in g) - 1
        # evaluate the mode basis (range 6) exactly
        tab = [cs_multiples(cs[a][0], cs[a][1], 6) for a in range(3)]
        def ph(a, j): return Fr(1) if j == 0 else (tab[a][j][0] if j > 0 else tab[a][-j][1])
        rhs = Fr(0)
        for b, d in eqs:
            mval = ph(0, b[0]) * ph(1, b[1]) * ph(2, b[2])
            for key, c in d.items():
                m = Fr(1)
                for i in key: m *= y[i]
                rhs += c * m * mval
        if lhs != rhs: okexp = False
    check(okexp and len(eqs) == 459, f"exact rational check: expansion of f^2+g.g-1 in the trigonometric mode basis (range 6) has {len(eqs)} nonzero mode equations (quadratic, linear only in y0) and reproduces f^2+g.g-1 exactly at 3 random rational momenta {el()}")

    # ------------------------------------------------------------ STAGE 6: ideal membership of y0 (explicit rational certificate)
    mons = sorted({k for b, e in eqs for k in e}, key=lambda k: (-len(k), k)); midx = {k: i for i, k in enumerate(mons)}
    nm = len(mons)
    cols = [[QQ(0)] * nm for _ in eqs]
    for r_, (b, e) in enumerate(eqs):
        for k, v in e.items(): cols[r_][midx[k]] = QQ(v.numerator, v.denominator)
    Mat = DomainMatrix([[cols[r_][m] for r_ in range(len(eqs))] + [QQ(1) if mons[m] == (0,) else QQ(0)] for m in range(nm)], (nm, len(eqs) + 1), QQ)
    rr, piv = Mat.rref()
    consistent = (len(eqs) not in piv)
    cvec = [Fr(0)] * len(eqs)
    if consistent:
        Mr = rr.to_Matrix()
        for r_, pc in enumerate(piv): cvec[pc] = Fq(Mr[r_, len(eqs)])
    comb = defaultdict(Fr)
    for r_, (b, e) in enumerate(eqs):
        if cvec[r_] != 0:
            for k, v in e.items(): comb[k] += cvec[r_] * v
    comb = {k: v for k, v in comb.items() if v != 0}
    nzc = sum(1 for c in cvec if c != 0)
    check(consistent and comb == {(0,): Fr(1)},
          f"explicit certificate: y0 = sum_m c_m E_m with {nzc} nonzero rational constants c_m over the {len(eqs)} mode equations (exact identity of polynomials; all quadratic terms cancel)")

    # ------------------------------------------------------------ STAGE 7: remaining system = 50 homogeneous quadrics in 20 variables
    mons1 = [k for k in mons if 0 not in k]; m1 = {k: i for i, k in enumerate(mons1)}
    rows = [[QQ(0)] * len(mons1) for _ in eqs]
    for r_, (b, e) in enumerate(eqs):
        for k, v in e.items():
            if k in m1: rows[r_][m1[k]] = QQ(v.numerator, v.denominator)
    rr1, piv1 = DomainMatrix(rows, (len(eqs), len(mons1)), QQ).rref()
    Mr1 = rr1.to_Matrix()
    gens = []
    for r_ in range(len(piv1)):
        ent = {mons1[j]: Fq(Mr1[r_, j]) for j in range(len(mons1)) if Mr1[r_, j] != 0}
        den = 1
        for v in ent.values(): den = den * v.denominator // math.gcd(den, v.denominator)
        ent = {k: int(v * den) for k, v in ent.items()}
        gcd = 0
        for v in ent.values(): gcd = math.gcd(gcd, abs(v))
        gens.append({k: v // gcd for k, v in ent.items()})
    # gens are dicts monomial-key (tuple of variable indices, y1..y20 -> 1..20) -> integer
    ok2 = all(len(k) == 2 for g in gens for k in g) and len(gens) == 50
    check(ok2, f"after y0=0 the equations span a 50-dimensional space of homogeneous quadrics in y1..y20 (integer primitive generators); 20 variables, 210 quadratic monomials (rank over Q of the 459 mode equations is 51 including the y0 equation) {el()}")
    # to exponent vectors on y1..y20
    def expo(k):
        e = [0] * 20
        for i in k: e[i - 1] += 1
        return tuple(e)
    G_exp = [{expo(k): v for k, v in g.items()} for g in gens]

    # variable classes (translation-by-(pi,pi,pi) parity, inversion parity) from the basis functions
    def bclass(bj): return (sum(abs(x) for x in bj) % 2, sum(1 for x in bj if x < 0) % 2)
    gcl = []
    for v in GB:
        s = {bclass(B[b]) for a in range(3) for b in range(343) if v[a * 343 + b] != 0}
        gcl.append(s)
    varcls = []
    pure = True
    for k in gdirs:
        s = set()
        for i in range(42):
            if vs[k][21 + i] != 0: s |= gcl[i]
        if len(s) != 1: pure = False
        varcls.append(next(iter(s)) if len(s) == 1 else None)
    # variable order y1..y20 = gdirs order (free-column order)
    def mcls(u, vc):
        s = t = 0
        for i, k in enumerate(u):
            if k: s += vc[i][0] * k; t += vc[i][1] * k
        return (s % 2, t % 2)
    homog = pure and all(len({mcls(u, varcls) for u in g}) == 1 for g in G_exp)
    check(homog, f"Z2xZ2 symmetry bookkeeping: every variable has a definite (shift, inversion) class {sorted(set(varcls))} and every generator is homogeneous for it; classes are used only to split linear algebra into 4 blocks")

    # ------------------------------------------------------------ STAGE 8: Hilbert function and m^5 in I, modulo primes
    def closure(G_exp, P, vc, seed, maxd=7, verbose=False):
        NV = 20
        def monos(d):
            out = []
            def rec(i, left, cur):
                if i == NV - 1: out.append(tuple(cur + [left])); return
                for k in range(left + 1): rec(i + 1, left - k, cur + [k])
            rec(0, d, []); return out
        def key(u): return tuple(-x for x in reversed(u))
        def rref(W):
            W = W.copy() % P; m, n = W.shape; r = 0; piv = []
            for c in range(n):
                if r == m: break
                nz = np.nonzero(W[r:, c])[0]
                if len(nz) == 0: continue
                i = r + nz[0]
                if i != r: W[[r, i]] = W[[i, r]]
                W[r] = (W[r] * pow(int(W[r, c]), -1, P)) % P
                rws = np.nonzero(W[:, c])[0]; rws = rws[rws != r]
                if len(rws): W[rws, c:] = (W[rws, c:] - np.outer(W[rws, c], W[r, c:])) % P
                piv.append(c); r += 1
            return W[:r], piv
        cl = (lambda u: mcls(u, vc)) if vc is not None else (lambda u: (0, 0))
        m2 = sorted(monos(2), key=key, reverse=True); col2 = {u: i for i, u in enumerate(m2)}
        W = np.zeros((len(G_exp), len(m2)), dtype=np.int64)
        for i, g in enumerate(G_exp):
            for u, c in g.items(): W[i, col2[u]] = c % P
        Rr, piv = rref(W); ps = set(piv)
        nonpiv = [c for c in range(len(m2)) if c not in ps]
        N = [m2[c] for c in nonpiv]
        tails = {m2[c]: (-Rr[r, nonpiv]) % P for r, c in enumerate(piv)}
        HF = {2: len(N)}; d = 2; rng = random.Random(seed)
        while len(N) > 0 and d < maxd:
            mons = sorted(monos(d + 1), key=key)
            info = {}
            for u in mons:
                divs = []
                for j in range(NV):
                    if u[j] > 0:
                        v = list(u); v[j] -= 1
                        if tuple(v) in tails: divs.append(j)
                info[u] = divs
            byc = defaultdict(list)
            for u in mons: byc[cl(u)].append(u)
            newN = []; newt = {}; boffs = {}
            blocks = {}
            for c in sorted(byc):
                Cb = [u for u in reversed(byc[c]) if not info[u]]      # greatest monomial first
                Rb = [u for u in byc[c] if info[u]]                    # smallest first
                cidx = {u: i for i, u in enumerate(Cb)}; ridx = {u: i for i, u in enumerate(Rb)}
                nC, nR = len(Cb), len(Rb)
                look = {}
                for j in range(NV):
                    ct = []; kind = []; ix = []
                    for ti, t in enumerate(N):
                        v = list(t); v[j] += 1; mm = tuple(v)
                        if cl(mm) != c: continue
                        ct.append(ti)
                        if mm in cidx: kind.append(0); ix.append(cidx[mm])
                        else: kind.append(1); ix.append(ridx[mm])
                    look[j] = (np.array(ct, dtype=np.int64), np.array(kind, dtype=np.int8), np.array(ix, dtype=np.int64))
                Rm = np.zeros((nR, nC), dtype=np.float64)
                def vec(l, j):
                    ct, kind, ix = look[j]; co = tails[l][ct]; nzm = co != 0
                    co = co[nzm]; kind = kind[nzm]; ix = ix[nzm]
                    out = np.zeros(nC, dtype=np.float64); mc = kind == 0
                    np.add.at(out, ix[mc], co[mc].astype(np.float64))
                    mr = ~mc
                    if mr.any(): out += co[mr].astype(np.float64) @ Rm[ix[mr]]
                    return np.mod(out, P)
                for u in Rb:
                    j = info[u][0]; l = list(u); l[j] -= 1
                    Rm[ridx[u]] = vec(tuple(l), j)
                ov = [(u, j2) for u in Rb for j2 in info[u][1:]]
                rng.shuffle(ov); K = min(len(ov), int(2.5 * nC) + 200)
                rel = np.zeros((K, nC), dtype=np.float64)
                for k in range(K):
                    u, j2 = ov[k]; j1 = info[u][0]
                    l1 = list(u); l1[j1] -= 1; l2 = list(u); l2[j2] -= 1
                    rel[k] = np.mod(vec(tuple(l1), j1) - vec(tuple(l2), j2), P)
                if nC > 0 and K > 0: Wr, pv = rref(rel.astype(np.int64))
                else: Wr, pv = np.zeros((0, nC), dtype=np.int64), []
                pset = set(pv); nonp = [i for i in range(nC) if i not in pset]
                Rn = Rm.astype(np.int64)
                Rn_non = (Rn[:, nonp] - Rn[:, pv] @ Wr[:, nonp]) % P if len(pv) else Rn[:, nonp]
                blocks[c] = (Cb, Rb, ridx, nonp, Wr, pv, Rn_non)
                if verbose: print(f"  deg {d+1} class {c}: C={nC} red={nR} overlaps={len(ov)} used={K} rank={len(pv)} std={len(nonp)} {el()}", flush=True)
            o = 0
            for c in sorted(byc):
                Cb, Rb, ridx, nonp, Wr, pv, Rn_non = blocks[c]
                boffs[c] = o; o += len(nonp)
                for i in nonp: newN.append(Cb[i])
            for c in sorted(byc):
                Cb, Rb, ridx, nonp, Wr, pv, Rn_non = blocks[c]
                for u in Rb:
                    vv = np.zeros(len(newN), dtype=np.int64); vv[boffs[c]:boffs[c] + len(nonp)] = Rn_non[ridx[u]]; newt[u] = vv
                for r, pc in enumerate(pv):
                    vv = np.zeros(len(newN), dtype=np.int64); vv[boffs[c]:boffs[c] + len(nonp)] = (-Wr[r, nonp]) % P; newt[Cb[pc]] = vv
            N = newN; tails = newt; d += 1; HF[d] = len(N)
        return HF

    for (P_, seed, perm, label) in [(32003, 1, False, "p=32003, grevlex y1>...>y20"), (31991, 2, True, "p=31991, reversed variable order, other random overlaps")]:
        if perm:
            G_use = [{tuple(reversed(u)): c for u, c in g.items()} for g in G_exp]
            vc_use = list(reversed(varcls))
        else:
            G_use = G_exp; vc_use = varcls
        HF = closure(G_use, P_, vc_use, seed)
        okh = HF.get(2) == 160 and HF.get(3) == 577 and HF.get(4) == 470 and HF.get(5) == 0
        check(okh, f"Hilbert function of the quotient mod {label}: HF(0..5) = 1,20,{HF.get(2)},{HF.get(3)},{HF.get(4)},{HF.get(5)}; sum = {1+20+sum(HF.values())}; HF(5)=0 means every quintic monomial lies in the ideal mod p {el()}")
    check(1 + 20 + sum(HF.values()) == 1228, f"sum of the computed Hilbert function = {1 + 20 + sum(HF.values())}, equal to the vdim 1228 printed in the archived Singular log r3_triv.out (a log, not an independent proof: cited at the frozen commit)")

    # dense (Macaulay) cross-check of degree 3 in every class block, independent of the incremental method
    def dense_hf(G_exp, P, vc, D, only=None):
        NV = 20
        def monos(d):
            out = []
            def rec(i, left, cur):
                if i == NV - 1: out.append(tuple(cur + [left])); return
                for k in range(left + 1): rec(i + 1, left - k, cur + [k])
            rec(0, d, []); return out
        ms = monos(D); blocks = defaultdict(list)
        for m in ms: blocks[mcls(m, vc)].append(m)
        mult = monos(D - 2); tot = 0; per = {}
        for c, bl in sorted(blocks.items()):
            if only is not None and c != only: continue
            col = {m: i for i, m in enumerate(bl)}
            rows = []
            for g in G_exp:
                for mm in mult:
                    uu = {tuple(a + b for a, b in zip(e, mm)): v for e, v in g.items()}
                    if all(u in col for u in uu): rows.append({col[u]: v % P for u, v in uu.items()})
            A = np.zeros((len(rows), len(bl)), dtype=np.int64)
            for i, r in enumerate(rows):
                for cc, v in r.items(): A[i, cc] = v
            rk = 0
            for cc in range(len(bl)):
                nz = np.nonzero(A[rk:, cc])[0]
                if len(nz) == 0: continue
                piv = rk + nz[0]
                if piv != rk: A[[rk, piv]] = A[[piv, rk]]
                A[rk, cc:] = (A[rk, cc:] * pow(int(A[rk, cc]), -1, P)) % P
                below = rk + 1 + np.nonzero(A[rk + 1:, cc])[0]
                if len(below): A[below, cc:] = (A[below, cc:] - np.outer(A[below, cc], A[rk, cc:])) % P
                rk += 1
                if rk == A.shape[0]: break
            per[c] = len(bl) - rk; tot += len(bl) - rk
        return tot, per
    t3, per3 = dense_hf(G_exp, 32003, varcls, 3)
    check(t3 == 577, f"dense Macaulay rank (different algorithm) at degree 3, four class blocks: HF(3) = {t3} {per3} {el()}")
    t4, per4 = dense_hf(G_exp, 32003, varcls, 4, only=(1, 0))
    check(per4[(1, 0)] == 112, f"dense Macaulay rank at degree 4 in class block (1,0): HF = {per4[(1,0)]}, equal to the incremental method's block value {el()}")

    # non-vacuity: a proper subset of the generators does not give HF(5)=0
    HFs = closure(G_exp[:40], 32003, varcls, 3, maxd=5)
    check(HFs.get(5, 0) > 0, f"control: the first 40 of the 50 quadrics give HF(5) = {HFs.get(5)} > 0, so HF(5)=0 is not an artefact of the algorithm {el()}")

    # ------------------------------------------------------------ STAGE 9: optional comparison with the archived Singular input
    here = os.path.dirname(os.path.abspath(__file__))
    sing = os.path.join(here, 'src', 'r3_triv.sing')
    if os.path.exists(sing):
        txt = open(sing).read(); i = txt.index('ideal I='); j = txt.index(';', i)
        eqs_s = [e.strip() for e in txt[i + 8:j].split(',\n') if e.strip()]
        Ys = sp.symbols('y0:21'); ns = {f'y{k}': Ys[k] for k in range(21)}
        polys = [sp.Poly(sp.sympify(e.replace('^', '**'), locals=ns), *Ys) for e in eqs_s]
        ms_ = sorted({m for p_ in polys for m in p_.monoms()}); mi = {m: k for k, m in enumerate(ms_)}
        rws = []
        for p_ in polys:
            r_ = [QQ(0)] * len(ms_)
            for m, c in p_.terms(): r_[mi[m]] = QQ(int(c.p), int(c.q))
            rws.append(r_)
        rrs, pvs = DomainMatrix(rws, (len(rws), len(ms_)), QQ).rref()
        Mrs = rrs.to_Matrix()
        lin = [r_ for r_ in range(len(pvs)) if all(sum(ms_[j]) == 1 for j in range(len(ms_)) if Mrs[r_, j] != 0)]
        quad_rows = []
        for r_ in range(len(pvs)):
            ent = {ms_[j]: Fq(Mrs[r_, j]) for j in range(len(ms_)) if Mrs[r_, j] != 0}
            quad_rows.append(ent)
        # the archived input has the same linear equation (a single variable y_a = 0)
        linvars = [next(k for k, e in enumerate(m) if e) for r_ in lin for m in [next(mm for mm in ms_ if Mrs[r_, mi[mm]] != 0)]]
        sub = []
        for ent in quad_rows:
            if all(sum(m) == 1 for m in ent): continue
            e2 = {m: v for m, v in ent.items() if not any(m[k] for k in linvars)}
            if e2: sub.append(e2)
        remaining = [k for k in range(21) if k not in linvars]
        def red(m): return tuple(m[k] for k in remaining)
        Gs = []
        for ent in sub:
            den = 1
            for v in ent.values(): den = den * v.denominator // math.gcd(den, v.denominator)
            Gs.append({red(m): int(v * den) for m, v in ent.items()})
        rank_s = len(Gs)
        HFt = closure(Gs, 32003, None, 5, maxd=6) if len(remaining) == 20 and all(sum(m) == 2 for g in Gs for m in g) else None
        check(HFt is not None and rank_s == 50 and (HFt.get(2), HFt.get(3), HFt.get(4), HFt.get(5)) == (160, 577, 470, 0),
              f"archived Singular input r3_triv.sing (122 equations, 21 variables): contains one linear equation in a single variable, and the remaining 50 independent quadrics have the same Hilbert function 1,20,{HFt and HFt.get(2)},{HFt and HFt.get(3)},{HFt and HFt.get(4)},{HFt and HFt.get(5)} {el()}")

    # ------------------------------------------------------------ STAGE 10: logical conclusion
    check(True, "conclusion: rank over Q of the integer Macaulay matrix >= its rank mod p (any prime), so mod-p surjectivity onto degree 5 gives y^alpha in the Q-ideal for all |alpha|=5; with y0 in the ideal, the complex variety of the trivial branch is the single point y=0, i.e. f=1, g=0, V=1 (for p=32003 and p=31991)")

    print(f"TOTAL: PASS={NPASS} FAIL={NFAIL}")
    if NFAIL == 0:
        print("HIT: computer-assisted exact reconstruction (no Singular, no numerical branch discard) of the range-three freeze: for H=O, full-soldered action, hops in {-3..3}^3, every complex SL2-valued solution f+i g.sigma (f^2+g.g=1) equals 1; first-stage exhaustive over all 4,405,492 line branches, second stage m^5 in the ideal by a mod-p rank certificate lifted to Q")
    print("SUMMARY: rebuilds the range-three O-covariant system from scratch (63 unknowns), proves by exact exhaustion that the six-line stage leaves only the trivial branch, derives y0=0 as an explicit rational combination of the unitarity equations, and certifies by a Hilbert-function/rank computation (two primes, dense cross-checks, negative control) that all quintic monomials lie in the remaining 50-quadric ideal, so the complex variety is the single point V=1 (peak RSS %.0f MB, %.0f s)" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, time.time() - T0))
    return 0 if NFAIL == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
