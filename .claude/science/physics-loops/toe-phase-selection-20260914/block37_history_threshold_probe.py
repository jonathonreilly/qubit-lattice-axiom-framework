#!/usr/bin/env python3
"""Author finite checks of endpoint fillings and history threshold comparison."""
from pathlib import Path
import itertools,hashlib,json
import numpy as np

def main():
    rows=[];cube_rows=[]
    D=np.zeros((4,4),dtype=int)
    for e in range(4):D[e,e]=-1;D[e,(e+1)%4]=1
    j=np.array([1,0,0,0]);loop=np.ones(4,dtype=int);zero=np.zeros(4,dtype=int)
    histories=[ [('u',j)], [('u',j),('t',1),('u',loop)],
        [('u',loop),('t',2),('u',j)], [('u',j),('t',1),('u',-loop),('t',1)],
        [('u',2*j),('t',1),('u',-j)], [], [('u',loop),('t',1),('u',-loop)],
        [('u',-j),('t',1),('u',j)], [('u',j),('t',2),('u',j)] ]
    for N,beta in [(2,.4),(3,.6),(4,.8)]:
        a=np.array(list(itertools.product(range(N),repeat=4)));count=len(a)
        angles=2*np.pi*np.arange(N)/N
        weight=np.exp(-beta*(angles[:,None]+2*np.pi*np.arange(-10,11))**2/2).sum(axis=1)
        coeff=np.fft.fft(weight).real/N
        delta=(a[:,None,:]-a[None,:,:])%N
        C=np.prod(weight[delta],axis=2)/count
        root=np.sqrt(weight[a.sum(axis=1)%N]);T=root[:,None]*C*root[None,:]
        eig,vec=np.linalg.eigh(T);lam=eig[-1];Omega=vec[:,-1]
        if Omega.sum()<0:Omega=-Omega
        tau=T/lam
        for index,history in enumerate(histories):
            phi=Omega.astype(complex);total=sum((arg for kind,arg in history if kind=='u'),start=zero.copy())
            t=0;past=zero.copy();strips=[];insertions={}
            for kind,arg in history:
                if kind=='u':
                    phi*=np.exp(2j*np.pi*(a@arg)/N);past+=arg
                    insertions[t]=insertions.get(t,zero.copy())+arg
                else:
                    phi=np.linalg.matrix_power(tau,arg)@phi
                    for _ in range(arg):strips.append(-(total-past));t+=1
            length=t;R=1.
            spatial=np.zeros((length+1,4),dtype=int);temporal=np.zeros((length,4),dtype=int)
            for t,current in enumerate(strips):
                spatial[t]+=current;spatial[t+1]-=current;temporal[t]+=D.T@current
                R*=float(np.prod([max(coeff/coeff[(np.arange(N)+int(q))%N]) for q in current]))
            expected_spatial=np.zeros_like(spatial);expected_spatial[0]-=total
            for t,current in insertions.items():expected_spatial[t]+=current
            assert np.array_equal(spatial,expected_spatial)
            cumulative=zero.copy()
            for t in range(length):
                cumulative+=insertions.get(t,zero)
                assert np.array_equal(temporal[t],D.T@(cumulative-total))
            ref=np.exp(2j*np.pi*(a@total)/N)*Omega
            for n in (0,1,3,7):
                value=float(np.vdot(phi,np.linalg.matrix_power(tau,n)@phi).real)
                reference=float(np.vdot(ref,np.linalg.matrix_power(tau,n+2*length)@ref).real)
                assert reference>0 and value>0
                assert reference/R**2-5e-12<=value<=reference*R**2+5e-12
                wrong_time=float(np.vdot(ref,np.linalg.matrix_power(tau,n)@ref).real)
                rows.append({'N':N,'beta':beta,'word':index,'time':n,'history_length':length,
                    'endpoint_ratio':R,'history_value':value,'reference_value':reference,
                    'ratio':value/reference,'omitted_time_shift_difference':abs(wrong_time-reference)})
    # Independent full cube: direct link-clock enumeration versus plaquette
    # Fourier fibers. Faces: lower/upper spatial squares and four time faces.
    P=np.zeros((6,12),dtype=int);P[0,:4]=1;P[1,4:8]=1
    for e in range(4):
        P[e+2,e]=1;P[e+2,e+4]=-1;P[e+2,8+(e+1)%4]=1;P[e+2,8+e]=-1
    for N,beta in [(2,.4),(3,.6)]:
        angles=2*np.pi*np.arange(N)/N
        weight=np.exp(-beta*(angles[:,None]+2*np.pi*np.arange(-10,11))**2/2).sum(axis=1)
        coeff=np.fft.fft(weight).real/N
        flux=np.array(list(itertools.product(range(N),repeat=6)))
        charges=(flux@P)%N;fweights=np.prod(coeff[flux],axis=1)
        base=np.zeros(6,dtype=int);base[2]=1;J0=base@P
        shifts=[np.array([1,0,0,0,0,0]),np.array([0,0,1,1,0,0]),np.array([1,-1,2,0,-1,0])]
        targets=[np.zeros(12,dtype=int),J0]+[J0+shift@P for shift in shifts]
        numer=np.zeros(len(targets),dtype=complex);denom=0.
        # Chunk the actual link sum; no fitted expected constants.
        iterator=itertools.product(range(N),repeat=12)
        while True:
            batch=list(itertools.islice(iterator,8192))
            if not batch:break
            links=np.array(batch);weights=np.prod(weight[(links@P.T)%N],axis=1);denom+=weights.sum()
            numer+=np.sum(weights[:,None]*np.exp(2j*np.pi*(links@np.array(targets).T)/N),axis=0)
        direct=numer/denom
        z=np.array([fweights[np.all(charges==target%N,axis=1)].sum() for target in targets]);fourier=z/z[0]
        assert np.max(abs(direct-fourier))<2e-12
        comparisons=[]
        for index,shift in enumerate(shifts):
            R=float(np.prod([max(coeff/coeff[(np.arange(N)+int(q))%N]) for q in shift]))
            assert fourier[1]/R-2e-12<=fourier[index+2]<=R*fourier[1]+2e-12
            comparisons.append({'shift':shift.tolist(),'R':R,'base':float(fourier[1]),'shifted':float(fourier[index+2])})
        cube_rows.append({'N':N,'beta':beta,'link_assignments':N**12,'plaquette_assignments':N**6,
            'direct_fourier_discrepancy':float(np.max(abs(direct-fourier))),'comparisons':comparisons})
    assert max(abs(x['ratio']-1) for x in rows)>1e-2
    assert max(x['omitted_time_shift_difference'] for x in rows)>1e-2
    print(json.dumps({'status':'personal_finite_checks_not_independent_review',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'history_comparisons':rows,'cube_current_fibers':cube_rows,
        'limits':'Finite Fourier fibers and actual histories; infinite state passage and dense-space spectral conclusion require the proof.'},indent=2))
if __name__=='__main__':main()
