#!/usr/bin/env python3
"""Exact checks of an imported beta2 polynomial; no graph or physics derivation."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s
CA, CF, TF, nf = s.symbols('CA CF TF nf')
R=s.Rational
beta=R(2857,54)*CA**3+(2*CF**2-R(205,9)*CF*CA-R(1415,27)*CA**2)*TF*nf+(R(44,9)*CF+R(158,27)*CA)*(TF*nf)**2
su3=s.expand(beta.subs({CA:3,CF:R(4,3),TF:R(1,2)}))
checks={
 'SU3 polynomial':s.expand(su3-(R(2857,2)-R(5033,18)*nf+R(325,54)*nf**2))==0,
 'nf6 value':su3.subs(nf,6)==-R(65,2),
 'CF2 TF nf coefficient':s.Poly(beta,CA,CF,TF,nf).coeff_monomial(CF**2*TF*nf)==2,
 'old half coefficient rejected':s.Poly(beta,CA,CF,TF,nf).coeff_monomial(CF**2*TF*nf)!=R(1,2),
 'mixed contraction has two formal channels':len(s.Poly(CF*(CF-CA/2),CA,CF).terms())==2,
}
for name,ok in checks.items(): print(('PASS' if ok else 'FAIL')+': '+name)
print('Imported MS coefficient identity only. Graph enumeration and physical selection remain open.')
raise SystemExit(0 if all(checks.values()) else 1)
