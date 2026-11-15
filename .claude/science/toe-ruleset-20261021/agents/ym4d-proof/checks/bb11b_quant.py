#!/usr/bin/env python3
# checks/bb11b_quant.py -- BFT_B session 11, check bb11b.
# Criteria: checks/bb11b_criteria.md, written after reading checks/bb11.out (bb11 A5 FAIL) and before this script.
# checks/bb11_criteria.md, checks/bb11_bgd.py, checks/bb11.out, checks/bb11.time are NOT altered.
# The model, the backgrounds and every operator are imported unchanged from checks/bb11_bgd.py by exec of its
# definitions only (the file is read, its test section is cut at the TESTS banner, and nothing in it is modified).
from fractions import Fraction as F
import sys, io, os

src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bb11_bgd.py")).read()
head = src.split("# ================================================================ TESTS")[0]
g = {}
exec(compile(head, "bb11_bgd.py[definitions]", "exec"), g)
for nm in ("F", "Lev", "Box", "rng", "rand_fun", "rand_form1", "dZ_fun", "bg_curved", "bg_abelian",
           "gauge_sites", "bg_flat", "vsub", "vadd", "vzero", "mv", "I3"):
    globals()[nm] = g[nm]

res = {}
def record(tag, ok, note=""):
    res[tag] = (bool(ok), note)
    print("%-6s %s  %s" % (tag, "PASS" if ok else "FAIL", note))

print("bb11b -- the quantifier on the covariant gauge shift (d=2, L=3, K=2, SU(2) adjoint, exact Q)")
print()

lev6 = Lev(6)
nxt = rng(20261028)
Gs = gauge_sites(lev6, nxt)       # consume the same stream as bb11 so the data match
A_flat = bg_flat(lev6, Gs)
A_curv = bg_curved(lev6, nxt)
A_ab = bg_abelian(lev6)
box = Box(lev6, (2, 2), 2)
c0 = box.c

def shift_by(x0, A, mu_f):
    dmu = dZ_fun(lev6, A, mu_f)
    return {b: vadd(x0[b], dmu[b]) for b in lev6.links}

# A5p: mu pinned at c_X
ok5p = True
for _ in range(4):
    x0 = rand_form1(lev6, nxt)
    mu_f = rand_fun(lev6, nxt)
    mu_f = {z: vsub(mu_f[z], mu_f[c0]) for z in lev6.sites}       # pin mu(c_X) = 0
    la = box.coulomb(A_curv, x0)
    lb = box.coulomb(A_curv, shift_by(x0, A_curv, mu_f))
    if la is None or lb is None:
        ok5p = False; break
    for z in box.sites:
        if not vzero(vsub(lb[z], vsub(la[z], mu_f[z]))):
            ok5p = False
record("A5p", ok5p, "mu(c_X) = 0: lam^{E,Z}(x + d_Z mu) = lam^{E,Z}(x) - mu exactly (curved background)")

# A5g / A5n: general mu, corrected identity with the constant kappa
ok5g, nz_dk, nz_lam = True, False, False
for _ in range(4):
    x0 = rand_form1(lev6, nxt)
    mu_f = rand_fun(lev6, nxt)
    kap = {z: mu_f[c0] for z in lev6.sites}                        # the CONSTANT function mu(c_X)
    dk = dZ_fun(lev6, A_curv, kap)
    if any(not vzero(dk[b]) for b in lev6.links):
        nz_dk = True
    la_k = box.coulomb(A_curv, shift_by(x0, A_curv, kap))
    la_0 = box.coulomb(A_curv, x0)
    lb = box.coulomb(A_curv, shift_by(x0, A_curv, mu_f))
    if la_k is None or la_0 is None or lb is None:
        ok5g = False; break
    if any(not vzero(vsub(la_k[z], la_0[z])) for z in box.sites):
        nz_lam = True
    for z in box.sites:
        pred = vadd(vsub(la_k[z], mu_f[z]), mu_f[c0])
        if not vzero(vsub(lb[z], pred)):
            ok5g = False
record("A5g", ok5g, "general mu: lam^{E,Z}(x + d_Z mu) = lam^{E,Z}(x + d_Z kappa) - mu + mu(c_X) exactly, kappa = mu(c_X)")
record("A5n", nz_dk and nz_lam, "non-vacuity: d_Z kappa != 0 (%s) and lam^{E,Z}(x + d_Z kappa) != lam^{E,Z}(x) (%s)"
       % (nz_dk, nz_lam))

# A5a: bb11's original A5 identity on the abelian background
ok5a = True
for _ in range(4):
    x0 = rand_form1(lev6, nxt)
    mu_f = rand_fun(lev6, nxt)
    la = box.coulomb(A_ab, x0)
    lb = box.coulomb(A_ab, shift_by(x0, A_ab, mu_f))
    if la is None or lb is None:
        ok5a = False; break
    for z in box.sites:
        pred = vadd(vsub(la[z], mu_f[z]), mu_f[c0])
        if not vzero(vsub(lb[z], pred)):
            ok5a = False
record("A5a", ok5a, "abelian background: bb11's original A5 identity holds exactly (so the curvature is the cause)")

# A6q: constants are not covariantly closed
cc = {z: (F(1), F(2), F(-1)) for z in lev6.sites}
dc_curv = dZ_fun(lev6, A_curv, cc)
dc_ab = dZ_fun(lev6, A_ab, cc)
ok6q = any(not vzero(dc_curv[b]) for b in lev6.links) and all(vzero(dc_ab[b]) for b in lev6.links)
record("A6q", ok6q, "d_Z(const) != 0 at a curved background, = 0 at the abelian one: Lambda_0 cannot be read modulo constants")

print()
allok = all(v[0] for v in res.values())
print("VERDICT bb11b: %s" % ("ALL PASS" if allok else "NOT ALL PASS -- FAILED: "
                             + ", ".join(t for t, v in res.items() if not v[0])))
