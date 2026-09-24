#!/usr/bin/env python3
"""Small independent controls; no original cubic builder or trajectory run.

x is a real harmonic coordinate and h a compact harmonic angle. The toy
magnetic matrix is cos(h)*sigma_x; its exponential changes harmonic momentum.
This checks the new smooth-multiplier/graph estimates, not physical Gauss
selection or the provisional original two-mark effect.
"""
import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss
from numpy.polynomial.legendre import leggauss


def magnetic_vector(theta, h):
    z, dz, ddz = theta*np.cos(h), -theta*np.sin(h), -theta*np.cos(h)
    v = np.stack((np.cos(z), -1j*np.sin(z)), axis=-1)
    dv = np.stack((-np.sin(z)*dz, -1j*np.cos(z)*dz), axis=-1)
    ddv = np.stack((-np.cos(z)*dz**2-np.sin(z)*ddz,
                    1j*np.sin(z)*dz**2-1j*np.cos(z)*ddz), axis=-1)
    return v, dv, ddv


def run():
    start = time.perf_counter()
    y, w = hermgauss(48)
    w = w/math.sqrt(math.pi)
    h = 2*math.pi*np.arange(128)/128
    rows, displaced, bins = [], [], []
    for g in (0.4, 0.2, 0.1, 0.05):
        x = g*y
        boundary = -g*g*math.exp(-g*g/4)
        for theta in (0.05, 0.2, 0.5, 1.0):
            v, dv, ddv = magnetic_vector(theta, h)
            assert np.max(abs(np.sum(abs(v)**2, axis=1)-1)) < 1e-14
            # B_j e_0=sqrt(5)e_0 and M_l=diag((23+2cos x)/5,4).
            f = (23+2*np.cos(x[:,None]))*abs(v[None,:,0])**2+20*abs(v[None,:,1])**2
            f_avg = f.mean(axis=1)
            p_v = float(np.dot(w,f_avg))
            p_1 = float(np.dot(w,2*y*y*f_avg))
            contrast = p_1-p_v
            haar_factor = float(np.mean(abs(v[:,0])**2))
            identity_error = abs(contrast-haar_factor*boundary)
            assert identity_error < 5e-13
            assert abs(contrast-boundary) <= 1.1*g*g*theta
            graph = []
            for label, p, q, fourth in (
                ('vacuum',np.ones_like(y),1-y*y,3),
                ('one_particle',math.sqrt(2)*y,math.sqrt(2)*(3*y-y**3),15),
            ):
                # D_q=E_x^2+E_h(E_h+k_q), k=(+1,-1), on the full
                # two-component space; the h dependence is retained.
                d_eta = math.sqrt(5)*(q[:,None,None]*v[None,:,:]/g**2
                    -p[:,None,None]*ddv[None,:,:]
                    -1j*p[:,None,None]*dv[None,:,:]*np.array([1,-1]))
                norm_d = math.sqrt(float(np.dot(w,np.mean(np.sum(abs(d_eta)**2,axis=2),axis=1))))
                scaled = g*g*norm_d/2
                n_dv = math.sqrt(float(np.mean(np.sum(abs(dv)**2,axis=1))))
                n_ddv = math.sqrt(float(np.mean(np.sum(abs(ddv)**2,axis=1))))
                bound = math.sqrt(5)*g*g/2*(math.sqrt(fourth)/(2*g*g)+n_dv+n_ddv)
                assert scaled <= bound+1e-12
                graph.append({'state':label,'K_D_magnetic_state_norm':scaled,'analytic_upper_bound':bound})
            rows.append({'g':g,'theta':theta,'magnetic_contrast':contrast,
                'boundary_contrast':boundary,'contrast_change_over_g2_theta':(contrast-boundary)/(g*g*theta),
                'haar_averaged_factor':haar_factor,'incorrect_h_equals_zero_factor':math.cos(theta)**2,
                'exact_factor_identity_error':identity_error,'electric_graph_checks':graph})
        # A noncentered coherent Gaussian is an intentional excluded case:
        # F=theta sin(x) gives contrast of order g*theta, not g^2*theta.
        shift_mean = math.exp(-g*g/4)*math.sin(g)
        displaced.append({'g':g,'mean_sin_displaced_by_g':shift_mean,
            'mean_over_g':shift_mean/g,'mean_over_g2':shift_mean/(g*g)})
    nodes, weights = leggauss(48)
    for beta in (0.1,0.5,1.0):
        thetas=beta*(nodes+1)/2
        factors=np.cos(thetas[:,None]*np.cos(h[None,:]))**2
        avg=float(np.dot(weights,factors.mean(axis=1))/2)
        bins.append({'magnetic_scaled_lag_beta':beta,'bin_averaged_contrast_factor':avg,
                     'boundary_coefficient_factor':1.0})
        assert avg < 1 and avg > 0
    result={'scope':'Independent two-state smooth-multiplier and graph-domain machinery controls, not an original-cube simulation.',
        'limitations':['Original Gauss covariance and two-mark coefficients are premises, not numerically checked here.',
                       'The Gaussian coordinate is a harmonic reference, not a compact-cutoff trajectory.',
                       'Finite quadrature checks are not interval enclosures.',
                       'A fixed harmonic angle is not the correct initial harmonic projection.',
                       'The magnetic-only toy does not settle the full original model at larger lags.'],
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python':platform.python_version(),'numpy':np.__version__,'rows':rows,
        'excluded_displaced_state_rows':displaced,'fixed_magnetic_bin_rows':bins,
        'elapsed_seconds':time.perf_counter()-start,'all_assertions_passed':True}
    text=json.dumps(result,indent=2,allow_nan=False)+'\n'
    Path(__file__).with_name('CONTROL_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':
    run()
