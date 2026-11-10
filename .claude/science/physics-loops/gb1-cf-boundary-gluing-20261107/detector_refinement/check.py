#!/usr/bin/env python3
"""Exact finite diagnostic of the selected neighborhood detector.

Integer payload v represents the scalar matrix v I, not an orthogonal qubit
state. This emitter executes a local parser; the separate checker reconstructs
a global prefix graph without importing this module. No external scientific
input is read. The source is read once for its provenance hash.
"""
import argparse
from collections import defaultdict, deque
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

RADIUS = 16
ALPHABET = (0, 1, 2, 3, 4, 100, 101, 102, 103)
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
HEADER = {(0, 0, 0): 100, (1, 0, 0): 101,
          (0, 1, 0): 102, (0, 0, 1): 103}
PREP, FINE, COARSE = (2, 0, 0), (0, 8, 0), (0, 9, 0)
POOL = tuple((2+j % 4, 8+(j//4) % 2, j//8) for j in range(16))
POOL_INDEX = {x: j for j, x in enumerate(POOL)}


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def determinant(v):
    a, b, c = v
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def world(x, origin, axes):
    return tuple(origin[k]+sum(x[j]*axes[j][k] for j in range(3))
                 for k in range(3))


def proper_frames():
    result = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            axes = tuple(tuple(signs[j] if k == perm[j] else 0
                               for k in range(3)) for j in range(3))
            if determinant(axes) == 1:
                result.append(axes)
    return sorted(result)


def geometry(records):
    by_tag = {tag: [x for x, value in records.items() if value == tag]
              for tag in range(100, 104)}
    if any(len(xs) != 1 for xs in by_tag.values()):
        return None
    a = by_tag[100][0]
    axes = tuple(sub(by_tag[101+j][0], a) for j in range(3))
    if any(sum(abs(v) for v in axis) != 1 for axis in axes):
        return None
    if determinant(axes) != 1:
        return None
    return a, axes


def make_seed(columns, selector, groups, origin=(0, 0, 0), axes=IDENTITY):
    r = dict(HEADER)
    r[PREP] = selector
    for t, col in enumerate(columns):
        for i, value in enumerate(col):
            r[(2+i, 2+t, 0)] = value
    for i, flag in enumerate(groups):
        r[(2+i, 6, 0)] = flag
    assert len(r) == 25
    return {world(x, origin, axes): value for x, value in r.items()}


def parse(eta, q, fault):
    geom = geometry(eta)
    if geom is None:
        return None
    a, axes = geom
    if fault == 'preferred-frame' and axes != IDENTITY:
        return None
    body = {tuple(dot(sub(x, a), axis) for axis in axes): value
            for x, value in eta.items()}
    s = body.get(PREP)
    if s not in range(4):
        return None
    columns = []
    for t in range(4):
        col = tuple(body.get((2+i, 2+t, 0)) for i in range(4))
        if any(n not in range(5) for n in col) or sum(col) != 4:
            return None
        columns.append(col)
    groups = tuple(body.get((2+i, 6, 0)) for i in range(4))
    if any(g not in (0, 1) for g in groups):
        return None
    seed = make_seed(columns, s, groups)
    if any(body.get(x) != value for x, value in seed.items()):
        return None
    extra = {x: value for x, value in body.items() if x not in seed}
    blocks = tuple(i for i, n in enumerate(columns[s]) for _ in range(n**q))
    if not extra:
        return a, axes, 0, blocks, groups, None
    race = [(POOL_INDEX[x], value) for x, value in extra.items()
            if x in POOL_INDEX]
    if len(race) != 1:
        return None
    j, value = race[0]
    if j >= len(blocks) or value != 1:
        return None
    expected = {POOL[j]: 1}
    if extra == expected:
        return a, axes, 1, blocks, groups, j
    expected[FINE] = blocks[j]+1
    if extra == expected:
        return a, axes, 2, blocks, groups, j
    # Terminals and all malformed/holey contexts are not enabling predecessors.
    return None


def local_query(x, records, q, fault='none'):
    eta = {y: value for y, value in records.items()
           if y != x and sum(abs(a-b) for a, b in zip(y, x)) <= RADIUS}
    parsed = parse(eta, q, fault)
    content = None
    if parsed is not None:
        origin, axes, phase, blocks, groups, winner = parsed
        center = tuple(dot(sub(x, origin), axis) for axis in axes)
        j = POOL_INDEX.get(center)
        if phase == 0 and j is not None and j < len(blocks):
            content = 1
        elif (fault == 'reopen-race' and phase == 1 and j is not None
              and j < len(blocks) and j != winner):
            content = 1
        elif phase == 1 and center == FINE:
            content = blocks[winner]+1
        elif phase == 2 and center == COARSE:
            content = groups[blocks[winner]]
            if fault == 'wrong-group':
                content = 1-content
    if content is not None:
        return content, {content: F(1)}
    k, l = len(eta), sum(v == 1 for v in eta.values())
    p = F(1+2*l, 2*(1+k))
    law = {v: F(1, 18) for v in ALPHABET}
    law[1] += p/2
    law[0] += (1-p)/2
    assert sum(law.values()) == 1 and all(w > 0 for w in law.values())
    return None, law


def encode(records):
    return [[list(x), value] for x, value in sorted(records.items())]


def key(records):
    return tuple(sorted(records.items()))


def candidate_sites(records):
    # Derived from actual header records, not an external target mask.
    geom = geometry(records)
    if geom is None:
        return ()
    a, axes = geom
    return tuple(world(x, a, axes) for x in POOL+(FINE, COARSE))


def emit_case(name, q, seed, fault):
    todo, seen, nodes = deque([seed]), set(), []
    while todo:
        records = todo.popleft()
        if key(records) in seen:
            continue
        seen.add(key(records))
        events = []
        for x in candidate_sites(records):
            if x in records:
                continue
            content, law = local_query(x, records, q, fault)
            if content is None:
                continue
            assert law == {content: F(1)}
            events.append({'site': list(x), 'content': content, 'rate': [1, 1]})
            child = dict(records)
            child[x] = content
            todo.append(child)
        support = []
        for x, value in sorted(records.items()):
            _, law = local_query(x, records, q, fault)
            mass = law.get(value, F(0))
            support.append({'site': list(x), 'p_content': [mass.numerator, mass.denominator]})
        nodes.append({'records': encode(records), 'events': events, 'support': support})
    return {'name': name, 'q': q, 'seed': encode(seed), 'nodes': nodes}


def case_bank(small):
    bank = []
    if not small:
        for a, b, c in product(range(5), repeat=3):
            d = 4-a-b-c
            if d < 0:
                continue
            col = (a, b, c, d)
            columns = (col, (4, 0, 0, 0), (4, 0, 0, 0), (4, 0, 0, 0))
            for q in (1, 2):
                bank.append((f'composition_{a}{b}{c}{d}_q{q}', q,
                             make_seed(columns, 0, (1, 1, 0, 0))))
    frames = proper_frames() if not small else [IDENTITY, proper_frames()[0]]
    for j, axes in enumerate(frames):
        origins = ((0, 0, 0), (7, -5, 3)) if not small else ((7, -5, 3),)
        for t, origin in enumerate(origins):
            for q in (1, 2):
                bank.append((f'orbit_{j}_{t}_q{q}', q,
                             make_seed(((1, 1, 2, 0),)*4, 0,
                                       (1, 1, 0, 0), origin, axes)))
    for q in (1, 2):
        bank.append((f'direct_q{q}', q,
                     make_seed(((2, 2, 0, 0),)*4, 0, (1, 0, 0, 0))))
        bank.append((f'refined_q{q}', q,
                     make_seed(((1, 1, 2, 0),)*4, 0, (1, 1, 0, 0))))
        columns = ((4, 0, 0, 0), (4, 0, 0, 0), (0, 4, 0, 0), (0, 4, 0, 0))
        for s in range(4):
            bank.append((f'tomography_s{s}_q{q}', q,
                         make_seed(columns, s, (1, 0, 0, 0))))
    return bank


def terminal_distribution(case):
    seed = {tuple(x): value for x, value in case['seed']}
    origin, axes = geometry(seed)
    fp, cp = world(FINE, origin, axes), world(COARSE, origin, axes)
    masses = defaultdict(F)
    masses[key(seed)] = F(1)
    terminal = defaultdict(F)
    for node in sorted(case['nodes'], key=lambda node: len(node['records'])):
        records = {tuple(x): value for x, value in node['records']}
        mass = masses[key(records)]
        if not node['events']:
            terminal[(records.get(fp), records.get(cp))] += mass
        else:
            total = sum(F(*event['rate']) for event in node['events'])
            for event in node['events']:
                child = dict(records)
                child[tuple(event['site'])] = event['content']
                masses[key(child)] += mass*F(*event['rate'])/total
    return terminal


def terminal_law(case):
    terminal = terminal_distribution(case)
    return {str(k): str(v) for k, v in sorted(terminal.items(), key=lambda kv: str(kv[0]))}


def finite_diagonal_checks(responses):
    effects = list(product(range(5), repeat=2))
    pairs = 0
    for e in effects:
        for f in effects:
            if all(a+b <= 4 for a, b in zip(e, f)):
                columns = tuple((e[s], f[s], 4-e[s]-f[s], 0) for s in range(2))
                for s in range(2):
                    fine_mass = sum(F(columns[s][i], sum(columns[s])) for i in (0, 1))
                    coarse_weights = (e[s]+f[s], 4-e[s]-f[s])
                    assert fine_mass == F(coarse_weights[0], sum(coarse_weights))
                pairs += 1
    # Candidate Pauli tomography uses the emitted process responses, not a target table.
    scalar = (responses[0]+responses[1])/2
    z = (responses[0]-responses[1])/2
    x, y = responses[2]-scalar, responses[3]-scalar
    determinant_e = scalar**2-x**2-y**2-z**2
    return {'diagonal_effects': len(effects), 'summable_pairs': pairs,
            'tomography_coefficients': [str(a) for a in (scalar, x, y, z)],
            'tomography_determinant': str(determinant_e),
            'scope': 'exact finite arithmetic, not an M2 physical calibration'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--small', action='store_true')
    ap.add_argument('--fault', choices=['none', 'reopen-race', 'wrong-group', 'preferred-frame'], default='none')
    args = ap.parse_args()
    cases = [emit_case(name, q, seed, args.fault) for name, q, seed in case_bank(args.small)]
    cert = {'schema': 'detector-refinement-v1',
            'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': cases}
    Path(args.certificate).write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    selected = {case['name']: terminal_law(case) for case in cases
                if case['name'].startswith(('direct_', 'refined_', 'tomography_'))}
    by_name = {case['name']: case for case in cases}
    responses = tuple(sum((mass for (fine, coarse), mass in
                           terminal_distribution(by_name[f'tomography_s{s}_q1']).items()
                           if coarse == 1), F(0)) for s in range(4))
    print(json.dumps({'status': 'emitted; independent validation required', 'fault': args.fault,
                      'cases': len(cases), 'states': sum(len(c['nodes']) for c in cases),
                      'support_entries': sum(len(n['support']) for c in cases for n in c['nodes']),
                      'terminal_laws': selected, 'finite_diagonal_checks': finite_diagonal_checks(responses)}, indent=2))


if __name__ == '__main__':
    main()
