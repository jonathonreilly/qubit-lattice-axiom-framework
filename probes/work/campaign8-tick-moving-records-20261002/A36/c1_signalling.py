"""
A36 check C1: a tick timed by records does not signal; a tick timed by the possibilities does.

Supplied toy (not framework content), in the record-tick shape (Option R):
- qubits (b, y, x, z); b is distant (no coupling), y-x-z is a chain.
- two permanent classical records w_y (next to y) and w_x (next to x), content |0>, so y and x
  are gate-open from the start; z is gate-open only once x holds a record (A28 gating).
- smooth change between instants: H = J(SWAP_yx + SWAP_xz) + J(|0><0|_y + |0><0|_x)
  (the last two terms are the compressed fields of w_y, w_x), compressed onto every dynamic
  record (Q = |1><1| on a recorded site), i.e. H_R = Q_R H Q_R.
- formation at a gate-open empty site s: weight F = c|1><1|_s, Kraus sqrt(c)|1><1|_s (lock |1>)
  and sqrt(1 - F) (no record).
- RECORD-SET schedule: period tau, two sub-instants per period (0 and tau/2). A site fires at
  sub-instant 0 if it has exactly one recorded neighbour, at tau/2 if it has two or more
  (gate on the records present at the start of the sub-instant).
- POSSIBILITY-SET schedule (contrast): x instead fires at a sub-instant iff its own normalized
  occupation in the current branch, <n_x>, is >= theta (a set time read off the possibilities).
- distant choice at t = 0: b forms no record / a record in the Z menu / a record in the X menu
  (Born odds; shared possibilities cut to agree, Q1).
Readout: the local record configuration (y, x, z) at time T, summed over b's outcome.
"""
import signal, itertools
import numpy as np
signal.alarm(55)

I2 = np.eye(2); P0 = np.diag([1.0, 0.0]); P1 = np.diag([0.0, 1.0])
def op(single, site, n=4):
    mats = [I2] * n; mats[site] = single
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out
def swap(i, j, n=4):
    d = 2 ** n; S = np.zeros((d, d))
    for s in range(d):
        bits = [(s >> (n - 1 - k)) & 1 for k in range(n)]
        bits[i], bits[j] = bits[j], bits[i]
        t = sum(b << (n - 1 - k) for k, b in enumerate(bits))
        S[t, s] = 1.0
    return S
B, Y, X, Z = 0, 1, 2, 3
J = 1.0
H0 = J * (swap(Y, X) + swap(X, Z)) + J * (op(P0, Y) + op(P0, X))

def evolve(rho, rec, dt):
    """rec: dict site->1 for dynamic records (content |1>). Compressed change."""
    Q = np.eye(16)
    for s in rec:
        Q = Q @ op(P1, s)
    HR = Q @ H0 @ Q
    E, V = np.linalg.eigh(HR)
    U = V @ np.diag(np.exp(-1j * E * dt)) @ V.conj().T
    return U @ rho @ U.conj().T

def neighbours_recorded(site, rec):
    k = 0
    if site == Y:
        k = 1 + (X in rec)
    elif site == X:
        k = 1 + (Y in rec) + (Z in rec)
    elif site == Z:
        k = (X in rec)
    return k

def run(psi, choice, c, tau, ncyc, mode, theta=0.5):
    rho = np.outer(psi, psi.conj())
    # b's choice at t = 0
    branches = {}
    if choice == 'none':
        branches[('-', ())] = rho
    else:
        if choice == 'Z':
            vecs = [np.array([1, 0]), np.array([0, 1])]
        else:
            vecs = [np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)]
        for o, v in enumerate(vecs):
            Pb = op(np.outer(v, v.conj()), B)
            branches[(choice + str(o), ())] = Pb @ rho @ Pb
    Kf = {s: np.sqrt(c) * op(P1, s) for s in (Y, X, Z)}
    Kn = {s: op(P0, s) + np.sqrt(1 - c) * op(P1, s) for s in (Y, X, Z)}
    for n in range(ncyc):
        for sub in (0, 1):
            new = {}
            for (blab, recs), r in branches.items():
                rec = dict(recs)
                r = evolve(r, rec, tau / 2)
                # who fires now (decided from the start-of-sub-instant records)
                fire = []
                for s in (Y, X, Z):
                    if s in rec:
                        continue
                    k = neighbours_recorded(s, rec)
                    if k == 0:
                        continue
                    if mode == 'possibility' and s == X:
                        tr = np.trace(r).real
                        nx = np.trace(op(P1, X) @ r).real / tr if tr > 1e-300 else 0.0
                        if nx >= theta:
                            fire.append(s)
                        continue
                    want = 0 if k == 1 else 1
                    if want == sub:
                        fire.append(s)
                parts = [(rec, r)]
                for s in fire:
                    nxt = []
                    for (rc, rr) in parts:
                        rf = Kf[s] @ rr @ Kf[s].conj().T
                        rn = Kn[s] @ rr @ Kn[s].conj().T
                        rc2 = dict(rc); rc2[s] = 1
                        nxt.append((rc2, rf)); nxt.append((rc, rn))
                    parts = nxt
                for (rc, rr) in parts:
                    key = (blab, tuple(sorted(rc.items())))
                    new[key] = new.get(key, 0) + rr
            branches = new
    dist = {}
    total = 0.0
    for (blab, recs), r in branches.items():
        p = np.trace(r).real
        total += p
        dist[recs] = dist.get(recs, 0.0) + p
    return dist, total

def tv(P, Q):
    keys = set(P) | set(Q)
    return 0.5 * sum(abs(P.get(k, 0) - Q.get(k, 0)) for k in keys)

print("C1. Local record law at time T across a distant choice (b: none / Z / X).")
print("    tau=0.4, 6 periods (12 sub-instants), J=1. TV over the 8 local configurations of (y,x,z).")
rng = np.random.default_rng(36)
for seed in range(4):
    v = rng.normal(size=16) + 1j * rng.normal(size=16)
    psi = v / np.linalg.norm(v)
    for c in (0.3, 0.8):
        res = {}
        for mode in ('record', 'possibility'):
            Ps = {}
            tots = []
            for ch in ('none', 'Z', 'X'):
                Ps[ch], t = run(psi, ch, c, 0.4, 6, mode)
                tots.append(t)
            d = max(tv(Ps['none'], Ps['Z']), tv(Ps['none'], Ps['X']), tv(Ps['Z'], Ps['X']))
            res[mode] = (d, max(abs(t - 1) for t in tots))
        print(f"  state {seed}, c={c}: record-set tick: max TV = {res['record'][0]:.2e} (prob. sum err {res['record'][1]:.1e});"
              f"  possibility-set tick (theta=0.5): max TV = {res['possibility'][0]:.3e}")

print("\nC1b. The same with a maximally entangled b-x pair (|00>+|11>)/sqrt2 on (b,x), y,z in |0>:")
psi = np.zeros(16, complex)
for bx in (0, 1):
    idx = (bx << 3) | (bx << 1)
    psi[idx] = 1 / np.sqrt(2)
for c in (0.3, 0.8):
    for mode in ('record', 'possibility'):
        Ps = {ch: run(psi, ch, c, 0.4, 6, mode)[0] for ch in ('none', 'Z', 'X')}
        d = max(tv(Ps['none'], Ps['Z']), tv(Ps['none'], Ps['X']), tv(Ps['Z'], Ps['X']))
        print(f"  c={c}, {mode}-set tick: max TV = {d:.3e}")
