"""A27 check 3: two records competing for one empty site, in a supplied 1D toy.

Sites (qubit order): m = -1 (empty), A = 0 (record, content rA), y = 1 (empty, Bell-linked with a
distant qubit b), B = 2 (record, content rB), p = 3 (empty), b (distant).  Emptiness |1>.
Weights G(r) = beta*1 + (alpha-beta)|r><r|; 1D coordination z = 2, so per-direction weight c/2.

CLAIM rule (CL): stage 1, every empty site next to records applies ONE instrument on its own qubit
with outcomes 'claims record i' (E_i = (c/2) G(r_i)) or 'claims nobody'; stage 2, a record claimed
by several sites picks one uniformly (classical); then SWAP(record site, chosen site).
LITERAL I3: each record proposes independently with its pre-tick local odds; if both propose y,
A wins with relative odds pA/(pA+pB).
Distant choice at b: no record / record with menu Z / record with menu X (outcome unread).
"""
import signal, itertools
import numpy as np

signal.alarm(55)
alpha, beta, c = 0.15, 0.85, 0.9
I2 = np.eye(2)
k0 = np.array([1.0, 0]); k1 = np.array([0, 1.0]); kp = (k0+k1)/np.sqrt(2); km = (k0-k1)/np.sqrt(2)
rA, rB, emp = k0, kp, k1
names = ["m", "A", "y", "B", "p", "b"]; idx = {n: i for i, n in enumerate(names)}; N = 6

def op_on(ops):
    out = np.array([[1.0+0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def G(r):
    return beta*I2 + (alpha-beta)*np.outer(r, r)

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V*np.sqrt(np.clip(w, 0, None))) @ V.conj().T

def swap_op(i, j):
    D = 2**N; S = np.zeros((D, D))
    for bb in range(D):
        bits = [(bb >> (N-1-k)) & 1 for k in range(N)]
        bits[i], bits[j] = bits[j], bits[i]
        S[sum(bit << (N-1-k) for k, bit in enumerate(bits)), bb] = 1
    return S

# initial state: m, A, (y,b) Bell, B, p
bell = (np.kron(k0, k0) + np.kron(k1, k1))/np.sqrt(2)          # (y, b)
psi = np.einsum("a,b,cf,d,e->abcdef", emp, rA, bell.reshape(2, 2), rB, emp).reshape(-1)
rho0 = np.outer(psi, psi)

def after_choice(rho, choice):
    """Return list of (weight, normalized state) branches after b's choice (outcome unread)."""
    if choice == "none":
        return [(1.0, rho)]
    basis = (k0, k1) if choice == "Z" else (kp, km)
    out = []
    for v in basis:
        P = op_on({idx["b"]: np.outer(v, v)})
        s = P @ rho @ P
        w = np.real(np.trace(s))
        out.append((w, s/w))
    return out

# --- CL rule -----------------------------------------------------------------
E = {("m", "A"): (c/2)*G(rA), ("y", "A"): (c/2)*G(rA), ("y", "B"): (c/2)*G(rB), ("p", "B"): (c/2)*G(rB)}
claim_sites = {"m": ["A"], "y": ["A", "B"], "p": ["B"]}
pos = {"m": -1, "A": 0, "y": 1, "B": 2, "p": 3}

def cl_law(rho):
    law = {}
    opts = {s: recs + [None] for s, recs in claim_sites.items()}
    for combo in itertools.product(*[opts[s] for s in ["m", "y", "p"]]):
        claims = dict(zip(["m", "y", "p"], combo))
        ops = {}
        for s, who in claims.items():
            if who is None:
                Es = sum(E[(s, rr)] for rr in claim_sites[s])
                ops[idx[s]] = sqrtm_psd(I2 - Es)
            else:
                ops[idx[s]] = sqrtm_psd(E[(s, who)])
        K = op_on(ops)
        w = np.real(np.trace(K @ rho @ K.conj().T))
        if w < 1e-300:
            continue
        cand = {rec: [s for s, who in claims.items() if who == rec] for rec in ["A", "B"]}
        choicesA = cand["A"] or [None]; choicesB = cand["B"] or [None]
        for ca in choicesA:
            for cb in choicesB:
                pr = w/len(choicesA)/len(choicesB)
                key = (pos[ca] if ca else 0, pos[cb] if cb else 2)
                law[key] = law.get(key, 0) + pr
    return law

# --- literal I3 ----------------------------------------------------------------
def red1(rho, keep):
    t = rho.reshape([2]*(2*N))
    in_idx = list(range(2*N))
    for i in range(N):
        if i != keep:
            in_idx[i+N] = in_idx[i]
    return np.einsum(t, in_idx, [keep, keep+N])

def lit_law(rho):
    g = lambda s, r: np.real(np.trace(G(r) @ red1(rho, idx[s])))
    pAm, pAy = (c/2)*g("m", rA), (c/2)*g("y", rA)
    pBy, pBp = (c/2)*g("y", rB), (c/2)*g("p", rB)
    A_opts = {-1: pAm, 1: pAy, 0: 1-pAm-pAy}
    B_opts = {1: pBy, 3: pBp, 2: 1-pBy-pBp}
    law = {}
    for a, pa in A_opts.items():
        for b, pb in B_opts.items():
            if a == 1 and b == 1:
                law[(1, 2)] = law.get((1, 2), 0) + pa*pb*pAy/(pAy+pBy)
                law[(0, 1)] = law.get((0, 1), 0) + pa*pb*pBy/(pAy+pBy)
            else:
                law[(a, b)] = law.get((a, b), 0) + pa*pb
    return law

def avg_law(rule, choice):
    tot = {}
    for w, s in after_choice(rho0, choice):
        for k, v in rule(s).items():
            tot[k] = tot.get(k, 0) + w*v
    return tot

def tv(l1, l2):
    keys = set(l1) | set(l2)
    return 0.5*sum(abs(l1.get(k, 0) - l2.get(k, 0)) for k in keys)

for name, rule in [("CL (claim rule)", cl_law), ("literal I3", lit_law)]:
    L = {ch: avg_law(rule, ch) for ch in ["none", "Z", "X"]}
    print(f"{name}: total prob {sum(L['none'].values()):.15f}; "
          f"P(both at y) {L['none'].get((1, 1), 0):.1e}; "
          f"TV none/Z {tv(L['none'], L['Z']):.2e}, none/X {tv(L['none'], L['X']):.2e}, Z/X {tv(L['Z'], L['X']):.2e}")
    print("   law (A pos, B pos):", {k: round(v, 5) for k, v in sorted(L["none"].items())})

# relative-odds identity at the clash site under CL (state with no choice at b)
rho_y = np.eye(2)/2
wA = np.real(np.trace(E[("y", "A")] @ rho_y)); wB = np.real(np.trace(E[("y", "B")] @ rho_y))
print(f"CL at the clash site: P(y takes A | y takes someone) = {wA/(wA+wB):.6f}  (relative odds wA/(wA+wB))")
