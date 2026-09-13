"""Finite challenges for the prior BLOCK05 source and infrared derivations.

Exact small identities and direct position/Fock calculations are used.
Finite momentum probes do not establish the infrared asymptotic or the
global convexity theorem, whose proofs are in the paired markdown files.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import math
import time
import numpy as np
import sympy as s
from scipy.optimize import minimize
from scipy.linalg import null_space

HERE = Path(__file__).resolve().parent
PAULI = [np.array([[0,1],[1,0]],complex),
         np.array([[0,-1j],[1j,0]],complex),
         np.diag([1,-1]).astype(complex)]
W = [(-PAULI[2]+1j*PAULI[0])/2,
     (-PAULI[2]+1j*PAULI[1])/2, -PAULI[2]/2]


def spectral(h):
    e,u=np.linalg.eigh(h)
    occupied=e<0
    p=u[:,occupied]@u[:,occupied].conj().T
    return e,u,p,e[occupied].sum()


def run():
    start=time.monotonic()
    checks=[]
    def check(name,ok,**detail):
        assert bool(ok), (name,detail)
        checks.append(dict(name=name,**detail))
    def eq(name,a,b):
        d=a-b
        vals=list(d) if isinstance(d,s.MatrixBase) else [d]
        check(name,all(s.simplify(x)==0 for x in vals))
    def near(name,a,b,tol=2e-11):
        resid=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
        check(name,resid<tol,max_residual=resid,tolerance=tol)

    # Exact algebra, before any spectral sampling.
    a,b,r=s.symbols('a b r',positive=True)
    zz=s.diag(1,-1)
    mm=s.Matrix([[1-r*r,2*r],[2*r,r*r-1]])/(1+r*r)
    pp=(s.eye(2)-zz)/2
    qq=(s.eye(2)+mm)/2
    vertex=(a*zz+b*mm)/2
    eq('exact_interband_energy_vertex',qq*vertex*pp,(b-a)*qq*pp/2)
    eq('exact_overlap',s.trace(qq*pp),r*r/(1+r*r))
    eq('exact_congruence_sign_after_contact',
       -(b-a)**2/(2*(b+a))+(b+a)/2,2*a*b/(a+b))
    eps,x,y=s.symbols('eps x y',real=True)
    root=s.sqrt(1+eps*x)*s.sqrt(1+eps*y)
    eq('first_bond_derivatives_equal',s.diff(root,eps).subs(eps,0),(x+y)/2)
    eq('geometric_contact_derivative',s.diff(root,eps,2).subs(eps,0),-(x-y)**2/4)
    mu=s.symbols('mu',real=True)
    radius,transfer=s.symbols('radius transfer',positive=True)
    ep=s.sqrt(radius**2+transfer**2+2*radius*transfer*mu)
    integrand=(ep-radius)**2/(4*(ep+radius))*(1-(radius+transfer*mu)/ep)
    fourth=s.diff(integrand,transfer,4).subs(transfer,0)/s.factorial(4)
    eq('exact_cone_fourth_order',fourth,mu**2*(1-mu**2)/(16*radius**3))
    eq('angular_log_coefficient',
       2*s.pi*s.integrate(mu**2*(1-mu**2),(mu,-1,1))/(16*(2*s.pi)**3),
       1/(240*s.pi**2))
    uu,vv,qqabs=s.symbols('uu vv qqabs',positive=True)
    ee=qqabs*(uu-vv)/2
    ee2=qqabs*(uu+vv)/2
    ndot=(uu*uu+vv*vv-2)/(uu*uu-vv*vv)
    jac=qqabs**3*(uu*uu-vv*vv)/8
    eq('independent_prolate_integrand',
       (ee2-ee)**2*(1-ndot)*jac/(4*(ee+ee2)),
       qqabs**4*vv**2*(1-vv**2)/(16*uu))
    eq('square_integral_bound',s.integrate(1/s.sqrt(1+x*x),(x,0,1)),s.asinh(1))

    # Independent position-space stencil on a 3^3 periodic torus.
    shape=(3,3,3)
    sites=list(product(*(range(n) for n in shape)))
    index={v:i for i,v in enumerate(sites)}
    vol=len(sites)
    dim=2*vol
    onsite=np.kron(np.eye(vol),2.5*PAULI[2])
    bonds=[]
    for v in sites:
        ix=index[v]
        for direction in range(3):
            w=list(v)
            w[direction]=(w[direction]+1)%shape[direction]
            iy=index[tuple(w)]
            bond=np.zeros((dim,dim),complex)
            bond[2*ix:2*ix+2,2*iy:2*iy+2]+=W[direction]
            bond[2*iy:2*iy+2,2*ix:2*ix+2]+=W[direction].conj().T
            bonds.append((ix,iy,direction,bond))
    h0=onsite+sum((b[-1] for b in bonds),np.zeros_like(onsite))
    energies,evec,p0,e0=spectral(h0)
    check('finite_band_gap',np.min(abs(energies))>.49,gap=float(np.min(abs(energies))))
    check('filled_negative_count',np.count_nonzero(energies<0)==vol)
    occ=energies<0
    eo=energies[occ]
    eu=energies[~occ]
    uo=evec[:,occ]
    uuvec=evec[:,~occ]
    gap=eu[:,None]-eo[None,:]
    hx=[]
    local=[]
    for i in range(vol):
        px=np.zeros_like(h0)
        px[2*i:2*i+2,2*i:2*i+2]=np.eye(2)
        cell=np.zeros_like(h0)
        cell[2*i:2*i+2,2*i:2*i+2]=2.5*PAULI[2]
        cell+=sum((bond/2 for ix,iy,di,bond in bonds if i in(ix,iy)),np.zeros_like(h0))
        hx.append(cell)
        local.append(px)
        near('cell_energy_vs_variation_'+str(i),cell,(px@h0+h0@px)/2)
    near('cell_energy_sum',sum(hx,np.zeros_like(h0)),h0)
    mats=np.array([uuvec.conj().T@v@uo for v in hx])
    chiA=-2*np.einsum('xij,yij,ij->xy',mats.conj(),mats,1/gap).real
    overlaps=np.array([uuvec.conj().T@v@uo for v in local])
    positive_weights=-2*eu[:,None]*eo[None,:]/gap
    chiC=np.einsum('xij,yij,ij->xy',overlaps.conj(),overlaps,positive_weights).real
    contact=np.zeros((vol,vol))
    lap=np.zeros((vol,vol))
    bond_means=[[] for _ in range(3)]
    for ix,iy,di,bond in bonds:
        mean=np.trace(p0@bond).real
        bond_means[di].append(mean)
        for i,j,factor in((ix,ix,1),(iy,iy,1),(ix,iy,-1),(iy,ix,-1)):
            contact[i,j]+=-mean*factor/4
            lap[i,j]+=factor
    near('full_contact_identity',chiC-chiA,contact)
    near('arithmetic_uniform_null',chiA@np.ones(vol),np.zeros(vol))
    near('congruence_uniform_null',chiC@np.ones(vol),np.zeros(vol))
    check('arithmetic_negative_semidefinite',np.max(np.linalg.eigvalsh(chiA))<2e-12)
    check('congruence_positive_semidefinite',np.min(np.linalg.eigvalsh(chiC))>-2e-12)
    for di in range(3):
        near('translated_bond_means_'+str(di),bond_means[di],np.mean(bond_means[di]))

    ks=2*np.pi*np.array(sites)/np.array(shape)
    def dfield(k):
        return np.array([np.sin(k[:,0]),np.sin(k[:,1]),
                         2.5-np.cos(k[:,0])-np.cos(k[:,1])-np.cos(k[:,2])]).T
    d=dfield(ks)
    en=np.linalg.norm(d,axis=1)
    nhat=d/en[:,None]
    i1=float(np.mean(1/en))
    maxresA=maxresC=maxBloch=0.
    momentum_rows=[]
    for q in ks:
        dp=dfield(ks+q)
        enn=np.linalg.norm(dp,axis=1)
        dot=np.einsum('ki,ki->k',nhat,dp/enn[:,None])
        ca=-np.mean((enn-en)**2*(1-dot)/(4*(en+enn)))
        cc=np.mean(en*enn*(1-dot)/(en+enn))
        fourier=np.exp(-1j*np.array(sites)@q)/math.sqrt(vol)
        fa=fourier.conj()@chiA@fourier
        fc=fourier.conj()@chiC@fourier
        maxresA=max(maxresA,abs(fa-ca))
        maxresC=max(maxresC,abs(fc-cc))
        ell=float(np.sum(4*np.sin(q/2)**2))
        check('finite_global_bound_'+str(len(momentum_rows)),-ca<=.75*i1*ell+2e-12)
        # Fourier block of the actual position-space one-body operator.
        isom=np.kron(fourier[:,None],np.eye(2))
        expected=sum((z*m for z,m in zip(dfield(q[None,:])[0],PAULI)),np.zeros((2,2),complex))
        maxBloch=max(maxBloch,np.max(abs(isom.conj().T@h0@isom-expected)))
        momentum_rows.append({'q_over_2pi':(q/(2*np.pi)).tolist(),
                              'chiA':float(ca),'chiC':float(cc),'laplacian':ell})
    near('all_momentum_arithmetic_vs_position_Hessian',maxresA,0)
    near('all_momentum_congruence_vs_position_Hessian',maxresC,0)
    near('all_Bloch_blocks_vs_stencil',maxBloch,0)

    def matrix(N,kind):
        answer=onsite*np.repeat(N,2)[:,None]
        for ix,iy,di,bond in bonds:
            factor=(N[ix]+N[iy])/2 if kind=='A' else math.sqrt(N[ix]*N[iy])
            answer=answer+factor*bond
        return answer
    rng=np.random.default_rng(5130913)
    phi=rng.normal(size=vol)
    phi-=phi.mean()
    phi/=max(abs(phi))
    step=.003
    numerical_curvatures={}
    for kind,target in(('A',chiA),('C',chiC)):
        es={n:spectral(matrix(1+n*step*phi,kind))[3] for n in(-2,-1,0,1,2)}
        second=(-es[2]+16*es[1]-30*es[0]+16*es[-1]-es[-2])/(12*step**2)
        predicted=phi@target@phi
        near('actual_energy_second_derivative_'+kind,second,predicted,tol=3e-7)
        numerical_curvatures[kind]={'finite_difference':float(second),'spectral':float(predicted)}
    N1=1+.4*phi
    phi2=rng.normal(size=vol)
    phi2-=phi2.mean()
    phi2/=max(abs(phi2))
    N2=1+.3*phi2
    lam=.37
    for kind in('A','C'):
        lhs=spectral(matrix(lam*N1+(1-lam)*N2,kind))[3]
        rhs=lam*spectral(matrix(N1,kind))[3]+(1-lam)*spectral(matrix(N2,kind))[3]
        check('global_curvature_challenge_'+kind,lhs>=rhs-1e-11 if kind=='A' else lhs<=rhs+1e-11,
              chord_residual=float(lhs-rhs))
    hc=matrix(N1,'C')
    near('geometric_mean_is_congruence',hc,
         np.sqrt(np.repeat(N1,2))[:,None]*h0*np.sqrt(np.repeat(N1,2))[None,:])
    e,u,p,energy=spectral(hc)
    check('congruence_inertia_preserved',np.count_nonzero(e<0)==vol)
    check('congruence_gap_bound',np.min(abs(e))>=N1.min()*np.min(abs(energies))-1e-11)
    nd=np.diag(np.repeat(N1,2))
    root=np.diag(np.sqrt(np.repeat(N1,2)))
    fidelity=np.sqrt(np.maximum(0,np.linalg.eigvalsh(root@h0@nd@h0@root))).sum()
    near('fidelity_energy_identity',energy,(np.trace(nd@h0).real-fidelity)/2,tol=2e-10)
    near('uniform_source_not_energy_readout',
         np.array([np.trace(p0@cell).real for cell in hx]),
         np.array([np.trace(spectral(1.3*h0)[2]@cell).real for cell in hx]))
    check('uniform_readout_changes',abs(1.3*e0-e0)>1)

    # Actual nonlinear finite static source branch, not a supplied stationary point.
    basis=null_space(np.ones((1,vol)))
    kappa=1.
    g=.2
    rho=np.cos(ks[1]@np.array(sites).T)*.01
    rho-=rho.mean()
    lambda1=float(np.linalg.eigvalsh(lap)[1])
    check('finite_existence_hypothesis',2*g*g*np.linalg.norm(rho)<kappa*lambda1)
    rho0=np.array([np.trace(p0@cell).real for cell in hx])
    def objective(coords):
        field=basis@coords
        N=1+g*field
        if min(N)<=0:
            raise ValueError('optimizer left positive lapse domain')
        hn=matrix(N,'C')
        e,u,p,energy=spectral(hn)
        local_energy=np.real(np.diag(hn@p)).reshape(vol,2).sum(axis=1)
        src=local_energy/N
        value=kappa*field@lap@field/2+energy-e0-g*rho0@field+g*rho@field
        grad=kappa*lap@field+g*(src-rho0+rho)
        return float(value),basis.T@grad
    opt=minimize(objective,np.zeros(vol-1),jac=True,method='BFGS',
                 options={'gtol':2e-10,'maxiter':100})
    field=basis@opt.x
    value,grad=objective(opt.x)
    check('finite_reciprocal_stationary_solution',np.max(abs(grad))<2e-8,
          gradient_max=float(max(abs(grad))),iterations=opt.nit,solver_success=bool(opt.success))
    check('finite_solution_bound',np.linalg.norm(field)<=g*np.linalg.norm(rho)/(kappa*lambda1)+2e-9)
    check('finite_solution_nonzero',np.linalg.norm(field)>1e-6)

    result={'status':'PASS','checks':len(checks),'details':checks,
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'momentum_rows':momentum_rows,'curvature':numerical_curvatures,
            'bond_means':[float(np.mean(v)) for v in bond_means],'I1_finite':i1,
            'static_solution':{'norm':float(np.linalg.norm(field)),
                               'min_lapse':float(min(1+g*field)),
                               'objective':value,'gradient_max':float(max(abs(grad)))},
            'scope':'Finite free author challenges. Interacting finite Kato and code checks still separate. IR and convexity are analytical proofs, not proved by these finite cases.'}
    (HERE/'BLOCK05_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in('details','momentum_rows')},indent=2))


if __name__=='__main__':
    run()
