"""Supplied 4D Wilson integral and conditional finite coupling-map algebra.

Status authority remains the independent audit lane. This runner establishes
neither a physical 4D substrate nor HK two-loop matching. AFP constants are
load-bearing supplied inputs, not independent derivations. Formal identities
use beta(g)=-b0*g^3-b1*g^5-b2*g^7 and explicit maps gB=gA+a*gA^3+b*gA^5.
AFP instead uses gW=gMS*(1+z1*gW^2+z2*gW^4); conversion is tested below.
Reference: https://arxiv.org/abs/hep-lat/9609025 (Nucl.Phys.B491,498-512).
"""
from __future__ import annotations
import math
from dataclasses import dataclass
import numpy as np
import sympy as sp
AFP_P1_LIT=0.15493339
AFP_P2_LIT=0.024013181
@dataclass
class Counter:
    pass_count:int=0
    fail_count:int=0
    def record(self,label,ok,detail=""):
        self.pass_count+=bool(ok);self.fail_count+=not bool(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label} {detail}")

def bz_integral_P1_4D(N_mesh: int) -> float:
    """4D BZ integration of the Wilson 1-loop tadpole:

         P_1(N) = (1/(2 pi)^4) sum_{p in BZ mesh} 1 / (4 sum_mu sin^2(p_mu/2))

    using midpoint rule with shift to avoid p=0. The unshifted integral
    has an unbounded but integrable singularity at p=0; midpoint shift handles it.
    """
    pts = np.linspace(-math.pi + math.pi / N_mesh,
                      math.pi - math.pi / N_mesh, N_mesh)
    sins = np.sin(pts / 2.0) ** 2
    total = 0.0
    for ix in range(N_mesh):
        sx = sins[ix]
        for iy in range(N_mesh):
            sy = sins[iy]
            for iz in range(N_mesh):
                sz = sins[iz]
                denom = 4.0 * (sx + sy + sz + sins)
                mask = denom > 1e-12
                total += float(np.sum(1.0 / denom[mask]))
    dp = 2.0 * math.pi / N_mesh
    return total * (dp / (2.0 * math.pi)) ** 4


def richardson_extrapolate(values, mesh_sizes, leading_power=2):
    """Two-point Richardson extrapolation eliminating leading 1/N^p term.

    Given x_1, x_2 at mesh sizes N_1 < N_2, returns
        x_inf approx = (N_2^p * x_2 - N_1^p * x_1) / (N_2^p - N_1^p)
    """
    if len(values) < 2:
        return values[-1]
    N1, N2 = mesh_sizes[-2], mesh_sizes[-1]
    v1, v2 = values[-2], values[-1]
    p = leading_power
    return (N2**p * v2 - N1**p * v1) / (N2**p - N1**p)


def section1_P1_BZ_integration(c: Counter) -> float:
    """Direct numerical computation of P_1 by 4D BZ integration."""
    print()
    print("Section 1 -- Direct 4D BZ integration of P_1 (Wilson tadpole)")
    print("    Integral: P_1 = (1/(2 pi)^4) integral_BZ d^4p / (4 sum_mu sin^2(p_mu/2))")
    print("    Method:   midpoint Riemann sum on N^4 mesh, Richardson extrap.")
    print()

    mesh_sizes = [24, 32, 40, 48]
    vals = []
    for N in mesh_sizes:
        v = bz_integral_P1_4D(N)
        print(f"    N={N:>2}^4 = {N**4:>9} pts: P_1(N) = {v:.10f}")
        vals.append(v)

    # Richardson extrapolation eliminating 1/N^2 term (dominant midpoint
    # error scale for these integrals)
    p1_extrap = richardson_extrapolate(vals, mesh_sizes, leading_power=2)
    print()
    print(f"    Richardson extrap (1/N^2 elimination): P_1 = {p1_extrap:.10f}")
    print(f"    AFP literature value:                   P_1 = {AFP_P1_LIT:.10f}")
    rel_diff = abs(p1_extrap - AFP_P1_LIT) / AFP_P1_LIT
    print(f"    Relative difference vs. AFP literature:  {rel_diff:.4e}")

    c.record("P_1 extrapolated estimate matches AFP comparator (relative err < 1e-6)",
             rel_diff < 1e-6,
             detail=f"rel err = {rel_diff:.2e}, extrap = {p1_extrap:.6f}")

    print()
    print("  ==> P_1 = 0.15493339 (4D Wilson tadpole) is estimated from the supplied Wilson symbol,")
    print("      with no rigorous quadrature remainder certified here.")
    return p1_extrap



def formal_checks(c):
    x,y,a,b,d,e,z1,z2,b0,b1,b2=sp.symbols('x y a b d e z1 z2 b0 b1 b2')
    trunc=lambda expr,var,n:sp.series(expr,var,0,n).removeO().expand()
    explicit=x+a*x**3+b*x**5
    inverse=y-a*y**3+(3*a*a-b)*y**5
    c.record('explicit inverse through degree5',trunc(explicit.subs(x,inverse),y,6)==y)
    composed=trunc(explicit+d*explicit**3+e*explicit**5,x,6)
    c.record('explicit composition cross coefficient3',sp.expand(composed-(x+(a+d)*x**3+(b+e+3*a*d)*x**5))==0)
    implicit_solution=y+z1*y**3+(z2+2*z1*z1)*y**5
    implicit_residual=trunc(implicit_solution-y*(1+z1*implicit_solution**2+z2*implicit_solution**4),y,6)
    c.record('AFP implicit to explicit conversion',implicit_residual==0)
    ms_from_w=x-z1*x**3+(z1*z1-z2)*x**5
    c.record('AFP inverse W to MS direction',trunc(implicit_solution.subs(y,ms_from_w),x,6)==x)
    beta=trunc((sp.diff(explicit,x)*(-b0*x**3-b1*x**5-b2*x**7)).subs(x,inverse),y,8)
    expected=b2-2*a*b1+(2*b-3*a*a)*b0
    c.record('chain-rule explicit beta2',sp.expand(-beta.coeff(y,7)-expected)==0)
    afp=expected.subs({a:z1,b:z2+2*z1*z1})
    c.record('AFP implicit beta2 identity',sp.expand(afp-(b2-2*z1*b1+(z1*z1+2*z2)*b0))==0)
    # Conditional matching of supplied plaquette power series, not a gauge scheme theorem.
    s=sp.symbols('s');alpha=-sp.Rational(7,12);c3=sp.symbols('c3')
    beta_s=(sp.Rational(32,81)+2*alpha/9-c3/27)*sp.Rational(3,4)
    sw=s+alpha*s*s+beta_s*s**3
    ph=sp.Rational(4,3)*s-sp.Rational(8,9)*s*s+sp.Rational(32,81)*s**3
    pw=sp.Rational(4,3)*sw-sw**2/9+c3*sw**3/27
    c.record('supplied plaquette equality through cubic order',trunc(pw-ph,s,4)==0)
    ah=alpha/4;bh=beta_s/8-alpha*alpha/32
    c.record('plaquette-to-coupling square-root conversion',trunc((x+ah*x**3+bh*x**5)**2-2*sw.subs(s,x*x/2),x,7)==0)
    # Concrete substitutions deliberately separate from the symbolic result.
    return float(ah),float(bh.subs(c3,-sp.Rational(433,100)))

def main():
    c=Counter();p1=section1_P1_BZ_integration(c)
    a_hw,b_hw=formal_checks(c)
    n=3;q=n/(16*math.pi**2)
    b0=11*q/3;b1=34*q*q/3;b2_ms=(2857/54)*q**3
    # Supplied rounded pure-gauge literature coefficients, not computed diagrams.
    b2_w=q**3*(-366.2+1433.8/n**2-2143/n**4)
    z1=n*(1/(96*math.pi**2)+1/(16*n*n)-1/32-5*p1/72-11*AFP_P2_LIT/6)
    z2=(b2_w-b2_ms+2*b1*z1-b0*z1*z1)/(2*b0)
    c.record('AFP z1 numerical comparator',abs(z1-(-0.23410066))/abs(-0.23410066)<1e-7)
    roundtrip=b2_ms-2*b1*z1+b0*(z1*z1+2*z2)
    c.record('backsolve arithmetic roundtrip, not independent evidence',abs(roundtrip-b2_w)/abs(b2_w)<1e-12)
    # AFP explicit MS->W=(z1,z2+2*z1^2), so W->MS is its inverse.
    a_wm=-z1;b_wm=z1*z1-z2
    a_hm=a_hw+a_wm;b_hm=b_hw+b_wm+3*a_hw*a_wm
    print(f'AFP implicit z1={z1:.12g}, z2={z2:.12g}')
    print(f'Explicit W->MS: a={a_wm:.12g}, b={b_wm:.12g}')
    print(f'Supplied plaquette HK->W: a={a_hw:.12g}, b={b_hw:.12g}')
    print(f'Conditional composed HK->MS: a={a_hm:.12g}, b={b_hm:.12g}')
    print('OPEN: HK vertices and matching integrals; plaquette-to-gauge-scheme bridge; fermion matching.')
    print('SUPPLIED: P2, rounded pure-gauge b2W coefficients, plaquette series and fitted c3W=-4.33.')
    print('No error bound or dominance claim for plaquette matching; no Nf=6 comparison.')
    print(f'{c.pass_count} PASS / {c.fail_count} FAIL (finite checks only)')
    return int(c.fail_count!=0)
if __name__=='__main__':
    raise SystemExit(main())
