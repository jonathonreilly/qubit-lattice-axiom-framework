"""Independent enumeration of the L=2 cubic-ice sector of the spin-half RK note.

Own code: 24 link bits, all vertex constraints, flux sectors, square flips,
graph Laplacian, charged orbits, twisted trial vector, plus a small
independent Monte Carlo for the flippability density at L=6 and the exact
formula ladders.  Nothing is imported from the note's runner.
"""
import sys, itertools, math, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

L = 2
def site(x, y, z): return ((x % L) * L + (y % L)) * L + (z % L)
SITES = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
def link(r, i): return site(*r) * 3 + i
def shift(r, i, s=1):
    r = list(r); r[i] += s; return tuple(v % L for v in r)
NL = 3 * L ** 3          # 24 links
par = lambda r: (-1) ** (r[0] + r[1] + r[2])

# vertex incidence lists: for each site, the six link indices
VERT = []
for r in SITES:
    inc = []
    for i in range(3):
        inc.append(link(r, i)); inc.append(link(shift(r, i, -1), i))
    VERT.append(inc)
check("each L=2 vertex has six distinct incident links", all(len(set(v)) == 6 for v in VERT))

# all 24-bit words with a given popcount, built without itertools.combinations on 2.7M tuples
words = np.arange(1 << NL, dtype=np.uint32)
pc = np.zeros(1 << NL, dtype=np.uint8)
for b in range(NL): pc += ((words >> np.uint32(b)) & np.uint32(1)).astype(np.uint8)

def bits(sel):
    return np.stack([((sel >> np.uint32(b)) & np.uint32(1)).astype(np.int8) for b in range(NL)], axis=1)

sel12 = words[pc == 12]
check("C(24,12) candidate occupations", len(sel12) == math.comb(24, 12), f"n={len(sel12)}")
B12 = bits(sel12)
deg = np.stack([B12[:, v].sum(axis=1) for v in VERT], axis=1)
ice_mask = (deg == 3).all(axis=1)
ice = sel12[ice_mask]; Bice = B12[ice_mask]
print("ice configurations over all fluxes:", len(ice))
check("all-flux ice count is 9600", len(ice) == 9600)

# flux: sum of staggered E over the links crossing the plane r_i = c, doubled to stay integer
def flux2(Bm, i, c):
    tot = np.zeros(len(Bm), dtype=np.int64)
    for r in SITES:
        if r[i] == c:
            tot += par(r) * (2 * Bm[:, link(r, i)].astype(np.int64) - 1)
    return tot
F0 = np.stack([flux2(Bice, i, 0) for i in range(3)], axis=1)
F1 = np.stack([flux2(Bice, i, 1) for i in range(3)], axis=1)
check("flux through plane 0 equals flux through plane 1 (Gauss law, all 9600)", (F0 == F1).all())
zero = (F0 == 0).all(axis=1)
print("zero-flux count:", zero.sum())
check("zero-flux ice count is 880", zero.sum() == 880)
vals, cnts = np.unique(F0, axis=0, return_counts=True)
print("flux-sector sizes (2*flux vector -> count), first 12:", [(tuple(v), int(c)) for v, c in list(zip(vals, cnts))[:12]], "... total sectors", len(vals))
check("sector sizes add to 9600", cnts.sum() == 9600)

# plaquettes: (r,i,j) with i<j ; bottom (r,i), right (r+e_i,j), top (r+e_j,i), left (r,j)
PLAQ = []
for r in SITES:
    for i in range(3):
        for j in range(i + 1, 3):
            b, rt, t, lf = link(r, i), link(shift(r, i), j), link(shift(r, j), i), link(r, j)
            PLAQ.append((b, rt, t, lf))
check("24 plaquettes each with four distinct links", len(PLAQ) == 24 and all(len(set(p)) == 4 for p in PLAQ))

def flips_of(word):
    """list of (plaquette index, new word) for every flippable plaquette (1010 <-> 0101)."""
    out = []
    for k, (b, rt, t, lf) in enumerate(PLAQ):
        nb, nr, nt, nl = (word >> b) & 1, (word >> rt) & 1, (word >> t) & 1, (word >> lf) & 1
        if nb == nt and nr == nl and nb != nr:
            out.append((k, word ^ ((1 << b) | (1 << rt) | (1 << t) | (1 << lf))))
    return out

def laplacian_from_states(states):
    idx = {int(w): n for n, w in enumerate(states)}
    rows, cols, deg_ = [], [], np.zeros(len(states))
    for n, w in enumerate(states):
        for k, w2 in flips_of(int(w)):
            m = idx.get(w2)
            if m is None: return None, None, "leaves set"
            rows.append(n); cols.append(m); deg_[n] += 1
    A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(states),) * 2).tocsr()
    return A, deg_, None

Z = [int(w) for w in ice[zero]]
A, dg, err = laplacian_from_states(Z)
check("square flips keep the zero-flux ice set closed (no exits)", err is None)
check("move graph symmetric (every flip is an involution)", abs(A - A.T).sum() == 0)
ncomp, lab = connected_components(A, directed=False)
sizes = sorted(np.bincount(lab).tolist(), reverse=True)
print("component sizes in zero-flux sector:", sizes[:5], "... count", ncomp)
check("zero-flux sector = one 864-state component + 16 singletons", sizes[0] == 864 and sizes[1:] == [1] * 16 and len(sizes) == 17)
frozen = [n for n in range(len(Z)) if dg[n] == 0]
check("the 16 singletons are exactly the states with no flippable plaquette", len(frozen) == 16)

# mobile orbit Hamiltonian, built two ways
big = int(np.argmax(np.bincount(lab)))
mob = [n for n in range(len(Z)) if lab[n] == big]
Zm = [Z[n] for n in mob]
Am, dm, _ = laplacian_from_states(Zm)
Hm = np.diag(dm) - Am.toarray()
idxm = {w: n for n, w in enumerate(Zm)}
H2 = np.zeros_like(Hm)
for n, w in enumerate(Zm):                       # H = sum_p (|s>-|t>)(<s|-<t|) over unordered pairs, once per plaquette
    for k, w2 in flips_of(w):
        m = idxm[w2]
        if n < m:
            v = np.zeros(len(Zm)); v[n] = 1; v[m] -= 1
            H2 += np.outer(v, v)
check("H = D - A equals the sum of rank-one plaquette projector terms", np.abs(H2 - Hm).max() == 0)
ev = np.linalg.eigvalsh(Hm)
print("lowest eigenvalues:", np.round(ev[:8], 9))
check("equal-amplitude vector is annihilated", np.abs(Hm @ np.ones(len(Zm))).max() < 1e-12)
check("positive semidefinite", ev[0] > -1e-10)
check("exactly one zero mode (connected)", (np.abs(ev) < 1e-9).sum() == 1)
check("first positive eigenvalue 0.969623617, doubly degenerate", abs(ev[1] - 0.969623617) < 5e-10 and abs(ev[2] - 0.969623617) < 5e-10 and ev[3] - ev[2] > 0.1)
check("third level 1.16086551, doubly degenerate", abs(ev[3] - 1.16086551) < 5e-9 and abs(ev[4] - 1.16086551) < 5e-9)
print("rounded full spectrum multiplicities (top 10 lowest distinct):", [(round(float(v), 6), int(c)) for v, c in zip(*np.unique(np.round(ev, 7), return_counts=True))][:10])

# ---- twisted trial vector ----
def E2(word, i, r):     # doubled staggered field on link (r,i)
    return par(r) * (2 * ((word >> link(r, i)) & 1) - 1)
Bf = 2 * math.pi / L ** 2
Acoef = {}
for r in SITES:
    Acoef[(r, 1)] = Bf * r[0]                          # A_y(x,y,z) = B x
for r in SITES:
    if r[0] == L - 1: Acoef[(r, 0)] = -Bf * L * r[1]   # A_x(L-1,y,z) = -B L y
# curls of this A on every plaquette, mod 2 pi
def circ(r, i, j):
    g = lambda rr, k: Acoef.get((rr, k), 0.0)
    return g(r, i) + g(shift(r, i), j) - g(shift(r, j), i) - g(r, j)
curls = {}
for r in SITES:
    for i in range(3):
        for j in range(i + 1, 3):
            curls[(r, i, j)] = circ(r, i, j)
frac = {k: round(((v + math.pi) % (2 * math.pi) - math.pi) / Bf, 9) for k, v in curls.items()}
print("plaquette curl in units of B (mod 2pi):", sorted(set(frac.values())), " raw values:", sorted(set(round(v / Bf, 6) for v in curls.values())))
xy_ok = all(abs(frac[k] - 1) < 1e-8 for k in frac if (k[1], k[2]) == (0, 1))
other_ok = all(abs(frac[k]) < 1e-8 for k in frac if (k[1], k[2]) != (0, 1))
check("xy plaquettes carry flux B mod 2 pi, xz and yz plaquettes carry none", xy_ok and other_ok)
dirac = [k for k, v in curls.items() if (k[1], k[2]) == (0, 1) and abs(v / Bf + 3) < 1e-8]
check("the x-jump puts a -3B = B - 2 pi (one Dirac quantum) on the xy plaquettes with y=1 at x=L-1", len(dirac) == 2 and all(k[0][0] == 1 and k[0][1] == 1 for k in dirac), f"{len(dirac)} such plaquettes")
psi = np.array([np.exp(1j * sum(0.5 * Acoef.get((r, i), 0.0) * E2(w, i, r) for r in SITES for i in range(3))) for w in Zm])
nrm = np.vdot(psi, psi).real
Hpsi = Hm @ psi
Eexp = (np.vdot(psi, Hpsi) / nrm).real
E2exp = (np.vdot(Hpsi, Hpsi) / nrm).real
ov = abs(np.sum(psi)) ** 2 / (len(Zm) * nrm)
print(f"<H> = {Eexp:.12f}  (8/3 = {8/3:.12f});  var = {E2exp - Eexp**2:.12f}  (44/9 = {44/9:.12f});  overlap^2 = {ov:.12f} (1/16 = {1/16})")
check("twisted vector expectation 8/3", abs(Eexp - 8 / 3) < 1e-10)
check("twisted vector variance 44/9", abs(E2exp - Eexp ** 2 - 44 / 9) < 1e-10)
check("squared overlap with equal-amplitude state 1/16", abs(ov - 1 / 16) < 1e-12)
# gauge invariance of the trial state's statistics under shifting A by a constant curl-free amount is not assumed; instead print the flip phases
dth = set()
for n, w in enumerate(Zm):
    for k, w2 in flips_of(w):
        d = np.angle(psi[idxm[w2]] / psi[n]); dth.add(round(d / (math.pi / 2), 6))
print("phase step across a flip in units of pi/2:", sorted(dth))

# ---- charged sectors: 13 occupied links, exactly two degree-4 vertices ----
sel13 = words[pc == 13]
B13 = bits(sel13)
deg13 = np.stack([B13[:, v].sum(axis=1) for v in VERT], axis=1)
two4 = ((deg13 == 4).sum(axis=1) == 2) & ((deg13 == 3).sum(axis=1) == 6)
Ch = sel13[two4]; degC = deg13[two4]
print("configs with exactly two degree-4 vertices and six degree-3:", len(Ch))
Cw = [int(w) for w in Ch]
Ac, dc, err = laplacian_from_states(Cw)
check("square flips keep the charged set closed", err is None)
nc, labc = connected_components(Ac, directed=False)
szc = np.bincount(labc)
print("charged orbit size census (size:count):", dict(zip(*[a.tolist() for a in np.unique(szc, return_counts=True)])))
check("an orbit of exactly 508 states exists among two-charge sectors", (szc == 508).any(), f"sizes seen {sorted(set(szc.tolist()), reverse=True)[:8]}")
for o in np.where(szc == 508)[0][:6]:
    members = [n for n in range(len(Cw)) if labc[n] == o]
    dv = tuple(int(np.where(degC[members[0]] == 4)[0][k]) for k in range(2))
    ps = [SITES[v] for v in dv]
    opp = par(ps[0]) != par(ps[1])
    same_defects = all(tuple(np.where(degC[m] == 4)[0]) == tuple(np.where(degC[members[0]] == 4)[0]) for m in members)
    Hc = np.diag(dc[members]) - Ac[members][:, members].toarray()
    evc = np.linalg.eigvalsh(Hc)
    fx = tuple(int(flux2(np.array([bits(np.array([Cw[members[0]]], dtype=np.uint32))[0]]), i, 0)[0]) for i in range(3))
    print(f"  508-orbit {o}: charges at {ps}, opposite sublattices={opp}, defect sites fixed over orbit={same_defects}, zero modes={(np.abs(evc)<1e-9).sum()}, lowest positive={evc[evc>1e-9][0]:.9f}, plane-0 flux2={fx}, |A e|max={np.abs(Hc@np.ones(len(members))).max():.1e}")
o508 = np.where(szc == 508)[0]
if len(o508):
    ok = True
    for o in o508:
        members = [n for n in range(len(Cw)) if labc[n] == o]
        ps = [SITES[v] for v in np.where(degC[members[0]] == 4)[0]]
        ok &= (par(ps[0]) != par(ps[1]))
    check("every 508-orbit has its two charges on opposite sublattices", ok)
# every two-degree-4 config has opposite-parity endpoints?
opp_all = all(par(SITES[int(a)]) != par(SITES[int(b)]) for a, b in (np.where(row == 4)[0] for row in degC))
print("all 13-link two-defect configs have opposite-sublattice defects:", opp_all)
# find which single-link addition on a zero-flux mobile state yields a 508-orbit
addable = {}
for w in Zm[:3]: pass
cw_index = {w: n for n, w in enumerate(Cw)}
starts = set()
for w in Z:
    for b in range(NL):
        if not (w >> b) & 1:
            w13 = w | (1 << b)
            if w13 in cw_index: starts.add(int(labc[cw_index[w13]]))
print("charged orbits reachable by adding one link to a zero-flux ice state (orbit sizes):", sorted(int(szc[o]) for o in starts))
check("a 508-orbit arises by adding one link to a zero-flux ice state", any(szc[o] == 508 for o in starts))

# ---- exact formula ladders ----
ratios = [Lx ** 4 * (1 - math.cos(2 * math.pi / Lx ** 2)) / (2 * math.pi ** 2) for Lx in (6, 8, 10, 12)]
print("L E_trial / (2 pi^2 n_f) for L=6,8,10,12:", [round(r, 5) for r in ratios])
check("trial-formula ratios run from 0.99746 to 0.99984", abs(ratios[0] - 0.99746) < 6e-6 and abs(ratios[-1] - 0.99984) < 6e-6)

def curl_eigs(k):
    q = np.exp(1j * np.array(k)) - 1
    C = np.array([[0, -q[2], q[1]], [q[2], 0, -q[0]], [-q[1], q[0], 0]])
    return np.sort(np.linalg.eigvalsh(C.conj().T @ C)), float((abs(q) ** 2).sum())
worst = 0.0; nk = 0
for Lx in (4, 6, 8, 12):
    for m in itertools.product(range(Lx), repeat=3):
        if m == (0, 0, 0): continue
        ev3, q2 = curl_eigs([2 * math.pi * a / Lx for a in m])
        worst = max(worst, abs(ev3[0]), abs(ev3[1] - q2), abs(ev3[2] - q2)); nk += 1
check("curl^dagger curl has eigenvalues 0, |q|^2, |q|^2 at every nonzero momentum on L=4,6,8,12", worst < 1e-12, f"worst dev {worst:.1e} over {nk} momenta")
om = [2 * math.sin(math.pi / Lx) / (2 * math.pi / Lx) for Lx in (8, 16, 32, 64, 128)]
check("omega/|k| along the axis increases toward one and exceeds 0.9998 at L=128", all(a < b for a, b in zip(om, om[1:])) and om[-1] > 0.9998, f"{[round(v,6) for v in om]}")

# ---- independent Monte Carlo of the flippable-plaquette density on L=6 ----
def mc_density(Lm, sweeps, burn, seed, start='lines'):
    rng = np.random.default_rng(seed)
    ax = np.arange(Lm)
    X, Y, Zg = np.meshgrid(ax, ax, ax, indexing='ij')
    parity = (-1) ** (X + Y + Zg)
    if start == 'stripes':
        n = np.stack([((X, Y, Zg)[i] % 2).astype(np.int8) for i in range(3)])
    else:
        n = np.zeros((3, Lm, Lm, Lm), dtype=np.int8)
        # E constant along each axial line, half the lines reversed -> zero flux, divergence free
        for i in range(3):
            others = [k for k in range(3) if k != i]
            sgn = np.ones((Lm, Lm)); flat = sgn.reshape(-1); flat[: Lm * Lm // 2] = -1
            rng.shuffle(flat)
            s3 = np.zeros((Lm, Lm, Lm))
            for a in range(Lm):
                for b in range(Lm):
                    idx = [None, None, None]; idx[others[0]] = a; idx[others[1]] = b; idx[i] = slice(None)
                    s3[tuple(idx)] = sgn[a, b]
            n[i] = ((1 + parity * s3) // 2).astype(np.int8)
    def flippable(i, j):
        b = n[i]; t = np.roll(n[i], -1, axis=j); rt = np.roll(n[j], -1, axis=i); lf = n[j]
        return (b == t) & (rt == lf) & (b != rt)
    def check_ice():
        d = np.zeros((Lm,) * 3, dtype=int)
        for i in range(3): d += n[i] + np.roll(n[i], 1, axis=i)
        return (d == 3).all()
    dens = []
    for sw in range(sweeps + burn):
        for i in range(3):
            for j in range(i + 1, 3):
                for ci in range(2):
                    for cj in range(2):
                        cls = np.zeros((Lm,) * 3, dtype=bool)
                        sl = [slice(None)] * 3; sl[i] = slice(ci, None, 2); sl[j] = slice(cj, None, 2)
                        cls[tuple(sl)] = True
                        m = flippable(i, j) & cls & (rng.random((Lm,) * 3) < 0.5)
                        n[i] ^= m.astype(np.int8); n[i] ^= np.roll(m, 1, axis=j).astype(np.int8)
                        n[j] ^= np.roll(m, 1, axis=i).astype(np.int8); n[j] ^= m.astype(np.int8)
        if sw >= burn:
            tot = sum(flippable(i, j).sum() for i in range(3) for j in range(i + 1, 3))
            dens.append(tot / (3 * Lm ** 3))
    assert check_ice()
    return np.array(dens)

def blocked(x, nb=20):
    m = len(x) // nb; return x[: m * nb].reshape(nb, m).mean(axis=1)
t0 = time.time()
# (a) two different zero-flux starts on L=6 -- random axial lines vs the stripe pattern n=r_i mod 2 -- long chains
dl = mc_density(6, 30000, 1000, 11, 'lines'); ds = mc_density(6, 30000, 1000, 12, 'stripes')
el = blocked(dl).std(ddof=1) / math.sqrt(20); es = blocked(ds).std(ddof=1) / math.sqrt(20)
print(f"L=6 long chains: lines start {dl.mean():.5f}+-{el:.5f}, stripe start {ds.mean():.5f}+-{es:.5f}")
check("the L=6 flippability density does not depend on the zero-flux start (lines vs stripes)", abs(dl.mean() - ds.mean()) < 4 * math.hypot(el, es) + 2e-4)
# (b) the note's protocol (500 burn-in, 1600 samples every 2 sweeps) repeated with independent seeds: distribution of one chain's mean
note_val = {6: 0.262313, 8: 0.260063, 10: 0.259975, 12: 0.259755}
note_err = {6: 0.000310, 8: 0.000155, 10: 0.000183, 12: 0.000105}
nchain = {6: 16, 8: 16, 10: 8, 12: 6}
ens = {}
for Lm in (6, 8, 10, 12):
    m = np.array([mc_density(Lm, 3200, 500, 5000 + 31 * Lm + s, 'stripes')[1::2].mean() for s in range(nchain[Lm])])
    ens[Lm] = m
    z = (note_val[Lm] - m.mean()) / m.std(ddof=1)
    print(f"L={Lm}: {nchain[Lm]} independent note-length chains: mean {m.mean():.5f}, sd of a single chain {m.std(ddof=1):.5f}; note's single chain {note_val[Lm]:.6f} is {z:+.2f} sd from my mean ({time.time()-t0:.0f}s)")
    check(f"note's L={Lm} density is a plausible draw from the ensemble of same-length chains (|z|<3.5)", abs(z) < 3.5, f"z={z:+.2f}")
means = {Lm: ens[Lm].mean() for Lm in ens}
check("my ensemble means stay between 0.2590 and 0.2620 at L=6..12 and decrease with L", all(0.259 < v < 0.262 for v in means.values()) and means[6] > means[8] > means[10] > means[12] - 1e-4, f"{ {k: round(v, 5) for k, v in means.items()} }")
print("note L=6..12 densities minus my ensemble means:", {Lm: round(note_val[Lm] - means[Lm], 5) for Lm in means})
if FAIL == 0:
    print(f"SUMMARY: no falsifier fired: the L=2 census (9600 / 880 / 864 + 16), the graph-Laplacian spectrum, the 508-state charged orbit, the twisted vector (8/3, 44/9, 1/16), the formula ladders and the sampled densities at L=6..12 all reproduce; {PASS} checks pass; the note's fixed-seed densities are single-chain draws (ensemble means {means[6]:.4f}, {means[8]:.4f}, {means[10]:.4f}, {means[12]:.4f})")
else:
    print(f"SUMMARY: {FAIL} of my own checks failed; see the [FAIL] lines above")
sys.exit(0)
