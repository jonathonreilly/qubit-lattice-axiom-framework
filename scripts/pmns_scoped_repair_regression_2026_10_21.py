#!/usr/bin/env python3
"""Discriminating author checks for the four scoped B05 calculation repairs.

Synthetic PMNS phases are held inputs; no source fit or target changes occur.
Exact symbolic checks use separately specified matrices/series. These are
independent calculations by the author, not independent peer review.
"""
import math
import numpy as np
import sympy as sp
from frontier_pmns_from_dm_neutrino_source_h_diagonalization_closure_theorem import (
    observables_from_pmns, pmns_observables,
)
from frontier_dm_neutrino_source_surface_info_geometric_selection_obstruction import gaussian_kl2
from frontier_dm_neutrino_source_surface_active_affine_point_selection_boundary import active_affine_h
from frontier_dm_neutrino_source_surface_active_half_plane_theorem import q_floor
from frontier_dm_split2_interval_certified_dominance_closure_2026_04_21 import (
    L_DELTA, T_DELTA, T_Q, CAP_BOX, ENDPOINT_BOX, estimate_box,
)


def pdg_unitary(delta_deg):
    s12,s13,s23 = .55,.15,.70
    c12,c13,c23 = [math.sqrt(1-s*s) for s in (s12,s13,s23)]
    z=np.exp(1j*math.radians(delta_deg))
    return np.array([[c12*c13,s12*c13,s13/z],
      [-s12*c23-c12*s23*s13*z,c12*c23-s12*s23*s13*z,s23*c13],
      [s12*s23-c12*c23*s13*z,-c12*s23-s12*c23*s13*z,c23*c13]])


def main():
    # All quadrants, arbitrary row/column rephasing, and conjugation.
    for phase in (35.,145.,215.,325.):
        U=pdg_unitary(phase)
        for V, expected in [(U,phase),
            (np.diag(np.exp(1j*np.array([.2,.4,.9])))@U@np.diag(np.exp(1j*np.array([.7,-.1,.3]))),phase),
            (U.conj(),(-phase)%360)]:
            obs=observables_from_pmns(V)
            assert abs((obs['dcp_deg']-expected+180)%360-180)<1e-10
            assert abs(obs['sin_dcp']**2+obs['cos_dcp']**2-1)<1e-12
    assert math.isnan(observables_from_pmns(np.eye(3))['dcp_deg'])
    obs=pmns_observables(.657061,.933806,.715042)
    # Independently reconstruct cosine from the muon-second modulus identity.
    a,b,c=obs['s12sq'],obs['s13sq'],obs['s23sq']
    cos2=((1-a)*(1-c)+a*c*b-abs(obs['PMNS'][1,1])**2)/(2*math.sqrt(a*(1-a)*c*(1-c)*b))
    assert abs(cos2-obs['cos_dcp'])<1e-12
    assert 180<obs['dcp_deg']<270
    assert abs(obs['dcp_deg']-(math.degrees(math.asin(obs['sin_dcp']))%360))>10
    print('PHASE quadrant/rephasing/conjugation passed; pin =',obs['dcp_deg'])

    x=sp.symbols('x')
    series=sp.series(1/(1+x)-1+sp.log(1+x),x,0,4).removeO()
    assert sp.expand(series-(x*x/2-2*x**3/3))==0
    wrong=sp.series(1/(1+x)-1-sp.log(1+x),x,0,4).removeO()
    assert wrong.coeff(x,2)==sp.Rational(3,2)
    # Independent covariance formula at a nonsingular noninfinitesimal point.
    D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],float)
    Q=np.ones((3,3))-np.eye(3)
    for m,d,q in [(1.,.05,.1),(2.,-.2,.15),(3.,.1,-.3)]:
        H=m*np.eye(3)+d*D+q*Q
        C=m*np.linalg.inv(H)
        expected=np.trace(C)-3-np.linalg.slogdet(C)[1]
        assert abs(gaussian_kl2(d,q,m)-expected)<1e-12
        assert expected>0
    errors=[]
    for eps in (.02,.01,.005):
        value=gaussian_kl2(0,eps)
        approx=3*eps**2-4*eps**3 # tr J^3=6 q^3
        errors.append(abs(value-approx))
    assert errors[0]/errors[1]>14 and errors[1]/errors[2]>14
    for args in [(0,0,0),(0,0,-1),(math.sqrt(6)/3,math.sqrt(6)/3,1)]:
        try: gaussian_kl2(*args)
        except ValueError: pass
        else: raise AssertionError('invalid Gaussian domain accepted')
    print('KL scalar series, covariance formula, fourth-order residual and domain passed',errors)

    exactD=sp.Matrix(D.astype(int));exactQ=sp.ones(3)-sp.eye(3)
    assert set((exactD-exactQ).eigenvals())=={-2,1-sp.sqrt(3),1+sp.sqrt(3)}
    assert abs(L_DELTA-(1+math.sqrt(3)))<1e-12
    m,d,slack=.1,1.1,.02;eps=1e-6
    tangent=(active_affine_h(m,d+eps,q_floor(d+eps)+slack)-active_affine_h(m,d-eps,q_floor(d-eps)+slack))/(2*eps)
    assert np.max(abs(tangent-(T_DELTA-T_Q)))<1e-8
    for label,box in [('CAP',CAP_BOX),('ENDPOINT',ENDPOINT_BOX)]:
        result=estimate_box(label,box)
        print('NUMERICAL SUPPORT',label,'radius',result['radius'],'eta',result['row_eta_ubs'])
        assert max(result['row_eta_ubs'])<1
    print('All discriminating author regression checks passed; no rigorous transport certificate claimed.')


if __name__=='__main__':
    main()
