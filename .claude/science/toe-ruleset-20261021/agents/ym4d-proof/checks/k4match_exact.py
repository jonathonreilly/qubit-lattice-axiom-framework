#!/usr/bin/env python3
"""Registered exact algebra checks; no Yang--Mills coefficient evaluation."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, prod
from pathlib import Path
from functools import lru_cache
import datetime
import fcntl
import hashlib
import json
import os
import re
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
THREADS = ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
           'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS')
RECORDS = []
GUARDS = []
START = time.monotonic()
CAP = 800 * 1024**2


def guard():
    output = subprocess.check_output(['/usr/bin/memory_pressure', '-Q'], text=True)
    free = int(re.search(r'free percentage:\s*(\d+)%', output).group(1))
    loads = os.getloadavg()
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != 'darwin':
        peak *= 1024
    item = dict(loads=loads, free_percent=free, peak_rss_bytes=peak,
                elapsed_seconds=time.monotonic()-START)
    GUARDS.append(item)
    assert max(loads) < 8 and free >= 30, item
    assert peak < CAP and item['elapsed_seconds'] < 90, item


def check(name, condition, **data):
    RECORDS.append(dict(name=name, passed=bool(condition), **data))
    assert condition, name


@lru_cache(None)
def partitions(labels):
    if not labels:
        return ((),)
    first, rest = labels[0], labels[1:]
    out = []
    for p in partitions(rest):
        out.append(((first,),)+p)
        for j in range(len(p)):
            out.append(p[:j]+((first,)+p[j],)+p[j+1:])
    return tuple(out)


def cumulant(moment, labels):
    return sum((F((-1)**(len(p)-1)*factorial(len(p)-1)) *
                prod(moment(b) for b in p) for p in partitions(tuple(labels))), F(0))


def table_moment(table, labels):
    return sum((weight*prod(row[i] for i in labels) for weight, row in table), F(0))


def free_and_partitions():
    a = 96*(F(1,81)+F(1,256)+F(1,20736))
    check('free_normalization', a == F(169,108) and a/144 == F(169,15552),
          A_point=a, R_point_one_colour=a/144)
    check('smooth_support_margins',
          F(3,2) < F(9971,6480) < F(10309,6480) < F(5,3)
          and 11 < 12*F(2500,2501)**8 < 12*F(2500,2499)**8 < 13)
    counts = {}
    for p in partitions((0,1,2,3)):
        shape = '+'.join(map(str, sorted(map(len,p), reverse=True)))
        counts[shape] = counts.get(shape,0)+1
    check('partition_counts', counts == {'4':1,'3+1':4,'2+2':3,
                                        '2+1+1':6,'1+1+1+1':1}, counts=counts)
    rows = [(-2,1,3,0),(1,0,-1,2),(2,3,1,-2),
            (0,2,-2,1),(3,-1,0,2),(-1,2,4,3)]
    table = [(F(j+1,21),r) for j,r in enumerate(rows)]
    groups = [table[:3],table[3:]]
    masses = [sum(w for w,_ in t) for t in groups]
    groups = [[(w/m,r) for w,r in t] for m,t in zip(masses,groups)]
    lhs = cumulant(lambda b:table_moment(table,b), range(4))
    rhs = F(0)
    family = {}
    for p in partitions((0,1,2,3)):
        outer = [(mass,tuple(cumulant(lambda q:table_moment(t,q),b) for b in p))
                 for mass,t in zip(masses,groups)]
        term = cumulant(lambda q:table_moment(outer,q), range(len(p)))
        rhs += term
        shape = '+'.join(map(str,sorted(map(len,p),reverse=True)))
        family[shape] = family.get(shape,F(0))+term
    check('total_cumulance_rational_table', lhs == rhs, lhs=lhs, rhs=rhs, families=family)
    et = F(1+3,2)
    et2 = F(1+9,2)
    k4 = 3*et2-3*et**2
    check('conditional_covariance_mutation_detected', k4 == 3 and k4 != 0,
          full=k4, omit_two_plus_two=0)
    for t in (F(-1,2),F(0),F(1,2)):
        table = [(F(1,16)*(1+t*prod(x)),x) for x in product((-1,1),repeat=4)]
        proper = [table_moment(table,b) for n in range(1,4)
                  for b in combinations(range(4),n)]
        check('pair_data_do_not_fix_k4_'+str(t),
              all(v == 0 for v in proper) and
              cumulant(lambda b:table_moment(table,b),range(4)) == t)


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matsum(matrices):
    return [[sum(a[i][j] for a in matrices) for j in range(2)] for i in range(2)]


def cycles():
    slices = [[[F(2),F(1)],[F(1),F(1)]],
              [[F(1,2),F(-1,2)],[F(-1,2),F(1)]],
              [[F(1),F(1,3)],[F(1,3),F(2,3)]]]
    weights = [[[F(a),F(0)],[F(0),F(b)]] for a,b in ((1,2),(2,1),(1,3),(3,1))]
    orderings = ((0,1,2,3),(0,1,3,2),(0,2,1,3))
    def cycle(order,edges):
        z = [[F(1),F(0)],[F(0),F(1)]]
        for vertex,edge in zip(order,edges):
            z = matmul(matmul(z,weights[vertex]),edge)
        return z[0][0]+z[1][1]
    def poly(g):
        return 16*sum(cycle(c,[g]*4) for c in orderings)
    increments = [poly(matsum(slices[i:]))-poly(matsum(slices[i+1:])) for i in range(3)]
    allocated = [F(0)]*3
    for assignment in product(range(3),repeat=4):
        allocated[min(assignment)] += 16*sum(cycle(c,[slices[j] for j in assignment]) for c in orderings)
    full = poly(matsum(slices))
    wrong = sum(poly(g) for g in slices)
    check('mixed_slice_cycle_telescoping', increments == allocated and sum(increments) == full,
          increments=increments, allocated=allocated, full=full)
    check('same_slice_mutation_detected', wrong != full, same_slice_only=wrong)


def padd(a,b):
    n = max(len(a),len(b))
    return tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n))


def pscale(a,c):
    return tuple(c*v for v in a)


def pmul(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def gm(p):
    def wick(n):
        return 0 if n%2 else prod(range(1,n,2))
    return sum(c*wick(n) for n,c in enumerate(p))


def pcum(polys):
    def moment(labels):
        out = (F(1),)
        for i in labels:
            out = pmul(out,polys[i])
        return gm(out)
    return cumulant(moment,range(len(polys)))


def smul(a,b):
    return tuple(sum(a[i]*b[n-i] for i in range(n+1)) for n in range(3))


def spmul(a,b):
    out = []
    for n in range(3):
        z = (F(0),)
        for i in range(n+1):
            z = padd(z,pmul(a[i],b[n-i]))
        out.append(z)
    return tuple(out)


def perturbation():
    zero, one = (F(0),), (F(1),)
    obs = []
    for j in range(1,5):
        obs.append(((F(j-1),F(0),F(j)),
                    (F(0),F(j,5),F(0),F(j+1,7)),
                    (F(0),F(0),F(j,13),F(0),F(5-j,11))))
    v1 = (F(0),F(0),F(0),F(1,7))
    v2 = (F(0),F(0),F(1,13),F(0),F(1,11))
    weight = (one,pscale(v1,-1),padd(pscale(pmul(v1,v1),F(1,2)),pscale(v2,-1)))
    denominator = tuple(gm(p) for p in weight)
    inv = (F(1),-denominator[1],denominator[1]**2-denominator[2])
    def moments(labels):
        p = (one,zero,zero)
        for i in labels:
            p = spmul(p,obs[i])
        p = spmul(p,weight)
        return smul(tuple(gm(q) for q in p),inv)
    def direct(labels):
        out = [F(0)]*3
        for partition in partitions(tuple(labels)):
            z = (F(1),F(0),F(0))
            for block in partition:
                z = smul(z,moments(block))
            factor = (-1)**(len(partition)-1)*factorial(len(partition)-1)
            out = [a+factor*b for a,b in zip(out,z)]
        return out
    for labels in ((1,2),(0,1,2,3)):
        base = [obs[i][0] for i in labels]
        a = sum(pcum([obs[j][2] if j == i else obs[j][0] for j in labels]) for i in labels)
        b = sum(pcum([obs[j][1] if j in pair else obs[j][0] for j in labels])
                for pair in combinations(labels,2))
        c = -sum(pcum([obs[j][1] if j == i else obs[j][0] for j in labels]+[v1]) for i in labels)
        d = -pcum(base+[v2])
        e = F(1,2)*pcum(base+[v1,v1])
        exact = direct(labels)
        check('perturbative_formula_order_'+str(len(labels)),
              exact[0] == pcum(base) and exact[1] == 0 and exact[2] == a+b+c+d+e,
              direct=exact, families=[a,b,c,d,e], scope='formal polynomial control, not YM')
        check('double_cubic_mutation_order_'+str(len(labels)), exact[2] != a+b+c+d)


def normalization():
    check('running_log_coefficients', -4-2*(-2) == 0)
    for x in (F(0),F(1,16),F(1,8),F(1,4)):
        check('exact_running_ratio_'+str(x), (1+x)**(-4)/((1+x)**(-2))**2 == 1)
    for z in (F(-2,3),F(0),F(3,7)):
        a,b = F(5,11),F(-2,13)
        check('common_field_factor_'+str(z), (a+4*z)-2*(b+2*z) == a-2*b)
    lo,hi = F(3,4)/F(5,4)**2,F(5,4)/F(3,4)**2
    check('noncancellation_exact_margins', lo == F(12,25) and hi == F(20,9)
          and lo*F(3,338) == F(18,4225), lower=lo, upper=hi,
          lower_times_d=F(18,4225))
    grid = (F(-1,4),F(-1,8),F(0),F(1,8),F(1,4))
    for a,b in product(grid,repeat=2):
        r = (1+a)/(1+b)**2
        check('ratio_grid_'+str(a)+'_'+str(b), lo<=r<=hi and
              abs(r-1)<=(abs(a)+2*abs(b)+b*b)/(1-abs(b))**2)
    for mask in range(16):
        projection = sum((-1)**(4-j.bit_count()) for j in range(16) if mask & ~j == 0)
        check('four_support_projection_'+str(mask), projection == (1 if mask==15 else 0))


def main():
    report = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  scope='exact algebra only; actual YM coefficient sign and uniform matching OPEN',
                  criteria_sha256=hashlib.sha256((HERE/'k4match_criteria.md').read_bytes()).hexdigest(),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  nice=os.getpriority(os.PRIO_PROCESS,0),
                  threads={k:os.environ.get(k) for k in THREADS}, passed=False)
    locks = []
    try:
        assert report['nice'] >= 10
        assert all(os.environ.get(k)=='1' for k in THREADS)
        assert os.environ.get('K4MATCH_WATCHDOG') == '1', 'RSS watchdog required'
        signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(RuntimeError('90-second guard')))
        signal.setitimer(signal.ITIMER_REAL,90)
        report['rss_enforcement'] = 'external 800 MiB combined-RSS watchdog plus self checks'
        for name,mode in (('k4match_numeric.lock','a+'),('cumul_numeric.lock','r'),('combo_numeric.lock','r')):
            lock = (HERE/name).open(mode)
            locks.append(lock)
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        report['locks'] = [str(p.name) for p in locks]
        guard()
        for fn in (free_and_partitions,cycles,perturbation,normalization):
            fn()
            guard()
        report['passed'] = all(r['passed'] for r in RECORDS)
    except BaseException as exc:
        report['failure'] = repr(exc)
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        for lock in reversed(locks):
            lock.close()
    report.update(checks=RECORDS,guards=GUARDS,check_count=len(RECORDS),
                  elapsed_seconds=time.monotonic()-START)
    print(json.dumps(report,indent=2,default=str))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
