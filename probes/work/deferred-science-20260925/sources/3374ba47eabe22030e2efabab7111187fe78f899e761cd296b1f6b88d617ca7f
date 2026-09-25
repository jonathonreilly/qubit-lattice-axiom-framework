#!/usr/bin/env python3
"""Exact Laurent certificates for the conditional sharp rotor cube energy tail.

Modular elimination proposes rational coefficients. Every reported identity is
then verified over rational Laurent polynomials; no modular rank is a theorem.
The written note supplies the infinite-time analytic argument. This runner has
no execution-time scientific file reads; source notes are declared for binding.
"""
AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    'docs/SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md',
)
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import hashlib,itertools,json,math,time
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'outputs/sharp_rotor_cube_energy_tail_20260924'
P=(1<<521)-1
A=(0,3,5,6); B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
CHORDS=(0,5,7,8,10)

def primitive_Q():
    words=[]
    for occupied in itertools.combinations(range(8),6):
        for negative in occupied:
            words.append(tuple((-1 if i==negative else 1) if i in occupied else 0 for i in range(8)))
    middle=[q for q in words if sum(not q[a] for a in A)==1]
    dark=[q for q in middle if not any(q[a]==q[b]==0 for a,b in EDGES)]
    bright=[q for q in middle if q not in dark]
    assert (len(middle),len(dark),len(bright))==(96,24,72)
    def hop(q,inward):
        for e,(a,b) in enumerate(EDGES):
            source,target=(b,a) if inward else (a,b)
            if not q[source] or q[target]:continue
            charge=q[source];qq=list(q);qq[target]=charge;qq[source]=0
            exponent=[0]*5
            if e in CHORDS:exponent[CHORDS.index(e)]=(1 if inward else -1)*charge
            yield tuple(qq),tuple(exponent)
    terms=defaultdict(int)
    for column,q in enumerate(dark):
        for inward,sign in ((True,1),(False,-1)):
            for q1,e1 in hop(q,inward):
                for q2,e2 in hop(q1,not inward):
                    terms[(q2,column,tuple(a+b for a,b in zip(e1,e2)))]+=sign
    terms={key:c for key,c in terms.items() if c}
    assert all(q in bright for q,column,e in terms), 'The entire dark-dark Laurent block must cancel.'
    rows=[defaultdict(dict) for _ in bright]
    for (q,column,e),c in terms.items():rows[bright.index(q)][column][e]=c
    return {'rows':[[{'column':column,'terms':[{'exponent':e,'coefficient':c} for e,c in cell.items()]} for column,cell in row.items()] for row in rows],
            'edges':EDGES,'chords':CHORDS,'dark_charge_words':dark,'bright_charge_words':bright}

def sign_phase_ranks(data):
    answer=[]
    for bits in itertools.product((0,1),repeat=5):
        Q=sp.zeros(72,24)
        for i,row in enumerate(data['rows']):
            for cell in row:
                for term in cell['terms']:
                    Q[i,cell['column']]+=term['coefficient']*(-1 if sum(a*b for a,b in zip(bits,term['exponent']))%2 else 1)
        answer.append({'pi_bits':bits,'exact_rank':Q.rank()})
    expected={(0,0,0,0,0):23,(0,0,0,1,1):23,(0,1,1,0,1):22,(0,1,1,1,0):23,
              (1,0,1,0,0):23,(1,0,1,1,1):22,(1,1,0,0,1):20,(1,1,0,1,0):22}
    assert {row['pi_bits']:row['exact_rank'] for row in answer if row['exact_rank']<24}==expected
    assert all(row['exact_rank']==24 or row['pi_bits'] in expected for row in answer)
    return answer

def exact_certificates(data):
    degree=3
    shifts=sorted((e for e in itertools.product(range(-degree,degree+1),repeat=5) if sum(map(abs,e))<=degree),key=lambda e:(sum(map(abs,e)),e))
    rows=[];all_keys=set()
    for shift in shifts:
        for row in data['rows']:
            poly={}
            for cell in row:
                for term in cell['terms']:
                    key=(cell['column'],tuple(a+b for a,b in zip(shift,term['exponent'])))
                    poly[key]=poly.get(key,0)+term['coefficient']
            poly={key:c for key,c in poly.items() if c}
            all_keys.update(poly);rows.append(poly)
    targets=[]
    for j in range(5):
        e=tuple(int(k==j) for k in range(5));minus=tuple(-x for x in e)
        for col in range(24):
            t={(col,e):1,(col,minus):-1};targets.append((j,col,t));all_keys.update(t)
    ordered=sorted(all_keys,key=lambda key:(sum(map(abs,key[1])),key[1],key[0]))
    indices={key:i for i,key in enumerate(ordered)}
    basis={};dag={};start=time.monotonic()
    def reduce(poly):
        operations=[]
        while poly:
            pivot=max(poly)
            if pivot not in basis:return poly,operations
            coeff=poly[pivot];operations.append((pivot,coeff))
            for k,v in basis[pivot].items():
                value=(poly.get(k,0)-coeff*v)%P
                if value:poly[k]=value
                elif k in poly:del poly[k]
        return poly,operations
    for n,row in enumerate(rows):
        poly,operations=reduce({indices[key]:c%P for key,c in row.items()})
        if poly:
            pivot=max(poly);inverse=pow(poly[pivot],P-2,P)
            basis[pivot]={k:(c*inverse)%P for k,c in poly.items()}
            assert all(parent>pivot for parent,c in operations)
            dag[pivot]=(n,inverse,operations)
        if n%2000==0:print(json.dumps({'rows_processed':n,'rank':len(basis),'elapsed':time.monotonic()-start}),flush=True)
    keys=sorted(basis)
    def rational_reconstruct(value):
        bound=math.isqrt(P//2);a,b=P,value;s0,s1=0,1
        while abs(b)>bound:
            q=a//b;a,b=b,a-q*b;s0,s1=s1,s0-q*s1
        assert s1 and abs(s1)<=bound and math.gcd(b,s1)==1 and (b-value*s1)%P==0, (value,b,s1)
        return Fraction(b,s1)
    selected=targets
    certificates=[]
    for phase,col,target in selected:
        rem,operations=reduce({indices[k]:v%P for k,v in target.items()})
        assert not rem,(phase,col,len(rem))
        pending={};original={}
        for pivot,c in operations:pending[pivot]=(pending.get(pivot,0)+c)%P
        for pivot in keys:
            value=pending.pop(pivot,0)
            if not value:continue
            n,inverse,ops=dag[pivot];w=value*inverse%P
            original[n]=(original.get(n,0)+w)%P
            for parent,c in ops:pending[parent]=(pending.get(parent,0)-w*c)%P
        assert not any(pending.values())
        coefficients={n:rational_reconstruct(c) for n,c in original.items() if c}
        exact={}
        for n,c in coefficients.items():
            for key,v in rows[n].items():exact[key]=exact.get(key,Fraction(0))+c*v
        exact={k:c for k,c in exact.items() if c}
        assert exact==target, (phase,col,'exact identity failed')
        certificate={'phase':phase,'column':col,'row_combination':[[n,c.numerator,c.denominator] for n,c in sorted(coefficients.items())],'exact_identity_verified':True,'maximum_numerator':max(abs(c.numerator) for c in coefficients.values()),'maximum_denominator':max(c.denominator for c in coefficients.values())}
        certificates.append(certificate)
        if col==23: print(json.dumps({'phase':phase,'verified_columns':24,'elapsed_seconds':time.monotonic()-start}),flush=True)
    return certificates,shifts,time.monotonic()-start

def certificate_mutation_control(data,certificates,shifts):
    # Reconstruct one relation using a separate direct monomial accumulator.
    first=certificates[0]
    def residual(combination):
        result=defaultdict(Fraction)
        for n,numerator,denominator in combination:
            shift=shifts[n//72];row=data['rows'][n%72]
            for cell in row:
                for term in cell['terms']:
                    exponent=tuple(a+b for a,b in zip(shift,term['exponent']))
                    result[(cell['column'],exponent)]+=Fraction(numerator,denominator)*term['coefficient']
        unit=tuple(int(k==first['phase']) for k in range(5))
        result[(first['column'],unit)]-=1
        result[(first['column'],tuple(-x for x in unit))]+=1
        return {key:c for key,c in result.items() if c}
    assert not residual(first['row_combination'])
    changed=[list(row) for row in first['row_combination']]
    changed[0][1]+=changed[0][2]
    remainder=residual(changed)
    assert remainder, 'An altered rational coefficient must be rejected.'
    return {'changed_coefficient_remainder_terms':len(remainder),'mutation_rejected':True}

def energy_sign_control():
    # Exact scalar Q=1, B=0, delta=kappa=1 exercises the cross-term sign.
    alpha=sp.Rational(1,6);I=sp.I
    generator=sp.Matrix([[0,-I],[-I,-1]])
    cross=sp.Matrix([[0,I/2],[-I/2,0]])
    correct=sp.eye(2)-alpha*cross;wrong=sp.eye(2)+alpha*cross
    derivative=generator.conjugate().T*correct+correct*generator
    bad=generator.conjugate().T*wrong+wrong*generator
    assert derivative[0,0]==-alpha and bad[0,0]==alpha
    claimed=derivative+sp.diag(alpha/2,1)
    assert claimed[0,0]<0 and claimed.det()>0 and claimed==claimed.conjugate().T
    return {'correct_dark_derivative':str(derivative[0,0]),'wrong_sign_dark_derivative':str(bad[0,0]),'claimed_bound_determinant':str(claimed.det()),'mutation_rejected':True}

def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    started=time.monotonic();data=primitive_Q()
    certificates,shifts,elapsed=exact_certificates(data)
    assert len(certificates)==120
    assert {(c['phase'],c['column']) for c in certificates}==set(itertools.product(range(5),range(24)))
    assert all(c['exact_identity_verified'] for c in certificates)
    ranks=sign_phase_ranks(data)
    ceilings=[math.ceil(sum((abs(Fraction(a,b)) for n,a,b in c['row_combination']),Fraction(0))) for c in certificates]
    L=max(ceilings)
    assert L<=68891, 'The explicit Laurent coefficient bound in the note must hold.'
    full={'primitive_Q':data,'shifts':shifts,'certificates':certificates,'row_order':'shift major, then primitive row 0..71','identity':'sum_n c_n z^shift(n) Q[row(n),:] = (z_phase-z_phase^-1) e_column^T'}
    raw=json.dumps(full,separators=(',',':'))+'\n'
    (OUTPUT/'RATIONAL_LAURENT_CERTIFICATES.json').write_text(raw)
    result={'primitive_dimensions':{'bright':72,'dark':24,'cycle':5},'multiplier_l1_degree':3,'identity_count':120,'exact_coefficient_checks':True,
            'maximum_row_coefficient_L1_ceiling':L,'sum_matrix_sup_norm_squared_bound':120*L*L,
            'sign_phase_exact_ranks':ranks,'certificate_sha256':hashlib.sha256(raw.encode()).hexdigest(),'certificate_bytes':len(raw.encode()),
            'coefficient_mutation':certificate_mutation_control(data,certificates,shifts),'energy_sign_control':energy_sign_control(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-started,
            'scope':'Exact finite Laurent identities and ranks; the written proof supplies the rotor infinite-time bounds. No finite-spin growing-time theorem, asymptotic constant, reservoir, or physical law is inferred.'}
    (OUTPUT/'SHARP_TAIL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    print('TOTAL: PASS=4 FAIL=0',flush=True)

if __name__=='__main__':main()
