#!/usr/bin/env python3
"""Preregistered finite algebra and geometry, not a physical-model test."""
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import os
import re
import resource
import subprocess
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / 'checks/extcont_numeric.lock'
OUT = ROOT / 'checks/extcont_result.json'
THREADS = ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


report = {
    'kind': 'preregistered exact finite regression; no Yang-Mills verification',
    'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'criteria_sha256': sha(ROOT / 'checks/extcont_criteria.md'),
    'script_sha256': sha(Path(__file__)),
    'status': 'NOT_RUN', 'checks': [], 'resources': []}


class ResourceRefusal(RuntimeError):
    pass


def guard(label):
    if sys.platform != 'darwin':
        raise ResourceRefusal('Registered memory-free measurement requires macOS')
    proc = subprocess.run(['/usr/bin/memory_pressure', '-Q'], text=True,
                          capture_output=True, check=True)
    match = re.search(r'free percentage:\s*([0-9.]+)%', proc.stdout)
    if not match:
        raise ResourceRefusal('Cannot establish free memory')
    sample = {'label': label, 'load': list(os.getloadavg()),
              'free_percent': float(match.group(1)),
              'rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'nice': os.getpriority(os.PRIO_PROCESS, 0),
              'threads': {key: os.environ.get(key) for key in THREADS}}
    report['resources'].append(sample)
    if not (max(sample['load']) < 8 and sample['free_percent'] >= 30
            and sample['rss_bytes'] < 1_000_000_000 and sample['nice'] >= 10
            and all(v == '1' for v in sample['threads'].values())):
        raise ResourceRefusal('Resource guard failed: ' + json.dumps(sample))


def components(vertices, adj):
    unseen = set(vertices)
    result = []
    while unseen:
        todo = [min(unseen)]
        unseen.remove(todo[0])
        found = set(todo)
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w)
                    found.add(w)
                    todo.append(w)
        result.append(frozenset(found))
    return result


def saturation(support, active, vertices, adj):
    holes = components(set(vertices) - set(active), adj)
    touching = [h for h in holes if h & support or
                any(adj[v] & support for v in h)]
    filled = frozenset(set(support).union(*touching))
    return filled, sum(map(len, touching))


def iterative(support, active, vertices, adj):
    out = set(support)
    while True:
        added = {v for v in vertices if v not in active and
                 (v in out or adj[v] & out)}
        if added <= out:
            return frozenset(out)
        out.update(added)


def full_norm(records, vertices, active, active_weights=False, active_roots=False):
    roots = active if active_roots else vertices
    sums = {v: Q(0) for v in roots}
    for support, amplitude in records:
        n = len(support & active) if active_weights else len(support)
        weight = 2**n * abs(amplitude)
        for v in support:
            if v in sums:
                sums[v] += weight
    return max(sums.values(), default=Q(0)), sums


def graph(n, edges):
    adj = {i: set() for i in range(n)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return frozenset(range(n)), adj


def geometry():
    graphs = {
        'path6': graph(6, [(i, i+1) for i in range(5)]),
        'cycle6': graph(6, [(i, (i+1) % 6) for i in range(6)]),
        'grid2x3': graph(6, [(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)])}
    counts = Counter()
    worst = Q(0)
    for name, (vertices, adj) in graphs.items():
        supports = []
        for mask in range(1, 1 << len(vertices)):
            x = frozenset(v for v in vertices if mask & (1 << v))
            if len(components(x, adj)) == 1:
                supports.append((x, Q(1, 1+mask)))
        for active_mask in range(1 << len(vertices)):
            active = frozenset(v for v in vertices if active_mask & (1 << v))
            outputs = []
            for x, amplitude in supports:
                if x & active:
                    y, size = saturation(x, active, vertices, adj)
                    assert y == iterative(x, active, vertices, adj), (name, x, active)
                    assert y & active == x & active
                    assert x <= y and len(y)-len(x) <= size
                    output_amplitude = amplitude / 4**size
                    counts['saturation_identities'] += 1
                else:
                    y, output_amplitude = x, amplitude
                outputs.append((y, output_amplitude))
                input_one = full_norm([(x, amplitude)], vertices, active)[0]
                output_one = full_norm([(y, output_amplitude)], vertices, active)[0]
                assert output_one <= Q(11, 2)*input_one
                counts['single_support_bounds'] += 1
            norm_in = full_norm(supports, vertices, active)[0]
            norm_out = full_norm(outputs, vertices, active)[0]
            assert norm_out <= Q(11, 2)*norm_in, (name, active_mask, norm_out, norm_in)
            worst = max(worst, norm_out/norm_in)
            counts['whole_family_bounds'] += 1
        guard('geometry_' + name)
    return {'counts': dict(counts), 'maximum_observed_ratio': str(worst),
            'acceptance_bound': '11/2', 'jet_scope': 'arbitrary coefficient magnitudes; constant activities in this finite check'}


def norm_witnesses(norm_impl):
    vertices, adj = graph(4, [(0,1),(1,2),(2,3),(3,0)])
    active = frozenset({0})
    inp = [(frozenset({0}), Q(1))]
    out = [(saturation(inp[0][0], active, vertices, adj)[0], Q(1))]
    assert norm_impl(inp, vertices, active)[0] == 2, 'cycle4_input'
    assert norm_impl(out, vertices, active)[0] == 16, 'cycle4_full_output'
    assert full_norm(out, vertices, active, True, True)[0] == 2, 'cycle4_active_output'
    vertices, adj = graph(3, [(0,1),(1,2)])
    active = frozenset({0,2})
    inp = [(frozenset({0}), Q(1)), (frozenset({2}), Q(1))]
    out = [(saturation(x, active, vertices, adj)[0], amplitude) for x, amplitude in inp]
    assert norm_impl(inp, vertices, active)[0] == 2, 'path3_input'
    out_norm, roots = norm_impl(out, vertices, active)
    assert out_norm == 8, 'path3_full_output'
    assert roots[1] == 8, 'path3_inactive_root'


def mutations():
    norm_witnesses(full_norm)
    outcomes = []
    for name, mutant in [
        ('active_weights', lambda records, vertices, active:
         full_norm(records, vertices, active, active_weights=True)),
        ('inactive_roots_omitted', lambda records, vertices, active:
         full_norm(records, vertices, active, active_roots=True))]:
        try:
            norm_witnesses(mutant)
        except AssertionError as exc:
            outcomes.append({'mutation': name, 'status': 'REJECTED', 'witness': str(exc)})
        else:
            raise AssertionError('Mutation survived: ' + name)
    return {'baseline': 'PASS', 'mutations': outcomes}


def project(poly):
    return {key: val for key, val in poly.items() if key[0] <= 2 and val}


def source_derivative(poly, n):
    return {(r,c-n): val*factorial(c)/factorial(c-n)
            for (r,c),val in poly.items() if c >= n}


def dilation(poly, block, field_dimension=2):
    return {key: val * Q(block**4, block**(field_dimension*key[0]))
            for key, val in poly.items()}


def taylor():
    checks = 0
    for block in (3,5):
        for r in range(11):
            for c in range(5):
                poly = {(r,c): Q(1)}
                p = project(poly)
                assert project(p) == p
                remainder = {key: val for key,val in poly.items() if key not in p}
                assert not any(key[0] <= 2 for key in remainder)
                for s in range(5):
                    assert source_derivative(p, s) == project(source_derivative(poly, s))
                if r >= 3:
                    got = dilation(poly, block)[(r,c)]
                    assert got == Q(block**4, block**(2*r)) <= Q(1, block**2)
                checks += 1
    try:
        assert dilation({(3,0): Q(1)}, 3, 1)[(3,0)] <= Q(1,9)
    except AssertionError:
        mutation = 'REJECTED at degree three, L=3'
    else:
        raise AssertionError('Wrong scaling dimension survived')
    return {'monomials': checks, 'dimension_one_mutation': mutation,
            'scope': 'projection and coefficient scaling, not a nonlinear RG operator'}


def trim(poly):
    while len(poly)>1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(p, q):
    out = [0]*max(len(p),len(q))
    for i,v in enumerate(p): out[i] += v
    for i,v in enumerate(q): out[i] += v
    return trim(out)


def multiply(p,q):
    out = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): out[i+j] += a*b
    return trim(out)


def scale(p,c):
    return trim([a*c for a in p])


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n-1):
        yield p+((n,),)
        for i in range(len(p)):
            yield p[:i]+(p[i]+(n,),)+p[i+1:]


def bell():
    shapes = []
    m = []
    for n in range(11):
        counter = Counter(tuple(sorted(map(len,p))) for p in partitions(n))
        shapes.append(counter)
        coeff = [0]*(n+1)
        for shape,count in counter.items(): coeff[len(shape)] += count
        m.append(trim(coeff))
        if n in (5,10): guard('bell_partitions_' + str(n))
    inverse = [[1]]
    for n in range(1,11):
        result = [0]
        for r in range(1,n+1):
            result = add(result, scale(multiply(m[r], inverse[n-r]),comb(n,r)))
        inverse.append(result)
    partition_inverse = []
    for n in range(11):
        result = [0]
        for shape,count in shapes[n].items():
            term = [1]
            for size in shape: term = multiply(term,m[size])
            result = add(result,scale(term,count*factorial(len(shape))))
        partition_inverse.append(result)
    assert inverse == partition_inverse
    quotient = []
    for n in range(11):
        result = [0]
        for r in range(n+1):
            result = add(result,scale(multiply(m[r],inverse[n-r]),comb(n,r)))
        quotient.append(result)
    assert m[:5] == [[1],[0,1],[0,1,1],[0,1,3,1],[0,1,7,6,1]]
    assert inverse[:5] == [[1],[0,1],[0,1,3],[0,1,9,13],[0,1,21,78,75]]
    assert quotient[:5] == [[1],[0,2],[0,2,6],[0,2,18,26],[0,2,42,156,150]]
    for family in (m,inverse,quotient):
        assert all(poly[0] == 0 for poly in family[1:])
    return {'orders_checked': list(range(11)),
            'partitions_enumerated': sum(sum(c.values()) for c in shapes),
            'C4_coefficients_ascending': quotient[4],
            'C10_coefficients_ascending': quotient[10]}


def derivative_scaling():
    rows = []
    for n in (2,4,8):
        amplitude = Q(1,n**6)
        derivative_amplitude = amplitude*n**6
        assert derivative_amplitude == 1
        assert derivative_amplitude/amplitude == n**6
        rows.append({'n': n, 'value_amplitude': str(amplitude),
                     'sixth_derivative_amplitude': str(derivative_amplitude),
                     'sixth_T_term': str(derivative_amplitude/factorial(6)),
                     'ratio': n**6})
    return {'scaling_only_not_trigonometric_sampling': rows}


start = time.monotonic()
lock_owned = False
exit_code = 0
try:
    guard('initial')
    fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    lock_owned = True
    with os.fdopen(fd, 'w') as f:
        f.write(json.dumps({'pid':os.getpid(),'started_utc':report['started_utc']})+'\n')
    for name, fn in [('geometry_and_payment', geometry),
                     ('shared_norm_and_mutations', mutations),
                     ('taylor_projection_and_dilation', taylor),
                     ('ordered_jet_polynomials', bell),
                     ('value_to_derivative_diagnostic', derivative_scaling)]:
        guard('before_' + name)
        try:
            result = fn()
            report['checks'].append({'name':name,'status':'PASS','result':result})
        except AssertionError as exc:
            report['checks'].append({'name':name,'status':'FAIL','error':str(exc),
                                     'traceback':traceback.format_exc()})
            exit_code = 1
        guard('after_' + name)
    report['status'] = 'FAIL' if exit_code else 'PASS'
except ResourceRefusal as exc:
    report['status'] = 'STOPPED' if report['checks'] else 'NOT_RUN'
    report['reason'] = str(exc)
    exit_code = 2
except Exception as exc:
    report['status'] = 'ERROR'
    report['reason'] = str(exc)
    report['traceback'] = traceback.format_exc()
    exit_code = 3
finally:
    if lock_owned:
        LOCK.unlink()
    report['elapsed_seconds'] = time.monotonic()-start
    report['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    output = json.dumps(report,indent=2)+'\n'
    OUT.write_text(output)
    print(output,end='')
sys.exit(exit_code)
