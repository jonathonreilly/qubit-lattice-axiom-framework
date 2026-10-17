import sympy as S
import json
from pathlib import Path
x,z=S.symbols('tau zeta', positive=True)
out={}
for s in (S.Rational(1,2),S.Rational(1,4)):
    A=x**s
    dt=lambda f:S.simplify(A*S.diff(f,x))
    H=(2-s)*x**(s-1)
    zd=s*x**(s-1)
    rho=S.Rational(1,8)*x**(4*s-6)
    Fz=2*(2-s)*(1-s)/s**2-S.exp((2*s-4)*z/s)/(8*s**2)
    Vz=(2-s)*(5-2*s)*S.exp((2*s-2)*z/s)-S.exp((4*s-6)*z/s)/16
    sub=lambda f:S.simplify(f.subs(z,s*S.log(x)))
    F,V=sub(Fz),sub(Vz)
    checks={
       'Friedmann':3*H**2-rho-F*zd**2/2-V,
       'Raychaudhuri':-2*dt(H)-rho-F*zd**2,
       'dust_continuity':dt(rho)+3*H*rho-zd*rho,
       'scalar_equation':F*dt(zd)+3*H*F*zd+sub(S.diff(Fz,z))*zd**2/2+sub(S.diff(Vz,z))+rho,
       'Jordan_density':rho/A**4-S.Rational(1,8)*x**-6,
       'Jordan_Hubble':H/A+zd/A-2/x,
       'Jordan_scale':x**(2-s)*A-x**2,
       'normalization_A1':A.subs(x,1)-1,
    }
    checks={k:S.simplify(v) for k,v in checks.items()}
    assert all(v==0 for v in checks.values()),checks
    # F is increasing since its negative-power coefficient is negative.
    assert (2*s-4)<0
    assert 2*(2-s)*(1-s)/s**2 > 0
    Fmin=S.simplify(F.subs(x,S.Rational(1,2)))
    assert Fmin>0
    # V'=x^(4s-7) [negative coefficient*x^(4-2s) + (6-4s)/16].
    dv_bracket=S.simplify(S.diff(V,x)/x**(4*s-7))
    # Bracket decreases with x; checking its maximum at x=1/2 proves V'<0.
    coeff=(2*s-2)*(2-s)*(5-2*s)
    assert coeff<0 and (4-2*s)>0
    assert S.simplify(dv_bracket-(coeff*x**(4-2*s)+(6-4*s)/16))==0
    assert dv_bracket.subs(x,S.Rational(1,2))<0
    Vmin=V.subs(x,1)
    assert Vmin>0
    out[str(s)]={
      'F':str(Fz),'V':str(Vz),'H_E':str(H),'zeta_dot':str(zd),'rho_E':str(rho),
      'identities':{k:str(v) for k,v in checks.items()},
      'F_min':str(Fmin),'V_min':str(Vmin),
      'V_derivative_bracket':str(dv_bracket),
      'alpha_squared_at_A1':str(S.simplify(1/F.subs(x,1))),
      'V_at_A1':str(V.subs(x,1)),
    }
Path('/private/tmp/background-scalar-twins/result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
mutations={}
for s in (S.Rational(1,2),S.Rational(1,4)):
    A=x**s; H=(2-s)*x**(s-1); zd=s*x**(s-1)
    rho=S.Rational(1,8)*x**(4*s-6)
    F=2*(2-s)*(1-s)/s**2-x**(2*s-4)/(8*s**2)
    V=(2-s)*(5-2*s)*x**(2*s-2)-x**(4*s-6)/16
    variants={
       'wrong_scalar_source_sign':-2*rho,
       'forgot_proper_time_conversion_in_Raychaudhuri':-2*S.diff(H,x)-rho-F*zd**2,
       'dropped_negative_dust_term_in_potential':3*H**2-rho-F*zd**2/2-(V+rho/2),
       'wrong_density_conformal_power':rho/A**3-S.Rational(1,8)*x**-6,
    }
    for k,v in variants.items():
      val=S.simplify(v.subs(x,S.Rational(3,4)))
      assert val!=0,(s,k,val)
      mutations[str(s)+' '+k]=str(val)
Path('/private/tmp/background-scalar-twins/mutations.json').write_text(json.dumps(mutations,indent=2)+'\n')
print('Eight mutation controls rejected.')
