"""A31 c4: one-excitation spectra over the calm emptiness for the spin-rotation-invariant signed
exchange H = J sum_b eta_b s.s (one qubit per site), on an 8x8x8 torus (512 one-excitation states).

One excitation (a flipped site) over |n...n>: hop 2J eta_b, on-site energy -2J s_x relative to the
emptiness, s_x = sum of eta over the six bonds at x ("site sum").
(1) eta = 1 (plain Heisenberg): one band, no cone.
(2) KS gauge eta: cone points and their energy relative to the emptiness; spread of the cone energies.
(3) A gauge with constant site sum 0 (found by annealing on 4^3, tiled to 8^3): cone exactly at the
    emptiness energy (E_c = 0)?
(4) Masses: (a) staggered (-1)^(x+y+z) on-site potential [not producible by pair terms; added by hand],
    (b) bond dimerization on all axes, (c) the three role-symmetric bond modulations (classes A, B, C
    relative to the field's role layout s=0), (d) role-symmetric staggered next-nearest exchange.
    Reported: the gap at the cone energy.
"""
import signal, itertools, numpy as np
signal.alarm(55)
rng = np.random.default_rng(7)
def lattice(L):
    sites = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
    idx = {s:i for i,s in enumerate(sites)}
    E = [(1,0,0),(0,1,0),(0,0,1)]
    bonds = [(idx[s], idx[tuple((s[i]+E[a][i]) % L for i in range(3))], a, s) for s in sites for a in range(3)]
    return sites, idx, bonds
def ks(s, a): return [1, (-1)**s[0], (-1)**(s[0]+s[1])][a]
def site_sums(N, bonds, eta):
    ss = np.zeros(N)
    for k,(i,j,a,s) in enumerate(bonds): ss[i] += eta[k]; ss[j] += eta[k]
    return ss
# (3) anneal a constant-site-sum-0 gauge on 4^3, then tile it periodically to 8^3
s4, i4, b4 = lattice(4)
eta4 = np.array([ks(s,a) for i,j,a,s in b4], float)
U4 = np.array([i for i,j,a,s in b4]); V4 = np.array([j for i,j,a,s in b4])
def ss4(g):
    e = eta4 * g[U4] * g[V4]; out = np.zeros(64); np.add.at(out, U4, e); np.add.at(out, V4, e); return out
best = None
for rep in range(6):
    g = rng.choice([1.,-1.], 64); c = np.abs(ss4(g)).sum(); T = 2.0
    for sw in range(400):
        for _ in range(64):
            i = rng.integers(64); g[i] *= -1; c2 = np.abs(ss4(g)).sum()
            if c2 <= c or rng.random() < np.exp(-(c2-c)/T): c = c2
            else: g[i] *= -1
        T = max(0.02, T*0.99)
        if c == 0: break
    if c == 0: best = g.copy(); break
assert best is not None, "no constant-sum-0 gauge found"
g4 = {s4[i]: best[i] for i in range(64)}
L = 8
sites, idx, bonds = lattice(L); N = len(sites)
def onemag(eta, extra_diag=None, nnn=None):
    H = np.zeros((N, N))
    ss = site_sums(N, bonds, eta)
    H[np.diag_indices(N)] = -2.0 * ss
    for k,(i,j,a,s) in enumerate(bonds):
        H[i,j] += 2.0*eta[k]; H[j,i] += 2.0*eta[k]
    if extra_diag is not None: H[np.diag_indices(N)] += extra_diag
    if nnn is not None:
        for (i,j,w) in nnn:   # SU(2)-invariant exchange w s_i.s_j: hop 2w, on-site -2w at both ends
            H[i,j] += 2*w; H[j,i] += 2*w; H[i,i] -= 2*w; H[j,j] -= 2*w
    return H
def report(name, H, Ec=None):
    w = np.linalg.eigvalsh(H)
    if Ec is None:
        print(f"  {name}: band [{w.min():.3f}, {w.max():.3f}]"); return w
    d = np.abs(w - Ec); order = np.argsort(d)
    print(f"  {name}: 8 levels nearest E_c={Ec:+.3f}: {np.round(w[order[:8]]-Ec, 4).tolist()}  gap at E_c = {2*d[order[0]]:.4f}")
    return w
print("(1) plain Heisenberg (eta = 1):")
w = report("one band", onemag(np.ones(len(bonds))))
k = 2*np.pi*np.arange(L)/L
disp = sorted(-4*sum(1-np.cos(kk) for kk in kv) for kv in itertools.product(k, repeat=3))
print(f"      matches -4J sum(1-cos k_a) [one analytic band, quadratic at k=0]: max dev {np.max(np.abs(np.sort(w)-np.array(disp))):.1e}")
eta_ks = np.array([ks(s,a) for i,j,a,s in bonds], float)
print("(2) KS gauge: site sums", sorted(set(site_sums(N, bonds, eta_ks).tolist())))
Hks = onemag(eta_ks)
wks = np.linalg.eigvalsh(Hks)
print(f"      spectrum range [{wks.min():.3f}, {wks.max():.3f}]; the site-sum potential mixes tastes, so the cone is distorted")
eta0 = np.array([ks(s,a) * g4[tuple(c%4 for c in s)] * g4[tuple(c%4 for c in sites[j])] for i,j,a,s in bonds], float)
ss0 = site_sums(N, bonds, eta0)
print(f"(3) constant-site-sum gauge: site sums {sorted(set(ss0.tolist()))}")
bdict = {}
for kk,(i,j,a,s_) in enumerate(bonds): bdict[frozenset((i,j))] = kk
E3 = [(1,0,0),(0,1,0),(0,0,1)]
def ad(p,e): return tuple((p[t]+e[t]) % L for t in range(3))
fl = set()
for s_ in sites:
    for a,b in [(0,1),(1,2),(0,2)]:
        p = [s_, ad(s_,E3[a]), ad(ad(s_,E3[a]),E3[b]), ad(s_,E3[b])]
        fl.add(int(np.prod([eta0[bdict[frozenset((idx[p[q]], idx[p[(q+1)%4]]))]] for q in range(4)])))
print(f"      plaquette products over all {3*N} plaquettes: {sorted(fl)}")
H0 = onemag(eta0)
w0 = report("cone at the emptiness energy", H0, Ec=0.0)
v = np.sort([4*np.sqrt(sum(np.cos(kk)**2 for kk in kv)) for kv in itertools.product(k, repeat=3)])
expect = np.sort(np.concatenate([v[::2], -v[::2]]))
print(f"      levels equal +-4J sqrt(sum_a cos^2 k_a) (pi-flux cones at k=(+-pi/2)^3, E_c = 0): max dev {np.max(np.abs(np.sort(w0)-expect)):.1e}")
print("(4) masses on the constant-site-sum-0 pattern (gap at E_c = 0):")
eps = np.array([(-1)**(x+y+z) for x,y,z in sites], float)
print(f"    pair-term site sums carry no staggered part: sum_x eps_x s_x = {np.dot(eps, ss0):.1f} (identically 0 for any bond weights)")
report("(a) staggered on-site mu=0.3 (by hand)", onemag(eta0, extra_diag=0.3*eps), Ec=0.0)
dim = np.array([(1+0.1*(-1)**s[a]) for i,j,a,s in bonds])
report("(b) bond dimerization 10% on all axes", onemag(eta0*dim), Ec=0.0)
def role(s): return sum(c % 2 for c in s)   # 0 vertex, 1 edge, 2 face, 3 cube (role pattern s=0)
cls = np.array([min(role(s), role(sites[j])) for i,j,a,s in bonds])   # A:0 (v-e), B:1 (e-f), C:2 (f-c)
for cname, cv in [('A', 0), ('B', 1), ('C', 2)]:
    mod = np.where(cls == cv, 1.1, 1.0)
    report(f"(c) role-symmetric modulation on class {cname} (+10%)", onemag(eta0*mod), Ec=0.0)
nnn = []
for i,(x,y,z) in enumerate(sites):
    for d in [(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]:
        j = idx[((x+d[0])%L, (y+d[1])%L, (z+d[2])%L)]
        nnn.append((i, j, 0.05*eps[i]))   # same-parity pair, staggered sign
report("(d) staggered next-nearest exchange 0.05", onemag(eta0, nnn=nnn), Ec=0.0)
