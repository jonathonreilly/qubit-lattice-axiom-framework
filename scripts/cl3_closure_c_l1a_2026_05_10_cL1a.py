"""Conditional explicit/implicit scheme algebra; no physical HK matching proof.
See CLOSURE_C_L1_HK_MSBAR_3L_CONVERSION_NOTE_2026-05-10_cL1a.md.
No repository inputs, ledger status, fitted HK parameters or literal-True receipts.
"""
import math
import sympy as sp


def main():
    failures = 0
    passes = 0
    def check(label, condition):
        nonlocal failures, passes
        result = bool(condition)
        failures += not result
        passes += result
        print(f"[{'PASS' if result else 'FAIL'}] {label}")
    g,a,b,c,u,v,z1,z2,b0,b1,b2 = sp.symbols('g a b c u v z1 z2 b0 b1 b2')
    trunc = lambda p,n: sp.series(p,g,0,n).removeO().expand()
    transform = lambda A,B,B2: B2-2*A*b1+(2*B-3*A*A)*b0
    f = g+a*g**3+b*g**5+c*g**7
    beta = -b0*g**3-b1*g**5-b2*g**7
    target = -b0*f**3-b1*f**5-transform(a,b,b2)*f**7
    residual = trunc(sp.diff(f,g)*beta-target,9)
    check('explicit chain rule through g^7, arbitrary coefficients',residual==0)
    check('g^7 transformation independent of c',sp.diff(transform(a,b,b2),c)==0)
    wrong = b2-2*a*b1+(a*a+2*b)*b0
    check('former explicit-map formula rejected by exact residual',sp.expand(wrong-transform(a,b,b2))==4*a*a*b0)
    fw = g+z1*g**3+(z2+2*z1*z1)*g**5
    check('AFP implicit equation solved through g^5',trunc(fw-g*(1+z1*fw**2+z2*fw**4),7)==0)
    check('AFP beta formula follows only after convention conversion',sp.expand(transform(z1,z2+2*z1*z1,b2)-(b2-2*z1*b1+(z1*z1+2*z2)*b0))==0)
    inverse = g-a*g**3+(3*a*a-b)*g**5
    check('explicit inverse through g^5',trunc(f.subs(g,inverse)-g,7)==0)
    composite = trunc(f+u*f**3+v*f**5,7)
    check('directed composition coefficient identity',sp.expand(composite-(g+(a+u)*g**3+(b+v+3*a*u)*g**5))==0)
    check('beta transformation composes',sp.expand(transform(u,v,transform(a,b,b2))-transform(a+u,b+v+3*a*u,b2))==0)
    nf=6;CA=sp.Integer(3);CF=sp.Rational(4,3);TF=sp.Rational(1,2)
    check('supplied stripped b0 polynomial at Nf6',(11*CA-2*nf)/3==7)
    check('supplied stripped b1 polynomial at Nf6',sp.Rational(34,3)*CA**2-sp.Rational(20,3)*CA*TF*nf-4*CF*TF*nf==26)
    check('supplied stripped MSbar b2 polynomial at Nf6',sp.Rational(2857,2)-sp.Rational(5033,18)*nf+sp.Rational(325,54)*nf**2==-sp.Rational(65,2))
    s=sp.symbols('s');P=sp.series(1-sp.exp(-4*s/3),s,0,4).removeO()
    check('supplied plaquette Taylor coefficients only',[P.coeff(s,k) for k in (1,2,3)]==[sp.Rational(4,3),-sp.Rational(8,9),sp.Rational(32,81)])
    # Supplied pure-gauge N=3 example: all beta coefficients share normalization.
    N=3;pi2=math.pi**2;factor=N/(16*pi2)
    B0=11/3*factor;B1=34/3*factor**2;B2MS=2857/54*factor**3
    B2W=factor**3*(-366.2+1433.8/N**2-2143/N**4)
    Z1=N*(1/(96*pi2)+1/(16*N*N)-1/32-5/72*.15493339-11/6*.024013181)
    Z2=(B2W-B2MS+2*B1*Z1-B0*Z1**2)/(2*B0)
    back=B2MS-2*B1*Z1+B0*Z1**2+2*B0*Z2
    print(f'IMPORTED example: z1={Z1:.12g}, back-solved z2={Z2:.12g}, b2W={B2W:.12g}')
    check('non-independent arithmetic round-trip (same 1e-10 threshold)',abs(back-B2W)/abs(B2W)<1e-10)
    correction=(B1**2-B2W*B0)/(2*B0**3)
    print(f'IMPORTED rounded Lambda comparator: computed={correction:.12g}, supplied=.1896')
    check('rounded supplied Lambda comparator (same 1 percent threshold)',abs(correction-.1896)/.1896<.01)
    print('NOT VERIFIED: physical HK coupling/beta function, common continuum theory, HK matching coefficients, upstream identifications or audit authority.')
    print('32/81 is a supplied plaquette Taylor coefficient, not a derived beta coefficient. Back-solving z2 is not independent matching.')
    print(f'Total: {passes} PASS, {failures} FAIL')
    return 1 if failures else 0


if __name__=='__main__':
    raise SystemExit(main())
