"""A31 c2: sign patterns, role patterns and cells on the 4x4x4 torus (exact integer arithmetic).

(1) Bond orbits under the field's role-pattern stabilizer G_s = 2Z^3 x| O(about vertex-role site 0).
    Every G_s-invariant sign pattern: fluxes through all plaquettes.
(2) Kogut-Susskind (KS) signs: flux pi everywhere; site sums; gauges with constant site sum.
(3) Largest exact stabilizer of a pi-flux sign pattern among the 256 period-2 gauge images of KS.
(4) G_s-invariant bond modulations: any component with momentum pi along the bond axis?
(5) Joint stabilizer (inside G_s) of the role pattern and a 2x2x2 block decomposition (A26 cells).
(6) A26's in-cell face-diagonal pairs under a site-centred half turn.
"""
import signal, itertools, numpy as np
signal.alarm(55)
L = 4
sites = [(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
sidx = {s:i for i,s in enumerate(sites)}
E = [(1,0,0),(0,1,0),(0,0,1)]
def add(a,b): return tuple((a[i]+b[i]) % L for i in range(3))
bonds = [(s, a) for s in sites for a in range(3)]          # bond from s to s+e_a
bidx = {b:i for i,b in enumerate(bonds)}
def bond_of(u, v):
    for a in range(3):
        if add(u, E[a]) == v: return bidx[(u,a)]
        if add(v, E[a]) == u: return bidx[(v,a)]
    raise ValueError
plaq = []
for s in sites:
    for a, b in [(0,1),(1,2),(0,2)]:
        p0, p1, p2, p3 = s, add(s,E[a]), add(add(s,E[a]),E[b]), add(s,E[b])
        plaq.append([bond_of(p0,p1), bond_of(p1,p2), bond_of(p2,p3), bond_of(p3,p0)])
plaq = np.array(plaq)
def fluxes(eta): return np.prod(eta[plaq], axis=1)
# proper rotations: signed permutation matrices with det +1
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1], repeat=3):
        M = np.zeros((3,3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: rots.append(M)
assert len(rots) == 24
def act(M, t, s):   # x -> M x + t  (mod L), rotation about the origin site 0
    v = M @ np.array(s) + np.array(t); return tuple(int(c) % L for c in v)
def bond_image(M, t, b):
    s, a = b; u = act(M,t,s); v = act(M,t,add(s,E[a])); return bond_of(u, v)
# (1) orbits under G_s = translations by 2Z^3 (mod 4) x| O about site 0
G_s = [(M, t) for M in rots for t in itertools.product([0,2], repeat=3)]
orb = -np.ones(len(bonds), int); k = 0
for i in range(len(bonds)):
    if orb[i] >= 0: continue
    stack = [i]; orb[i] = k
    while stack:
        j = stack.pop()
        for M,t in G_s:
            jj = bond_image(M,t,bonds[j])
            if orb[jj] < 0: orb[jj] = k; stack.append(jj)
    k += 1
print(f"(1) bond orbits under G_s (2Z^3 x| O about a vertex-role site): {k}")
allflux = set()
for signs in itertools.product([1,-1], repeat=k):
    eta = np.array([signs[o] for o in orb]); allflux |= set(fluxes(eta).tolist())
print(f"    plaquette products over all {2**k} G_s-invariant sign patterns: {sorted(allflux)} (+1 only => no pi flux)")
# (4) longitudinal-pi component of G_s-invariant bond modulations: along x-bonds, does the orbit
#     label depend on the bond's start coordinate parity along x (with transverse coords fixed)?
dep = 0
for a in range(3):
    for s in sites:
        s2 = list(s); s2[a] = (s2[a]+1) % L
        if orb[bidx[(s,a)]] != orb[bidx[(tuple(s2),a)]]: dep += 1
print(f"(4) bonds whose G_s-orbit changes under a unit shift along their own axis: {dep} (0 => no dimerization component)")
# (2) KS signs
def ks(s, a):
    x,y,z = s
    return [1, (-1)**x, (-1)**(x+y)][a]
eta_ks = np.array([ks(s,a) for s,a in bonds])
print(f"(2) KS fluxes: {sorted(set(fluxes(eta_ks).tolist()))} (all -1 => pi everywhere)")
U = np.array([sidx[s] for s,a in bonds]); V = np.array([sidx[add(s,E[a])] for s,a in bonds])
def site_sums(eta):
    ss = np.zeros(len(sites), int); np.add.at(ss, U, eta); np.add.at(ss, V, eta); return ss
print(f"    KS site sums: {sorted(set(site_sums(eta_ks).tolist()))}")
def gauge(eta, g): return eta * g[U] * g[V]
# period-2 gauges
p2 = []
for bits in itertools.product([1,-1], repeat=8):
    g = np.array([bits[(x%2)*4+(y%2)*2+(z%2)] for x,y,z in sites]); p2.append(gauge(eta_ks, g))
print(f"    period-2 gauges: site-sum sets found = {sorted(set(tuple(sorted(set(site_sums(e).tolist()))) for e in p2))}")
# annealing over all 2^64 gauges for constant site sum s0 in {2, 0}
rng = np.random.default_rng(7)
nbr = [[] for _ in sites]
for i,(u,v) in enumerate(zip(U,V)): nbr[u].append((v,i)); nbr[v].append((u,i))
def anneal(s0, sweeps=1500):
    g = rng.choice([1,-1], size=len(sites))
    def cost(g): return np.sum(np.abs(site_sums(gauge(eta_ks,g)) - s0))
    c = cost(g); T = 2.0
    for sw in range(sweeps):
        for _ in range(len(sites)):
            i = rng.integers(len(sites)); g[i] *= -1; c2 = cost(g)
            if c2 <= c or rng.random() < np.exp(-(c2-c)/T): c = c2
            else: g[i] *= -1
        T = max(0.02, T*0.995)
        if c == 0: break
    return c, g
for s0 in (2, 0):
    best = min(anneal(s0, 300)[0] for _ in range(4))
    print(f"    annealed gauges on 4^3: best total |site sum - {s0}| = {best} (0 => a pi-flux sign pattern with constant site sum {s0} exists)")
# (3) largest exact stabilizer among period-2 gauge images of KS (192 cosets = 24 rotations x 8 offsets)
cos = [(M, t) for M in rots for t in itertools.product([0,1], repeat=3)]
perms = [np.array([bond_image(M,t,b) for b in bonds]) for M,t in cos]
best = 0; bestset = None
seen = set()
for e in p2:
    key = tuple(e)
    if key in seen: continue
    seen.add(key)
    cnt = 0
    for pm in perms:
        img = np.empty_like(e); img[pm] = e
        if np.array_equal(img, e): cnt += 1
    if cnt > best: best = cnt
print(f"(3) distinct period-2 pi-flux sign patterns: {len(seen)}; largest exact stabilizer (cosets of 2Z^3): {best} of 192 "
      f"(the field's role pattern keeps 24 of them: all rotations about a vertex-role site)")
# (5) joint stabilizer of role pattern s=0 and block decompositions with corner offset c0
print("(5) elements of G_s/2Z^3 (24 rotations about vertex 0) that also preserve a 2x2x2 block decomposition:")
for c0 in itertools.product([0,1], repeat=3):
    def block(s): return tuple(((s[i]-c0[i]) % L)//2 for i in range(3))
    cnt = 0
    for M in rots:
        # preserved iff the image of each block is a block: compare partitions
        part = {}
        ok = True
        for s in sites:
            bimg = block(act(M,(0,0,0),s))
            part.setdefault(block(s), set()).add(bimg)
        if all(len(v)==1 for v in part.values()) and len(set(next(iter(v)) for v in part.values()))==len(part): cnt += 1
    print(f"    block corner offset c0={c0}: {cnt} of 24 rotations")
# (6) in-cell face-diagonal pairs (x,y plane) with cells anchored at even coordinates, under the half turn about z through site 0
def incell(u, v):   # u -> v = u + e_x + e_y, in-cell iff u has even x and y
    return (u[0] % 2 == 0) and (u[1] % 2 == 0)
M = np.diag([-1,-1,1]); moved = 0; tot = 0
for u in sites:
    v = add(add(u,E[0]),E[1])
    if not incell(u,v): continue
    tot += 1
    ui, vi = act(M,(0,0,0),u), act(M,(0,0,0),v)
    lo = vi if (ui[0]-vi[0]) % L == 1 else ui   # lower-left end of the image pair
    if not ((lo[0] % 2 == 0) and (lo[1] % 2 == 0)): moved += 1
print(f"(6) in-cell xy face-diagonal pairs mapped to out-of-cell pairs by the site-centred half turn: {moved} of {tot}")
