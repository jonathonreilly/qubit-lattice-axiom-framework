"""A33 P2-A core: period-2 covariant stabilizer states with ONE generator per site.

Roles: o = x mod 2 (vertex roles at even sites, the state's pattern label s = 0).
  |o| = 0 -> V (site group O);  |o| = 3 -> C (cube role, O);
  |o| = 1 -> E, axis a = the odd coordinate (site group D4_a);
  |o| = 2 -> F, normal c = the even coordinate (site group D4_c).
The generator at x has shape g_role (E/F shapes are given for reference axis z and turned by a
fixed R_a with R_a e_z = e_a; exact D4_z invariance makes this choice-free). All shapes live in the
ball |d|^2 <= r2. The space group of every such state is P432 on the coarse lattice 2Z^3:
translations 2Z^3 and the 24 turns about any vertex-role site (A25's role layout).
"""
import itertools
from p2lib import (group, invariant_basis, ball_sites, combo, rot_pattern, axis_rotation, pcomm,
                   translate, exact_invariant, popc)

ROLES = ("V", "C", "E", "F")


def role_of(x):
    o = tuple(c % 2 for c in x)
    w = sum(o)
    if w == 0:
        return "V", None
    if w == 3:
        return "C", None
    if w == 1:
        return "E", o.index(1)
    return "F", o.index(0)


def shape_at(shape_ref, role, axis, x):
    """place a role shape at site x (E/F turned from reference axis z to `axis`). Mod-2 + sign."""
    if role in ("E", "F") and axis != 2:
        s, p = rot_pattern(axis_rotation(axis), shape_ref)
    else:
        s, p = 1, dict(shape_ref)
    return s, translate(p, x)


class Space:
    def __init__(self, r2):
        self.r2 = r2
        B = ball_sites(r2)
        self.ball = B
        self.rinf = max(max(abs(c) for c in y) for y in B)
        self.basis = {"V": invariant_basis(B, group("O"))[0], "C": invariant_basis(B, group("O"))[0],
                      "E": invariant_basis(B, group("D4", 2))[0], "F": invariant_basis(B, group("D4", 2))[0]}
        self.dim = {r: len(self.basis[r]) for r in ROLES}

    def placed_basis(self, x):
        role, axis = role_of(x)
        out = []
        for b in self.basis[role]:
            _, p = shape_at(b, role, axis, x)
            out.append(p)
        return role, out

    def bilinear_constraints(self):
        """dict (R1,R2) -> set of matrices (tuple of row bitmasks over R2 coefficients) such that
        all commutation conditions read c1^T B c2 = 0 (bit j of row i = omega(b_i(x), b_j(y)))."""
        cons = {}
        cell = list(itertools.product((0, 1), repeat=3))
        span = 2 * self.rinf
        offs = list(itertools.product(range(-span, span + 1), repeat=3))
        cache = {}
        for x in cell:
            r1, B1 = self.placed_basis(x)
            for d in offs:
                if d == (0, 0, 0):
                    continue
                y = tuple(a + b for a, b in zip(x, d))
                key = tuple(c % 2 for c in y)
                if key not in cache:
                    cache[key] = self.placed_basis(key)
                r2, B2base = cache[key]
                shift = tuple(a - b for a, b in zip(y, key))
                B2 = [translate(p, shift) for p in B2base]
                rows = []
                nz = False
                for b1 in B1:
                    row = 0
                    for j, b2 in enumerate(B2):
                        if pcomm(b1, b2):
                            row |= 1 << j
                            nz = True
                    rows.append(row)
                if nz:
                    cons.setdefault((r1, r2), set()).add(tuple(rows))
        return cons


def quad_ok(c, mats):
    """c^T B c = 0 for all B in mats (c, rows as bitmasks)."""
    for B in mats:
        t = 0
        for i, row in enumerate(B):
            if (c >> i) & 1:
                t ^= popc(row & c) & 1
        if t:
            return False
    return True


def functional(c1, B):
    """the linear functional c1^T B on the second argument, as a bitmask."""
    f = 0
    for i, row in enumerate(B):
        if (c1 >> i) & 1:
            f ^= row
    return f


def sign_ok_role(space, r, c):
    p = combo(space.basis[r], [(c >> i) & 1 for i in range(space.dim[r])])
    g = group("O") if r in ("V", "C") else group("D4", 2)
    return exact_invariant(p, g)


def solve(space, verbose=True, presign=False):
    cons = space.bilinear_constraints()
    d = space.dim
    valid = {}
    for r in ROLES:
        mats = list(cons.get((r, r), ()))
        valid[r] = [c for c in range(1, 1 << d[r]) if quad_ok(c, mats)]
        if presign:
            if r == "C" and d["C"] == d["V"]:
                valid[r] = [c for c in valid[r] if c in set(valid["V"]) or sign_ok_role(space, r, c)]
            valid[r] = [c for c in valid[r] if sign_ok_role(space, r, c)]
    if verbose:
        print("  basis dims:", d, " self-commuting nonzero shapes:", {r: len(valid[r]) for r in ROLES})
        print("  distinct bilinear constraint matrices per role pair:",
              {f"{a}{b}": len(v) for (a, b), v in sorted(cons.items())})

    def cross(r1, c1, r2):
        fs = set()
        for B in cons.get((r1, r2), ()):
            f = functional(c1, B)
            if f:
                fs.add(f)
        # constraints from the transposed pairs (r2, r1): c2^T B c1 = 0 -> functional on c2
        for B in cons.get((r2, r1), ()):
            # bit j of row i is omega(b_i^{r2}, b_j^{r1}); functional on c2: sum_i c2_i [popc(row_i & c1)]
            f = 0
            for i, row in enumerate(B):
                if popc(row & c1) & 1:
                    f |= 1 << i
            if f:
                fs.add(f)
        return fs

    def ok_lin(c, fs):
        return all(popc(c & f) % 2 == 0 for f in fs)

    sols = []
    for cV in valid["V"]:
        fC = cross("V", cV, "C")
        for cC in valid["C"]:
            if not ok_lin(cC, fC):
                continue
            fE = cross("V", cV, "E") | cross("C", cC, "E")
            for cE in valid["E"]:
                if not ok_lin(cE, fE):
                    continue
                fF = cross("V", cV, "F") | cross("C", cC, "F") | cross("E", cE, "F")
                for cF in valid["F"]:
                    if ok_lin(cF, fF):
                        sols.append({"V": cV, "C": cC, "E": cE, "F": cF})
    return sols


def shapes_of(space, sol):
    return {r: combo(space.basis[r], [(sol[r] >> i) & 1 for i in range(space.dim[r])]) for r in ROLES}


def exact_signs_ok(shapes):
    return (exact_invariant(shapes["V"], group("O")) and exact_invariant(shapes["C"], group("O"))
            and exact_invariant(shapes["E"], group("D4", 2)) and exact_invariant(shapes["F"], group("D4", 2)))


def generator_patterns(shapes, L, signs=None):
    """all N generators on the L-torus as (site, sign, pattern-with-absolute-coords)."""
    out = []
    for x in itertools.product(range(L), repeat=3):
        role, axis = role_of(x)
        s, p = shape_at(shapes[role], role, axis, x)
        if signs is not None:
            s *= signs[role]
        out.append((x, s, p))
    return out


def _fbasis(fs):
    """reduce a set of functionals (bitmasks) to an echelon basis (list)."""
    piv = {}
    for f in fs:
        while f:
            h = f.bit_length() - 1
            if h in piv:
                f ^= piv[h]
            else:
                piv[h] = f
                break
    return list(piv.values())


def solve_fast(space, verbose=True):
    """same solution set as solve(presign=True), organised for speed: per-role valid lists
    (self-commuting + exact sign), functionals reduced to bases, E->F functionals cached."""
    cons = space.bilinear_constraints()
    d = space.dim
    valid = {}
    for r in ROLES:
        mats = list(cons.get((r, r), ()))
        valid[r] = [c for c in range(1, 1 << d[r]) if quad_ok(c, mats) and sign_ok_role(space, r, c)]

    def cross(r1, c1, r2):
        fs = set()
        for B in cons.get((r1, r2), ()):
            f = functional(c1, B)
            if f:
                fs.add(f)
        for B in cons.get((r2, r1), ()):
            f = 0
            for i, row in enumerate(B):
                if popc(row & c1) & 1:
                    f |= 1 << i
            if f:
                fs.add(f)
        return fs

    def ok(c, fb):
        for f in fb:
            if popc(c & f) & 1:
                return False
        return True

    fEF = {cE: _fbasis(cross("E", cE, "F")) for cE in valid["E"]}
    sols = []
    for cV in valid["V"]:
        fC = _fbasis(cross("V", cV, "C"))
        fVE, fVF = cross("V", cV, "E"), cross("V", cV, "F")
        for cC in valid["C"]:
            if not ok(cC, fC):
                continue
            fE = _fbasis(fVE | cross("C", cC, "E"))
            fF = _fbasis(fVF | cross("C", cC, "F"))
            SE = [c for c in valid["E"] if ok(c, fE)]
            SF = [c for c in valid["F"] if ok(c, fF)]
            for cE in SE:
                fb = fEF[cE]
                for cF in SF:
                    if ok(cF, fb):
                        sols.append({"V": cV, "C": cC, "E": cE, "F": cF})
    if verbose:
        print("  valid (self-commuting + exact sign):", {r: len(valid[r]) for r in ROLES})
    return sols
