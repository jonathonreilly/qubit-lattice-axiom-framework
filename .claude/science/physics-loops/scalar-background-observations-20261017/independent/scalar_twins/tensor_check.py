import sympy as S
import json
from pathlib import Path
e,t,z=S.symbols('eta tau z',positive=True)
k=S.symbols('k',positive=True)
B=S.Function('B')(e); v=S.Function('v')(e)
h=v/B
transport=S.simplify(B*(S.diff(h,e,2)+2*S.diff(B,e)/B*S.diff(h,e)+k*k*h)-(S.diff(v,e,2)+(k*k-S.diff(B,e,2)/B)*v))
assert transport==0
results={'exact_v_B_transformation':str(transport),'twins':{}}
for s in (S.Rational(1,2),S.Rational(1,4)):
    ratio=(1+z)**(-s/2)
    H=2*S.sqrt(1+z)
    q_z=S.simplify(-(1+z)*H*S.diff(S.log(ratio),z))
    q=S.simplify(q_z.subs(z,t**-2-1)); A=t**s; hj=2/t; ell=hj-q
    R=A**2*t**-6/8
    F=S.simplify((-2*(S.diff(ell,t)+q*ell)-R)/q**2)
    V=S.simplify(A**2*(3*ell**2-R-F*q*q/2))
    E=S.simplify(S.diff(F*q,t)+(3*hj-2*q)*F*q+R)
    E_direct=S.simplify(S.diff(F,t)*q/2-S.diff(V,t)/(q*A**2))
    assert S.simplify(q-s/t)==0
    assert S.simplify(F-(2*(2-s)*(1-s)/s**2-t**(2*s-4)/(8*s*s)))==0
    assert S.simplify(V-((2-s)*(5-2*s)*t**(2*s-2)-t**(4*s-6)/16))==0
    assert S.simplify(E-E_direct)==0
    assert S.simplify(ratio.subs(z,3)-2**(-s))==0
    # Incorrect inverse propagation ratio gives wrong q and does not recover this witness.
    q_wrong=S.simplify(-(1+z)*H*S.diff(S.log(1/ratio),z))
    assert S.simplify(q_wrong-q_z)!=0
    results['twins'][str(s)]={'ratio':str(ratio),'q':str(q),'R':str(R),'F':str(F),'V':str(V),'E':str(E),'ratio_z3':str(ratio.subs(z,3))}
Path('/private/tmp/background-scalar-twins/tensor_result.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
