#!/usr/bin/env python3
"""J:note falsifier for CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02 (on main).

Falsifiers implemented: "a frame-free Spin(3)/Pin(3)-equivariant grade-1 endomorphism that is not a scalar and anticommutes
with Gamma_chi", "an error in the exact commutant solve or in one of the named operation matrices" and "one of the tested ambient
Clifford operations has a different grade-1 action".

The note's runner solves [M, L_k] = 0 for the three so(3) generators on the 3-dim grade-1 block. Disjoint machinery here, all exact:
  1. the WHOLE algebra Cl(3,0) in the Pauli model, real basis {1, s1, s2, s3, b1=s2s3, b2=s3s1, b3=s1s2, w=s1s2s3}; every real-linear
     map X of the 8-dim algebra (64 unknowns) commuting with the action of GROUP ELEMENTS (four exact rational SU(2) rotors, not Lie
     generators), exact nullspace; three readings: Spin(3) by adjoint action; Pin(3) by algebra automorphisms (grade involution added);
     Pin(3) by the twisted adjoint x -> alpha(g) x g^-1 (the vector s1 added). The grade-1 -> grade-1 block of every equivariant map
     (routes through the other grades included) is tested for scalarity and for anticommuting with Gamma_chi = (2/3)J - I.
  2. the note's table rows computed from their definitions on products of generator matrices (reversal of the factor order, sign
     flip of every generator), cross-checked against matrix formulas (X^dag, s2 conj(X) s2, s2 X^T s2); the Hodge row against an
     exterior algebra built from index tuples (e_j ^ *e_i = delta_ij e1^e2^e3); conjugation by the even [1,1,1] element b1+b2+b3;
     the coordinate bivector commutators [b_k, -].
  3. the anticommutant of Gamma_chi in End(R^3) (all of it, not only the equivariant part), split into symmetric and antisymmetric
     parts; the L4 family H = (1/3)(1 h^T + h 1^T), sum h = 0, symbolically; the single-axis family a I + b v v^T.
  4. analogue outside the note's scope (beyond its size): grade 1 of Cl(n,0), Gamma_n = (2/n)J - I, SO(n) from exact Cayley
     rotations and O(n) with one reflection added, n = 2, 4, 5, 6.
HIT lines only for the note's own rows and claims (n = 3); items 3's antisymmetric part and 4 are reported as numbers.
"""
from __future__ import annotations


import sympy as sp

R = sp.Rational
I2 = sp.eye(2)
S = {1: sp.Matrix([[0, 1], [1, 0]]), 2: sp.Matrix([[0, -sp.I], [sp.I, 0]]), 3: sp.Matrix([[1, 0], [0, -1]])}
BLADES = [(), (1,), (2,), (3,), (2, 3), (3, 1), (1, 2), (1, 2, 3)]
GRADE = [len(b) for b in BLADES]


def product(factors):
    M = I2
    for f in factors:
        M = M * f
    return M


BASIS = [product([S[k] for k in b]) for b in BLADES]


def coords(M):
    """real coordinates in BASIS; the basis is orthonormal for <A, B> = Re tr(A^dag B) / 2."""
    return [sp.re(sp.expand((B.H * M).trace())) / 2 for B in BASIS]


def matrix_of(op):
    cols = [coords(op(B)) for B in BASIS]
    return sp.Matrix(8, 8, lambda i, j: cols[j][i])


def blade_op(sign_of_generator, reverse):
    """the linear map sending the blade s_{i1}...s_{ik} to (sign s_{i1})...(sign s_{ik}), factor order reversed if asked."""
    cols = []
    for b in BLADES:
        fs = [sign_of_generator * S[k] for k in b]
        cols.append(coords(product(fs[::-1] if reverse else fs)))
    return sp.Matrix(8, 8, lambda i, j: cols[j][i])


def rotor(a, b, c, d):
    assert a * a + b * b + c * c + d * d == 1
    return a * I2 - sp.I * (b * S[1] + c * S[2] + d * S[3])


ROTORS = [rotor(R(3, 5), R(4, 5), 0, 0), rotor(R(2, 3), R(2, 3), R(1, 3), 0), rotor(R(1, 2), R(1, 2), R(1, 2), R(1, 2)),
          rotor(R(2, 7), 0, R(3, 7), R(6, 7))]


def commutant(gens, n):
    xs = sp.symbols(f"x0:{n * n}")
    X = sp.Matrix(n, n, xs)
    eqs = []
    for A in gens:
        eqs += list(X * A - A * X)
    M, _ = sp.linear_eq_to_matrix(eqs, xs)
    return [sp.Matrix(n, n, list(v)) for v in M.nullspace()]


def anticommuting_members(space, G):
    """dimension of {X in span(space) : X G + G X = 0}."""
    if not space:
        return 0
    cs = sp.symbols(f"c0:{len(space)}")
    X = sum((c * B for c, B in zip(cs, space)), sp.zeros(*G.shape))
    M, _ = sp.linear_eq_to_matrix(list(X * G + G * X), cs)
    images = [list(X.subs(dict(zip(cs, s)))) for s in M.nullspace()]
    return sp.Matrix(images).rank() if images else 0


def is_zero(M):
    return all(sp.simplify(e) == 0 for e in M)


# ----- a tiny exterior algebra on R^3 from index tuples (independent of the Pauli matrices) -----
def wedge(a, b):
    """wedge of two basis blades given as tuples; returns (sign, sorted tuple) or (0, None)."""
    idx = list(a) + list(b)
    if len(set(idx)) < len(idx):
        return 0, None
    sign = 1
    arr = idx[:]
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sign = -sign
    return sign, tuple(arr)


BIV_EXT = [((2, 3), 1), ((1, 3), -1), ((1, 2), 1)]  # b1 = e2^e3, b2 = e3^e1 = -e1^e3, b3 = e1^e2


def hodge_grade1_exterior():
    """column i = coordinates of *e_i in (b1, b2, b3), from e_j ^ *e_i = delta_ij e1^e2^e3."""
    beta = sp.symbols("beta1:4")
    cols = []
    for i in (1, 2, 3):
        eqs = []
        for j in (1, 2, 3):
            top = 0
            for (blade, sgn), bk in zip(BIV_EXT, beta):
                s, t = wedge((j,), blade)
                if s:
                    assert t == (1, 2, 3)
                    top += s * sgn * bk
            eqs.append(sp.Eq(top, 1 if i == j else 0))
        sol = sp.solve(eqs, beta, dict=True)[0]
        cols.append([sol[b] for b in beta])
    return sp.Matrix(3, 3, lambda r, c: cols[c][r])


def cayley(Sk):
    n = Sk.shape[0]
    return (sp.eye(n) - Sk).inv() * (sp.eye(n) + Sk)


def skew(n, seed):
    M = sp.zeros(n, n)
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            k += 1
            M[i, j] = R(((seed * (k + 2) + k * 5 + i * 3 + j) % 7) - 3, 2)
            M[j, i] = -M[i, j]
    return M


def main():
    Gamma = R(2, 3) * sp.ones(3, 3) - sp.eye(3)
    ads = [matrix_of(lambda X, g=g: g * X * g.H) for g in ROTORS]
    sane = all(A[1:4, 1:4].T * A[1:4, 1:4] == sp.eye(3) and A[1:4, 1:4].det() == 1 and A[0, 0] == 1 and A[7, 7] == 1 for A in ads)
    gi_full = blade_op(-1, False)
    twisted_s1 = matrix_of(lambda X: (-S[1]) * X * S[1].inv())
    print(f"1. four rational rotors: adjoints are rotations on grade 1 fixing grades 0 and 3: {sane}; twisted adjoint of s1 on grade 1 = "
          f"{twisted_s1[1:4, 1:4].tolist()}")
    fails = []
    dims = {}
    for label, gens in (("Spin(3) adjoint", ads), ("Pin(3) automorphisms", ads + [gi_full]), ("Pin(3) twisted adjoint", ads + [twisted_s1])):
        comm = commutant(gens, 8)
        blocks = [X[1:4, 1:4] for X in comm]
        scalar = all(is_zero(Bk - Bk[0, 0] * sp.eye(3)) for Bk in blocks)
        n_anti = anticommuting_members(blocks, Gamma)
        dims[label] = len(comm)
        print(f"   {label}: equivariant real-linear maps of the 8-dim algebra: dimension {len(comm)}; every grade-1 block scalar: {scalar}; "
              f"nonzero grade-1 blocks anticommuting with Gamma_chi: {n_anti}")
        if not (scalar and n_anti == 0):
            fails.append(label)

    g1 = lambda M: M[1:4, 1:4]
    rev_full, cc_full = blade_op(1, True), blade_op(-1, True)
    cross = (matrix_of(lambda X: X.H) == rev_full, matrix_of(lambda X: S[2] * X.conjugate() * S[2]) == gi_full,
             matrix_of(lambda X: S[2] * X.T * S[2]) == cc_full)
    w = BASIS[7]
    pc = g1(matrix_of(lambda X: w * X * w.inv()))
    q = BASIS[4] + BASIS[5] + BASIS[6]
    q_even = coords(q)
    qc = g1(matrix_of(lambda X: q * X * q.inv()))
    hodge_pauli = sp.Matrix(3, 3, lambda r, c: coords(w * BASIS[1 + c])[4 + r])
    hodge_ext = hodge_grade1_exterior()
    rows = [("grade involution", g1(gi_full), -sp.eye(3)), ("reversion", g1(rev_full), sp.eye(3)), ("Clifford conjugation", g1(cc_full), -sp.eye(3)),
            ("pseudoscalar conjugation", pc, sp.eye(3)), ("Hodge omega*s_k -> b_k (index map)", hodge_pauli, sp.eye(3)),
            ("conjugation by the even [1,1,1] element b1+b2+b3", qc, Gamma)]
    print(f"2. matrix-formula cross-checks (reversion = X^dag, grade involution = s2 conj(X) s2, Clifford conjugation = s2 X^T s2): {cross}; "
          f"b1+b2+b3 coordinates {q_even} (even: {all(q_even[i] == 0 for i in (0, 1, 2, 3, 7))}); exterior-algebra Hodge *e_i in (b1,b2,b3) = "
          f"{hodge_ext.tolist()}")
    for name, got, want in rows:
        anti = is_zero(got * Gamma + Gamma * got)
        print(f"   {name}: grade-1 action {got.tolist()}; note's table {want.tolist()}: {got == want}; anticommutes with Gamma_chi: {anti}")
        if got != want or anti:
            fails.append(name)
    if not (all(cross) and hodge_ext == sp.eye(3)):
        fails.append("cross-checks")
    ad_b = []
    for k in range(3):
        bk = BASIS[4 + k]
        A = g1(matrix_of(lambda X, bk=bk: bk * X - X * bk))
        ad_b.append(A)
        anti = is_zero(A * Gamma + Gamma * A)
        print(f"   [b{k + 1}, -] on grade 1 = {A.tolist()} (antisymmetric: {A.T == -A}); anticommutes with Gamma_chi: {anti}")
        if anti or A.T != -A:
            fails.append(f"[b{k + 1},-]")

    xs = sp.symbols("y0:9")
    X = sp.Matrix(3, 3, xs)
    M, _ = sp.linear_eq_to_matrix(list(X * Gamma + Gamma * X), xs)
    anti_space = [sp.Matrix(3, 3, list(v)) for v in M.nullspace()]
    sym = [B + B.T for B in anti_space]
    asym = [B - B.T for B in anti_space]
    rank = lambda L: sp.Matrix([list(B) for B in L]).rank() if L else 0
    cs = sp.symbols("c1:4")
    adb = sum((c * A for c, A in zip(cs, ad_b)), sp.zeros(3, 3))
    Mb, _ = sp.linear_eq_to_matrix(list(adb * Gamma + Gamma * adb), cs)
    cb = Mb.nullspace()
    cb_sum_zero = all(sum(v) == 0 for v in cb)
    c_ex = sp.Matrix([1, -1, 0])
    A_ex = adb.subs(dict(zip(cs, c_ex)))
    v = sp.ones(3, 1) / sp.sqrt(3)
    what = (c_ex.cross(v)) / sp.sqrt(c_ex.dot(c_ex))
    xp = v - sp.I * what
    lam = A_ex.eigenvals()
    mu = sp.simplify(sp.radsimp(sp.expand_complex((A_ex * xp)[0] / xp[0])))
    xp_eig = is_zero(A_ex * xp - mu * xp)
    herm = sp.simplify(sum(sp.Abs(e) ** 2 for e in xp) / sp.Abs(sum(xp)) ** 2)
    bil = sp.simplify(sum(e ** 2 for e in xp) / sum(xp) ** 2)
    print(f"3. anticommutant of Gamma_chi in End(R^3): dimension {len(anti_space)} = symmetric {rank(sym)} + antisymmetric {rank(asym)}; "
          f"bivector commutators [c1 b1 + c2 b2 + c3 b3, -] anticommuting with Gamma_chi: dimension {len(cb)}, all with c1+c2+c3 = 0: {cb_sum_zero}; "
          f"example [b1 - b2, -] = {A_ex.tolist()}, eigenvalues {lam}; v - i w (w = c x v/|c|) is its eigenvector for {mu}: {xp_eig}; there sum|x|^2/|sum x|^2 = {herm}, "
          f"sum x^2/(sum x)^2 = {bil}")

    h1, h2 = sp.symbols("h1 h2", real=True)
    h = sp.Matrix([h1, h2, -h1 - h2])
    one = sp.ones(3, 1)
    H = (one * h.T + h * one.T) / 3
    anti_H = is_zero(H * Gamma + Gamma * H)
    nh = sp.sqrt(h.dot(h))
    Qs = []
    for sign in (1, -1):
        x = sign * nh / sp.sqrt(3) * one + h
        eig_ok = is_zero(H * x - sign * nh / sp.sqrt(3) * x)
        Qs.append((eig_ok, sp.simplify(sum(xi ** 2 for xi in x) / sum(x) ** 2)))
    a, b = sp.symbols("a b")
    single = is_zero((a * sp.eye(3) + b * v * v.T) * Gamma - Gamma * (a * sp.eye(3) + b * v * v.T))
    print(f"   L4 family: {{H, Gamma_chi}} = 0 for every h with sum 0: {anti_H}; nonzero eigenvectors (eigen, Q): {Qs}; a I + b vv^T commutes "
          f"with Gamma_chi: {single}")
    if not (anti_H and all(e and Q == R(2, 3) for e, Q in Qs) and single):
        fails.append("L4/single-axis")

    analog = {}
    for n in (2, 4, 5, 6):
        rots = [cayley(skew(n, s)) for s in range(4)]
        assert all(Q.T * Q == sp.eye(n) and Q.det() == 1 for Q in rots)
        Gn = R(2, n) * sp.ones(n, n) - sp.eye(n)
        cso = commutant(rots, n)
        refl = sp.diag(*([-1] + [1] * (n - 1)))
        co = commutant(rots + [refl], n)
        analog[n] = (len(cso), anticommuting_members(cso, Gn), len(co), anticommuting_members(co, Gn))
    print(f"4. analogue outside the note's scope, grade 1 of Cl(n,0), Gamma_n = (2/n)J - I, four exact Cayley rotations (+ one reflection): "
          + "; ".join(f"n={n}: SO(n) commutant dim {d1}, anticommuting {a1}; O(n) commutant dim {d2}, anticommuting {a2}"
                      for n, (d1, a1, d2, a2) in analog.items()))

    if fails or not sane:
        print(f"HIT: a falsifier fires at n = 3: {fails} (rotor sanity {sane})")
        print("SUMMARY: falsifier fired; see the HIT line")
    else:
        print(f"SUMMARY: the falsifiers do not fire: over the whole 8-dim algebra the equivariant real-linear maps (Spin(3) adjoint: dimension "
              f"{dims['Spin(3) adjoint']}; Pin(3) automorphisms: {dims['Pin(3) automorphisms']}; Pin(3) twisted adjoint: "
              f"{dims['Pin(3) twisted adjoint']}; from four exact rational rotors) all have scalar grade-1 blocks and none anticommutes with "
              f"Gamma_chi; the seven table rows computed from their definitions (the last as the three coordinate generators [b_k,-]) "
              f"equal the note's matrices and none anticommutes with Gamma_chi; beyond the table: the anticommutant of Gamma_chi has dimension {len(anti_space)} = L4 (symmetric, "
              f"{rank(sym)}) + the bivector commutators [b,-] with c1+c2+c3 = 0 (antisymmetric, {len(cb)}); analogue outside the note's "
              f"scope: at n = 2 the SO(2) commutant has dimension {analog[2][0]} with {analog[2][1]} direction anticommuting with Gamma_2, "
              f"O(2) dimension {analog[2][2]}; at n = 4, 5, 6 SO(n) dimension {analog[4][0]}, {analog[5][0]}, {analog[6][0]}")


if __name__ == "__main__":
    main()
