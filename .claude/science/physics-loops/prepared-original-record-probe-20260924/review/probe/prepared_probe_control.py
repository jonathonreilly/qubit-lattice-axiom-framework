"""Own primitive qutrit/rotor and Gauss enumeration, with exact rational effects.

No prior or author scientific helper is imported. Whole graphs are finite
admissible cubic tori; electric words are sparse integer translations, never
cyclic or finite-spin approximations. Effect values are rate coefficients,
not probabilities for a finite selected jump.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
from fractions import Fraction
import hashlib,json

ROOT=Path(__file__).resolve().parent
checks=[];certificates=[]
def check(name,condition,**details):
    assert condition,(name,details)
    row=dict(name=name,verified=True,**details);checks.append(row)
    print(json.dumps(row,sort_keys=True))
def add(*words):
    out=defaultdict(int)
    for word in words:
        for k,v in word.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def scale(word,c):return {k:c*v for k,v in word.items() if c*v}
def key(word):return tuple(sorted(word.items()))
def serialized(word):return [[int(k),int(v)] for k,v in sorted(word.items())]
def graph(periods):
    verts=list(product(*(range(n) for n in periods)));index={v:i for i,v in enumerate(verts)}
    def pos(v):return tuple(x%n for x,n in zip(v,periods))
    def move(v,axis,s):
        a=list(v);a[axis]+=s;return pos(a)
    edges=[(v,move(v,axis,1)) for v in verts for axis in range(3)]
    edge_index={e:i for i,e in enumerate(edges)}
    A={v for v in verts if sum(v)%2==0}
    neigh={v:sorted({move(v,axis,s) for axis in range(3) for s in (-1,1)}) for v in verts}
    def oriented(x,y):
        if (x,y) in edge_index:return {edge_index[(x,y)]:1}
        return {edge_index[(y,x)]:-1}
    def divergence(word):
        out=defaultdict(int)
        for ei,value in word.items():
            x,y=edges[ei];out[index[x]]+=value;out[index[y]]-=value
        return {x:v for x,v in out.items() if v}
    def gauss(q,word):
        target={i:int(charge)-int(v in A) for i,(v,charge) in enumerate(zip(verts,q))}
        return divergence(word)=={i:x for i,x in target.items() if x}
    return verts,index,pos,edges,A,neigh,oriented,gauss

all_rows=[]
for periods in [(6,6,6),(6,8,10)]:
    verts,idx,pos,edges,A,neigh,e,gauss=graph(periods)
    a=pos((0,0,0));b=pos((-1,0,0));c=pos((1,0,0));d=pos((1,1,0));v=pos((0,1,0))
    r0=pos((0,-1,0));rp=pos((0,0,1));rm=pos((0,0,-1))
    baseline=tuple(int(x in A) for x in verts)
    beta=add(e(a,rp),e(a,rm),scale(e(a,r0),-1))
    loop=add(e(a,c),scale(e(d,c),-1),e(d,v),scale(e(a,v),-1))
    eta_v=add(beta,scale(e(a,v),-1))
    eta_c_star=add(beta,scale(e(a,c),-1))
    eta_c_loop=add(beta,e(d,v),scale(e(a,v),-1),scale(e(d,c),-1))
    check('dressing_difference_'+str(periods),add(eta_c_loop,scale(eta_c_star,-1))==loop,
          periods=periods,loop=serialized(loop),preparation_edges=len(set(eta_v)|set(eta_c_loop)))
    initial=[]
    for occupied in [c,v]:
        q=list(baseline)
        for x,s in [(r0,1),(rp,-1),(rm,-1),(occupied,1)]:q[idx[x]]=s
        initial.append(tuple(q))
    check('physical_charge_words_'+str(periods),initial[0]!=initial[1]
          and all(sum(q)==len(A) and sum(x!=0 for x in q)==len(A)+4 for q in initial)
          and all(q[idx[b]]==0 for q in initial),initial_particle_number=len(A)+4,total_signed_charge=len(A))

    # Full primitive sequence, including the old hop into b that kills j.
    def apply_mark(q,field,sigma):
        out=[];old_hops=[]
        charge=q[idx[a]]
        if charge==0:return out,old_hops
        for destination in neigh[a]:
            if q[idx[destination]]!=0:continue
            qh=list(q);qh[idx[a]]=0;qh[idx[destination]]=charge
            Eh=add(field,scale(e(a,destination),-charge))
            assert gauss(qh,Eh)
            old_hops.append(dict(destination=destination,field=serialized(Eh),birth_legal=qh[idx[b]]==0))
            if qh[idx[a]]!=0 or qh[idx[b]]!=0:continue
            qf=qh.copy();qf[idx[a]]=sigma;qf[idx[b]]=-sigma
            Ef=add(Eh,scale(e(a,b),sigma))
            assert gauss(qf,Ef) and all(qf[idx[x]]!=0 for x in A)
            out.append((tuple(qf),Ef,destination))
        return out,old_hops

    gauss_tests=0
    for m in [-3,0,4]:
        reference=scale(loop,m)
        for dressings in [[eta_c_loop,eta_v],[eta_c_star,eta_v]]:
            for q,eta in zip(initial,dressings):
                field=add(reference,eta);assert gauss(q,field)
                for sigma in [-1,1]:
                    paths,hops=apply_mark(q,field,sigma)
                    assert len(hops)==2 and len(paths)==1
                    gauss_tests+=1
    check('all_primitive_gauss_steps_'+str(periods),gauss_tests==24,initial_and_mark_cases=gauss_tests,
          legal_old_hops_per_branch=2,surviving_mark_paths_per_branch=1)

    for dressing,dressings in [('loop',[eta_c_loop,eta_v]),('star',[eta_c_star,eta_v])]:
        for relative_sign in [-1,1]:
            for channel,signs in [('resolved_plus',[1]),('resolved_minus',[-1]),('coherent',[-1,1])]:
                paths=[]
                for branch,(q,eta,amplitude) in enumerate(zip(initial,dressings,[1,relative_sign])):
                    for sigma in signs:
                        produced,hops=apply_mark(q,eta,sigma)
                        for qf,Ef,destination in produced:
                            assert sum(x!=0 for x in qf)==len(A)+6
                            paths.append(dict(branch=branch,amplitude=amplitude,q=qf,E=Ef,sigma=sigma,destination=destination))
                for dephased in [False,True]:
                    effect=defaultdict(Fraction)
                    for x in paths:
                        for y in paths:
                            if x['q']!=y['q'] or (dephased and x['branch']!=y['branch']):continue
                            effect[key(add(y['E'],scale(x['E'],-1)))]+=Fraction(x['amplitude']*y['amplitude'],2)
                    effect={k:w for k,w in effect.items() if w}
                    mult=len(signs)
                    expected={():Fraction(mult)}
                    if not dephased:
                        if dressing=='loop':
                            expected[key(loop)]=Fraction(relative_sign*mult,2)
                            expected[key(scale(loop,-1))]=Fraction(relative_sign*mult,2)
                        else:expected={():Fraction(mult*(1+relative_sign))} if relative_sign==1 else {}
                    assert effect==expected,(periods,dressing,relative_sign,channel,dephased,effect,expected)
                    result=dict(periods=periods,dressing=dressing,relative_sign=relative_sign,channel=channel,dephased=dephased,
                                effect=[dict(shift=serialized(dict(k)),coefficient=str(w)) for k,w in sorted(effect.items())],
                                path_count=len(paths),final_matter_word_count=len({p['q'] for p in paths}))
                    all_rows.append(result)
                    certificates.append(dict(**result,paths=[dict(branch=p['branch'],amplitude=p['amplitude'],sigma=p['sigma'],destination=p['destination'],
                        occupied_B=[[verts[i],q] for i,q in enumerate(p['q']) if verts[i] not in A and q],
                        A_minus=[verts[i] for i,q in enumerate(p['q']) if verts[i] in A and q==-1],field_shift=serialized(p['E'])) for p in paths]))
    check('all_prepared_laurent_effects_'+str(periods),len([r for r in all_rows if r['periods']==periods])==24,
          rows=[r for r in all_rows if r['periods']==periods])

    # Direct output norms for exact normalizable reference fields, not merely a
    # Laurent expectation. Input coefficients are unnormalized integers;
    # total normalization denominator is 2*sum |c_m|^2.
    direct=[]
    for label,coeffs in [('zero_flux',{0:1}),('even_two_flux',{0:1,1:1}),('odd_two_flux',{0:1,1:-1})]:
        for dephased in [False,True]:
            amplitudes=defaultdict(int)
            for m,field_amp in coeffs.items():
                for branch,(q,eta,branch_amp) in enumerate(zip(initial,[eta_c_loop,eta_v],[1,-1])):
                    paths,_=apply_mark(q,add(eta,scale(loop,m)),1)
                    for qf,Ef,_ in paths:
                        decoherence_label=branch if dephased else None
                        amplitudes[(qf,key(Ef),decoherence_label)]+=field_amp*branch_amp
            denominator=2*sum(x*x for x in coeffs.values())
            value=Fraction(sum(x*x for x in amplitudes.values()),denominator)
            expected=Fraction(1) if dephased else {'zero_flux':Fraction(1),'even_two_flux':Fraction(1,2),'odd_two_flux':Fraction(3,2)}[label]
            assert value==expected
            direct.append(dict(input=label,dephased=dephased,rate_coefficient=str(value)))
    check('direct_physical_output_norms_'+str(periods),len(direct)==6,rows=direct)

check('complete_effect_inventory',len(all_rows)==48 and len(certificates)==48,
      total_effect_rows=len(all_rows),serialized_path_count=sum(len(x['paths']) for x in certificates))
(ROOT/'PATH_CERTIFICATES.json').write_text(json.dumps(certificates,indent=2)+'\n')
result=dict(scope='Own exact local qutrit/rotor path and Gauss checks; no dynamical or photon-absorption simulation.',
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),check_count=len(checks),checks=checks,
            effect_row_count=len(all_rows),path_certificate_sha256=hashlib.sha256((ROOT/'PATH_CERTIFICATES.json').read_bytes()).hexdigest())
(ROOT/'CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL',len(checks),'checks completed')
