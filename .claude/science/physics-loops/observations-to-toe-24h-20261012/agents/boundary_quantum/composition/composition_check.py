#!/usr/bin/env python3
"""Frozen pair-law composition tests; one CPU, no empirical data fitting.

Run from any directory: python3 /absolute/path/composition_check.py
Results are new local files in this script's directory. Existing freeze files
are never changed. mpmath interval midpoint bounds are numerical enclosures,
not a formal verification of the interval library or transcendental backend.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
import hashlib
import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.optimize import differential_evolution
from scipy.special import eval_legendre, roots_legendre

HERE = Path(__file__).resolve().parent
CAMPAIGN = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')

def guard():
    deadline = json.loads((CAMPAIGN / 'DEADLINE.json').read_text())['deadline_epoch']
    if time.time() >= deadline:
        raise SystemExit('Campaign deadline reached')
    for name in ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json', 'STOP_REQUESTED', 'USER_STOP_REQUESTED'):
        if (CAMPAIGN / name).exists():
            raise SystemExit('Campaign stop marker present: ' + name)

def dump(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')

def f(c, k):
    c = np.clip(np.asarray(c, dtype=float), -1., 1.)
    u = (2 / np.pi) * np.arcsin(c)
    with np.errstate(divide='ignore', invalid='ignore'):
        out = np.tanh(np.arctanh(u) + k*c)
    return np.where(c == 1, 1., np.where(c == -1, -1., out))

def fm(c, k):
    if abs(c) == 1:
        return c
    return mp.tanh(mp.atanh(2*mp.asin(c)/mp.pi) + k*c)

def a3mp(k):
    # theta substitution removes the endpoint arcsine cusp.
    return 7*mp.quad(lambda t: fm(mp.cos(t), k)*mp.legendre(3, mp.cos(t))*mp.sin(t), [0, mp.pi/4, mp.pi/2])

def legendre_coefficients(k, order):
    nodes, weights = roots_legendre(order)
    theta = (nodes+1)*np.pi/4
    c = np.cos(theta)
    base = f(c, k)*np.sin(theta)*weights*np.pi/4
    return [(2*l+1)*float(np.dot(base, eval_legendre(l, c))) for l in range(1,32,2)]

def a3_interval_midpoint(k, n=4096):
    # |d/dtheta[g(theta) P3(cos theta) sin theta]| <= 2/pi+k+7.
    # Composite midpoint error <= L*(pi/2)^2/(4*n), multiplied by 7.
    iv = mp.iv
    iv.dps = 35
    ki = iv.mpf(str(k))
    total = iv.mpf(0)
    width = iv.pi/(2*n)
    for j in range(n):
        theta = (iv.mpf(j)+iv.mpf('0.5'))*width
        c = iv.cos(theta)
        u = 1-2*theta/iv.pi
        z = iv.log((1+u)/(1-u))/2 + ki*c
        ez = iv.exp(2*z)
        g = (ez-1)/(ez+1)
        total += g*(5*c**3-3*c)/2*iv.sin(theta)
    estimate = 7*width*total
    err = 7*(2/iv.pi+ki+7)*(iv.pi/2)**2/(4*n)
    enclosure = estimate + iv.mpf([-1,1])*err
    return {
        'n': n,
        'lower': float(np.nextafter(float(enclosure.a), -np.inf)),
        'upper': float(np.nextafter(float(enclosure.b), np.inf)),
        'analytic_error_bound_upper': float(np.nextafter(float(err.b), np.inf)),
        'arithmetic': 'mpmath.iv 35 decimal digits; outward expanded binary64 endpoints; not formally verified'
    }

def geometries():
    output = {
        'equilateral': np.array([[1,0,0],[-.5,np.sqrt(3)/2,0],[-.5,-np.sqrt(3)/2,0]]),
        'tetrahedron': np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]])/np.sqrt(3)
    }
    for n in range(3,33):
        t = 2*np.pi*np.arange(n)/n
        output[f'polygon_{n}'] = np.column_stack((np.cos(t),np.sin(t),np.zeros(n)))
    golden_angle = np.pi*(3-np.sqrt(5))
    for n in (12,24,48,96):
        j = np.arange(n)
        z = 1-2*(j+.5)/n
        r = np.sqrt(1-z*z)
        output[f'fibonacci_{n}'] = np.column_stack((r*np.cos(j*golden_angle),r*np.sin(j*golden_angle),z))
    return output

def gram(directions, k):
    dots = directions @ directions.T
    # Avoid endpoint amplification of direction-coordinate rounding.
    dots[np.abs(dots-1)<2e-14] = 1.
    dots[np.abs(dots+1)<2e-14] = -1.
    return f(dots, k)

def chsh_general(parameters, k):
    # Rotational gauge: a0=z, a1 in xz plane; remaining directions arbitrary.
    alpha, tb0, pb0, tb1, pb1 = parameters
    a0 = np.array([0.,0.,1.])
    a1 = np.array([np.sin(alpha),0.,np.cos(alpha)])
    b0 = np.array([np.sin(tb0)*np.cos(pb0),np.sin(tb0)*np.sin(pb0),np.cos(tb0)])
    b1 = np.array([np.sin(tb1)*np.cos(pb1),np.sin(tb1)*np.sin(pb1),np.cos(tb1)])
    return float(f(a0@b0,k)+f(a1@b0,k)+f(a0@b1,k)-f(a1@b1,k))

def bell_probabilities(E):
    # Last two axes are A=(+1,-1), B=(+1,-1), with fair marginals.
    E = np.asarray(E)
    output = np.empty(E.shape+(2,2))
    output[...,0,0] = output[...,1,1] = (1+E)/4
    output[...,0,1] = output[...,1,0] = (1-E)/4
    return output

def quantum_construction(h, visibility):
    p = np.ones((3,3))/3
    eye = np.eye(3)
    G = (1+h)*eye-h*np.ones((3,3))
    t = max(1.,(1+4*h)/3)
    if visibility*t > 1+1e-13:
        return {'feasible': False, 'reason': 'nuclear norm exceeds 3'}
    sign = eye-2*p if h>.5 else eye
    L = np.sqrt(1+h)*(eye-p)+np.sqrt(abs(1-2*h))*p
    slack = np.sqrt(max(0.,1-visibility*t))
    X = np.column_stack((np.sqrt(visibility)*L, np.full(3,slack),np.zeros(3)))
    Y = np.column_stack((np.sqrt(visibility)*(sign@L),np.zeros(3),np.full(3,slack)))
    sigma_x = np.array([[0,1],[1,0]],complex)
    sigma_y = np.array([[0,-1j],[1j,0]],complex)
    sigma_z = np.diag([1.,-1.])
    I2 = np.eye(2)
    gamma = np.array([np.kron(sigma_x,I2),np.kron(sigma_y,I2),np.kron(sigma_z,sigma_x),np.kron(sigma_z,sigma_y),np.kron(sigma_z,sigma_z)])
    A = np.einsum('il,ljk->ijk',X,gamma)
    B = -np.einsum('il,lkj->ijk',Y,gamma) # transpose for maximally entangled state
    quantum_E = np.array([[np.trace(A[i]@B[j].T).real/4 for j in range(3)] for i in range(3)])
    residuals = {
        'unit_row_norm': max(float(np.max(np.abs(np.sum(X*X,axis=1)-1))),float(np.max(np.abs(np.sum(Y*Y,axis=1)-1)))),
        'cross_factor': float(np.max(np.abs(X@Y.T-visibility*G))),
        'A_squared_identity': float(np.max(np.abs(A@A-np.eye(4)))),
        'B_squared_identity': float(np.max(np.abs(B@B-np.eye(4)))),
        'quantum_correlators': float(np.max(np.abs(quantum_E+visibility*G))),
        'marginals': max(float(np.max(np.abs(np.trace(A,axis1=1,axis2=2)))),float(np.max(np.abs(np.trace(B,axis1=1,axis2=2)))))/4
    }
    return {'feasible':True,'local_Hilbert_dimension':4,'X':X.tolist(),'Y':Y.tolist(),'quantum_E':quantum_E.tolist(),'residuals':residuals}

def main():
    guard()
    started = datetime.now(timezone.utc).isoformat()
    freeze = json.loads((HERE/'PRECOMPUTE_FREEZE.json').read_text())
    visibility_freeze = json.loads((HERE/'VISIBILITY_EXTENSION_FREEZE.json').read_text())
    mp.mp.dps = 80
    values = freeze['k_values']
    data = geometries()
    dump('finite_directions.json', {name:dirs.tolist() for name,dirs in data.items()})
    rows = []
    for k in values:
        guard()
        km = mp.mpf(str(k))
        h = fm(mp.mpf('.5'),km)
        leg = {str(n):legendre_coefficients(k,n) for n in (256,512,1024)}
        scans = []
        for name,dirs in data.items():
            G = gram(dirs,k)
            vals, vecs = np.linalg.eigh(G)
            scans.append({'geometry':name,'n':len(dirs),'minimum_eigenvalue':float(vals[0]),'witness_weights':vecs[:,0].tolist()})
        hfloat=float(h)
        equi=(1+hfloat)*np.eye(3)-hfloat*np.ones((3,3))
        opt=differential_evolution(lambda z:-chsh_general(z,k),[(0,np.pi),(0,np.pi),(0,2*np.pi),(0,np.pi),(0,2*np.pi)],seed=8291,popsize=10,maxiter=200,tol=1e-10,polish=True,workers=1)
        chsh_exact=4*mp.tanh(mp.atanh(mp.mpf('.5'))+km/mp.sqrt(2))
        # Frozen symmetric CHSH scan is a lower-bound numerical check.
        angles=np.linspace(0,np.pi/2,20001)
        symvals=3*f(np.cos(angles),k)-f(np.cos(3*angles),k)
        symarg=int(np.argmax(symvals))
        row={
            'k':k,'h_80dps':str(h),'triangle_lambda_min_80dps':str(1-2*h),
            'triangle_ones_quadratic_form_80dps':str(3-6*h),
            'triangle_G':equi.tolist(),'triangle_E':(-equi).tolist(),
            'triangle_joint_probabilities_AB_order_plus_minus':bell_probabilities(-equi).tolist(),
            'legendre_odd_ell':list(range(1,32,2)),'legendre_by_order':leg,
            'max_legendre_512_to_1024_change':float(np.max(np.abs(np.array(leg['512'])-leg['1024']))),
            'a3_80dps':str(a3mp(km)), 'a3_midpoint_enclosure':a3_interval_midpoint(k),
            'finite_gram_scans':scans,
            'global_chsh_analytic_80dps':str(chsh_exact),
            'chsh_numerical_general':{'value':-float(opt.fun),'parameters_radians':opt.x.tolist(),'success':bool(opt.success),'iterations':int(opt.nit),'analytic_minus_numerical':float(chsh_exact)+float(opt.fun)},
            'chsh_symmetric_scan':{'angle_radians':float(angles[symarg]),'value':float(symvals[symarg]),'grid_n':len(angles)},
            'visibility_cases':[]
        }
        t=max(1.,(1+4*hfloat)/3)
        row['gamma2_G']=t
        row['visibility_critical']=1/t
        sign=np.eye(3)-2*np.ones((3,3))/3
        for V in visibility_freeze['V_cases']:
            E=-V*equi
            bell=-float(np.sum(sign*E))
            uniform_N_variance=3*(1-V*V)+24*(1-V*V*hfloat*hfloat)
            optimal_N_variance=(np.sqrt(max(0,1-V*V))+4*np.sqrt(1-V*V*hfloat*hfloat))**2
            margin=bell-3
            row['visibility_cases'].append({
                'V':V,'E':E.tolist(),'joint_probabilities_AB_order_plus_minus':bell_probabilities(E).tolist(),
                'bell_value':bell,'quantum_upper_bound':3.,'margin':margin,
                'nuclear_norm':float(np.linalg.svd(E,compute_uv=False).sum()),
                'optimal_N_times_counting_variance':float(optimal_N_variance),
                'uniform_N_times_counting_variance':float(uniform_N_variance),
                'illustrative_total_N_for_margin_5_counting_SE_optimal':float(25*optimal_N_variance/margin**2) if margin>1e-12 else None,
                'one_sigma_visibility_equal_to_margin':float(margin/(1+4*hfloat)) if margin>1e-12 else None,
                'quantum_construction':quantum_construction(hfloat,V)
            })
        rows.append(row)
        print(json.dumps({'k':k,'a3':row['a3_80dps'],'triangle_lambda':row['triangle_lambda_min_80dps'],'Vcrit':row['visibility_critical'],'Smax':row['global_chsh_analytic_80dps']}),flush=True)
    # Root value is a numerical location; unique defining integral is exact.
    a3_root=mp.findroot(a3mp,(mp.mpf('.31'),mp.mpf('.33')))
    # Check both deterministic local strategies and the explicit quantum construction.
    sign=np.eye(3)-2*np.ones((3,3))/3
    import itertools
    deterministic=[np.array(s) for s in itertools.product((-1.,1.),repeat=3)]
    local_max=max(abs(float(x@sign@y)) for x in deterministic for y in deterministic)
    results={
        'started_at':started,'completed_at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'precompute_freeze_sha256':hashlib.sha256((HERE/'PRECOMPUTE_FREEZE.json').read_bytes()).hexdigest(),
        'visibility_freeze_sha256':hashlib.sha256((HERE/'VISIBILITY_EXTENSION_FREEZE.json').read_bytes()).hexdigest(),
        'dependencies':{'numpy':np.__version__,'mpmath':mp.__version__,'scipy':__import__('scipy').__version__},
        'thresholds':{'triangle_k_exact':'log(3/2)','triangle_k_80dps':str(mp.log(mp.mpf('1.5'))),'a3_unique_root_80dps_numerical':str(a3_root),'a3_root_residual_80dps':str(a3mp(a3_root)),
                      'tetrahedron_k_80dps':str(3*(mp.atanh(mp.mpf(1)/3)-mp.atanh(2*mp.asin(mp.mpf(1)/3)/mp.pi))),
                      'chsh_tsirelson_crossing_k_80dps':str(mp.sqrt(2)*(mp.atanh(1/mp.sqrt(2))-mp.atanh(mp.mpf('.5'))))},
        'bell_sign_matrix':sign.tolist(),'bell_local_deterministic_bound':local_max,
        'rows':rows
    }
    dump('COMPUTATION_RESULTS.json',results)
    print('Wrote COMPUTATION_RESULTS.json and finite_directions.json',flush=True)

if __name__=='__main__':
    main()
