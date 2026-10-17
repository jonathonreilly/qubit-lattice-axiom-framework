#!/usr/bin/env python3
"""Site-localizable anyons and the spin-1/2 class on the cube rotation group.

Finite group reconstruction (floating-point matrices/characters) for the companion note
SITE_LOCALIZABLE_STABILIZER_CODE_FERMION_CANNOT_CARRY_THE_SPIN_HALF_CLASS_DIRECTION_SHELL_BOUNDED_THEOREM_NOTE_2026-10-17.md

Checks:
  1. O (24 proper cube rotations) and 2O (48 unit quaternions) with the
     covering map 2O -> O.
  2. The four classes of H^2(O; Z2), built as explicit cocycles
     (0, w1^2, w2 from a section of 2O, w2 + w1^2), and for each the
     central extension E: is -1 in [E, E]?  A one-dimensional local state
     with the class exists iff -1 is not a commutator.
  3. For every subgroup H of O (up to conjugacy), whether the restriction
     of w2 admits a one-dimensional realization (H's preimage in 2O has
     a character sending -1 to -1).
  4. Orbit sizes of subgroups: odd orbits of O occur only for stabilizers
     O and D4.
  5. Shells: the induced representations of 2O on the orbit of the six
     directions, the eight octants and the twelve face diagonals, for
     linear and spinorial characters of the stabilizer, decomposed into
     2O irreps.
"""
import itertools
import numpy as np


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("outputs/campaign_c16_c18_landing_2026_10_17/independent_controls/exact-controls.py.txt", "outputs/campaign_c16_c18_landing_2026_10_17/independent_controls/exact-controls.json")

def _run_reviewed_program():
    global A, ALL, B, D2, D2l, DIRS, E, E2, FAIL, G2, H, H2_basis, INV2, M1, MUL, MUL2, N, N2, PASS, PAULI, R, ROT, S, SEC, U, W1, a, a_el, b, b_el, binary_octahedral, c, cc, check, chi_E12, chi_E52, chi_G32, chi_spin2, closure, cocycle, coeffs, conj_class, coords, d, dec, deg, describe, expect_deg, extension_minus_one_is_commutator, fmt, g, gens, h, idx2, inner, invs, irreps, k, kchar, label, lin, m, n, name, odd, ok_dir, ok_face, ok_oct, ok_patterns, orbit_sizes, order_of, order_of2, out, patterns, perm_sign, proj, quat_to_su2, reps, res, ridx, shell, size, spin, spin_char, spin_decs, spinors, squares, su2_to_so3, subgroups, table, v, vec, w1, w2, x, y
    PASS = 0
    FAIL = 0


    def check(name, ok, detail=""):
        global PASS, FAIL
        if ok:
            PASS += 1
        else:
            FAIL += 1
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


    # ---------------------------------------------------------------- groups
    def quat_to_su2(q):
        a, b, c, d = q
        return np.array([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]])


    def binary_octahedral():
        qs = []
        for i in range(4):
            for s in (1, -1):
                v = [0, 0, 0, 0]
                v[i] = s
                qs.append(v)
        for signs in itertools.product((1, -1), repeat=4):
            qs.append([s / 2 for s in signs])
        r = 1 / np.sqrt(2)
        for i, j in itertools.combinations(range(4), 2):
            for si, sj in itertools.product((1, -1), repeat=2):
                v = [0, 0, 0, 0]
                v[i], v[j] = si * r, sj * r
                qs.append(v)
        return [quat_to_su2(q) for q in qs]


    PAULI = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]),
             np.array([[1, 0], [0, -1]])]


    def su2_to_so3(U):
        R = np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                R[i, j] = 0.5 * np.real(np.trace(PAULI[i] @ U @ PAULI[j] @ U.conj().T))
        return np.rint(R).astype(int)


    G2 = binary_octahedral()
    N2 = len(G2)


    def idx2(U):
        for k, V in enumerate(G2):
            if np.allclose(U, V, atol=1e-9):
                return k
        raise ValueError


    MUL2 = np.array([[idx2(A @ B) for B in G2] for A in G2])
    E2 = idx2(np.eye(2))
    M1 = idx2(-np.eye(2))
    INV2 = [int(np.where(MUL2[a] == E2)[0][0]) for a in range(N2)]

    ROT = []
    proj = []
    for U in G2:
        R = su2_to_so3(U)
        for k, S in enumerate(ROT):
            if (S == R).all():
                proj.append(k)
                break
        else:
            ROT.append(R)
            proj.append(len(ROT) - 1)
    N = len(ROT)
    check("O has 24 proper rotations, 2O has 48 elements, 2O -> O is 2:1",
          N == 24 and N2 == 48 and all(proj.count(k) == 2 for k in range(N))
          and all(round(np.linalg.det(R)) == 1 for R in ROT))


    def ridx(R):
        for k, S in enumerate(ROT):
            if (S == R).all():
                return k
        raise ValueError


    MUL = np.array([[ridx(A @ B) for B in ROT] for A in ROT])
    E = ridx(np.eye(3, dtype=int))

    # section O -> 2O and the w2 cocycle
    SEC = [proj.index(k) for k in range(N)]


    def w2(g, h):
        prod = MUL2[SEC[g], SEC[h]]
        return 0 if prod == SEC[MUL[g, h]] else 1


    # w1: sign of the permutation of the six directions (+-e_a)
    DIRS = [tuple(int(x) for x in v) for v in
            (np.eye(3, dtype=int).tolist() + (-np.eye(3, dtype=int)).tolist())]


    def perm_sign(p):
        p = list(p)
        s = 1
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                s = -s
        return s


    def w1(g):
        R = ROT[g]
        p = [DIRS.index(tuple(int(x) for x in R @ np.array(d))) for d in DIRS]
        return 0 if perm_sign(p) == 1 else 1


    W1 = [w1(g) for g in range(N)]


    def cocycle(a, b):
        return lambda g, h: (a * w2(g, h) + b * W1[g] * W1[h]) % 2


    def extension_minus_one_is_commutator(c, elems):
        """Central extension of the subgroup `elems` by Z2 with cocycle c.
        Elements (g, s); (g,s)(h,t) = (gh, s+t+c(g,h)).  Returns whether
        (e, 1) lies in the commutator subgroup."""
        def mul(x, y):
            return (MUL[x[0], y[0]], (x[1] + y[1] + c(x[0], y[0])) % 2)

        ext = [(g, s) for g in elems for s in (0, 1)]
        ident = (E, c(E, E) % 2)  # identity is (e, c(e,e)) for a normalized cocycle

        def inv(x):
            for y in ext:
                if mul(x, y) == ident:
                    return y
            raise ValueError

        comms = {mul(mul(x, y), mul(inv(x), inv(y))) for x in ext for y in ext}
        sub = set(comms)
        frontier = set(sub)
        while frontier:
            new = {mul(a, b) for a in frontier for b in sub} | {mul(b, a) for a in frontier for b in sub}
            new -= sub
            sub |= new
            frontier = new
        minus = (E, (ident[1] + 1) % 2)
        return minus in sub


    ALL = list(range(N))
    # normalization: w2(e, e) = 0 since SEC[e] = identity
    check("section is normalized (w2(e,e) = 0) and w2 is a cocycle",
          w2(E, E) == 0 and all((w2(g, h) + w2(MUL[g, h], k) + w2(h, k) + w2(g, MUL[h, k])) % 2 == 0
                                for g in ALL for h in ALL for k in ALL))

    res = {}
    for a, b, name in ((0, 0, "0"), (0, 1, "w1^2"), (1, 0, "w2"), (1, 1, "w2+w1^2")):
        res[name] = extension_minus_one_is_commutator(cocycle(a, b), ALL)
    print("   O: -1 in [E,E] for class:", res)
    check("on O, a one-dimensional local state exists exactly for the classes 0 and w1^2 "
          "(the kernel of H^2(O;Z2) -> H^2(O;U(1))); never for w2 or w2+w1^2",
          res == {"0": False, "w1^2": False, "w2": True, "w2+w1^2": True})


    # ---------------------------------------------------------------- subgroups
    def closure(gens):
        s = {E}
        frontier = {E}
        while frontier:
            new = {MUL[a, g] for a in frontier for g in gens} - s
            s |= new
            frontier = new
        return frozenset(s)


    subgroups = set()
    for k in range(1, 3):
        for gens in itertools.combinations(ALL, k):
            subgroups.add(closure(gens))
    subgroups = list(subgroups)


    def conj_class(H):
        return frozenset(frozenset(MUL[MUL[g, h], [x for x in ALL if MUL[g, x] == E][0]] for h in H)
                         for g in ALL)


    reps = {}
    for H in subgroups:
        cc = conj_class(H)
        if cc not in reps:
            reps[cc] = H
    print(f"   conjugacy classes of subgroups of O: {len(reps)}")
    check("O has 11 conjugacy classes of subgroups", len(reps) == 11)


    def order_of(g):
        k, x = 1, g
        while x != E:
            x = MUL[x, g]
            k += 1
        return k


    def describe(H):
        n = len(H)
        orders = sorted(order_of(h) for h in H)
        axisC2 = sum(1 for h in H if order_of(h) == 2 and W1[h] == 0)
        edgeC2 = sum(1 for h in H if order_of(h) == 2 and W1[h] == 1)
        if n == 1:
            return "1"
        if n == 24:
            return "O"
        if n == 12:
            return "T"
        if n == 8:
            return "D4"
        if n == 6:
            return "D3" if 2 in orders else "C6?"
        if n == 4:
            if 4 in orders:
                return "C4"
            return "D2(axis)" if axisC2 == 3 else "D2(axis+edge)"
        if n == 3:
            return "C3"
        if n == 2:
            return "C2(axis)" if axisC2 else "C2(edge)"
        return f"order{n}"


    table = {}
    for H in reps.values():
        name = describe(H)
        table[name] = (len(H), extension_minus_one_is_commutator(cocycle(1, 0), sorted(H)))
    print("   restriction of w2: (|H|, needs dimension >= 2)")
    for name in sorted(table, key=lambda s: table[s][0]):
        print(f"     {name:16s} |H|={table[name][0]:2d}  degenerate-only={table[name][1]}")
    expect_deg = {"1": False, "C2(axis)": False, "C2(edge)": False, "C3": False, "C4": False,
                  "D2(axis)": True, "D2(axis+edge)": True, "D3": False, "D4": True,
                  "T": True, "O": True}
    check("w2 needs a local dimension >= 2 exactly for D2 (both classes), D4, T, O; "
          "cyclic groups and D3 admit a one-dimensional spin-1/2 local state",
          {k: v[1] for k, v in table.items()} == expect_deg)

    # D2(axis): the eight square patterns; one-dimensional iff even number of -1
    D2 = [H for H in reps.values() if describe(H) == "D2(axis)"][0]
    D2l = sorted(D2)
    invs = [h for h in D2l if h != E]
    H2_basis = []
    ok_patterns = True
    patterns = {}
    for coeffs in itertools.product((0, 1), repeat=3):
        # cocycle on D2 = Z2 x Z2 with generators a, b: x_a^2, x_b^2, x_a x_b
        a_el, b_el = invs[0], invs[1]

        def coords(g):
            if g == E:
                return (0, 0)
            if g == a_el:
                return (1, 0)
            if g == b_el:
                return (0, 1)
            return (1, 1)

        def c(g, h, co=coeffs):
            (g1, g2), (h1, h2) = coords(g), coords(h)
            return (co[0] * g1 * h1 + co[1] * g2 * h2 + co[2] * g1 * h2) % 2

        squares = tuple(c(x, x) for x in invs)
        deg = extension_minus_one_is_commutator(c, D2l)
        patterns[squares] = deg
        if deg != (sum(squares) % 2 == 1):
            ok_patterns = False
    check("axis D2: all 8 square patterns occur; a one-dimensional state exists iff the "
          "number of C2 lifts squaring to -1 is even (so (-,-,-) is excluded)",
          len(patterns) == 8 and ok_patterns and patterns[(1, 1, 1)] is True)

    # ---------------------------------------------------------------- orbits
    orbit_sizes = {describe(H): N // len(H) for H in reps.values()}
    odd = sorted(k for k, v in orbit_sizes.items() if v % 2 == 1)
    check("an O-orbit has odd size only when the stabilizer is O (size 1) or D4 (size 3)",
          odd == ["D4", "O"], f"odd-orbit stabilizers {odd}")


    # ---------------------------------------------------------------- shells
    def spin_char(j2, U):
        """Character of the spin j = j2/2 representation at U in SU(2)."""
        tr = np.real(np.trace(U)) / 2
        tr = max(-1.0, min(1.0, tr))
        th = 2 * np.arccos(tr)
        if abs(np.sin(th / 2)) < 1e-12:
            return float(j2 + 1) * (1 if np.isclose(tr, 1) else (-1) ** j2)
        return np.sin((j2 + 1) * th / 2) / np.sin(th / 2)


    chi_E12 = np.array([spin_char(1, U) for U in G2])
    chi_G32 = np.array([spin_char(3, U) for U in G2])
    chi_E52 = np.array([spin_char(5, U) for U in G2]) - chi_G32
    lin = {}
    lin["A1"] = np.ones(N2)
    lin["T1"] = np.array([spin_char(2, U) for U in G2])
    # A2 = sign character w1 pulled back; E, T2 from spin-2 = E + T2
    lin["A2"] = np.array([(-1.0) ** W1[proj[k]] for k in range(N2)])
    chi_spin2 = np.array([spin_char(4, U) for U in G2])
    lin["T2"] = lin["T1"] * lin["A2"]
    lin["E"] = chi_spin2 - lin["T2"]
    spinors = {"E1/2": chi_E12, "E5/2": chi_E52, "G3/2": chi_G32}
    irreps = {**lin, **spinors}


    def inner(a, b):
        return np.sum(np.conj(a) * b) / N2


    check("the 8 irreps of 2O are orthonormal (5 linear, 3 spinorial; sum of squared dims 48)",
          all(np.isclose(inner(irreps[x], irreps[y]), 1.0 if x == y else 0.0, atol=1e-9)
              for x in irreps for y in irreps)
          and sum(round(irreps[x][E2].real) ** 2 for x in irreps) == 48)


    def shell(vec, label):
        """Induced representations of 2O from the stabilizer of the position `vec`
        (an orbit under O), for every character of the (cyclic) stabilizer lift."""
        v = np.array(vec)
        Ht = [k for k in range(N2) if (ROT[proj[k]] @ v == v).all()]
        size = N2 // len(Ht)
        # generator convention: maximal order, then largest real trace (trace +sqrt 2 for Z8)
        gen = max(Ht, key=lambda k: (order_of2(k), round(np.real(np.trace(G2[k])), 9)))
        n = order_of2(gen)
        assert n == len(Ht), "stabilizer lift must be cyclic"
        powers = {}
        x = E2
        for m in range(n):
            powers[x] = m
            x = MUL2[x, gen]
        out = {}
        for kchar in range(n):
            zeta = np.exp(2j * np.pi * kchar / n)
            chi = {h: zeta ** powers[h] for h in Ht}
            spin = np.isclose(chi[M1], -1)
            ind = np.zeros(N2, dtype=complex)
            for g in range(N2):
                s = 0
                for xg in range(N2):
                    y = MUL2[MUL2[INV2[xg], g], xg]
                    if y in chi:
                        s += chi[y]
                ind[g] = s / len(Ht)
            dec = {name: int(round(inner(ch, ind).real)) for name, ch in irreps.items()}
            dec = {k: m for k, m in dec.items() if m}
            out[kchar] = (spin, dec)
        return size, n, out


    def order_of2(k):
        m, x = 1, k
        while x != E2:
            x = MUL2[x, k]
            m += 1
        return m


    def fmt(dec):
        return " + ".join(f"{m}{k}" if m > 1 else k for k, m in dec.items())


    ok_dir = ok_oct = ok_face = True
    for vec, label in (((0, 0, 1), "six directions (half-edges / direction qubits)"),
                       ((1, 1, 1), "eight octants (cubes around the site)"),
                       ((1, 1, 0), "twelve face diagonals (plaquette corners)")):
        size, n, out = shell(vec, label)
        print(f"   shell: {label}: orbit {size}, stabilizer lift Z{n}")
        for kchar, (spin, dec) in out.items():
            print(f"     character k={kchar} ({'spinorial' if spin else 'linear'}): {fmt(dec)}")
        if size == 6:
            ok_dir = (out[0][1] == {"A1": 1, "T1": 1, "E": 1}
                      and out[1][1] == {"E1/2": 1, "G3/2": 1} and out[7][1] == {"E1/2": 1, "G3/2": 1}
                      and out[3][1] == {"E5/2": 1, "G3/2": 1} and out[5][1] == {"E5/2": 1, "G3/2": 1})
        if size == 8:
            spin_decs = [dec for (spin, dec) in out.values() if spin]
            ok_oct = (out[0][1] == {"A1": 1, "A2": 1, "T1": 1, "T2": 1}
                      and all(sum(irreps[k][E2].real * m for k, m in d.items()) == 8 for d in spin_decs)
                      and any("E1/2" in d for d in spin_decs))
        if size == 12:
            spin_decs = [dec for (spin, dec) in out.values() if spin]
            ok_face = all("E1/2" in d for d in spin_decs)
    check("six directions: linear shell A1 + E + T1; every spinorial shell is "
          "E1/2 + G3/2 (k = 1, 7) or E5/2 + G3/2 (k = 3, 5)", ok_dir)
    check("eight octants: linear shell A1 + A2 + T1 + T2; spinorial shells have dimension 8 "
          "and some contain E1/2", ok_oct)
    check("twelve face diagonals: every spinorial shell contains E1/2", ok_face)

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

    raise SystemExit(1 if FAIL else 0)

if __name__ == "__main__":
    _run_reviewed_program()
