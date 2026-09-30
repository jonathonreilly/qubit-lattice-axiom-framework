#!/usr/bin/env python3
"""Independent small source-word, cutoff, and integer-bound controls.

No author code imported; the graded one-rotor fixture is not the source model.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time,hashlib,resource
HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
AUTHOR=HERE.parent/'rotor-process-energy-bridge'
def budget():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()

def original_birth_words():
    count=0
    for qa in (-1,1):
        for qb in product((-1,0,1),repeat=6):
            before=sum(v!=0 for v in qb)
            for birth_edge in range(6):
                if qb[birth_edge]!=0:continue
                for dest in range(6):
                    if dest==birth_edge or qb[dest]!=0:continue
                    for sigma in (-1,1):
                        new=list(qb);new[dest]=qa;new[birth_edge]=-sigma
                        field=[0]*6;field[dest]=-qa;field[birth_edge]=sigma
                        assert sum(field)==sigma-qa
                        for j in range(6):assert -field[j]==new[j]-qb[j]
                        assert sum(x!=0 for x in new)==before+2
                        assert sum(abs(x) for x in field)==2
                        count+=1
    assert count==2*2*6*5*3**4==9720
    degrees=[(6-o)*(o+1) for o in range(6)]
    assert max(degrees)==12
    # The stronger resolved-mark incidence bound is not needed in the report.
    resolved=[(5-o)*(o+1) for o in range(5)]
    assert max(resolved)==9
    assert 2*12**2==288 and 288*9==2592
    assert 12*25==6*50==300
    return {'legal_B_words':count,'Gauss_increment_and_grade_checked':True,
            'F_squared_degree_bound':max(degrees),'resolved_squared_degree_bound':max(resolved),
            'pair_norm_bound':288,'global_A_coefficient':2592,'conservative_jump_sum_coefficient':300}

def ga(a,b):return (a[0]+b[0],a[1]+b[1])
def gm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,b):return (a[0]*b,a[1]*b)
def add(d,key,v):
    q=ga(d.get(key,(0,0)),v)
    if q!=(0,0):d[key]=q
    else:d.pop(key,None)
ROOT=[(1,0),(0,-1),(-1,0),(0,1)]

def toy_apply(state,word,R=None):
    # Grade g=0,1,2; jump +/- takes (g,e) to (g+1,e+/-2).
    # Magnetic A shifts e by +/-4 and preserves grade; D=e^2/4+g.
    d={}
    for (g,e),v in state.items():
        if word=='G':
            for shift in (-4,4):
                if R is None or abs(e+shift)<=R:add(d,(g,e+shift),gm(v,(0,-(2*g+1))))
            gamma=0 if g==2 else sum((g+1)**2 for shift in (-2,2) if R is None or abs(e+shift)<=R)
            add(d,(g,e),scale(v,F(-gamma,2)))
        elif g<2:
            target=e+(2 if word=='+' else -2)
            if R is None or abs(target)<=R:add(d,(g+1,target),scale(v,g+1))
    return d

def toy_word(word,R=None):
    d={(0,0):(F(1),F(0))}
    for n,letter in enumerate(word):
        # Nontrivial exact electric interaction-picture phases; even e stays even.
        d={key:gm(v,ROOT[((key[1]**2//4+key[0])*(n+1))%4]) for key,v in d.items()}
        d=toy_apply(d,letter,R)
    return d

def cutoff_fixture():
    cases=0;nonreal=0
    for length in range(7):
        for word in product('G+-',repeat=length):
            n=word.count('G');j=length-n
            if n>3 or j>2:continue
            radius=4*n+2*j
            full=toy_word(word);cut=toy_word(word,radius)
            assert full==cut,(word,radius,full,cut)
            assert all(g==j and abs(e)<=radius for g,e in full)
            cases+=1;nonreal+=any(v[1] for v in full.values())
    assert toy_word('+++')=={}
    # At R=1, both jumps from the origin leave the box. The actual cutoff
    # loss is zero; compressed original Gamma would remain two.
    assert toy_apply({(0,0):(1,0)},'G',1)=={}
    actual_cutoff_loss=0;compressed_old_loss=2
    assert compressed_old_loss-actual_cutoff_loss>0
    # Entire graded toy history normalization from a separate forward ODE:
    # coefficients in the basis (1,exp(-2t),exp(-8t)).
    p=[(F(0),F(1),F(0)),(F(0),F(1,3),F(-1,3)),(F(1),F(-4,3),F(1,3))]
    derivative=lambda x:tuple(-r*c for r,c in zip((0,2,8),x))
    linear=lambda a,x,b,y:tuple(a*u+b*v for u,v in zip(x,y))
    assert derivative(p[0])==tuple(-2*x for x in p[0])
    assert derivative(p[1])==linear(2,p[0],-8,p[1])
    assert derivative(p[2])==tuple(8*x for x in p[1])
    assert tuple(sum(row[i] for row in p) for i in range(3))==(1,0,0)
    assert [sum(row) for row in p]==[1,0,0]
    return {'safe_phase_word_comparisons':cases,'nonreal_final_word_vectors':nonreal,
            'third_jump_zero':True,'actual_R1_loss':actual_cutoff_loss,
            'incorrect_compressed_loss':compressed_old_loss,'graded_history_ODE_normalization':True,
            'fixture_is_original_source_model':False}

def cbrt_up(n):
    low=0;high=1<<((n.bit_length()+2)//3)
    while low+1<high:
        mid=(low+high)//2
        if mid**3>=n:high=mid
        else:low=mid
    return high

def bound_controls():
    assert (2*2+1)*(1+2)**2==45
    assert (2*4+1)*(1+4)**2==225
    assert 2*45+1+225==316
    assert F(4,3)*F(22,7)**2*F(3,2)<20
    assert F(1,4)+F(11,56)+F(1,4)+F(1,28)==F(41,56)<1
    # Independent integer evaluation of the proposed large example; no huge
    # exponentials or enormous Hilbert-space dimensions are instantiated.
    L=24;N=L**3//2;M=N//2;v=2592*N;g=300*N
    X=v+g//2;Y=g;b=1+2*M;k=336531472;r=k-1;R=2*M+4*r+8
    assert k>=6*X
    EX=Y+2*X;EY=1+Y-k
    PX=(b+4*X)**2+16*X;PY=(b+4*k)**2
    SH=2*PX+v;SP=g*(316*PX+2*v)
    EH=4*PY+3*v;EP=4*g*(316*PY+2*v)
    errors={'process':(4,EY),'energy1':(4*SH,EX+EY),
            'energy2':(2*SH*EH,EX+EY),'current1':(2*SP+EP,EX+EY),
            'current2':(2*SP*EP,EX+EY)}
    exponents={key:c.bit_length()+e for key,(c,e) in errors.items()}
    assert all(vv<=-100 for vv in exponents.values())
    assert R==1346132804 and M==3456 and v==17915904 and g==2073600 and X==18952704
    hbar=2*R*R+2*v;pbar=g*(316*(1+R)**2+2*v)
    q=3;nu_den=1000*(1+hbar*hbar+pbar*pbar)
    cmark=7*g*g+4*hbar*g
    n=max(8,2*g,(704*q)**6*g**3*nu_den**6,4*cmark*nu_den,64*q*nu_den)
    n=((n+2)//3)*3 # observations at T/3,2T/3,T
    w=cbrt_up(n);assert (w-1)**3<n<=w**3
    clock_dimension=n+w+32*n+1
    system_qubits=3*N+6*N*(2*R).bit_length()
    assert system_qubits==1347840
    assert len(str(n))==382 and len(str(clock_dimension))==384
    return {'relative_range_factors':[45,225],'current_K_constant':316,
            'resource_example':{'M':M,'v':v,'g':g,'x':X,'k':k,'R':R,
                                'error_log2_strict_upper_bounds':exponents,
                                'system_qubit_encoding_bound':system_qubits,
                                'collision_count_decimal_digits':len(str(n)),
                                'clock_dimension_decimal_digits':len(str(clock_dimension)),
                                'n_rounded_to_multiple_of':3},
            'apparatus_error_fraction_upper_bound':'41/56 of requested nu0'}

def main():
    budget();start=time.time()
    sha=hashlib.sha256((AUTHOR/'REPORT.md').read_bytes()).hexdigest()
    assert sha=='f8d902e18bc95ed146cda93cc0c83c81b6fa13f57379514e871b0ee90d14e28c'
    out={'frozen_author_report_sha256':sha,'original_words':original_birth_words(),
         'cutoff_fixture':cutoff_fixture(),'bounds':bound_controls()}
    budget();out['elapsed_seconds']=time.time()-start
    out['maxrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
