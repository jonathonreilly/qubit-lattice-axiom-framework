#!/usr/bin/env python3
"""Post-seal comparison; author code is read separately, never imported."""
import sys
sys.dont_write_bytecode=True
import argparse
import hashlib
import itertools as it
import json
from pathlib import Path
import sympy as s
import independent_check as independent

HERE=Path(__file__).resolve().parent;RAW=HERE.parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def authenticate():
    seal=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in seal['artifacts']+seal['dependencies']+seal['procedures']:
        p=Path(row['path']);assert p.stat().st_size==row['bytes'] and digest(p)==row['sha256']
    result=json.loads((RAW/'geometric_last_pair_clock_checks/RESULTS.json').read_text())
    for name,sha in result['sources_sha256'].items():assert digest(RAW/name)==sha
    assert result['sources_sha256']['geometric_last_pair_clock_check.py']=='60eae29b78c46d04fff388d7d4eba6b918fabe0669625c8a61239ef541c21e38'
    assert result['sources_sha256']['GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md']=='0f5c6bdb5ce0c2ac3e7aa32bef5dfe57e1de0f914c81af984e4195d92722ebd7'
    decoder=json.JSONDecoder();text=(RAW/'GEOMETRIC_LAST_PAIR_CLOCK_RUN.log').read_text();objects=[]
    while text.strip():
        obj,end=decoder.raw_decode(text.lstrip());objects.append(obj);text=text.lstrip()[end:]
    assert objects[:-1]==result['rows']
    assert objects[-1]=={'groups':len(result['rows']),'sources_sha256':result['sources_sha256']}
    assert all(row['pass'] for row in result['rows']) and (RAW/'GEOMETRIC_LAST_PAIR_CLOCK_RUN.stderr').read_bytes()==b''
    return result,{'preseal_artifacts_unchanged':len(seal['artifacts']),'author_groups':len(result['rows']),
                   'four_source_bindings_match':len(result['sources_sha256'])==4,'recorded_log_matches_results':True,
                   'stderr_empty':True,'author_runner_imported_or_executed':False}

def generic_author_fixture(result):
    beta,z=s.symbols('beta z',positive=True);S=s.zeros(3)
    for i,j,rate in ((0,1,1),(1,2,2)):
        S[i,j]+=rate;S[j,i]+=rate;S[i,i]-=rate;S[j,j]-=rate
    A=s.Matrix([[1,0],[0,0],[0,1]]);h=A*s.ones(2,1)
    U=(-S+beta*(s.diag(*h)+z*s.eye(3))).inv(method='DM')*beta*A
    total=U*s.ones(2,1)
    first=[s.factor(-x.diff(z).subs(z,0)) for x in total]
    second=[s.factor(x.diff(z,2).subs(z,0)) for x in total]
    row=result['rows'][0]
    assert all(s.limit(x,beta,0)==s.Rational(row['mean_limit']) for x in first)
    assert all(s.limit(x,beta,0)==s.Rational(row['second_moment_limit']) for x in second)
    p=sum(h)/3
    assert p==s.Rational(row['rate'])
    assert all(s.simplify(s.limit(x,beta,0)-p/(p+z)/2)==0 for x in U)
    n=s.symbols('n',positive=True);birth=1/n;motion=1/n**2
    same=(birth+motion)/(birth+2*motion)
    assert s.factor(same-(n+1)/(n+2))==0 and s.limit(same,n,s.oo)==1
    return {'joint_Laplace_limit_per_target':'1/(3*s+2)','scaled_first_moment_limits':list(map(str,[s.limit(x,beta,0) for x in first])),
            'scaled_second_moment_limits':list(map(str,[s.limit(x,beta,0) for x in second])),
            'two_state_countercontrol_confirmed':True,'method':'First and second derivatives of the joint transform; no author implementation import.'}

def cube_receipts(result):
    own=json.loads((HERE/'INDEPENDENT_RESULTS.json').read_text())['cube_mean']
    author=result['rows'][1];beta=s.symbols('beta',positive=True);parse=lambda x:s.sympify(x,locals={'beta':beta})
    assert author['hazard_probability']==own['p'] and author['integrated_hazard_covariance']==own['C_0']
    assert author['scaled_mean_limit']==own['leading_scaled_mean']
    classes=own['mean_classes'];functions=[parse(row['exact_mean']) for row in classes]
    for f,g in zip(functions,author['exact_mean_types']):assert s.factor(f-parse(g))==0
    stationary=sum(row['states']*f for row,f in zip(classes,functions))/own['near_states']
    rows=[]
    for row in author['rows']:
        b=s.Rational(row['beta']);mean=s.factor(stationary.subs(beta,b))
        error=max(abs(b*f.subs(beta,b)-s.Rational(own['leading_scaled_mean'])) for f in functions)
        assert mean==s.Rational(row['mean_from_uniform']) and error==s.Rational(row['maximum_scaled_mean_error'])
        rows.append({'beta':str(b),'stationary_mean':str(mean),'maximum_scaled_error':str(error)})
    return rows

def monomer_receipts(result):
    rows=[]
    for author in result['rows'][2]['rows']:
        shape=author['shape'];periodic=author['periodic'];coords=list(it.product(*(range(n) for n in shape)));edges=set()
        for i,x in enumerate(coords):
            for j in range(i+1,len(coords)):
                differences=[abs(a-b) for a,b in zip(x,coords[j])]
                if periodic:differences=[min(delta,N-delta) for delta,N in zip(differences,shape)]
                if sum(differences)==1:edges.add(independent.edge(i,j))
        mask,perfect,poly=independent.counting_dp(len(coords),edges);Z=perfect(mask)
        opposite=[i for i,x in enumerate(coords) if sum(x)%2]
        ratios=[s.Rational(perfect(mask^(1<<0)^(1<<i)),Z) for i in opposite]
        assert Z==author['perfect_matchings'] and poly[len(coords)//2-1]==author['near_perfect_matchings']
        assert list(map(str,ratios))==author['origin_monomer_ratios']
        assert sum(ratios)==s.Rational(author['chi']) and 1/sum(ratios)==s.Rational(author['p'])
        rows.append({'shape':shape,'Z':Z,'near_matchings':poly[len(coords)//2-1],
                     'all_origin_ratios_match':True,'method':'Independent minimum-vertex matching-polynomial and removed-vertex recursion; no permanent-minor author code import.'})
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    author,authentication=authenticate()
    result={'authentication':authentication,'generic_fixture':generic_author_fixture(author),
            'cube_receipts':cube_receipts(author),'monomer_receipts':monomer_receipts(author),
            'limits':'No numerical control verifies the external d>2 theorem. Its definitions/statements/hypotheses were checked separately against authenticated primary sources; its full proof was not independently verified.'}
    args.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
