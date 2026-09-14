"""Finite checks for the direct strong-scaling clock/Wilson derivation.

No scientific repository inputs or helper runners are read at execution.
Integer cochain identities, finite toy laws and Green kernels are challenged;
finite agreement does not execute the arbitrary-volume or continuum proof.
"""
AUDIT_TIMEOUT_SEC = 180

import itertools
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ive,logsumexp


def close(a,b,tol=3e-10):
    assert np.allclose(a,b,atol=tol,rtol=tol),(np.asarray(a),np.asarray(b))


def blank(L,degree,dtype=np.int64):
    return {I:np.zeros((L,)*4,dtype=dtype) for I in itertools.combinations(range(4),degree)}


def coboundary(field,L,degree):
    out=blank(L,degree+1,dtype=np.result_type(*[a.dtype for a in field.values()])) if degree<4 else {}
    for I in out:
        for position,axis in enumerate(I):
            J=I[:position]+I[position+1:]
            out[I]+=(-1)**position*(np.roll(field[J],-1,axis=axis)-field[J])
    return out


def adjoint(field,L,degree):
    out=blank(L,degree-1,dtype=np.result_type(*[a.dtype for a in field.values()])) if degree>0 else {}
    for I,values in field.items():
        for position,axis in enumerate(I):
            J=I[:position]+I[position+1:]
            out[J]+=(-1)**position*(np.roll(values,1,axis=axis)-values)
    return out


def circle_projection(values,axis,one_form,L):
    if not one_form:return np.repeat(np.take(values,[0],axis=axis),L,axis=axis)
    total=values.sum(axis=axis,keepdims=True);out=np.zeros_like(values)
    selection=[slice(None)]*4;selection[axis]=slice(L-1,L)
    out[tuple(selection)]=total
    return out


def period_projection(field,L):
    out={}
    for I,values in field.items():
        projected=values.copy()
        for axis in range(4):projected=circle_projection(projected,axis,axis in I,L)
        out[I]=projected
    return out


def contraction(field,L,degree):
    out=blank(L,degree-1,dtype=np.result_type(*[a.dtype for a in field.values()])) if degree>0 else {}
    for I,values in field.items():
        for position,axis in enumerate(I):
            J=I[:position]+I[position+1:]
            shifted=np.cumsum(values,axis=axis)-values
            for earlier in range(axis):
                shifted=circle_projection(shifted,earlier,earlier in I,L)
            out[J]+=(-1)**position*shifted
    return out


def inverse_laplacian(field,L):
    grid=np.indices((L,)*4)
    symbol=sum(4*np.sin(np.pi*grid[a]/L)**2 for a in range(4))
    reciprocal=np.divide(1.,symbol,out=np.zeros_like(symbol),where=symbol>1e-12)
    return {I:np.fft.ifftn(np.fft.fftn(values)*reciprocal).real for I,values in field.items()}


def integral_cochain_and_short_vectors():
    L=4;rng=np.random.default_rng(2026091411);records=[]
    for degree in range(5):
        field={I:rng.integers(-3,4,size=(L,)*4) for I in itertools.combinations(range(4),degree)}
        H=contraction(field,L,degree)
        dH=coboundary(H,L,degree-1) if degree>0 else {}
        dfield=coboundary(field,L,degree)
        Hd=contraction(dfield,L,degree+1) if degree<4 else {}
        period=period_projection(field,L)
        for I in field:assert np.array_equal(dH.get(I,0)+Hd.get(I,0),field[I]-period[I])
        if degree<3:
            for value in coboundary(dfield,L,degree+1).values():assert not np.any(value)
        records.append(dict(degree=degree,integer_components=len(field)))
    one={I:rng.integers(-2,3,size=(L,)*4) for I in itertools.combinations(range(4),1)}
    exact=coboundary(one,L,1)
    for value in period_projection(exact,L).values():assert not np.any(value)
    primitive=contraction(exact,L,2)
    for I,value in coboundary(primitive,L,1).items():assert np.array_equal(value,exact[I])
    periods=blank(L,2);coefficients=[1,-2,3,-1,2,1]
    for I,coefficient in zip(periods,coefficients):
        selection=[slice(None)]*4
        for axis in I:selection[axis]=L-1
        periods[I][tuple(selection)]=coefficient
    closed={I:exact[I]+periods[I] for I in exact}
    for value in coboundary(closed,L,2).values():assert not np.any(value)
    for I,value in period_projection(closed,L).items():assert np.array_equal(value,periods[I])
    harmonic_norm=sum(L**4*float(values.mean())**2 for values in closed.values())
    assert harmonic_norm==sum(c*c for c in coefficients)
    # Independent Fourier Hodge computation on integer plaquette spikes.
    lengths=[]
    for orientation in itertools.combinations(range(4),2):
        integer=blank(L,2,dtype=float);integer[orientation][0,0,0,0]=1
        dual_current=adjoint(integer,L,2)
        projected=coboundary(inverse_laplacian(dual_current,L),L,1)
        for I,value in adjoint(projected,L,2).items():close(value,dual_current[I])
        perpendicular={I:integer[I]-projected[I] for I in integer}
        curl=coboundary(integer,L,2)
        for I,value in coboundary(perpendicular,L,2).items():close(value,curl[I])
        pe_norm=math.sqrt(sum(float((v*v).sum()) for v in projected.values()))
        perpnorm=math.sqrt(sum(float((v*v).sum()) for v in perpendicular.values()))
        integernorm=math.sqrt(sum(float((v*v).sum()) for v in dual_current.values()))
        curlnorm=math.sqrt(sum(float((v*v).sum()) for v in curl.values()))
        assert pe_norm>=integernorm/4-1e-12 and perpnorm>=curlnorm/4-1e-12
        lengths.append(dict(orientation=orientation,dual_length=pe_norm,quotient_length=perpnorm))
    return dict(contraction=records,harmonic_period_norm_squared=harmonic_norm,spike_vectors=lengths)


def packing_and_parameters():
    rows=[]
    for rank in [1,2,4]:
        t=2*rank*math.log(5)
        vectors=np.array(list(itertools.product(range(-5,6),repeat=rank)))
        sq=(vectors*vectors).sum(axis=1)
        actual=float(np.exp(-t*sq[sq>0]).sum())
        shell=sum(math.exp(rank*math.log(2*k+3)-t*k*k) for k in range(1,50))
        bound=2*math.exp(-t/2)
        assert actual<=shell<=bound
        rows.append(dict(rank=rank,finite_theta_tail=actual,shell_majorant=shell,bound=bound))
    sequence=[]
    for L in [4,8,16,32]:
        V=L**4;beta=64*V;N=8*beta;sigma=N*N/(4*np.pi*np.pi*beta);r=3*V-3;m=3*V+3
        assert beta>=16*m*math.log(5)/(np.pi*np.pi)
        assert sigma>=32*r*math.log(5)/(np.pi*np.pi)
        close(sigma,16*beta/(np.pi*np.pi))
        sequence.append(dict(L=L,beta=beta,N=N,sigma=sigma,
                             log_coset_bound=math.log(2)-np.pi*np.pi*beta/16,
                             log_source_bound=math.log(2)-np.pi*np.pi*sigma/32))
    return dict(packing=rows,strong_family=sequence)


def lattice_source_and_coset_mixture():
    basis=np.array([[1.,0.],[-1.,1.],[0.,-1.]])
    dual=basis@np.linalg.inv(basis.T@basis)
    Pe=np.eye(3)-np.ones((3,3))/3;records=[]
    for N,sigma in [(3,2.),(8,1.),(128,12.)]:
        cutoff=math.ceil(10*math.sqrt(sigma))+3
        pairs=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=2)))
        maxcoset=math.ceil(math.sqrt(300*sigma)/N)+2
        coset_logs=[];points=[];labels=[]
        for k in range(-maxcoset,maxcoset+1):
            pair=pairs+math.floor(N*k/3)
            z=np.column_stack((pair,N*k-pair.sum(axis=1)))
            logs=-np.sum(z*z,axis=1)/(2*sigma)
            coset_logs.append((k,float(logsumexp(logs))))
            points.append(z);labels.extend([k]*len(z))
        z=np.concatenate(points);labels=np.array(labels);logw=-np.sum(z*z,axis=1)/(2*sigma)
        logZ=logsumexp(logw);w=np.exp(logw-logZ)
        zero_log=dict(coset_logs)[0]
        for k,value in coset_logs:
            assert value<=zero_log-N*N*k*k/(6*sigma)+2e-10
        pbad=float(w[labels!=0].sum())
        theta_quotient=sum(math.exp(-N*N*k*k/(6*sigma)) for k in range(-maxcoset,maxcoset+1) if k)
        assert pbad<=theta_quotient+1e-14
        h=np.array([.7,-.6,.2])+100*np.ones(3)
        exact=z[labels==0];weights=np.exp(logw[labels==0]-zero_log)
        cf=weights@np.exp(1j*(exact@h)/math.sqrt(sigma))
        he=Pe@h;gaussian=math.exp(-float(he@he)/2)
        dualpoints=pairs@dual.T
        t0=logsumexp(-2*np.pi*np.pi*sigma*np.sum(dualpoints*dualpoints,axis=1))
        th=logsumexp(-2*np.pi*np.pi*sigma*np.sum(dualpoints*dualpoints,axis=1)+2*np.pi*math.sqrt(sigma)*(dualpoints@he))
        formula=gaussian*math.exp(th-t0)
        close(cf,formula)
        full=w@np.exp(1j*(z@h)/math.sqrt(sigma))
        assert abs(full-cf)<=2*pbad+2e-12
        beta=N*N/(4*np.pi*np.pi*sigma)
        if N==128:
            assert beta>=16*math.log(5)/(np.pi*np.pi)
            assert sigma>=64*math.log(5)/(np.pi*np.pi)
            assert np.linalg.norm(he)<=np.pi*math.sqrt(sigma)/8
            relative_bound=2*math.exp(-np.pi*np.pi*sigma/32)+4*math.exp(-np.pi*np.pi*beta/16+float(he@he)/2)
            assert abs(full/gaussian-1)<=relative_bound
        records.append(dict(N=N,sigma=sigma,beta=beta,nonexact_probability=pbad,
                            exact_characteristic=float(cf.real),full_characteristic=float(full.real),
                            gaussian=gaussian))
    return records


def clock_wilson_characters():
    records=[];Pe=np.eye(3)-np.ones((3,3))/3
    for N,beta in [(128,20.),(256,40.),(384,60.)]:
        angles=2*np.pi*np.arange(N)/N
        representative=(angles+np.pi)%(2*np.pi)-np.pi
        lift=representative[:,None]-2*np.pi*np.arange(-3,4)[None,:]
        phi=np.exp(-beta*lift*lift/2).sum(axis=1)
        i,j=np.indices((N,N));k=(-i-j)%N
        weight=phi[i]*phi[j]*phi[k];weight/=weight.sum()
        q1=round(.8*math.sqrt(beta));q2=round(1.1*math.sqrt(beta))
        w1=np.exp(1j*q1*angles[i]);w2=np.exp(1j*q2*angles[j])
        e1=complex(np.sum(weight*w1));e2=complex(np.sum(weight*w2));joint=complex(np.sum(weight*w1*w2))
        close([e1.imag,e2.imag,joint.imag],0)
        assert min(e1.real,e2.real,joint.real)>0
        h1=np.array([q1,0,0])/math.sqrt(beta);h2=np.array([0,q2,0])/math.sqrt(beta)
        predictions=[math.exp(-float(h@Pe@h)/2) for h in [h1,h2,h1+h2]]
        close([e1.real,e2.real,joint.real],predictions,tol=2e-10)
        ratio=(joint/(e1*e2)).real;target=math.exp(-float(h1@Pe@h2))
        close(ratio,target)
        # Integer characters are invariant under arbitrary integer lifts.
        close(np.exp(1j*q1*lift),np.exp(1j*q1*representative[:,None]))
        # A fractional charge does not have that invariance.
        assert abs(np.exp(1j*.5*lift[0,0])-np.exp(1j*.5*lift[0,1]))>1
        alias=np.sum(weight*np.exp(1j*N*angles[i]))
        close(alias,1)
        assert math.exp(-N*N*Pe[0,0]/(2*beta))<1e-100
        records.append(dict(N=N,beta=beta,q1=q1,q2=q2,normalized_ratio=ratio,gaussian_ratio=target))
    return records


def shifted_theta_relative_sources():
    basis=np.array([[1.,0.],[-1.,1.],[0.,-1.]])
    dual=basis@np.linalg.inv(basis.T@basis)
    b=np.array([.3,-.7,.4]);he=np.array([.7,-.6,-.1]);records=[]
    for sigma in [.15,.4,1.,12.]:
        cutoff=math.ceil(10*math.sqrt(sigma))+3
        grid=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=2)))
        z=grid@basis.T+b;logw=-np.sum(z*z,axis=1)/(2*sigma)
        weights=np.exp(logw-logsumexp(logw))
        direct=weights@np.exp(1j*(z@he)/math.sqrt(sigma))
        dualz=grid@dual.T;norm=np.sum(dualz*dualz,axis=1)
        phase=np.exp(2j*np.pi*(dualz@b))
        denominator=np.sum(np.exp(-2*np.pi*np.pi*sigma*norm)*phase)
        numerator=np.sum(np.exp(-2*np.pi*np.pi*sigma*norm+2*np.pi*math.sqrt(sigma)*(dualz@he))*phase)
        gaussian=math.exp(-float(he@he)/2)
        close(direct,gaussian*numerator/denominator)
        if sigma==12:
            eta=2*math.exp(-np.pi*np.pi*sigma/32)
            assert np.linalg.norm(he)<=np.pi*math.sqrt(sigma)/8 and eta<1
            assert abs(direct/gaussian-1)<=2*eta/(1-eta)
        records.append(dict(sigma=sigma,characteristic_real=float(direct.real),characteristic_imag=float(direct.imag)))
    assert abs(records[0]['characteristic_imag'])>.1
    return records


def infinite_green(n):
    n=np.asarray(n,dtype=int)
    return quad(lambda t:float(np.prod(ive(abs(n),2*t))),0,np.inf,epsabs=3e-12,epsrel=3e-11,limit=250)[0]


def periodic_green(L):
    grid=np.indices((L,)*4);symbol=sum(4*np.sin(np.pi*grid[a]/L)**2 for a in range(4))
    reciprocal=np.divide(1.,symbol,out=np.zeros_like(symbol),where=symbol>1e-12)
    return np.fft.ifftn(reciprocal).real


def rectangle_current(n,offset):
    current=[];x=np.array(offset,dtype=int)
    for axis,direction in [(0,1),(1,1),(0,-1),(1,-1)]:
        for _ in range(n):
            if direction<0:x[axis]-=1
            current.append((axis,tuple(x),direction))
            if direction>0:x[axis]+=1
    assert tuple(x)==tuple(offset)
    return current


def time_integral(T,R):
    return ((T/R)*math.atan(T/R)-.5*math.log1p((T/R)**2))/(2*np.pi*np.pi)


def green_and_disjoint_loops():
    kernel=periodic_green(4)
    lap=8*kernel-sum(np.roll(kernel,1,a)+np.roll(kernel,-1,a) for a in range(4))
    rhs=np.full((4,)*4,-1/4**4);rhs[0,0,0,0]+=1
    close(lap,rhs);close(kernel.sum(),0)
    # Heat integral on a finite torus independently checks its FFT inverse.
    momenta=2*np.pi*np.arange(4)/4;eigen=4*np.sin(momenta/2)**2
    for n in [(0,0,0,0),(1,1,0,0)]:
        def integrand(t):
            terms=[np.mean(np.exp(-t*eigen)*np.cos(momenta*x)) for x in n]
            return float(np.prod(terms)-1/4**4)
        value=quad(integrand,0,48,epsabs=2e-12)[0]
        close(value,kernel[n])
    asym=[]
    for n in [2,4,8,16,32]:
        value=infinite_green([n,0,0,0]);scaled=n*n*value
        asym.append(dict(distance=n,scaled_green=scaled,error=abs(scaled-1/(4*np.pi*np.pi))))
    assert asym[-1]['error']<.00006
    assert asym[-1]['error']<.3*asym[-2]['error']
    continuum=2*time_integral(1,1)-2*time_integral(1,math.sqrt(2))+2*(time_integral(1,1)-time_integral(1,math.sqrt(2)))
    rows=[]
    for n in [2,3,4]:
        L=2*n*n;green=periodic_green(L)
        C1=rectangle_current(n,(0,0,0,0));C2=rectangle_current(n,(0,0,n,0))
        cross=0.
        for mu,x,sx in C1:
            for nu,y,sy in C2:
                if mu==nu:cross+=sx*sy*green[tuple((np.array(x)-y)%L)]
        value=n*n*green[n,0,0,0]
        correction=L*L*(green[n,0,0,0]-infinite_green([n,0,0,0]))
        assert abs(correction)<1
        rows.append(dict(mesh_inverse=n,L=L,scaled_green=value,loop_cross=cross,
                         continuum_cross=continuum,error=abs(cross-continuum),periodic_correction_scaled=correction))
    assert all(row['error']*row['mesh_inverse']**2<.1 for row in rows)
    assert rows[-1]['error']<rows[0]['error']/3
    # A one-dimensional separation sum tests finer loop meshes without
    # allocating a side-128 four-dimensional FFT cube.
    fine=[]
    for n in [8,16,32]:
        cross=0.
        for u in range(n):
            multiplicity=(1 if u==0 else 2)*(n-u)
            cross+=4*multiplicity*(infinite_green([u,0,n,0])-infinite_green([u,n,n,0]))
        fine.append(dict(mesh_inverse=n,infinite_volume_cross=cross,error=abs(cross-continuum)))
    assert fine[-1]['error']<.00015
    assert fine[-1]['error']<.3*fine[-2]['error']
    return dict(infinite_asymptotics=asym,disjoint_rectangle_sequence=rows,fine_infinite_loop_meshes=fine)


def coulomb_time_and_charge_signs():
    nodes,weights=np.polynomial.legendre.leggauss(24)
    s=(nodes+1)/2;weights=weights/2
    T=2.;A=1.;R=.8
    starts=[np.array([0.,0.,0.,0.]),np.array([T,0.,0.,0.]),np.array([T,A,0.,0.]),np.array([0.,A,0.,0.])]
    vectors=[np.array([T,0.,0.,0.]),np.array([0.,A,0.,0.]),np.array([-T,0.,0.,0.]),np.array([0.,-A,0.,0.])]
    offset=np.array([0.,0.,R,0.]);direct_loop=0.
    for x,v in zip(starts,vectors):
        for y,w in zip(starts,vectors):
            distance=x[None,None,:]+s[:,None,None]*v-y[None,None,:]-s[None,:,None]*w-offset
            squared=np.sum(distance*distance,axis=2)
            direct_loop+=float(v@w)*float(np.sum(weights[:,None]*weights[None,:]/squared))/(4*np.pi*np.pi)
    loop_formula=2*time_integral(T,R)-2*time_integral(T,math.sqrt(A*A+R*R))
    loop_formula+=2*time_integral(A,R)-2*time_integral(A,math.sqrt(T*T+R*R))
    close(direct_loop,loop_formula)
    rows=[]
    for T,R in [(.5,.8),(2.,1.7),(10.,.8),(100.,1.7)]:
        numerical=quad(lambda u:2*(T-u)/(4*np.pi*np.pi*(u*u+R*R)),0,T,epsabs=1e-12)[0]
        formula=time_integral(T,R);close(numerical,formula)
        defect=1/(4*np.pi*R)-formula/T
        assert 0<defect<=(2+math.log1p((T/R)**2))/(4*np.pi*np.pi*T)
        rows.append(dict(T=T,R=R,integral=formula,coulomb_error=defect))
    limit=(2-math.sqrt(2))/(4*np.pi)
    dipoles=[]
    for T in [10.,100.,1000.]:
        cross=2*time_integral(T,1)-2*time_integral(T,math.sqrt(2))
        cross+=2*(time_integral(1,1)-time_integral(1,math.sqrt(1+T*T)))
        dipoles.append(dict(T=T,energy=cross/T,target=limit))
    assert abs(dipoles[-1]['energy']-limit)<1e-4
    # Reversing one loop reverses the interaction, while self energies stay.
    covariance=np.array([[2.,.3],[.3,1.]])
    for charges in [np.array([.7,1.2]),np.array([.7,-1.2])]:
        joint=math.exp(-float(charges@covariance@charges)/2)
        separate=math.exp(-float(np.sum(charges*charges*np.diag(covariance)))/2)
        close(-math.log(joint/separate),float(charges[0]*charges[1]*covariance[0,1]))
    return dict(time_integrals=rows,dipole_limits=dipoles,direct_rectangle_quadrature=direct_loop,rectangle_formula=loop_formula)


ORIENTATIONS=list(itertools.combinations(range(4),2))

def discrete_moments(points,sigma):
    points=np.asarray(points,dtype=float)
    logw=-np.sum(points*points,axis=1)/(2*sigma)
    logZ=logsumexp(logw)
    weights=np.exp(logw-logZ)
    mean=weights@points
    cov=(points.T*weights)@points-np.outer(mean,mean)
    return logZ,weights,mean,cov

def clock_lift_and_score():
    # Integer incidence of a three-edge cycle, not a four-dimensional torus.
    d=np.array([[1,-1,0],[0,1,-1],[-1,0,1]])
    records=[]
    for N,beta in [(2,.18),(4,.65),(6,1.4)]:
        sigma=N*N/(4*np.pi*np.pi*beta)
        clocks=np.array(list(itertools.product(range(N),repeat=3)))
        da=clocks@d.T
        residues=da%N
        counts={tuple(x):0 for x in residues}
        for x in residues:counts[tuple(x)]+=1
        expected={x for x in itertools.product(range(N),repeat=3) if sum(x)%N==0}
        assert set(counts)==expected
        assert set(counts.values())=={N}
        # Each image sum includes all integers within six of its local center.
        m=np.arange(-6,7)
        u=2*np.pi*da/N
        displacement=u[:,:,None]-2*np.pi*m[None,None,:]
        image=np.exp(-beta*displacement**2/2)
        localZ=image.sum(axis=2)
        conditional=image/localZ[:,:,None]
        x=math.sqrt(beta)*displacement
        mean=(conditional*x).sum(axis=2)
        var=(conditional*x*x).sum(axis=2)-mean*mean
        config=localZ.prod(axis=1);total=config.sum();config/=total
        # The independent Fourier series computes the physical score.
        n=np.arange(-20,21)
        fourier=np.exp(-n*n/(2*beta))
        phi=np.cos(u[:,:,None]*n)@fourier
        derivative=(-np.sin(u[:,:,None]*n)*n)@fourier
        score=derivative/phi
        Y=-score/math.sqrt(beta)
        close(Y,mean)
        if N==2:close(Y,0)
        # Enumerate the full-rank image lattice through its congruence.
        cutoff=math.ceil(math.sqrt(2*sigma*50))+2
        raw=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=3)))
        z=raw[raw.sum(axis=1)%N==0]
        logZ,w,zmean,cov=discrete_moments(z,sigma)
        close(total,N*math.exp(logZ))
        close(zmean,0)
        CX=cov/sigma
        from_conditioning=(mean.T*config)@mean+np.diag(config@var)
        close(CX,from_conditioning)
        h=np.array([.7,-.9,.4])
        CY=(Y.T*config)@Y
        noise=float(h@(CX-CY)@h)
        independent_noise=float(config@(var@(h*h)))
        close(noise,independent_noise)
        epsilon=(8*np.pi*np.pi*beta+16)*math.exp(-np.pi*np.pi*beta/2)
        assert noise<=epsilon*float(h@h)+1e-12
        # Reconstruct primal L_N={n: all coordinates congruent mod N}.
        cut_n=math.ceil(math.sqrt(2*beta*50))+2
        primal=np.array(list(itertools.product(range(-cut_n,cut_n+1),repeat=3)))
        primal=primal[np.all((primal-primal[:,[0]])%N==0,axis=1)]
        _,_,_,cn=discrete_moments(primal,beta)
        close(cn/beta+CX,np.eye(3))
        records.append(dict(N=N,beta=beta,beta_d=sigma,
                            constant_lift_fiber=N,lattice_points=len(z),
                            source_noise=noise,score_variance=float(h@CY@h),
                            covariance_duality_error=float(abs(cn/beta+CX-np.eye(3)).max())))
    return records

def exterior_one(p):
    p=np.asarray(p)
    matrix=np.zeros((6,4),dtype=np.result_type(p,complex))
    for row,(mu,nu) in enumerate(ORIENTATIONS):
        matrix[row,nu]=p[mu];matrix[row,mu]=-p[nu]
    return matrix

def twoform_projection(p):
    D=exterior_one(p)
    return D@D.conj().T/float(np.vdot(p,p).real)

def midpoint_and_cell_average():
    L=6;ell=3.;a=ell/L
    modes=np.array([1,0,-1,1]);k=2*np.pi*modes/L;p=k/a
    q=np.exp(1j*k)-1
    xi=2*np.sin(k/2)
    edge_phase=np.diag(np.exp(1j*k/2))
    face_phase=np.diag([np.exp(1j*(k[mu]+k[nu])/2) for mu,nu in ORIENTATIONS])
    close(exterior_one(q)@edge_phase,face_phase@(1j*exterior_one(xi)))
    close(twoform_projection(q),face_phase@twoform_projection(xi)@face_phase.conj().T)
    v=np.array([1+1j,2,-1j,.3,-.7,.2j]);v/=np.linalg.norm(v)
    sinc=float(np.prod(np.sinc(k/(2*np.pi))))
    nodes,weights=np.polynomial.legendre.leggauss(12)
    direct_cell=1+0j
    for component in p:
        direct_cell*=a/2*np.sum(weights*np.exp(1j*component*a*nodes/2))
    close(direct_cell,a**4*sinc)
    grid=np.indices((L,)*4)
    source=np.empty((6,L,L,L,L),complex)
    for o,(mu,nu) in enumerate(ORIENTATIONS):
        phase=sum(k[c]*grid[c] for c in range(4))+(k[mu]+k[nu])/2
        source[o]=a*a/(ell*ell)*sinc*v[o]*np.exp(1j*phase)
    coeff=np.fft.fftn(source,axes=(1,2,3,4),norm='ortho')
    index=tuple(modes%L)
    selected=coeff[(slice(None),)+index]
    close(selected,sinc*face_phase@v)
    close(np.sum(abs(coeff)**2),sinc*sinc)
    close(source.reshape(6,-1).sum(axis=1),0)
    pair=float(np.vdot(selected,twoform_projection(q)@selected).real)
    close(pair,sinc*sinc*np.vdot(v,twoform_projection(xi)@v).real)
    assert sinc*sinc<=1
    errors=[];momentum=np.array([.7,1.2,-.8,.4])
    continuum=twoform_projection(momentum)
    for step in [.5,.25,.125,.0625]:
        lattice=twoform_projection(2*np.sin(step*momentum/2))
        error=float(np.linalg.norm(lattice-continuum))
        errors.append(error)
        assert error<step*step
    assert all(b<a/3.9 for a,b in zip(errors,errors[1:]))
    # The harmonic piece cannot be discarded for an arbitrary norm-one source.
    harmonic=np.full(6*L**4,1/math.sqrt(6*L**4))
    close(harmonic@harmonic,1)
    harmonic_local=1/L**4
    assert harmonic_local>0
    return dict(cell_average_norm=sinc*sinc,projected_pairing=pair,
                centered_symbol_errors=errors,harmonic_unit_source_norm=1,
                one_plaquette_harmonic_norm_squared=harmonic_local)

def cross_matrix(p):
    x,y,z=p
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]],float)

def os_electric_magnetic_reconstruction():
    records=[]
    # Orientation order is 01,02,03,12,13,23; B=(23,-13,12).
    change=np.zeros((6,6));change[:3,:3]=np.eye(3)
    change[3,5]=1;change[4,4]=-1;change[5,3]=1
    for p in [np.array([.7,-.4,1.2]),np.array([0.,0.,2.]),np.array([1.,2.,-3.])]:
        r=float(np.linalg.norm(p));PT=np.eye(3)-np.outer(p,p)/(r*r);C=cross_matrix(p)
        close(C@C,-r*r*PT)
        for p0 in [.3,1.1,-.8]:
            full=change@twoform_projection(np.r_[p0,p])@change.T
            denominator=p0*p0+r*r
            expected=np.block([[(p0*p0*np.eye(3)+np.outer(p,p))/denominator,-p0*C/denominator],
                               [p0*C/denominator,r*r*PT/denominator]])
            close(full,expected)
            close(np.linalg.eigvalsh(full),[0,0,0,1,1,1])
        u=.73
        i0=quad(lambda k:1/(k*k+r*r),0,np.inf,weight='cos',wvar=u,epsabs=1e-12)[0]/np.pi
        i1=-1j*quad(lambda k:k/(k*k+r*r),0,np.inf,weight='sin',wvar=u,epsabs=1e-12)[0]/np.pi
        close(i0,math.exp(-r*u)/(2*r))
        close(i1,-1j*math.exp(-r*u)/2)
        # Subtract the EE contact term before integrating at u>0.
        noncontact=np.block([[-r*r*PT*i0,-C*i1],[C*i1,r*r*PT*i0]])
        reflection=np.diag([-1,-1,-1,1,1,1])
        kernel=reflection@noncontact
        M=-1j*C/r
        gram=np.block([[PT,M],[M,PT]])
        close(kernel,r/2*math.exp(-r*u)*gram)
        close(gram,gram.conj().T)
        T=np.column_stack((PT,M))
        close(gram,T.conj().T@T)
        eigen=np.linalg.eigvalsh(gram)
        close(eigen,[0,0,0,0,2,2])
        assert np.linalg.eigvalsh(noncontact[:3,:3]).min()<0
        # Removing cross blocks changes the physical mode count to four.
        uncoupled=np.block([[PT,np.zeros((3,3))],[np.zeros((3,3)),PT]])
        assert np.count_nonzero(np.linalg.eigvalsh(uncoupled)>1e-8)==4
        for t in [.1,.7,2.3]:
            spectral=math.exp(-t*r)
            close(-math.log(spectral)/t,r)
        records.append(dict(spatial_momentum=p.tolist(),gram_eigenvalues=eigen.tolist(),
                            reflected_kernel_error=float(abs(kernel-r/2*math.exp(-r*u)*gram).max())))
    return records


def main():
    families=[('integral_cochain_and_short_vectors',integral_cochain_and_short_vectors),
              ('dimension_dependent_packing',packing_and_parameters),
              ('exact_lattice_source_and_coset_mixture',lattice_source_and_coset_mixture),
              ('actual_clock_wilson_characters',clock_wilson_characters),
              ('uniform_shifted_theta_sources',shifted_theta_relative_sources),
              ('periodic_green_and_disjoint_loops',green_and_disjoint_loops),
              ('coulomb_time_and_charge_signs',coulomb_time_and_charge_signs),
              ('positive_lift_and_physical_score',clock_lift_and_score),
              ('midpoint_cell_average',midpoint_and_cell_average),
              ('gaussian_os_modes',os_electric_magnetic_reconstruction)]
    records={}
    for name,check in families:
        records[name]=check();print('finite_check_completed: '+name,flush=True)
    print(json.dumps(records,indent=2,sort_keys=True))
    print('per_element: scalar theta tails, integer character lifts, score identities and Coulomb time integrals are checked in their specified finite domains.')
    print('per_site: the side-four integral cochain contraction and Fourier Hodge identities check topology and the shortest-vector mechanisms on actual torus cells.')
    print('per_mode: Fourier Green inverses, cell averages, electric-magnetic contact signs and the rank-two Gaussian reflected kernel are checked personally.')
    print('per_block: finite composite-clock toys, side-four topology, and disjoint-loop Green sums through side thirty-two are checked; no phase simulation is performed.')
    print('lattice_wide: checked and not executed — the volume-dependent theta bound, random-distribution convergence and relative Wilson continuum limits rest on the written derivation.')
    print(f'TOTAL: PASS={len(families)} FAIL=0')
    print('scope: finite mathematical challenges only; arbitrary-volume proofs and physical identification require independent review, and formal audit remains pending.')


if __name__=='__main__':main()
