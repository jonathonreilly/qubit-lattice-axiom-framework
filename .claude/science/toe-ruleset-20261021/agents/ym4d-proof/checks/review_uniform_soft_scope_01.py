#!/usr/bin/env python3
"""Actual SU(2) S4-prime finite-u normalized-kernel scope control."""
import itertools
from collections import Counter
import json
import sys
import time
import traceback
import mpmath as mp

mp.mp.dps = 80
start = time.time()
checks = []
details = {}

def record(name, ok, **extra):
    checks.append(dict(name=name, passed=bool(ok), **extra))

def path(start, end, order):
    pos = list(start)
    result = []
    for mu in order:
        while pos[mu] != end[mu]:
            step = 1 if pos[mu] < end[mu] else -1
            old = tuple(pos)
            pos[mu] += step
            result.append((old, tuple(pos), mu, step))
    return result

def reverse(edges):
    return [(end, start, mu, -step) for start, end, mu, step in reversed(edges)]

def field_integral(edges):
    ans = 0
    for start, end, mu, step in edges:
        base = start if step > 0 else end
        if mu == 0 and base == (0, 1, 0, 0):
            ans += step
    return ans

def lam(pos):
    x = [p % 9 for p in pos]
    return x[0] + x[0]*x[1] + 2*x[2] - x[3]**3

def class_integral(x, moment=False):
    fun = lambda theta: mp.sin(theta)**2 * mp.exp(x*(mp.cos(theta)-1)) * (mp.cos(theta) if moment else 1)
    return (2/mp.pi)*mp.quad(fun, [0, mp.pi/8, mp.pi/2, mp.pi])

def logZ(x):
    return x + mp.log(class_integral(x))

def main():
    contours = []
    origin = (0, 0, 0, 0)
    endpoint = (3, 0, 0, 0)
    for order in itertools.permutations(range(4)):
        for y in itertools.product((-1, 0, 1), repeat=4):
            shifted = (y[0]+3, y[1], y[2], y[3])
            contours.append(path(origin, y, order) + path(y, shifted, [0]) + reverse(path(endpoint, shifted, order)))
    angles = [field_integral(c) for c in contours]
    hist = Counter(angles)
    count = len(angles)
    mean = mp.mpf(sum(angles))/count
    variance = mp.mpf(sum(x*x for x in angles))/count - mean**2
    gradients = [sum(lam(end)-lam(start) for start, end, _, _ in c) for c in contours]
    constants = [sum(step for _, _, mu, step in c if mu == 0) for c in contours]
    record('all_actual_S4prime_contours_counted', count == 24*81, count=count)
    record('predeclared_actual_link_has_nonzero_spread', 0 in hist and 1 in hist and variance > 0, histogram={str(k):v for k,v in sorted(hist.items())}, mean=str(mean), variance=str(variance))
    record('actual_periodic_gradient_has_zero_spread', set(gradients) == {lam(endpoint)-lam(origin)}, endpoint_difference=lam(endpoint)-lam(origin))
    record('actual_constant_link_has_zero_spread', set(constants) == {3}, value=3)
    def pathmean(epsilon):
        return sum(mp.mpf(n)*mp.exp(1j*epsilon*x) for x,n in hist.items())/count
    results = []
    for t in map(mp.mpf, ['.5', '2', '8', '32']):
        c = class_integral(t, moment=True)/class_integral(t)
        z0 = logZ(t)
        record(f'finite_t_{t}_coefficient_strictly_between_zero_and_one', 0 < c < 1, c=float(c))
        for delta in map(mp.mpf, ['0', '.3']):
            b = mean+delta
            expected = t*(delta**2 + (1-c)*variance)
            finite = []
            tree = []
            for h in [mp.mpf(1)/1000, mp.mpf(1)/2000]:
                m = pathmean(h)
                trace_value = mp.re(mp.exp(-1j*h*b)*m)
                difference = t*(1-trace_value)+logZ(t*abs(m))-z0
                phase = abs(m)-trace_value
                finite.append(2*difference/h**2)
                tree.append(2*phase/h**2)
            richardson = (4*finite[1]-finite[0])/3
            tree_richardson = (4*tree[1]-tree[0])/3
            error = abs(richardson-expected)
            name = f't{t}_residual{delta}'
            record(name+'_finite_u_actual_kernel_hessian', error < mp.mpf('1e-8'), error=float(error), expected=float(expected), observed=float(richardson))
            record(name+'_tree_phase_hessian', abs(tree_richardson-delta**2) < mp.mpf('1e-8'), error=float(abs(tree_richardson-delta**2)), expected=float(delta**2), observed=float(tree_richardson))
            if not delta:
                record(name+'_finite_u_equals_tree_mutation_rejected', abs(richardson) > mp.mpf('1e-6'), discrepancy=float(abs(richardson)))
            results.append(dict(t=str(t),linear_residual=str(delta),c=str(c),variance=str(variance),expected_hessian=str(expected),hessian_estimators=[str(x) for x in finite],richardson=str(richardson),tree_estimators=[str(x) for x in tree],tree_richardson=str(tree_richardson),error=str(error)))
    asymptotic = []
    for t in map(mp.mpf, ['64', '256', '1024']):
        c = class_integral(t, moment=True)/class_integral(t)
        value = t*(1-c)
        asymptotic.append(dict(t=int(t),coefficient=str(value),error_to_three_halves=float(abs(value-mp.mpf('1.5')))))
    errors = [x['error_to_three_halves'] for x in asymptotic]
    record('SU2_large_t_asymptotic_corroboration', errors[0] > errors[1] > errors[2] and errors[2] < .005, samples=asymptotic)
    details.update(contours=count,group='SU(2)',dimension=4,L=3,coarse_link_direction=0,fine_edge=[[0,1,0,0],[1,1,0,0]],trace_convention='Re tr / 2; generator i diag(1,-1) has norm one',precision_decimal_digits=mp.mp.dps,quadrature='direct SU(2) Haar class integration; stabilized exponent x(cos(theta)-1)',results=results)

exception = None
try:
    main()
except Exception:
    exception = traceback.format_exc()
    traceback.print_exc()
print(json.dumps(dict(schema='review-uniform-soft-scope-independent-v1',passed=sum(c['passed'] for c in checks),total=len(checks),checks=checks,details=details,exception=exception,elapsed_seconds=time.time()-start,scope='One actual S4-prime SU(2) link kernel at finite t; does not establish depth-uniform finite-u estimates.',author_helpers_imported=False),indent=2))
sys.exit(0 if exception is None and all(c['passed'] for c in checks) else 1)
