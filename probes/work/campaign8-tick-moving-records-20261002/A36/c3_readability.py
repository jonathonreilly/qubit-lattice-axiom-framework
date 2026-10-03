"""
A36 check C3: how readable is a tick timed by the surrounding records?  (record-tick shape, Option R)

Supplied toy (not framework content):
- ring of L = 10 sites, hard-core excitations (two of them), hopping H = -J sum(b+_x b_y + h.c.)
  on unrecorded sites only (compression; for hopping the compressed record fields vanish);
- a permanent record at site 0 with content |0> (prepared); records formed later lock |1>
  (weight F = c|1><1| at a gate-open site; gate = at least one recorded neighbour, A28);
- once a record forms, the excitation it locks is frozen and its neighbours' classes change;
- class of a gate-open site = whether any recorded neighbour holds |1> (toy class; the toy weight
  already singles out the |1> direction).
Schedules (c = chance per firing; gamma = 0.5, J = 1, T = 8):
  G      : every gate-open site fires at n*tau, c = gamma*tau;
  PH     : sites next to the |0> record only fire at n*tau; sites next to a |1> record at (n+1/2)tau;
           c = gamma*tau  (record-set PHASES);
  PER    : first class at n*tau with c = gamma*tau; second class at 2n*tau with c = 2*gamma*tau
           (record-set PERIODS, chance scaled with the interval: P1);
  PERfix : second class at 2n*tau with c = gamma*tau (fixed chance per firing: P1');
  C      : continuous-time limit, rate gamma at every gate-open site;
  Cr     : continuous-time limit, rate gamma (first class) and gamma/2 (second class).
Readout: which sites hold records at time T (no time stamps: records carry none).
Expected: TV(G,PH), TV(G,C), TV(PER,C), TV(PERfix,Cr) all O(tau); TV(PERfix,C) order 1.
"""
import signal, itertools, time
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import expm_multiply
signal.alarm(55)
t0 = time.time()
L, J, gamma, T = 10, 1.0, 0.5, 8.0
NEX = 2

def ring_nbrs(x):
    return [(x - 1) % L, (x + 1) % L]

class Config:
    def __init__(self, recs):
        self.recs = dict(recs)                       # site -> content (0 or 1)
        self.free = [x for x in range(L) if x not in self.recs]
        self.nex = NEX - sum(1 for v in self.recs.values() if v == 1)
        self.basis = list(itertools.combinations(self.free, self.nex))
        self.index = {b: i for i, b in enumerate(self.basis)}
        d = len(self.basis)
        H = np.zeros((d, d))
        for i, b in enumerate(self.basis):
            occ = set(b)
            for x in b:
                for y in ring_nbrs(x):
                    if y in self.recs or y in occ:
                        continue
                    nb = tuple(sorted((occ - {x}) | {y}))
                    H[self.index[nb], i] += -J
        self.H = H
        self.E, self.V = np.linalg.eigh(H)
        self.ucache = {}
    def U(self, dt):
        key = round(dt, 12)
        if key not in self.ucache:
            self.ucache[key] = self.V @ np.diag(np.exp(-1j * self.E * dt)) @ self.V.conj().T
        return self.ucache[key]
    def gate_open(self):
        out = []
        for x in self.free:
            nb = [self.recs[y] for y in ring_nbrs(x) if y in self.recs]
            if nb:
                out.append((x, 1 if 1 in nb else 0))   # (site, class)
        return out
    def n_op(self, x):
        return np.diag([1.0 if x in b else 0.0 for b in self.basis])

CONF = {}
def conf(recs):
    key = tuple(sorted(recs.items()))
    if key not in CONF:
        CONF[key] = Config(recs)
    return CONF[key]

def form_map(cfrom, x):
    """Map from cfrom's space to (cfrom + record 1 at x)'s space, after projecting n_x = 1."""
    recs = dict(cfrom.recs); recs[x] = 1
    cto = conf(recs)
    A = np.zeros((len(cto.basis), len(cfrom.basis)))
    for i, b in enumerate(cfrom.basis):
        if x in b:
            nb = tuple(sorted(set(b) - {x}))
            A[cto.index[nb], i] = 1.0
    return cto, A

start = conf({0: 0})
psi0 = np.zeros(len(start.basis), complex)
psi0[start.index[(3, 6)]] = 1.0
rho0 = np.outer(psi0, psi0.conj())

def ticked(schedule, tau):
    """Return distribution over final record sets for the ticked process."""
    # build the list of instants with, for each, a function (cls) -> (fires?, chance)
    events = []
    n = 0
    while True:
        t = n * tau
        if t > T - 1e-9:
            break
        if schedule == 'G':
            events.append((t, {0: gamma * tau, 1: gamma * tau}))
        elif schedule == 'PH':
            events.append((t, {0: gamma * tau}))
            if t + tau / 2 < T - 1e-9:
                events.append((t + tau / 2, {1: gamma * tau}))
        elif schedule in ('PER', 'PERfix'):
            fire = {0: gamma * tau}
            if n % 2 == 0:
                fire[1] = 2 * gamma * tau if schedule == 'PER' else gamma * tau
            events.append((t, fire))
        n += 1
    events.sort(key=lambda e: e[0])
    state = {tuple(sorted(start.recs.items())): rho0.copy()}
    tnow = 0.0
    for (t, fire) in events:
        dt = t - tnow
        new = {}
        for key, r in state.items():
            cf = CONF[key]
            if dt > 0:
                U = cf.U(dt)
                r = U @ r @ U.conj().T
            firing = [(x, fire[cl]) for (x, cl) in cf.gate_open() if cl in fire]
            parts = [(cf, r)]
            for (x, c) in firing:
                nxt = []
                for (cc, rr) in parts:
                    if cc.nex == 0:          # nothing left to record (weight c|1><1| vanishes)
                        nxt.append((cc, rr))
                        continue
                    nx = cc.n_op(x)
                    Kn = np.eye(len(cc.basis)) - nx + np.sqrt(1 - c) * nx
                    nxt.append((cc, Kn @ rr @ Kn.conj().T))
                    cto, A = form_map(cc, x)
                    Kf = np.sqrt(c) * A
                    nxt.append((cto, Kf @ rr @ Kf.conj().T))
                parts = nxt
            for (cc, rr) in parts:
                k2 = tuple(sorted(cc.recs.items()))
                new[k2] = new.get(k2, 0) + rr
        state = new
        tnow = t
    dist = {}
    for key, r in state.items():
        cf = CONF[key]
        if tnow < T:
            U = cf.U(T - tnow)
            r = U @ r @ U.conj().T
        s = frozenset(x for x, v in cf.recs.items() if v == 1)
        dist[s] = dist.get(s, 0) + np.trace(r).real
    return dist

def continuum(rate):
    """rate: dict class -> gamma. Exact integration of the classical-quantum master equation."""
    # enumerate reachable configurations
    keys = [tuple(sorted(start.recs.items()))]
    i = 0
    while i < len(keys):
        cf = CONF[keys[i]]
        if cf.nex > 0:
            for (x, cl) in cf.gate_open():
                cto, _ = form_map(cf, x)
                k2 = tuple(sorted(cto.recs.items()))
                if k2 not in keys:
                    keys.append(k2)
        i += 1
    offs, tot = {}, 0
    for k in keys:
        d = len(CONF[k].basis)
        offs[k] = (tot, d)
        tot += d * d
    G = lil_matrix((tot, tot), dtype=complex)
    for k in keys:
        cf = CONF[k]; o, d = offs[k]
        Id = np.eye(d)
        Gam = np.zeros((d, d))
        for (x, cl) in cf.gate_open():
            if cf.nex == 0:
                continue
            g = rate[cl]
            Gam += g * cf.n_op(x)
            cto, A = form_map(cf, x)
            k2 = tuple(sorted(cto.recs.items())); o2, d2 = offs[k2]
            # vec(A rho A^T) = (A kron A) vec(rho), column-stacking, A real
            G[o2:o2 + d2 * d2, o:o + d * d] += g * np.kron(A, A)
        Heff = cf.H - 0.5j * Gam
        # d rho = -i Heff rho + i rho Heff^dag ; vec(X rho) = (I kron X) vec, vec(rho Y) = (Y^T kron I) vec
        G[o:o + d * d, o:o + d * d] += -1j * np.kron(Id, Heff) + 1j * np.kron(Heff.conj(), Id)
    v0 = np.zeros(tot, complex)
    o, d = offs[keys[0]]
    v0[o:o + d * d] = rho0.reshape(-1, order='F')
    vT = expm_multiply((G * T).tocsr(), v0)
    dist = {}
    for k in keys:
        cf = CONF[k]; o, d = offs[k]
        r = vT[o:o + d * d].reshape((d, d), order='F')
        s = frozenset(x for x, v in cf.recs.items() if v == 1)
        dist[s] = dist.get(s, 0) + np.trace(r).real
    return dist

def tv(P, Q):
    ks = set(P) | set(Q)
    return 0.5 * sum(abs(P.get(k, 0) - Q.get(k, 0)) for k in ks)

Pc = continuum({0: gamma, 1: gamma})
Pcr = continuum({0: gamma, 1: gamma / 2})
print("C3. Ring L=10, permanent |0> record at 0, two excitations starting at sites 3 and 6; J=1, gamma=0.5, T=8.")
print("    continuum (rate gamma everywhere):   ", {tuple(sorted(k)): round(v, 5) for k, v in sorted(Pc.items(), key=lambda kv: -kv[1])[:6]},
      " sum", round(sum(Pc.values()), 12))
print("    continuum (gamma, gamma/2 by class):", {tuple(sorted(k)): round(v, 5) for k, v in sorted(Pcr.items(), key=lambda kv: -kv[1])[:6]},
      " sum", round(sum(Pcr.values()), 12))
print(f"    TV(C, Cr) = {tv(Pc, Pcr):.4f}  (a record-dependent RATE is readable at order 1)")
print("\n    tau     TV(G,PH)   /tau     TV(G,C)    /tau     TV(PER,C)  /tau     TV(PERfix,Cr) /tau     TV(PERfix,C)")
for tau in (0.4, 0.2, 0.1, 0.05, 0.025):
    Pg = ticked('G', tau); Pph = ticked('PH', tau); Pper = ticked('PER', tau); Pfix = ticked('PERfix', tau)
    a, b, c_, d, e = tv(Pg, Pph), tv(Pg, Pc), tv(Pper, Pc), tv(Pfix, Pcr), tv(Pfix, Pc)
    print(f"    {tau:<7} {a:.3e} {a/tau:.4f}   {b:.3e} {b/tau:.4f}   {c_:.3e} {c_/tau:.4f}   {d:.3e} {d/tau:.4f}      {e:.4f}"
          f"    (sum-1: {abs(sum(Pg.values())-1):.0e})")
print(f"    [elapsed {time.time()-t0:.1f}s]")

print("\nC3b. Order-1 chances per firing (c = 0.5 and 1) at tau = 0.5: nothing small suppresses TV(G,PH)")
for c_fix in (0.5, 1.0):
    gsave = gamma
    gamma = c_fix / 0.5
    Pg = ticked('G', 0.5); Pph = ticked('PH', 0.5)
    gamma = gsave
    print(f"    c = {c_fix}: TV(G, PH) = {tv(Pg, Pph):.4f}")
print(f"    [elapsed {time.time()-t0:.1f}s]")

print("\nC3c. Separate 'order c' from 'order tau*frequency': fixed tau = 0.1, vary gamma (c = gamma*tau).")
print("     E[#] = expected number of records formed by T; per event = TV(G,PH)/E[#].")
print("    gamma    c        TV(G,PH)    TV/c       E[#]     per event   per event/tau")
for g_ in (1.0, 0.5, 0.25, 0.125, 0.0625):
    gamma = g_
    Pg = ticked('G', 0.1); Pph = ticked('PH', 0.1)
    d = tv(Pg, Pph)
    En = sum(len(k) * v for k, v in Pg.items())
    print(f"    {g_:<8} {g_*0.1:<8.4g} {d:.3e}   {d/(g_*0.1):.4f}    {En:.4f}   {d/En:.3e}   {d/En/0.1:.4f}")
gamma = 0.5
print(f"    [elapsed {time.time()-t0:.1f}s]")
