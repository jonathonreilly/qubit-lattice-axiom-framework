"""Exact stationary laws on a 4x4 torus with n records (no formation), by full enumeration.
Model T1 (parallel tick, heat-bath over destinations incl. stay, conflicts by relative odds) vs
model K (continuous-time, rate exp(g S_y) per move, S_y = records around y other than the mover).
Compares each stationary law with the Gibbs law  pi(eta) ~ exp(g * #nearest-neighbour record pairs).
Reports: max relative deviation from Gibbs, P(at least one adjacent pair), and detailed-balance violation.
"""
import itertools
import numpy as np

Lx = Ly = 4
N = Lx * Ly
def nb(i):
    x, y = divmod(i, Ly)
    return [((x + 1) % Lx) * Ly + y, ((x - 1) % Lx) * Ly + y, x * Ly + (y + 1) % Ly, x * Ly + (y - 1) % Ly]
NB = [nb(i) for i in range(N)]

def bonds(occ):
    return sum(1 for i in occ for j in NB[i] if j in occ) // 2

def run(n, g):
    states = [frozenset(c) for c in itertools.combinations(range(N), n)]
    index = {s: k for k, s in enumerate(states)}
    M = len(states)
    P = np.zeros((M, M))
    Qg = np.zeros((M, M))
    for k, s in enumerate(states):
        recs = sorted(s)
        opts = []
        for r in recs:
            Sx = sum(1 for j in NB[r] if j in s)
            o = [(r, np.exp(g * Sx))]
            for y in NB[r]:
                if y not in s:
                    Sy = sum(1 for j in NB[y] if j in s and j != r)
                    o.append((y, np.exp(g * Sy)))
                    Qg[k, index[(s - {r}) | {y}]] += np.exp(g * Sy)   # model K generator
            Z = sum(w for _, w in o)
            opts.append([(d, w / Z) for d, w in o])
        for choice in itertools.product(*opts):
            pc = np.prod([p for _, p in choice])
            # group claims on each empty destination
            claims = {}
            for r, (dst, p) in zip(recs, choice):
                if dst != r:
                    claims.setdefault(dst, []).append((r, p))
            # enumerate winners for each contested destination (relative odds)
            dests = list(claims.items())
            winner_lists = [[(r, p / sum(q for _, q in lst)) for r, p in lst] for _, lst in dests]
            for wins in itertools.product(*winner_lists):
                pw = np.prod([p for _, p in wins]) if wins else 1.0
                new = set(s)
                for (dst, _), (r, _) in zip(dests, wins):
                    new.discard(r); new.add(dst)
                P[k, index[frozenset(new)]] += pc * pw
    assert np.allclose(P.sum(axis=1), 1)
    # stationary laws
    w, v = np.linalg.eig(P.T)
    pi = np.real(v[:, np.argmin(np.abs(w - 1))]); pi /= pi.sum()
    np.fill_diagonal(Qg, -Qg.sum(axis=1))
    w2, v2 = np.linalg.eig(Qg.T)
    piK = np.real(v2[:, np.argmin(np.abs(w2))]); piK /= piK.sum()
    gib = np.array([np.exp(g * bonds(s)) for s in states]); gib /= gib.sum()
    adj = np.array([bonds(s) > 0 for s in states])
    db = np.max(np.abs(pi[:, None] * P - (pi[:, None] * P).T))
    print(f"n={n} g={g}: T1 max|pi/gibbs-1|={np.max(np.abs(pi/gib-1)):.4f}  K max|pi/gibbs-1|={np.max(np.abs(piK/gib-1)):.2e}  "
          f"P(adjacent pair): T1={pi[adj].sum():.4f} K={piK[adj].sum():.4f} Gibbs={gib[adj].sum():.4f}  "
          f"T1 detailed-balance violation max|pi_i P_ij - pi_j P_ji|={db:.2e}")

for n in (2, 3):
    for g in (0.0, 1.0, 2.0):
        run(n, g)
