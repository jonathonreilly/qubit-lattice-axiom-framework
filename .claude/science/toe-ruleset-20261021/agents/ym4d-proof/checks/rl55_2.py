"""rl55_2 -- is supp D_c (links used by the S4' words of c) exactly the set of links with both endpoints in Box(c)?

Criteria: rl55_2_criteria.md (written first). Integer arithmetic only; same word construction as rl55_1.
"""
from itertools import permutations, product
import sys

D = 4


def add(z, w):
    return tuple(a + b for a, b in zip(z, w))


def unit(nu, t=1):
    return tuple(t if i == nu else 0 for i in range(D))


def axial_path(a, b, order):
    verts = [a]
    z = list(a)
    for nu in order:
        while z[nu] != b[nu]:
            z[nu] += 1 if b[nu] > z[nu] else -1
            verts.append(tuple(z))
    return verts


def word_vertices(L, mu, order, y):
    o = (L - 1) // 2
    cX = (o,) * D
    cY = add(cX, unit(mu, L))
    leg1 = axial_path(cX, y, order)
    leg2 = [add(y, unit(mu, t)) for t in range(L + 1)]
    leg3 = list(reversed(axial_path(cY, add(y, unit(mu, L)), order)))
    return leg1 + leg2[1:] + leg3[1:]


def links_of(verts):
    out = set()
    for a, b in zip(verts, verts[1:]):
        diff = tuple(bb - aa for aa, bb in zip(a, b))
        nu = [i for i in range(D) if diff[i] != 0][0]
        out.add((a if diff[nu] == 1 else b, nu))
    return out


def used_links(L, mu, offsets):
    o = (L - 1) // 2
    cX = (o,) * D
    u = set()
    for order in permutations(range(D)):
        for off in offsets:
            u |= links_of(word_vertices(L, mu, order, add(cX, off)))
    return u


def in_box(z, L, mu):
    return all(0 <= z[nu] <= (2 * L - 1 if nu == mu else L - 1) for nu in range(D))


def omega(L, mu):
    out = set()
    for z in product(*[range(2 * L if nu == mu else L) for nu in range(D)]):
        for nu in range(D):
            if in_box(add(z, unit(nu)), L, mu):
                out.add((z, nu))
    return out


def staircase_ok(bset, nu, b, bp):
    lo = [min(b[i], bp[i]) for i in range(D)]
    hi = [max(b[i], bp[i]) for i in range(D)]
    for z in product(*[range(lo[i], hi[i] + 1) for i in range(D)]):
        if (z, nu) not in bset:
            return False
    return True


def main():
    lines = []
    q1 = True
    q2 = True
    k1 = False
    for L in (3, 5):
        o = (L - 1) // 2
        centred = list(product(range(-o, o + 1), repeat=D))
        for mu in range(D):
            u = used_links(L, mu, centred)
            om = omega(L, mu)
            eq = (u == om)
            q1 = q1 and eq
            lines.append("L=%d mu=%d: |N_c| = %d, |Omega_c| = %d, equal: %s" % (L, mu, len(u), len(om), eq))
            for nu in range(D):
                bases = [b for (b, n) in u if n == nu]
                if L == 3:
                    for i in range(len(bases)):
                        for j in range(i + 1, len(bases)):
                            if not staircase_ok(u, nu, bases[i], bases[j]):
                                q2 = False
                else:
                    lo = tuple(min(b[i] for b in bases) for i in range(D))
                    hi = tuple(max(b[i] for b in bases) for i in range(D))
                    if not staircase_ok(u, nu, lo, hi):
                        q2 = False
            # control: y = c_X only
            u0 = used_links(L, mu, [(0,) * D])
            if u0 != om:
                k1 = True
            lines.append("   control (y = c_X only): |N_c| = %d (strict subset: %s)" % (len(u0), u0 < om))
    for ln in lines:
        print(ln)
    print("Q1 (N_c == Omega_c): %s" % ("PASS" if q1 else "FAIL"))
    print("Q2 (staircases inside N_c): %s" % ("PASS" if q2 else "FAIL"))
    print("K1 (control fires): %s" % ("FIRES" if k1 else "DOES NOT FIRE"))
    overall = q1 and q2 and k1
    print("OVERALL rl55_2: %s" % ("PASS" if overall else "FAIL"))
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
