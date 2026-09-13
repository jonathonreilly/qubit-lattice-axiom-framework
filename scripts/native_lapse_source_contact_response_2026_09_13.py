"""Finite checks of specified native lapse source and contact response.

The paired note proves the free infrared asymptotic and global convexity.
This runner checks exact identities, finite spectra, local Pauli algebra and
an exact rational canonical witness. No physical metric selection is tested.
"""
from pathlib import Path
from itertools import product
from math import isqrt
import hashlib
import json
import math
import time
import numpy as np
import sympy as s
from scipy.optimize import minimize
from scipy.linalg import null_space

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_LAPSE_SOURCE_CONTACT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-13.md',
)
ROOT = Path(__file__).resolve().parents[1]

WITNESS = {'lambda': -20,
 'sector_particles': 3,
 'basis': [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 49, 50, 52, 56],
 'lower_ground_shift': '-8.34999098',
 'vector_scale': 1000000000000,
 'trials': [{'sign': -1,
             'vector': [[-69953857841, 0],
                        [0, 476342142492],
                        [-48520647199, 0],
                        [0, -362071479381],
                        [-48520647199, 0],
                        [0, 0],
                        [15890090581, 0],
                        [3757719813, 0],
                        [0, 0],
                        [48520647199, 0],
                        [0, -362071479381],
                        [15890090581, 0],
                        [0, 0],
                        [0, 0],
                        [-45717547625, 0],
                        [0, -362071479381],
                        [48520647199, 0],
                        [0, -362071479381],
                        [69953857841, 0],
                        [0, 476342142492]]},
            {'sign': 1,
             'vector': [[69588897206, 0],
                        [0, -484092203592],
                        [48834972553, 0],
                        [0, 356914794857],
                        [48834972553, 0],
                        [0, 0],
                        [-15689818047, 0],
                        [-3774579822, 0],
                        [0, 0],
                        [-48834972553, 0],
                        [0, 356914794857],
                        [-15689818047, 0],
                        [0, 0],
                        [0, 0],
                        [45006200156, 0],
                        [0, 356914794857],
                        [-48834972553, 0],
                        [0, 356914794857],
                        [-69588897206, 0],
                        [0, -484092203592]]}]}

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


def run_free():
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

    # Independent finite derivatives challenge the actual source at an
    # inhomogeneous lapse, including the division required for congruence.
    for kind in ('A', 'C'):
        hn = matrix(N1, kind)
        vals, vecs, pn, en0 = spectral(hn)
        if kind == 'A':
            source = np.array([np.trace(pn@cell).real for cell in hx])
        else:
            source = np.real(np.diag(hn@pn)).reshape(vol,2).sum(axis=1)/N1
        for cell in (0, 7, vol-1):
            delta = np.zeros(vol)
            delta[cell] = .00001
            finite = (spectral(matrix(N1+delta,kind))[3]
                      -spectral(matrix(N1-delta,kind))[3])/.00002
            near('inhomogeneous_source_derivative_'+kind+'_'+str(cell),
                 source[cell], finite, tol=2e-8)

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
    return result


def run_fock():
    start=time.monotonic()
    checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        d=a-b
        vals=list(d) if isinstance(d,s.MatrixBase) else [d]
        check(name,all(s.simplify(x)==0 for x in vals))
    def near(name,a,b,tol=2e-9):
        residual=float(np.max(abs(np.asarray(a)-np.asarray(b))))
        check(name,residual<tol,max_residual=residual,tolerance=tol)
    c=[]
    for j in range(6):
        a=s.zeros(64)
        for word in range(64):
            if word&(1<<j):
                a[word^(1<<j),word]=(-1)**((word&((1<<j)-1)).bit_count())
        c.append(a)
    ident=s.eye(64)
    occ=[a.H*a for a in c]
    B0, B1 = ident-2*occ[0], ident-2*occ[1]
    A01 = -s.I*(c[0]+c[0].H)*(c[1]+c[1].H)
    eq('exact_native_imaginary_hopping_dictionary',
       -A01*(ident-B0*B1)/2, s.I*(c[0].H*c[1]-c[1].H*c[0]))
    sigma1=s.Matrix([[0,1],[1,0]])
    sigma3=s.diag(1,-1)
    hop=(-sigma3+s.I*sigma1)/2
    bonds=[]
    for x in range(2):
        bond=s.zeros(64)
        for i in range(2):
            for j in range(2):
                term=hop[i,j]*c[2*x+i].H*c[2*(x+1)+j]
                bond+=term+term.H
        bonds.append(bond)
    lam=s.symbols('lam',real=True)
    ox=[s.Rational(5,2)*(occ[2*x]-occ[2*x+1])
        +lam*(occ[2*x]-ident/2)*(occ[2*x+1]-ident/2) for x in range(3)]
    hx=[o+sum((bonds[j]/2 for j in range(2) if x in(j,j+1)),s.zeros(64))
        for x,o in enumerate(ox)]
    ham=sum(hx,s.zeros(64))
    totaln=sum(occ,s.zeros(64))
    eq('exact_interacting_number_conservation',ham*totaln,totaln*ham)
    eq('exact_local_energy_continuity',
       s.I*(ham*hx[0]-hx[0]*ham)
       +sum((s.I*(hx[0]*hx[y]-hx[y]*hx[0]) for y in(1,2)),s.zeros(64)),s.zeros(64))
    check('current_is_nonzero',hx[0]*hx[1]-hx[1]*hx[0]!=s.zeros(64))
    results=[]
    sector=[word for word in range(64) if word.bit_count()==3]
    check('declared_three_particle_sector',len(sector)==20)
    for strength in(-20,-5,-1,-.2,0,.2,1,5,20):
        op=[np.array(o.subs(lam,strength).extract(sector,sector),complex) for o in ox]
        bb=[np.array(b.extract(sector,sector),complex) for b in bonds]
        hh=sum(op)+sum(bb)
        values,vectors=np.linalg.eigh(hh)
        check('finite_many_body_gap_'+str(strength),values[1]-values[0]>1e-6,
              gap=float(values[1]-values[0]))
        ground=vectors[:,0]
        energies=[a+sum((bb[j]/2 for j in range(2) if x in(j,j+1)),np.zeros_like(a))
                  for x,a in enumerate(op)]
        off=np.array([vectors[:,1:].conj().T@h@ground for h in energies])
        chi=-2*np.einsum('xi,yi,i->xy',off.conj(),off,1/(values[1:]-values[0])).real
        bmean=[float(np.vdot(ground,b@ground).real) for b in bb]
        contact=np.zeros((3,3))
        for x,b in enumerate(bmean):
            v=np.zeros(3)
            v[x],v[x+1]=1,-1
            contact-=b*np.outer(v,v)/4
        cc=chi+contact
        near('interacting_arithmetic_uniform_null_'+str(strength),chi@np.ones(3),np.zeros(3))
        check('interacting_arithmetic_sign_'+str(strength),np.max(np.linalg.eigvalsh(chi))<1e-10)
        direction=np.array([1.,-2.,1.])
        # The preserved 45-digit convergence diagnosis resolves the first
        # lambda=-20 failure as the five-point formula's O(step^4) error.
        step=.0005 if abs(strength)>=10 else .001
        record={'lambda':strength,'gap':float(values[1]-values[0]),
                'ground_number':float(np.vdot(ground,np.array(totaln.extract(sector,sector),float)@ground).real),
                'chiA_direction':float(direction@chi@direction),
                'chiC_direction':float(direction@cc@direction),'bond_energy':bmean}
        for kind,target in(('A',chi),('C',cc)):
            es={}
            for n in(-2,-1,0,1,2):
                N=1+n*step*direction
                factors=[(N[x]+N[x+1])/2 if kind=='A' else np.sqrt(N[x]*N[x+1]) for x in range(2)]
                hn=sum(N[x]*op[x] for x in range(3))+sum(factors[x]*bb[x] for x in range(2))
                e=np.linalg.eigvalsh(hn)[0]
                es[n]=e
            second=(-es[2]+16*es[1]-30*es[0]+16*es[-1]-es[-2])/(12*step**2)
            predicted=direction@target@direction
            near('actual_interacting_energy_curvature_'+kind+'_'+str(strength),
                 second,predicted,tol=2e-6)
        results.append(record)
        if strength==.2:
            check('interacting_response_is_exercised',record['chiA_direction']<-.001)

    # Exact symplectic Pauli words on a 4-by-2 rectangle. Every edge is a
    # physical edge qubit; this is a small literal carrier, not CAR matrices.
    vertices=[(x,y) for x in range(4) for y in range(2)]
    edges=[]
    for v in vertices:
        for delta in((1,0),(0,1)):
            w=(v[0]+delta[0],v[1]+delta[1])
            if w in vertices:
                edges.append(tuple(sorted((v,w))))
    edges.sort()
    ei={e:i for i,e in enumerate(edges)}
    incident={v:sorted([e for e in edges if v in e]) for v in vertices}
    # Ignore the scalar phase for commutation; X and Z masks suffice.
    def mul(a,b):
        return a[0]^b[0],a[1]^b[1]
    def commute(a,b):
        return ((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2==0
    def edgeword(v,w):
        e=tuple(sorted((v,w)))
        z=0
        for endpoint in(v,w):
            for f in incident[endpoint]:
                if f<e:
                    z^=1<<ei[f]
        return 1<<ei[e],z
    def parity(v):
        return 0,sum(1<<ei[e] for e in incident[v])
    candidates=[e for e in edges if e[0][0]==e[1][0] and e[0][0]%2==1]
    protected=[e for e in edges if e not in candidates]
    cycles=[]
    for x in range(3):
        path=[(x,0),(x+1,0),(x+1,1),(x,1),(x,0)]
        word=(0,0)
        for v,w in zip(path,path[1:]):
            word=mul(word,edgeword(v,w))
        cycles.append(word)
    generators=[edgeword(*e) for e in protected]+[parity(v) for v in vertices]
    for i,a in enumerate(generators):
        check('native_generator_cycle_centrality_'+str(i),all(commute(a,c) for c in cycles))
        check('native_generator_candidate_Z_'+str(i),
              all(commute(a,(0,1<<ei[e])) for e in candidates))
    check('two_literal_candidate_record_edges',len(candidates)==2)
    # A missed direct candidate would be rejected by its own Z commutator.
    check('candidate_hopping_negative_control',
          all(not commute(edgeword(*e),(0,1<<ei[e])) for e in candidates))
    eq('native_quartic_identity',
       (1-2*s.symbols('n0'))*(1-2*s.symbols('n1'))/4,
       (s.symbols('n0')-s.Rational(1,2))*(s.symbols('n1')-s.Rational(1,2)))

    out={'status':'PASS','checks':len(checks),'details':checks,
         'finite_interacting_probes':results,
         'elapsed_seconds':time.monotonic()-start,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'scope':'Finite three-cell, three-particle-sector author checks; no small-coupling Weyl interval is asserted for these sampled couplings. No interacting thermodynamic convexity, infrared coefficient or quantum gravity claimed.'}
    return out


def run_certificate():
    start = time.monotonic()
    data = WITNESS
    checks = []

    def check(name, condition):
        assert bool(condition), name
        checks.append(name)

    basis = [word for word in range(64) if word.bit_count() == 3]
    check('fixed_declared_sector', data['basis'] == basis
          and data['sector_particles'] == 3 and data['lambda'] == -20)
    index = {word: n for n, word in enumerate(basis)}
    dim = len(basis)
    onsite = []
    for x in range(3):
        diagonal = []
        for word in basis:
            a, b = (word >> (2*x)) & 1, (word >> (2*x+1)) & 1
            diagonal.append(s.Rational(5, 2)*(a-b)
                            - 20*(a-s.Rational(1, 2))*(b-s.Rational(1, 2)))
        onsite.append(s.diag(*diagonal))

    # Direct occupation-basis CAR signs, independent of the full-space JW
    # matrices in the other finite checker.
    def adag_a(i, j):
        result = s.zeros(dim)
        for col, word in enumerate(basis):
            if not (word >> j) & 1:
                continue
            sign = (-1)**((word & ((1 << j)-1)).bit_count())
            after = word ^ (1 << j)
            if (after >> i) & 1:
                continue
            sign *= (-1)**((after & ((1 << i)-1)).bit_count())
            result[index[after | (1 << i)], col] = sign
        return result

    W = s.Matrix([[-1, s.I], [s.I, 1]]) / 2
    bond = s.zeros(dim)
    for x in range(2):
        for a in range(2):
            for b in range(2):
                t = W[a, b]*adag_a(2*x+a, 2*(x+1)+b)
                bond += t+t.H
    H0 = sum(onsite, s.zeros(dim)) + bond
    check('literal_hermitian_matrix', H0 == H0.H)
    lower = s.Rational(data['lower_ground_shift'])
    matrix = H0-lower*s.eye(dim)
    L = s.eye(dim)
    pivots = []
    for j in range(dim):
        pivot = s.cancel(matrix[j, j]-sum(L[j, k]*s.conjugate(L[j, k])*pivots[k]
                                          for k in range(j)))
        check('strict_positive_rational_pivot_'+str(j), pivot.is_Rational and pivot > 0)
        pivots.append(pivot)
        for i in range(j+1, dim):
            L[i, j] = s.cancel((matrix[i, j]-sum(
                L[i, k]*s.conjugate(L[j, k])*pivots[k] for k in range(j)))/pivot)
    residue = L*s.diag(*pivots)*L.H-matrix
    check('exact_LDL_reconstruction', all(s.cancel(v) == 0 for v in residue))

    trials = []
    for trial in data['trials']:
        sign = trial['sign']
        check('trial_sign_'+str(sign), sign in (-1, 1))
        eps = s.Rational(sign, 1000)
        N = [1+eps, 1-2*eps, 1+eps]
        check('positive_mean_one_lapse_'+str(sign), min(N) > 0 and sum(N) == 3)
        # Scale cancels in a Rayleigh quotient; retain integer Gaussian entries.
        vector = s.Matrix([a+s.I*b for a, b in trial['vector']])
        norm = (vector.H*vector)[0]
        check('nonzero_trial_'+str(sign), norm.is_Rational and norm > 0)
        diagonal = s.cancel((vector.H*sum((N[x]*onsite[x] for x in range(3)),
                                          s.zeros(dim))*vector)[0]/norm)
        coefficient = s.cancel((vector.H*bond*vector)[0]/norm)
        check('real_rational_rayleigh_parts_'+str(sign),
              diagonal.is_Rational and coefficient.is_Rational)
        square = N[0]*N[1]
        scale = 10**20
        root_floor = isqrt(int(s.numer(square))*scale**2//int(s.denom(square)))
        lo, hi = s.Rational(root_floor, scale), s.Rational(root_floor+1, scale)
        check('exact_sqrt_bracket_'+str(sign), 0 <= lo and lo**2 <= square <= hi**2)
        upper = diagonal+coefficient*(hi if coefficient >= 0 else lo)
        trials.append(dict(sign=sign, upper_rational=str(upper),
                           upper_display=float(upper), sqrt_interval=[str(lo), str(hi)]))
    check('both_opposite_trials', sorted(t['sign'] for t in trials) == [-1, 1])
    midpoint_upper = sum(s.Rational(t['upper_rational']) for t in trials)/2
    margin = lower-midpoint_upper
    check('strict_midpoint_convexity_violation', margin > s.Rational(8, 100000))
    out = dict(status='PASS', checks=len(checks), details=checks,
               lower_ground_bound=str(lower), trial_bounds=trials,
               midpoint_violation_margin_rational=str(margin),
               midpoint_violation_margin_display=float(margin),
               positive_LDL_pivots=[str(p) for p in pivots],
               elapsed_seconds=time.monotonic()-start,
               source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               scope='Exact finite three-cell, three-particle-sector nonconvexity at lambda=-20. No grand-canonical or weak-coupling claim.')
    return out

if __name__ == '__main__':
    result = {'free': run_free(), 'fock': run_fock(), 'certificate': run_certificate()}
    receipt = ROOT/'outputs/native_lapse_source_contact_response_2026_09_13.json'
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result, indent=2)+'\n')
    for family, data in result.items():
        for row in data['details']:
            print('PASS '+family+': '+(row if isinstance(row,str) else row['name']))
    print('per_element: Exact band vertices, mean derivatives, contact signs and rational Rayleigh inequalities are exercised.')
    print('per_site: Actual position-space energy cells, literal Fock CAR signs and physical edge Pauli commutators are checked.')
    print('per_mode: All 27 reciprocal modes of the declared three-cubed free torus are compared with its position Hessian.')
    print('per_block: Finite interacting sectors and an exact three-particle midpoint witness are checked, with the sector fixed explicitly.')
    print('lattice_wide: The integral limit, quartic-log remainder and convexity proofs are analytical in the note; infinity is not enumerated.')
    print('Scientific input reads: no external data files; frozen trial vectors are in this source. Integrity read: this source for its hash; the cache also binds the paired note.')
    print('TOTAL: PASS='+str(sum(d['checks'] for d in result.values()))+' FAIL=0')
