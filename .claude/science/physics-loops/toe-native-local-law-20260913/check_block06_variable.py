"""Finite Fourier challenges for the analytical variable-frame error bound."""
from pathlib import Path
from itertools import product
import hashlib,json,math,time
import numpy as np

HERE=Path(__file__).resolve().parent
SIG=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
EPS=np.zeros((3,3,3))
for a,b,c in product(range(3),repeat=3):
    EPS[a,b,c]=(a-b)*(b-c)*(c-a)/2


def run():
    start=time.monotonic();checks=[];reports=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    zz=.5;v=math.sqrt(1-zz*zz);star=math.acos(zz)
    F0=np.diag([1,1,v]);inv0=np.diag([1,1,1/v])
    px,py=.7,-.4;K=math.sqrt(px*px+py*py+1)
    grid=128;x=2*math.pi*np.arange(grid)/grid
    pz=np.fft.fftfreq(grid,1/grid)
    psi=np.zeros((grid,2,6),complex)
    for j,q in enumerate((-1,0,1)):
        for orb in(0,1):psi[:,orb,2*j+orb]=np.exp(1j*q*x)
    def mul_symbol(symbol,u):
        return np.fft.ifft(np.einsum('nab,nbc->nac',symbol,np.fft.fft(u,axis=0)),axis=0)
    def opnorm(u):return float(np.linalg.norm(u.reshape(grid*2,6)/math.sqrt(grid),2))
    def neumann(F,m):
        X=np.einsum('ab,nbc->nac',inv0,F-F0)
        power=np.broadcast_to(np.eye(3),(len(F),3,3)).copy();total=power.copy()
        for _ in range(m):
            power=-np.einsum('nab,nbc->nac',power,X);total+=power
        return np.einsum('nab,bc->nac',total,inv0)
    def connection(F,deriv,Q):
        # Only spatial derivative i=3 is nonzero in these examples.
        return -np.einsum('abc,na,nbj,njc->n',EPS,F[:,:,2],deriv,Q)/4
    for family in('xy_shear','all_shears'):
        t,b,c,d=(.025,.015,0.,0.) if family=='xy_shear' else(.025,.015,.01,.008)
        def field(z):
            f=np.zeros((len(z),3,3));f[:,0,0]=t
            if family=='all_shears':f[:,1,1]=-t/2
            f[:,0,1]=f[:,1,0]=b*np.sin(z)
            f[:,0,2]=f[:,2,0]=c*np.cos(z)
            f[:,1,2]=f[:,2,1]=d*np.sin(z)
            return F0+f
        F=field(x);f=F-F0
        derivative=np.zeros_like(F)
        derivative[:,0,1]=derivative[:,1,0]=b*np.cos(x)
        derivative[:,0,2]=derivative[:,2,0]=-c*np.sin(x)
        derivative[:,1,2]=derivative[:,2,1]=d*np.cos(x)
        q=np.array([[t,b,c],[b,t/2 if family=='all_shears' else 0,d],[c,d,0]])
        fbound=float(np.linalg.norm(q));rho=fbound/v;M0=1+fbound
        M1=M3=math.sqrt(2*(b*b+c*c+d*d))
        check(family+'_small_frame_preserves_constant_symbols',fbound<v*v/math.sqrt(10))
        check(family+'_Neumann_rho',rho<1)
        Cexact=connection(F,derivative,np.linalg.inv(F))
        mref=20;Cref=connection(F,derivative,neumann(F,mref))
        etaref=1.5*M0*M1*rho**(mref+1)/(v*(1-rho))
        check(family+'_nonzero_connection',np.max(np.abs(Cexact))>1e-5,amplitude=float(np.max(np.abs(Cexact))))
        check(family+'_reference_connection',np.max(np.abs(Cref-Cexact))<1e-15,
              analytical_tail_bound=etaref)
        if family=='xy_shear':
            expected=-v*t*b*np.cos(x)/(4*(1+t-b*b*np.sin(x)**2))
            check('exact_xy_connection_formula',np.max(np.abs(expected-Cexact))<1e-15)
        for m in(0,2,4):
            Q=neumann(F,m)
            bound=rho**(m+1)/(v*(1-rho))
            residual=float(np.max(np.linalg.norm(Q-np.linalg.inv(F),axis=(1,2))))
            # Frobenius can exceed operator norm; use actual singular values.
            residual=float(np.max(np.linalg.svd(Q-np.linalg.inv(F),compute_uv=False)[:,0]))
            check(family+'_inverse_remainder_'+str(m),residual<=bound+1e-14,error=residual,bound=bound)
        L=np.array([[.5,.5,(zz+2)/(2*v*v)],[.5,.5,(zz+2)/(2*v*v)],[1/v,1/v,1/(2*v)]])
        for w in(-1,1):
            R=np.array([1,1,w]);p=np.array([np.full(grid,px),np.full(grid,py),pz]).T
            tangent=p*np.array([1,1,w*v])
            hlin=np.einsum('na,aij->nij',tangent,SIG)
            continuum=mul_symbol(hlin,psi)
            for a,j in product(range(3),repeat=2):
                V=np.einsum('n,ij->nij',R[a]*p[:,j],SIG[a])
                continuum+=(f[:,a,j,None,None]*mul_symbol(V,psi)+mul_symbol(V,f[:,a,j,None,None]*psi))/2
            continuum+=w*Cref[:,None,None]*psi
            results=[]
            for aa in(.12,.06,.03,.015,1e-6):
                m=6 if aa==1e-6 else 4
                P=K+(m+2)
                check(family+'_separated_bands_'+str((w,aa)),aa*P<star)
                k=np.array([np.full(grid,aa*px),np.full(grid,aa*py),w*star+aa*pz]).T
                sk=np.sin(k);ck=np.cos(k)
                ds=np.array([sk[:,0],sk[:,1],2+zz-ck.sum(axis=1)]).T
                native=mul_symbol(np.einsum('na,aij->nij',ds/aa,SIG),psi)
                vertices=np.empty((grid,3,3))
                vertices[:,0,:]=vertices[:,1,:]=np.array([sk[:,0],sk[:,1],(zz-ck[:,2])*sk[:,2]/(v*v)]).T
                vertices[:,2,:]=np.array([sk[:,2]*sk[:,0]/v,sk[:,2]*sk[:,1]/v,(zz-ck[:,2])/v]).T
                for a,j in product(range(3),repeat=2):
                    V=np.einsum('n,ij->nij',vertices[:,a,j]/aa,SIG[a])
                    native+=(f[:,a,j,None,None]*mul_symbol(V,psi)+mul_symbol(V,f[:,a,j,None,None]*psi))/2
                no_connection=native.copy()
                central=(field(x+aa)-field(x-aa))/(2*aa)
                Q=neumann(F,m);Cm=connection(F,central,Q)
                eta=1.5*M0*M1*rho**(m+1)/(v*(1-rho))+aa*aa*M0*M3/(4*v*(1-rho))
                check(family+'_local_connection_bound_'+str((w,aa)),np.max(np.abs(Cm-Cexact))<=eta+1e-13)
                Bsym=np.einsum('n,ij->nij',sk[:,2]/v,np.eye(2))
                native+=(Cm[:,None,None]*mul_symbol(Bsym,psi)+mul_symbol(Bsym,Cm[:,None,None]*psi))/2
                error=opnorm(native-continuum)
                cm=1.5*M0*(M1+aa*aa*M3/6)/(v*(1-rho))
                bound=aa*P*P/2+aa*aa*P**3/6+aa*P*P*np.sum(q*L)+cm*aa*P/v+eta
                check(family+'_operator_bound_'+str((w,aa)),error+etaref<bound,
                      error=error,analytical_bound=bound,reference_tail=etaref)
                # The polynomial reference has degree <=mref+2; 128-point
                # Parseval is exact for its norm matrix (roundoff excepted).
                check(family+'_Parseval_degree_'+str((w,aa)),2*(mref+3)<grid)
                results.append(dict(spacing=aa,m=m,error=error,bound=bound))
                if aa==1e-6:
                    omitted=opnorm(no_connection-continuum)
                    check(family+'_omitted_connection_has_nonzero_limit_'+str(w),omitted>2e-5 and error<3e-6,
                          omitted_error=omitted,completed_error=error)
            check(family+'_resolved_convergence_'+str(w),all(results[i+1]['error']<results[i]['error'] for i in range(len(results)-1)))
            reports.append(dict(frame=family,node=w,values=results))
    out=dict(status='PASS',checks=len(checks),details=checks,reports=reports,elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Finite Fourier operator challenges on variable frames. Exact continuum connection is enclosed by an analytical Neumann tail; no sampled proof of the general theorem or long-time claim.')
    (HERE/'BLOCK06_VARIABLE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in('details',)},indent=2))

if __name__=='__main__':run()
