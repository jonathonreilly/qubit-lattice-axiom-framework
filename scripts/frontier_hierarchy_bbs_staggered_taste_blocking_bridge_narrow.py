"""Supplied staircase arithmetic and counterexamples to old bridge inferences.
No literature-domain, RG contraction or audit verdict is established by this runner.
"""
from fractions import Fraction
import math
import numpy as np

AUDIT_TIMEOUT_SEC = 120


def main():
    checks=[]
    def check(name,ok,detail=''):
        checks.append(bool(ok));print(('PASS' if ok else 'FAIL')+': '+name+' '+detail)
    b=[(Fraction(33)-2*(16-k))/3 for k in range(17)]
    check('endpoint indices from n_k=16-k',b[0]==Fraction(1,3) and b[16]==11)
    check('exact cumulative coefficient',sum(b[:16])==Fraction(256,3))
    check('exact successive difference',all(b[k+1]-b[k]==Fraction(2,3) for k in range(16)))
    for alpha in [0.09067,float(Fraction(907,10000))]:
        u0=0.87768138
        traj=[u0-math.fsum(float(x) for x in b[:k])*abs(math.log(alpha))/(8*math.pi**2) for k in range(17)]
        check('supplied truncated inverse-coupling diagnostic crosses zero',traj[0]>0 and traj[-1]<0,f'alpha={alpha}; final={traj[-1]}; first nonpositive rung={next(k for k,u in enumerate(traj) if u<=0)}')
    alpha=Fraction(9067,100000)
    check('chosen scalar contraction may have norm equal to alpha',0<alpha<1 and abs(alpha*Fraction(7,3))/abs(Fraction(7,3))==alpha)
    # Exact finite-box autocorrelation at every separation in each tested block.
    for j in range(5):
        R=2**j
        for r in range(R+2):
            overlap=max(R-r,0)
            value=Fraction(1,4**j)*Fraction(overlap,R)
            expected=Fraction(1,4**j)*max(1-Fraction(r,R),0)
            check(f'box autocorrelation j={j} r={r}',value==expected)
    # Independent numerical PSD sanity, not the proof of positive definiteness.
    sites=np.arange(-8,9)
    def kernel(r,j):return 4.**(-j)*max(1-abs(r)/2**j,0)
    gram=sum(np.array([[kernel(x-y,j) for y in sites] for x in sites]) for j in range(12))
    check('finite covariance sum PSD',np.linalg.eigvalsh(gram).min()>-1e-12)
    for n in range(7):
        tail=sum(Fraction(1,4**j)*(1-Fraction(2**n,2**j)) for j in range(n+1,40))
        exact=Fraction(4,21)*Fraction(1,4**n)
        check(f'long-range dyadic value n={n}',abs(tail-exact)<Fraction(2,4**40))
    print('per_element: exact staircase endpoints/sums and finite-box autocorrelations checked.')
    print('per_site: toy covariance separations only; no physical gauge or fermion update law executed.')
    print('per_mode: supplied taste counts, not a derived spectrum or effective-theory decoupling sequence.')
    print('per_block: finite rung and covariance blocks tested; no physical RG contraction inferred.')
    print('lattice_wide: checked and not executed — actual gauge covariance decomposition and RG estimates remain open.')
    print(f'TOTAL: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}')
    return int(not all(checks))


if __name__=='__main__':
    raise SystemExit(main())
