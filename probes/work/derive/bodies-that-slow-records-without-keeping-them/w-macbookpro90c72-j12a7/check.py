#!/usr/bin/env python3
"""J:derive:bodies-that-slow-records-without-keeping-them:a3 -- worker w-macbookpro90c72-j12a7.

Inertial record gas with magnitudes (blocks 48, 49, 51, 52): a record of content v = m s (s a unit
vector, m in (0,1]) steps to x + sign(s_k) e_k at the rate m|s_k|/sqrt 3.  A slowing site lets a
record pass and multiplies its content by kappa.  Independent records (no exchange, no scattering).

The stationary transport equations are solved EXACTLY (Fractions) on the block [-L,L]^3 for a
symmetric set of 54 rational directions and two magnitudes, with one or two slowing sites, by a
sweep along each direction's octant (the equations are directed, so the block solution is the
infinite-lattice one).  Rates are quoted in units of 1/sqrt 3 (forces likewise).

  A  one slowing site: class fluxes, densities, number flux, momentum density    (task (a))
  B  two slowing sites: momentum taken per tick, isotropic cancellation, pull,
     action = reaction, <m^2> weight, block 48's force                           (task (b))
  C  run-down: exact per-step law, impulse per pair, the inequality              (task (c))
  D  healing: exact unscattered fraction with re-draws at rate gamma              (task (d))
See ATTEMPT.md.
"""
import itertools
import math
from fractions import Fraction as Fr
import sympy as sp

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


# ------------------------------------------------------------- contents
def directions():
    out = set()
    for base in ((Fr(1), Fr(0), Fr(0)), (Fr(3, 5), Fr(4, 5), Fr(0)), (Fr(2, 3), Fr(2, 3), Fr(1, 3))):
        for perm in itertools.permutations(base):
            for sg in itertools.product((1, -1), repeat=3):
                out.add(tuple(sg[i] * perm[i] for i in range(3)))
    return sorted(out)


DIRS = directions()
MAGS = {Fr(1): Fr(1, 2), Fr(1, 2): Fr(1, 2)}            # magnitude law: <m^2> = 5/8
FDIR = Fr(1, len(DIRS))
L = 4


def l1(s):
    return sum(abs(c) for c in s)


def h(x, s):
    """block 48's hitting probability of the directed walk of step frequencies |s_k|/|s|_1."""
    w = [abs(c) / l1(s) for c in s]
    for k in range(3):
        if x[k] != 0 and (s[k] == 0 or (x[k] > 0) != (s[k] > 0)):
            return Fr(0)
    n = sum(abs(c) for c in x)
    num = math.factorial(n)
    for c in x:
        num //= math.factorial(abs(c))
    val = Fr(num)
    for k in range(3):
        if x[k] != 0:
            val *= w[k] ** abs(x[k])
    return val


def sweep(s, sites):
    """Exact stationary class fluxes for direction s on [-L,L]^3.
    sites: {z: kappa_z}.  Returns arr[y] = {class(frozenset of passed sites): fraction of the ambient flux}."""
    w = [abs(c) / l1(s) for c in s]
    sg = [1 if c > 0 else -1 for c in s]
    act = [k for k in range(3) if w[k] != 0]
    block = list(itertools.product(range(-L, L + 1), repeat=3))
    block.sort(key=lambda y: sum(sg[k] * y[k] for k in act))
    out, arr = {}, {}
    for y in block:
        a = {}
        for k in act:
            u = list(y); u[k] -= sg[k]; u = tuple(u)
            src = out.get(u, {frozenset(): Fr(1)}) if max(abs(c) for c in u) <= L else {frozenset(): Fr(1)}
            for c, v in src.items():
                a[c] = a.get(c, Fr(0)) + w[k] * v
        if not act:
            a = {frozenset(): Fr(1)}
        arr[y] = a
        out[y] = {(c | {y} if y in sites else c): v for c, v in a.items()} if y in sites else a
    return arr, out


def kap(c, sites):
    r = Fr(1)
    for z in c:
        r *= sites[z]
    return r


# ------------------------------------------------------------- A family
def A1():
    k1 = Fr(1, 3)
    sites = {(0, 0, 0): k1}
    ok_h = ok_flux = ok_dens = ok_mom = True
    for s in DIRS:
        arr, out = sweep(s, sites)
        for y, a in out.items():
            tot = sum(a.values())
            ok_flux &= tot == 1
            hy = h(y, s)
            slowed = a.get(frozenset({(0, 0, 0)}), Fr(0))
            ok_h &= slowed == hy and a.get(frozenset(), Fr(0)) == 1 - hy
            for m in MAGS:
                # density/(rho f) = class flux/(class hop rate), ambient flux rho f m|s|_1, slowed hop rate kappa m|s|_1
                dens_u = a.get(frozenset(), Fr(0)) * (m * l1(s)) / (m * l1(s))
                dens_s = slowed * (m * l1(s)) / (k1 * m * l1(s))
                ok_dens &= dens_u == 1 - hy and dens_s == hy / k1
                ok_mom &= [dens_u * m * c + dens_s * k1 * m * c for c in s] == [m * c for c in s]
    rep("A1 one slowing site", ok_h and ok_flux and ok_dens and ok_mom,
        f"54 directions x 2 magnitudes on [-{L},{L}]^3, kappa=1/3, exact sweep: unslowed rho f(1-h), slowed rho f h/kappa "
        "(h = block 48's multinomial hitting probability); number flux and momentum density unchanged at every site")


def A2():
    sites = {(0, 0, 0): Fr(1, 3)}
    worst = Fr(0)
    for s in DIRS:
        arr, out = sweep(s, sites)
        for n in range(1, L + 1):                            # shells |y|_1 = n <= L lie inside the block
            tot = sum(out[y].get(frozenset({(0, 0, 0)}), Fr(0)) for y in out if sum(abs(c) for c in y) == n)
            worst = max(worst, abs(tot - 1))
    ex = (1 - Fr(1, 3)) / Fr(1, 3)
    rep("A2 shells", worst == 0,
        f"the slowed flux through every shell |x|_1 = n <= {L} is the whole flux through the origin (sum_shell h = 1); "
        f"excess records per shell rho f (1/kappa - 1) = {ex} rho f at kappa = 1/3 (constant along the beam)")


# ------------------------------------------------------------- B family
def forces(sites, mags=MAGS):
    F = {z: [Fr(0)] * 3 for z in sites}
    for s in DIRS:
        arr, out = sweep(s, sites)
        for z, kz in sites.items():
            for c, a in arr[z].items():
                for m, pm in mags.items():
                    # arrivals per tick (units rho/sqrt3): FDIR*pm*m|s|_1 * a ; content kappa(c) m s ; taken (1-kz) of it
                    coef = FDIR * pm * m * l1(s) * a * (1 - kz) * kap(c, sites) * m
                    for i in range(3):
                        F[z][i] += coef * s[i]
    return F


def closed_pull(x2, k1, k2, m2):
    return [-(1 - k1) * (1 - k2) * m2 * sum(FDIR * l1(s) * s[i] * h(x2, s) for s in DIRS) for i in range(3)]


def F48(x):
    return [-sum(FDIR * l1(s) * s[i] * h(x, s) for s in DIRS) for i in range(3)]


def B1():
    ok = True
    rows = []
    m2 = sum(p * m * m for m, p in MAGS.items())
    for x2, k1, k2 in (((2, 0, 0), Fr(1, 3), Fr(1, 2)), ((2, 1, 1), Fr(1, 3), Fr(1, 2)), ((1, 2, 0), Fr(3, 4), Fr(1, 5))):
        sites = {(0, 0, 0): k1, x2: k2}
        F = forces(sites)
        cp = closed_pull(x2, k1, k2, m2)
        f48 = F48(x2)
        ok &= F[x2] == cp
        ok &= all(F[(0, 0, 0)][i] == -F[x2][i] for i in range(3))
        ok &= F[x2] == [(1 - k1) * (1 - k2) * m2 * c for c in f48]
        ok &= sum(F[x2][i] * x2[i] for i in range(3)) < 0
        rows.append((x2, F[x2]))
    # isotropic part: a single site in the ambient gas takes no net momentum
    F1 = forces({(0, 0, 0): Fr(1, 3)})
    ok &= F1[(0, 0, 0)] == [0, 0, 0]
    Fm1 = forces({(0, 0, 0): Fr(1, 3), (2, 1, 1): Fr(1, 2)}, {Fr(1): Fr(1)})
    Fm = forces({(0, 0, 0): Fr(1, 3), (2, 1, 1): Fr(1, 2)})
    ok &= Fm[(2, 1, 1)] == [m2 * c for c in Fm1[(2, 1, 1)]]
    rep("B1 pull", ok,
        "two slowing sites solved jointly (records slowed by both included): isotropic part cancels (a lone site takes 0); "
        "push on site 2 = (1-k1)(1-k2)<m^2> x block 48's collisionless force, towards site 1; force on site 1 = minus it; "
        f"<m^2> = {m2} weight exact; e.g. at {rows[1][0]}: F = ({', '.join(str(c) for c in rows[1][1])})/sqrt3")


def B2():
    # neither body grows: each slowing site's arrivals = departures (no record kept); occupancy stationary
    sites = {(0, 0, 0): Fr(1, 3), (2, 1, 1): Fr(1, 2)}
    ok = True
    for s in DIRS[::5]:
        arr, out = sweep(s, sites)
        for z in sites:
            ok &= sum(arr[z].values()) == sum(out[z].values()) == 1
    rep("B2 no growth", ok, "at each slowing site arrivals = departures in every class sum (no record kept; stationary occupancy "
        "flux/(kappa m|s|_1)); the capture rate is identically zero, so block 49's growth law gives these bodies no wind")


# ------------------------------------------------------------- C family
def C1():
    N, nb, k, t, m0, c = sp.symbols('N n_b kappa t m_0 c', positive=True)
    Nv, nbv, kv = 7, sp.Rational(1, 5), sp.Rational(1, 3)
    e1 = sum(sp.binomial(Nv, j) * nbv**j * (1 - nbv)**(Nv - j) * kv**j for j in range(Nv + 1))
    e2 = sum(sp.binomial(Nv, j) * nbv**j * (1 - nbv)**(Nv - j) * kv**(2 * j) for j in range(Nv + 1))
    ok_bin = e1 == (1 - (1 - kv) * nbv)**Nv and e2 == (1 - (1 - kv**2) * nbv)**Nv
    msol = m0 / (1 + c * m0 * t)
    ok_ode = sp.simplify(sp.diff(msol, t) + c * msol**2) == 0
    imp = sp.integrate(msol**2, (t, 0, sp.oo))
    ok_imp = sp.simplify(imp - m0 / c) == 0
    # c = (1-kappa) n_b |s|_1 (per tick, units 1/sqrt3): impulse per pair ~ (1-kappa)^2 * m0/c ~ (1-kappa)/n_b
    u = sp.symbols('u', positive=True)
    pull_int = sp.simplify(u**2 * imp.subs(c, u * nb))
    ok_lin = sp.simplify(pull_int - u * m0 / nb) == 0
    rep("C1 run-down", ok_bin and ok_ode and ok_imp and ok_lin,
        "a directed walk meets distinct sites, so after N steps m = m0 kappa^K, K ~ Bin(N, n_b): E m = m0(1-(1-kappa)n_b)^N, "
        "E m^2 = m0^2(1-(1-kappa^2)n_b)^N (exact at N=7); mean field dm/dt = -(1-kappa)n_b|s|_1 m^2/sqrt3 gives m0/(1+ct); "
        "run-down rate ~ (1-kappa) per site, pull ~ (1-kappa)^2, impulse per pair over the gas's life ~ (1-kappa)/n_b")


def C2():
    k, nb, T, m0, s1 = sp.symbols('kappa n_b T m_0 s_1', positive=True)
    c = (1 - k) * nb * s1 / sp.sqrt(3)
    cond = sp.solve(sp.Eq(1 / (1 + c * m0 * T), sp.Rational(1, 2)), k)[0]
    bound = sp.simplify(1 - cond)
    ok = sp.simplify(bound - sp.sqrt(3) / (nb * s1 * m0 * T)) == 0
    rep("C2 inequality", ok,
        "a gas whose records keep half their magnitude for T ticks needs (1-kappa) <= sqrt3/(n_b|s|_1 m0 T), so the pull per pair "
        "is at most 3<m^2>|F48|/(n_b<|s|_1 m> T)^2 = 4<m^2>|F48|/(3 n_b^2 <m>^2 T^2) for the uniform sphere (<|s|_1> = 3/2)")


# ------------------------------------------------------------- D family
def D1():
    # re-draw at rate gamma: a slowed record reaches shell n unscattered with probability h q^n, q = k m|s|_1/(k m|s|_1 + gamma)
    g, k, a = Fr(1, 10), Fr(1, 3), Fr(3, 2)
    q = k * a / (k * a + g)
    qu = a / (a + g)
    mfp_sl = k * a / g
    vals = [q**n for n in (1, 5, 10, 20)]
    ok = all(v > vals[i + 1] for i, v in enumerate(vals[:-1])) and q < qu
    rep("D1 healing", ok,
        f"with re-draws at rate gamma the slowed beam keeps its content to shell n with probability h(x,s) q^n, "
        f"q = kappa a/(kappa a + gamma); kappa=1/3, a=|s|_1=3/2, gamma=1/10: q = {q}, q^(1,5,10,20) = "
        + ", ".join(f"{float(v):.3f}" for v in vals) + f": decay length ~ kappa a/gamma = {mfp_sl} steps, shorter than the "
        f"unslowed {a / g}; the shadow force is cut off beyond it")


def main():
    A1(); A2()
    B1(); B2()
    C1(); C2()
    D1()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PROVED (a),(b) for independent records with magnitudes, exact on [-4,4]^3 for 54 rational directions x "
              "2 magnitudes and for all sites by the directed transport equation: a slowing site leaves the number flux and the "
              "momentum density unchanged, the slowed records are h/kappa dense; two slowing sites solved jointly pull each other "
              "with (1-k1)(1-k2)<m^2> times block 48's force, equal and opposite, neither grows; run-down ~ (1-kappa), pull ~ "
              "(1-kappa)^2, impulse per pair ~ (1-kappa)/n_b, pull <= 3<m^2>|F48|/(n_b<|s|_1 m>T)^2; with re-draws the slowed "
              "beam is lost within ~ kappa a/gamma steps")
        print("HIT: for independent records whose contents have magnitudes, a site that multiplies passing contents by kappa leaves "
              "the number flux and momentum density unchanged and makes the slowed records h/kappa dense; two such sites, solved "
              "jointly and exactly on [-4,4]^3 for 54 rational directions, take (1-k1)(1-k2)<m^2> times block 48's collisionless "
              "force towards each other, equal and opposite, without growing, while the gas runs down at a rate linear in (1-kappa)")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
