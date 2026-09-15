#!/usr/bin/env python3
"""Real/Fourier theta and square-root-log comparison: finite author probes."""
from pathlib import Path
import hashlib,json
import numpy as np

def evaluate(alpha,z,beta,points):
    # w(x)=exp(-alpha*x^2/2)*(1+z*cos(beta*x))/(1+z)>0.
    # Its transform is a positive mixture of three shifted Gaussians.
    grid=np.arange(-30,31,dtype=float)
    x=grid[None,:]+points[:,None]
    chi=(1+z*np.cos(beta*x))/(1+z)
    chip=-z*beta*np.sin(beta*x)/(1+z)
    chipp=-z*beta*beta*np.cos(beta*x)/(1+z)
    gauss=np.exp(-alpha*x*x/2)
    w=gauss*chi
    wp=gauss*(chip-alpha*x*chi)
    wpp=gauss*(chipp-2*alpha*x*chip+(alpha*alpha*x*x-alpha)*chi)
    T=w.sum(axis=1);Tp=wp.sum(axis=1);Tpp=wpp.sum(axis=1)
    origin=np.sum(np.exp(-alpha*grid*grid/2)*(1+z*np.cos(beta*grid))/(1+z))
    f=-np.log(T/origin);fp=-Tp/T;fpp=(Tp/T)**2-Tpp/T
    freq=np.arange(-30,31,dtype=float)
    coef=np.sqrt(2*np.pi/alpha)/(1+z)*(np.exp(-(2*np.pi*freq)**2/(2*alpha))
       +z/2*np.exp(-(2*np.pi*freq-beta)**2/(2*alpha))
       +z/2*np.exp(-(2*np.pi*freq+beta)**2/(2*alpha)))
    fourier=np.cos(2*np.pi*points[:,None]*freq)@coef
    M=alpha+z*beta*beta/(1-z)**2
    assert coef.min()>=0 and T.min()>0
    assert np.max(abs(T-fourier))<3e-13*max(1,T.max())
    assert f.min()>-3e-14
    assert fpp.max()<=M+3e-12
    assert np.max(fp*fp-2*M*f)<3e-12
    sqrtf=np.sqrt(np.maximum(f,0))
    lhs=abs(sqrtf[:,None]-sqrtf[None,:])
    rhs=np.sqrt(M/2)*abs(points[:,None]-points[None,:])
    assert np.max(lhs-rhs)<3e-7
    return {'alpha':alpha,'z':z,'beta_frequency':beta,'M':M,'points':len(points),
        'max_real_fourier_discrepancy':float(np.max(abs(T-fourier))),
        'min_log_cost':float(f.min()),'max_curvature':float(fpp.max()),
        'max_gradient_self_bound_residual':float(np.max(fp*fp-2*M*f)),
        'max_square_root_comparison_residual':float(np.max(lhs-rhs)),
        'min_fourier_weight':float(coef.min())}

def general_path_green():
    rows=[]
    paths=[[(0,(0,0,0)),(0,(1,0,0)),(1,(2,0,0))],
           [(1,(0,0,0)),(0,(0,1,0)),(0,(1,1,0))]]
    for size in (24,40,64):
        grid=2*np.pi*(np.arange(size)+.5)/size-np.pi
        ks=np.stack(np.meshgrid(grid,grid,grid,indexing='ij'),axis=-1)
        d=np.exp(-1j*ks)-1;lam=np.sum(abs(d)**2,axis=-1)
        root=np.sqrt(lam*(lam+4));decay=2/(lam+2+root)
        g0=1/root
        rho_expected=np.exp(-1j*(2*ks[...,0]+ks[...,1]))-1
        for index,path in enumerate(paths):
            eta=np.zeros(ks.shape,dtype=complex)
            for direction,position in path:
                eta[...,direction]+=np.exp(-1j*np.sum(ks*np.array(position),axis=-1))
            rho=np.sum(d*eta,axis=-1)
            assert np.max(abs(rho-rho_expected))<4e-15
            norm=np.sum(abs(eta)**2,axis=-1);longitudinal=abs(rho)**2/lam
            assert np.min(norm-longitudinal)>-3e-14
            static=float(np.mean(longitudinal));last=None
            for time in (1,2,5,12):
                direct_time=sum(decay**abs(a-b)*g0 for a in range(time) for b in range(time))
                direct=float(np.mean(abs(rho)**2*direct_time+2*norm*g0*(1-decay**time)))
                end=float(np.mean(2*g0*(1-decay**time)*(norm-longitudinal)))
                reduced=time*static+end
                assert abs(direct-reduced)<3e-12*max(1,direct)
                assert 0<=end<=2*len(path)**2*float(np.mean(g0))+3e-12
                if last is not None:assert reduced/time<last
                last=reduced/time
                rows.append({'grid_side':size,'path_index':index,'T':time,'direct_time_sum':direct,
                    'reduced_energy':reduced,'static_limit':static,'positive_remainder':end})
    return rows

def main():
    points=np.unique(np.r_[np.linspace(-2,2,161),[-.0001,.0001,.013,1.0001]])
    cases=[evaluate(a,z,b,points) for a,z,b in [(1.,.2,.7),(3.,.4,2.3),(12.,.7,4.2),(30.,.15,9.)]]
    # Omitting the Fourier-positive centered maximum is a real false shortcut.
    # A shifted Gaussian theta has its maximum at the shifted center, not0.
    k=np.arange(-30,31,dtype=float);a=30.;center=.3
    T0=np.exp(-a*(k-center)**2/2).sum();Tc=np.exp(-a*k*k/2).sum()
    shifted_cost=-np.log(Tc/T0)
    assert shifted_cost<-.5
    # The difference of two time-separated fixed currents has energy bounded
    # by4 times one current energy for every positive translation-invariant
    # Fourier Green kernel. Check literal loop currents on periodic Z4.
    green=[]
    for side in (8,12,16):
        j=np.zeros((4,)+(side,)*4)
        j[1,0,0,0,0]=1;j[2,0,1,0,0]=1
        j[1,0,0,1,0]=-1;j[2,0,0,0,0]=-1
        div=sum(np.roll(j[i],1,axis=i)-j[i] for i in range(4))
        assert np.max(abs(div))==0
        one=2-2*np.cos(2*np.pi*np.arange(side)/side)
        lam=sum(one.reshape((1,)*i+(side,)+(1,)*(3-i)) for i in range(4));lam[(0,)*4]=1
        def energy(x):return float(sum(np.sum(abs(np.fft.fftn(x[i]))**2/lam) for i in range(4))/side**4)
        base=energy(j)
        for t in (1,2,3):
            delta=j-np.roll(j,t,axis=1)
            cost=energy(delta)
            assert 0<=cost<=4*base+3e-13
            green.append({'side':side,'time_separation':t,'single_loop_energy':base,'difference_energy':cost,'bound':4*base})
    data={'status':'personal_finite_checks_not_independent_review','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'general_path_green':general_path_green(),'theta_cases':cases,'shifted_origin_countercontrol':float(shifted_cost),'fixed_loop_time_difference':green,
       'limitations':'Floating finite sums; neither interval bounds nor the infinite path-threshold theorem are computed.'}
    dest=Path(__file__).with_name('BLOCK33_STATIC_PATH_COMPARISON_CHECKS.json');dest.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'theta_cases':len(cases),'time_difference_cases':len(green),
        'general_path_cases':len(data['general_path_green']),'max_theta_discrepancy':max(x['max_real_fourier_discrepancy'] for x in cases),'output':str(dest)}))
if __name__=='__main__':main()
