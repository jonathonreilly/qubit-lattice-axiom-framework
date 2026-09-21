#!/usr/bin/env python3
"""Algebraic controls of entropy, energy flux and second-order record transport."""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent


def main():
    checks=[]
    def check(name,condition,detail=None):
        assert condition,(name,detail)
        checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
    axes=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    cubes=list(product((-1,1),repeat=3))
    E=s.Matrix(axes+[(0,0,0)]*8).T
    B=s.Matrix([(0,0,0)]*6+cubes).T
    rA,rB,gamma=s.symbols('rho_A rho_B gamma',positive=True)
    pbar=s.Matrix([rA/6]*6+[rB/8]*8);p0=1-rA-rB
    H=s.diag(*[1/v for v in pbar])+s.ones(14)/p0
    C=s.diag(*pbar)-pbar*pbar.T
    check('full_simplex_entropy_metric_inverse',all(s.factor(v)==0 for v in H*C-s.eye(14)))
    X=s.Matrix(s.symbols('Xx Xy Xz',real=True));Y=s.Matrix(s.symbols('Yx Yy Yz',real=True))
    # Zero scalar/quadrupole perturbations; all vector values are arbitrary.
    u=E.T*X/2+B.T*Y/8
    check('pure_vector_species_reconstruction',E*u==X and B*u==Y and sum(u)==0)
    energy=s.factor((u.T*H*u)[0]/2)
    expected=3*(X.dot(X))/(2*rA)+(Y.dot(Y))/(2*rB)
    check('positive_quadratic_wave_energy',s.factor(energy-expected)==0,dict(expression=str(expected)))
    # Other fields are retained in the general perturbation used for q2.
    general=s.Matrix(s.symbols('u1:15',real=True));Gx=E*general;Gy=B*general
    theta1=H*general
    psi=gamma*Gx.cross(Gy)
    for i in range(3):
        gradient=s.Matrix([s.diff(psi[i],v) for v in general])
        J1=C*gradient
        q2=(theta1.T*J1)[0]-psi[i]
        check(f'quadratic_entropy_flux_is_Poynting_component_{i}',s.expand(q2-psi[i])==0)
    pp=s.Matrix(s.symbols('p1:15',real=True))
    rhoA=sum(pp[:6]);rhoB=sum(pp[6:]);vacancy=1-rhoA-rhoB
    Cp=s.diag(*pp)-pp*pp.T;Xp=E*pp;Yp=B*pp;potential=gamma*Xp.cross(Yp)
    for i in range(3):
        J=Cp*s.Matrix([s.diff(potential[i],v) for v in pp])
        check(f'exact_orbit_and_total_record_current_{i}',
            s.expand(sum(J[:6])-(1-2*rhoA)*potential[i])==0 and
            s.expand(sum(J[6:])-(1-2*rhoB)*potential[i])==0 and
            s.expand(sum(J)-2*vacancy*potential[i])==0)
    # Independent component differentiation of the vector calculus identities.
    electric=s.Matrix(s.symbols('Ex Ey Ez',real=True));magnetic=s.Matrix(s.symbols('Bx By Bz',real=True))
    dE=s.Matrix(3,3,s.symbols('dE0:9',real=True));dB=s.Matrix(3,3,s.symbols('dB0:9',real=True))
    speed=s.symbols('c',positive=True)
    curl=lambda D:s.Matrix([D[2,1]-D[1,2],D[0,2]-D[2,0],D[1,0]-D[0,1]])
    electric_t=speed*curl(dB);magnetic_t=-speed*curl(dE)
    energy_t=electric.dot(electric_t)+magnetic.dot(magnetic_t)
    poynting=speed*electric.cross(magnetic)
    divS=sum(s.diff(poynting[j],electric[k])*dE[k,j]+s.diff(poynting[j],magnetic[k])*dB[k,j]
             for j in range(3) for k in range(3))
    check('energy_continuity_without_Gauss_assumption',s.expand(energy_t+divS)==0)
    momentum_t=(electric_t.cross(magnetic)+electric.cross(magnetic_t))/speed
    stress=s.eye(3)*(electric.dot(electric)+magnetic.dot(magnetic))/2-electric*electric.T-magnetic*magnetic.T
    divergence=s.Matrix([sum(s.diff(stress[i,j],electric[k])*dE[k,j]+s.diff(stress[i,j],magnetic[k])*dB[k,j]
                            for j in range(3) for k in range(3)) for i in range(3)])
    defect=momentum_t+divergence
    check('stress_identity_with_both_divergence_terms',all(s.expand(v)==0 for v in defect+electric*s.trace(dE)+magnetic*s.trace(dB)))
    check('unconstrained_product_requires_Gauss_defect',any(s.expand(v)!=0 for v in defect))
    # Exact occupancy coefficient expansion about arbitrary interior orbit masses.
    eps,da,db=s.symbols('epsilon dA dB')
    Ps=s.symbols('Psi')
    for name,density,coefficient in [('A',rA+eps**2*da,1-2*rA),('B',rB+eps**2*db,1-2*rB)]:
        flux=(1-2*density)*eps**2*Ps
        check('second_order_record_energy_coefficient_'+name,s.expand(s.expand(flux).coeff(eps,2)-coefficient*Ps)==0)
    total=2*(p0-eps**2*(da+db))*eps**2*Ps
    check('second_order_total_record_energy_coefficient',s.expand(s.expand(total).coeff(eps,2)-2*p0*Ps)==0)
    result=dict(count=len(checks),checks=checks,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='Symbolic controls of the stated conditional classical continuum identities; not physical energy identification, quantization, Gauss-sector preparation or a smooth-solution existence theorem.')
    (HERE/'MAXWELL_ENTROPY_ENERGY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(checks),'PASS',flush=True)


if __name__=='__main__': main()
