#!/usr/bin/env python3
"""Independent rational interval and polynomial controls; no author imports."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import datetime as dt
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import time

import mpmath as mp
import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent.parent
RUN = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/quantum/direct_reflection')
S = 10**45


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def floor_q(x):
    return x.numerator // x.denominator


def ceil_q(x):
    return -((-x.numerator) // x.denominator)


class I:
    # Fraction endpoints, outward projection to a different decimal scale.
    def __init__(self, lo, hi=None):
        lo = Q(lo)
        hi = lo if hi is None else Q(hi)
        assert lo <= hi
        self.lo = Q(floor_q(lo*S), S)
        self.hi = Q(ceil_q(hi*S), S)

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = self.cast(other)
        return I(self.lo+other.lo, self.hi+other.hi)
    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        other = self.cast(other)
        corners = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(corners), max(corners))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.cast(other)
        assert other.lo > 0
        corners = [x/y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(min(corners), max(corners))


def atan_bracket(x, n):
    total = Q(0)
    power = x
    for j in range(n):
        total += (-1)**j * power / (2*j+1)
        power *= x*x
    adjacent = total + (-1)**n * power / (2*n+1)
    return min(total, adjacent), max(total, adjacent)


def pi_box():
    low5, high5 = atan_bracket(Q(1, 5), 60)
    low239, high239 = atan_bracket(Q(1, 239), 18)
    # Exact tangent calculation for Machin's identity.
    tan_four = (2*Q(5,12))/(1-Q(5,12)**2)
    assert (tan_four-Q(1,239))/(1+tan_four*Q(1,239)) == 1
    out = I(16*low5-4*high239, 16*high5-4*low239)
    assert 3 < out.lo < out.hi < Q(22,7)
    return out


def atanh_box(x):
    assert 0 < x.lo <= x.hi < Q(71,100)
    power, total = x, I(0)
    for j in range(180):
        total += power / (2*j+1)
        power = power*x*x
    # Uniform rational positive-series tail, independent of computed endpoints.
    r = Q(71,100)
    tail = r**361 / (361*(1-r*r))
    return total + I(0, tail)


def k_box():
    root_floor = math.isqrt(2*S*S)
    assert root_floor*root_floor < 2*S*S < (root_floor+1)**2
    root = I(Q(root_floor,S), Q(root_floor+1,S))
    out = root*(atanh_box(I(1)/root)-atanh_box(I(Q(1,2))))
    assert 0 < out.lo < out.hi < Q(1,2)
    return out


def sincos_box(x):
    assert 0 < x.lo <= x.hi < Q(8,5)
    squared = x*x
    sine_term, sine = x, x
    cosine_term, cosine = I(1), I(1)
    for j in range(1,17):
        sine_term = -sine_term*squared/((2*j)*(2*j+1))
        sine += sine_term
        cosine_term = -cosine_term*squared/((2*j-1)*(2*j))
        cosine += cosine_term
    sine_remainder = Q(8,5)**35 / math.factorial(35)
    cosine_remainder = Q(8,5)**34 / math.factorial(34)
    return sine+I(-sine_remainder,sine_remainder), cosine+I(-cosine_remainder,cosine_remainder)


def exp_box(x):
    assert 0 <= x.lo <= x.hi < 1
    total, term = I(1), I(1)
    for j in range(1,33):
        term = term*x/j
        total += term
    return total+I(0,Q(3,math.factorial(33)))


def rat(x):
    x = Q(x)
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator),
            'decimal': mp.nstr(mp.mpf(x.numerator)/x.denominator, 60)}


def read_rat(x):
    return Q(int(x['numerator']), int(x['denominator']))


def symbolic_bounds():
    u,t,theta,c = sy.symbols('u t theta c', real=True)
    g = (u+t)/(1+u*t)
    identities = [sy.simplify(sy.diff(g,u)-(1-t*t)/(1+u*t)**2),
                  sy.simplify(sy.diff(g,t)-(1-u*u)/(1+u*t)**2),
                  sy.simplify(sy.diff(g,u,2)+2*t*(1-t*t)/(1+u*t)**3),
                  sy.simplify(sy.diff(g,t,2)+2*u*(1-u*u)/(1+u*t)**3),
                  sy.simplify(sy.diff(g,u,t)+2*(u+t)/(1+u*t)**3)]
    assert all(x == 0 for x in identities)
    p3 = (5*c**3-3*c)/2
    h = p3.subs(c,sy.cos(theta))*sy.sin(theta)
    explicit = sy.diff(p3,c,2).subs(c,sy.cos(theta))*sy.sin(theta)**3 \
               - 3*sy.diff(p3,c).subs(c,sy.cos(theta))*sy.sin(theta)*sy.cos(theta) \
               - p3.subs(c,sy.cos(theta))*sy.sin(theta)
    assert sy.trigsimp(sy.diff(h,theta,2)-explicit) == 0
    g_second_bound = 2*Q(2,3)**2+8*Q(2,3)*Q(1,2)+4*Q(1,2)**2+Q(1,2)
    product_second_bound = g_second_bound+2*Q(7,6)*7+25
    assert g_second_bound == Q(91,18)
    assert product_second_bound == Q(835,18) < 48
    return {'partial_derivative_identities_checked': len(identities),
            'H_second_derivative_identity_checked': True,
            'g_second_derivative_upper': rat(g_second_bound),
            'gH_second_derivative_upper': rat(product_second_bound)}


def controls():
    nodes, weights = np.polynomial.legendre.leggauss(4)
    azimuth = 2*np.pi*np.arange(9)/9
    directions = np.array([[math.sqrt(1-z*z)*math.cos(phi),math.sqrt(1-z*z)*math.sin(phi),z]
                            for z in nodes for phi in azimuth])
    p = np.repeat(weights/18,9)
    c = directions@directions.T
    np.fill_diagonal(c,1.)
    p3 = (5*c**3-3*c)/2
    root = np.sqrt(p)
    projection = 7*root[:,None]*p3*root[None,:]
    reflection = np.eye(len(p))-2*projection
    projector_error = float(np.max(np.abs(projection@projection-projection)))
    reflection_error = float(np.max(np.abs(reflection@reflection-np.eye(len(p)))))
    assert projector_error < 3e-14 and reflection_error < 5e-14
    def witness(correlation):
        return -float(np.dot(p,np.diag(correlation)))+14*float(np.einsum('i,j,ij,ij',p,p,p3,correlation))
    eta, visibility = .25,.75
    values = {'cosine_quantum_saturation':witness(-c),
              'degree3_positive_quantum_saturation':witness(p3),
              'normalized_signed_polynomial':witness(-visibility*((1+eta)*c-eta*p3)),
              'unnormalized_signed_polynomial':witness(-visibility*(c-eta*p3))}
    expected = {'cosine_quantum_saturation':1.,'degree3_positive_quantum_saturation':1.,
                'normalized_signed_polynomial':1.125,'unnormalized_signed_polynomial':.9375}
    for key in values:
        assert abs(values[key]-expected[key]) < 5e-14
    z=sy.symbols('z')
    P3=(5*z**3-3*z)/2
    assert sy.integrate(z*P3,(z,-1,1)) == 0
    assert sy.integrate(P3*P3,(z,-1,1)) == sy.Rational(2,7)
    return {'settings':len(p),'projector_error':projector_error,'reflection_square_error':reflection_error,
            'computed':values,'independent_exact_expected':expected}


def certificate(n, author):
    pi, k = pi_box(), k_box()
    total = I(0)
    for j in range(n):
        theta = pi*Q(2*j+1,4*n)
        sine,c = sincos_box(theta)
        u=Q(2*n-(2*j+1),2*n)
        q=exp_box(2*k*c)
        g=((1+u)*q-(1-u))/((1+u)*q+(1-u))
        # Different association for the degree-three polynomial.
        P3=c*(5*c*c-3)/2
        total += g*P3*sine
    estimate=7*pi*total/(2*n)
    error=Q(14)*Q(11,7)**3/(n*n)
    assert error == read_rat(author['quadrature_error_upper'])
    interval=(estimate.lo-error,estimate.hi+error)
    original=(read_rat(author['a3_interval'][0]),read_rat(author['a3_interval'][1]))
    original_k=tuple(read_rat(x) for x in author['k_exact_interval'])
    assert original_k[0] <= k.lo <= k.hi <= original_k[1]
    assert original[0] <= interval[0] < interval[1] <= original[1] < 0
    witnesses=[]
    J=Q(111,20)
    for row in author['witnesses']:
        V=read_rat(row['V'])
        low, high=V*(1-2*interval[1]),V*(1-2*interval[0])
        author_low,author_high=map(read_rat,row['B_interval'])
        assert author_low <= low <= high <= author_high
        gap=author_low-1
        N=None
        if gap>0:
            threshold=40*J*J/(gap*gap)
            N=ceil_q(threshold)
            assert N == row['N_for_each_error_at_most_one_percent_using_ln100_lt_5']
            assert N*gap*gap >= 40*J*J > (N-1)*gap*gap
        witnesses.append({'V':rat(V),'independent_B_interval':[rat(low),rat(high)],
                          'author_certified_gap_lower':rat(gap),'sample_bound_reproduced':N})
    e5_lower=sum((Q(5)**j/math.factorial(j) for j in range(12)),Q(0))
    assert e5_lower>100
    absolute_integral=2*(Q(9,40)+(Q(9,40)-Q(1,8)))
    assert absolute_integral == Q(13,20)
    assert 1+7*absolute_integral==J
    assert Q(20,111)*J==1
    assert Q(91,111)*J*Q(20,13)==7
    return {'scale':str(S),'atanh_terms':180,'sine_highest_degree':33,
            'cosine_highest_degree':32,'exp_highest_degree':32,
            'panels':n,'k_interval':[rat(k.lo),rat(k.hi)],
            'midpoint_estimate_interval':[rat(estimate.lo),rat(estimate.hi)],
            'quadrature_error_upper':rat(error),'independent_a3_interval':[rat(x) for x in interval],
            'independent_interval_nested_in_author_interval':True,
            'witnesses':witnesses,'absolute_P3_integral':rat(absolute_integral),
            'total_absolute_weight':rat(J),'exp5_positive_partial_sum':rat(e5_lower),
            'sampling_coefficients_checked_exactly':True}


def main():
    start=time.time()
    mp.mp.dps=70
    author=json.loads((RUN/'RESULTS_v1.json').read_text())
    freeze=json.loads((RUN/'FREEZE.json').read_text())
    files={name:sha(HERE/name) for name in freeze['source_hashes']}
    assert files == freeze['source_hashes'] == author['source_hashes']
    freeze_sha=sha(RUN/'FREEZE.json')
    results_sha=sha(RUN/'RESULTS_v1.json')
    assert freeze_sha==author['freeze_sha256']
    derivatives=symbolic_bounds()
    polynomial=controls()
    result=certificate(freeze['panels'],author)
    assert files=={name:sha(HERE/name) for name in files}
    data={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':sha(__file__),
          'reviewed_sources':files,'freeze_sha256':freeze_sha,'author_results_sha256':results_sha,
          'symbolic_bounds':derivatives,'polynomial_controls':polynomial,
          'independent_certificate':result,'elapsed_seconds':time.time()-start,
          'required_alternative_error_premise':'E[Z_i | past] >= 1+Delta for every included trial; an unconditional mean alone is insufficient.',
          'limits':'Scoped conditional mathematics and arithmetic check. No apparatus, observed data, original sphere classification, novelty or formal audit disposition.'}
    out=RUN/'independent_reflection_review/CHECKS_v1.json'
    assert not out.exists()
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))


if __name__=='__main__':
    main()
