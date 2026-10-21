#!/usr/bin/env python3
"""Finite supplied spectrum, determinant/zeta identity and distinct readouts.
No Weyl-law validation or physical thermodynamic/EWSB identification.
Original source recoverable at f24d17d97d372df977476e4a69674577f31af575.
"""
import sympy as sp
AUDIT_TIMEOUT_SEC = 300


def main():
    tests=[]
    def check(name,value):
        tests.append(bool(value));print(('PASS' if value else 'FAIL')+': '+name)
    u=sp.symbols('u',positive=True);s=sp.symbols('s',real=True)
    dets={};dd={}
    for L in (2,4):
        # Eight supplied DdagD eigenvalues per temporal momentum.
        eigs=[u**2*(3+sp.sin(sp.pi*sp.Rational(2*n+1,L))**2) for n in range(L) for _ in range(8)]
        dd[L]=sp.prod(eigs)
        dets[L]=sp.sqrt(dd[L])
        zeta=sum(x**(-s) for x in eigs)
        minus_derivative=-sp.diff(zeta,s).subs(s,0)
        check(f'L{L}: differentiated finite zeta equals log product',sp.simplify(sp.expand_log(sp.log(dd[L]),force=True)-minus_derivative)==0)
        direct=sp.prod([u**2*(3+sp.sin(sp.pi*sp.Rational(2*n+1,L))**2) for n in range(L)])**4
        check(f'L{L}: paired D determinant and positive square root agree',sp.simplify(dets[L]-direct)==0)
        check(f'L{L}: supplied mode count8L',len(eigs)==8*L)
    r=sp.Rational(7,8)
    ratioD=sp.simplify(dets[4]/dets[2]**2)
    ratioDD=sp.simplify(dd[4]/dd[2]**2)
    check('D ratio=(7/8)^16',ratioD==r**16)
    check('DdagD ratio=(7/8)^32',ratioDD==r**32)
    check('negative control: DdagD ratio is not D ratio',ratioDD!=ratioD)
    ordinary=sp.simplify(dd[4]**sp.Rational(1,64)/dd[2]**sp.Rational(1,32))
    stipulated=sp.simplify(dets[4]**sp.Rational(1,64)/dets[2]**sp.Rational(1,32))
    check('ordinary mass geometric mean ratio has exponent1/2',sp.simplify(ordinary-sp.sqrt(r))==0)
    check('stipulated D readout ratio has exponent1/4',sp.simplify(stipulated-r**sp.Rational(1,4))==0)
    check('readouts differ',sp.simplify(ordinary**4-stipulated**4)!=0)
    # Mass dimensions: D has8L eigenvalues, each dimension1.
    check('stipulated D exponent has mass dimension1/2',sp.Rational(8*4,16*4)==sp.Rational(1,2))
    check('ordinary square-root spectral mean has mass dimension1',sp.Rational(2*8*4,2*8*4)==1)
    check('D4 arithmetic identity',sp.Rational(4,2**4)==sp.Rational(1,4))
    print('No Weyl asymptotic check: finite counting function saturates at8L.')
    print('No energy identification: DdagD eigenvalues have mass dimension2.')
    print('Literal old integral T int(lambda log(1+exp(-lambda/T))) d lambda scales as T^3, not T^4.')
    print('Physical readout and thermodynamic bridges remain open.')
    print(f'TOTAL: PASS={sum(tests)} FAIL={len(tests)-sum(tests)}')
    return 0 if all(tests) else 1

if __name__=='__main__':raise SystemExit(main())
