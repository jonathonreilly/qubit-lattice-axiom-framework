"""A28 c5: is the 'quiet class' dark sector invariant under the whole gated Option R package?
(supplied toy, 1D ring of N qubits; aligned emptiness |n> = |0>).

Per tick: Stage 1 gated joint instruments (pre-tick pattern) at empty sites with a recorded
neighbour: form (weight F), claim a recorded neighbour (SW-blind, c_m/z each), or nothing;
Stage 2 uniform pick; Stage 3 SWAP; then compressed Heisenberg change exp(-i Q H Q tau).
Weights:  B (pair weight on UNRECORDED pairs only): F = c * sum_{z unrec nbr} P_singlet(s,z) / 2
          A (ferro, includes recorded nbrs, compressed): F = c * sum_{y nbr} <P_singlet(s,y)> / 2
We follow only the no-formation branches and report P(at least one formation within T ticks).
Cases: record content r = |0> (= n), |1> (= -n, on axis), |+> (off axis); emptiness aligned,
or the emptiness replaced by a random entangled state (a stand-in for a full-rank vacuum).
"""
import signal, itertools
import numpy as np
from scipy.linalg import expm
signal.alarm(55)

N = 6
NB = {s: [(s - 1) % N, (s + 1) % N] for s in range(N)}
BONDS = [(s, (s + 1) % N) for s in range(N)]
SW2 = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
s_ = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
PS = np.outer(s_, s_.conj())


def apply(op, sites, psi):
    k = len(sites)
    out = np.tensordot(op.reshape((2,) * (2 * k)), psi, axes=(list(range(k, 2 * k)), sites))
    return np.moveaxis(out, list(range(k)), sites)


def full(op, sites):
    d = 2 ** N; M = np.zeros((d, d), dtype=complex)
    for j in range(d):
        e = np.zeros(d, dtype=complex); e[j] = 1
        M[:, j] = apply(op, sites, e.reshape((2,) * N)).reshape(d)
    return M


H = sum(full(SW2, list(b)) for b in BONDS)


def sqrtm_psd(A):
    w, v = np.linalg.eigh((A + A.conj().T) / 2)
    return (v * np.sqrt(np.clip(w, 0, None))) @ v.conj().T


def weight(s, recs, variant, c):
    """Return (F as a matrix on sites list, sites)."""
    un = [z for z in NB[s] if z not in recs]
    sites = [s] + un
    dim = 2 ** len(sites)
    F = np.zeros((dim, dim), dtype=complex)
    for j, z in enumerate(un):
        # P_singlet on (s, z) embedded in sites
        F += full_small(PS, [0, 1 + j], len(sites)) * c / 2
    if variant == 'A':
        for y in NB[s]:
            if y in recs:
                r = recs[y]; rp = np.array([-np.conj(r[1]), np.conj(r[0])])
                F += full_small(np.outer(rp, rp.conj()) / 2, [0], len(sites)) * c / 2
    return F, sites


def full_small(op, idx, n):
    d = 2 ** n; M = np.zeros((d, d), dtype=complex)
    for j in range(d):
        e = np.zeros(d, dtype=complex); e[j] = 1
        M[:, j] = apply(op, idx, e.reshape((2,) * n)).reshape(d)
    return M


_UCACHE = {}


def U_for(rc_key, rc, tau):
    if rc_key not in _UCACHE:
        Q = np.array([[1.0 + 0j]])
        for q in range(N):
            Q = np.kron(Q, np.outer(rc[q], rc[q].conj()) if q in rc else np.eye(2))
        _UCACHE[rc_key] = expm(-1j * tau * (Q @ H @ Q))
    return _UCACHE[rc_key]


def run(r, vac, variant, T=6, c=0.4, c_m=0.4, tau=0.3, seed=0):
    """Density matrices merged by record configuration; follow no-formation branches only."""
    _UCACHE.clear()
    rng = np.random.default_rng(seed)
    if vac == 'aligned':
        rest = np.zeros((2,) * (N - 1), dtype=complex); rest[(0,) * (N - 1)] = 1
    else:
        rest = rng.normal(size=(2,) * (N - 1)) + 1j * rng.normal(size=(2,) * (N - 1)); rest /= np.linalg.norm(rest)
    psi = np.einsum('i,...->i...', r, rest).reshape(-1)
    confs = {(0,): ({0: r}, np.outer(psi, psi.conj()))}
    for t in range(T):
        new = {}
        for key, (pre, rho) in confs.items():
            stage = [(rho, [])]
            for s in range(N):
                if s in pre or not any(y in pre for y in NB[s]):
                    continue
                F, sites = weight(s, pre, variant, c)
                rn = [y for y in NB[s] if y in pre]
                E0 = np.eye(F.shape[0]) - F - (c_m / 2) * len(rn) * np.eye(F.shape[0])
                K0 = full(sqrtm_psd(E0), sites)
                nxt = []
                for rh, cl in stage:
                    nxt.append((K0 @ rh @ K0.conj().T, cl))
                    for y in rn:
                        nxt.append((rh * (c_m / 2), cl + [(y, s)]))
                stage = nxt
            for rh, cl in stage:
                tg = {}
                for y, s in cl:
                    tg.setdefault(y, []).append(s)
                opts = [[(y, s) for s in ss] for y, ss in sorted(tg.items())]
                for combo in (itertools.product(*opts) if opts else [()]):
                    w = np.prod([1.0 / len(ss) for ss in tg.values()]) if tg else 1.0
                    r3 = rh * w; rc = dict(pre)
                    for y, s in combo:
                        S = full(SW2, [y, s]); r3 = S @ r3 @ S.conj().T; rc[s] = rc.pop(y)
                    k2 = tuple(sorted(rc))
                    U = U_for(k2, rc, tau)
                    r3 = U @ r3 @ U.conj().T
                    if k2 in new:
                        new[k2] = (rc, new[k2][1] + r3)
                    else:
                        new[k2] = (rc, r3)
        confs = new
    surv = sum(np.trace(rh).real for _, rh in confs.values())
    return 1.0 - surv, len(confs)


cases = [('|0> = n', np.array([1, 0], dtype=complex)), ('|1> = -n', np.array([0, 1], dtype=complex)),
         ('|+> off axis', np.array([1, 1], dtype=complex) / np.sqrt(2))]
print('P(at least one formation within 6 ticks); ring N=6, one record at site 0')
for vac in ('aligned', 'random'):
    for variant in ('B', 'A'):
        row = f'  vacuum={vac:7s} weight={variant}: '
        for name, r in cases:
            p, nb = run(r, vac, variant)
            row += f'{name}: {p:.3e}   '
        print(row)
