#!/usr/bin/env python3
"""tu1_twisted.py -- check tu1 for TUNIF.md (T-uniformity worker, session 25).

Tests the twisted-cell-complex division construction CONSTR of checks/tu1_criteria.md,
in EXACT rational arithmetic (fractions only, no BLAS, no lock needed).

Model: C = (Z/l)^d with twisted differences
   (D_mu psi)(u) = f_mu(u) * psi(u + e_mu) - psi(u),  f_mu(u) = z_mu if u_mu = l-1 else 1.
The 2-form under test is F := D^a for a fixed random rational 1-form a (the application's
class: the fine curvature response is exact).  F is an explicit function of z, so it can be
evaluated at z_1 = 1 and z_2 = 1 as the construction requires.

Criteria are pre-registered in checks/tu1_criteria.md (written before this file).
"""

from fractions import Fraction as Fr
from itertools import product
import random
import sys


# ---------------------------------------------------------------- lattice utils
def sites(l, d):
    return list(product(range(l), repeat=d))


def shift(u, mu, l):
    """u + e_mu (mod l) and whether the mu-seam was crossed."""
    v = list(u)
    crossed = (u[mu] == l - 1)
    v[mu] = (u[mu] + 1) % l
    return tuple(v), crossed


def Dmu(psi, mu, l, z):
    """Twisted difference of a scalar field psi: dict site -> Fr."""
    out = {}
    for u in psi:
        v, crossed = shift(u, mu, l)
        fac = z[mu] if crossed else Fr(1)
        out[u] = fac * psi[v] - psi[u]
    return out


def wedge(a, l, d, z):
    """(D^a)_{mu nu} = D_mu a_nu - D_nu a_mu for a 1-form a: dict (site,mu) -> Fr."""
    comp = {mu: {u: a[(u, mu)] for u in sites(l, d)} for mu in range(d)}
    F = {}
    for mu in range(d):
        for nu in range(mu + 1, d):
            dmu_anu = Dmu(comp[nu], mu, l, z)
            dnu_amu = Dmu(comp[mu], nu, l, z)
            for u in sites(l, d):
                F[(u, mu, nu)] = dmu_anu[u] - dnu_amu[u]
    return F


def Fget(F, u, mu, nu):
    if mu == nu:
        return Fr(0)
    if mu < nu:
        return F[(u, mu, nu)]
    return -F[(u, nu, mu)]


# ------------------------------------------------- line sum and telescoping sum
def sigma(g, mu, l, d):
    """sigma_mu(g)(u_perp) = sum over u_mu.  Returned as dict on full sites
    (constant in the mu slot) so that later D_nu's are easy."""
    out = {}
    for u in sites(l, d):
        tot = Fr(0)
        for i in range(l):
            w = list(u)
            w[mu] = i
            tot += g[tuple(w)]
        out[u] = tot
    return out


def Theta(g, mu, l, d):
    """Theta_mu(g)(u) = sum_{0<=i<u_mu} g(..., i, ...)   (zero at u_mu = 0)."""
    out = {}
    for u in sites(l, d):
        tot = Fr(0)
        for i in range(u[mu]):
            w = list(u)
            w[mu] = i
            tot += g[tuple(w)]
        out[u] = tot
    return out


# ------------------------------------------------------------------- CONSTR
def constr(Fz, Fz1, l, d, z, use_b1=True):
    """Fz  : the 2-form at the actual z (dict (u,mu,nu) -> Fr), mu<nu.
       Fz1 : the same 2-form evaluated at z_1 = 1 (other z's unchanged).
       Returns (b, diag) with b: dict (site,mu) -> Fr."""
    nu1 = z[0] - 1
    nu2 = z[1] - 1
    diag = {}

    # 1. Omega_beta = sigma_1(F_{1 beta}) at z_1 = 1,  beta >= 2 (index 1..d-1)
    Omega = {}
    for beta in range(1, d):
        g = {u: Fget(Fz1, u, 0, beta) for u in sites(l, d)}
        Omega[beta] = sigma(g, 0, l, d)

    # 2. Phi = sigma_2(Omega_2) at z_2 = 1.  sigma_2 at z_2 = 1 is just the plain
    #    sum over u_2 (the seam factor never enters a sum), so sigma() is correct
    #    here as written: Omega itself does not depend on z_2 through a seam factor
    #    except inside Fz1, which is evaluated at the actual z_2.  To get Phi we
    #    therefore need Omega_2 recomputed at z_2 = 1 as well; the caller supplies
    #    Fz1z2 via the Phi computation below (see phi_of).
    #    (Phi is reported separately by phi_of(); CONSTR itself only needs mu.)

    # 3. mu := Theta_2(Omega_2) + sigma_2(Omega_2)/nu_2
    s2 = sigma(Omega[1], 1, l, d)
    th2 = Theta(Omega[1], 1, l, d)
    mu_f = {u: th2[u] + s2[u] / nu2 for u in sites(l, d)}

    # D_beta mu should equal Omega_beta for every beta >= 2 (diagnostic)
    worst = Fr(0)
    for beta in range(1, d):
        Dm = Dmu(mu_f, beta, l, z)
        for u in sites(l, d):
            diff = abs(Dm[u] - Omega[beta][u])
            if diff > worst:
                worst = diff
    diag["max|D_beta mu - Omega_beta|"] = worst

    # 4. b_1 := -mu/l , independent of u_1
    if use_b1:
        b1 = {}
        for u in sites(l, d):
            w = list(u)
            w[0] = 0                      # mu_f does not depend on u_1 anyway
            b1[u] = -mu_f[tuple(w)] / l
    else:
        b1 = {u: Fr(0) for u in sites(l, d)}

    # 5. G_beta := F_{1 beta} + D_beta b_1 ;  b_beta := Theta_1(G) + sigma_1(G)/nu_1
    b = {(u, 0): b1[u] for u in sites(l, d)}
    for beta in range(1, d):
        Db1 = Dmu(b1, beta, l, z)
        G = {u: Fget(Fz, u, 0, beta) + Db1[u] for u in sites(l, d)}
        s1 = sigma(G, 0, l, d)
        th1 = Theta(G, 0, l, d)
        for u in sites(l, d):
            b[(u, beta)] = th1[u] + s1[u] / nu1
    return b, diag


def phi_of(Fz1z2, l, d):
    """Phi(u_3..u_d) = sum_{u_1,u_2} F_{12}, with F evaluated at z_1 = z_2 = 1."""
    g = {u: Fget(Fz1z2, u, 0, 1) for u in sites(l, d)}
    s1 = sigma(g, 0, l, d)
    s12 = sigma(s1, 1, l, d)
    return s12


def residual(b, Fz, l, d, z):
    """count of (u, mu<nu) where D_mu b_nu - D_nu b_mu != F_{mu nu}, and the worst gap."""
    comp = {mu: {u: b[(u, mu)] for u in sites(l, d)} for mu in range(d)}
    bad, worst = 0, Fr(0)
    for mu in range(d):
        for nu in range(mu + 1, d):
            A = Dmu(comp[nu], mu, l, z)
            B = Dmu(comp[mu], nu, l, z)
            for u in sites(l, d):
                gap = abs(A[u] - B[u] - Fz[(u, mu, nu)])
                if gap != 0:
                    bad += 1
                    if gap > worst:
                        worst = gap
    return bad, worst


def maxabs(x):
    return max((abs(v) for v in x.values()), default=Fr(0))


# ------------------------------------------------------------------- instances
def rand_oneform(l, d, rng):
    return {(u, mu): Fr(rng.randint(-9, 9), rng.randint(1, 7))
            for u in sites(l, d) for mu in range(d)}


def run_instance(name, l, d, z, rng, perturb=False, use_b1=True, quiet=False):
    a = rand_oneform(l, d, rng)
    z1 = list(z); z1[0] = Fr(1)
    z12 = list(z); z12[0] = Fr(1); z12[1] = Fr(1)
    Fz = wedge(a, l, d, z)
    Fz1 = wedge(a, l, d, tuple(z1))
    Fz12 = wedge(a, l, d, tuple(z12))
    if perturb:
        # designed-FAIL control #1: break closedness with one entry (d >= 3 only)
        u0 = tuple([0] * d)
        delta = Fr(1)
        for FF in (Fz, Fz1, Fz12):
            FF[(u0, 0, 1)] = FF[(u0, 0, 1)] + delta
    b, diag = constr(Fz, Fz1, l, d, z, use_b1=use_b1)
    bad, worst = residual(b, Fz, l, d, z)
    phi = phi_of(Fz12, l, d)
    mb, mF = maxabs(b), maxabs(Fz)
    if not quiet:
        print(f"  [{name}] l={l} d={d} z={[str(t) for t in z]}")
        print(f"      residual nonzero entries = {bad}   worst = {float(worst):.3e}")
        print(f"      max|Phi| = {float(maxabs(phi)):.3e}   "
              f"max|D_beta mu - Omega_beta| = {float(diag['max|D_beta mu - Omega_beta|']):.3e}")
        print(f"      max|b| = {float(mb):.6g}   max|F| = {float(mF):.6g}   "
              f"ratio/(l*max|F|) = {float(mb / (l * mF)):.4g}")
    return dict(bad=bad, phi=maxabs(phi), maxb=mb, maxF=mF, l=l,
                ratio=mb / (l * mF) if mF != 0 else None)


def main():
    rng = random.Random(20261028)
    gen4 = (Fr(2, 3), Fr(5, 4), Fr(3, 7), Fr(7, 5))
    gen3 = (Fr(2, 3), Fr(5, 4), Fr(3, 7))
    eps = Fr(1, 10 ** 6)

    print("=" * 78)
    print("tu1-A / tu1-B / tu1-E : the construction on exact closed inputs")
    print("=" * 78)
    res = []
    cases = [
        ("A1 d=4 l=3 generic", 3, 4, gen4),
        ("A2 d=4 l=3 z1~1", 3, 4, (Fr(1) + eps, Fr(5, 4), Fr(3, 7), Fr(7, 5))),
        ("A3 d=4 l=3 z2~1", 3, 4, (Fr(2, 3), Fr(1) + eps, Fr(3, 7), Fr(7, 5))),
        ("A4 d=4 l=3 z1,z2~1", 3, 4, (Fr(1) + eps, Fr(1) + eps, Fr(3, 7), Fr(7, 5))),
        ("A5 d=4 l=9 generic", 9, 4, gen4),
        ("A6 d=4 l=9 z1~1", 9, 4, (Fr(1) + Fr(1, 10 ** 4), Fr(5, 4), Fr(3, 7), Fr(7, 5))),
        ("A7 d=3 l=5 generic", 5, 3, gen3),
        ("A8 d=3 l=5 z1,z2~1", 5, 3, (Fr(1) + eps, Fr(1) + eps, Fr(3, 7))),
    ]
    for nm, l, d, z in cases:
        res.append((nm, run_instance(nm, l, d, z, rng)))

    tu1A = all(r["bad"] == 0 for _, r in res)
    tu1B = all(r["phi"] == 0 for _, r in res)
    generic_names = {"A1 d=4 l=3 generic", "A5 d=4 l=9 generic", "A7 d=3 l=5 generic"}
    tu1E = all(r["ratio"] is not None and r["ratio"] <= 100
               for nm, r in res if nm in generic_names)
    print()
    print(f"tu1-A  (D^b = F exactly, every instance)      : {'PASS' if tu1A else 'FAIL'}")
    print(f"tu1-B  (Phi = 0 exactly, every instance)      : {'PASS' if tu1B else 'FAIL'}")
    print(f"tu1-E  (max|b| <= 100*l*max|F|, generic z)    : {'PASS' if tu1E else 'FAIL'}")

    print()
    print("=" * 78)
    print("tu1-C : DESIGNED-FAIL control #1 -- a non-closed input")
    print("=" * 78)
    ctrl = []
    for nm, l, d, z in [("C1 d=4 l=3 generic", 3, 4, gen4), ("C2 d=3 l=5 generic", 5, 3, gen3)]:
        ctrl.append(run_instance(nm, l, d, z, rng, perturb=True))
    ctrl_failed = all(c["bad"] > 0 for c in ctrl)
    ctrl_phi = any(c["phi"] != 0 for c in ctrl)
    print()
    print(f"tu1-C  control breaks the identity (expected) : "
          f"{'CONTROL FAILED AS DESIGNED' if ctrl_failed else 'CONTROL PASSED -- GATE HAS NO POWER'}")
    print(f"tu1-C  control gives Phi != 0 somewhere       : {ctrl_phi}")

    print()
    print("=" * 78)
    print("tu1-D : DESIGNED-FAIL control #2 -- omit b_1 and watch the 1/eps pole")
    print("=" * 78)
    corr, unco = [], []
    for j in (1, 2, 3, 4):
        e = Fr(1, 10 ** j)
        zz = (Fr(1) + e, Fr(5, 4), Fr(3, 7), Fr(7, 5))
        r_on = run_instance(f"D{j} corrected  eps=1e-{j}", 3, 4, zz, random.Random(777), quiet=True)
        r_off = run_instance(f"D{j} uncorrected eps=1e-{j}", 3, 4, zz, random.Random(777),
                             use_b1=False, quiet=True)
        corr.append(float(r_on["maxb"]))
        unco.append(float(r_off["maxb"]))
        print(f"  eps=1e-{j}:  max|b| corrected = {corr[-1]:12.6g}   "
              f"uncorrected = {unco[-1]:12.6g}   residual(corrected) = {r_on['bad']}")
    grow = unco[-1] / unco[0] if unco[0] else float("inf")
    vary = max(corr) / min(corr) if min(corr) else float("inf")
    print()
    print(f"  uncorrected growth over 4 decades = {grow:.4g}  (criterion: >= 1e3)")
    print(f"  corrected variation over the same = {vary:.4g}  (criterion: < 10)")
    tu1D = (grow >= 1e3) and (vary < 10)
    print(f"tu1-D  : {'PASS' if tu1D else 'FAIL'}")

    print()
    print("=" * 78)
    print("SUMMARY  tu1-A %s | tu1-B %s | tu1-C control %s | tu1-D %s | tu1-E %s" % (
        "PASS" if tu1A else "FAIL", "PASS" if tu1B else "FAIL",
        "FAILED-AS-DESIGNED" if ctrl_failed else "NO-POWER",
        "PASS" if tu1D else "FAIL", "PASS" if tu1E else "FAIL"))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
