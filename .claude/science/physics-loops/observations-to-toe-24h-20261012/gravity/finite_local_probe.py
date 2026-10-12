#!/usr/bin/env python3
"""Finite positive local realizations: analytic error bounds and numeric probes."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import gammainc, gammaincc, gammaln, roots_genlaguerre


def local_noise(omega, shape, width):
    # mu=omega*u removes the moving endpoint and exposes the IR scaling.
    integral = quad(lambda u: u ** (shape - 1) * math.exp(-omega * u)
                    * math.sqrt(max(0.0, 1 - u * u))
                    * math.exp(-width**2 * omega**2 * (1 - u*u)),
                    0, 1, epsabs=2e-12, epsrel=2e-11)[0]
    return omega ** (shape + 1) * integral / (4 * math.pi**2 * math.gamma(shape))


def atomic_noise(omega, nodes, weights, width):
    momenta = np.sqrt(np.maximum(omega**2 - nodes**2, 0))
    return float(np.dot(weights, momenta * np.exp(-width**2 * momenta**2))) / (4 * math.pi**2)


def gauss_bound(shape, order, radius):
    return math.exp(2 * order * math.log(radius) + gammaln(order+1)
                    + gammaln(order+shape) - gammaln(2*order+1) - gammaln(shape))


def positive_bins(shape, count, cap):
    edges = np.linspace(0, cap, count+1)
    weights = np.diff(gammainc(shape, edges))
    # A retained positive tail atom preserves canonical normalization.
    tail = float(gammaincc(shape, cap))
    tail_mean = shape * float(gammaincc(shape+1, cap)) / tail
    return np.append((edges[:-1]+edges[1:])/2, tail_mean), np.append(weights, tail)


def run(contract):
    rows, checks = [], []
    def check(name, condition, **data):
        checks.append(dict(name=name, passed=bool(condition), **data))
    for shape in contract['s_grid']:
        for order in contract['gauss_orders']:
            nodes, raw = roots_genlaguerre(order, shape-1)
            weights = raw / math.gamma(shape)
            check('gauss_positive_normalized', np.all(nodes > 0) and np.all(weights > 0)
                  and abs(sum(weights)-1)<2e-14, s=shape, order=order)
            static = []
            for radius in contract['radius_grid']:
                exact = (1+radius)**(-shape)
                force = exact * (1 + shape*radius/(1+radius))
                approx = float(np.dot(weights, np.exp(-nodes*radius)))
                approx_force = float(np.dot(weights, (1+nodes*radius)*np.exp(-nodes*radius)))
                bound = gauss_bound(shape, order, radius)
                check('gauss_potential_enclosure', -3e-14 <= exact-approx <= bound+3e-14,
                      s=shape, order=order, radius=radius)
                check('gauss_force_enclosure', abs(force-approx_force) <= (2*order-1)*bound+3e-14,
                      s=shape, order=order, radius=radius)
                static.append(dict(radius=radius, potential_exact=exact, potential_approx=approx,
                                   potential_error=exact-approx, potential_bound=bound,
                                   force_error=force-approx_force, force_bound=(2*order-1)*bound))
            noise = []
            for omega in contract['frequency_grid']:
                exact = local_noise(omega, shape, contract['spatial_width'])
                approx = atomic_noise(omega, nodes, weights, contract['spatial_width'])
                noise.append(dict(omega=omega, exact=exact, approx=approx,
                                  relative_error=(approx-exact)/exact))
            below_gap = float(nodes[0]/2)
            check('explicit_spectral_gap', atomic_noise(below_gap, nodes, weights,
                  contract['spatial_width']) == 0 and local_noise(below_gap, shape,
                  contract['spatial_width']) > 0, s=shape, order=order)
            rows.append(dict(method='gauss', s=shape, order=order,
                             smallest_mass=float(nodes[0]), static=static, noise=noise))
        for count in contract['bin_counts']:
            cap = contract['bin_mass_cap']; h = cap/count
            nodes, weights = positive_bins(shape, count, cap)
            tail = weights[-1]
            check('bins_positive_normalized', np.all(nodes > 0) and np.all(weights > 0)
                  and abs(sum(weights)-1)<2e-14, s=shape, count=count)
            R = contract['radius_window_max']; Omega=contract['frequency_window_max']
            potential_bound = R*h/2 + tail
            force_bound = R*h/(2*math.e) + tail
            noise_bound = math.sqrt(Omega*h)/(4*math.pi**2)
            static=[]; noise=[]
            for radius in contract['radius_grid']:
                if radius > R: continue
                exact=(1+radius)**(-shape)
                force=exact*(1+shape*radius/(1+radius))
                approx=float(np.dot(weights,np.exp(-nodes*radius)))
                af=float(np.dot(weights,(1+nodes*radius)*np.exp(-nodes*radius)))
                check('bins_uniform_static_bounds', abs(exact-approx)<=potential_bound
                      and abs(force-af)<=force_bound,s=shape,count=count,radius=radius)
                static.append(dict(radius=radius,potential_error=exact-approx,force_error=force-af))
            for omega in contract['frequency_grid']:
                exact=local_noise(omega,shape,contract['spatial_width'])
                approx=atomic_noise(omega,nodes,weights,contract['spatial_width'])
                check('bins_uniform_noise_bound', abs(exact-approx)<=noise_bound,
                      s=shape,count=count,omega=omega)
                noise.append(dict(omega=omega,exact=exact,approx=approx,
                                  relative_error=(approx-exact)/exact))
            rows.append(dict(method='bins',s=shape,count=count,smallest_mass=float(nodes[0]),
                             tail_probability=float(tail),potential_uniform_bound=float(potential_bound),
                             force_uniform_bound=float(force_bound),noise_uniform_bound=noise_bound,
                             static=static,noise=noise))
    return dict(status='conditional-support',observations_fitted=False,
                passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks),
                checks=checks,results=rows)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output',required=True)
    args=parser.parse_args(); source=Path(__file__)
    contract_path=source.with_name('FINITE_LOCAL_CONTRACT.json')
    result=run(json.loads(contract_path.read_text()))
    result['source_sha256']=hashlib.sha256(source.read_bytes()).hexdigest()
    result['contract_sha256']=hashlib.sha256(contract_path.read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['passed','failed','source_sha256','contract_sha256']}))
    raise SystemExit(bool(result['failed']))
