#!/usr/bin/env python3
"""Selective source/result comparison; does not execute the author's checker."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from fractions import Fraction
import json,math
import numpy as np
import mpmath as mp

OUT=Path(__file__).resolve().parent;RAW=OUT.parent
def row(path):
    data=path.read_bytes();return {'path':str(path),'bytes':len(data),'sha256':sha256(data).hexdigest()}

def main():
    pre=json.loads((OUT/'PRE_COMPARISON_SEAL.json').read_text())
    for r in pre['artifacts']+[pre['primary_note']]+pre['dependencies']:assert row(Path(r['path']))==r
    path=RAW/'dimer_routed_preparation_checks/RESULTS.json';result=json.loads(path.read_text())
    for name,h in result['sources_sha256'].items():assert row(RAW/name)['sha256']==h
    groups={x['group']:x for x in result['groups']}
    evidence=[row(path),row(RAW/'DIMER_ROUTED_PREPARATION_RUN.log'),row(RAW/'DIMER_ROUTED_PREPARATION_RUN.stderr')]
    assert (RAW/'DIMER_ROUTED_PREPARATION_RUN.stderr').read_bytes()==b''
    for name,g in groups.items():
        p=RAW/'dimer_routed_preparation_checks'/(name+'.json')
        assert json.loads(p.read_text())==g['detail'];assert g['passed'];evidence.append(row(p))
    inventory=[]
    for g in groups['physical_graph_comparison']['detail']['rows']:
        k=g['K'];edges=list(combinations(range(k),2));connected=0
        # Alternative bitset reachability; no author path routine imported.
        for mask in range(1<<len(edges)):
            reach=1
            while True:
                old=reach
                for i,(a,b) in enumerate(edges):
                    if mask&(1<<i) and (reach&((1<<a)|(1<<b))):reach|=(1<<a)|(1<<b)
                if reach==old:break
            connected+=reach==((1<<k)-1)
        assert connected==g['connected_labeled_graphs']
        counts=[sum(j%3==i for j in range(k)) for i in range(3)]
        assert math.factorial(k)//math.prod(math.factorial(c) for c in counts)==g['color_sector_size']
        inventory.append({'K':k,'independently_counted_connected_graphs':connected})
    detail=groups['physical_graph_comparison']['detail']
    assert sum(g['independently_counted_connected_graphs'] for g in inventory)==detail['graphs']
    assert sum(g['independently_counted_connected_graphs']*math.comb(g['K'],2) for g in inventory)==detail['immutable_endpoint_transposition_replays']
    density=groups['nonreversible_preparation']['detail'];cyclic=[]
    for r in density['nonreversible_density_rows']:
        t=r['t'];theta=2*np.pi*np.arange(5)/5
        eigen=2*np.exp(1j*theta)+.5*np.exp(-1j*theta)-2.5
        # Character inversion gives the whole row law from site 0, independently
        # of the author's matrix exponential.
        law=np.real(np.exp(-1j*np.outer(np.arange(5),theta))@np.exp(t*eigen)/5)
        l2=math.sqrt(float(np.sum(np.exp(2*t*eigen[1:].real))))
        tv=float(np.sum(abs(law-.2))/2)
        expected_bound=2*math.exp(-5*t/96)
        assert abs(l2-r['centered_L2'])<3e-14
        assert abs(tv-r['total_variation'])<3e-14
        assert abs(expected_bound-r['L2_bound'])<3e-14
        cyclic.append({'time':t,'L2_absolute_difference':abs(l2-r['centered_L2']),
                       'TV_absolute_difference':abs(tv-r['total_variation'])})
    mp.mp.dps=80;schedules=[]
    for r in density['schedule']:
        n=r['N'];k=n**3//2;g=mp.mpf(11)/(10*4*(3*n-1)*(k-1));eps=mp.mpf(n)**-4
        prep=(k*mp.log(14)/2+mp.log(1/(2*eps)))/g
        relative=float(abs(mp.mpf(r['sufficient_post_completion_time'])/prep-1))
        assert relative<5e-16
        assert r['pairs']==k and r['epsilon']==float(eps)
        assert abs(r['gap_lower_bound']/float(g)-1)<3e-16
        schedules.append({'N':n,'independent_80_digit_preparation_time':mp.nstr(prep,40),
                          'reported_float_relative_error':relative})
    out={'scope':'Author source/log binding, group consistency, independent inventory and analytic/numerical receipt controls; no full author-suite rerun.',
         'author_checker':row(RAW/'dimer_routed_preparation_check.py'),'author_evidence':evidence,
         'graph_inventory':inventory,'five_cycle_character_inversion':cyclic,'schedule_high_precision':schedules,
         'all_771_author_spectral_eigenvalue_rows_independently_recomputed':False,
         'author_conditional_random_test_values_independently_recomputed':False,'unresolved_findings':[]}
    (OUT/'AUTHOR_COMPARISON_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'author_groups_bound':len(groups),'inventory_graphs':detail['graphs'],
                      'character_inversions':len(cyclic),'high_precision_schedules':len(schedules),
                      'unresolved_findings':[]},indent=2))

if __name__=='__main__':main()
