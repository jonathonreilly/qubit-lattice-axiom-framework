#!/usr/bin/env python3
"""Frozen selective controls; no author source code is imported."""
import argparse, importlib.util, json, math, sys, traceback
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.special import erf, roots_jacobi, roots_legendre

p = argparse.ArgumentParser()
p.add_argument('--candidate', required=True)
p.add_argument('--variant', required=True)
args = p.parse_args()
sp = importlib.util.spec_from_file_location('independent_candidate', args.candidate)
c = importlib.util.module_from_spec(sp)
sp.loader.exec_module(c)
rows = []

def emit(name, passed, **values):
    record = {'gate': name, 'passed': bool(passed), 'values': values}
    rows.append(record)
    print(json.dumps(record, sort_keys=True), flush=True)

def adj(x): return np.swapaxes(x.conj(), -1, -2)

def actual_D(m, v, a, q):
    # Recovered directly from the two oriented stencil matrix entries.
    s = math.hypot(m/2, v/a)
    g, J = (s+m/2)/2, (s-m/2)/2
    z = 2j*(g-J*np.exp(-1j*a*np.asarray(q)))
    out = np.zeros(z.shape+(2,2), complex)
    out[...,0,1], out[...,1,0] = z, z.conj()
    return out

def continuum_D(m,v,p):
    z = -v*np.asarray(p)+1j*m
    out = np.zeros(z.shape+(2,2), complex)
    out[...,0,1], out[...,1,0] = z, z.conj()
    return out

def projection(D):
    _, u = np.linalg.eigh(D)
    pos = u[..., :, 1]
    return pos[..., :, None]*pos.conj()[..., None, :]

def fourier_lattice(a, q, sites, coefficients):
    return np.sqrt(a/(2*np.pi))*(np.exp(-1j*a*np.asarray(q)[:,None]*sites[None,:]) @ coefficients)

def spin_controls():
    X=np.array([[0,1],[1,0]],complex)
    Y=np.array([[0,-1j],[1j,0]],complex)
    Z=np.diag([1,-1]).astype(complex)
    I=np.eye(2,dtype=complex)
    N=4; dim=2**N; m,v,a=1.1,.9,.6
    sg=math.hypot(m/2,v/a); g=(sg+m/2)/2; J=(sg-m/2)/2
    def tensor(xs):
        ans=np.array([[1]],complex)
        for x in xs: ans=np.kron(ans,x)
        return ans
    def at(n,P): return tensor([P if k==n else I for k in range(N)])
    xs=[at(n,X) for n in range(N)]; ys=[at(n,Y) for n in range(N)]; zs=[at(n,Z) for n in range(N)]
    gam=[tensor([Z if k<n else (P if k==n else I) for k in range(N)]) for n in range(N) for P in (X,Y)]
    H=-g*sum(zs)-J*sum(xs[n]@xs[n+1] for n in range(N-1))
    dens=[-J*xs[n]@xs[n+1]-.5*g*(zs[n]+zs[n+1]) for n in range(N-1)]
    B=a*sum(n*dens[n] for n in range(N-1))
    P=J*g*sum(xs[n]@ys[n+1]-ys[n]@xs[n+1] for n in range(N-1))
    def coeff(Q):
        A=np.array([[np.trace((1j*(Q@gi-gi@Q))@gj)/dim for gj in gam] for gi in gam])
        return 1j*A
    D=np.zeros((2*N,2*N),complex)
    Pc=np.zeros_like(D)
    for n in range(N):
        D[2*n,2*n+1]=2j*g;D[2*n+1,2*n]=-2j*g
        if n>0:
            D[2*n,2*(n-1)+1]=-2j*J;D[2*(n-1)+1,2*n]=2j*J
        if n<N-1:
            for comp in (0,1):
                Pc[2*n+comp,2*(n+1)+comp]=-2j*J*g
                Pc[2*(n+1)+comp,2*n+comp]=2j*J*g
    XX=np.diag(np.repeat(a*np.arange(N),2))
    Bformal=(XX@D+D@XX)/2-a*D/2
    rH=float(np.max(np.abs(coeff(H)-D)))
    rB=float(np.max(np.abs((coeff(B)-Bformal)[2:6,:])))
    rP=float(np.max(np.abs(coeff(P)-Pc)))
    edge=float(np.max(np.abs(coeff(B)-Bformal)))
    emit('literal_spin_energy_boost_current',max(rH,rB,rP)<2e-12 and edge>.1,energy=rH,bulk_boost=rB,current=rP,retained_endpoint_mismatch=edge)

def intertwining_controls():
    worst={'D':0.,'P':0.,'time':0.,'reality':0.}
    for m,v,a in [(1.4,1.1,.8),(.3,2.,1.2),(2.1,.6,.17)]:
        q=np.linspace(-2.8,2.8,17)/a
        pp=2*np.sin(a*q/2)/a
        M=c.amplitude(m,v,a,pp); A=actual_D(m,v,a,q); D=continuum_D(m,v,pp)
        Pd,Pa=projection(D),projection(A)
        for k in range(len(q)):
            scale=max(1.,np.linalg.norm(M[k]))
            worst['D']=max(worst['D'],float(np.linalg.norm(D[k]@M[k]-M[k]@A[k])/(scale*max(1.,np.linalg.norm(A[k])))))
            worst['P']=max(worst['P'],float(np.linalg.norm(Pd[k]@M[k]-M[k]@Pa[k])/scale))
            worst['time']=max(worst['time'],float(np.linalg.norm(expm(.71j*D[k])@M[k]-M[k]@expm(.71j*A[k]))/scale))
        worst['reality']=max(worst['reality'],float(np.max(np.abs(c.amplitude(m,v,a,-pp)-M.conj()))/max(1.,np.max(np.abs(M)))))
    for name,val in worst.items(): emit('actual_'+name+'_intertwining',val<2e-11,residual=val)

def measure_controls():
    m,v,a=1.4,1.1,.8
    sites=np.array([-2,0,1,3]); z=np.array([[.3,-.2],[1.,.4],[-.5,.7],[.1,.2]])
    y=np.array([[.7,.1],[-.2,.5],[.4,-.3],[.6,.2]])
    x,wt=roots_jacobi(512,-.5,-.5); pp=2*x/a; q=2*np.arcsin(x)/a
    M=c.amplitude(m,v,a,pp)
    zz=fourier_lattice(a,q,sites,z); yy=fourier_lattice(a,q,sites,y)
    iz=np.einsum('nij,nj->ni',M,zz); iy=np.einsum('nij,nj->ni',M,yy)
    dp_weights=(2/a)*wt*np.sqrt(1-x*x)
    got=float(np.sum(dp_weights*np.sum(np.abs(iz)**2,axis=1)))
    wanted=float(np.sum(z*z))
    emit('full_measure_isometry',abs(got-wanted)<2e-10,transported_norm2=got,coefficient_norm2=wanted,residual=abs(got-wanted))
    P=projection(continuum_D(m,v,pp))
    outcov=2*np.sum(dp_weights*np.einsum('ni,nij,nj->n',iz.conj(),P,iy))
    t,ww=roots_legendre(600); qq=np.pi*t/a; ww=ww*np.pi/a
    zin=fourier_lattice(a,qq,sites,z); yin=fourier_lattice(a,qq,sites,y)
    incov=2*np.sum(ww*np.einsum('ni,nij,nj->n',zin.conj(),projection(actual_D(m,v,a,qq)),yin))
    emit('actual_covariance_integral',abs(outcov-incov)<2e-9,input=[incov.real,incov.imag],output=[outcov.real,outcov.imag],residual=float(abs(outcov-incov)))

def alias_controls():
    a=.8; sites=np.arange(-16,17); q=np.linspace(-3.8,3.8,43)
    shifts=np.array([.3,-.2]); factors=np.array([1.,.4])
    cells=np.sqrt(np.pi)/(2*np.sqrt(a))*(erf(a*(sites[:,None]+1)-shifts)-erf(a*sites[:,None]-shifts))*factors
    direct=fourier_lattice(a,q,sites,cells)
    def hat(k):return np.exp(-np.asarray(k)[:,None]**2/4)*np.exp(-1j*np.asarray(k)[:,None]*shifts)*factors/np.sqrt(2)
    got=c.alias_cell(a,q,hat)
    residual=float(np.max(np.abs(got-direct)))
    emit('direct_cell_alias_normalization',residual<3e-11,residual=residual,number_of_cells=len(sites))

def convergence_controls():
    m,v=1.4,1.1
    t,weights=roots_legendre(2048)
    for kind,spacings in [('gaussian',[.8,.4,.2,.1,.05]),('haar',[.5,.25,.125,.0625])]:
        errors=[];details=[]
        for a in spacings:
            if kind=='gaussian':
                sites=np.arange(-math.ceil(9/a),math.ceil(9/a)+1)
                vals=np.sqrt(np.pi)/(2*np.sqrt(a))*(erf(a*(sites+1))-erf(a*sites))
                norm=math.sqrt(np.pi/2)
            else:
                sites=np.arange(-1,math.ceil(1/a)+1)
                vals=np.maximum(0,np.minimum(1,a*(sites+1))-np.maximum(0,a*sites))/np.sqrt(a)
                norm=1.
            cs=np.column_stack([vals,np.zeros_like(vals)])
            q=np.pi*t/a; wq=weights*np.pi/a; pp=2*np.sin(a*q/2)/a; w=np.cos(a*q/2)
            phi=fourier_lattice(a,q,sites,cs)
            image=np.einsum('nij,nj->ni',c.amplitude(m,v,a,pp),phi)
            hat=np.zeros_like(image)
            hat[:,0]=np.exp(-pp**2/4)/np.sqrt(2) if kind=='gaussian' else np.exp(-.5j*pp)*np.sinc(pp/(2*np.pi))/np.sqrt(2*np.pi)
            image_norm=float(np.sum(wq*w*np.sum(np.abs(image)**2,axis=1)))
            cross=np.sum(wq*w*np.sum(image.conj()*hat,axis=1))
            err2=image_norm+norm-2*cross.real
            if err2 < -2e-9:raise ValueError(('negative square distance',kind,a,err2))
            err=math.sqrt(max(0,err2));errors.append(err)
            details.append({'a':a,'error':err,'image_norm2':image_norm,'full_target_norm2':norm,'cross_real':float(cross.real)})
        ok=(errors[-1]<.1 and errors[-1]<.4*errors[0]) if kind=='gaussian' else errors[-1]<.8*errors[0]
        emit('weak_'+kind+'_cell_limit',ok,samples=details,rate_claimed=False)

def boost_controls():
    m,v,a=1.4,1.1,.8; pp=np.array([-.9,-.2,.3,.8,1.2])
    q=2*np.arcsin(a*pp/2)/a; w=np.cos(a*q/2)
    def psi(p):return np.exp(-.4*p*p)*(1+.25j*p+.1*p*p)
    def dpsi(p):return np.exp(-.4*p*p)*(.25j+.2*p-.8*p*(1+.25j*p+.1*p*p))
    def phi(q):
        p=2*np.sin(a*q/2)/a
        return np.sqrt(np.cos(a*q/2))*psi(p)
    def energy(q):return np.abs(actual_D(m,v,a,q)[...,0,1])
    proposed=c.boost_p(m,v,a,pp,psi(pp),dpsi(pp))
    residuals=[]
    for h in [.002,.001,.0005]:
        E=energy(q); dqphi=(phi(q+h)-phi(q-h))/(2*h); dE=(energy(q+h)-energy(q-h))/(2*h)
        actual=(1j*(E*dqphi+.5*dE*phi(q))-.5*a*E*phi(q))/np.sqrt(w)
        residuals.append(float(np.linalg.norm(actual-proposed)/max(1.,np.linalg.norm(proposed))))
    ratio=residuals[0]/max(residuals[-1],1e-30)
    emit('boost_differential_transport',residuals[-1]<2e-6 and (ratio>=10 or max(residuals)<1e-11),residuals=residuals,first_final_ratio=ratio,scope='interior test; smooth compact extension possible')
    b=.4; ep=np.array([1e-3,5e-4,2.5e-4,1.25e-4]); pcut=2/a; pvals=pcut-ep
    qvals=2*np.arcsin(a*pvals/2)/a
    F=c.lattice_frame(m,v,a,qvals); eplus=np.array([1,-1j])/np.sqrt(2)
    lat=np.einsum('nij,j->ni',adj(F),eplus)
    transported=np.einsum('nij,nj->ni',c.amplitude(m,v,a,pvals),lat)
    amp=(1-b*b*pvals*pvals/4)**.25*np.linalg.norm(transported,axis=1)
    slopes=np.diff(np.log(amp))/np.diff(np.log(ep))
    emit('coarse_boost_domain_singularity',np.max(np.abs(slopes+.25))<.02,epsilons=ep.tolist(),amplitudes=amp.tolist(),log_slopes=slopes.tolist(),analytic_domain_reason='one-dimensional H1 representative is continuous, while this interior cutoff is unbounded')
    qc=2*math.asin(b/a)/b
    initial=[qc-.04,qc-.02]; duration=.05
    finals=[]
    for q0 in initial:
        sol=solve_ivp(lambda s,qq:np.abs(actual_D(m,v,b,qq)[...,0,1]),(0,duration),[q0],rtol=1e-11,atol=1e-12)
        if not sol.success:raise RuntimeError(sol.message)
        finals.append(float(sol.y[0,-1]))
    emit('even_boost_band_escape',min(finals)>qc+.01 and max(finals)<np.pi/b,coarse_cutoff_in_fine_q=qc,initial=initial,finals=finals,support_group_parameter=-duration,pullback_characteristic_duration=duration)

def phase_witnesses():
    a,b,m,v=.8,.4,1.4,1.1; lo,hi=.4,2.2
    x,ww=roots_legendre(512); pp=(lo+hi)/2+(hi-lo)*x/2; ww=ww*(hi-lo)/2
    density=np.exp(-2/((pp-lo)*(hi-pp))); weights=ww*density;weights/=weights.sum()
    qa=2*np.arcsin(a*pp/2)/a; qb=2*np.arcsin(b*pp/2)/b
    ka=pp*np.sqrt(1-a*a*pp*pp/4); kb=pp*np.sqrt(1-b*b*pp*pp/4)
    def proj_distance(delta):
        overlap=np.sum(weights*np.exp(1j*delta));return math.sqrt(max(0.,1-abs(overlap)**2))
    ds=proj_distance(.8*(qa-qb)); dc=proj_distance(.9*(ka-kb)); dz=proj_distance(np.zeros_like(pp))
    emit('even_spatial_projection_witness',ds>1e-5 and dz<2e-7,distance=ds,zero_parameter_distance=dz,common_displacement=.8)
    emit('even_actual_current_projection_witness',dc>1e-5 and dz<2e-7,distance=dc,zero_parameter_distance=dz,parameter=.9)

try:
    for fun in [spin_controls,intertwining_controls,measure_controls,alias_controls,convergence_controls,boost_controls,phase_witnesses]: fun()
except Exception:
    traceback.print_exc()
    emit('uncaught_control_error',False,exception=True)
finally:
    passed=sum(r['passed'] for r in rows); failed=len(rows)-passed
    print(json.dumps({'summary':{'variant':args.variant,'pass':passed,'fail':failed,'failed_gates':[r['gate'] for r in rows if not r['passed']],'surviving_gates':[r['gate'] for r in rows if r['passed']]}}),flush=True)
sys.exit(0 if failed==0 else 1)
