"""Independently enumerate complete small physical sectors and their operators."""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
from hashlib import sha256
import json
import numpy as np
import sympy as s
from scipy import sparse as sp
from scipy.sparse.linalg import expm_multiply

HERE=Path(__file__).resolve().parent


def build(vertices, edges, apart, reference):
    states=[]; charges=[]
    for word in range(1<<len(edges)):
        q=[int(x in apart) for x in range(vertices)]
        for e,(x,y) in enumerate(edges):
            change=((word>>e)&1)-((reference>>e)&1)
            q[x]+=change; q[y]-=change
        if all(z in (-1,0,1) for z in q): states.append(word); charges.append(q)
    index={word:i for i,word in enumerate(states)}; size=len(states)
    hop=[]; births=[]; vacant=[]
    for e,(x,y) in enumerate(edges):
        a=s.zeros(size); vv={q:s.zeros(size) for q in (-1,1)}
        for i,word in enumerate(states):
            target=word^(1<<e)
            if target not in index: continue
            j=index[target]; old,new=charges[i],charges[j]
            if (old[x]==0)!=(old[y]==0) and new[x]==old[y] and new[y]==old[x]: a[j,i]=1
            if old[x]==old[y]==0 and new[x]==-new[y] and abs(new[x])==1: vv[new[x]][j,i]=1
        assert a==a.T
        hop.append(a); births.append(vv)
        vacant.append(s.diag(*[int(q[x]==q[y]==0) for q in charges]))
    occ=np.array([[int(q!=0) for q in qs] for qs in charges],dtype=int)
    minus=np.array([[int(q==-1) for q in qs] for qs in charges],dtype=int)
    b=[int(sum(row[x] for x in range(vertices) if x not in apart)) for row in occ]
    na=[int(sum(row[x] for x in apart)) for row in minus]
    nb=[int(sum(row[x] for x in range(vertices) if x not in apart)) for row in minus]
    holes_a=[int(len(apart)-sum(row[x] for x in apart)) for row in occ]
    field=[s.Rational(1,2)*sum((q[x]-int(x in apart))**2 for x in range(vertices)) for q in charges]
    for i,q in enumerate(charges):
        assert sum(q)==len(apart)
        assert b[i]==holes_a[i]+2*(na[i]+nb[i])
        assert field[i]==b[i]+na[i]-nb[i]
        assert s.Rational(b[i],2)<=field[i]<=s.Rational(3*b[i],2)
    return dict(vertices=vertices,edges=edges,apart=apart,reference=reference,states=states,charges=charges,
                hop=hop,births=births,vacant=vacant,b=b,field=field,occ=occ,minus=minus)


def dual(j, o):
    loss=j.T*j
    return j.T*o*j-(loss*o+o*loss)/2


def exact_controls(model):
    n=len(model['states']); zero=s.zeros(n); eye=s.eye(n)
    hop=sum(model['hop'],zero); pot=s.diag(*model['b']); fld=s.diag(*model['field'])
    total=s.diag(*map(int,model['occ'].sum(axis=1)))
    minus=s.diag(*map(int,model['minus'].sum(axis=1)))
    assert hop*total==total*hop and hop*minus==minus*hop
    channels={mode:[] for mode in ('coherent_plus','coherent_minus','resolved')}
    energy_changes=set()
    for e,v in enumerate(model['births']):
        plus,negative=v[1],v[-1]
        assert plus.T*negative==zero and plus*negative.T==zero
        for mode,jumps in [('coherent_plus',[plus+negative]),('coherent_minus',[plus-negative]),('resolved',[plus,negative])]:
            assert sum((j.T*j for j in jumps),zero)==model['vacant'][e]
            channels[mode].extend(jumps)
            assert sum((dual(j,total) for j in jumps),zero)==2*model['vacant'][e]
            assert sum((dual(j,pot) for j in jumps),zero)==model['vacant'][e]
            assert sum((dual(j,minus) for j in jumps),zero)==model['vacant'][e]
            for f,af in enumerate(model['hop']):
                shared=set(model['edges'][e])&set(model['edges'][f])
                answer=zero
                if len(shared)==1:
                    third=next(iter(set(model['edges'][e])-shared))
                    qz=s.diag(*[int(q[third]==0) for q in model['charges']])
                    answer=-qz*af/2
                assert sum((dual(j,af) for j in jumps),zero)==answer
        for vv in v.values():
            for out,inn in zip(*np.nonzero(np.array(vv,dtype=int))):
                change=model['field'][out]-model['field'][inn]
                assert change in (0,2)
                energy_changes.add(int(change))
    plus_ids=[i for i,q in enumerate(model['charges']) if all(x>=0 for x in q)]
    low=[i for i in plus_ids if model['b'][i]==0]
    aa=hop.extract(plus_ids,plus_ids); dd=[model['b'][i] for i in plus_ids]
    r=s.diag(*[s.Rational(1,x) if x else 0 for x in dd]); lo=[plus_ids.index(i) for i in low]
    b2=(aa*r*aa).extract(lo,lo); a2=(aa*r*r*aa).extract(lo,lo)
    c4=(aa*r*aa*r*aa*r*aa).extract(lo,lo)
    h2=-b2; h4=-c4+(a2*b2+b2*a2)/2
    assert fld.extract(plus_ids,plus_ids)==pot.extract(plus_ids,plus_ids)
    return {'physical_dimension':n,'plus_only_dimension':len(plus_ids),'low_dimension':len(low),
            'states':model['states'],'charges':model['charges'],
            'low_states':[model['states'][i] for i in low],
            'second_order_coefficient':[[str(x) for x in row] for row in h2.tolist()],
            'fourth_order_coefficient':[[str(x) for x in row] for row in h4.tolist()],
            'unfolded_fourth_excursion':[[str(-x) for x in row] for row in c4.tolist()],
            'folded_fourth_term':[[str(x) for x in row] for row in ((a2*b2+b2*a2)/2).tolist()],
            'field_potential_birth_changes_in_units_Delta':sorted(energy_changes),
            'exact_controls':'charge/count/potential identities, coherent and resolved loss, all dissipative hopping identities, and complete fourth-order physical-sector matrices'},channels


def dynamics(model,channels):
    dim=len(model['states']); vertices=model['vertices']; d=1
    delta=64.0; coupling=2.25; beta=0.3
    a=np.array(sum(model['hop'],s.zeros(dim)),dtype=float)
    initial=np.zeros(dim,dtype=complex)
    initial[model['states'].index(0)]=1/np.sqrt(2)
    initial[model['states'].index((1<<len(model['edges']))-1)]=1/np.sqrt(2)
    rho=np.outer(initial,initial.conj()); identity=sp.eye(dim,format='csr')
    times=[0.0,0.2,0.5,1.0]; rows=[]; endpoints={}
    for potential,values,alpha,kappab in [('sublattice',model['b'],1.0,1),('field_squared',model['field'],0.5,2)]:
        ham=sp.csr_matrix(delta*np.diag(np.array(values,dtype=float))-coupling*a)
        for mode,operators in channels.items():
            gen=-1j*(sp.kron(identity,ham)-sp.kron(ham.T,identity))
            for op in operators:
                j=sp.csr_matrix(np.array(op,dtype=float))*np.sqrt(beta); loss=j.T@j
                gen+=sp.kron(j.conjugate(),j)-(sp.kron(identity,loss)+sp.kron(loss.T,identity))/2
            for time in times:
                rr=expm_multiply(time*gen,rho.reshape(-1,order='F')).reshape((dim,dim),order='F')
                tr=float(np.trace(rr).real); mineig=float(np.linalg.eigvalsh(rr).min())
                assert abs(tr-1)<1e-10 and np.max(abs(rr-rr.conj().T))<1e-10 and mineig>-1e-10
                pop=float(np.dot(np.diag(rr).real,model['occ'].sum(axis=1))/vertices)
                bmean=float(np.dot(np.diag(rr).real,model['b'])/vertices)
                holes=float(np.dot(np.diag(rr).real,[sum(q[x]==0 for x in model['apart']) for q in model['charges']])/vertices)
                c2=8*d*d; lam=coupling/delta; rate=(4*kappab*d/alpha+2*d-1)*beta; c_b=(2*d-1)*beta
                bound=c2*lam*lam/(alpha*alpha)*(np.exp(rate*time)+c_b/rate*np.expm1(rate*time))
                assert -1e-10<=pop-0.5<=bmean+1e-10 and bmean<=bound+1e-10
                rows.append({'potential':potential,'instrument':mode,'time':time,'record_density':pop,'B_occupation_density':bmean,'A_vacancy_density':holes,'proved_bound_B_density':float(bound),'trace':tr,'minimum_eigenvalue':mineig})
                if time==times[-1]: endpoints[potential+'_'+mode]=rr
    np.savez_compressed(HERE/'FINITE_DENSITIES.npz',**endpoints)
    differences={pot:float(np.linalg.norm(endpoints[pot+'_coherent_plus']-endpoints[pot+'_resolved'])) for pot in ['sublattice','field_squared']}
    return {'geometry':'complete six-cycle physical sector; mean-density control, not a cubic plaquette-dynamics test',
            'Delta':delta,'t':coupling,'beta':beta,'initial':'equal coherent cat of two ice words','rows':rows,
            'coherent_plus_vs_resolved_final_HS_difference':differences}


def main():
    cases={}
    for length in [4,6]:
        m=build(length,[(i,(i+1)%length) for i in range(length)],set(range(0,length,2)),0)
        result,channels=exact_controls(m);cases['cycle_'+str(length)]=result
        if length==4:
            assert result['second_order_coefficient']==[['-2','0'],['0','-2']]
            assert result['fourth_order_coefficient']==[['2','-2'],['-2','2']]
        if length==6:
            assert result['second_order_coefficient']==[['-3','0'],['0','-3']]
            assert result['fourth_order_coefficient']==[['3','0'],['0','3']]
            dyn=dynamics(m,channels)
    star=build(5,[(0,j) for j in range(1,5)],{0},3)
    result,_=exact_controls(star); cases['four_leaf_star_with_frozen_external_ice_flow']=result
    assert result['second_order_coefficient']==[['-2']]
    assert result['fourth_order_coefficient']==[['4']]
    assert result['field_potential_birth_changes_in_units_Delta']==[0,2]
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
         'cases':cases,'dynamics':dyn,'limits':'Complete finite physical sectors. Four-cycle and star are local controls with fixed exterior flows and selected active internal hopping edges, not replacements for the prescribed large torus. Six-cycle obeys the d=1 period>=6 condition. No extrapolation of numerical values.'}
    txt=json.dumps(out,indent=2)+'\n';(HERE/'FINITE_SECTOR_RESULTS.json').write_text(txt);print(txt,end='')


if __name__=='__main__': main()
