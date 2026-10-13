#!/usr/bin/env python3
"""Independent symbolic checks of the handwritten radiation derivation."""
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
A,S,R,L,b=s.symbols('a S R L b',positive=True)
CHECKS=[]
DETAIL={}


def check(name, expression, expected=0):
    residual=s.factor(s.together(expression-expected))
    CHECKS.append(dict(name=name,passed=residual==0,residual=str(residual)))


def total(expr):
    return s.diff(expr,S)+s.Rational(4,3)*R/S*s.diff(expr,R)


# The unchanged potential fixes chi-dot from matter conservation. Eliminate
# that speed from Friedmann before differentiating the derived H^2.
H0sq=s.Rational(2,3)*((1+A)*S+L)
B=(2+A)*S+2*L
F=s.factor((2*(S+R+L)+A*S)/(3-A*S/H0sq))
check('unchanged_Friedmann_solution',F,H0sq*(1+2*R/B))
hd_from=-s.Rational(3,2)*S*s.diff(F,S)-2*R*s.diff(F,R)
hd_ray=-S-s.Rational(4,3)*R-A*S*F/H0sq
residual=s.factor(hd_from-hd_ray)
check('unchanged_radiation_residual',residual,2*A*R*S*((2+A)*S-L)/(3*B**2))
DETAIL['unchanged_residual']=str(residual)

# Reconstructed exact path and independent background identities.
C=(1+A)*(S+R)+L
Hsq=s.Rational(2,3)*C
W=S+s.Rational(4,3)*R
U=L+A*S/2+A*R/3
v2=A*W
Sdot_over_H=-3*S
Rdot_over_H=-4*R
check('new_Friedmann',3*Hsq,2*(S+R+U)+v2)
check('new_Raychaudhuri',(-3*S*s.diff(Hsq,S)-4*R*s.diff(Hsq,R))/2,-W-v2)
check('u_force_cancellation',-s.sqrt(A)*S+s.sqrt(A)*S)
# Multiply chi EOM by chi-dot/H to remove square roots without division at S=0.
accel_times_v_over_H=(-3*S*s.diff(v2,S)-4*R*s.diff(v2,R))/2
Uchi_times_v_over_H=-3*S*total(U)
check('chi_equation',accel_times_v_over_H+3*v2+Uchi_times_v_over_H)
check('claimed_chi_acceleration',accel_times_v_over_H,-A*(3*S+s.Rational(16,3)*R)/2)
check('claimed_U_chi',Uchi_times_v_over_H,-A*(s.Rational(3,2)*S+s.Rational(4,3)*R))
check('matter_and_radiation_relation',(-3*S)*total(b*S**s.Rational(4,3)), -4*b*S**s.Rational(4,3))

# Coordinate curvature from the square of dS/dchi.
J=6*C*S*S/(A*W)
U1=total(U);U2=total(U1)
Ucc=s.factor(J*U2+total(J)*U1/2)
check('U_S',U1,A*(s.Rational(1,2)+4*R/(9*S)))
check('U_SS',U2,4*A*R/(27*S*S))
r=s.symbols('r',positive=True)
claimed_Jprime=18/A*(total(C)*S*(3+4*R/S)+C*(3+s.Rational(8,3)*R/S))/(3+4*R/S)**2
check('positive_coordinate_derivative',total(J),claimed_Jprime)
transverse=A*J/Ucc+A*S*S/U
check('Hessian_determinant',transverse*Ucc-A*J,A*S*S*Ucc/U)
u=s.symbols('u',real=True)
potential=U-s.sqrt(A)*S*u+transverse*u*u/2
check('complete_square',potential,transverse*(u-s.sqrt(A)*S/transverse)**2/2+U-A*S*S/(2*transverse))
DETAIL['U_chichi']=str(Ucc)
DETAIL['F_Scoord_derivative']=str(s.factor(total(J)))

# Field coordinate form and exact-path denominator and kinetic terms.
g=A*W/(9*Hsq)
h=-W/Hsq-9*g
Gamma=S*total(g)/(2*g)
check('coordinate_metric',J,S*S/g)
check('trajectory_Friedmann_coordinate',Hsq*(3-9*g),2*(S+R+U))
check('trajectory_Raychaudhuri_coordinate',h,-(1+A)*W/Hsq)
check('trajectory_x_equation',3*(3+h)-9*Gamma-S*U1/(g*Hsq))
check('positive_denominator_numerator',3*Hsq-A*W,(2+A)*S+(2+s.Rational(2,3)*A)*R+2*L)
DETAIL['coordinate_denominator_numerator']=str(s.factor(3*Hsq-A*W))

# Limiting slopes. These are ratios r=R/S and ell=L/S, not an asserted dust
# epoch for every arbitrary fixed b,L pair.
ratio=s.factor((W/Hsq).subs({R:r*S,L:0}))
rad=s.limit(ratio,r,s.oo)
dust=s.limit(ratio,r,0)
check('radiation_velocity_squared',rad,2/(1+A))
check('dust_velocity_squared_handwritten',dust,3/(1+A))
check('dust_velocity_squared_corrected',dust,s.Rational(3,2)/(1+A))
slope_squared=s.factor((total(U)/U)**2*J)
rad_slope=s.limit(slope_squared.subs({R:r*S,L:0}),r,s.oo)
dust_slope=s.limit(slope_squared.subs({R:r*S,L:0}),r,0)
check('radiation_exponential_slope_squared',rad_slope,8*(1+A)/A)
check('dust_exponential_slope_squared',dust_slope,6*(1+A)/A)
DETAIL['velocity_limits_squared']=dict(radiation=str(rad),dust=str(dust))

# Use y=S^(1/6) so the fractional endpoint integral has an ordinary series.
# q = (3Hv/(2sqrt(a))) * (chi_c-chi); dq/dS=1/2 S^-1/2
# sqrt(1+4bS^(1/3)/3)/sqrt(1+(1+a)(S+bS^(4/3))/L).
y,z=s.symbols('y z',positive=True)
dqdy=3*y*y*s.sqrt(1+4*b*y*y/3)/s.sqrt(1+(1+A)*(y**6+b*y**8)/L)
q_of_y=s.integrate(s.series(dqdy,y,0,8).removeO(),y)
DETAIL['endpoint_q_of_y']=str(q_of_y)
# Invert using y=z(1+c z^2+d z^4), where z=q^(1/3).
c,d=s.symbols('c d')
yin=z*(1+c*z*z+d*z**4)
composition=s.series(q_of_y.subs(y,yin),z,0,8).removeO()
solve=s.solve([s.expand(composition-z**3).coeff(z,5),s.expand(composition-z**3).coeff(z,7)],(c,d),dict=True)[0]
S_of_z=s.series(yin.subs(solve)**6,z,0,11).removeO().expand()
U_of_z=s.series((L+A*yin**6/2+A*b*yin**8/3).subs(solve),z,0,11).removeO().expand()
check('endpoint_S_q2',S_of_z.coeff(z,6),1)
check('endpoint_S_q8over3',S_of_z.coeff(z,8),-4*b/5)
check('endpoint_U_q2',U_of_z.coeff(z,6),A/2)
check('endpoint_U_q8over3',U_of_z.coeff(z,8),-A*b/15)
DETAIL['endpoint_S_series_z_q_one_third']=str(S_of_z)
DETAIL['endpoint_U_series_z_q_one_third']=str(U_of_z)

# The full potential's transverse coefficient must also be checked, not just U.
# Since d/dchi=-beta d/dq, beta cancels from a*(S_chi)^2/U_chichi.
q=s.symbols('q',positive=True)
ss=S_of_z.subs(z,q**s.Rational(1,3))
uu=U_of_z.subs(z,q**s.Rational(1,3))
mm=A*s.diff(ss,q)**2/s.diff(uu,q,2)+A*ss**2/uu
Mseries=s.series(mm.subs(q,z**3),z,0,9).removeO().expand()
check('endpoint_M_q2',Mseries.coeff(z,6),4)
check('endpoint_M_q8over3',Mseries.coeff(z,8),-s.Rational(992,135)*b)
DETAIL['endpoint_M_series_z_q_one_third']=str(Mseries)
DETAIL['full_V_q2_coefficient']=str(A/2-s.sqrt(A)*u+2*u*u)
DETAIL['full_V_q8over3_coefficient']=str(-A*b/15+4*s.sqrt(A)*b*u/5-s.Rational(496,135)*b*u*u)

out=dict(checks_count=len(CHECKS),all_passed=all(c['passed'] for c in CHECKS),checks=CHECKS,details=DETAIL)
(ROOT/'ALGEBRA_RESULTS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks_count=len(CHECKS),all_passed=out['all_passed'],failures=[c for c in CHECKS if not c['passed']])))
raise SystemExit(0 if out['all_passed'] else 1)
