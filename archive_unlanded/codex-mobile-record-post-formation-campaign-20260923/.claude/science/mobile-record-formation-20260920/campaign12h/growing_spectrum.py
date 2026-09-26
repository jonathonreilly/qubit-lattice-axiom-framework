#!/usr/bin/env python3
"""Empty-start spectrum probe for the calibrated continuous-time generator.

This version explicitly varies the motion proposal intensity. The event kernel
is checked against the earlier implementation before its new outputs are used.
Only per-trajectory observables and shell averages are saved, not full histories.
"""
from pathlib import Path
import argparse
import hashlib
import json
import time
import numpy as np
from numba import njit
from growing_sim import (AXES, COLS, birth_values, fenwick_add, fenwick_total,
                         fenwick_select, refresh, observe, geometry, weights)


@njit(cache=True)
def sampled_trajectory(seed, nb, edges, ball, phase, W, epsilon, rho0, taus,
                       theta, mobility, max_events):
    np.random.seed(seed)
    n = len(nb); s = np.zeros(n, np.int64); M0 = np.zeros(3); N = 0
    for x in range(n):
        if np.random.random() < rho0:
            a = 1+np.random.randint(6); s[x] = a; N += 1
            for i in range(3):
                M0[i] += AXES[a,i]
    rates = np.zeros(n); tree = np.zeros(n+1)
    for x in range(n):
        rates[x] = birth_values(s,x,nb,W).sum()
        fenwick_add(tree,x,rates[x])
    out = np.zeros((len(taus),12))
    snapshots = np.zeros((len(taus),n),np.int8)
    t = 0.; hops = 0; events = 0
    edge_rate = mobility*len(edges)
    for kt in range(len(taus)):
        target = taus[kt]/(6*epsilon)
        while t < target and N < n:
            totalB = fenwick_total(tree); R = edge_rate+epsilon*totalB
            wait = -np.log(max(np.random.random(),1e-300))/R
            if t+wait > target:
                t = target; break
            t += wait; events += 1
            if events > max_events:
                raise RuntimeError('declared event budget exceeded')
            choose = np.random.random()*R
            if choose < edge_rate:
                k = np.random.randint(len(edges)); x,y = edges[k]
                if (s[x] == 0) == (s[y] == 0):
                    continue
                if s[x] == 0:
                    x,y = y,x
                a = s[x]; old = 1.; new = 1.
                for k in range(nb.shape[1]):
                    old *= W[a,s[nb[x,k]]]
                    u = nb[y,k]
                    if u != x:
                        new *= W[a,s[u]]
                if np.random.random() < new/(old+new):
                    s[y] = a; s[x] = 0; hops += 1
                    refresh(s,x,y,nb,W,rates,tree)
            else:
                x = fenwick_select(tree,np.random.random()*totalB)
                if x >= n or s[x] != 0:
                    raise RuntimeError('invalid birth-hazard selection')
                bv = birth_values(s,x,nb,W)
                a = 0; u = np.random.random()*bv.sum(); partial = 0.
                for k in range(6):
                    partial += bv[k]
                    if u < partial:
                        a = k+1; break
                if a == 0:
                    raise RuntimeError('invalid content selection')
                s[x] = a; N += 1
                refresh(s,x,-1,nb,W,rates,tree)
        if N == n:
            t = target
        assert abs(fenwick_total(tree)-rates.sum()) < 1e-7*max(1.,rates.sum())
        out[kt,:10] = observe(s,M0,nb,edges,ball,phase,W,epsilon,theta)
        # The imported local-residual diagnostic assumes mobility one. Suppress
        # it explicitly for other intensities; the remaining moments are valid.
        if mobility != 1.:
            out[kt,9] = np.nan
        out[kt,10] = hops/n; out[kt,11] = events/n
        snapshots[kt] = s
    return out,snapshots


def shell_geometry(side, dim):
    signed = np.rint(np.fft.fftfreq(side)*side).astype(int)
    coords = np.array(np.meshgrid(*([signed]*dim),indexing='ij'))
    squared = np.sum(coords*coords,axis=0).reshape(-1)
    labels,inverse,counts = np.unique(squared,return_inverse=True,return_counts=True)
    return labels,inverse,counts


def spectra(snapshots, side, dim):
    n = side**dim
    labels,inverse,counts = shell_geometry(side,dim)
    shells = np.empty((len(snapshots),len(labels),4))
    for kt,s in enumerate(snapshots):
        field = AXES[s].reshape((side,)*dim+(3,))
        transform = np.fft.fftn(field,axes=tuple(range(dim)))
        vector_power = np.sum(abs(transform)**2,axis=-1)/n
        occupied = (s != 0).reshape((side,)*dim)
        density_power = abs(np.fft.fftn(occupied))**2/n
        vector_corr = np.fft.ifftn(vector_power).real
        density_corr = np.fft.ifftn(density_power).real
        rho = occupied.mean()
        assert abs(vector_power.sum()/n-rho) < 1e-10
        assert abs(density_power.sum()/n-rho) < 1e-10
        assert abs(vector_corr.flat[0]-rho) < 1e-10
        assert abs(density_corr.flat[0]-rho) < 1e-10
        for c,values in enumerate((vector_power,density_power,vector_corr,density_corr)):
            shells[kt,:,c] = np.bincount(inverse,weights=values.reshape(-1))/counts
    return shells,labels,counts


def run(args):
    assert args.side >= 3 and 1 <= args.dim <= 3
    assert min(args.p,args.q,args.r,args.epsilon) > 0
    assert 0 <= args.rho0 < 1 and args.mobility >= 0 and args.reps >= 2
    assert args.steps >= 2 and args.tau_max > 0
    if args.out.exists() or args.out.with_suffix('.npz').exists():
        raise RuntimeError('Refusing to overwrite previous evidence')
    nb,edges,ball,phase = geometry(args.side,args.dim)
    W = weights(args.p,args.q,args.r)
    theta = 6*(args.p-args.q)/(args.p+args.q+4*args.r)
    taus = np.linspace(0,args.tau_max,args.steps)
    raw = np.empty((args.reps,args.steps,12)); spectral = []
    began = time.monotonic()
    for k in range(args.reps):
        values,snapshots = sampled_trajectory(args.seed+k,nb,edges,ball,phase,W,
            args.epsilon,args.rho0,taus,theta,args.mobility,args.max_events)
        raw[k] = values
        shells,labels,counts = spectra(snapshots,args.side,args.dim)
        # Independent direct-sum versus FFT diagnostics, including empty frames.
        assert np.allclose(shells[:,0,0],values[:,1],atol=1e-10)
        unit_shell = int(np.flatnonzero(labels == 1)[0])
        assert np.allclose(shells[:,unit_shell,0],values[:,2],atol=1e-10)
        spectral.append(shells)
    spectral = np.asarray(spectral)
    # NaN residual outside its domain is stored in NPZ; JSON declares validity
    # and uses null for unavailable values instead of nonstandard JSON NaN.
    means = raw.mean(axis=0); errors = raw.std(axis=0,ddof=1)/np.sqrt(args.reps)
    def clean(array):
        return [[None if not np.isfinite(x) else float(x) for x in row] for row in array]
    here = Path(__file__).resolve()
    meta = {'scope':'Finite-system spectrum measurements; no phase or force inference.',
            'side':args.side,'dimension':args.dim,'vertices':args.side**args.dim,
            'raw_weights':[args.p,args.q,args.r],'normalized_weights':W.tolist(),
            'epsilon':args.epsilon,'mobility':args.mobility,'rho0':args.rho0,
            'replicates':args.reps,'seed_start':args.seed,'seed_end':args.seed+args.reps-1,
            'taus':taus.tolist(),'tau_definition':'6 epsilon t','columns':COLS,
            'shell_squared_integer_radius':labels.tolist(),'shell_multiplicity':counts.tolist(),
            'spectral_columns':['vector_structure_per_site','density_structure_per_site',
                                'vector_pair_correlation','density_pair_correlation'],
            'density_structure_note':'Uncentered. At zero wave number subtract V*(ensemble mean density)^2 to obtain the connected density structure factor.',
            'radius_note':'The same integer shells index wave numbers 2 pi n/L and shortest periodic spatial displacements n; they are distinct axes.',
            'local_residual_valid':args.mobility == 1.,
            'mean':clean(means),'standard_error':clean(errors),
            'spectral_mean':spectral.mean(axis=0).tolist(),
            'spectral_standard_error':(spectral.std(axis=0,ddof=1)/np.sqrt(args.reps)).tolist(),
            'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in (here,here.with_name('growing_sim.py'))},
            'elapsed_seconds':time.monotonic()-began}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(meta,indent=2,allow_nan=False)+'\n')
    np.savez_compressed(args.out.with_suffix('.npz'),raw=raw,spectra=spectral,
                        taus=taus,shell_squared_radius=labels,shell_multiplicity=counts)
    print(json.dumps({k:meta[k] for k in ('side','raw_weights','epsilon','mobility',
        'rho0','replicates','elapsed_seconds','source_sha256')},indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name,default in (('side',8),('dim',3),('reps',512),('seed',20273000),
                         ('steps',21),('max-events',50_000_000)):
        parser.add_argument('--'+name,type=int,default=default)
    for name,default in (('p',3.),('q',1.),('r',2.),('epsilon',.1),('rho0',0.),
                         ('mobility',1.),('tau-max',4.)):
        parser.add_argument('--'+name,type=float,default=default)
    parser.add_argument('--out',type=Path,required=True)
    run(parser.parse_args())
