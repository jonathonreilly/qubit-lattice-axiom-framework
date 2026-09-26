#!/usr/bin/env python3
"""Unfitted six-species smooth-profile targets for the declared native-birth screen."""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
VELOCITY=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=float)
FIELD=np.array([[1]*6,[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1],
                 [1,1,-1,-1,0,0],[1,1,1,1,-2,-2]],dtype=float)


def current_and_source(p,beta,j):
    rho=p.sum(axis=0);vacancy=1-rho
    g=VELOCITY.T@p
    f=VELOCITY[:,0];feature=2-3*f*f
    S=feature@p
    J=p*(S[None,:]*f[:,None]+(feature[:,None]-2*S[None,:])*g[0][None,:])
    B=beta*vacancy[None,:]*(1+j*(VELOCITY@g))**6
    return J,B


def continuum(j,grid,amplitude=.04,beta=.04):
    x=np.arange(grid)/grid;times=np.linspace(0,2.5,65)
    pinit=np.tile((.5+amplitude*np.cos(2*np.pi*x))/6,(6,1))
    frequencies=np.fft.fftfreq(grid,d=1/grid)
    def rhs(t,y):
        p=y.reshape(6,grid);J,B=current_and_source(p,beta,j)
        gradient=np.fft.ifft(2j*np.pi*frequencies[None,:]*np.fft.fft(J,axis=1),axis=1).real
        return (-gradient+B).ravel()
    result=solve_ivp(rhs,(times[0],times[-1]),pinit.ravel(),t_eval=times,
                     method='DOP853',rtol=1e-9,atol=1e-12)
    assert result.success,result.message
    profiles=result.y.T.reshape(len(times),6,grid)
    fields=np.einsum('ab,tbx->tax',FIELD,profiles)
    transform=np.fft.fft(fields,axis=2)/grid
    modes=transform[:,:,:4].transpose(0,2,1)
    probabilities=np.concatenate((1-profiles.sum(axis=1)[:,None,:],profiles),axis=1)
    tail=np.abs(transform[:,:,np.abs(frequencies)>grid/4])
    diagnostics=dict(j=j,grid=grid,amplitude=amplitude,beta=beta,
       function_evaluations=result.nfev,minimum_sampled_probability=float(probabilities.min()),
       maximum_high_mode_tail=float(np.max(tail)),
       maximum_transverse_vector=float(np.max(np.abs(fields[:,2:4]))),
       maximum_transverse_axis_difference=float(np.max(np.abs(profiles[:,2]+profiles[:,3]-profiles[:,4]-profiles[:,5]))))
    assert diagnostics['minimum_sampled_probability']>0
    if j==0:
        target=1-.5*np.exp(-6*beta*times)
        diagnostics['uniform_birth_exact_mean_density_error']=float(np.max(np.abs(modes[:,0,0]-target)))
        assert diagnostics['uniform_birth_exact_mean_density_error']<1e-9
    return times,modes,diagnostics


def linear_target(j,beta=.04,amplitude=.04):
    times=np.linspace(0,2.5,65);K=2*np.pi
    def rhs(t,y):
        rho=1-.5*np.exp(-6*beta*t)
        a=2*rho*(1-rho);b=2*rho/3
        lam=12*beta*j*(1-rho)
        return np.array([-6*beta*y[0]-1j*K*a*y[1],-1j*K*b*y[0]+lam*y[1]])
    result=solve_ivp(rhs,(0,2.5),np.array([amplitude/2+0j,0j]),t_eval=times,
                     method='DOP853',rtol=1e-12,atol=1e-14)
    assert result.success
    return result.y.T


def main():
    output=HERE/'admissibility_wave_continuum_targets';output.mkdir(exist_ok=True)
    summary=[]
    for j in (0.,.5,.9):
        runs=[]
        for grid in (64,128,256):
            times,modes,diagnostics=continuum(j,grid)
            runs.append((modes,diagnostics));print(json.dumps(diagnostics),flush=True)
        coarse,medium,fine=[r[0] for r in runs]
        discrepancy64=float(np.max(np.abs(coarse-fine)));discrepancy128=float(np.max(np.abs(medium-fine)))
        assert discrepancy128<1e-7,'Reference mode resolution gate failed; inspect before using targets.'
        linear=linear_target(j)
        _,half,halfdiag=continuum(j,128,amplitude=.02)
        full_difference=float(np.max(np.abs(fine[:,1,:2]-linear)))
        half_difference=float(np.max(np.abs(half[:,1,:2]-linear/2)))
        path=output/f'j{int(10*j):02d}.npz'
        np.savez_compressed(path,times=times,fields=fine,linear_density_longitudinal=linear,
                            half_amplitude_fields=half,fields_grid64=coarse,fields_grid128=medium)
        record=dict(j=j,diagnostics=[r[1] for r in runs],half_amplitude_diagnostics=halfdiag,
                    max_mode_difference_grid64_vs256=discrepancy64,max_mode_difference_grid128_vs256=discrepancy128,
                    maximum_first_mode_finite_amplitude_minus_linear=full_difference,
                    maximum_half_amplitude_first_mode_minus_linear=half_difference,
                    raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        summary.append(record)
    times=np.linspace(0,2.5,65);control=linear_target(0,beta=0)
    exact=.02*np.cos((2*np.pi/np.sqrt(6))*times)
    error=float(np.max(np.abs(control[:,0]-exact)))
    assert error<1e-11
    report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                cases=summary,stationary_acoustic_linear_control_error=error,
                scope='Numerical Fourier collocation solutions of the specified continuum equation, computed without inspecting the large-lattice outcomes. Resolution and sampled positivity checks do not prove PDE existence or convergence of the stochastic process.')
    (HERE/'ADMISSIBILITY_WAVE_CONTINUUM_TARGETS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)


if __name__=='__main__': main()
