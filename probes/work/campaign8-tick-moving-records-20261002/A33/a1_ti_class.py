"""A33 a1: translation-invariant (TI) covariant stabilizer vacua, one qubit per site.

Finite class (exhaustive): one generator per site, all generators translates of one Pauli u,
 (i)  site-centred u supported in the ball |d|^2 <= 6 (81 sites), invariant under the 24 soldered
      turns about the site (mod 2: 2^7 - 1 = 127 nonzero shapes), or invariant under T only (control);
 (ii) cube-centred u supported in |y - c|^2 <= 6.75 around c = (1/2,1/2,1/2) (88 sites), O-invariant
      about c (2^6 - 1 = 63 shapes).
Filters: exact sign invariance (every turn maps the canonical string to itself with sign +1);
isotropy (all translates commute); purity on Z^3 = primitivity gcd(a, b) = 1 over F2[z^+-1]
(a, b = X- and Z-parts as Laurent polynomials; gcd computed after clearing monomials).
For survivors: on L-tori, k(L) = N - rank, whether a single defect is creatable, the number of
displacements v != 0 by which a lone defect can be moved by ANY Pauli (c5's test), and the
"quiet" test: dimension of the stabilizer elements supported inside one 7-site star.
"""
import signal, sys, itertools, time
signal.alarm(55)
import sympy as sp
from p2lib import (group, invariant_basis, ball_sites, combo, exact_invariant, pcomm, translate,
                   Torus, Elim, syndrome_table, LBITS, pat_str)

t0 = time.time()
zs = sp.symbols("z1 z2 z3")


def laurent_parts(pat):
    xs, zz = [], []
    for y, l in pat.items():
        bx, bz = LBITS[l]
        if bx:
            xs.append(y)
        if bz:
            zz.append(y)
    return xs, zz


def to_poly(mons):
    if not mons:
        return sp.Poly(0, *zs, modulus=2)
    mins = [min(m[i] for m in mons) for i in range(3)]
    e = sum(sp.Mul(*[zs[i] ** (m[i] - mins[i]) for i in range(3)]) for m in mons)
    return sp.Poly(e, *zs, modulus=2)


def primitive(pat):
    xs, zz = laurent_parts(pat)
    if not xs or not zz:
        return False   # one part zero -> gcd = the other part (a non-unit unless monomial)
    g = sp.gcd(to_poly(xs), to_poly(zz))
    return g.total_degree() == 0


def isotropic(pat):
    sites = list(pat)
    diffs = {tuple(a - b for a, b in zip(y1, y2)) for y1 in sites for y2 in sites}
    return all(pcomm(pat, translate(pat, t)) == 0 for t in diffs if t != (0, 0, 0))


def survivors(B, grp, c2):
    basis, orbits = invariant_basis(B, grp, c2)
    out = []
    for bits in itertools.product([0, 1], repeat=len(basis)):
        if not any(bits):
            continue
        p = combo(basis, bits)
        if not exact_invariant(p, grp, c2):
            continue
        if not isotropic(p):
            continue
        if not primitive(p):
            continue
        out.append(p)
    return basis, out


def label_sum(p):
    sx = sum(LBITS[l][0] for l in p.values()) % 2
    sz = sum(LBITS[l][1] for l in p.values()) % 2
    return sx, sz


def torus_tests(p, L):
    T = Torus(L)
    gens = []
    for x in T.sites:
        gens.append(T.bits(T.wrapped(translate(p, x))))
    rk = Elim()
    for g in gens:
        rk.add(g[0] | (g[1] << T.N))
    sx, sz = syndrome_table(T, gens)
    sp_ = Elim()
    for v in sx + sz:
        sp_.add(v)
    single = sp_.reduce(1 << 0)[0] == 0
    mob = sum(1 for i in range(1, T.N) if sp_.reduce(1 | (1 << i))[0] == 0)
    return T.N - len(rk), single, mob


def quiet_dim(p):
    """dim of Paulis supported in the star of the origin that commute with every generator
    (= stabilizer elements inside one star, since the state is pure)."""
    star = [(0, 0, 0)] + [tuple(s * (i == a) for i in range(3)) for a in range(3) for s in (1, -1)]
    gens = []
    sites = set()
    for y in star:
        sites.add(y)
    # generators touching the star: translates t with (t + supp) meeting the star
    cand = {tuple(a - b for a, b in zip(y, d)) for y in star for d in p}
    rows = []
    for t in cand:
        g = translate(p, t)
        row = 0
        for k, y in enumerate(star):
            l = g.get(y, 0)
            bx, bz = LBITS[l]
            # unknown Pauli on the star: bits (x_k, z_k); commutation = sum x_k bz + z_k bx
            if bz:
                row |= 1 << (2 * k)
            if bx:
                row |= 1 << (2 * k + 1)
        rows.append(row)
    E = Elim()
    for r in rows:
        E.add(r)
    return 14 - len(E)


cases = [("site-centred, O, |d|^2<=6", ball_sites(6), group("O"), (0, 0, 0)),
         ("cube-centred, O, |y-c|^2<=6.75", ball_sites(6.75, (1, 1, 1)), group("O"), (1, 1, 1)),
         ("site-centred, T only, |d|^2<=3", ball_sites(3), group("T"), (0, 0, 0))]
for name, B, G, c2 in cases:
    basis, surv = survivors(B, G, c2)
    print(f"[{name}] invariant shapes dim {len(basis)} -> {2**len(basis)-1} nonzero; "
          f"pure covariant TI states (exact sign, isotropic, primitive): {len(surv)}   ({time.time()-t0:.1f}s)")
    for p in surv:
        ls = label_sum(p)
        diam = max(max(y[i] for y in p) - min(y[i] for y in p) for i in range(3)) + 1
        res = []
        for L in (4, 6, 8):
            if L < diam:
                continue
            k, single, mob = torus_tests(p, L)
            res.append(f"L={L}: k={k}, single creatable={'yes' if single else 'no'}, mobile v={mob}")
        print(f"   |supp|={len(p)} label-sum(z=1)={ls} quiet-dim(star)={quiet_dim(p)} :: " + "; ".join(res))
        if len(p) <= 12:
            print("      u =", pat_str(p))
    sys.stdout.flush()
print(f"total {time.time()-t0:.1f}s")
