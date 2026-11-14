#!/usr/bin/env python3
"""Preregistered finite controls; no actual RG/locality estimate is tested."""
from fractions import Fraction as F
from pathlib import Path
import fcntl
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

ROOT = Path(__file__).resolve().parent
THREADS = ('OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'OMP_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS', 'BLIS_NUM_THREADS')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


report = dict(started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
              criteria_sha256=sha(ROOT / 'spurion_criteria.md'),
              script_sha256=sha(Path(__file__)), status='NOT_RUN', checks=[],
              resources=[], scope='Finite algebra and SU(2) radial quadrature only')


class Refusal(RuntimeError):
    pass


def guard(label):
    if sys.platform != 'darwin':
        raise Refusal('Registered memory measurement requires macOS')
    p = subprocess.run(['/usr/bin/memory_pressure', '-Q'], capture_output=True,
                       text=True, check=True)
    m = re.search(r'free percentage:\s*([0-9.]+)%', p.stdout)
    if not m:
        raise Refusal('No memory-free measurement')
    sample = dict(label=label, load=list(os.getloadavg()),
                  free_percent=float(m.group(1)),
                  rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  nice=os.getpriority(os.PRIO_PROCESS, 0),
                  threads={k: os.environ.get(k) for k in THREADS})
    report['resources'].append(sample)
    if not (max(sample['load']) < 8 and sample['free_percent'] >= 30
            and sample['rss_bytes'] < 1_000_000_000 and sample['nice'] >= 10
            and all(v == '1' for v in sample['threads'].values())):
        raise Refusal(json.dumps(sample))


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


I = [[1+0j, 0j], [0j, 1+0j]]


def su2(angle, axis):
    norm = math.sqrt(sum(x*x for x in axis))
    x, y, z = [math.sin(angle)*v/norm for v in axis]
    c = math.cos(angle)
    return [[complex(c, z), complex(y, x)], [complex(-y, x), complex(c, -z)]]


def err(a, b):
    return max(abs(x-y) for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def tr(a):
    return (a[0][0]+a[1][1]).real/2


def log_su2(a):
    theta = math.acos(max(-1.0, min(1.0, tr(a))))
    scale = theta/math.sin(theta) if theta > 1e-12 else 1.0
    return [[scale*(a[i][j]-tr(a)*I[i][j]) for j in range(2)] for i in range(2)]


def covariance():
    t = su2(.31, (1, 2, 3))
    v = su2(.47, (-2, 1, 1))
    a, b = su2(.71, (1, 0, 1)), su2(.83, (0, 2, 1))
    tg, vg = mul(mul(a, t), adj(b)), mul(mul(a, v), adj(b))
    r, rg = mul(v, adj(t)), mul(vg, adj(tg))
    maximum = max(abs(tr(r)-tr(rg)), err(log_su2(rg),
                  mul(mul(a, log_su2(r)), adj(a))))
    control = abs(tr(mul(vg, adj(t)))-tr(r))
    assert maximum < 1e-11 and control > 1e-4
    return dict(maximum_error=maximum, one_field_only_change=control)


def haar_z(r, n=2048):
    # Probability Haar on SU(2)=S^3: (2/pi) sin(theta)^2 dtheta.
    h = math.pi/n
    z = dz = 0.0
    for i in range(n+1):
        theta = i*h
        w = (1 if i in (0, n) else (4 if i % 2 else 2))
        v = math.sin(theta)**2 * math.exp(r*math.cos(theta))
        z += w*v
        dz += w*v*math.cos(theta)
    return z*h*2/(3*math.pi), dz*h*2/(3*math.pi)


def haar_reader():
    t, s = 2., 3.
    errors = []
    for r in (0., t, s, t+s):
        z0, dz0 = haar_z(r, 1024)
        z1, dz1 = haar_z(r, 2048)
        errors.extend((abs(z0-z1), abs(dz0/z0-dz1/z1)))
    assert abs(haar_z(0)[0]-1) < 1e-10 and max(errors) < 1e-10
    z, dz = haar_z(t+s)
    coefficient = t*s/(t+s)*dz/z
    delta = 1e-3
    radius = math.sqrt(t*t+s*s+2*t*s*math.cos(delta))
    second_difference = 2*(math.log(z)-math.log(haar_z(radius)[0]))/delta**2
    relerr = abs(second_difference/coefficient-1)
    reader_integral = z/(haar_z(t)[0]*haar_z(s)[0])
    assert relerr < 1e-5 and coefficient > .1 and abs(reader_integral-1) > .01
    return dict(refinement_error=max(errors), relative_hessian=coefficient,
                centered_difference=second_difference, relative_error=relerr,
                normalized_two_kernel_reader_integral=reader_integral,
                note='Analytic Haar formula and its positivity are proved in SPURION.md')


def gaussian():
    # H=diag(0,h), Q=I, T=diag(t,t), exact block Schur complement.
    t, h, mass = F(3), F(5), F(2)
    output = [t-t*t/t, t-t*t/(h+t)]
    mutation = t-t*t/(mass+t)
    assert output == [F(0), F(15, 8)] and t > 0 and mutation == F(6, 5)
    return dict(output_diagonal=list(map(str, output)),
                frozen_input_output_hessian=str(t), mass_mutation=str(mutation))


def tree_projector():
    u01, u12, u02 = su2(.2, (1, 0, 1)), su2(.3, (0, 1, 1)), su2(.4, (1, 1, 0))
    transports = [I, u01, mul(u01, u12)]
    # g_v is the root-to-v tree product for U_xy -> g_x U_xy g_y^-1.
    fixed01 = mul(mul(transports[0], u01), adj(transports[1]))
    fixed12 = mul(mul(transports[1], u12), adj(transports[2]))
    loop = mul(u02, adj(transports[2]))
    reconstructed02 = mul(loop, transports[2])
    e = max(err(fixed01, I), err(fixed12, I), err(reconstructed02, u02))
    assert e < 1e-11
    probe = {(0, 0): F(2), (1, 0): F(3), (0, 2): F(5), (2, 2): F(7),
             (3, 2): F(11), (0, 6): F(13)}
    project = lambda p: {k: v for k, v in p.items() if sum(k) <= 4}
    assert project(project(probe)) == project(probe)
    assert (3, 2) not in project(probe) and probe[(3, 2)] == 11
    return dict(tree_reconstruction_error=e, retained_monomials=len(project(probe)),
                remainder_degree_five=str(probe[(3, 2)]),
                note='Polynomial algebra is a coordinate regression, not an RG bound')


def readers():
    kernel = (F(1, 4), F(3, 4))
    reader = (F(2), F(4))
    unread = sum(kernel)
    selected = [kernel[i]*reader[i] for i in range(2)]
    full = sum(selected)
    assert unread == 1 and full == F(7, 2) and full != unread
    assert sum(selected) == sum(k*h for k, h in zip(kernel, reader))
    assert sum(selected[i]/full for i in range(2)) == 1
    return dict(unread=str(unread), reader_integral=str(full),
                selected_masses=list(map(str, selected)))


def main():
    with (ROOT/'spurion_numeric.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise Refusal('Lane numeric lock occupied') from exc
        guard('before')
        for name, fun in [('covariance', covariance), ('haar_reader', haar_reader),
                          ('gaussian_schur', gaussian), ('tree_projector', tree_projector),
                          ('complete_readers', readers)]:
            try:
                report['checks'].append(dict(name=name, status='PASS', result=fun()))
            except Exception:
                report['checks'].append(dict(name=name, status='FAIL', error=traceback.format_exc()))
            guard('after '+name)
        report['status'] = 'FAIL' if any(c['status']=='FAIL' for c in report['checks']) else 'PASS'


try:
    main()
except Refusal as exc:
    report['status'] = 'RESOURCE_REFUSAL' if report['checks'] else 'NOT_RUN'
    report['reason'] = str(exc)
except Exception:
    report['status'] = 'FAIL'
    report['error'] = traceback.format_exc()
finally:
    report['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    (ROOT/'spurion_results.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
sys.exit(0 if report['status']=='PASS' else 1)
