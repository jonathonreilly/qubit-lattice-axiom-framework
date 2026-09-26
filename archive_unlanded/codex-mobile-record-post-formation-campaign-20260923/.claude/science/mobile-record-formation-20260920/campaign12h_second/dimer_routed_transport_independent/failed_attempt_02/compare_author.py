#!/usr/bin/env python3
"""Selective post-seal comparison; does not rerun the author's complete suite."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import datetime, hashlib, importlib.util, json, sys
import numpy as np
import sympy as sp
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;RAW=HERE.parent

def ident(p):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def module(name,p):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for row in pre['artifacts']:assert ident(Path(row['path']))==row
    assert ident(RAW/'DIMER_ROUTED_RECORD_TRANSPORT.md')==pre['sources']['primary_source']
    result=json.loads((RAW/'dimer_routed_transport_checks/RESULTS.json').read_text())
    for name,h in result['sources_sha256'].items():assert ident(RAW/name)['sha256']==h
    groups={r['group']:r['detail'] for r in result['groups']}
    assert all(r['passed'] for r in result['groups'])
    for name,row in groups.items():assert row==json.loads((RAW/'dimer_routed_transport_checks'/(name+'.json')).read_text())
    log=(RAW/'DIMER_ROUTED_TRANSPORT_RUN.log').read_text().splitlines()
    assert [json.loads(s) for s in log[:-1]]==[{'group':name,'passed':True} for name in groups]
    assert log[-1]=='PASS: five complete dimer-routed transport groups'
    assert (RAW/'DIMER_ROUTED_TRANSPORT_RUN.stderr').read_bytes()==b''
    for row in groups['geometry']['rows']:
        assert row['pairs']==row['N']**3//2 and row['directed_nonfixed_channels']==5*row['pairs']
        assert row['minimum_cycle']>=row['N']//2
    for row in groups['blocks']['connected_block_controls']:
        B=row['black_cube'];C=row['touching_pairs'];assert Fraction(row['average_difference_variance'])==Fraction(C-B,B*C)
    own=module('independent_routed_check',HERE/'independent_check.py')
    author=module('author_routed_check',RAW/'dimer_routed_transport_check.py')
    assert np.array_equal(own.E,author.EV) and np.array_equal(own.B,author.BV)
    s2=np.array([[[int(np.dot(delta,np.cross(ea,bb)+np.cross(eb,ba))) for eb,bb in zip(own.E,own.B)]
                  for ea,ba in zip(own.E,own.B)] for delta in own.DELTAS],dtype=int)
    assert np.array_equal(s2[::2],author.S2)
    cases=[]
    for sample in [0,1]:
        N=8;partner,accepted=author.matching(N,0 if sample==0 else 8*N**3,1000+N+sample,
                                            axis=sample%3,sign=1,winding=sample==0)
        g=own.Matching(N);g.partner=partner.copy();d,q,inv=g.arrays()
        data=author.routing(N,partner)
        assert np.array_equal(d,data[5]) and np.array_equal(q,data[6]) and np.array_equal(inv,data[7])
        receipt=groups['geometry']['rows'][sample]
        assert accepted==receipt['accepted_geometry_flips']
        colors=(13*np.arange(len(g.black))+5)%14;site=np.empty(N**3,dtype=int)
        site[g.black]=colors;site[partner[g.black]]=colors
        expected=Counter()
        for k in range(6):
            for u,v in enumerate(q[k]):
                if u==v:continue
                l,a,b,r=map(int,[colors[inv[k,u]],colors[u],colors[v],colors[q[k,v]]])
                h2=int(s2[k,l,a]+s2[k,a,r]-s2[k,l,b]-s2[k,b,r])
                action=tuple(sorted((tuple(sorted((g.black[u],g.black[v]))),tuple(sorted((int(partner[g.black[u]]),int(partner[g.black[v]])))))))
                expected[action]+=8+h2
        assert expected==author.events(N,partner,site,0)==author.events(N,partner,site,1)
        cases.append({'sample':sample,'accepted_geometry_flips':accepted,'independent_exact_action_rate_count':len(expected),
                      'all_routing_arrays_and_both_parity_event_rates_agree':True})
    # Independently assemble the stated equal-color symbol and generic full-support
    # covariance symmetry, using the exact product-current derivative.
    p=sp.ones(14,1)/14;Q=sp.Matrix([1,2,-1]);S=sum((Q[i]*sp.Matrix(s2[2*i].tolist())/2 for i in range(3)),sp.zeros(14))
    A=2*sp.diag(*p)*S;lam=sp.symbols('lambda')
    tangent_poly=sp.cancel(A.charpoly(lam).as_expr()/lam)
    assert sp.simplify(tangent_poly-sp.sympify(groups['wave']['tangent_characteristic_polynomial']))==0
    weights=sp.Matrix(range(1,15));p=weights/sum(weights);C=sp.diag(*p)-p*p.T
    for i in range(3):
        S=sp.Matrix(s2[2*i].tolist())/2;s=S*p;F=(p.T*S*p)[0]
        A=2*sp.diag(*(s-sp.ones(14,1)*F))+2*sp.diag(*p)*S-4*p*s.T
        assert A*C==C*A.T
    # Independent N=6 exception to the distinct-four-position argument.
    short=own.Matching(6);qs=short.arrays()[1]
    assert any(qs[k,qs[k,qs[k,u]]]==u and qs[k,u]!=u for k in range(6) for u in range(len(short.black)))
    for row in pre['artifacts']:assert ident(Path(row['path']))==row
    output={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author_result':ident(RAW/'dimer_routed_transport_checks/RESULTS.json'),
            'source_bindings':[ident(RAW/name) for name in result['sources_sha256']],
            'all_group_files_and_logs_authenticate':True,'selected_complete_rate_comparisons':cases,
            'equal_color_wave_polynomial_agrees_exactly':True,'generic_full_support_A_C_symmetry_exact':True,
            'short_torus_countercontrol':'N=6 maximal-winding routing has nontrivial three-cycles, so l and r repeat.',
            'author_N32_block_geometry_or_FFT_replayed':False,
            'scope':'Author aggregate receipts are authenticated; uniform replacement is established by the independent proof assessment, not by these counts.',
            'remaining_finding':'F1: gamma != 0 must qualify the four-propagating-mode count.'}
    (HERE/'AUTHOR_COMPARISON_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(cases,indent=2));print('All declared sources/results authenticate; selected complete rates and exact wave/covariance matrices agree.')

if __name__=='__main__':main()
