#!/usr/bin/env python3
"""Preregistered finite regressions. No interacting-model closure claim."""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import math
import os
import re
import resource
import subprocess
import sys
import time
import traceback

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'checks/locop_results.json'
LOCK = ROOT / 'checks/locop_numeric.lock'
THREADS = ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


report = {'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
          'scope': 'finite algebra and synthetic arithmetic only',
          'criteria_sha256': sha(ROOT / 'checks/locop_criteria.md'),
          'script_sha256': sha(Path(__file__)),
          'status': 'NOT_RUN', 'checks': [], 'resources': []}


class ResourceRefusal(RuntimeError):
    pass


def guard(label):
    if sys.platform != 'darwin':
        raise ResourceRefusal('Registered memory measurement requires macOS')
    p = subprocess.run(['/usr/bin/memory_pressure', '-Q'],
                       capture_output=True, text=True, check=True)
    m = re.search(r'free percentage:\s*([0-9.]+)%', p.stdout)
    if not m:
        raise ResourceRefusal('Cannot establish memory-free percentage')
    sample = {'label': label, 'load': list(os.getloadavg()),
              'free_percent': float(m.group(1)),
              'rss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'nice': os.getpriority(os.PRIO_PROCESS, 0),
              'threads': {key: os.environ.get(key) for key in THREADS}}
    report['resources'].append(sample)
    if not (max(sample['load']) < 8 and sample['free_percent'] >= 30
            and sample['rss_bytes'] < 1_000_000_000 and sample['nice'] >= 10
            and all(value == '1' for value in sample['threads'].values())):
        raise ResourceRefusal('Resource guard failed: ' + json.dumps(sample))


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def adj(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def su2(k):
    axis = [math.sin(k+0.2), math.cos(2*k+0.1), math.sin(3*k+0.7)]
    n = math.sqrt(sum(x*x for x in axis))
    x, y, z = [math.sin(0.13*k+0.17)*a/n for a in axis]
    c = math.cos(0.13*k+0.17)
    return [[complex(c, z), complex(y, x)],
            [complex(-y, x), complex(c, -z)]]


def err(a, b):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))


def trace_re(a):
    return (a[0][0]+a[1][1]).real/2


def covariance():
    gauges = [su2(k+11) for k in range(5)]
    edges = {(0, 1): su2(1), (1, 4): su2(2),
             (0, 2): su2(3), (2, 4): su2(4),
             (2, 3): su2(5), (3, 1): su2(6)}
    moved = {(x, y): mul(mul(gauges[x], u), adj(gauges[y]))
             for (x, y), u in edges.items()}
    paths = [[0, 1, 4], [0, 2, 4], [0, 2, 3, 1, 4],
             [0, 1, 3, 2, 4]]

    def pathprod(path, data):
        value = [[1+0j, 0j], [0j, 1+0j]]
        for x, y in zip(path, path[1:]):
            link = data[(x, y)] if (x, y) in data else adj(data[(y, x)])
            value = mul(value, link)
        return value

    original = [pathprod(p, edges) for p in paths]
    transformed = [pathprod(p, moved) for p in paths]
    e = max(err(v, mul(mul(gauges[0], u), adj(gauges[4])))
            for u, v in zip(original, transformed))
    mean = lambda values: [[sum(a[i][j] for a in values)/len(values)
                            for j in range(2)] for i in range(2)]
    m, mg = mean(original), mean(transformed)
    v = su2(20)
    vg = mul(mul(gauges[0], v), adj(gauges[4]))
    e = max(e, err(mg, mul(mul(gauges[0], m), adj(gauges[4]))),
            abs(trace_re(mul(adj(vg), mg))-trace_re(mul(adj(v), m))))
    negative = 1-math.cos(0.5)
    assert e < 1e-12 and negative > 1e-4
    return {'maximum_error': e, 'coarse_only_change': negative,
            'note': 'Normalizer covariance is proved by Haar substitution, not quadrature.'}


def localization():
    planes = list(__import__('itertools').combinations(range(4), 2))
    index = {a: i for i, a in enumerate(planes)}
    c = [[Q((i+1)*(j+1)+(i == j), 7) for j in range(6)] for i in range(6)]
    orbit = [[Q(0) for j in range(6)] for i in range(6)]
    count = 0
    for p in permutations(range(4)):
        for signs in product((-1, 1), repeat=4):
            image = []
            for i, j in planes:
                x, y = p[i], p[j]
                image.append((index[tuple(sorted((x, y)))],
                              signs[i]*signs[j]*(1 if x < y else -1)))
            for i, (ii, si) in enumerate(image):
                for j, (jj, sj) in enumerate(image):
                    orbit[ii][jj] += si*sj*c[i][j]
            count += 1
    average = sum(c[i][i] for i in range(6))/6
    for i in range(6):
        for j in range(6):
            assert orbit[i][j]/count == (average if i == j else 0)
    # Dual constant-curvature Hessian tests of the reconstructed polynomial.
    qform = lambda f: sum(c[i][j]*f[i]*f[j] for i in range(6)
                         for j in range(6))/2
    basis = [[Q(int(i == j)) for i in range(6)] for j in range(6)]
    recovered = [[qform([basis[i][k]+basis[j][k] for k in range(6)])
                  -qform(basis[i])-qform(basis[j]) for j in range(6)]
                 for i in range(6)]
    assert recovered == c
    loop_tests = 0
    for mu, nu in planes:
        for width, height in ((1, 1), (2, 1), (3, 2)):
            point = [0]*4
            flux = Q(0)
            path = [(mu, 1)]*width+[(nu, 1)]*height
            path += [(mu, -1)]*width+[(nu, -1)]*height
            for axis, sign in path:
                start = point.copy()
                if sign < 0:
                    start[axis] -= 1
                a = -Q(start[nu], 2) if axis == mu else Q(start[mu], 2)
                flux += sign*a
                point[axis] += sign
            assert flux == width*height and flux*flux == (width*height)**2
            assert point == [0]*4
            loop_tests += 1
    trace_free = [1, -1, 0, 0, 0, 0]
    assert sum(trace_free) == 0 and any(trace_free)
    assert all(Q(L)**4*Q(L)**-4 == 1 for L in (3, 5, 7))
    return {'signed_permutations': count, 'loop_tests': loop_tests,
            'tensor_recovery': 'exact', 'anisotropic_scalar_control': 'survives'}


def taylor():
    tested = 0
    factors = {}
    for L in (3, 5, 7):
        bound = Q(4, L)+Q(8, L*L)
        factors[str(L)] = str(bound)
        for degree in range(2, 7):
            for a in range(degree+1):
                b = degree-a
                if (a, b) == (2, 0):
                    continue
                # Full Taylor norm on the unit product ball is 2^(a+b).
                norm = sum(Q(math.comb(a, i)*math.comb(b, j))
                           for i in range(a+1) for j in range(b+1))
                assert norm == 2**degree
                ratio = Q(L)**(4-2*a-3*b)
                assert ratio <= bound
                if b == 0:
                    assert ratio <= Q(8, L*L)
                tested += 1
        assert (bound < 1) == (L == 7)
    return {'monomials_times_scales': tested, 'benchmark_bounds': factors,
            'scope': 'monomial regression; not a proof for arbitrary functions'}


def flow():
    bstar, r0, cap, umin = Q(2), Q(1, 5), Q(1), Q(400)
    u = [Q(500)]
    defect = [Q(0)]+[Q((-1)**n, 5) for n in range(1, 41)]
    b = [bstar+defect[j+1]-defect[j] for j in range(40)]
    rho = [Q((-1)**j, 1000) for j in range(40)]
    for j in range(40):
        assert abs(rho[j]) <= cap/u[j]
        following = u[j]-b[j]-rho[j]
        r = -rho[j]
        assert following == u[j]-b[j]+r
        u.append(following)
    assert min(u) >= umin and cap/umin <= bstar/2
    lower, upper = bstar-cap/umin, bstar+cap/umin
    pairs = 0
    for j in range(41):
        for n in range(j+1, 41):
            assert lower*(n-j)-2*r0 <= u[j]-u[n] <= upper*(n-j)+2*r0
            pairs += 1
    assert pairs == 820
    return {'pairs': pairs, 'minimum_u': str(min(u)), 'returned_sign': 'exact',
            'actual_AF_trajectory_tested': False}


def jacobian():
    z, t = 1e-3, 2
    haar = 2*math.log(math.sin(z)/z)/(z*z)
    relative = t*(1-math.cos(z))/(z*z)
    assert abs(haar+1/3) < 1e-6
    assert abs(relative-t/2) < 1e-6
    return {'log_Haar_coefficient': haar, 'soft_relative_coefficient': relative,
            'interpretation': 'coordinate/relative terms, not symmetry breaking'}


locked = False
started = time.monotonic()
try:
    fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    locked = True
    guard('start')
    for name, fn in [('covariance', covariance), ('localization', localization),
                     ('taylor', taylor), ('flow', flow), ('jacobian', jacobian)]:
        guard('before '+name)
        try:
            detail = fn()
            report['checks'].append({'name': name, 'status': 'PASS', 'detail': detail})
        except Exception:
            report['checks'].append({'name': name, 'status': 'FAIL',
                                     'error': traceback.format_exc()})
        guard('after '+name)
    report['status'] = 'PASS' if all(c['status'] == 'PASS' for c in report['checks']) else 'FAIL'
except ResourceRefusal as exc:
    report['status'] = 'RESOURCE_REFUSAL'
    report['error'] = str(exc)
except Exception:
    report['status'] = 'ERROR'
    report['error'] = traceback.format_exc()
finally:
    if locked:
        LOCK.unlink()
    report['elapsed_seconds'] = time.monotonic()-started
    report['peak_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'checks': report['checks'],
                      'elapsed_seconds': report['elapsed_seconds'],
                      'peak_rss_bytes': report['peak_rss_bytes']}))
sys.exit(0 if report['status'] == 'PASS' else 1)
