#!/usr/bin/env python3
"""Independent actual-path, Stokes, KKT and counting controls; no repo helpers."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import itertools, json, time, sys, traceback
from collections import Counter
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
from scipy.sparse.linalg import cg, LinearOperator

checks=[]; details={}; started=time.time()
def record(name,ok,**data):
    checks.append(dict(name=name,passed=bool(ok),**data))
def tidy(c): return Counter({k:v for k,v in c.items() if v})
def plus(x,mu,n=1):
    y=list(x); y[mu]+=n; return tuple(y)
def walk(pos,mu,sgn,links):
    if sgn>0: links[(pos,mu)]+=1; return plus(pos,mu)
    nxt=plus(pos,mu,-1); links[(nxt,mu)]-=1; return nxt

def templates(L):
    h=L//2; zero=(0,)*4; perms=list(itertools.permutations(range(4)))
    contours=[[] for _ in range(4)]; surfaces=[[] for _ in range(4)]
    axial_sum=Counter(); root_sum=[Counter() for _ in range(4)]
    straight=[Counter() for _ in range(4)]; worst=0; failures=0; mut=False
    for y in itertools.product(range(-h,h+1),repeat=4):
        for order in perms:
            pos=zero; axial=Counter(); steps=[]
            for nu in order:
                for _ in range(abs(y[nu])):
                    sign=1 if y[nu]>0 else -1
                    base=pos if sign>0 else plus(pos,nu,-1)
                    steps.append((base,nu,sign))
                    pos=walk(pos,nu,sign,axial)
            axial_sum.update(axial)
            for mu in range(4):
                c=axial.copy(); pos=y
                for _ in range(L): pos=walk(pos,mu,1,c)
                for (base,nu),coef in axial.items(): c[(plus(base,mu,L),nu)]-=coef
                surface=Counter()
                for base,nu,sign in steps:
                    if nu==mu: continue
                    rho,sigma=sorted((nu,mu)); orient=1 if nu<mu else -1
                    for t in range(L): surface[(plus(base,mu,t),rho,sigma)]+=sign*orient
                surface=tidy(surface); bd=boundary(surface)
                expected=c.copy()
                for t in range(L): expected[(plus(zero,mu,t),mu)]-=1
                failures+=int(tidy(bd)!=tidy(expected)); worst=max(worst,sum(abs(v) for v in surface.values()))
                if surface and not mut:
                    damaged=surface.copy(); k=next(iter(damaged)); damaged[k]-=1
                    mut=(tidy(boundary(damaged))!=tidy(expected))
                contours[mu].append(tidy(c)); surfaces[mu].append(surface); root_sum[mu].update(c)
        for mu in range(4):
            for t in range(L): straight[mu][(plus(y,mu,t),mu)]+=1
    M=24*L**4; spread_fail=0; spreadnorm=0
    for mu in range(4):
        surfmean=Counter()
        for s in surfaces[mu]: surfmean.update(s)
        bdmean=boundary(surfmean)
        for c,s in zip(contours[mu],surfaces[mu]):
            lhs=Counter({k:M*v for k,v in boundary(s).items()}); lhs.subtract(bdmean)
            rhs=Counter({k:M*v for k,v in c.items()}); rhs.subtract(root_sum[mu])
            spread_fail+=int(tidy(lhs)!=tidy(rhs))
            ds=Counter({k:M*v for k,v in s.items()}); ds.subtract(surfmean)
            spreadnorm=max(spreadnorm,sum(abs(v) for v in ds.values())/M)
    record('all_actual_L3_swept_surface_boundaries',failures==0,contours=4*M,failures=failures,largest_l1=worst)
    record('all_actual_L3_centered_spread_boundaries',spread_fail==0,spreads=4*M,failures=spread_fail,largest_l1=spreadnorm)
    record('deleted_plaquette_mutation_rejected',mut)
    # A raw contour has nonzero boundary, whereas a spread must be a cycle.
    c=contours[0][-1]; endpoint=Counter()
    for (x,mu),coef in c.items(): endpoint[x]-=coef; endpoint[plus(x,mu)]+=coef
    record('missing_mean_spread_mutation_rejected',bool(tidy(endpoint)),endpoint_coefficients=list(tidy(endpoint).values()))
    return root_sum,straight,axial_sum,contours,M

def boundary(surface):
    out=Counter()
    for (x,r,s),v in surface.items():
        out[(x,r)]+=v; out[(plus(x,r),s)]+=v
        out[(plus(x,s),r)]-=v; out[(x,s)]-=v
    return tidy(out)

class Cell:
    def __init__(self,N,p):
        self.N=N; self.h=N//2; self.p=np.asarray(p); self.V=N**4
        self.sites=list(itertools.product(range(-self.h,self.h+1),repeat=4))
        self.pairs=list(itertools.combinations(range(4),2)); self.root=self.site((0,)*4)[0]
    def site(self,x):
        w=tuple((v+self.h)%self.N-self.h for v in x)
        shift=np.array([(v-z)//self.N for v,z in zip(x,w)])
        idx=0
        for v in w: idx=idx*self.N+v+self.h
        return idx,np.exp(1j*np.dot(self.p,shift))
    def link(self,x,mu):
        i,z=self.site(x); return 4*i+mu,z
    def grad(self):
        rr=[];cc=[];vv=[]
        for i,x in enumerate(self.sites):
            for mu in range(4):
                y,z=self.site(plus(x,mu)); rr += [4*i+mu]*2; cc += [y,i]; vv += [z,-1]
        return sp.coo_matrix((vv,(rr,cc)),shape=(4*self.V,self.V)).tocsr()
    def curl(self):
        rr=[];cc=[];vv=[]
        for i,x in enumerate(self.sites):
            for k,(r,s) in enumerate(self.pairs):
                for xx,mu,coef in [(x,r,1),(plus(x,r),s,1),(plus(x,s),r,-1),(x,s,-1)]:
                    col,z=self.link(xx,mu); rr.append(6*i+k);cc.append(col);vv.append(coef*z)
        return sp.coo_matrix((vv,(rr,cc)),shape=(6*self.V,4*self.V)).tocsr()
    def rows(self,outN,templates,denom,scalar=False,L=3):
        out=Cell(outN,self.p); rr=[];cc=[];vv=[]
        for i,X in enumerate(out.sites):
            origin=tuple(L*v for v in X)
            ts=[templates] if scalar else templates
            for mu,t in enumerate(ts):
                row=i if scalar else 4*i+mu
                for (x,nu),coef in t.items():
                    if not coef: continue
                    xx=tuple(a+b for a,b in zip(origin,x));col,z=self.link(xx,nu)
                    rr.append(row);cc.append(col);vv.append(coef*z/denom)
        return sp.coo_matrix((vv,(rr,cc)),shape=((1 if scalar else 4)*out.V,4*self.V)).tocsr()

def co_projector(p):
    nu=np.expm1(1j*np.asarray(p)); nu_bar=np.expm1(-1j*np.asarray(p));psi=nu_bar@nu
    return np.eye(4)-np.outer(nu,nu_bar)/psi,nu,nu_bar

def one_step(p,kappa,root_t,str_t,alpha_t,M,selected):
    f=Cell(3,p); c=Cell(1,p); G=f.grad(); C=f.curl(); Q=f.rows(1,root_t,M); S=f.rows(1,str_t,81); alpha=f.rows(1,alpha_t,M,scalar=True)
    keep=np.arange(f.V)!=f.root; Gamma=G[:,keep].toarray()
    H=(C.conj().T@C+kappa*Q.conj().T@Q).toarray()
    # Root-zero scalar gauge removes exactly the minimizer kernel for p != 0.
    K=np.block([[H,Gamma],[Gamma.conj().T,np.zeros((80,80))]])
    rhs=np.vstack([kappa*Q.conj().T.toarray(),np.zeros((80,4))])
    sol=la.solve(K,rhs,assume_a='her')[:324]
    residual=np.eye(4)-Q@sol; curvature=C@sol
    spread=[]
    for mu in range(4):
        t=selected[mu]; raw=f.rows(1,[t]*4,1).toarray()[mu]
        spread.append((raw-Q.toarray()[mu])@sol)
    return f,G,C,Q,S,alpha,sol,residual,curvature,np.asarray(spread)

def main():
    rt,st,at,contours,M=templates(3)
    selected=[cs[-1] for cs in contours]
    p=np.array([0.43,-0.71,1.12,0.29]);kap=1.37
    f,G,C,Q,S,alpha,sol,res,curv,z=one_step(p,kap,rt,st,at,M,selected)
    nu=np.expm1(1j*p);ev=np.zeros((1,81));ev[0,f.root]=1
    err=lambda a: float(np.max(np.abs(a)))
    record('actual_root_covariance',err(Q@G-np.outer(nu,ev[0]))<1e-10,error=err(Q@G-np.outer(nu,ev[0])))
    record('actual_root_straight_funnel',err(Q.toarray()-S.toarray()+np.outer(nu,alpha.toarray()[0]))<1e-10,error=err(Q.toarray()-S.toarray()+np.outer(nu,alpha.toarray()[0])))
    record('curl_gradient_zero',err((C@G).toarray())<1e-10,error=err((C@G).toarray()))
    record('normalized_stationarity',err(C.conj().T@curv-kap*Q.conj().T@res)<2e-8,error=err(C.conj().T@curv-kap*Q.conj().T@res))
    record('root_zero_gauge_constraint',err(G[:,np.arange(81)!=f.root].conj().T@sol)<2e-8,error=err(G[:,np.arange(81)!=f.root].conj().T@sol))
    record('gradient_data_annihilated',max(err(res@nu),err(curv@nu),err(z@nu))<2e-8,error=max(err(res@nu),err(curv@nu),err(z@nu)))
    P,_,_=co_projector(p)
    noise=Q@Q.conj().T; straightnoise=S@S.conj().T
    record('projected_root_straight_noise',err(P@(noise.toarray()-straightnoise.toarray())@P)<1e-10,error=err(P@(noise.toarray()-straightnoise.toarray())@P))
    record('unprojected_noise_mutation_rejected',err(noise.toarray()-straightnoise.toarray())>1e-3,difference=err(noise.toarray()-straightnoise.toarray()))
    lap=(G.conj().T@G).toarray(); lapinv=la.inv(lap)
    B=S@np.kron(lapinv,np.eye(4))@S.conj().T
    U=la.null_space(nu.conj()[None,:]); Bc=U.conj().T@B@U
    Hhard=la.inv(Bc); Hsoft=la.inv(Bc+np.eye(3)/kap)
    direct=U.conj().T@(kap*res)@U
    record('direct_KKT_matches_soft_Schur',err(direct-Hsoft)<2e-8,error=err(direct-Hsoft))
    rootH=la.sqrtm(Hhard).astype(complex)
    comparison=rootH@la.inv(np.eye(3)+rootH@rootH/kap)@rootH
    record('hard_soft_factorization_on_CoCl',err(comparison-Hsoft)<2e-8,error=err(comparison-Hsoft))
    record('hard_soft_order_on_CoCl',float(np.min(la.eigvalsh(Hhard-Hsoft)))>=-1e-10,minimum=float(np.min(la.eigvalsh(Hhard-Hsoft))))
    record('unprojected_inverse_mutation_rejected',err((P@B@P)@(U@Hhard@U.conj().T)-np.eye(4))>0.1,identity_failure=err((P@B@P)@(U@Hhard@U.conj().T)-np.eye(4)))
    for r in [3,9]:
        # One periodic cell counts every link incidence, including multiplicity.
        cell=Cell(r,np.zeros(4)); direct=[Counter() for _ in range(4)]
        for x in cell.sites:
            for mu in range(4):
                for t in range(r): direct[mu][(plus(x,mu,t),mu)]+=1
        D=cell.rows(1,direct,r**4,L=r).toarray()
        row=D.sum(axis=1).real; col=D.sum(axis=0).real
        record('counting_sums_r_'+str(r),max(err(row-r),err(col-r**-3))<1e-10,row=list(row),column_min=float(col.min()),column_max=float(col.max()))
        record('wrong_adjoint_scale_r_'+str(r)+'_rejected',err(col-r**-1)>0.01,difference=err(col-r**-1))
    f0=Cell(3,np.zeros(4));G0=f0.grad();C0=f0.curl();Q0=f0.rows(1,rt,M).toarray()
    lift=np.tile(np.eye(4)/3,(81,1));zero_res=np.eye(4)-Q0@lift
    record('harmonic_zero_energy_lift',max(err(zero_res),err(C0@lift))<1e-10,error=max(err(zero_res),err(C0@lift)))
    record('harmonic_residual_identity_mutation_rejected',err(np.eye(4)-zero_res)>0.9)
    record('d3_length_rescaling_mutation_rejected',err(Q0@lift/3-np.eye(4))>0.5,difference=err(Q0@lift/3-np.eye(4))))
    # Complete periodic top torus, built by direct gauge-constrained minimizations.
    T=3; shape=(T,)*4; fhat=np.zeros(shape+(486,4),complex);rhat=np.zeros(shape+(4,4),complex);zhat=np.zeros(shape+(4,4),complex)
    maxstat=0
    for idx in itertools.product(range(T),repeat=4):
        if idx==(0,)*4: continue
        p=2*np.pi*np.array(idx)/T
        ff,gg,cc,qq,ss,aa,mm,rr,cur,zz=one_step(p,1.,rt,st,at,M,selected)
        fhat[idx]=9*cur;rhat[idx]=rr;zhat[idx]=zz
        maxstat=max(maxstat,err(cc.conj().T@cur-qq.conj().T@rr))
    kernels={'F0':np.fft.ifftn(fhat,axes=(0,1,2,3)),'r0':np.fft.ifftn(rhat,axes=(0,1,2,3)),'spread_selected':np.fft.ifftn(zhat,axes=(0,1,2,3))}
    normrows={};m=.003
    for name,K in kernels.items():
        offsets=np.repeat(np.array(f0.sites)/3,6,axis=0) if name=='F0' else np.zeros((4,4))
        vals=np.abs(K);weighted=np.empty_like(vals)
        for idx in itertools.product(range(T),repeat=4):
            x=np.array(idx)[None,:]+offsets
            dist=np.sum(np.abs((x+T/2)%T-T/2),axis=1)
            weighted[idx]=vals[idx]*np.exp(m*dist)[:,None]
        row=weighted.sum(axis=(0,1,2,3,5));column=weighted.sum(axis=(0,1,2,3,4))
        normrows[name]={'row_max':float(row.max()),'column_max':float(column.max()),'columns':column.tolist(),'column_to_row':float(column.max()/row.max()),'imaginary_max':err(K.imag)}
    record('periodic_all_80_nonzero_fibres_stationary',maxstat<2e-8,max_error=maxstat)
    record('real_periodic_kernels',max(v['imaginary_max'] for v in normrows.values())<1e-10,max_imaginary=max(v['imaginary_max'] for v in normrows.values()))
    record('actual_kernel_density_loss_mutation_rejected',normrows['F0']['column_max']>normrows['F0']['row_max'],row=normrows['F0']['row_max'],column=normrows['F0']['column_max'],density=81)
    record('actual_spread_is_nonzero',normrows['spread_selected']['row_max']>1e-4,row=normrows['spread_selected']['row_max'])
    details['periodic_norms']=normrows;details['periodic_scope']={'T':T,'L':3,'depth':1,'m':m,'solver':'explicit root-zero-gauge KKT','source_orientations':4,'fine_plaquette_offsets_and_orientations':486,'selected_spreads':4}
    # Two-level direct normal solve with the coupled nested gauge kernel.
    p=np.array([.43,-.71,1.12,.29]);fine=Cell(9,p);mid=Cell(3,p)
    Gf=fine.grad();Cf=fine.curl();Gm=mid.grad();Cm=mid.curl();Qa=fine.rows(3,rt,M);Qb=mid.rows(1,rt,M);Sb=mid.rows(1,st,81)
    k0=.7;k1=1.4; nf=4*fine.V;nm=4*mid.V
    H=sp.bmat([[Cf.conj().T@Cf+k0*Qa.conj().T@Qa,-k0*Qa.conj().T],[-k0*Qa,k0*sp.eye(nm)+k1*Qb.conj().T@Qb]],format='csr')
    er=[];ec=[]
    for i,x in enumerate(mid.sites): er.append(i);ec.append(fine.site(tuple(3*v for v in x))[0])
    E=sp.coo_matrix((np.ones(len(er)),(er,ec)),shape=(mid.V,fine.V)).tocsr()
    keep=np.arange(fine.V)!=fine.root;Gam=sp.vstack([Gf,Gm@E],format='csr')[:,keep]
    rng=np.random.default_rng(27029);test=rng.normal(size=Gam.shape[1]);gaugeerr=la.norm(H@(Gam@test))/max(1,la.norm(Gam@test))
    record('nested_gauge_kernel_actual_chain',gaugeerr<1e-10,error=float(gaugeerr))
    v=np.array([.4+.2j,-.3+.1j,.7-.1j,.2+.3j]);rhs=np.r_[np.zeros(nf),k1*(Qb.conj().T@v)]
    def action(x):return H@x+Gam@(Gam.conj().T@x)
    Aop=LinearOperator(H.shape,matvec=action,dtype=complex)
    diag=np.asarray(H.diagonal()).real+np.asarray(Gam.multiply(Gam.conj()).sum(axis=1)).ravel().real
    prec=LinearOperator(H.shape,matvec=lambda x:x/diag,dtype=complex);steps=[0]
    def tick(x):steps[0]+=1
    sol,info=cg(Aop,rhs,M=prec,rtol=1e-12,atol=1e-14,maxiter=15000,callback=tick)
    af=sol[:nf];am=sol[nf:];rtop=v-Qb@am;rlow=am-Qa@af
    st_error=la.norm(H@sol-rhs)/max(1,la.norm(rhs));transport=err(rlow-(k1/k0)*(Sb.conj().T@rtop))
    record('depth_two_actual_stationarity',info==0 and st_error<2e-8,solver_info=int(info),iterations=steps[0],relative_error=float(st_error))
    record('depth_two_residual_transport_variable_kappa',transport<2e-8,error=transport)
    record('depth_two_wrong_kappa_mutation_rejected',err(rlow-Sb.conj().T@rtop)>1e-5,error=err(rlow-Sb.conj().T@rtop))
    record('depth_two_wrong_residual_sign_mutation_rejected',err(rlow+(k1/k0)*(Sb.conj().T@rtop))>1e-5,error=err(rlow+(k1/k0)*(Sb.conj().T@rtop)))
    # Actual positive plaquette average, with its own directly counted coefficients.
    rr=[];cc=[];vv=[]
    for i,X in enumerate(mid.sites):
        origin=tuple(3*v for v in X)
        for pair,(mu,nu) in enumerate(mid.pairs):
            for y in itertools.product(range(-1,2),repeat=4):
                base=tuple(a+b for a,b in zip(origin,y))
                for t in range(3):
                    for u in range(3):
                        x=plus(plus(base,mu,t),nu,u); ix,phase=fine.site(x)
                        rr.append(6*i+pair);cc.append(6*ix+pair);vv.append(phase/81)
    Q2=sp.coo_matrix((vv,(rr,cc)),shape=(6*mid.V,6*fine.V)).tocsr()
    Ffine=81*(Cf@af);Fmid=9*(Cm@am);dr=9*(Cm@rlow)
    correct=err(Fmid-(Q2@Ffine)/9-dr);wrong=err(Fmid-Q2@Ffine-dr)
    record('depth_two_curvature_scale_identity',correct<2e-8,error=correct)
    record('missing_curvature_scale_mutation_rejected',wrong>1e-4,error=wrong)
    details['depth_two']={'fine_side':9,'middle_side':3,'kappa':[k0,k1],'degrees_of_freedom':nf+nm,'gauge_parameters':Gam.shape[1]}

if __name__=='__main__':
    exception=None
    try: main()
    except Exception:
        exception=traceback.format_exc();traceback.print_exc()
    result={'schema':'review-uniform-soft-independent01-v1','checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'details':details,'exception':exception,'elapsed_seconds':time.time()-started,'finite_scope_only':True,'author_helpers_imported':False}
    print(json.dumps(result,indent=2))
    sys.exit(0 if exception is None and all(c['passed'] for c in checks) else 1)
