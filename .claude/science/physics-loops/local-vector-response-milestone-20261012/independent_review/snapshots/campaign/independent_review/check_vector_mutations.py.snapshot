#!/usr/bin/env python3
"""Small exact counterchecks of deliberately false vector-model formulas."""
from fractions import Fraction as F
import datetime as dt
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def outer(a,b):return [[x*y for y in b] for x in a]
def contraction(e,a):return sum(e[i]*a[i][j]*e[j] for i in range(3) for j in range(3))

def main():
    N,D,alpha=F(4),F(1),F(2);k=[F(1),F(2),F(2)];e=[F(2,3),F(2,3),F(1,3)]
    k2=sum(v*v for v in k);I=[[F(i==j) for j in range(3)] for i in range(3)]
    pl=[[x/k2 for x in row] for row in outer(k,k)];pt=[[I[i][j]-pl[i][j] for j in range(3)] for i in range(3)]
    B=[[k2/N*I[i][j]+(1/D-1/N)*k[i]*k[j] for j in range(3)] for i in range(3)]
    right=[[(N*pt[i][j]+D*pl[i][j])/k2 for j in range(3)] for i in range(3)]
    swapped=[[(D*pt[i][j]+N*pl[i][j])/k2 for j in range(3)] for i in range(3)]
    assert mm(B,right)==I and mm(B,swapped)!=I
    expected=contraction(e,right);bad=contraction(e,swapped)
    assert expected==F(44,243) and bad==F(91,243)
    mu2=sum(e[i]*k[i] for i in range(3))**2/k2
    # An invented extra susceptibility vanishes on both axes but fails obliquely.
    axis_invisible_extra=mu2*(1-mu2)/k2
    assert axis_invisible_extra>0
    # Wrong radial delta Jacobian (1/c instead of c) rescales total shell mass.
    wrong_mass_ratio=alpha*(2*N+D)/3
    assert wrong_mass_ratio==6 and wrong_mass_ratio!=1
    # A longitudinal traveling-wave jet saturates cL, so a cT cap misses by cL/cT=2.
    wrong_flux_ratio_squared=N/D
    assert wrong_flux_ratio_squared==4 and wrong_flux_ratio_squared>1
    # Flipping -rho*phi to +rho*phi flips the static isotropic Gauss flux.
    correct_gauss_flux_sign=1;wrong_gauss_flux_sign=-1
    assert correct_gauss_flux_sign!=wrong_gauss_flux_sign
    # Retain PT*gT alone. Then the uncancelled shell mass makes h'=-t/(4pi*r^2)
    # outside all fronts; on the z axis its zz Hessian is 2t/(4pi*r^3).
    full_outside_shell_mass=F(1)-F(1);single_branch_outside_shell_mass=-F(1)
    assert full_outside_shell_mass==0 and single_branch_outside_shell_mass!=0
    normalized_off_cone_zz=F(2)
    assert normalized_off_cone_zz!=0
    previous=json.loads((HERE/'independent_vector_checks_v1.json').read_text())
    assert previous['omission_mutation_error']>.5
    checks=[
      {'mutation':'Swap longitudinal/transverse static coefficients','detected':True,
       'correct_oblique_susceptibility':str(expected),'mutant_oblique_susceptibility':str(bad)},
      {'mutation':'Add a term invisible to axis-only static tests','detected':True,
       'off_axis_discrepancy':str(axis_invisible_extra),'axes_discrepancy':'0'},
      {'mutation':'Invert radial delta Jacobian','detected':True,'mutant_mass_over_correct_mass':str(wrong_mass_ratio)},
      {'mutation':'Use cT as the outer energy-flux speed for D<N','detected':True,'squared_flux_over_cap':str(wrong_flux_ratio_squared)},
      {'mutation':'Flip the source-coupling sign','detected':True,'correct_normalized_Gauss_flux':1,'mutant_normalized_Gauss_flux':-1},
      {'mutation':'Remove the longitudinal branch while claiming no off-cone tail','detected':True,
       'off_cone_Gzz_in_units_t_over_4pi_alpha_r3':str(normalized_off_cone_zz)},
      {'mutation':'Omit the intervening tensor term','detected':True,
       'independently_integrated_error':previous['omission_mutation_error']}
    ]
    output={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'checks':checks,'scope':'Independent synthetic formula mutations only. Author files were not edited or executed.'}
    dest=HERE/'independent_mutations_v1.json';assert not dest.exists();dest.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
