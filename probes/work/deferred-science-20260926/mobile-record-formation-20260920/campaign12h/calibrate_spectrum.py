#!/usr/bin/env python3
"""Cross-generator, pathwise, and direct Fourier controls for the new probe."""
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.sparse.linalg import expm_multiply
from growing_sim import trajectory, geometry, weights, AXES
from growing_spectrum import sampled_trajectory, spectra, shell_geometry
from growing_exact import direct_generator

HERE = Path(__file__).resolve().parent


def run():
    taus = np.linspace(0,4,21)
    pathwise = 0
    for dim,side in ((1,4),(3,4)):
        nb,edges,ball,phase = geometry(side,dim)
        for p,q,r in ((1,1,1),(3,1,2),(12,1,2)):
            W = weights(p,q,r); theta = 6*(p-q)/(p+q+4*r)
            for rho0 in (0.,.25):
                for seed in range(20274000,20274012):
                    old = trajectory(seed,nb,edges,ball,phase,W,.1,rho0,taus,theta,1_000_000)
                    new,_ = sampled_trajectory(seed,nb,edges,ball,phase,W,.1,rho0,taus,theta,1.,1_000_000)
                    assert np.array_equal(old,new)
                    pathwise += 1
    # All Fourier modes and real-space displacements against explicit sums.
    rng = np.random.default_rng(720923); fourier_cases = 0
    for dim,side in ((1,4),(2,3),(3,3)):
        n = side**dim
        coords = np.array(list(np.ndindex((side,)*dim)))
        labels,inverse,counts = shell_geometry(side,dim)
        for _ in range(12):
            s = rng.integers(7,size=n,dtype=np.int8)
            got,_,_ = spectra(s[None],side,dim)
            vec = AXES[s]; occ = (s != 0).astype(float)
            manual = np.zeros((n,4))
            for k,qvec in enumerate(coords):
                wave = np.exp(2j*np.pi*(coords@qvec)/side)
                manual[k,0] = np.sum(abs(wave@vec)**2)/n
                manual[k,1] = abs(wave@occ)**2/n
                shift = np.ravel_multi_index(tuple(((coords+qvec)%side).T),(side,)*dim)
                manual[k,2] = np.sum(vec*vec[shift])/n
                manual[k,3] = np.dot(occ,occ[shift])/n
            expected = np.column_stack([np.bincount(inverse,weights=manual[:,i])/counts for i in range(4)])
            assert np.allclose(got[0],expected,atol=1e-10)
            fourier_cases += 1
    # Empty-state laws on all 7^4 states, global-weight transition assembly.
    comparisons = []
    n = 4; nb,edges,ball,phase = geometry(n,1)
    for p,q,r in ((1,1,1),(3,1,2),(12,1,2)):
        W = weights(p,q,r); theta = 6*(p-q)/(p+q+4*r)
        states,Q,_ = direct_generator(n,edges,W,.1)
        _,H,_ = direct_generator(n,edges,W,0.)
        N = np.count_nonzero(states,axis=1)
        M = AXES[states].sum(axis=1)
        F = np.einsum('sxi,x->si',AXES[states],np.exp(2j*np.pi*np.arange(n)/n))
        observables = np.column_stack((N,np.sum(M*M,axis=1),np.sum(abs(F)**2,axis=1)))/n
        initial = np.zeros(len(states)); initial[0] = 1
        for mobility in (0.,1.):
            generator = (Q+(mobility-1)*H).T/.6
            laws = expm_multiply(generator,initial,start=0,stop=4,num=21,
                                 traceA=generator.diagonal().sum())
            exact = laws@observables
            raw = np.empty((8192,21,3))
            for k in range(len(raw)):
                values,_ = sampled_trajectory(20275000+k,nb,edges,ball,phase,W,.1,0.,taus,
                                               theta,mobility,1_000_000)
                raw[k] = values[:,:3]
            mean = raw.mean(axis=0); se = raw.std(axis=0,ddof=1)/np.sqrt(len(raw))
            error = abs(mean-exact)
            assert np.all(error[se == 0] < 1e-11)
            standardized = np.divide(error,se,out=np.zeros_like(error),where=se > 0)
            maximum = float(standardized.max())
            assert maximum < 5., maximum
            case = f'p{p}_mobility{mobility}'
            np.savez_compressed(HERE/f'spectrum_calibration_{case}.npz',raw=raw,exact=exact,taus=taus)
            comparisons.append({'case':case,'replicates':len(raw),'maximum_standardized_error':maximum,
                                'mean':mean.tolist(),'standard_error':se.tolist(),'exact':exact.tolist()})
            print(case,maximum,flush=True)
    report = {'scope':'Five-SE distributional sanity gate; not a formal confidence certificate.',
              'pathwise_identical_cases':pathwise,'direct_Fourier_and_displacement_cases':fourier_cases,
              'source_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in
                  (Path(__file__),HERE/'growing_spectrum.py',HERE/'growing_sim.py',HERE/'growing_exact.py')},
              'comparisons':comparisons}
    (HERE/'SPECTRUM_CALIBRATION.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    run()
