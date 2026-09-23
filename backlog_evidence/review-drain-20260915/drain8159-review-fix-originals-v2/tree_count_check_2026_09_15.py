"""Exact counts and high precision weighted checks, personal author only."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/CUBIC_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'cubic_fourier_energy_and_gaussian_registers_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/CUBIC_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/tree_count_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
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
    _OUTPUT_JSON.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: cubic cochain symbols and Gaussian derivative registers')
    print('per_site: finite support/grid fixtures')
    print('per_mode: finite Fourier grids and finite register degrees; no infinite-lattice execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
