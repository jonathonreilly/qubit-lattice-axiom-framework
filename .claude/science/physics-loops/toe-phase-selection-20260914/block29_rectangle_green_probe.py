#!/usr/bin/env python3
"""Direct currents, sparse Poisson solves and reduced Green quadrature."""
from pathlib import Path
import json
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg


def currents(side,r,t):
    assert max(r,t)<side
    j0=np.zeros((side,)*4);j1=np.zeros_like(j0)
    j0[:t,0,0,0]=1;j0[:t,r,0,0]=-1
    j1[t,:r,0,0]=1;j1[0,:r,0,0]=-1
    divergence=np.roll(j0,1,axis=0)-j0+np.roll(j1,1,axis=1)-j1
    assert np.max(np.abs(divergence))==0
    return j0,j1


def fft_energy(side,r,t):
    j0,j1=currents(side,r,t)
    one=2-2*np.cos(2*np.pi*np.arange(side)/side)
    lam=sum(one.reshape((1,)*i+(side,)+(1,)*(3-i)) for i in range(4))
    lam[0,0,0,0]=1
    energy=0.
    parts=[]
    for j in [j0,j1]:
        hat=np.fft.fftn(j)
        part=float(np.sum(np.abs(hat)**2/lam)/side**4)
        parts.append(part);energy+=part
    return energy,parts


def reduced_integrals(n,pairs):
    k=2*np.pi*(np.arange(n)+.5)/n-np.pi
    one=2-2*np.cos(k)
    l1=one[:,None,None]
    lam=l1+one[None,:,None]+one[None,None,:]
    root=np.sqrt(lam*(lam+4))
    exponent=2*np.arcsinh(np.sqrt(lam)/2)
    g4=float(np.mean(1/root))
    out={}
    for r,t in pairs:
        dr2=(np.sin(r*k/2)/np.sin(k/2))[:,None,None]**2
        static=float(np.mean(l1*dr2/lam))
        end=2*float(np.mean(dr2*(-np.expm1(-t*exponent))/root*(lam-l1)/lam))
        energy=t*static+end
        assert -1e-13<=end<=2*r*r*g4+1e-13
        out[f'{r},{t}']={'energy':energy,'energy_per_time':energy/t,
                         'static_limit':static,'positive_endpoint_remainder':end,
                         'remainder_upper':2*r*r*g4}
    return {'n':n,'G4_origin_quadrature':g4,'rectangles':out}


def main():
    data={'scope':'Finite Fourier and Poisson identities plus quadrature convergence; no numerical continuum proof.',
          'independent_review':False,'families':{}}
    timechecks=[]
    for lam in [.07,.4,2.,9.]:
        root=np.sqrt(lam*(lam+4));r=2/(lam+2+root)
        for t in [1,2,5,17]:
            matrix=r**np.abs(np.arange(t)[:,None]-np.arange(t)[None,:])/root
            direct=float(matrix.sum())
            formula=t/lam-2*(1-r**t)/(lam*root)
            assert abs(direct-formula)<2e-12*max(1,direct)
            timechecks.append({'lambda':lam,'T':t,'direct':direct,'formula':formula,'difference':abs(direct-formula)})
    data['families']['time_green_geometric_sum']={'cases':timechecks}

    periodic=[]
    for side in [8,12,16,24,32]:
        face,_=fft_energy(side,1,1)
        expected=.5*(1-side**-4)
        assert abs(face-expected)<2e-13
        e,parts=fft_energy(side,2,4)
        reversed_e,_=fft_energy(side,4,2)
        assert abs(e-reversed_e)<2e-13
        periodic.append({'side':side,'unit_face_energy':face,'exact_hodge_value':expected,
                         'rectangle_2_4_energy':e,'exchanged_rectangle_energy':reversed_e,
                         'side_contributions':parts})
    data['families']['explicit_periodic_currents']={'cases':periodic}

    side,r,t=8,2,3
    j0,j1=currents(side,r,t)
    def laplacian(vector):
        arr=vector.reshape((side,)*4)
        out=8*arr.copy()
        for axis in range(4):
            out-=np.roll(arr,1,axis)+np.roll(arr,-1,axis)
        return out.ravel()
    operator=LinearOperator((side**4,side**4),matvec=laplacian,dtype=float)
    energy=0.;residuals=[]
    for j in [j0,j1]:
        solved,info=cg(operator,j.ravel(),rtol=1e-13,atol=1e-14,maxiter=400)
        assert info==0
        residual=float(np.linalg.norm(laplacian(solved)-j.ravel()))
        residuals.append(residual);energy+=float(j.ravel()@solved)
    fourier,parts=fft_energy(side,r,t)
    assert abs(energy-fourier)<1e-12
    open_divergence=np.roll(j0,1,axis=0)-j0
    assert np.max(np.abs(open_divergence))==1
    assert abs(parts[0]-energy)>.1
    data['families']['independent_poisson_and_faults']={'cg_energy':energy,'fft_energy':fourier,
                  'poisson_residuals':residuals,'missing_spatial_ends_energy':parts[0],
                  'missing_spatial_ends_divergence':float(np.max(np.abs(open_divergence)))}

    pairs=[(1,1),(1,2),(2,1),(2,4),(4,2),(4,16),(4,64),(8,64)]
    levels=[reduced_integrals(n,pairs) for n in [24,32,48,64,96,128]]
    for level in levels:
        assert abs(level['rectangles']['1,1']['static_limit']-1/3)<2e-13
        assert level['rectangles']['4,64']['energy_per_time']<level['rectangles']['4,16']['energy_per_time']
    last=levels[-1]['rectangles']
    assert abs(last['1,1']['energy']-.5)<1e-7
    assert abs(last['1,2']['energy']-last['2,1']['energy'])<1e-7
    assert abs(last['2,4']['energy']-last['4,2']['energy'])<3e-7
    data['families']['reduced_infinite_time_quadrature']={'levels':levels,
          'infinite_volume_exact_calibrations':{'unit_face_energy':.5,'unit_separation_static_rate':1/3},
          'quadrature_error_certified':False}
    path=Path(__file__).with_name('BLOCK29_RECTANGLE_GREEN_CHECKS.json')
    path.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'families':len(data['families']),'all_assertions_completed':True,'output':str(path)},indent=2))


if __name__=='__main__':
    main()
