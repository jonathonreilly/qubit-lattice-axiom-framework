#!/usr/bin/env python3
"""Finite checks of the specified one-sided complex Gaussian norm test."""
import json
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss


def gaussian_vertex():
    # The six oriented faces of one free three-cube have the sole boundary
    # relation q=B n. Its exact/coexact projection split is elementary.
    boundary=np.array([1.,-1.,-1.,1.,1.,-1.])
    Q=np.outer(boundary,boundary)/6
    P=np.eye(6)-Q
    nodes,weights=hermgauss(64)
    nodes=np.sqrt(2)*nodes
    weights=weights/np.sqrt(np.pi)
    g,b=2.,np.pi
    c=g*b
    records=[]
    for si,ni in [(0,1),(0,3),(2,5)]:
        S,n=np.eye(6)[si],np.eye(6)[ni]
        covariance=np.array([[S@P@S,S@P@n],[n@P@S,n@P@n]])
        cholesky=np.linalg.cholesky(covariance)
        aS=cholesky[0,0]*nodes[:,None]+cholesky[0,1]*nodes[None,:]
        an=cholesky[1,0]*nodes[:,None]+cholesky[1,1]*nodes[None,:]
        part_A=np.sum(weights[:,None]*weights[None,:]*np.exp(1j*g*aS+b*an))
        part_B=np.sum(weights*np.exp(1j*b*np.sqrt(n@Q@n)*nodes))
        part_C=np.sum(weights*np.exp(1j*b*np.sqrt(n@P@n)*nodes))
        quadrature=part_A*part_B*part_C
        direct=np.exp(-g*g*(S@P@S)/2-b*b*(n@Q@n)/2+1j*c*(n@P@S))
        error=float(abs(quadrature-direct))
        assert error<2e-13
        absolute_quadrature=np.sum(weights*np.exp(b*np.sqrt(n@P@n)*nodes))
        absolute_exact=np.exp(b*b*(n@P@n)/2)
        assert abs(absolute_quadrature/absolute_exact-1)<2e-13
        records.append(dict(electric_face=si,magnetic_face=ni,
                            complex_identity_error=error,
                            physical_weight_modulus=float(abs(direct)),
                            absolute_magnetic_vertex=float(absolute_exact)))
    covariance_fault=np.block([[g*g*P,-c*P],[-c*P,.5*b*b*P]])
    lowest=float(np.linalg.eigvalsh(covariance_fault).min())
    assert lowest<-1
    # With P=I and integer fills, the phase is exactly one, yet the same
    # absolute Gaussian norm grows. This rejects a physical no-go inference.
    quantization=[float(abs(np.exp(2j*np.pi*N*s*n)-1))
                  for N in [1,2,5] for s in [-2,1,3] for n in [-3,1,2]]
    assert max(quantization)<1e-12
    return dict(quadratures=records,insufficient_imaginary_variance_fault_eigenvalue=lowest,
                decoupled_quantized_phase_error=max(quantization))


def planar_loops():
    records=[]
    for radius in [1,2,3,4,6,8]:
        L=max(16,4*radius)
        frequencies=2*np.sin(np.pi*np.fft.fftfreq(L))
        square=frequencies**2
        denominator=(square[:,None,None,None]+square[None,:,None,None]
                     +square[None,None,:,None]+square[None,None,None,:])
        p_numerator=square[None,None,:,None]+square[None,None,None,:]
        multiplier=np.zeros((L,)*4)
        np.divide(p_numerator,denominator,out=multiplier,where=denominator>0)
        n=np.zeros((L,)*4)
        # Primal34 two-cells indexed in a dual12 square.
        n[:radius,:radius,0,0]=1
        transformed=np.fft.fftn(n)
        Penergy=float(np.sum(abs(transformed)**2*multiplier)/L**4)
        harmonic=float(radius**4/L**4)
        Qenergy=float(np.sum(n*n)-Penergy)
        q0=np.roll(n,-1,axis=0)-n
        q1=np.roll(n,-1,axis=1)-n
        qmass=float(np.sum(abs(q0))+np.sum(abs(q1)))
        qnorm=float(np.sum(q0*q0)+np.sum(q1*q1))
        assert qmass==qnorm==4*radius
        charge_power=abs(np.fft.fftn(q0))**2+abs(np.fft.fftn(q1))**2
        green=np.zeros_like(denominator)
        np.divide(1.,denominator,out=green,where=denominator>0)
        charge_energy=float(np.sum(charge_power*green)/L**4)
        error=abs(charge_energy-(Qenergy-harmonic))
        assert error<2e-12
        records.append(dict(side=radius,torus_side=L,integer_filling_norm_squared=radius**2,
                            charge_mass=qmass,coexact_coulomb_energy=charge_energy,
                            exact_filling_energy=Penergy,harmonic_correction=harmonic,
                            charge_vs_projection_error=error,
                            exact_energy_per_area=Penergy/radius**2,
                            coulomb_energy_per_perimeter=charge_energy/(4*radius)))
    assert records[-1]['exact_energy_per_area']>records[0]['exact_energy_per_area']
    return records


if __name__=='__main__':
    print(json.dumps(dict(status='finite_checks_passed',
                         gaussian_embedding=gaussian_vertex(),
                         planar_loop_diagnostics=planar_loops(),
                         scope='Finite Gaussian quadrature and periodic cochain diagnostics; harmonic correction explicit. No phase claim or numerical proof of the infinite-lattice bound.'),indent=2))
