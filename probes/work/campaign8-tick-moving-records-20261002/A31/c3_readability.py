"""A31 c3: is the Kogut-Susskind (pi-flux) sign pattern readable from records under a smooth change?

Supplied toy (Option R shape): calm emptiness |0...0> (axis z), excitations |1>, records hold Z-basis
content and are compressed (their bits are frozen; the change acts on the rest), the change is a fixed
smooth generator, one tick lets a record trade places (swap step SW, blind weight), records form at the
end in the Z basis (all unrecorded sites) or in the X basis (two sites).

Laws compared (number-conserving; one qubit per site; bond signs eta):
  XXZ  : sum_b [eta_b (XX+YY) + ZZ]          (sign on the hop part only; A10's Z.G.Z form)
  SHEIS: sum_b  eta_b (XX+YY+ZZ)             (sign on the whole spin-rotation-invariant exchange)
  HEIS : sum_b (XX+YY+ZZ)                    (no pattern; control)
A lattice symmetry S maps the law L_eta to L_{S.eta}. "No site is privileged" for record statistics
means P_{L_eta}(S h | S S0) = P_{L_eta}(h | S0), i.e. L_eta and L_{S^-1.eta} give the same record
statistics on the same S0. We print TV between those two laws for each experiment.
"""
import signal, itertools, numpy as np
signal.alarm(55)

def build(sites, bonds_axis):
    idx = {s:i for i,s in enumerate(sites)}
    return idx

class Lattice:
    def __init__(self, sites, bonds, sym):
        self.sites = sites; self.N = len(sites); self.idx = {s:i for i,s in enumerate(sites)}
        self.bonds = bonds            # list of (i, j) site indices (may repeat a pair on a 2-torus)
        self.sym = sym                # dict site index -> site index (a lattice symmetry)
        self.nbrs = [[] for _ in range(self.N)]
        for k,(i,j) in enumerate(bonds):
            self.nbrs[i].append((j,k)); self.nbrs[j].append((i,k))
    def pullback(self, eta):
        # (S^-1 . eta)(b) = eta(S b): the pattern whose push-forward by S is eta
        bmap = {}
        for k,(i,j) in enumerate(self.bonds): bmap.setdefault(frozenset((i,j)), []).append(k)
        out = np.zeros(len(eta))
        used = {}
        for k,(i,j) in enumerate(self.bonds):
            key = frozenset((self.sym[i], self.sym[j]))
            lst = bmap[key]; n = used.get((k,), 0)
            # for doubled bonds on a 2-torus the two copies carry equal signs in our patterns
            out[k] = eta[lst[0]]
        return out
    def plaquette_check(self, eta, plaqs):
        return [np.prod([eta[b] for b in p]) for p in plaqs]

def sector(N, n):
    return [b for b in range(1 << N) if bin(b).count('1') == n]

def hamiltonian(lat, eta, law, basis):
    pos = {b:i for i,b in enumerate(basis)}; D = len(basis)
    H = np.zeros((D, D))
    for k,(i,j) in enumerate(lat.bonds):
        e = eta[k]
        for b in basis:
            bi, bj = (b >> i) & 1, (b >> j) & 1
            zz = 1.0 if bi == bj else -1.0
            if law == 'XXZ': H[pos[b], pos[b]] += zz
            else:            H[pos[b], pos[b]] += e * zz
            if bi != bj:
                b2 = b ^ (1 << i) ^ (1 << j)
                H[pos[b2], pos[b]] += 2.0 * e
    return H

def evolve(H, psi, t):
    w, V = np.linalg.eigh(H); return V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))

def compressed(lat, eta, law, basis, rec):   # rec: dict site -> content bit
    keep = [k for k,b in enumerate(basis) if all(((b >> s) & 1) == c for s,c in rec.items())]
    H = hamiltonian(lat, eta, law, basis)
    return keep, H[np.ix_(keep, keep)]

def run(lat, eta, law, n, S0, rec=None, t1=0.9, sw=None, t2=0.8, c=0.9, readout='Z', xpair=None):
    """S0: dict basis-bitstring -> amplitude. Returns dict outcome -> probability."""
    basis = sector(lat.N, n); pos = {b:i for i,b in enumerate(basis)}
    psi = np.zeros(len(basis), complex)
    for b, a in S0.items(): psi[pos[b]] = a
    psi /= np.linalg.norm(psi)
    rec = dict(rec or {})
    keep, H = compressed(lat, eta, law, basis, rec)
    branches = [((), psi)]
    # first smooth stretch
    sub = evolve(H, psi[keep], t1); psi = np.zeros_like(psi); psi[keep] = sub
    branches = [('none', psi, rec)]
    if sw is not None:
        (r, cont), = rec.items()
        z = max(len(set(j for j,_ in lat.nbrs[q])) for q in range(lat.N))
        empty = sorted(set(j for j,_ in lat.nbrs[r]) - set(rec))
        new = []
        amp_stay = np.sqrt(max(0.0, 1 - c * len(empty) / z))
        new.append(('stay', amp_stay * psi, rec))
        for y in empty:
            k_ry = [k for j,k in lat.nbrs[r] if j == y][0]
            out = np.zeros_like(psi)
            for b, a in zip(basis, psi):
                if a == 0: continue
                by = (b >> y) & 1
                ph = (-1.0)**by if (sw == 'signed' and eta[k_ry] < 0) else 1.0
                br = (b >> r) & 1
                b2 = b
                if br != by: b2 = b ^ (1 << r) ^ (1 << y)
                out[pos[b2]] += np.sqrt(c / z) * ph * a
            new.append((f'to{y}', out, {y: cont}))
        branches = new
    probs = {}
    for lab, ps, rc in branches:
        keep, H = compressed(lat, eta, law, basis, rc)
        sub = evolve(H, ps[keep], t2); fin = np.zeros_like(ps); fin[keep] = sub
        if readout == 'Z':
            for b, a in zip(basis, fin):
                p = abs(a)**2
                if p > 1e-30: probs[(lab, b)] = probs.get((lab, b), 0) + p
        else:
            s, t = xpair
            w = float(np.vdot(fin, fin).real)
            xx = 0.0
            for b, a in zip(basis, fin):
                if ((b >> s) & 1) != ((b >> t) & 1):
                    b2 = b ^ (1 << s) ^ (1 << t); xx += (np.conj(fin[pos[b2]]) * a).real
            for es, et in itertools.product([1,-1], repeat=2):
                probs[(lab, es, et)] = (w + es*et*xx) / 4
    return probs

def tv(p, q):
    keys = set(p) | set(q); return 0.5 * sum(abs(p.get(k,0) - q.get(k,0)) for k in keys)

def bits(lat, ones): return sum(1 << lat.idx[s] for s in ones)

def experiments(name, lat, eta, a, b, r, xpair, rng):
    eta2 = lat.pullback(eta)
    print(f"--- {name}: pattern differs from its pull-back on {int(np.sum(eta != eta2))} of {len(eta)} bonds")
    for law in ('XXZ', 'SHEIS', 'HEIS'):
        e1, e2 = (eta, eta2) if law != 'HEIS' else (np.ones(len(eta)), np.ones(len(eta)))
        res = []
        S1 = {bits(lat,[a]): 1.0}
        res.append(('E1 one excitation, Z', tv(run(lat,e1,law,1,S1), run(lat,e2,law,1,S1))))
        S2 = {bits(lat,[a,b]): 1.0}
        res.append(('E2 two excitations, Z', tv(run(lat,e1,law,2,S2), run(lat,e2,law,2,S2))))
        # record at r with content 0, one excitation at a, blind swap step
        S3 = {bits(lat,[a]): 1.0}
        res.append(('E3 record(0) + blind SW, Z', tv(run(lat,e1,law,1,S3,rec={lat.idx[r]:0},sw='blind'),
                                                  run(lat,e2,law,1,S3,rec={lat.idx[r]:0},sw='blind'))))
        if law == 'XXZ':
            res.append(('E3s record(0) + signed SW, Z', tv(run(lat,e1,law,1,S3,rec={lat.idx[r]:0},sw='signed'),
                                                          run(lat,e2,law,1,S3,rec={lat.idx[r]:0},sw='signed'))))
        S3b = {bits(lat,[a, r]): 1.0}
        res.append(('E3b record(1) + blind SW, Z', tv(run(lat,e1,law,2,S3b,rec={lat.idx[r]:1},sw='blind'),
                                                   run(lat,e2,law,2,S3b,rec={lat.idx[r]:1},sw='blind'))))
        res.append(('E3c static record(0), no step, Z', tv(run(lat,e1,law,1,S3,rec={lat.idx[r]:0}),
                                                          run(lat,e2,law,1,S3,rec={lat.idx[r]:0}))))
        xp = (lat.idx[xpair[0]], lat.idx[xpair[1]])
        res.append(('E4 one excitation, X on two sites', tv(run(lat,e1,law,1,S1,readout='X',xpair=xp),
                                                          run(lat,e2,law,1,S1,readout='X',xpair=xp))))
        amps = rng.normal(size=lat.N) + 1j*rng.normal(size=lat.N)
        S5 = {1 << i: amps[i] for i in range(lat.N)}
        res.append(('E5 coherent start (not a record configuration), Z', tv(run(lat,e1,law,1,S5), run(lat,e2,law,1,S5))))
        print(f"  {law:5s} " + "; ".join(f"{k}: {v:.1e}" for k,v in res))

rng = np.random.default_rng(3)
# (A) 2D 3x3 open patch, quarter turn about the centre site
sitesA = [(x,y) for x in range(3) for y in range(3)]
idxA = {s:i for i,s in enumerate(sitesA)}
bondsA = []; etaA = []
for (x,y) in sitesA:
    if x < 2: bondsA.append((idxA[(x,y)], idxA[(x+1,y)])); etaA.append(1.0)
    if y < 2: bondsA.append((idxA[(x,y)], idxA[(x,y+1)])); etaA.append((-1.0)**x)
symA = {idxA[(x,y)]: idxA[(2-y, x)] for (x,y) in sitesA}
latA = Lattice(sitesA, bondsA, symA)
plA = []
for x in range(2):
    for y in range(2):
        def bk(u,v): return [k for k,(i,j) in enumerate(bondsA) if {i,j} == {idxA[u], idxA[v]}][0]
        plA.append([bk((x,y),(x+1,y)), bk((x+1,y),(x+1,y+1)), bk((x,y+1),(x+1,y+1)), bk((x,y),(x,y+1))])
etaA = np.array(etaA)
print("(A) 3x3 patch fluxes:", latA.plaquette_check(etaA, plA), "pulled-back:", latA.plaquette_check(latA.pullback(etaA), plA))
experiments("(A) 2D 3x3 patch, KS signs, quarter turn about the centre site", latA, etaA, a=(0,0), b=(2,1), r=(1,1), xpair=((0,0),(1,0)), rng=rng)

# (B) 2D 4x2 torus, unit translation along x; KS gauge and a constant-site-sum (staggered dimer) gauge
Lx, Ly = 4, 2
sitesB = [(x,y) for x in range(Lx) for y in range(Ly)]
idxB = {s:i for i,s in enumerate(sitesB)}
bondsB = []; ks = []; dim = []
for (x,y) in sitesB:
    bondsB.append((idxB[(x,y)], idxB[((x+1)%Lx, y)])); ks.append(1.0); dim.append(-1.0 if (x-y) % 2 == 0 else 1.0)
    bondsB.append((idxB[(x,y)], idxB[(x,(y+1)%Ly)])); ks.append((-1.0)**x); dim.append(1.0)
symB = {idxB[(x,y)]: idxB[((x+1)%Lx, y)] for (x,y) in sitesB}
latB = Lattice(sitesB, bondsB, symB)
def site_sums(lat, eta):
    s = np.zeros(lat.N)
    for k,(i,j) in enumerate(lat.bonds): s[i] += eta[k]; s[j] += eta[k]
    return s
print("(B) 4x2 torus site sums: KS", sorted(set(site_sums(latB, np.array(ks)))), " dimer", sorted(set(site_sums(latB, np.array(dim)))))
experiments("(B1) 2D 4x2 torus, KS gauge, unit translation", latB, np.array(ks), a=(0,1), b=(2,0), r=(1,0), xpair=((2,0),(3,0)), rng=rng)
experiments("(B2) 2D 4x2 torus, constant-site-sum gauge, unit translation", latB, np.array(dim), a=(0,1), b=(2,0), r=(1,0), xpair=((2,0),(3,0)), rng=rng)

# (C) 3D 2x2x3 open box, quarter turn about the box's long axis
sitesC = [(x,y,z) for x in range(2) for y in range(2) for z in range(3)]
idxC = {s:i for i,s in enumerate(sitesC)}
bondsC = []; etaC = []
for (x,y,z) in sitesC:
    if x < 1: bondsC.append((idxC[(x,y,z)], idxC[(x+1,y,z)])); etaC.append(1.0)
    if y < 1: bondsC.append((idxC[(x,y,z)], idxC[(x,y+1,z)])); etaC.append((-1.0)**x)
    if z < 2: bondsC.append((idxC[(x,y,z)], idxC[(x,y,z+1)])); etaC.append((-1.0)**(x+y))
symC = {idxC[(x,y,z)]: idxC[(1-y, x, z)] for (x,y,z) in sitesC}
latC = Lattice(sitesC, bondsC, symC)
experiments("(C) 3D 2x2x3 box, KS signs, quarter turn about the long axis", latC, np.array(etaC), a=(0,0,0), b=(1,1,2), r=(0,1,1), xpair=((0,0,0),(1,0,0)), rng=rng)
