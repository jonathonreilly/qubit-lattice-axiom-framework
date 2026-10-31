# f7: composite-covariance term of the uniform scalar U(1) chain (L = 3, n = 1..4) by explicit fine-link path sums.
# Criteria: checks/f7_criteria.md (written first). Closed form: FLOW.md §30 Proposition COV-sc.
import itertools, math, sys, time, resource
import numpy as np

L = 3
ORDERS = list(itertools.permutations(range(4)))
T0 = time.time()


def gauge(name):
    # returns A(mu, x) at eps = 1 (phases are linear in eps); x: (M, 4) int array of fine link base points
    if name == "A2=x1":
        return lambda mu, x: x[:, 0].astype(float) if mu == 1 else np.zeros(len(x))
    if name == "A1=-x2":
        return lambda mu, x: -x[:, 1].astype(float) if mu == 0 else np.zeros(len(x))
    raise ValueError(name)


def path_phases(start, end, A):
    """(24, M) phases of the axial paths start -> end, accumulated link by link, one row per coordinate order."""
    out = np.zeros((len(ORDERS), len(start)))
    for oi, order in enumerate(ORDERS):
        x = start.copy()
        ph = np.zeros(len(start))
        for mu in order:
            d = end[:, mu] - x[:, mu]
            for t in range(int(np.abs(d).max(initial=0))):
                fwd = d > t
                bwd = -d > t
                if fwd.any():
                    ph[fwd] += A(mu, x[fwd])
                    x[fwd, mu] += 1
                if bwd.any():
                    xm = x[bwd].copy()
                    xm[:, mu] -= 1
                    ph[bwd] -= A(mu, xm)
                    x[bwd, mu] -= 1
        assert (x == end).all()
        out[oi] = ph
    return out


def block_levels(n, centre):
    """sites[k] (k = 1..n) as (M_k, 4) fine coordinates inside the level-n block of `centre`; par[k] indexes sites[k+1]."""
    offs = np.array(list(itertools.product((-1, 0, 1), repeat=4)))  # L = 3: offsets m in {-1,0,1}^4
    sites = {n: np.array([centre])}
    par = {}
    for k in range(n - 1, 0, -1):
        up = sites[k + 1]
        sites[k] = (up[:, None, :] + (L**k) * offs[None, :, :]).reshape(-1, 4)
        par[k] = np.repeat(np.arange(len(up)), len(offs))
    return sites, par


def c_brute(n, s=1.0, gname="A2=x1", centre=(0, 0, 0, 0), eps_list=()):
    """returns (c_n by analytic second derivative, {eps: log C(eps) per block})."""
    A = gauge(gname)
    sites, par = block_levels(n, np.array(centre))
    var, w2 = {}, {}
    for k in range(1, n):
        ph = path_phases(sites[k], sites[k + 1][par[k]], A)
        var[k] = ph.var(axis=0)                                   # Var_sigma(phi), eps = 1
        w2[k] = {}
        for e in eps_list:                                        # row by row: no (24, M) complex temporary
            acc = np.zeros(ph.shape[1], dtype=complex)
            for row in ph:
                acc += np.exp(1j * e * row)
            w2[k][e] = np.abs(acc / len(ph))**2
        del ph
    C0 = 0.0
    C2 = 0.0
    Ce = {e: 0.0 for e in eps_list}
    for j in range(1, n + 1):
        kap = s * L**(2 * j)
        wgt = L**(-8.0 * (n - j)) / kap
        M = len(sites[j])
        idx = np.arange(M)
        sumvar = np.zeros(M)
        prod = {e: np.ones(M) for e in eps_list}
        for k in range(j, n):                                     # walk the ancestor chain explicitly
            sumvar += var[k][idx]
            for e in eps_list:
                prod[e] *= w2[k][e][idx]
            idx = par[k][idx]
        C0 += wgt * M
        C2 += wgt * np.sum(-2.0 * sumvar)
        for e in eps_list:
            Ce[e] += wgt * prod[e].sum()
    c = 0.5 * C2 / C0 / L**(4 * n)
    return c, {e: math.log(Ce[e]) for e in eps_list}, math.log(C0)


def c_closed(n):
    x = L**-2.0
    cinf = -(L**2 - 1) / (576.0 * (L**4 + L**2 + 1))
    return cinf * (1 - x**(n - 1) * (1 + x**n) / (1 + x)), cinf


print("f7: uniform scalar U(1) chain, L = 3, composite-covariance term; criteria checks/f7_criteria.md")
res = {}
fin = {}
for n in (1, 2, 3, 4):
    t = time.time()
    h = 2e-4
    eps = (h, -h, h / 2, -h / 2) if n >= 2 else ()
    c, ge, g0 = c_brute(n, eps_list=eps)
    res[n] = c
    if n >= 2:
        D = lambda hh: (ge[hh] + ge[-hh] - 2 * g0) / hh**2
        g2 = (4 * D(h / 2) - D(h)) / 3
        fin[n] = 0.5 * g2 / L**(4 * n)
    cc, cinf = c_closed(n)
    extra = f"; finite-eps (Richardson) {fin[n]:.9e}" if n >= 2 else ""
    print(f"   n={n} ell={L**n}: brute c={c:.12e}  closed {cc:.12e}  diff {c-cc:+.2e}{extra}  [{time.time()-t:.1f}s]")
    sys.stdout.flush()
cinf = c_closed(1)[1]
print(f"   c_inf = {cinf:.12e}")
p1 = abs(res[1]) <= 1e-15
print(f"[P1] {'PASS' if p1 else 'FAIL'} :: |c_1| = {abs(res[1]):.1e} (<= 1e-15)")
ref = res[3]
g_alt, _, _ = c_brute(3, gname="A1=-x2")
pos_alt, _, _ = c_brute(3, centre=(27, -54, 0, 81))
d4 = max(abs(g_alt - ref), abs(pos_alt - ref)) / abs(ref)
print(f"[P4] {'PASS' if d4 <= 1e-12 else 'FAIL'} :: gauge A1=-x2: {g_alt:.12e}; centre 27(1,-2,0,3): {pos_alt:.12e}; "
      f"max rel {d4:.1e} (<= 1e-12)")
sv = [c_brute(3, s=s)[0] for s in (0.25, 1.0, 4.0)]
d5 = max(abs(v - ref) for v in sv) / abs(ref)
print(f"[P5] {'PASS' if d5 <= 1e-12 else 'FAIL'} :: s = 0.25, 1, 4: max rel {d5:.1e} (<= 1e-12)")
d2 = max(abs(res[n] - c_closed(n)[0]) for n in (2, 3, 4))
print(f"[P2] {'PASS' if d2 <= 1e-10 * abs(cinf) else 'FAIL'} :: max |c_n - closed|, n = 2..4: {d2:.2e} "
      f"(<= {1e-10*abs(cinf):.2e})")
d3 = abs(res[2] - (-0.00013717))
print(f"[P3] {'PASS' if d3 <= 1e-8 else 'FAIL'} :: |c_2 - f6 stored -0.00013717| = {d3:.2e} (<= 1e-8)")
r = abs(res[4] - res[3]) / abs(res[3] - res[2])
f7a = r <= 0.2
f7b = abs(res[4]) <= abs(cinf) * (1 + 1e-10)
print(f"[F7] {'PASS' if (f7a and f7b) else 'FAIL'} :: |c4-c3|/|c3-c2| = {r:.4f} (<= 0.2); |c4|/|c_inf| = "
      f"{abs(res[4])/abs(cinf):.6f} (<= 1 + 1e-10)")
print(f"   informational: finite-eps minus brute: " +
      ", ".join(f"n={n}: {fin[n]-res[n]:+.1e}" for n in (2, 3, 4)))
mx = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print(f"f7 done; wall {time.time()-T0:.1f}s; ru_maxrss {mx} (bytes on darwin)")
