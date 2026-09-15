"""Exact counts and high precision weighted checks, personal author only."""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp


def coefficient_power(coefficients,power,order):
    result=[mp.mpf(1)]+[mp.mpf(0)]*order
    for _ in range(power):
        result=[sum(result[j]*coefficients[k-j] for j in range(k+1)) for k in range(order+1)]
    return result[order]


def main():
    mp.mp.dps=60
    checks=[];error=mp.mpf(0)
    for n in range(2,8):
        degree_hist={}
        for word in itertools.product(range(n),repeat=n-2):
            degrees=[1+word.count(v) for v in range(n)]
            product=math.prod(math.factorial(d) for d in degrees)
            degree_hist[product]=degree_hist.get(product,0)+1
        assert sum(degree_hist.values())==n**(n-2)
        for theta in [mp.mpf(0),mp.mpf('.5'),mp.mpf('.75')]:
            actual=sum(count*mp.mpf(product)**theta for product,count in degree_hist.items())
            coefficients=[mp.mpf(math.factorial(k+1))**theta/math.factorial(k) for k in range(n-1)]
            predicted=math.factorial(n-2)*coefficient_power(coefficients,n,n-2)
            error=max(error,abs(actual-predicted)/max(1,abs(actual)))
            checks.append(dict(n=n,theta=str(theta),weighted_count=mp.nstr(actual,25)))
    assert error<mp.mpf('1e-55')
    rational=[]
    for k in range(16):
        numerator=(k+1)**3*1000**4;denominator=math.factorial(k)
        ceil=math.isqrt(math.isqrt(numerator//denominator))
        while ceil**4*denominator<numerator:ceil+=1
        assert ceil**4*denominator>=numerator
        assert (ceil-1)**4*denominator<numerator
        rational.append(F(ceil,1000))
    assert 17**3<9**4
    bound=sum(rational[:15])+F(16,7)*rational[15]
    assert bound==F(79781,7000)
    counts=[]
    for r in range(2,6):
        # Fix electric vertex0 at the beginning, and quotient reversal.
        cycles=set()
        for electric in itertools.permutations(range(1,r)):
            for magnetic in itertools.permutations(range(r,2*r)):
                cycle=tuple(v for pair in zip((0,)+electric,magnetic) for v in pair)
                rev=(cycle[0],)+tuple(reversed(cycle[1:]))
                cycles.add(min(cycle,rev))
        paths={min(path,tuple(reversed(path))) for path in itertools.permutations(range(r))}
        assert len(cycles)==math.factorial(r)*math.factorial(r-1)//2
        assert len(paths)==math.factorial(r)//2
        normalized=F(len(cycles)*len(paths)**2,math.factorial(r)**2)
        assert normalized==F(math.factorial(r)**2,8*r)
        counts.append(dict(r=r,cycles=len(cycles),paths_per_species=len(paths),
                           normalized_path_decorations=str(normalized)))
    result=dict(status='finite_author_checks_passed',independent_review=False,
                weighted_tree_checks=checks,maximum_relative_identity_error=mp.nstr(error,8),
                exact_series_upper_bound=str(bound),first_sixteen_upper_coefficients=list(map(str,rational)),
                direct_cycle_path_counts=counts,
                limitations=['counts concern specified combinatorial objects, not an identified physical expansion',
                             'divergence is of the stated series of common upper bounds, not of physical coefficients',
                             'no second factorial normalization is introduced'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
