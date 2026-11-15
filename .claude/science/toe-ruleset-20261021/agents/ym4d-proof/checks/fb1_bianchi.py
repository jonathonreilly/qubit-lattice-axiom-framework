#!/usr/bin/env python3
# fb1 — FACEB.md (T55-G).  Criteria: checks/fb1_criteria.md, written 2026-10-28T21:20:47Z.
# Exact integer / exact decimal arithmetic in plain python.  No numpy, no BLAS, no lock.
#
# A1  d.d = 0 on 0-forms
# A2  <d phi, delta W> = 0                      (source leg: divergence-form slots are invisible)
# A3  <d mu, u> = 0 for u = delta(1_p)          (response leg: the witness has no exact part)
# A4  non-vacuity of A3: u != 0, delta u = 0, d u != 0
# A5  discriminating power: <d phi, j> != 0 for a generic 1-form j
# A6  DESIGNED-FAIL CONTROL: corrupt one incidence sign; A1/A2/A3 must fail
# A7  price arithmetic at 50 and 100 digits

import random
from decimal import Decimal, getcontext

D = 4
N = 4
SITES = N ** D


def site_index(c):
    i = 0
    for a in c:
        i = i * N + (a % N)
    return i


def site_coords(i):
    c = []
    for _ in range(D):
        c.append(i % N)
        i //= N
    return tuple(reversed(c))


SHIFT = []                                  # SHIFT[mu][z] = index of z + e_mu
for mu in range(D):
    row = []
    for z in range(SITES):
        c = list(site_coords(z))
        c[mu] = (c[mu] + 1) % N
        row.append(site_index(c))
    SHIFT.append(row)

LINKS = [(z, mu) for mu in range(D) for z in range(SITES)]
LINK_ID = {lk: i for i, lk in enumerate(LINKS)}
NL = len(LINKS)

PLAQS = [(z, mu, nu) for mu in range(D) for nu in range(mu + 1, D) for z in range(SITES)]
NP = len(PLAQS)

# ---- incidence of d on 0-forms: (d phi)(z,mu) = phi(z+e_mu) - phi(z)
D0 = []                                     # D0[link] = [(site, coeff), ...]
for (z, mu) in LINKS:
    D0.append([(SHIFT[mu][z], 1), (z, -1)])

# ---- incidence of d on 1-forms:
# (dA)(z,mu,nu) = A(z,mu) + A(z+e_mu,nu) - A(z+e_nu,mu) - A(z,nu)
def build_D1():
    out = []
    for (z, mu, nu) in PLAQS:
        out.append([(LINK_ID[(z, mu)], 1),
                    (LINK_ID[(SHIFT[mu][z], nu)], 1),
                    (LINK_ID[(SHIFT[nu][z], mu)], -1),
                    (LINK_ID[(z, nu)], -1)])
    return out


def apply_inc(inc, vec_in, n_out):
    out = [0] * n_out
    for i, row in enumerate(inc):
        s = 0
        for (j, c) in row:
            s += c * vec_in[j]
        out[i] = s
    return out


def apply_inc_T(inc, vec_in, n_out):
    """transpose of `inc` applied to vec_in; built by transposing the SAME lists."""
    out = [0] * n_out
    for i, row in enumerate(inc):
        v = vec_in[i]
        if v:
            for (j, c) in row:
                out[j] += c * v
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def run_core(D1, tag, rng):
    """returns dict of results for A1, A2, A3, A4, A5 with this (possibly corrupted) D1."""
    res = {}

    # ---- A1 : d d phi = 0
    bad1 = 0
    tests0 = []
    for _ in range(5):
        tests0.append([rng.randint(-9, 9) for _ in range(SITES)])
    for z in (0, 37, 211):
        v = [0] * SITES
        v[z] = 1
        tests0.append(v)
    for phi in tests0:
        a = apply_inc(D0, phi, NL)
        w = apply_inc(D1, a, NP)
        bad1 += sum(1 for x in w if x != 0)
    res['A1_nonzero'] = bad1

    # ---- A2 : <d phi, delta W> = 0 ; delta = transpose of D1
    bad2 = 0
    Ws = [[rng.randint(-9, 9) for _ in range(NP)] for _ in range(5)]
    phis = tests0[:5]
    for phi in phis:
        a = apply_inc(D0, phi, NL)
        for W in Ws:
            dW = apply_inc_T(D1, W, NL)
            if dot(a, dW) != 0:
                bad2 += 1
    res['A2_nonzero'] = bad2

    # ---- A3 : the witness u = delta(1_p), p = (site 0; mu=0, nu=1)
    p_index = PLAQS.index((0, 0, 1))
    onep = [0] * NP
    onep[p_index] = 1
    u = apply_inc_T(D1, onep, NL)
    bad3 = 0
    mus = tests0[:5]
    for z in (0, 1, 5, 64, 200):
        v = [0] * SITES
        v[z] = 1
        mus = mus + [v]
    for mu_f in mus:
        a = apply_inc(D0, mu_f, NL)
        if dot(a, u) != 0:
            bad3 += 1
    res['A3_nonzero'] = bad3
    res['A3_tests'] = len(mus)

    # ---- A4 : non-vacuity
    du = apply_inc(D1, u, NP)
    delta_u = apply_inc_T(D0, u, SITES)      # codifferential 1-form -> 0-form
    res['A4_u_nonzero'] = any(x != 0 for x in u)
    res['A4_u_coclosed'] = all(x == 0 for x in delta_u)
    res['A4_du_nonzero'] = any(x != 0 for x in du)
    res['A4_u_support'] = sum(1 for x in u if x != 0)
    res['A4_u_values'] = sorted(set(x for x in u if x != 0))

    # ---- A5 : discriminating power, generic 1-form j
    nz = 0
    for _ in range(5):
        j = [rng.randint(-9, 9) for _ in range(NL)]
        phi = [rng.randint(-9, 9) for _ in range(SITES)]
        a = apply_inc(D0, phi, NL)
        if dot(a, j) != 0:
            nz += 1
    res['A5_nonzero_count'] = nz
    return res


print("fb1 — FACEB.md / T55-G.  criteria: checks/fb1_criteria.md (21:20:47Z)")
print("lattice: periodic Z_%d^%d  |  sites %d  links %d  plaquettes %d" % (N, D, SITES, NL, NP))
print()

rng = random.Random(20261028)
D1 = build_D1()
clean = run_core(D1, "clean", rng)

print("=== CLEAN COMPLEX ===")
print("A1  d(d phi) nonzero components over 8 phi :", clean['A1_nonzero'],
      "->", "PASS" if clean['A1_nonzero'] == 0 else "FAIL")
print("A2  <d phi, delta W> nonzero over 25 pairs :", clean['A2_nonzero'],
      "->", "PASS" if clean['A2_nonzero'] == 0 else "FAIL")
print("A3  <d mu, u> nonzero over %d mu          :" % clean['A3_tests'], clean['A3_nonzero'],
      "->", "PASS" if clean['A3_nonzero'] == 0 else "FAIL")
print("A4  u != 0                                 :", clean['A4_u_nonzero'])
print("A4  delta u == 0  (u is co-closed)         :", clean['A4_u_coclosed'])
print("A4  d u != 0      (u carries curvature)    :", clean['A4_du_nonzero'])
print("A4  |supp u| =", clean['A4_u_support'], " distinct values:", clean['A4_u_values'])
a4 = clean['A4_u_nonzero'] and clean['A4_u_coclosed'] and clean['A4_du_nonzero']
print("A4  ->", "PASS" if a4 else "FAIL")
print("A5  <d phi, j> nonzero for generic j       :", clean['A5_nonzero_count'], "/5 ->",
      "PASS" if clean['A5_nonzero_count'] >= 4 else "FAIL")
print()

# ---- A6 DESIGNED-FAIL CONTROL : flip one incidence sign
print("=== A6  DESIGNED-FAIL CONTROL (one incidence sign flipped) ===")
rng2 = random.Random(20261028)
D1c = [list(r) for r in build_D1()]
tgt = 0
(j0, c0) = D1c[tgt][0]
D1c[tgt][0] = (j0, -c0)
print("corrupted plaquette row %d: entry (link %d) %+d -> %+d" % (tgt, j0, c0, -c0))
corr = run_core(D1c, "corrupt", rng2)
print("A1 under corruption: nonzero =", corr['A1_nonzero'],
      "->", "CONTROL FIRED (A1 fails)" if corr['A1_nonzero'] > 0 else "CONTROL DID NOT FIRE")
print("A2 under corruption: nonzero =", corr['A2_nonzero'],
      "->", "CONTROL FIRED (A2 fails)" if corr['A2_nonzero'] > 0 else "CONTROL DID NOT FIRE")
print("A3 under corruption: nonzero =", corr['A3_nonzero'],
      "->", "CONTROL FIRED (A3 fails)" if corr['A3_nonzero'] > 0 else "CONTROL DID NOT FIRE")
fired = (corr['A1_nonzero'] > 0) and (corr['A2_nonzero'] > 0) and (corr['A3_nonzero'] > 0)
print("A6  ->", "PASS (control failed the clauses, as designed)" if fired else "FAIL (gate has no power)")
print()

# ---- A7 price arithmetic at two precisions
print("=== A7  PRICE ARITHMETIC (exact decimal, 50 and 100 digits) ===")


def price_rows(prec):
    getcontext().prec = prec
    L3 = Decimal(3).ln() / Decimal(10).ln()
    rows = {}
    for k in (10, 42, 160, 183, 356):
        rows['P(%d)' % k] = (Decimal(2 * k - 3) * L3)
    DXp = Decimal('2.456E-152')
    eps1 = Decimal('6.7E-40')
    needDX = -(DXp.log10())
    needE1 = -(eps1.log10())
    rows['need_DXprime_decades'] = needDX
    rows['need_eps1_decades'] = needE1
    rows['k_star_DXprime'] = (needDX / L3 + Decimal(3)) / Decimal(2)
    rows['k_star_eps1'] = (needE1 / L3 + Decimal(3)) / Decimal(2)
    rows['P(183.4)'] = (Decimal('2') * Decimal('183.4') - Decimal(3)) * L3
    rows['P(355.6)'] = (Decimal('2') * Decimal('355.6') - Decimal(3)) * L3
    rows['excess_at_183.4_vs_DXprime'] = rows['P(183.4)'] - needDX
    rows['excess_at_42_vs_eps1'] = rows['P(42)'] - needE1
    return rows


r50 = price_rows(50)
r100 = price_rows(100)
worst = Decimal(0)
for key in sorted(r50):
    getcontext().prec = 60
    diff = abs(Decimal(r50[key]) - Decimal(r100[key]))
    if diff > worst:
        worst = diff
    print("  %-30s %s" % (key, (+Decimal(r100[key])).quantize(Decimal('1.000000'))))
print("  worst 50-vs-100-digit disagreement:", worst)
print("A7  ->", "PASS" if worst < Decimal('1e-30') else "FAIL")
print()
print("=== SUMMARY ===")
verdicts = {
    'A1': clean['A1_nonzero'] == 0,
    'A2': clean['A2_nonzero'] == 0,
    'A3': clean['A3_nonzero'] == 0,
    'A4': a4,
    'A5': clean['A5_nonzero_count'] >= 4,
    'A6': fired,
    'A7': worst < Decimal('1e-30'),
}
for k in sorted(verdicts):
    print("  %s : %s" % (k, "PASS" if verdicts[k] else "FAIL"))
print("ALL PASS" if all(verdicts.values()) else "NOT ALL PASS")
