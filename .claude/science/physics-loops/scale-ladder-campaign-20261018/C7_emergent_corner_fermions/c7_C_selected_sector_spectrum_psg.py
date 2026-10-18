#!/usr/bin/env python3
"""C7 part C: the sector selected at Majorana half filling (1c+11: square = plaquette = tube = pi,
octant triangles +pi/2 outward), its Majorana spectrum, its projective symmetry group, its flux
excitation cost, and how it compares with the corner model.

 C0  1c+11 admits a translation-invariant (period-1) gauge; 12-band Bloch energy = 2^3-cell value.
 C1  Majorana spectrum: gap Delta(t2) = min over k of the lowest positive band (24^3 grid +
     Nelder-Mead), scan t2 in [0.05, 3]; every band 2-fold at random k; valleys (minima set).
 C2  PSG on L = 4 (orientation-aware Z2 sign propagation, imaginary amplitudes): C4^4, C2, C3
     signs, Tx Ty commutation, O-fixed momenta; the same for the corner model (real, u-pattern 1011)
     as a control (C6 A4: fixed momenta (1,3,1), (3,1,3) in units pi/2).
 C3  flux excitations: energy of flipping one u_e (one edge; changes the flux of its 3 faces) on
     the L = 4 torus with 8 boundary twists, every edge of one site.
 C4  the corner-model hopping family (t1 = -1, u-pattern 1011, chiral lambda): its face fluxes;
     is 1c+11 gauge-equivalent to any member?  (Exact: square pi - 4 arctan(lambda), triangle
     pi + 3 arctan(lambda), so no.)
 C5  the parton model with a chemical potential (imaginary hopping at filling nu): winners vs nu.
"""
import itertools, os, sys, time
import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from c7_common import Lattice, per_site, majorana_amp, real_amp, uniform_targets, TYPES, gf2_solve

PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)


L1 = Lattice(1); L2 = Lattice(2); L4 = Lattice(4)
P0 = (1, 'c+', 1, 1)


def ugauge(lat, P, model='maj'):
    base = majorana_amp(lat, np.zeros(lat.nE, np.uint8), 1, 1) if model == 'maj' else real_amp(lat, np.zeros(lat.nE, np.uint8), 1, 1)
    return lat.solve_u(base, uniform_targets(lat, *P, model))


# ------------------------------------------------------------------ C0
u1 = ugauge(L1, P0); u2 = ugauge(L2, P0)
e1 = per_site(L1.spectrum(majorana_amp(L1, u1, 1, 0.2), 16), 6)
e2 = per_site(L2.spectrum(majorana_amp(L2, u2, 1, 0.2), 8), 6)
check("C0: 1c+11 has a period-1 gauge (u translation invariant, 12 Majorana bands); E/site equals the 2^3-cell value",
      u1 is not None and abs(e1 - e2) < 1e-8, f"E = {e1:.8f} vs {e2:.8f}")
for P in [(1, 'c+', 0, 1), (1, 'c+', 1, 0), (1, 's+', 1, 1)]:
    print(f"   period-1 gauge for {P}: {'yes' if ugauge(L1, P) is not None else 'no'}")


# ------------------------------------------------------------------ C1
def bands(lat, amp, Ks):
    return np.linalg.eigvalsh(lat.blochH(amp, Ks))


def gap(lat, amp, nk=24, refine=True):
    Ks = lat.kgrid(nk)
    ev = bands(lat, amp, Ks)
    pos = np.where(ev > 1e-12, ev, np.inf).min(axis=1)
    i = int(np.argmin(pos))
    if not refine:
        return pos[i], Ks[i], Ks[np.abs(pos - pos[i]) < 1e-9]
    f = lambda k: np.min(np.abs(np.linalg.eigvalsh(lat.blochH(amp, k[None])[0])))
    best = (pos[i], Ks[i])
    for j in np.argsort(pos)[:6]:
        r = minimize(f, Ks[j], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-13, maxiter=3000))
        if r.fun < best[0]:
            best = (r.fun, r.x)
    return best[0], best[1], Ks[np.abs(pos - pos[i]) < 1e-9]


print(f"\nC1: Majorana spectrum of 1c+11 (period-1 gauge, 12 bands; t1 = 1); t = {time.time()-T0:.1f}s")
rng = np.random.default_rng(3)
deg_ok = True
for t2 in (0.2, 1.0):
    ev = bands(L1, majorana_amp(L1, u1, 1, t2), rng.uniform(0, 2 * np.pi, (50, 3)))
    deg_ok &= np.allclose(ev[:, ::2], ev[:, 1::2], atol=1e-9)
check("every Majorana band of 1c+11 is 2-fold at 50 random k (t2 = 0.2, 1)", deg_ok)
print("   t2     gap Delta   minimum at k/pi (this gauge)   #grid minima   bandwidth")
gaps = {}
for t2 in (0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.3, 1.6, 2.0, 2.5, 3.0):
    a = majorana_amp(L1, u1, 1, t2)
    D, k, mins = gap(L1, a)
    gaps[t2] = D
    bw = np.abs(bands(L1, a, L1.kgrid(8))).max()
    print(f"   {t2:4.2f}   {D:9.5f}   {np.round(k/np.pi, 4)}   {len(mins):3d}: {[tuple(np.round(m/np.pi,2)) for m in mins][:6]}   {bw:.3f}")
check("1c+11 is fully gapped (Delta > 0.5 |t1|) for every t2 scanned in [0.05, 3]: no Majorana nodes, "
      "no Weyl points at the Majorana Fermi level", min(gaps.values()) > 0.5, f"min Delta = {min(gaps.values()):.4f}")
print(f"   t = {time.time()-T0:.1f}s")

# ------------------------------------------------------------------ C2: PSG
print(f"\nC2: projective symmetry group on L = 4 (24 proper rotations about a site, translations)")
G4 = L4.G; L = 4
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = signs[i]
        if round(np.linalg.det(M)) == 1: ROTS.append(M)


def vmap(f):
    return np.array([G4.vid[f(q)] for q in G4.verts])


def rot(R):
    def f(q):
        v, c = q
        return (tuple(int(x) % L for x in R @ np.array(v)), frozenset(tuple(int(x) for x in R @ np.array(d)) for d in c))
    return f


def trans(t):
    def f(q):
        v, c = q
        return (tuple((a + b) % L for a, b in zip(v, t)), c)
    return f


PAIR = {}
for k, (i, j, _, _) in enumerate(G4.edges):
    PAIR.setdefault(frozenset((i, j)), []).append(k)
assert all(len(v) == 1 for v in PAIR.values())


def psg(fmap, u, oriented):
    """Z2 gauge s with h(P i, P j) = s_i s_j h(i, j); for imaginary (oriented) amplitudes the
    image edge's stored orientation enters."""
    P = vmap(fmap)
    rows, rhs = [], []
    for k, (i, j, _, _) in enumerate(G4.edges):
        fk = PAIR[frozenset((P[i], P[j]))][0]
        flip = 0
        if oriented:
            fi, fj = G4.edges[fk][0], G4.edges[fk][1]
            flip = 0 if (fi == P[i] and fj == P[j]) else 1
        rows.append([i, j]); rhs.append(int(u[k]) ^ int(u[fk]) ^ flip)
    s = gf2_solve(rows, rhs, G4.nV)
    return P, s


def power_sign(P, s, m):
    cur = np.arange(len(P)); sign = np.zeros(len(P), np.uint8)
    for _ in range(m):
        sign ^= s[cur]; cur = P[cur]
    assert (cur == np.arange(len(P))).all()
    vals = set(sign.tolist())
    return (-1 if vals.pop() else 1) if len(vals) == 1 else None


def comp(ops):
    perm = np.arange(G4.nV); sign = np.zeros(G4.nV, np.uint8)
    for P, s in reversed(ops):
        sign = sign ^ s[perm]; perm = P[perm]
    return perm, sign


def inv(P, s):
    Pi = np.empty(len(P), int); Pi[P] = np.arange(len(P)); return Pi, s[Pi]


def psg_table(u, oriented):
    out = {}
    for R in ROTS:
        tr = int(np.trace(R)); m = {3: 1, -1: 2, 0: 3, 1: 4}[tr]
        P, s = psg(rot(R), u, oriented)
        if s is None:
            return None
        kind = {1: 'e', 3: 'C3', 4: 'C4'}.get(m)
        if m == 2: kind = 'C2axis' if np.allclose(np.abs(np.diag(R)), 1) else 'C2edge'
        out.setdefault(kind, set()).add(power_sign(P, s, m))
    E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    T = {a: psg(trans(a), u, oriented) for a in E3}
    (Px, sx), (Py, sy) = T[E3[0]], T[E3[1]]
    q = np.arange(G4.nV)
    out['TxTy'] = set(((sx[q] ^ sy[Px[q]]) ^ (sy[q] ^ sx[Py[q]])).tolist())
    if out['TxTy'] != {0}:
        out['fixed'] = 'n/a'
        return out
    shifts = []
    for R in ROTS:
        MR = psg(rot(R), u, oriented)
        sh = np.zeros(3, int)
        for a in E3:
            Ra = tuple(int(x) for x in R @ np.array(a))
            ax = int(np.argmax(np.abs(Ra))); sgn = Ra[ax]
            Ta = T[E3[ax]] if sgn > 0 else inv(*T[E3[ax]])
            perm, sign = comp([MR, T[a], inv(*MR), inv(*Ta)])
            assert (perm == np.arange(G4.nV)).all()
            vals = set(sign.tolist()); assert len(vals) == 1
            sh += vals.pop() * np.abs(np.array(Ra))
        shifts.append(sh % 2)
    out['fixed'] = [k for k in itertools.product(range(4), repeat=3)
                    if all(((R @ np.array(k) + 2 * s - np.array(k)) % 4 == 0).all() for R, s in zip(ROTS, shifts))]
    out['_shifts'] = shifts
    return out


# extend the period-1 gauge of 1c+11 to L = 4 (same descriptors), so L = 4 momenta = Bloch momenta of C1
desc1 = {}
for k, (v, c, disp, c2) in enumerate(L1.G.edesc):
    desc1[(c, disp, c2)] = (k, 0)
    desc1[(c2, tuple(-x for x in disp), c)] = (k, 1)
u4 = np.zeros(L4.nE, np.uint8)
for k4, (v, c, disp, c2) in enumerate(L4.G.edesc):
    k1, rev = desc1[(c, disp, c2)]
    u4[k4] = u1[k1] ^ rev      # imaginary amplitude: reversing the stored orientation flips the sign
ph4 = L4.face_phases(majorana_amp(L4, u4, 1, 1))
tg4 = uniform_targets(L4, *P0, 'maj')
check("period-1 gauge of 1c+11 lifted to L = 4 reproduces the 1c+11 fluxes on every face",
      np.allclose(np.exp(1j * ph4), np.exp(1j * tg4)))
tabM = psg_table(u4, True)
print("   1c+11 (Majorana):", {k: (sorted(v) if isinstance(v, set) else v) for k, v in tabM.items() if k != '_shifts'})
uR = gf2_solve([[e for e, _ in trav] for _, trav, _ in L4.faces],
               [{'square': 1, 'triangle': 0, 'plaquette': 1, 'tube': 1}[k] for k, _, _ in L4.faces], L4.nE)
tabR = psg_table(uR, False)
print("   corner model u-pattern 1011 (real, control):", {k: (sorted(v) if isinstance(v, set) else v) for k, v in tabR.items() if k != '_shifts'})
check("control: corner model 1011 reproduces C6 A4 (C4^4 = -1, commuting translations, fixed momenta (1,3,1),(3,1,3))",
      tabR['C4'] == {-1} and tabR['TxTy'] == {0} and sorted(tabR['fixed']) == [(1, 3, 1), (3, 1, 3)])
check("1c+11 PSG: C4^4 = -1 and the translations commute (two of the three corner-model design targets)",
      tabM is not None and tabM['C4'] == {-1} and tabM['TxTy'] == {0})
print(f"FINDING C2: O-fixed momenta of 1c+11 (units pi/2): {tabM['fixed']}  "
      f"(corner model 1011: {tabR['fixed']}); the third design target (an O-fixed momentum) "
      f"{'FAILS' if tabM['fixed'] in ([], 'n/a') else 'holds'} for the Majorana-selected sector")


def spectral_psg_check(lat1, amp1, shifts, nrand=40):
    """E(R k + pi s_R) = E(k) for every rotation R, at random k (tests the PSG shifts)."""
    dev = 0.0
    ks = rng.uniform(0, 2 * np.pi, (nrand, 3))
    e0 = bands(lat1, amp1, ks)
    for R, sR in zip(ROTS, shifts):
        e1 = bands(lat1, amp1, ks @ R.T + np.pi * sR)
        dev = max(dev, np.max(np.abs(e1 - e0)))
    return dev


uR1 = gf2_solve([[e for e, _ in trav] for _, trav, _ in L1.faces],
                [{'square': 1, 'triangle': 0, 'plaquette': 1, 'tube': 1}[k] for k, _, _ in L1.faces], L1.nE)
devM = spectral_psg_check(L1, majorana_amp(L1, u1, 1, 0.37), tabM['_shifts'])
check("PSG shifts of 1c+11 verified spectrally: E(R k + pi s_R) = E(k) for all 24 rotations, 40 random k "
      "(so the empty fixed set is not a bookkeeping artefact)", devM < 1e-9, f"max dev {devM:.1e}")
# the lift u4 of the period-1 gauge is the same gauge on L = 4, so L1 Bloch momenta = L4 momenta; for the
# real control the L = 4 gauge uR is a different gauge than uR1, so only the Majorana check is meaningful here.
print("   PSG of the other O-invariant Majorana patterns (chiral triangles c+):")
for P in [(sq, 'c+', pl, tu) for sq in (0, 1) for pl in (0, 1) for tu in (0, 1)]:
    uP = ugauge(L4, P)
    t = psg_table(uP, True)
    print(f"     {P[0]}{P[1]}{P[2]}{P[3]}: " + (str({k: (sorted(v) if isinstance(v, set) else v) for k, v in t.items() if k != '_shifts'}) if t else 'no unitary PSG with these gauges'))

# where is the Majorana gap minimum relative to the O-fixed momenta?
if tabM and tabM['fixed'] not in ([], 'n/a'):
    print("   Majorana levels at the O-fixed momenta (period-1 gauge, t1 = 1):")
    for t2 in (0.2, 1.0):
        a = majorana_amp(L1, u1, 1, t2)
        for kf in tabM['fixed']:
            e = np.linalg.eigvalsh(L1.blochH(a, (np.pi / 2 * np.array(kf, float))[None])[0])
            print(f"     t2={t2}: k = (pi/2){kf}: lowest positive levels {np.round(e[e > 0][:4], 5)};  gap Delta = {gaps[t2]:.5f}")
print(f"   t = {time.time()-T0:.1f}s")

# ------------------------------------------------------------------ C3: flux excitations
print(f"\nC3: cost of flipping one gauge link u_e (flux change on its 3 faces), L = 4 torus, 2^3 boundary twists")
for t2 in (0.2, 1.0):
    a0 = majorana_amp(L4, u4, 1, t2)
    E0 = per_site(L4.spectrum(a0, 2), 6) * 64   # twist-averaged total energy of the L = 4 torus
    res = {'onsite': [], 'link': []}
    site0 = [k for k, (v, c, disp, c2) in enumerate(L4.G.edesc) if v == (0, 0, 0)]
    for k in site0:
        uu = u4.copy(); uu[k] ^= 1
        E1 = per_site(L4.spectrum(majorana_amp(L4, uu, 1, t2), 2), 6) * 64
        res['onsite' if L4.onsite[k] else 'link'].append(E1 - E0)
    for kind, v in res.items():
        v = np.array(v)
        print(f"   t2={t2}: {kind:6s} flips ({len(v)} edges): dE in [{v.min():.5f}, {v.max():.5f}]")
    if t2 == 0.2:
        check("every single-link flip costs energy > 0 at t2 = 0.2 and 1 (1c+11 stable against one-edge flux pairs on L = 4)",
              min(min(v) for v in res.values()) > 0, f"min {min(min(v) for v in res.values()):.5f}")
        mn02 = min(min(v) for v in res.values())
    else:
        check("  ... and at t2 = 1", min(min(v) for v in res.values()) > 0, f"min {min(min(v) for v in res.values()):.5f}")
print(f"   t = {time.time()-T0:.1f}s")

# ------------------------------------------------------------------ C4: corner-model family fluxes
print("\nC4: gauge-invariant fluxes of the corner-model family (t1 = -1, u-pattern 1011, chiral lambda on oriented triangles)")
uC = gf2_solve([[e for e, _ in trav] for _, trav, _ in L1.faces],
               [{'square': 1, 'triangle': 0, 'plaquette': 1, 'tube': 1}[k] for k, _, _ in L1.faces], L1.nE)
assert uC is not None   # u-convention pattern 1011 (prod u = -1 on squares, plaquettes, tubes) on L = 1
# oriented triangle hops (outward orientation), each on-site edge in exactly one triangle
tri_or = np.zeros(L1.nE)
for k, trav, chi in L1.faces:
    if k == 'triangle':
        for e, s in trav:
            tri_or[e] += s * chi
assert np.all(np.abs(tri_or[L1.onsite]) == 1) and np.all(tri_or[~L1.onsite] == 0)
okC4 = True
for lam in (0.0, -0.5, -1 / np.sqrt(3), 0.3):
    t1, t2 = -1.0, 0.2
    uu = (-1.0) ** uC
    amp = np.where(L1.onsite, -t1 * uu + 1j * lam * uu * tri_or, -t2 * uu)
    ph = L1.face_phases(amp)
    summ = {}
    for t_, k in enumerate(TYPES):
        sel = ph[L1.ftype == t_]
        if k == 'triangle':
            chis = np.array([chi for kk, _, chi in L1.faces if kk == 'triangle'])
            sel = sel * chis
        summ[k] = np.unique(np.round(np.mod(sel, 2 * np.pi) / np.pi, 4)).tolist()
    a_ = np.arctan(lam)
    m = lambda x: sorted({round(float(np.mod(v, 2 * np.pi) / np.pi), 4) for v in x})
    # squares and tubes are listed with arbitrary orientation, so both signs of the shift may appear
    okC4 &= set(summ['square']) <= set(m([np.pi - 4 * a_, np.pi + 4 * a_]))
    okC4 &= set(summ['tube']) <= set(m([np.pi - 2 * a_, np.pi + 2 * a_]))
    okC4 &= summ['triangle'] == m([np.pi + 3 * a_]) and summ['plaquette'] == [1.0]
    print(f"   lambda = {lam:+.4f}: flux/pi (triangles outward): {summ}")
check("corner-model family: square flux pi -+ 4 arctan(lambda), tube pi -+ 2 arctan(lambda) (sign = orientation), "
      "triangle (outward) pi + 3 arctan(lambda), plaquette pi; so square = pi forces lambda = 0 and triangle = pi: "
      "no member is gauge-equivalent to 1c+11", okC4)

# ------------------------------------------------------------------ C5: parton with chemical potential
print(f"\nC5: complex parton with imaginary hopping (H_M2 + mu N, exactly solvable) at filling nu: uniform winners; t = {time.time()-T0:.1f}s")
PATS = [(sq, tr, pl, tu) for sq in (0, 1) for tr in ('c+', 's+') for pl in (0, 1) for tu in (0, 1)]
g2 = {P: ugauge(L2, P) for P in PATS}
lab = lambda P: f"{P[0]}{P[1]}{P[2]}{P[3]}"
for t2 in (0.2, 1.0):
    ev = {P: L2.spectrum(majorana_amp(L2, g2[P], 1, t2), 6) for P in PATS}
    line = []
    for nu in range(1, 12):
        E = {P: per_site(ev[P], nu) for P in PATS}
        o = sorted(PATS, key=lambda P: E[P])
        line.append(f"nu={nu}: {lab(o[0])} (1c+11 rank {o.index(P0)+1})")
    print(f"   t2={t2}: " + "; ".join(line))
    if t2 == 0.2:
        E1 = {P: per_site(ev[P], 1) for P in PATS}
        o1 = sorted(PATS, key=lambda P: E1[P])
        print(f"   t2=0.2, nu=1: winner {lab(o1[0])} E = {E1[o1[0]]:.4f}; 1c+11 E = {E1[P0]:.4f} (rank {o1.index(P0)+1}/16)")

print(f"\nelapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
