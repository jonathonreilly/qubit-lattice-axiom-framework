#!/usr/bin/env python3
"""Independent normalized-oscillator, real-curl and Gaussian-quadrature checks.
No author module is imported. The script reads no repository scientific data.
Finite floating checks supplement the proof in PHOTON_INDEPENDENT_REVIEW.txt.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
import itertools
import json
import math
import sys
import time
import numpy as np
from numpy.polynomial.hermite import hermgauss


def emit(name, **data):
    print(json.dumps({'check': name, **data}), flush=True)


def require_small(name, value, tolerance=2e-11):
    if not value < tolerance:
        raise AssertionError((name, float(value), tolerance))


def maxabs(x):
    return float(np.max(np.abs(x)))


def frame():
    axis=np.array([1.,2.,3.]); axis/=np.linalg.norm(axis)
    a,b,c=axis
    skew=np.array([[0,-c,b],[c,0,-a],[-b,a,0]])
    angle=.73
    rot=np.eye(3)*np.cos(angle)+(1-np.cos(angle))*np.outer(axis,axis)+np.sin(angle)*skew
    return .5*np.vstack((np.eye(3),rot))


def oscillator_check():
    rows=frame(); m=3; cutoff=7; w=1.; c=.25
    basis=[n for n in itertools.product(range(cutoff+1),repeat=m) if sum(n)<=cutoff]
    loc={n:i for i,n in enumerate(basis)}; size=len(basis)
    energy=np.array([sum(n)*w for n in basis])
    create=[]
    for j in range(m):
        a=np.zeros((size,size))
        for n,i in loc.items():
            nn=list(n); nn[j]+=1; nn=tuple(nn)
            if nn in loc: a[loc[nn],i]=np.sqrt(n[j]+1)
        create.append(a)
    vac=np.zeros(size); vac[loc[(0,0,0)]]=1
    one=np.column_stack([a@vac for a in create])
    fields=[sum(v*(a+a.T) for v,a in zip(row,create)) for row in rows]
    v4=-sum(np.linalg.matrix_power(b,4) for b in fields)/24
    v6=sum(np.linalg.matrix_power(b,6) for b in fields)/720
    mean4=float(vac@v4@vac); mean6=float(vac@v6@vac)
    v0=v4@vac-mean4*vac
    q=(energy>=3*w)&(np.array([sum(n)%2 for n in basis])==1)
    ev=(energy>0)&(np.array([sum(n)%2 for n in basis])==0)
    u=v4@one; u[~q]=0
    vacuum_form=float(np.sum(v0[ev]**2/energy[ev]))
    direct6=one.T@v6@one-mean6*np.eye(m)
    direct=direct6-u[q].T@(u[q]/(energy[q,None]-w))+vacuum_form*np.eye(m)
    connected=np.zeros((size,m))
    for row in rows:
        bplus=sum(v*a for v,a in zip(row,create))
        connected-=np.outer(np.linalg.matrix_power(bplus,3)@vac,row)/6
    spectator=np.column_stack([a@v0 for a in create])
    km=connected[q].T@(connected[q]/(energy[q,None]-w))
    kp=connected[q].T@(connected[q]/(energy[q,None]+w))
    cross=spectator[q].T@(connected[q]/(energy[q,None]-w))
    exchange=spectator[q].T@(spectator[q]/(energy[q,None]-w))-vacuum_form*np.eye(m)
    expected=-c*c*w*np.eye(m)/32-km-kp
    errors={
        'frame_gram':maxabs(rows.T@rows-w*np.eye(m)/2),
        'constant_variance':maxabs(np.sum(rows*rows,axis=1)-c),
        'connected_decomposition':maxabs(u-spectator-connected),
        'direct_sextic':maxabs(direct6-c*c*w*np.eye(m)/16),
        'exchange':maxabs(exchange-c*c*w*np.eye(m)/32-kp),
        'interference':maxabs(cross-c*c*w*np.eye(m)/32),
        'whole_g4':maxabs(direct-expected),
    }
    for name,error in errors.items():require_small(name,error)
    # A complex change of basis exposes off-diagonal Hermitian entries.
    z=np.exp(2j*np.pi*np.arange(3)[:,None]*np.arange(3)[None,:]/3)/np.sqrt(3)
    complex_gap=z.conj().T@direct@z
    f=np.array([1,1j,1+1j],complex); f/=np.linalg.norm(f)
    sf=spectator@f; cf=connected@f
    exact_scalar=np.vdot(f,direct@f)
    scalar6=np.vdot(f,direct6@f)
    fullq=(sf+cf)[q]
    direct_scalar=scalar6-np.vdot(fullq,fullq/(energy[q]-w))+vacuum_form
    require_small('complex_external_state',abs(exact_scalar-direct_scalar))
    controls={'omit_one_interference_copy':maxabs(direct-(expected+cross)),
              'omit_plus_exchange':maxabs(direct-(expected+kp)),
              'omit_vacuum_subtraction':vacuum_form}
    if min(controls.values())<1e-6:raise AssertionError(('insensitive mutation',controls))
    emit('normalized_ladder_complete_g4',basis_size=size,cutoff=cutoff,
         frequencies=[w]*m,variance=c,errors=errors,
         complex_basis_max_offdiagonal=float(np.max(np.abs(complex_gap-np.diag(np.diag(complex_gap))))),
         coefficient_eigenvalues=np.linalg.eigvalsh(direct).tolist(),
         omitted_term_discrepancies=controls)


def curl_matrix(L):
    points=list(itertools.product(range(L),repeat=3)); loc={p:i for i,p in enumerate(points)}
    orientations=[(0,1),(0,2),(1,2)]
    C=np.zeros((3*len(points),3*len(points)))
    for ix,x in enumerate(points):
        for o,(i,j) in enumerate(orientations):
            xp=list(x); xp[i]=(xp[i]+1)%L
            xq=list(x); xq[j]=(xq[j]+1)%L
            rr=3*ix+o
            C[rr,3*ix+i]+=1
            C[rr,3*loc[tuple(xp)]+j]+=1
            C[rr,3*loc[tuple(xq)]+i]-=1
            C[rr,3*ix+j]-=1
    return points,C


def momentum_curl(k,L):
    d=np.expm1(2j*np.pi*np.array(k)/L); omega=float(np.linalg.norm(d))
    C=np.zeros((3,3),complex)
    for o,(i,j) in enumerate(((0,1),(0,2),(1,2))):
        C[o,j]=d[i]; C[o,i]=-d[j]
    return d,omega,C


def cubic_check(L, external):
    points,C=curl_matrix(L); N=L**3
    eig,U=np.linalg.eigh(C.T@C); select=eig>1e-9
    U=U[:,select]; freq=np.sqrt(eig[select]); modes=len(freq)
    assert modes==2*(N-1)
    V=(C@U)/np.sqrt(2*freq)[None,:]
    c=float(np.sum(freq)/(6*N))
    require_small('real_mode_gram',maxabs(V.T@V-np.diag(freq/2)))
    require_small('real_mode_variance',maxabs(np.sum(V*V,axis=1)-c))
    blocks={p:momentum_curl(p,L) for p in points if any(p)}
    H={p:cc@cc.conj().T/(2*w) for p,(d,w,cc) in blocks.items()}
    e3=freq[:,None,None]+freq[None,:,None]+freq[None,None,:]
    mix=np.array([[1,1j],[1j,1]],complex)/np.sqrt(2)
    for k in external:
        d,w,cc=blocks[k]
        _,_,vh=np.linalg.svd(d.conj()[None,:],full_matrices=True)
        pol=vh[1:].conj().T@mix
        require_small('transversality',maxabs(d.conj()@pol))
        phase=np.exp(2j*np.pi*(np.array(points)@np.array(k))/L)
        link=(phase[:,None,None]*pol[None,:,:]/np.sqrt(N)).reshape((3*N,2))
        f=U.T@link
        vf=V@f
        expected_field=(phase[:,None,None]*(cc@pol)[None,:,:]/np.sqrt(2*N*w)).reshape((3*N,2))
        errors={'complex_fourier_field':maxabs(vf-expected_field),
                'one_photon_norm':maxabs(f.conj().T@f-np.eye(2)),
                'one_photon_energy':maxabs(freq[:,None]*f-w*f),
                'real_conjugation':maxabs(V@f.conj()-vf.conj())}
        # All same-parity three-particle energies are > w for these L=3,4 checks.
        assert np.min(e3-w)>0
        tensor=np.einsum('pm,pn,pr,pa->mnra',V,V,V,vf,optimize=True).reshape((-1,2))
        real_minus=tensor.conj().T@(tensor/(e3.reshape(-1,1)-w))/6
        real_plus=tensor.conj().T@(tensor/(e3.reshape(-1,1)+w))/6
        sums=[np.zeros((3,3),complex),np.zeros((3,3),complex)]
        for p,(dp,wp,cp) in blocks.items():
            for q,(dq,wq,cq) in blocks.items():
                r=tuple((kk-pp-qq)%L for kk,pp,qq in zip(k,p,q))
                if r not in blocks:continue
                energy=wp+wq+blocks[r][1]
                assert energy-w>0
                gram=H[p]*H[q]*H[r]
                sums[0]+=gram/(energy-w)
                sums[1]+=gram/(energy+w)
        external_field=cc@pol/np.sqrt(2*w)
        projected=[external_field.conj().T@s@external_field/(6*N*N) for s in sums]
        errors['real_vs_projector_minus']=maxabs(real_minus-projected[0])
        errors['real_vs_projector_plus']=maxabs(real_plus-projected[1])
        for name,error in errors.items():require_small(name,error)
        D=-c*c*w*np.eye(2)/32-real_minus-real_plus
        km=np.linalg.eigvalsh(real_minus)/w; kp=np.linalg.eigvalsh(real_plus)/w; dd=np.linalg.eigvalsh(D)/w
        assert km[0]>-1e-13 and kp[0]>-1e-13 and km[-1]<1 and kp[-1]<1/3
        assert dd[0]>-65/48 and dd[-1]<-1/96
        emit('real_curl_vs_fourier_projector',L=L,k=list(k),real_modes=modes,c=c,
             self_inverse=all((2*x)%L==0 for x in k),errors=errors,
             Kminus_over_omega=km.tolist(),Kplus_over_omega=kp.tolist(),D4_over_omega=dd.tolist())


def full_cosine_quadrature(g,cutoff,nodes):
    # Direct coordinate-space cosine and sine integration, without normal-order input.
    rows=frame(); m=3; w=1.; c=.25
    x,weights=hermgauss(nodes); weights/=np.sqrt(np.pi)
    h=np.empty((cutoff+1,nodes)); h[0]=1; h[1]=np.sqrt(2)*x
    for n in range(1,cutoff):
        h[n+1]=(np.sqrt(2)*x*h[n]-np.sqrt(n)*h[n-1])/np.sqrt(n+1)
    hw=h*weights
    X=np.stack(np.meshgrid(x,x,x,indexing='ij'),axis=-1)
    B=np.sqrt(2)*np.einsum('...j,pj->...p',X,rows)
    W=np.sum(2*np.sin(g*B/2)**2/g**2-B*B/2,axis=-1)
    derivative=np.sin(g*B)/g-B
    ones=np.sqrt(2)*X
    connected_function=np.einsum('...p,pj->...j',derivative,rows)
    def transform(values):
        a=np.einsum('ai,ijk...->ajk...',hw,values,optimize=True)
        b=np.einsum('bj,ajk...->abk...',hw,a,optimize=True)
        return np.einsum('ck,abk...->abc...',hw,b,optimize=True)
    vg=transform(W)
    ug=transform(W[...,None]*ones)
    cg=transform(connected_function)
    states=np.array(list(itertools.product(range(cutoff+1),repeat=3)))
    total=np.sum(states,axis=1); even=(total>=2)&(total<=cutoff)&(total%2==0)
    odd=(total>=3)&(total<=cutoff)&(total%2==1)
    vv=vg.reshape(-1); uu=ug.reshape((-1,3)); cc=cg.reshape((-1,3))
    vac=float(np.sum(vv[even]**2/(w*total[even])))
    S=uu[odd].T@(uu[odd]/(w*(total[odd,None]-1)))-vac*np.eye(3)
    km=cc[odd].T@(cc[odd]/(w*(total[odd,None]-1)))
    kp=cc[odd].T@(cc[odd]/(w*(total[odd,None]+1)))
    cross=np.zeros((3,3))
    for n in states[even]:
        if np.sum(n)>=cutoff:continue
        for j in range(3):
            nn=n.copy(); nn[j]+=1
            cross[j,:]+=vg[tuple(n)]/(w*np.sum(n))*np.sqrt(n[j]+1)*cg[tuple(nn)]
    y=g*g*c; r=np.exp(-y/2); t=np.expm1(-y/2)/2
    predicted=t*t*w*np.eye(3)/2+km+kp+cross+cross.T
    X2=-t*r*y*w*np.eye(3)/8
    gram=rows@rows.T
    Xhigh=np.zeros((3,3))
    for power in range(4,38,2):
        kernel_weights=np.sum(gram**power,axis=0)/(power*w)
        J=rows.T@(kernel_weights[:,None]*rows)
        Xhigh-=r*r*g**(2*power-2)*J/math.factorial(power)
    expected_cross=X2+Xhigh
    residual=maxabs(S-predicted)
    cross_residual=maxabs(cross-expected_cross)
    require_small('full_cosine_direct_vs_cancellation',residual,3e-12)
    require_small('full_cosine_direct_vs_covariance_cross',cross_residual,3e-12)
    if np.linalg.eigvalsh(Xhigh)[-1]>1e-15:raise AssertionError('wrong high-cross sign')
    # Stable evaluation of the rigorous scalar high-interference bound.
    cosh_tail=sum(y**p/math.factorial(p) for p in range(4,38,2))
    scalar_bound=r*r*w*cosh_tail/(8*y)
    assert np.linalg.eigvalsh(Xhigh)[0]>=-scalar_bound-1e-14
    return {'g':g,'cutoff':cutoff,'hermite_nodes_per_coordinate':nodes,
            'S_eigenvalues':np.linalg.eigvalsh(S).tolist(),
            'direct_vs_cancellation_error':residual,
            'cross_vs_covariance_error':cross_residual,
            'high_cross_eigenvalues':np.linalg.eigvalsh(Xhigh).tolist(),
            'positive_degree_two_cross':float(X2[0,0]),
            'rigorous_scalar_high_cross_magnitude_bound':float(scalar_bound)}


def main():
    started=time.monotonic()
    emit('runtime',python=sys.version.split()[0],numpy=np.__version__)
    oscillator_check()
    cubic_check(3,[(1,1,0),(2,2,0)])
    cubic_check(4,[(2,0,0),(2,1,0),(2,2,2)])
    for g in (.125,.25,.5):
        low=full_cosine_quadrature(g,10,32)
        high=full_cosine_quadrature(g,14,44)
        stability=max(abs(x-y) for x,y in zip(low['S_eigenvalues'],high['S_eigenvalues']))
        require_small('quadrature_cutoff_stability',stability,3e-12)
        emit('full_cosine_coordinate_quadrature',**high,
             low_degree_low_nodes_comparison=low['S_eigenvalues'],stability_error=stability,
             scope='finite Gaussian quadrature and Fock projection, not a rigorous numerical tail or compact-spectrum certificate')
    emit('completed',elapsed_seconds=time.monotonic()-started,
         scope='independent finite checks only; uniform and infinite-series claims rely on the written derivation')

if __name__=='__main__':main()
