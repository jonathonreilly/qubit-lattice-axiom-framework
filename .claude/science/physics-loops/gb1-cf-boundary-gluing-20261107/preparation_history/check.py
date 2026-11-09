#!/usr/bin/env python3
"""Bounded exact checks, not a simulation of the full native Hilbert space."""
import argparse
from hashlib import sha256
from itertools import permutations, product
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

AUDIT_TIMEOUT_SEC = 60


def rotations():
    out = []
    for p in permutations(range(3)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))
        for s in product((-1, 1), repeat=3):
            if sign*s[0]*s[1]*s[2] == 1:
                out.append(tuple(tuple(s[j] if i == p[j] else 0 for i in range(3))
                                 for j in range(3)))
    return out


ROTATIONS = rotations()
FRAME = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
MARKER = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 2, 0),
          (0, 0, 1), (0, 0, 2), (0, 0, 3))


def image(z, a, f, side):
    return tuple((a[i]+5*sum(z[j]*f[j][i] for j in range(3))) % side
                 for i in range(3))


def encode(a, f, d, header, history, n):
    r = {image(z, a, f, 5*n): 1 for z in MARKER}
    for j, b in enumerate(header+history, 1):
        x = image((2*j, 4, 0), a, f, 5*n)
        assert x not in r
        r[x] = b
    return r


def decode(r, d, N, n):
    # Search every possible anchor and every proper frame; no degree/arm proof.
    candidates = []
    for a in r:
        for f in ROTATIONS:
            marker = {image(z, a, f, 5*n) for z in MARKER}
            if not all(r.get(x) == 1 for x in marker):
                continue
            word = [image((2*j, 4, 0), a, f, 5*n) for j in range(1, d+N+1)]
            present = [x in r for x in word]
            count = sum(present)
            if count < d or present != [True]*count+[False]*(len(word)-count):
                continue
            if set(r) != marker | set(word[:count]):
                continue
            bits = tuple(r[x] for x in word[:count])
            candidates.append((a, f, bits[:d], bits[d:]))
    return candidates


def distance(x, y, side):
    return sum(min((a-b) % side, (b-a) % side) for a, b in zip(x, y))


def geometry(fault):
    cases = 0
    for d, N in ((1, 1), (2, 2), (1, 3)):
        M, n = d+N, 2*(d+N)+8
        a = (5*n-2, 5*n-1, 5*n-3)  # straddles periodic boundaries
        for f in ROTATIONS:
            for header in product((0, 1), repeat=d):
                for k in range(N+1):
                    for h in product((0, 1), repeat=k):
                        r = encode(a, f, d, header, h, n)
                        if fault == 'missing-marker':
                            del r[image((0, 0, 3), a, f, 5*n)]
                        # Reversed insertion order cannot carry hidden history.
                        parsed = decode(dict(reversed(list(r.items()))), d, N, n)
                        assert parsed == [(a, f, header, h)], ('parser', parsed)
                        assert len(r) == 7+d+k
                        if k < N:
                            target = image((2*(d+k+1), 4, 0), a, f, 5*n)
                            assert target not in r
                            assert max(distance(x, target, 5*n) for x in r) <= 10*M+35
                        cases += 1
    phase_cases = 0
    for a in product(range(5), repeat=3):
        r = encode(a, FRAME, 1, (0,), (1, 0), 14)
        assert decode(r, 1, 2, 14) == [(a, FRAME, (0,), (1, 0))]
        assert all(tuple(x % 5 for x in v) == a for v in r)
        phase_cases += 1
    return {'parser_cases': cases, 'phase_cases': phase_cases, 'proper_rotations': len(ROTATIONS),
            'tested_d_N': [[1, 1], [2, 2], [1, 3]], 'radius_bound': '10(d+N)+35'}


def algebra(fault):
    from sympy import Matrix, Rational as Q, I, eye, zeros, expand
    ident = eye(4)
    # Exact exponentials of the source B_L and B_R at cos(tau)=3/5.
    U_L = Matrix([[-Q(7,25),-I*Q(24,25),0,0],
                  [-I*Q(24,25),-Q(7,25),0,0],
                  [0,0,Q(3,5),-I*Q(4,5)],
                  [0,0,-I*Q(4,5),Q(3,5)]])
    S = Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    U_R = S*U_L*S
    assert U_L.H*U_L == ident and U_R.H*U_R == ident
    P_L = Matrix.diag(0,1,0,1)
    P_R = Matrix.diag(0,0,1,1)
    vectors = [eye(4)[:,j] for j in range(4)]
    comparisons = zero_children = 0
    fixtures = [(vectors[0],), (vectors[1],),
                ((vectors[0]+I*vectors[3])/2, (vectors[1]+vectors[2])/2)]
    for seed in fixtures:
        rho = sum((v*v.H for v in seed), zeros(4))
        assert rho.trace() == 1
        front = [((), rho, list(seed))]
        for depth in range(3):
            new = []
            U, P = ((U_L, P_L) if depth % 2 == 0 else (U_R, P_R))
            for h, sigma, ensemble in front:
                # Three equally likely hidden channels: one electric test,
                # two vacuum incident-edge tests. Six-edge multiplicities cancel.
                child_traces = []
                for b in (0,1):
                    gates = ([P, zeros(4), zeros(4)] if b else [ident-P, ident, ident])
                    moved = U*sigma*U.H
                    if fault == 'coherent-hidden':
                        T = sum(gates, zeros(4))
                        child = T*moved*T.H/3
                    else:
                        child = sum((T*moved*T.H for T in gates), zeros(4))/3
                    # Independent rank-one path propagation; weights remain exact.
                    next_vectors = [(T*U*v).applyfunc(expand) for v in ensemble for T in gates]
                    next_vectors = [v for v in next_vectors if v != zeros(4,1)]
                    reconstructed = sum((v*v.H for v in next_vectors), zeros(4))/(3**(depth+1))
                    child = child.applyfunc(expand)
                    reconstructed = reconstructed.applyfunc(expand)
                    assert child == reconstructed, ('density/ensemble', h, b)
                    comparisons += 1
                    child_traces.append(child.trace())
                    if child.trace() != 0:
                        new.append((h+(b,), child, next_vectors))
                    else:
                        zero_children += 1
                assert sum(child_traces) == sigma.trace()
            front = new
        assert sum(s.trace() for _,s,_ in front) == 1

    v0 = vectors[0]
    timing_before = (v0.H*P_L*v0)[0]/3
    timing_after = ((U_L*v0).H*P_L*(U_L*v0))[0]/3
    assert timing_before != timing_after
    # Same named outcomes, omitted chronological order: Z0,Y0 versus Y0,Z0.
    Z0 = Matrix([[1,0],[0,0]])
    Y0 = Matrix([[Q(1,2),-I/2],[I/2,Q(1,2)]])
    z = Matrix([1,0])
    values, masses = [], []
    for word in ((Z0,Y0),(Y0,Z0)):
        v = z
        for P in word:
            v = P*v
        mass = (v.H*v)[0]
        masses.append(str(mass))
        values.append(str((v.H*(eye(2)-Z0)*v)[0]/mass))
    assert values[0] != values[1]
    return {'density_ensemble_comparisons': comparisons, 'zero_children': zero_children,
            'horizon': 3, 'preparations': len(fixtures),
            'unrecorded_magnetic_evolution_corner_probabilities': [str(timing_before),str(timing_after)],
            'order_control_masses': masses, 'order_control_future_Z1': values,
            'scope': 'exact reduced gauge/control fixtures, not a many-body native simulation'}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--fault', choices=('missing-marker','coherent-hidden'))
    args = p.parse_args()
    for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
        assert os.environ.get(key) == '1', key
    resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    start = time.monotonic()
    def guard(_s,_f):
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss = rss if sys.platform == 'darwin' else rss*1024
        if time.monotonic()-start > 60 or rss > 270_000_000:
            raise RuntimeError('resource bound exceeded')
    signal.signal(signal.SIGALRM,guard)
    signal.setitimer(signal.ITIMER_REAL,0.2,0.2)
    result = {'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
              'geometry':geometry(args.fault),'algebra':algebra(args.fault)}
    result['elapsed_seconds'] = time.monotonic()-start
    result['max_rss_host_units'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result['status'] = 'ok'
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
