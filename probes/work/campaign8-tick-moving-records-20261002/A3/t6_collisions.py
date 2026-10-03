"""Check 6: collisions.  Ring N=6, ticks act on 3-site blocks, records may compete for a site.

Supplied model: each tick applies number-conserving 3-qubit block unitaries on a partition
into 3-site blocks (alternating partitions {0,1,2},{3,4,5} and {2,3,4},{5,0,1}).
Inside a block, one record may move only to a neighbouring site (1-record block sector is
a pair-mix plus a phase); two records in a block {s0,s2} may end as {s1,s2} or {s0,s1}:
they compete for s1.  Every configuration change moves each record at most one site.

Rules:
  CONFIG-L1   : LP coupling on configurations (one-step-reachable pairs) - valid by Theorem A.
  CONFIG-MINMH: simultaneous minimal MH rule on configurations (may break the outflow bound).
  I3-LITERAL  : every record proposes a move with its own one-body (neighbourhood) odds,
                independently; if several records want the same site one wins with its
                relative proposal odds, losers stay; a mover into a site whose record stays
                is blocked (cascading).  Exact distribution by enumeration.
"""
import itertools
from collections import defaultdict
import numpy as np
from common import haar_unitary, mh_split, rule_from_flow, rule_from_coupling, lp_coupling, tv
from manybody import sector, gate_full, configs_of, one_step_reachable

N, TICKS = 6, 24
rng = np.random.default_rng(17)
PARTS = [[(0, 1, 2), (3, 4, 5)], [(2, 3, 4), (5, 0, 1)]]


def block_gate():
    g = np.zeros((8, 8), complex)
    g[0, 0] = np.exp(2j * np.pi * rng.random())
    g[7, 7] = np.exp(2j * np.pi * rng.random())
    one = [4, 2, 1]                     # record at block position 0, 1, 2
    if rng.random() < 0.5:
        pair, single = [one[0], one[1]], one[2]
    else:
        pair, single = [one[1], one[2]], one[0]
    g[np.ix_(pair, pair)] = haar_unitary(2, rng)
    g[single, single] = np.exp(2j * np.pi * rng.random())
    two = [6, 5, 3]                     # {0,1}, {0,2}, {1,2}
    g[np.ix_(two, two)] = haar_unitary(3, rng)
    return g


def one_body(P, confs):
    nb = np.zeros(N)
    for p, C in zip(P, confs):
        for s in C:
            nb[s] += p
    return nb


def resolve(props, w):
    """props: {site: target}; w[(x,y)] proposal odds.  Returns list of (config, prob)."""
    movers = {x: y for x, y in props.items() if y != x}
    groups = defaultdict(list)
    for x, y in movers.items():
        groups[y].append(x)
    items = list(groups.items())
    choices = []
    for y, xs in items:
        if len(xs) == 1:
            choices.append([(xs[0], 1.0)])
        else:
            ws = np.array([w[(x, y)] for x in xs]); ws = ws / ws.sum()
            choices.append(list(zip(xs, ws)))
    out = []
    for combo in itertools.product(*choices):
        prob = float(np.prod([p for _, p in combo]))
        final = {x: x for x in props}
        for (y, _), (x, _) in zip(items, combo):
            final[x] = y
        changed = True
        while changed:
            changed = False
            for x, y in list(final.items()):
                if y != x and y in props and final[y] == y:
                    final[x] = x
                    changed = True
        conf = tuple(sorted(final.values()))
        assert len(set(conf)) == len(conf)
        out.append((conf, prob))
    return out


def i3_literal_rule(P, Pn, confs, blocks):
    nb, nbn = one_body(P, confs), one_body(Pn, confs)
    q = {}
    for (s0, s1, s2) in blocks:
        F01 = nb[s0] - nbn[s0]
        F12 = F01 + nb[s1] - nbn[s1]
        q[(s0, s1)] = max(F01, 0) / nb[s0] if nb[s0] > 1e-15 else 0.0
        q[(s1, s0)] = max(-F01, 0) / nb[s1] if nb[s1] > 1e-15 else 0.0
        q[(s1, s2)] = max(F12, 0) / nb[s1] if nb[s1] > 1e-15 else 0.0
        q[(s2, s1)] = max(-F12, 0) / nb[s2] if nb[s2] > 1e-15 else 0.0
    idx = {C: i for i, C in enumerate(confs)}
    T = np.zeros((len(confs), len(confs)))
    excess = 0.0
    for i, C in enumerate(confs):
        opts = []
        for x in C:
            o = [(y, q.get((x, y), 0.0)) for y in range(N) if (x, y) in q]
            stay = 1.0 - sum(p for _, p in o)
            excess = max(excess, -stay)
            o = [(y, p) for y, p in o if p > 0] + [(x, max(stay, 0.0))]
            opts.append([(x, y, p) for y, p in o])
        for combo in itertools.product(*opts):
            pr = float(np.prod([p for _, _, p in combo]))
            if pr == 0:
                continue
            props = {x: y for x, y, _ in combo}
            for conf, pp in resolve(props, q):
                T[i, idx[conf]] += pr * pp
    return T, excess


def run(nrec, label, entangled):
    states = sector(N, nrec)
    confs = configs_of(states, N)
    nc = len(confs)
    reach = np.array([[one_step_reachable(C, Cp, N) for Cp in confs] for C in confs])
    if entangled:
        Psi = rng.normal(size=nc) + 1j * rng.normal(size=nc); Psi /= np.linalg.norm(Psi)
    else:
        Psi = np.zeros(nc, complex); Psi[0] = 1.0
    P = np.abs(Psi) ** 2
    Q = {'CONFIG-L1': P.copy(), 'I3-LITERAL': P.copy()}
    worst = {k: 0.0 for k in Q}
    bad_min, ex_min, nonreach, ex_q = 0, -1.0, 0.0, 0.0
    st_joint, st_one = 0.0, 0.0
    for t in range(TICKS):
        blocks = PARTS[t % 2]
        U = np.eye(1 << N, dtype=complex)
        for b in blocks:
            U = gate_full(N, list(b), block_gate()) @ U
        U = U[np.ix_(states, states)]
        nonreach = max(nonreach, float(np.abs(U[~reach.T]).max()) if (~reach.T).any() else 0.0)
        piMH, K, Psin = mh_split(U, Psi, nc, 1)
        Pn = np.abs(Psin) ** 2
        _, ex = rule_from_flow(piMH - piMH.T, P)
        ex_min = max(ex_min, ex); bad_min += ex > 1e-12
        ok, piL1, _ = lp_coupling(P, Pn, reach, 'moves')
        T_l1 = rule_from_coupling(piL1, P)
        T_i3, exq = i3_literal_rule(P, Pn, confs, blocks)
        ex_q = max(ex_q, exq)
        one_tick = P @ T_i3
        st_joint = max(st_joint, tv(one_tick, Pn))
        st_one = max(st_one, 0.5 * float(np.abs(one_body(one_tick, confs) - one_body(Pn, confs)).sum()) / nrec)
        for k, T in (('CONFIG-L1', T_l1), ('I3-LITERAL', T_i3)):
            Q[k] = Q[k] @ T
            worst[k] = max(worst[k], tv(Q[k], Pn))
        Psi, P = Psin, Pn
    print(f"[{label}] records={nrec}, configs={nc}, ticks={TICKS}; amplitude needing a 2-site move = {nonreach:.1e}")
    print(f"   CONFIG-L1 (valid by Theorem A): max TV(Q_t, P_t) = {worst['CONFIG-L1']:.1e}")
    print(f"   simultaneous CONFIG-MINMH: ticks breaking outflow bound = {bad_min}/{TICKS} (largest excess {ex_min:.3e})")
    print(f"   I3-LITERAL (independent proposals + relative-odds collisions): max TV(Q_t, P_t) = {worst['I3-LITERAL']:.4f}"
          f"  (one-body proposal outflow excess {ex_q:.1e})")
    print(f"   I3-LITERAL from the exact odds, one tick: max joint TV = {st_joint:.4f}; "
          f"max one-body (per-record) TV = {st_one:.4f}")


if __name__ == '__main__':
    run(2, 'two records, formed at sites 0 and 1', False)
    run(2, 'two records, random linked state', True)
    run(3, 'three records, random linked state', True)
