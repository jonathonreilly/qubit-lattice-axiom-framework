#!/usr/bin/env python3
"""Finite cochain/component challenges for the private all-shape coefficient."""
import itertools
import json
import math
import numpy as np


def complex4():
    cells={p:[(x,o) for o in itertools.combinations(range(4),p)
              for x in itertools.product(range(2),repeat=4)
              if all(x[j]==0 for j in o)] for p in range(5)}
    mats={}
    for p in range(4):
        lookup={c:i for i,c in enumerate(cells[p])}
        matrix=np.zeros((len(cells[p+1]),len(cells[p])))
        for i,(x,o) in enumerate(cells[p+1]):
            for pos,j in enumerate(o):
                sub=tuple(k for k in o if k!=j)
                xp=list(x)
                xp[j]+=1
                matrix[i,lookup[(tuple(xp),sub)]]+=(-1)**pos
                matrix[i,lookup[(x,sub)]]-=(-1)**pos
        mats[p]=matrix
    D,B=mats[1],mats[2]
    H2=D@D.T+B.T@B
    P=D@D.T@np.linalg.inv(H2)
    Q=B.T@B@np.linalg.inv(H2)
    assert np.max(abs(P+Q-np.eye(len(cells[2]))))<1e-13
    assert np.max(abs(P@Q))<1e-13
    return D,B,P,Q,mats


def frames():
    D,B,P,Q,mats=complex4()
    basis=np.eye(D.shape[0])
    S=[basis[i] for i in range(8)]
    n=[basis[i] for i in range(8,16)]
    # Non-elementary actual fills: connected adjoining faces and a doubled
    # current. These are finite frame controls, not an exhaustive shape gas.
    for i in [0,3,6,9]:
        j=next(j for j in range(len(basis)) if j!=i and
               np.count_nonzero(D[i]*D[j])>0)
        S.append(basis[i]+basis[j])
        n.append(basis[(i+5)%24]-basis[(j+5)%24])
    S.extend([2*basis[2],-2*basis[4]])
    n.extend([2*basis[17],-2*basis[20]])
    S,n=np.array(S),np.array(n)
    assert np.max(abs((S@D)@mats[0])) == 0
    assert np.max(abs((n@B.T)@mats[3].T)) == 0
    beta,N=.3,2
    g,b,c=N/math.sqrt(beta),2*math.pi*math.sqrt(beta),2*math.pi*N
    we=np.exp(-g*g*np.einsum('ni,ij,nj->n',S,P,S)/2)
    wm=np.exp(-b*b*np.einsum('ni,ij,nj->n',n,Q,n)/2)
    theta=c*S@P@n.T
    C=np.cos(theta)-1
    sine=np.sin(theta)
    product=we[:,None]*wm[None,:]
    Ke=S.T@(we[:,None]*S)
    Km=n.T@(wm[:,None]*n)
    Kec=S.T@((we*(C@wm))[:,None]*S)
    Kmc=n.T@((wm*(C.T@we))[:,None]*n)
    Rem=S.T@(product*(sine-theta))@n
    Kem=S.T@(product*sine)@n
    exact_factor=c*Ke@P@Km+Rem
    factor_error=float(np.max(abs(Kem-exact_factor)))
    assert factor_error<1e-13
    missing_projection=float(np.max(abs(Kem-(c*Ke@Km+Rem))))
    assert missing_projection>1e-5
    def moment(fills,weight,r):
        return float(np.max(abs(fills).T@(weight*np.sum(abs(fills),axis=1)**(r-1))))
    def schur(A):
        return max(float(np.max(np.sum(abs(A),axis=0))),
                   float(np.max(np.sum(abs(A),axis=1))))
    bounds={'Kec':[schur(Kec),c*c/2*moment(n,wm,2)*moment(S,we,4)],
            'Kmc':[schur(Kmc),c*c/2*moment(S,we,2)*moment(n,wm,4)],
            'Rem':[schur(Rem),c**3/6*moment(S,we,4)*moment(n,wm,4)]}
    assert all(actual<=bound+1e-12 for actual,bound in bounds.values())
    assert np.linalg.eigvalsh((Kec+Kec.T)/2).max()<1e-13
    assert np.linalg.eigvalsh((Kmc+Kmc.T)/2).max()<1e-13
    h=np.sin(np.arange(24)*.73+.4)/5
    x,y=P@h,Q@h
    U,V=g*S@x,b*n@y
    def direct(eps):
        return 4*np.sum(product*(C*(np.cosh(eps*U[:,None])*np.cos(eps*V[None,:])-1)
                                 -sine*np.sinh(eps*U[:,None])*np.sin(eps*V[None,:])))
    quadratic=2*g*g*x@Kec@x-2*b*b*y@Kmc@y-4*g*b*x@Kem@y
    direct_quadratic=np.sum(product*(2*C*(U[:,None]**2-V[None,:]**2)
                                    -4*sine*U[:,None]*V[None,:]))
    assert abs(quadratic-direct_quadratic)<1e-13
    # Full nonlinear operator identity used in the finite-boundary passage.
    # Stable removable-zero formulas retain components with tiny source.
    def sinhc(z):
        result=np.ones_like(z)
        np.divide(np.sinh(z),z,out=result,where=z!=0)
        return result
    alpha=.5*sinhc(U/2)**2
    eta=-.5*np.sinc(V/(2*np.pi))**2
    Eh=S.T@((we*alpha*(C@(wm*np.cos(V))))[:,None]*S)
    Mh=n.T@((wm*eta*(C.T@we))[:,None]*n)
    Rh=S.T@(product*(sine-theta)*sinhc(U)[:,None]*np.sinc(V/np.pi)[None,:])@n
    Je=S.T@(we*np.sinh(U))
    Jm=n.T@(wm*np.sin(V))
    nonlinear_factor=4*g*g*x@Eh@x+4*b*b*y@Mh@y-4*c*Je@P@Jm-4*g*b*x@Rh@y
    nonlinear_factor_error=float(abs(nonlinear_factor-direct(1)))
    assert nonlinear_factor_error<1e-13
    missing_signed_term=float(abs((nonlinear_factor+4*c*Je@P@Jm)-direct(1)))
    assert missing_signed_term>1e-6
    remainders=[dict(scale=e,remainder=float(direct(e)-e*e*quadratic),
                     divided_by_fourth_power=float((direct(e)-e*e*quadratic)/e**4))
                for e in [1.,.5,.25,.125]]
    assert abs(remainders[0]['remainder'])>1e-6
    assert max(abs(r['divided_by_fourth_power']) for r in remainders)<1
    # Finite source-energy estimate evaluated in logarithms, including large
    # sources. This avoids confusing underflow with a proven inequality.
    energy_checks=[]
    for scale in [.1,1.,7.,40.]:
        hs=scale*h
        u=g*S@P@hs
        lhs=np.log(we)+abs(u)
        rhs=.5*np.log(we)+hs@hs
        margin=float(np.min(rhs-lhs))
        assert margin>=-1e-12
        energy_checks.append(dict(source_scale=scale,minimum_log_margin=margin))
    # Change the integer fills while preserving their actual currents/charges.
    S2=S.copy(); n2=n.copy()
    for i in range(len(S2)):
        S2[i]+=B[i%B.shape[0]]
    for i in range(len(n2)):
        n2[i]+=D[:,i%D.shape[1]]
    assert np.max(abs((S2-S)@D))==0
    assert np.max(abs((n2-n)@B.T))==0
    U2,V2=g*S2@P@h,b*n2@Q@h
    theta2=c*S2@P@n2.T
    phase_error=float(np.max(abs(np.exp(1j*theta2)-np.exp(1j*theta))))
    source_error=max(float(np.max(abs(U2-U))),float(np.max(abs(V2-V))))
    assert phase_error<2e-13 and source_error<1e-13
    transformed=4*np.sum(product*((np.cos(theta2)-1)*(np.cosh(U2[:,None])*np.cos(V2[None,:])-1)
                                  -np.sin(theta2)*np.sinh(U2[:,None])*np.sin(V2[None,:])))
    assert abs(transformed-direct(1))<1e-13
    return dict(shape_counts={'electric_fills':len(S),'magnetic_fills':len(n)},
                factorization_error=factor_error,missing_projection_fault=missing_projection,
                full_nonlinear_factorization_error=nonlinear_factor_error,
                missing_signed_nonlinear_term_fault=missing_signed_term,
                schur_bounds=bounds,source_remainders=remainders,energy_checks=energy_checks,
                filling_invariance={'phase_error':phase_error,'source_error':source_error,
                                    'coefficient_error':float(abs(transformed-direct(1)))},
                scope='Finite free four-cube frames; chosen parameters test algebra, not the infinite-shape sufficient regime.')


if __name__=='__main__':
    print(json.dumps(dict(status='finite_checks_passed',component_frames=frames()),indent=2))
