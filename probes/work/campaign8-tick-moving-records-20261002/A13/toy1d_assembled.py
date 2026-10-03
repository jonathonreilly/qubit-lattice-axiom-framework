#!/usr/bin/env python3
"""A13 check 1: the assembled model on an open chain of N qubits (supplied toy, nothing adopted).

Possibilities: one qubit per site; aligned (quiet) emptiness |0...0>; an "excitation" is |1>.
The axis z stands in for a recorded frame (menus set by records), so lock outcomes are occupation outcomes.
Records: a recorded site carries the locked possibility |1>.

One tick = one brickwork layer of disjoint pairs (even bonds, then odd bonds, alternating):
  1. change: G = cos(th) I - i sin(th) SWAP on every pair of the layer (strictly range-1 per tick);
  2. one local instrument per pair (all pairs disjoint, so they commute):
     - both recorded       : nothing (frozen);
     - one recorded (at i) : relocation = re-formation with the cut (option A):
                             K_stay = |1><1|_i,  K_move = |0><0|_i (record now at partner j);
     - none recorded       : formation, chance tr(F rho) with F = c P_singlet (annihilates the emptiness):
                             K_i = sqrt(c)|10><10|P_s (record at i), K_j = sqrt(c)|01><01|P_s (record at j),
                             K_null = sqrt(1 - c P_s)   (a no-record tick also reshapes the possibilities).
Exact branch enumeration over all record outcomes (pure branch vectors, pruning at 1e-16).

Checks:
  (NS)  B's multi-tick record history vs a distant choice at A (A registers its excitation at tick 1, or follows
        the standard rule), with A and B linked; controls: 'nonull' (no reshaping on no-record ticks) and
        'product' (chance times raw lock odds), both nonlinear.
  (Q)   quiet emptiness: from |0..0> no record ever forms.
  (P1)  one record per site, records agree with possibilities, record count never decreases.
  (C)   lone record: position law equals the classical chain with kernel |G|^2 (stay 1-s, move s).
"""
import itertools
import numpy as np

TOL = 1e-16


def basis_ops(theta, c):
    sw = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    G = np.cos(theta) * np.eye(4) - 1j * np.sin(theta) * sw
    s = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)   # (|01> - |10>)/sqrt2, basis |ij>, i first
    Ps = np.outer(s, s.conj())
    P10 = np.diag([0, 0, 1, 0]).astype(complex)                # site i = 1, site j = 0
    P01 = np.diag([0, 1, 0, 0]).astype(complex)
    ops = {
        'G': G, 'Ps': Ps, 'P10': P10, 'P01': P01,
        'Ki': np.sqrt(c) * P10 @ Ps, 'Kj': np.sqrt(c) * P01 @ Ps,
        'Knull': np.eye(4) - (1 - np.sqrt(1 - c)) * Ps,
        'stay_i': np.diag([0, 0, 1, 1]).astype(complex),        # |1><1|_i (x) 1_j
        'move_i': np.diag([1, 1, 0, 0]).astype(complex),        # |0><0|_i (x) 1_j
        'stay_j': np.diag([0, 1, 0, 1]).astype(complex),        # 1_i (x) |1><1|_j
        'move_j': np.diag([1, 0, 1, 0]).astype(complex),        # 1_i (x) |0><0|_j
        'N_i': np.diag([0, 0, 1, 1]).astype(complex), 'N_j': np.diag([0, 1, 0, 1]).astype(complex),
        'reg_none': np.diag([1, 0, 0, 1]).astype(complex),
    }
    return ops


def apply2(psi, op, i, j):
    o = op.reshape(2, 2, 2, 2)
    out = np.tensordot(o, psi, axes=([2, 3], [i, j]))
    return np.moveaxis(out, [0, 1], [i, j])


def expect2(psi, op, i, j):
    return np.vdot(psi, apply2(psi, op, i, j)).real


def layer_pairs(N, t):
    start = 0 if t % 2 == 1 else 1          # tick 1, 3, ... even bonds; tick 2, 4, ... odd bonds
    return [(a, a + 1) for a in range(start, N - 1, 2)]


def step(branches, N, t, ops, rule='linear', a_choice=None, A_pair=(0, 1), Bmask=0, count_new=None):
    """Advance all branches by one tick. Returns new branch list."""
    pairs = layer_pairs(N, t)
    out = []
    for psi, rec, hist, nform in branches:
        for (i, j) in pairs:
            psi = apply2(psi, ops['G'], i, j)
        cur = [(psi, rec, nform)]
        for (i, j) in pairs:
            nxt = []
            for ps, rc, nf in cur:
                w = np.vdot(ps, ps).real
                ri, rj = (rc >> i) & 1, (rc >> j) & 1
                if ri and rj:
                    nxt.append((ps, rc, nf))
                    continue
                if ri or rj:
                    if ri:
                        opts = [(ops['stay_i'], rc), (ops['move_i'], (rc & ~(1 << i)) | (1 << j))]
                    else:
                        opts = [(ops['stay_j'], rc), (ops['move_j'], (rc & ~(1 << j)) | (1 << i))]
                    for K, rc2 in opts:
                        ch = apply2(ps, K, i, j)
                        if np.vdot(ch, ch).real > TOL:
                            nxt.append((ch, rc2, nf))
                    continue
                # no record in the pair
                if a_choice == 1 and t == 1 and (i, j) == A_pair:      # A registers its excitation
                    opts = [(ops['P10'], rc | (1 << i), nf + 1), (ops['P01'], rc | (1 << j), nf + 1),
                            (ops['reg_none'], rc, nf)]
                    for K, rc2, nf2 in opts:
                        ch = apply2(ps, K, i, j)
                        if np.vdot(ch, ch).real > TOL:
                            nxt.append((ch, rc2, nf2))
                    continue
                if rule == 'linear':
                    opts = [(ops['Ki'], rc | (1 << i), nf + 1), (ops['Kj'], rc | (1 << j), nf + 1),
                            (ops['Knull'], rc, nf)]
                    for K, rc2, nf2 in opts:
                        ch = apply2(ps, K, i, j)
                        if np.vdot(ch, ch).real > TOL:
                            nxt.append((ch, rc2, nf2))
                    continue
                # nonlinear controls
                p = c_of(ops) * expect2(ps, ops['Ps'], i, j) / w        # normalized chance
                if rule == 'nonull':
                    for K, rc2, nf2 in [(ops['Ki'], rc | (1 << i), nf + 1), (ops['Kj'], rc | (1 << j), nf + 1)]:
                        ch = apply2(ps, K, i, j)
                        if np.vdot(ch, ch).real > TOL:
                            nxt.append((ch, rc2, nf2))
                    if 1 - p > TOL:
                        nxt.append((ps * np.sqrt(1 - p), rc, nf))       # possibilities left untouched
                elif rule == 'product':
                    r_i = expect2(ps, ops['P10'], i, j) / w
                    r_j = expect2(ps, ops['P01'], i, j) / w
                    if p > TOL and r_i + r_j > TOL:
                        for P, r, rc2 in [(ops['P10'], r_i, rc | (1 << i)), (ops['P01'], r_j, rc | (1 << j))]:
                            if r <= TOL:
                                continue
                            ch = apply2(ps, P, i, j)
                            nrm = np.vdot(ch, ch).real
                            nxt.append((ch * np.sqrt(w * p * (r / (r_i + r_j)) / nrm), rc2, nf + 1))
                    if 1 - p > TOL:
                        nxt.append((ps * np.sqrt(1 - p), rc, nf))
            cur = nxt
        for ps, rc, nf in cur:
            out.append((ps, rc, hist + (rc & Bmask,), nf))
    if len(out) > 40000:
        raise SystemExit(f"branch guard: {len(out)} branches at tick {t}")
    return out


_C = {}


def c_of(ops):
    return _C['c']


def product_state(N, ones):
    v = np.zeros((2,) * N, dtype=complex)
    idx = tuple(1 if k in ones else 0 for k in range(N))
    v[idx] = 1.0
    return v


def run_ns(N, theta, c, T, rule, a_choice, Bsites):
    ops = basis_ops(theta, c)
    _C['c'] = c
    # A pair (0,1) and B pair (5,6) share a Bell link; record at site 7 (in B)
    psi = (product_state(N, {0, 5, 7}) + product_state(N, {1, 6, 7})) / np.sqrt(2)
    rec0 = 1 << 7
    Bmask = sum(1 << b for b in Bsites)
    br = [(psi, rec0, (), 0)]
    for t in range(1, T + 1):
        br = step(br, N, t, ops, rule=rule, a_choice=a_choice, Bmask=Bmask)
    return br


def hist_dist(br, T):
    out = {}
    per_tick = [dict() for _ in range(T)]
    for psi, rec, hist, nf in br:
        w = np.vdot(psi, psi).real
        out[hist] = out.get(hist, 0) + w
    return out


def tv(d0, d1):
    keys = set(d0) | set(d1)
    return 0.5 * sum(abs(d0.get(k, 0) - d1.get(k, 0)) for k in keys), max(abs(d0.get(k, 0) - d1.get(k, 0)) for k in keys)


def prefix(d, k):
    o = {}
    for h, w in d.items():
        o[h[:k]] = o.get(h[:k], 0) + w
    return o


def check_invariants(br, N, n_initial=1):
    worst_agree, nb = 0.0, 0
    for psi, rec, hist, nf in br:
        w = np.vdot(psi, psi).real
        # permanence: records are never destroyed; relocations keep the count; formations add one each
        assert bin(rec).count('1') == n_initial + nf, (rec, nf)
        for r in range(N):
            if (rec >> r) & 1:
                # probability that site r is NOT in |1> must vanish (record agrees with possibilities)
                v = np.take(psi, 0, axis=r)
                worst_agree = max(worst_agree, np.vdot(v, v).real / w)
        nb += 1
    return worst_agree, nb


def main():
    N, theta, c = 8, 0.6, 0.5
    Bsites = [5, 6, 7]
    T = 4
    print(f"chain N={N}, theta={theta} (s=sin^2={np.sin(theta)**2:.4f}), c={c}, B={Bsites}, A pair (0,1), ticks={T}")
    for rule in ['linear', 'nonull', 'product']:
        d = {}
        for a in (0, 1):
            br = run_ns(N, theta, c, T, rule, a, Bsites)
            d[a] = hist_dist(br, T)
            tot = sum(d[a].values())
            if rule == 'linear':
                wa, nb = check_invariants(br, N)
                print(f"  [linear, A choice {a}] branches={nb}, total prob={tot:.15f}, worst record/possibility disagreement={wa:.1e}")
        rows = []
        for k in range(1, T + 1):
            tvk, mk = tv(prefix(d[0], k), prefix(d[1], k))
            rows.append(f"t<={k}: TV={tvk:.2e}")
        print(f"  rule={rule:8s} B-history vs A's choice: " + "; ".join(rows))

    # light-cone control on a shorter chain (N=6): A pair (0,1), B = {4,5}, Bell link between (0,1) and (3,4),
    # record at 5.  A's tick-1 action can reach site 4 only at tick 4.
    ops6 = basis_ops(theta, c)
    _C['c'] = c
    N6, T6 = 6, 6
    d = {}
    for a in (0, 1):
        psi = (product_state(N6, {0, 3, 5}) + product_state(N6, {1, 4, 5})) / np.sqrt(2)
        br = [(psi, 1 << 5, (), 0)]
        for t in range(1, T6 + 1):
            br = step(br, N6, t, ops6, rule='linear', a_choice=a, Bmask=(1 << 4) | (1 << 5))
        d[a] = hist_dist(br, T6)
    rows = []
    for k in range(1, T6 + 1):
        tvk, mk = tv(prefix(d[0], k), prefix(d[1], k))
        rows.append(f"t<={k}: {tvk:.2e}")
    print(f"  cone control (N=6, B={{4,5}}, A's influence can reach B at tick 4), linear rule: " + "; ".join(rows))

    # (Q) quiet emptiness and (C) lone record
    ops = basis_ops(theta, 0.7)
    _C['c'] = 0.7
    br = [(product_state(N, set()), 0, (), 0)]
    for t in range(1, 9):
        br = step(br, N, t, ops)
    pform = sum(np.vdot(p, p).real for p, r, h, nf in br if nf > 0)
    print(f"  quiet emptiness: branches after 8 ticks = {len(br)}, probability that any record formed = {pform:.1e}")

    x0 = 3
    br = [(product_state(N, {x0}), 1 << x0, (), 0)]
    Tl = 6
    for t in range(1, Tl + 1):
        br = step(br, N, t, ops, Bmask=(1 << N) - 1)
    pnew = sum(np.vdot(p, p).real for p, r, h, nf in br if nf > 0)
    # classical chain with kernel |G|^2 on the same layers
    s = np.sin(theta) ** 2
    pc = np.zeros(N); pc[x0] = 1.0
    for t in range(1, Tl + 1):
        q = pc.copy()
        for (i, j) in layer_pairs(N, t):
            q[i], q[j] = (1 - s) * pc[i] + s * pc[j], (1 - s) * pc[j] + s * pc[i]
        pc = q
    pq = np.zeros(N)
    for psi, rec, hist, nf in br:
        w = np.vdot(psi, psi).real
        pos = [k for k in range(N) if (rec >> k) & 1]
        assert len(pos) == 1
        pq[pos[0]] += w
    print(f"  lone record: new-formation probability = {pnew:.1e}; max |P_branches - P_classical(|G|^2)| = {np.abs(pq - pc).max():.1e}")
    print(f"    position law after {Tl} ticks: " + " ".join(f"{v:.4f}" for v in pq))


if __name__ == '__main__':
    main()
