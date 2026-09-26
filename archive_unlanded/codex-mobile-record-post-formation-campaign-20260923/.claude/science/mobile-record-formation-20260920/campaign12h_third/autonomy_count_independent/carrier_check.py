#!/usr/bin/env python3
"""Independent packet identities and a finite gated-rail matrix control."""
from __future__ import annotations

import json
import math
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.linalg import expm
from scipy.special import jv

OUT = Path(__file__).resolve().parent


def rational_moments():
    rows = []
    for m in range(1, 17):
        z = math.comb(2*m, m)
        coeff = [math.comb(m, r) for r in range(m+1)]
        assert sum(c*c for c in coeff) == z
        for ell in [m, 2*m+1]:
            x = [r-ell for r in range(m+1)]
            mean_x = sum(F(xx*c*c, z) for xx, c in zip(x, coeff))
            var_x = sum(F(xx*xx*c*c, z) for xx, c in zip(x, coeff))-mean_x**2
            # J=1; all factors of i are evaluated explicitly from the i^r packet.
            adjacent = sum(F(coeff[r+1]*coeff[r], z) for r in range(m))
            two_step = sum(F(coeff[r+2]*coeff[r], z) for r in range(m-1))
            mean_v = 2*adjacent
            second_v = 2+2*two_step
            sym_xv = sum(F((2*(r-ell)+1)*coeff[r+1]*coeff[r], z) for r in range(m))
            assert mean_x == -ell+F(m, 2)
            assert var_x == F(m*m, 4*(2*m-1))
            assert mean_v == F(2*m, m+1)
            assert second_v-mean_v**2 == F(4*(2*m+1), (m+1)**2*(m+2))
            assert sym_xv-mean_x*mean_v == 0
            rows.append({"M":m,"L":ell,"mean_X":str(mean_x),"variance_X":str(var_x),
                         "mean_V_J1":str(mean_v),"variance_V_J1":str(second_v-mean_v**2),
                         "symmetric_covariance":0})
    return rows


def directional_and_bessel_checks():
    mp.mp.dps = 60
    rows = []
    for m in [1,2,3,4,8,16]:
        delta = mp.betainc(m+mp.mpf('0.5'), mp.mpf('0.5'), 0, mp.mpf('0.5'), regularized=True)
        upper = mp.mpf(2)**(m-1)/math.comb(2*m,m)
        assert 0 < delta < upper
        if m == 1:
            assert abs(delta-(mp.mpf('0.5')-1/mp.pi)) < mp.mpf('1e-50')
        if m == 2:
            assert abs(delta-(mp.mpf('0.5')-4/(3*mp.pi))) < mp.mpf('1e-50')
        ell=2*m
        v=2*m/(m+1)
        d=ell-m/2
        a=m*m/(4*(2*m-1))
        b=4*(2*m+1)/((m+1)**2*(m+2))
        threshold=2*d/v
        norm=math.sqrt(math.comb(2*m,m))
        tests=[]
        for multiple in [1,2,10,80]:
            t=multiple*threshold
            cut=int(math.ceil(2*t+ell+120))
            sites=np.arange(-cut,cut+1)
            # Exact bilateral propagator expressed by Bessel functions;
            # truncation here is numerical evidence, not the uniform proof.
            amp=sum(math.comb(m,r)*jv(sites+ell-r,2*t) for r in range(m+1))/norm
            prob=amp*amp
            mass=float(prob.sum())
            failure=float(prob[sites<=0].sum())
            bound=(a+b*t*t)/(a+b*t*t+(v*t-d)**2)
            assert abs(mass-1)<2e-10, (m,t,mass)
            assert failure <= bound+2e-10, (m,t,failure,bound)
            tests.append({"t":t,"truncation":cut,"mass":mass,"left_failure":failure,
                          "Cantelli_bound_at_t":bound})
        rows.append({"M":m,"L":ell,"directional_error":mp.nstr(delta,40),
                     "elementary_directional_upper":mp.nstr(upper,40),
                     "uniform_bound_for_t_ge_threshold":(a+b*threshold**2)/(a+b*threshold**2+d*d),
                     "threshold":threshold,"Bessel_checks":tests})
    return rows


def finite_gate():
    # The test rail is finite and reflecting: only the exact gate reduction,
    # locality and conservation are claimed for this finite matrix control.
    sites=np.arange(-6,7)
    count=len(sites)
    j=1.2
    theta=0.79
    t=0.37
    v=np.array([[0,0],[1,0]],complex)
    sf=np.array([[0,0],[1,0]],complex) # basis fuel,spent
    c=np.kron(v,sf)+np.kron(v.conj().T,sf.conj().T)
    u=expm(-1j*theta*c)
    n=np.diag([0,2])
    pf=np.diag([1,0])
    conserved=np.kron(n,np.eye(2))+2*np.kron(np.eye(2),pf)
    assert np.linalg.norm(c@conserved-conserved@c)<1e-14
    h=-j*(np.diag(np.ones(count-1),1)+np.diag(np.ones(count-1),-1))
    w=np.zeros((4*count,4*count),complex)
    for a,x in enumerate(sites):
        w[4*a:4*a+4,4*a:4*a+4]=np.eye(4) if x<=0 else u
    hg=w@np.kron(h,np.eye(4))@w.conj().T
    local=np.kron(h,np.eye(4)).astype(complex)
    zero=int(np.where(sites==0)[0][0])
    local[4*(zero+1):4*(zero+2),4*zero:4*(zero+1)]=-j*u
    local[4*zero:4*(zero+1),4*(zero+1):4*(zero+2)]=-j*u.conj().T
    locality=float(np.linalg.norm(hg-local))
    assert locality<1e-13
    rng=np.random.default_rng(921203)
    a=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    sigma=a@a.conj().T; sigma/=np.trace(sigma)
    psi=np.zeros(count,complex)
    for r in range(4):
        psi[np.where(sites==-4+r)[0][0]]=1j**r*math.comb(3,r)/math.sqrt(math.comb(6,3))
    init=np.kron(np.outer(psi,psi.conj()),sigma)
    evol=expm(-1j*t*hg)
    state=evol@init@evol.conj().T
    reduced=np.einsum('aiaj->ij',state.reshape(count,4,count,4))
    free=expm(-1j*t*h)@psi
    p=float(np.sum(abs(free[sites>=1])**2))
    predicted=(1-p)*sigma+p*u@sigma@u.conj().T
    error=float(np.linalg.norm(reduced-predicted))
    assert error<2e-13
    energy=1.7*np.kron(np.eye(count),conserved)
    comm=float(np.linalg.norm(hg@energy-energy@hg))
    assert comm<2e-13
    positive_min=float(np.linalg.eigvalsh(hg+energy+2*j*np.eye(4*count)).min())
    assert positive_min>-2e-13
    return {"finite_rail_sites":count,"right_probability":p,"mixture_residual":error,
            "single_dressed_bond_residual":locality,"rest_energy_commutator":comm,
            "shifted_positive_energy_minimum":positive_min,
            "boundary":"Finite rail verifies algebra only, not the infinite-rail asymptotic estimate."}


def main():
    result={"status":"PASS","exact_rational_moments":rational_moments(),
            "directional_and_numerical_controls":directional_and_bessel_checks(),
            "finite_gate":finite_gate(),"failed_attempts":[],
            "limits":"No author source/code used. Numerical Bessel truncations do not substitute for the analytic uniform bound."}
    (OUT/'CARRIER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
