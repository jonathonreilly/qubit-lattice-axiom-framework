#!/usr/bin/env python3
"""Exact small circuit checks plus explicit compiler/routing witnesses.

No full native-register simulation or physical timing inference. Gaussian
rationals and unnormalized Hadamards keep every comparison exact. Independent
proof checking is external to this supervisor-authored diagnostic program.
"""
import argparse
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

ZERO, ONE = (F(0), F(0)), (F(1), F(0))


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def put(v, z, a):
    v[z] = add(v.get(z, ZERO), a)
    if v[z] == ZERO:
        del v[z]


def gate(v, g):
    kind, a, *rest = g
    ma = 1 << a
    if kind == 'X':
        return {z ^ ma: x for z, x in v.items()}
    out = {}
    if kind == 'H':
        for z, x in v.items():
            put(out, z & ~ma, x)
            put(out, z | ma, mul((-1 if z & ma else 1, 0), x))
        return out
    mb = 1 << rest[0]
    for z, x in v.items():
        if kind == 'S':
            put(out, z ^ (ma | mb) if bool(z & ma) != bool(z & mb) else z, x)
        elif kind == 'C':
            put(out, z ^ mb if z & ma else z, x)
        elif kind in ('V', 'Vd'):
            if z & ma:
                s = 1 if kind == 'V' else -1
                put(out, z, mul((F(1, 2), F(s, 2)), x))
                put(out, z ^ mb, mul((F(1, 2), F(-s, 2)), x))
            else:
                put(out, z, x)
        else:
            raise ValueError(g)
    return out


def inverse(word):
    return [(('Vd' if g[0] == 'V' else 'V' if g[0] == 'Vd' else g[0]), *g[1:])
            for g in reversed(word)]


def run(v, word):
    for g in word:
        v = gate(v, g)
    return v


def ccx(a, b, t):
    return [('V', b, t), ('C', a, b), ('Vd', b, t), ('C', a, b), ('V', a, t)]


def herald_word(m, fault=None):
    r = 4*m
    work = list(range(r, 2*r-1))
    pointer = 2*r-1
    decode = []
    for e in range(m):
        a, b, c, d = range(4*e, 4*e+4)
        decode += [('S', c, d), ('S', b, c), ('C', a, b), ('H', a), ('C', c, d)]
        decode += [('X', a), ('X', c), ('X', d)]
    chain = ccx(0, 1, work[0])
    for j in range(2, r):
        chain += ccx(work[j-2], j, work[j-1])
    word = decode + chain + [('C', work[-1], pointer)]
    if fault != 'no-uncompute':
        word += inverse(chain)
    word += inverse(decode)
    return word, pointer


def expected(z, p, m, pointer):
    # Direct full-native rank-one projector, with no decoder/compiler import.
    scale = 2**m
    out = {z | (p << pointer): (F(scale), F(0))}
    occupied_words = [sum(t << (4*j) for j, t in enumerate(choice))
                      for choice in product((1, 8), repeat=m)]
    if z in occupied_words:
        for w in occupied_words:
            put(out, w | ((p ^ 1) << pointer), ONE)
            put(out, w | (p << pointer), (-F(1), F(0)))
    return out


def circuit_checks(fault):
    for z in range(8):
        target = z ^ 4 if z & 1 and z & 2 else z
        assert run({z: ONE}, ccx(0, 1, 2)) == {target: ONE}, ('ccx phase', z)
    counts = {}
    for m in (1, 2):
        word, pointer = herald_word(m, fault)
        pair_count = sum(len(g) == 3 for g in word)
        if fault is None:
            assert pair_count == 48*m-9
            assert len(word)-pair_count == 8*m
        cases = 0
        for z in range(2**(4*m)):
            for p in (0, 1):
                actual = run({z | (p << pointer): ONE}, word)
                assert actual == expected(z, p, m, pointer), ('herald', m, z, p)
                cases += 1
        counts[str(m)] = {'full_native_basis_columns': cases, 'pair_gates': pair_count,
                          'onsite_gates': len(word)-pair_count, 'clean_work': 4*m-1}
    return counts


def is_vertex(x):
    return all(t % 5 == 0 for t in x)


def hub_path(x, side):
    """Explicit path in the graph excluding all coarse vertices."""
    assert not is_vertex(x)
    out, z = [x], list(x)
    if z[1] % 5 == 0 and z[2] % 5 == 0:
        z[1] += 1
        out.append(tuple(z))
    for axis in range(3):
        while z[axis] != 1:
            z[axis] += 1 if z[axis] < 1 else -1
            out.append(tuple(z))
    return out


def path(x, y, side):
    def access(z):
        if not is_vertex(z):
            return hub_path(z, side)
        neighbor = ((z[0]+1) % side, z[1], z[2])
        return [z]+hub_path(neighbor, side)
    raw = access(x)+list(reversed(access(y)))[1:]
    simple, index = [], {}
    for z in raw:
        if z in index:
            cut = index[z]+1
            for old in simple[cut:]:
                del index[old]
            simple = simple[:cut]
        else:
            index[z] = len(simple)
            simple.append(z)
    return simple


def route_pair(kind, x, y, side):
    p = path(x, y, side)
    swaps = [('S', p[j], p[j+1]) for j in range(len(p)-2)]
    return swaps+[(kind, p[-2], y)]+list(reversed(swaps))


def routing_checks():
    cases, largest, reads = 0, 0, 0
    for n in (3, 12, 14):
        side = 5*n
        # Every residue class and some periodic seam/vertex endpoint cases.
        for x in product(range(5), repeat=3):
            y = tuple((side-1-2*t) % side for t in x)
            if x == y:
                continue
            p = path(x, y, side)
            assert p[0] == x and p[-1] == y
            assert len(set(p)) == len(p)
            assert not any(is_vertex(z) for z in p[1:-1])
            assert all(sum(min((u-v) % side, (v-u) % side) for u, v in zip(a, b)) == 1
                       for a, b in zip(p, p[1:]))
            assert all(sum(abs(u-v) for u, v in zip(a, b)) == 1
                       for a, b in zip(p, p[1:])), 'periodic shortcut is not a native Z3 edge'
            assert len(p)-1 <= 30*n+2
            labels = {z: z for z in p}
            for kind, a, b in route_pair('C', x, y, side):
                if kind == 'S':
                    labels[a], labels[b] = labels[b], labels[a]
                else:
                    assert (labels[a], labels[b]) == (x, y), 'wrong routed operands'
            assert all(a == b for a, b in labels.items()), 'permutation not returned'
            largest = max(largest, len(p)-1)
            cases += 1
        for record in ((0, 0, 0), (side-5, 5, 10)):
            work = (2, 3, 1)
            neighbor = ((record[0]+1) % side, record[1], record[2])
            p = path(work, neighbor, side)
            assert all(not is_vertex(z) for z in p)
            swaps = [('S', a, b) for a, b in zip(p, p[1:])]
            labels = {z: z for z in p+[record]}
            for kind, a, b in swaps+[('C', record, neighbor)]+list(reversed(swaps)):
                if kind == 'S':
                    assert record not in (a, b)
                    labels[a], labels[b] = labels[b], labels[a]
                else:
                    assert (labels[a], labels[b]) == (record, work)
                assert labels[record] == record
            assert all(a == b for a, b in labels.items())
            reads += 1
    return {'paths_and_returned_permutations': cases, 'largest_sampled_path': largest,
            'old_record_control_routes': reads,
            'n_values': [3, 12, 14], 'theorem_bound': '30n+2',
            'embedding': 'ordinary finite Z3 box, no periodic shortcut gates'}


def bool_run(bits, word):
    for g in word:
        if g[0] == 'C':
            bits[g[2]] ^= bits[g[1]]
        elif g[0] == 'T':
            bits[g[3]] ^= bits[g[1]] & bits[g[2]]
        elif g[0] == 'X':
            bits[g[1]] ^= 1
        else:
            raise ValueError(g)


def copy_word(d, N, masked=True):
    B = d+2*N
    # Input headers, values, flags; work headers, masked values, flags; temporary.
    word = [('C', i, B+i) for i in range(d)]
    for j in range(N):
        b, f, y, fw, t = d+j, d+N+j, B+d+j, B+d+N+j, 2*B
        word += [('C', f, fw)]
        word += ([('C', b, t), ('T', fw, t, y), ('C', b, t)]
                 if masked else [('C', b, y)])
    return word


def predicate_word(literals, scratch):
    """Reversible conjunction on WORK copies; caller reverses after its use."""
    assert len(literals) >= 2 and len(scratch) >= len(literals)-1
    word = [('X', bit) for bit, expected_bit in literals if expected_bit == 0]
    word += [('T', literals[0][0], literals[1][0], scratch[0])]
    for j in range(2, len(literals)):
        word += [('T', scratch[j-2], literals[j][0], scratch[j-1])]
    return word, scratch[len(literals)-2]


def controller_checks(fault):
    cases = branches = 0
    for d, N in ((1, 1), (1, 3), (2, 4)):
        B = d+2*N
        word = copy_word(d, N, masked=fault != 'unmasked-copy')
        for alpha in product((0, 1), repeat=d):
            for k in range(N+1):
                for h in product((0, 1), repeat=k):
                    input_bits = list(alpha+h+(0,)*(N-k)+(1,)*k+(0,)*(N-k))
                    for output in ((0, 1) if k < N else (0,)):
                        bits = input_bits+[0]*(B+1+d+N)
                        bool_run(bits, word)
                        H, Y, flags = bits[B:B+d], bits[B+d:B+d+N], bits[B+d+N:2*B]
                        selected = []
                        for j in range(N):
                            stage = (j == 0 or flags[j-1]) and not flags[j]
                            for a in product((0, 1), repeat=d):
                                for history in product((0, 1), repeat=j):
                                    if stage and tuple(H) == a and tuple(Y[:j]) == history:
                                        selected.append((j, a, history))
                                    literals = [(B+i, value) for i, value in enumerate(a)]
                                    literals += [(B+d+i, value) for i, value in enumerate(history)]
                                    if j:
                                        literals += [(B+d+N+j-1, 1)]
                                    literals += [(B+d+N+j, 0)]
                                    pred, indicator = predicate_word(literals, list(range(2*B+1, len(bits))))
                                    bool_run(bits, pred)
                                    want = bool(stage and tuple(H) == a and tuple(Y[:j]) == history)
                                    assert bits[indicator] == want, 'compiled predicate'
                                    bool_run(bits, list(reversed(pred)))
                                    assert not any(bits[2*B:]), 'predicate scratch not cleared'
                                    branches += 1
                        assert selected == ([(k, alpha, h)] if k < N else []), 'selector'
                        if k < N:
                            bits[d+k] = output
                        bool_run(bits, list(reversed(word)))
                        assert not any(bits[B:]), ('dirty controller', d, N, k, output)
                        assert bits[:d+k] == input_bits[:d+k], 'old values modified'
                        assert bits[d+N:B] == input_bits[d+N:B], 'flags prematurely modified'
                        cases += 1
    return {'prefix_outcome_cleanups': cases, 'branch_predicates': branches,
            'scope': 'exact reversible copy/cleanup and compiled conjunction predicates; no formation simulator'}


def witnesses():
    # Two-bit reader test has rank four outside the code: decoded 0000 passes,
    # but rank-one target is 0100. Presence-vs-blank |0> has equal quantum input.
    two_flag_accept = lambda z: not (z & 1) and not (z & 8)
    assert sum(two_flag_accept(z) for z in range(16)) == 4
    assert two_flag_accept(0) and 0 != 2
    return {'two_flag_full_native_rank': 4, 'full_word_projector_rank': 1,
            'recorded_zero_and_blank_zero_density_equal': True,
            'interpretation': 'specific encoding/interface witnesses, not axiom no-go claims'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fault', choices=('no-uncompute', 'unmasked-copy'))
    args = parser.parse_args()
    for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                 'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
        assert os.environ.get(name) == '1', name
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    started = time.monotonic()
    def guard(_s, _f):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss = rss if sys.platform == 'darwin' else rss*1024
        if time.monotonic()-started > 60 or rss > 270_000_000:
            raise RuntimeError('resource bound exceeded')
    signal.signal(signal.SIGALRM, guard)
    signal.setitimer(signal.ITIMER_REAL, 0.2, 0.2)
    result = {'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'circuits': circuit_checks(args.fault), 'routing': routing_checks(),
              'controller': controller_checks(args.fault), 'witnesses': witnesses()}
    result.update(status='ok', elapsed_seconds=time.monotonic()-started,
                  max_rss_host_units=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
