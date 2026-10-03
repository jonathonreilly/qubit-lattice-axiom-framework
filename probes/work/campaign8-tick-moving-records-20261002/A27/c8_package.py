"""A27 assembled toy for Option R (supplied 1D model, 8 qubits, exact branching).

Sites 0..7.  Site 1 (A's side) is Bell-linked with site 5 (B's side).  B's record sits at 6 with
content |0>; site 7 holds |+>; sites 0,2,3,4 hold the emptiness |1>.
Tick 0: A's choice -- no record at 1, or a record at 1 with menu Z, or with menu X (Q1 cut; A's
outcome unread by B).  Each tick then: (R-b) smooth change exp(-i tau QHQ), H = sum SWAP (Heisenberg),
compressed at recorded sites (locked possibilities kept); (R-a) B's record move instrument.
  SW  (linear): K_q = sqrt(c/2) SWAP_{pq} sqrt(G)_q, K_stay = sqrt(1 - (c/2) sum_q G_q)
  REN (ratio) : move with prob c, direction q with odds g_q / sum g (star-restricted renormalized)
B's readable history = its positions after ticks 1..n.  TV between A's choices, n = 1..3.
"""
import signal
import numpy as np
from scipy.linalg import expm
signal.alarm(55)
N = 8; D = 2**N
alpha, beta, c = 0.15, 0.85, 0.9
I2 = np.eye(2)
k0 = np.array([1.0, 0j]); k1 = np.array([0j, 1.0]); kp = (k0+k1)/np.sqrt(2); km = (k0-k1)/np.sqrt(2)

def op_on(ops):
    out = np.array([[1.0+0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def swap(i, j):
    S = np.zeros((D, D))
    for b in range(D):
        bits = [(b >> (N-1-k)) & 1 for k in range(N)]
        bits[i], bits[j] = bits[j], bits[i]
        S[sum(bit << (N-1-k) for k, bit in enumerate(bits)), b] = 1
    return S

SW = {(i, i+1): swap(i, i+1) for i in range(N-1)}
for i in range(N-1):
    SW[(i+1, i)] = SW[(i, i+1)]
H = sum(SW[(i, i+1)] for i in range(N-1))
rB = k0
Gm = beta*I2 + (alpha-beta)*np.outer(rB, rB.conj())

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V*np.sqrt(np.clip(w, 0, None))) @ V.conj().T

# initial state
bell = (np.kron(k0, k0) + np.kron(k1, k1))/np.sqrt(2)
psi = np.zeros(D, complex)
# order: 0..7 ; build as sum over bell components
for (s1, s5), amp in [((0, 0), 1/np.sqrt(2)), ((1, 1), 1/np.sqrt(2))]:
    st = [k1, [k0, k1][s1], k1, k1, k1, [k0, k1][s5], rB, kp]
    v = np.array([1.0+0j])
    for s in st:
        v = np.kron(v, s)
    psi += amp*v
rho0 = np.outer(psi, psi.conj())

ucache = {}
def U_for(records):
    key = tuple(sorted((s, tuple(np.round(v, 12))) for s, v in records.items()))
    if key not in ucache:
        Q = op_on({s: np.outer(v, v.conj()) for s, v in records.items()})
        ucache[key] = expm(-1j*tau*(Q @ H @ Q))
    return ucache[key]

def red1(rho, keep):
    t = rho.reshape([2]*(2*N))
    idx = list(range(2*N))
    for i in range(N):
        if i != keep:
            idx[i+N] = idx[i]
    return np.einsum(t, idx, [keep, keep+N])

def step_B(rho, pB, occupied, rule):
    """Return list of (new pB, rho_out unnormalized) for B's move instrument."""
    nbrs = [q for q in (pB-1, pB+1) if 0 <= q < N and q not in occupied]
    out = []
    if rule == "SW":
        Ksum = sum(op_on({q: (c/2)*Gm}) for q in nbrs) if nbrs else 0*np.eye(D)
        Ks = sqrtm_psd(np.eye(D) - Ksum)
        out.append((pB, Ks @ rho @ Ks.conj().T))
        for q in nbrs:
            K = np.sqrt(c/2)*SW[(pB, q)] @ op_on({q: sqrtm_psd(Gm)})
            out.append((q, K @ rho @ K.conj().T))
    else:  # REN: ratio odds, applied branch by branch (nonlinear)
        tr = np.real(np.trace(rho))
        g = {q: np.real(np.trace(Gm @ red1(rho, q)))/tr for q in nbrs}
        out.append((pB, (1-c)*rho if nbrs else rho))
        for q in nbrs:
            K = SW[(pB, q)] @ op_on({q: sqrtm_psd(Gm)})
            post = K @ rho @ K.conj().T
            post *= (c*g[q]/sum(g.values()))*tr/np.real(np.trace(post))
            out.append((q, post))
    return out

def history_law(choice, rule, n):
    branches = []
    if choice == "none":
        branches.append(({}, rho0))
    else:
        basis = (k0, k1) if choice == "Z" else (kp, km)
        for v in basis:
            P = op_on({1: np.outer(v, v.conj())})
            branches.append(({1: v}, P @ rho0 @ P))
    # attach B
    states = [(recA, 6, (), r) for recA, r in branches]
    for _ in range(n):
        new = []
        for recA, pB, hist, r in states:
            recs = dict(recA); recs[pB] = rB
            U = U_for(recs)
            r = U @ r @ U.conj().T
            for q, ro in step_B(r, pB, set(recA), rule):
                new.append((recA, q, hist + (q,), ro))
        states = new
    law = {}
    for recA, pB, hist, r in states:
        law[hist] = law.get(hist, 0) + np.real(np.trace(r))
    return law

def tv(a, b):
    ks = set(a) | set(b)
    return 0.5*sum(abs(a.get(k, 0) - b.get(k, 0)) for k in ks)

import sys
TAUS = [float(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [0.1, 0.5]
NS = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [1, 2, 3]
for tau in TAUS:
    ucache.clear()
    for rule in ["SW", "REN"]:
        row = []
        for n in NS:
            L = {ch: history_law(ch, rule, n) for ch in ["none", "Z", "X"]}
            tot = sum(L["none"].values())
            row.append((n, tv(L["Z"], L["X"]), tv(L["none"], L["Z"]), tot))
        print(f"tau={tau} rule={rule:3s}: " + "; ".join(
            f"n={n}: TV(Z,X)={a:.1e} TV(none,Z)={b:.1e}" for n, a, b, t in row) + f"  [total prob {row[-1][3]:.12f}]")
