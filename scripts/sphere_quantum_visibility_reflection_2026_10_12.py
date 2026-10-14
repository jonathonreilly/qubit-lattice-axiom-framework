#!/usr/bin/env python3
"""Conditional sphere-quantum criterion controls and exact reflection certificate.

The continuum theorem is proved in the paired note. The rational certificate
has explicit analytic remainders; floating controls do not prove the theorem.
No observational data or external scientific file is read by this runner.
The cache envelope binds the paired note as a package integrity input.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_key] = '1'

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/SPHERE_QUANTUM_VISIBILITY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md',
)

import argparse
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction as F
import mpmath as mp
import numpy as np
from scipy.special import roots_legendre

SCALE = 10**40
PANELS = 2048
COUNTS = [0, 0]
CHECKS = []


def rat(x):
    x = F(x)
    with localcontext() as ctx:
        ctx.prec = 45
        value = str(Decimal(x.numerator) / Decimal(x.denominator))
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator), 'decimal': value}


def check(name, condition, detail=None):
    ok = bool(condition)
    COUNTS[0 if ok else 1] += 1
    CHECKS.append({'name': name, 'passed': ok, 'detail': detail})


def atan_fraction_interval(x, terms):
    s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    other=s+(-1)**terms*x**(2*terms+1)/F(2*terms+1)
    return min(s,other),max(s,other)

def pi_interval():
    lo5,hi5=atan_fraction_interval(F(1,5),50)
    lo239,hi239=atan_fraction_interval(F(1,239),12)
    # tan(4 atan(1/5) - atan(1/239))=1, with the angle in(0,pi/2).
    return 16*lo5-4*hi239,16*hi5-4*lo239

class IV:
    """Closed fixed-point interval [lo/SCALE,hi/SCALE], outward operations."""
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        assert lo<=hi
        self.lo=int(lo); self.hi=int(hi)
    @staticmethod
    def bounds(lo,hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        return IV((lo.numerator*SCALE)//lo.denominator,-((-hi.numerator*SCALE)//hi.denominator))
    @staticmethod
    def coerce(x):
        return x if isinstance(x,IV) else IV.bounds(x)
    def __add__(self,other):
        o=self.coerce(other); return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,other): return self+(-self.coerce(other))
    def __rsub__(self,other): return self.coerce(other)+(-self)
    def __mul__(self,other):
        o=self.coerce(other)
        products=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return IV(min(products)//SCALE,-((-max(products))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.coerce(other); assert o.lo>0, 'Only positive denominator intervals are used'
        values=(F(self.lo*SCALE,o.lo),F(self.lo*SCALE,o.hi),F(self.hi*SCALE,o.lo),F(self.hi*SCALE,o.hi))
        low=min(values); high=max(values)
        return IV(low.numerator//low.denominator,-((-high.numerator)//high.denominator))
    def rationals(self): return F(self.lo,SCALE),F(self.hi,SCALE)

def polynomial(x, coefficients):
    ans=IV.bounds(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]): ans=ans*x+coefficient
    return ans

SIN_COEFF=[F((-1)**j,math.factorial(2*j+1)) for j in range(13)]
COS_COEFF=[F((-1)**j,math.factorial(2*j)) for j in range(13)]
EXP_COEFF=[F(1,math.factorial(j)) for j in range(25)]

def sincos_interval(x):
    # For0<=x<=pi/2<2, Lagrange remainders after the next zero term.
    x2=x*x
    sin= x*polynomial(x2,SIN_COEFF)+IV.bounds(-F(2**27,math.factorial(27)),F(2**27,math.factorial(27)))
    cos= polynomial(x2,COS_COEFF)+IV.bounds(-F(2**26,math.factorial(26)),F(2**26,math.factorial(26)))
    return sin,cos

def exp_interval(x):
    # 0<=x<1 and e<3; all omitted positive Taylor terms total <=3/25!.
    assert 0<=x.lo and x.hi<SCALE
    return polynomial(x,EXP_COEFF)+IV.bounds(0,F(3,math.factorial(25)))


def atanh_interval(x, n=140):
    assert 0 <= x.lo <= x.hi < SCALE
    power = x
    total = IV.bounds(0)
    for j in range(n):
        total += power / F(2*j+1)
        power = power*x*x
    upper = F(x.hi, SCALE)
    tail = upper**(2*n+1) / (F(2*n+1)*(1-upper*upper))
    return total + IV.bounds(0, tail)


def exact_k_interval():
    root_floor = math.isqrt(2*SCALE*SCALE)
    assert root_floor**2 < 2*SCALE*SCALE < (root_floor+1)**2
    root = IV.bounds(F(root_floor, SCALE), F(root_floor+1, SCALE))
    return root*(atanh_interval(IV.bounds(1)/root)-atanh_interval(IV.bounds(F(1, 2))))


def certificate():
    pilo, pihi = pi_interval()
    assert 3 < pilo < pihi < F(22, 7)
    pi = IV.bounds(pilo, pihi)
    k = exact_k_interval()
    assert 0 < k.lo < k.hi < SCALE//2
    total = IV.bounds(0)
    for j in range(PANELS):
        theta = pi*F(2*j+1, 4*PANELS)
        sine, c = sincos_interval(theta)
        u = 1-F(2*j+1, 2*PANELS)
        exponential = exp_interval(2*k*c)
        g = ((1+u)*exponential-(1-u))/((1+u)*exponential+(1-u))
        p3 = (5*c*c*c-3*c)/2
        total += g*p3*sine
    low, high = (7*pi*F(1, 2*PANELS)*total).rationals()
    error = F(7*48*11**3, 24*7**3*PANELS*PANELS)
    return k, (low-error, high+error), error


def arithmetic_controls():
    checks = []
    for a, b in ((F(-7, 3), F(2, 7)), (F(0), F(11, 6)), (F(2, 9), F(13, 7))):
        x = IV.bounds(a, b)
        for c, d in ((F(1, 7), F(5, 3)), (F(3, 4), F(5, 4))):
            y = IV.bounds(c, d)
            for computed, exact in ((x+y, [a+c, b+d]),
                                    (x*y, [a*c, a*d, b*c, b*d]),
                                    (x/y, [a/c, a/d, b/c, b/d])):
                lo, hi = computed.rationals()
                checks.append(lo <= min(exact) <= max(exact) <= hi)
    check('outward_rational_arithmetic', all(checks), {'predicates': len(checks)})
    mp.mp.dps = 65
    pilo, pihi = pi_interval()
    value = lambda q: mp.mpf(q.numerator)/q.denominator
    trans = [value(pilo) < mp.pi < value(pihi)]
    for t in (F(0), F(1, 9), F(3, 4), F(3, 2)):
        sine, cosine = sincos_interval(IV.bounds(t))
        for v, reference in ((sine, mp.sin(value(t))), (cosine, mp.cos(value(t)))):
            lo, hi = v.rationals()
            trans.append(value(lo) <= reference <= value(hi))
    for t in (F(0), F(1, 3), F(9, 10)):
        lo, hi = exp_interval(IV.bounds(t)).rationals()
        trans.append(value(lo) <= mp.exp(value(t)) <= value(hi))
    check('transcendental_numerical_controls', all(trans), 'Numerical consistency only; rational remainders are in the proof.')


def sphere_grid(order, azimuths):
    z, w = roots_legendre(order)
    phi = 2*np.pi*np.arange(azimuths)/azimuths
    a = np.array([[np.sqrt(1-t*t)*np.cos(p), np.sqrt(1-t*t)*np.sin(p), t]
                  for t in z for p in phi])
    return a, np.repeat(w/(2*azimuths), azimuths)


def reflection_controls():
    a, weights = sphere_grid(4, 9)
    dots = a@a.T
    p3 = (5*dots**3-3*dots)/2
    q = 7*np.sqrt(weights[:, None]*weights[None, :])*p3
    s = np.eye(len(weights))-2*q
    err = max(np.max(abs(q@q-q)), np.max(abs(s@s-np.eye(len(weights)))))
    check('harmonic_projection_reflection', err < 2e-13, {'max_error': float(err)})
    def observed(table):
        return -np.dot(weights, np.diag(table))+14*np.sum(weights[:, None]*weights[None, :]*p3*table)
    eta, v = .25, .75
    values = [observed(-dots), observed(-p3),
              observed(-v*((1+eta)*dots-eta*p3)), observed(-v*(dots-eta*p3))]
    exact = [1, -1, float(F(9, 8)), float(F(15, 16))]
    check('reflection_diagonal_and_multiplicity', max(abs(x-y) for x, y in zip(values, exact)) < 2e-13,
          {'computed': values, 'independent_polynomial_values': exact})


def signed_sector_controls():
    # Explicit finite realization for f=P0/4+P1-P2/4, threshold V=2/3.
    ident = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], complex)
    y = np.array([[0, -1j], [1j, 0]], complex)
    z = np.diag([1., -1.]).astype(complex)
    gamma = [np.kron(x, ident), np.kron(y, ident), np.kron(z, x), np.kron(z, y), np.kron(z, z)]
    def operators(a):
        ax, ay, az = a
        w = np.array([np.sqrt(3)*ay*az, np.sqrt(3)*az*ax, np.sqrt(3)*ax*ay,
                      np.sqrt(3)/2*(ax*ax-ay*ay), (3*az*az-1)/2])
        return [z, ax*x+ay*y+az*z, sum(t*g for t, g in zip(w, gamma))]
    directions, weights = sphere_grid(3, 7)
    spectrum = np.linalg.eigvalsh(np.sqrt(weights[:, None]*weights[None, :])
        *(.25+directions@directions.T-.25*(3*(directions@directions.T)**2-1)/2))
    check('signed_polynomial_trace_norm', abs(sum(abs(spectrum))-1.5) < 2e-13,
          {'computed_trace_norm': float(sum(abs(spectrum))), 'exact': '3/2'})
    maximum = 0.
    for visibility in (F(1, 2), F(2, 3)):
        masses = [float(visibility/4), float(visibility), float(visibility/4)]
        leftover = float(1-visibility*F(3, 2))
        psi = np.zeros((10, 10), complex)
        for start, size, mass in zip((0, 2, 4), (2, 2, 4), masses):
            psi[start:start+size, start:start+size] = np.eye(size)*np.sqrt(mass/size)
        psi[8:10, 8:10] = np.ones((2, 2))*np.sqrt(leftover)/2
        families = []
        for a in directions[:5]:
            aa = np.zeros((10, 10), complex)
            bb = aa.copy()
            for start, size, sign, op in zip((0, 2, 4), (2, 2, 4), (1, 1, -1), operators(a)):
                aa[start:start+size, start:start+size] = op
                bb[start:start+size, start:start+size] = -sign*op.T
            aa[8:10, 8:10] = z
            bb[8:10, 8:10] = z
            maximum = max(maximum, np.max(abs(aa@aa-np.eye(10))), np.max(abs(bb@bb-np.eye(10))),
                          abs(np.vdot(psi, aa@psi)), abs(np.vdot(psi, psi@bb.T)))
            families.append((aa, bb))
        for i, (aa, _) in enumerate(families):
            for j, (_, bb) in enumerate(families):
                c = float(directions[i]@directions[j])
                expected = -float(visibility)*(.25+c-.25*(3*c*c-1)/2)
                maximum = max(maximum, abs(np.vdot(psi, aa@psi@bb.T)-expected))
        maximum = max(maximum, abs(np.vdot(psi, psi)-1))
    check('one_state_signed_clifford_sectors', maximum < 2e-13, {'max_error': float(maximum)})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', action='store_true', help='Emit deterministic JSON to stdout; writes no files.')
    args = parser.parse_args()
    arithmetic_controls()
    reflection_controls()
    signed_sector_controls()
    k, (lo, hi), error = certificate()
    mp.mp.dps = 65
    km = mp.sqrt(2)*(mp.atanh(1/mp.sqrt(2))-mp.atanh(mp.mpf('0.5')))
    def integrand(theta):
        u = 1-2*theta/mp.pi
        t = mp.tanh(km*mp.cos(theta))
        c = mp.cos(theta)
        return 7*(u+t)/(1+u*t)*(5*c**3-3*c)/2*mp.sin(theta)
    numerical = mp.quad(integrand, [0, mp.pi/4, mp.pi/2])
    value = lambda q: mp.mpf(q.numerator)/q.denominator
    kl, kh = k.rationals()
    check('degree_three_exact_enclosure', lo < hi < 0 and value(lo) < numerical < value(hi)
          and value(kl) < km < value(kh) and error == F(1331, 102760448),
          {'a3_exact_interval': [rat(lo), rat(hi)], 'a3_numerical_only': str(numerical),
           'k_interval': [rat(kl), rat(kh)], 'quadrature_error': rat(error)})
    primitive_root = F(5, 8)*F(3, 5)**2-F(3, 4)*F(3, 5)
    absolute = 2*(-primitive_root+F(-1, 8)-primitive_root)
    j = 1+7*absolute
    pdiagonal, psphere = F(20, 111), F(91, 111)
    ln_upper_ok = sum((F(5)**n/F(math.factorial(n)) for n in range(12)), F(0)) > 100
    check('sampling_density_and_weight', absolute == F(13, 20) and j == F(111, 20)
          and pdiagonal+psphere == 1 and pdiagonal*j == 1
          and psphere*j*F(20, 13) == 7 and ln_upper_ok,
          {'integral_abs_P3': rat(absolute), 'range_bound': rat(j)})
    rows = []
    for v in (F(9, 10), F(19, 20), F(1)):
        blo, bhi = v*(1-2*hi), v*(1-2*lo)
        gap = blo-1
        n = None
        if gap > 0:
            need = 40*j*j/(gap*gap)
            n = -(-need.numerator//need.denominator)
            assert F(n-1) < need <= n
        rows.append({'visibility': rat(v), 'B_interval': [rat(blo), rat(bhi)], 'sample_bound': n})
    check('witness_and_conditional_error_bound',
          rows[0]['sample_bound'] is None and rows[1]['sample_bound'] == 469373
          and rows[2]['sample_bound'] == 108502 and F(19, 20)*(1-2*hi) > F(1051, 1000), rows)
    result = {'scope': 'Conditional continuum theorem controls and exact reflection certificate; no empirical data.',
              'panels': PANELS, 'checks': CHECKS, 'pass': COUNTS[0], 'fail': COUNTS[1]}
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for row in CHECKS:
            print(('PASS ' if row['passed'] else 'FAIL ')+row['name']+': '+json.dumps(row['detail'], sort_keys=True))
        print(f'TOTAL: PASS={COUNTS[0]} FAIL={COUNTS[1]}')
    raise SystemExit(bool(COUNTS[1]))


if __name__ == '__main__':
    main()
