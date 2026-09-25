"""Read-only PRE43 evidence check. No scientific source module is imported.

Reads every saved physical word and rechecks its charges, Gauss law, projector,
norm contribution and source/log bindings. An independently written sparse
charge-map enumerator recomputes the two full witness matrix elements, including
opposite-sign inputs, without the main control's bitset representation.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
from fractions import Fraction
from itertools import product
import json

HERE=Path(__file__).resolve().parent

def read(path):return json.loads(path.read_bytes())

def digest(path):return sha256(path.read_bytes()).hexdigest()

def neighbors(x,L):
    out=set()
    for axis in range(3):
        for sign in (-1,1):
            y=list(x);y[axis]=(y[axis]+sign)%L;out.add(tuple(y))
    return sorted(out)

def key(row):
    return (tuple(sorted(tuple(v) for v in row['occupied_B'])),
            tuple(sorted(tuple(v) for v in row['minus_locations'])),
            tuple(sorted((tuple(a),tuple(b),value) for a,b,value in row['electric'])),
            tuple(sorted(tuple(v) for v in row['vacant_A'])))

def check_word(row,L,expect_outside=None):
    B,minus,field,vac=key(row);vertices=list(product(range(L),repeat=3))
    A={v for v in vertices if sum(v)%2==0};occupied=(A-set(vac))|set(B)
    assert set(B).isdisjoint(A) and set(minus)<=occupied and set(vac)<=A
    charge={v:(-1 if v in minus else 1) for v in occupied}
    div=Counter();assert len(field)==len({(a,b) for a,b,v in field})
    for a,b,value in field:
        assert a in A and b in neighbors(a,L) and value!=0 and isinstance(value,int)
        div[a]+=value;div[b]-=value
    assert all(div[v]==charge.get(v,0)-(1 if v in A else 0) for v in vertices)
    assert sum(charge.values())==len(A)
    if expect_outside is not None:
        assert not vac and len(B)==2 and len(minus)==1
        outside=minus[0] in A and not(set(B)&set(neighbors(minus[0],L)))
        assert outside==expect_outside
    return key(row)

def shift(field,a,b,value):
    result=dict(field);result[(a,b)]=result.get((a,b),0)+value
    if not result[(a,b)]:del result[(a,b)]
    return result

def move(charges,field,a,b,out):
    source,target=(a,b) if out else (b,a)
    if source not in charges or target in charges:return None
    q=charges[source];result=dict(charges);del result[source];result[target]=q
    return result,shift(field,a,b,-q if out else q)

def physical_key(charges,field,A):
    return (tuple(sorted(v for v in charges if v not in A)),
            tuple(sorted(v for v,q in charges.items() if q==-1)),
            tuple(sorted((a,b,q) for (a,b),q in field.items())),
            tuple(sorted(A-set(charges))))

def witness_amplitudes(L,target_row):
    A={v for v in product(range(L),repeat=3) if sum(v)%2==0}
    a=(0,0,0);b=(L-1,0,0);target=key(target_row);target_minus=target[1][0]
    results={};accepted=[]
    for sign in (-1,1):
        coefficient=0;recorded=[]
        # To put the sole minus at target_minus, that A star must be a return
        # endpoint. If it began at A a, both a and target_minus must participate.
        if sign==-1:
            pair_candidates=[tuple(sorted((a,target_minus)))]
        else:
            pair_candidates=[tuple(sorted((target_minus,p))) for p in A if p!=target_minus
                             and set(neighbors(target_minus,L))&set(neighbors(p,L))]
        for c in neighbors(a,L):
            if c==b:continue
            charges={v:1 for v in A};charges[a]=sign;charges[b]=-sign;charges[c]=1
            field={(a,b):sign,(a,c):-1}
            for x,y in sorted(set(pair_candidates)):
                if x==y or not(set(neighbors(x,L))&set(neighbors(y,L))):continue
                for u in neighbors(x,L):
                    one=move(charges,field,x,u,True)
                    if one is None:continue
                    for v in neighbors(y,L):
                        two=move(*one,y,v,True)
                        if two is None:continue
                        for w in neighbors(y,L):
                            three=move(*two,y,w,False)
                            if three is None:continue
                            for z in neighbors(x,L):
                                four=move(*three,x,z,False)
                                if four is not None and physical_key(*four,A)==target:
                                    coefficient-=2
                                    recorded.append({'initial_partner':c,'A_pair':[x,y],
                                                     'outward_destinations':[u,v],'return_sources':[w,z]})
        results[sign]=coefficient
        accepted.append({'initial_sign':sign,'matrix_element':coefficient,'complete_matching_paths':recorded})
    return results,accepted

def main():
    pins=read(HERE/'SOURCE_PINS.json')
    for pin in pins['sources']:
        assert digest(HERE/pin['frozen_path'])==pin['sha256']
        if not pin['origin'].startswith('git:'):
            assert digest(Path(pin['origin']))==pin['sha256']
    output=[];all_words=0
    for L in (4,6,8):
        result_path=HERE/f'L{L}_RESULTS.json';result=read(result_path)
        assert result['source_sha256']==digest(HERE/'primitive_transport.py')
        receipt=read(HERE/f'L{L}.execution.json')
        assert receipt['exit_code']==0 and receipt['source_sha256']==result['source_sha256']
        for item in receipt['outputs'].values():
            assert digest(HERE/item['path'])==item['sha256'] and (HERE/item['path']).stat().st_size==item['bytes']
        assert receipt['outputs']['stderr.txt']['bytes']==0
        printed=read(HERE/f'L{L}.stdout.txt')
        for k,v in printed.items():
            if k not in ('resolved','coherent','row_counts'):assert result[k]==v
        n=L**3//2;assert result['A_sites']==n and result['edges']==6*n
        branch_rows=result['birth_branch_rows'];assert len(branch_rows)==10
        initial={-1:{},1:{}}
        for row in branch_rows:
            state=check_word(row['initial'],L,False);initial[row['sign']][state]=1;all_words+=1
            assert len(state[2])==2 and all(abs(v)==1 for a,b,v in state[2])
            # Actual occupied-B electric gate makes every summand vanish.
            assert all(b in state[0] for a,b,v in state[2])
        norms={};leaks={};losses={};summaries=[]
        for row in result['resolved']:
            sign=row['initial_sign'];assert row['input_norm_squared']==5
            leak={};gamma={}
            for physical in row['QH4_rows']:
                state=check_word(physical,L,True);assert state not in leak
                assert physical['coefficient']<0 and physical['coefficient']%2==0
                leak[state]=physical['coefficient'];all_words+=1
            for physical in row['loss_rows']:
                state=check_word(physical,L,False);assert state not in gamma
                assert physical['coefficient']>0 and physical['coefficient']%2==0
                gamma[state]=physical['coefficient'];all_words+=1
            raw_norm=sum(v*v for v in leak.values());norms[sign]=raw_norm;leaks[sign]=leak;losses[sign]=gamma
            assert raw_norm==row['QH4_raw_norm_squared']
            assert str(Fraction(raw_norm,5))==row['normalized_t_squared_delta_squared_coefficient']
            diagonal=sum(gamma.get(state,0) for state in initial[sign])
            assert str(Fraction(diagonal,5))==row['loss_expectation_over_kappa']
            expected_loss=Fraction(60*n)- (Fraction(232 if sign==-1 else 208) if L==4
                                           else Fraction(1164 if sign==-1 else 1044,5))
            assert Fraction(row['loss_expectation_over_kappa'])==expected_loss
            dephased=sum(r['individual_QH4_norm_squared'] for r in branch_rows if r['sign']==sign)
            assert Fraction(row['dephased_initial_branch_coefficient'])==Fraction(dephased,5)
            summaries.append({k:v for k,v in row.items() if k not in ('QH4_rows','loss_rows')})
        combined=Counter(leaks[-1]);combined.update(leaks[1])
        recorded={}
        for physical in result['coherent']['QH4_rows']:
            state=check_word(physical,L,True);assert state not in recorded
            recorded[state]=physical['coefficient'];all_words+=1
        assert dict(combined)==recorded
        cross=sum(v*leaks[1].get(state,0) for state,v in leaks[-1].items())
        raw_norm=sum(v*v for v in combined.values())
        assert cross==result['coherent']['cross_sign_QH4_inner_product']==0
        assert raw_norm==result['coherent']['QH4_raw_norm_squared']==norms[-1]+norms[1]
        assert result['coherent']['normalized_t_squared_delta_squared_coefficient']==str(Fraction(raw_norm,10))
        assert Fraction(result['coherent']['loss_expectation_over_kappa'])==sum(Fraction(row['loss_expectation_over_kappa']) for row in summaries)/2
        checked_witnesses=[]
        for witness in result['witnesses']:
            check_word(witness['initial'],L,False);all_words+=1
            for step in witness['steps']:check_word(step['state'],L);all_words+=1
            target=check_word(witness['final'],L,True);all_words+=1
            coefficients,paths=witness_amplitudes(L,witness['final'])
            sign=witness['initial_sign']
            assert coefficients[sign]==witness['H4_raw_birth_amplitude']==leaks[sign][target]
            assert coefficients[-sign]==witness['other_sign_amplitude']==0
            assert coefficients[sign]==(-4 if sign==-1 else -2)
            assert len(paths[0 if sign==-1 else 1]['complete_matching_paths'])==(2 if sign==-1 else 1)
            assert witness['minus_to_positive_B_distances']==[3,3]
            checked_witnesses.append({'witness_sign':sign,'final':witness['final'],'full_primitive_matrix_elements':paths})
        check_word(result['reassignment_inside_union'],L,False);all_words+=1
        assert result['explicit_resolved_and_coherent_instrument_loss_checked']==(L in (4,6))
        expected_printed_resolved=[{k:v for k,v in row.items() if k not in ('QH4_rows','loss_rows')} for row in result['resolved']]
        assert printed['resolved']==expected_printed_resolved
        assert printed['coherent']=={k:v for k,v in result['coherent'].items() if k!='QH4_rows'}
        assert printed['row_counts']=={'resolved_QH4':[len(row['QH4_rows']) for row in result['resolved']],
                                      'resolved_loss':[len(row['loss_rows']) for row in result['resolved']],
                                      'coherent_QH4':len(result['coherent']['QH4_rows'])}
        output.append({'side':L,'result_sha256':digest(result_path),
            'resolved':summaries,'coherent':printed['coherent'],'row_counts':printed['row_counts'],
            'independent_sparse_charge_witness_reconstructions':checked_witnesses,
            'source_and_stdout_bindings_match':True,'external_elapsed_seconds':receipt['elapsed_seconds']})
    print(json.dumps({'scope':__doc__,'source_sha256':digest(Path(__file__)),
                      'all_physical_rows_checked':all_words,'volumes':output,
                      'no_author_or_PRE40_scientific_program_imported':True},indent=2))

if __name__=='__main__':main()
