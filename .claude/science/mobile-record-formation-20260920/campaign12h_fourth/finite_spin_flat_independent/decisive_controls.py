import json,time
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
from flat_probe import *

TABLE=[[( -5,2),(-3,1),(0,0),(3,1),(5,2),(8,4)], [(-8,4),(-5,2),(-3,1),(0,0),(3,1),(5,2)]]

def expected_h4(a,r,z):
    ret={(a,r,z):12,(1-a,r,z):-2}
    if a==0:ret[1,(r-1)%6,z+(-1 if r==0 else 1)]=2
    else:
        rp=(r+1)%6;ret[0,rp,z-(-1 if rp==0 else 1)]=2
    return ret

def vec_in_basis(v,basis):
    return np.array([complex(v.get(s,0)) for s in basis])/np.sqrt(2)

def physical_limit(v,basis):
    ret=defaultdict(complex)
    for (a,r,z),amp in zip(basis,v):
        for s,c in flat_mode(a,r,z).items():ret[s]+=amp*complex(c)/np.sqrt(2)
    return dict(ret)

def limit_problem(R,K,delta,kappa):
    basis=[(a,r,z) for a in range(2) for r in range(6) for z in range(-R,R+1)]
    bi={s:i for i,s in enumerate(basis)};rr=[];cc=[];vv=[]
    for j,(a,r,z) in enumerate(basis):
        beta,gamma=TABLE[a][r]
        rr.append(j);cc.append(j);vv.append(K*(4*z*z+beta*z+gamma))
        for s,c in expected_h4(a,r,z).items():
            if s in bi:rr.append(bi[s]);cc.append(j);vv.append(delta*c)
    H=sp.csc_matrix((vv,(rr,cc)),shape=(len(basis),len(basis)))
    assert sp.linalg.norm(H-H.T)<1e-13
    v=np.zeros(len(basis),complex)
    for s,a in [((0,0,0),1),((0,3,1),1j),((1,2,-1),-.7)]:v[bi[s]]=a
    v/=np.linalg.norm(v)
    return basis,H,v

def main():
    res={'exact':{},'finite_spin':[],'dynamics':[],'limits':[]}
    exact_count=0
    for a in range(2):
        for r in range(6):
            v=flat_mode(a,r)
            beta,gamma=TABLE[a][r]
            assert compress(h2_apply(v,True))=={(a,r,0):4*f*f+beta*f+gamma}
            hv=h4_apply(v)
            assert not residual(hv)
            assert compress(hv)==expected_h4(a,r,0)
            for coherent in (False,True):
                rv=loss_apply(v,coherent)
                assert not residual(rv)
                assert compress(rv)=={(a,r,0):sy.Integer(4)}
            exact_count+=1
    leak=residual(h2_apply(flat_mode(0,0),True))
    leak_norm_sq=sy.simplify(sum(aa.subs(f,0)**2 for aa in leak.values())/2)
    assert leak_norm_sq==5
    gauss_count=0
    for q in words():
        g=offsets(q)
        for qq,d,e,k,gg in hop_data(q):
            gp=offsets(qq)
            assert all(gp[j]+d==g[j]+(k if j==e else 0) for j in range(8))
            gauss_count+=1
    res['exact']={'flat_basis_modes_checked':exact_count,'electric_counterexample_squared_leakage':str(leak_norm_sq),'exact_Gauss_hop_checks':gauss_count,'D_compression_table':TABLE,'H4_and_both_losses_invariant':True}
    K=.7;delta=1.1;kappa=.4;times=[0.,.05,.15,.4]
    limits={}
    for R in (12,20):
        basis,H,v=limit_problem(R,K,delta,kappa)
        for t in times:
            u=np.exp(-2*kappa*t)*expm_multiply(-1j*t*H,v)
            limits[R,t]=physical_limit(u,basis)
    for t in times:
        d1=limits[12,t];d2=limits[20,t];keys=set(d1)|set(d2)
        err=np.sqrt(sum(abs(d1.get(k,0)-d2.get(k,0))**2 for k in keys))
        assert err<1e-11
        res['limits'].append({'time':t,'flux_cutoffs':[12,20],'state_norm_difference':float(err)})
    for S in (4,8,16,32):
        p,n8,H2,H4,B,R=finite_operators(S,False); C=S*(S+1)
        u0=vec_in_basis(flat_mode(0,0),p)
        exactD=h2_apply(flat_mode(0,0),True)
        exactD={s:c.subs(f,0) for s,c in exactD.items()}
        du=vec_in_basis(exactD,p)
        h2err=np.linalg.norm(C*(H2@u0+4*u0)-du)
        h4u=vec_in_basis(h4_apply(flat_mode(0,0)),p)
        h4err=np.linalg.norm(H4@u0-h4u)
        losserr=np.linalg.norm(R@u0-4*u0)
        res['finite_spin'].append({'S':S,'P_dimension':len(p),'C':C,'H2_C_expansion_error':float(h2err),'C_times_H2_error':float(C*h2err),'H4_error':float(h4err),'loss_error':float(losserr)})
        initial=limits[20,0.]
        v=np.array([initial.get(s,0) for s in p])
        assert abs(np.linalg.norm(v)-1)<1e-13
        Hren=K*C*(H2+4*sp.eye(len(p)))+delta*H4
        gen=-1j*Hren-kappa*R/2
        for t in times:
            u=expm_multiply(t*gen,v)
            expected=limits[20,t];ud={s:a for s,a in zip(p,u)}
            keys=set(ud)|set(expected)
            error=np.sqrt(sum(abs(ud.get(s,0)-expected.get(s,0))**2 for s in keys))
            aa=float(np.vdot(u,u).real);bb=float(sum(abs(x)**2 for x in expected.values()));cc=complex(sum(np.conj(a)*expected.get(s,0) for s,a in ud.items()))
            perpendicular=sum(abs(expected.get(s,0)-(cc/aa)*ud.get(s,0))**2 for s in keys)
            density_error=np.sqrt((aa-bb)**2+4*aa*perpendicular)
            proj=defaultdict(complex)
            for (q,z),amp in ud.items():
                fc,sgn=flat_coord(q,z)
                if fc is not None:proj[fc]+=sgn*amp/np.sqrt(2)
            lifted=defaultdict(complex)
            for (a,r,z),amp in proj.items():
                for s,c in flat_mode(a,r,z).items():lifted[s]+=amp*complex(c)/np.sqrt(2)
            leakage=np.sqrt(sum(abs(ud.get(s,0)-lifted.get(s,0))**2 for s in set(ud)|set(lifted)))
            row={'S':S,'time':t,'state_error':float(error),'density_trace_error':float(density_error),'survival':aa,'limiting_survival':float(np.exp(-4*kappa*t)),'physical_flat_leakage_norm':float(leakage)}
            res['dynamics'].append(row)
        print('completed S',S,'endpoint',res['dynamics'][-1])
    assert res['dynamics'][-1]['state_error']<res['dynamics'][3]['state_error']
    # Two instruments can have different finite-spin losses; check their shared rotor limit directly.
    p,n8,H2,H4,B,R=finite_operators(8,True)
    u0=vec_in_basis(flat_mode(0,0),p)
    res['coherent_spin8_loss_error']=float(np.linalg.norm(R@u0-4*u0))
    res['parameters']={'K':K,'delta':delta,'kappa':kappa,'time_grid':times,'instruments':'resolved dynamic control; both exact rotor losses; finite coherent loss control','numerical_status':'Floating corroboration, no interval or generic-state error certificate.'}
    Path('DECISIVE_RESULTS.json').write_text(json.dumps(res,indent=2)+'\n')
    print(json.dumps(res,indent=2))

if __name__=='__main__':main()
