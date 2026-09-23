"""Physical local compensation identities, naive cancellation, and two births."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from collections import defaultdict
import importlib.util,hashlib,json,math
import numpy as np
import scipy.sparse as sparse
D=Path(__file__).resolve().parent
p=D.parent/'cube_unprepared_author/cube_physical_controls.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='20f0a6abf4066098cf719b74af22f9826d803b6ee51d9d772ed9ab56e104ce80'
spec=importlib.util.spec_from_file_location('cube_physical',p)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
q0=tuple(int(a in m.aset) for a in range(8));zero=(0,)*12

def clean(v):return {s:a for s,a in v.items() if a!=0}
def norm(v):return math.sqrt(sum(abs(a)**2 for a in v.values()))
def distance(v,w):return norm({s:v.get(s,0)-w.get(s,0) for s in set(v)|set(w)})

def electric(q,E):
    # P only: every allowed matter hop is outward from one occupied A.
    assert m.grade(q)==0
    value=0
    for qq,df,e,k in m.hop_table(q):value+=E[e]*(E[e]+k)
    assert value>=0
    return value

def delta(v,S):return {s:a*electric(*s)/(S*(S+1)) for s,a in v.items()}

def hop(v,targetgrade,S=None,site=None,outward=None):
    result=defaultdict(float)
    for (q,E),amp in v.items():
        for qq,shift in m.paths.legal_hops(q,m.edges):
            if m.grade(qq)!=targetgrade:continue
            if site is not None:
                if outward and not (q[site]!=0 and qq[site]==0):continue
                if not outward and not (q[site]==0 and qq[site]!=0):continue
            e=next(j for j,x in enumerate(shift) if x);k=shift[e]
            weight=1. if S is None else m.weight(E[e],k,S)
            if weight:result[qq,m.paths.add(E,shift)]-=amp*weight
    return clean(result)

def M(v,S=None):return hop(hop(v,1,S),0,S)
def Zsquare(v,S=None):
    for w in (1,2,1,0):v=hop(v,w,S)
    return v

def C1_naive(v):
    total=defaultdict(float)
    for a in m.aset:
        term=hop(hop(v,2,site=a,outward=True),1,site=a,outward=False)
        for s,c in term.items():total[s]+=c
    return clean(total)

def H4_compensated(v,S):
    first=M(delta(v,S),S);second=delta(M(v,S),S);third=Zsquare(v,S)
    return clean({s:-.5*(first.get(s,0)+second.get(s,0)+third.get(s,0))
                  for s in set(first)|set(second)|set(third)})

def direct_local_C(p,S):
    words,fields=p;ix={s:i for i,s in enumerate(words)};rr=[];cc=[];vv=[];Ds=[]
    for j,((q,f),E) in enumerate(zip(words,fields)):
        outward=m.hop_table(q);degree=len(outward)
        rr.append(j);cc.append(j);vv.append(float(degree))
        Ds.append(electric(q,E))
        for mid,df,e,k in outward:
            w=m.weight(int(E[e]),k,S)
            if not w:continue
            E1=E.copy();E1[e]+=k;f1=tuple(a+b for a,b in zip(f,df))
            vacated=next(a for a in m.aset if q[a]!=0 and mid[a]==0)
            # This is the local F_a^*F_a definition, with diagonal replaced
            # by its unit-weight count; no precomputed M is imported here.
            for qq,df2,e2,k2 in m.hop_table(mid):
                if not (mid[vacated]==0 and qq[vacated]!=0):continue
                if m.grade(qq)!=0:continue
                w2=m.weight(int(E1[e2]),k2,S)
                if not w2:continue
                to=(qq,tuple(a+b for a,b in zip(f1,df2)));i=ix.get(to)
                assert i is not None
                if i==j:continue
                rr.append(i);cc.append(j);vv.append(w*w2)
    return sparse.csc_matrix((vv,(rr,cc)),shape=(len(words),len(words))),np.array(Ds)

def finite_identity_controls():
    rows=[]
    for S in [1,2]:
        for number in [4,6,8]:
            p=m.states(number,0,S);q=m.states(number,1,S)
            A=m.hops(p,q,S);mass=A.T@A;C,diag=direct_local_C(p,S)
            residual=C-mass-sparse.diags(diag/(S*(S+1)))
            error=float(max(abs(residual.data),default=0.))
            herm=C-C.T;herm_error=float(max(abs(herm.data),default=0.))
            assert error<2e-12 and herm_error<2e-12
            assert min(diag,default=0)>=0
            # All cube A vertices are distance two: gates kill C outside P.
            tested=0
            for word in m.paths.charges(number):
                if m.grade(word)==0:continue
                for a in m.aset:
                    gate=all(word[c]!=0 for c in m.aset if c!=a)
                    assert not gate or word[a]==0;tested+=1
            rows.append({'S':S,'N':number,'P_dimension':len(p[0]),
                         'direct_local_C_minus_M_minus_D_over_C_max_error':error,
                         'direct_C_Hermiticity_error':herm_error,
                         'D_range':[int(min(diag,default=0)),int(max(diag,default=0))],
                         'outside_P_site_gate_checks':tested})
            print(json.dumps(rows[-1]),flush=True)
    return rows

def first_vector(edge=0,signs=(1,)):
    v=defaultdict(float)
    for q,E in m.paths.effective_paths(q0,m.edges,m.aset,edge,list(signs)):v[q,E]+=1.
    return dict(v)

def two_birth_controls():
    rows=[]
    for coherent_first in [False,True]:
        for coherent_second in [False,True]:
            total=0.;firsttotal=0.;count=0
            firstsigns=[[-1,1]] if coherent_first else [[-1],[1]]
            secondsigns=[[-1,1]] if coherent_second else [[-1],[1]]
            for edge in range(12):
                for signs in firstsigns:
                    v=first_vector(edge,signs);firsttotal+=norm(v)**2
                    for nextedge in range(12):
                        for nextsigns in secondsigns:
                            out=defaultdict(float)
                            for (q,E),a in v.items():
                                for qq,dE in m.paths.effective_paths(q,m.edges,m.aset,nextedge,nextsigns):
                                    field=m.paths.add(E,dE)
                                    assert m.paths.gauss_difference(q0,qq,field,m.edges)
                                    out[qq,field]+=a
                            total+=sum(abs(a)**2 for a in out.values());count+=bool(out)
            assert abs(firsttotal-48)<2e-12 and total==384
            rows.append({'coherent_first':coherent_first,'coherent_second':coherent_second,
                         'summed_first_norm_squared':firsttotal,
                         'summed_two_birth_norm_squared':total,
                         'small_time_N8_coefficient_over_kappa_squared':total/2,
                         'nonzero_two_mark_channels':count})
    return rows

def path_and_core_controls():
    first=first_vector()
    seeds={'initial_four':{(q0,zero):1.},'actual_resolved_first_unnormalized':first}
    result=[]
    for label,v in seeds.items():
        z=Zsquare(v)
        cq=hop(C1_naive(hop(v,1)),0)
        naive_error=distance(cq,{s:a/2 for s,a in z.items()})
        assert naive_error==0
        reference={s:-a/2 for s,a in z.items()}
        core=[]
        for S in [2,4,8,16,32,64]:
            error=distance(H4_compensated(v,S),reference)
            core.append({'S':S,'compensated_H4_core_error':error,
                         'C_times_core_error':S*(S+1)*error})
        result.append({'seed':label,'naive_C1_cancels_magnetic_H4_exact_error':naive_error,
                       'gated_H4_limit_action_norm':norm(reference),'finite_spin_core_rows':core})
    # Full first-field action: the original and gated limits differ only by 144 I.
    seed=seeds['initial_four'];z=Zsquare(seed)
    original={s:-a/2 for s,a in z.items()};original[q0,zero]+=144
    comp={s:-a/2 for s,a in z.items()}
    assert distance(original,{s:comp.get(s,0)+144*seed.get(s,0) for s in set(comp)|set(seed)})==0
    assert comp[q0,zero]==-84 and original[q0,zero]==60
    assert all(a==-2 for s,a in comp.items() if s!=(q0,zero))
    return {'seed_controls':result,'initial_compensated_scalar':-84,
            'initial_original_scalar':60,'oriented_face_terms':len(comp)-1,
            'oriented_face_coefficient':-2}

def main():
    out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'finite_complete_physical_identities':finite_identity_controls(),
         'naive_failure_and_gated_core_controls':path_and_core_controls(),
         'actual_two_birth_controls':two_birth_controls(),
         'status':'Author controls for an explicitly modified supplied Hamiltonian; analytic limit and microscopic derivation require their stated proof and independent checks.'}
    print('per_element: Local spin weights and compensating two-hop coefficients were explicitly executed.')
    print('per_site: All four A stars and all cube occupation gates were included in complete physical controls.')
    print('per_mode: checked and not executed — no individual spectral-band preparation is used or claimed.')
    print('per_block: Four-, six-, and eight-record physical blocks and all first/second mark types were checked.')
    print('lattice_wide: The complete finite cube was executed; larger graphs enter only the separate proof.')
    p=D/'LOCAL_COMPENSATION_CONTROLS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
