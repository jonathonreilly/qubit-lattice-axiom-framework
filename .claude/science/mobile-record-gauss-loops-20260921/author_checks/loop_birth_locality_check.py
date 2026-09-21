#!/usr/bin/env python3
"""Exact conditional-law witness for constant-rate four-record loop births."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from fractions import Fraction
import hashlib,json

HERE=Path(__file__).resolve().parent
N=7
unit=tuple(tuple(int(i==j) for j in range(3)) for i in range(3))
add=lambda p,q,a=1:tuple((p[j]+a*q[j])%N for j in range(3))
origin=(0,0,0)
def loop(center,i,j,species,sign):
    return {add(center,unit[j],-1):(species,i,sign),
            add(center,unit[i]):(species,j,sign),
            add(center,unit[j]):(species,i,-sign),
            add(center,unit[i],-1):(species,j,-sign)}
def charge(records):
    out=Counter()
    for point,(species,axis,sign) in records.items():
        out[(species,add(point,unit[axis],-1))]+=sign
        out[(species,add(point,unit[axis]))]-=sign
    return {key:value for key,value in out.items() if value}
empty={};blocked=loop((2,0,1),1,2,0,1)
neighbors={add(origin,e,sign) for e in unit for sign in (-1,1)}
checks=[]
def check(name,condition,detail=None):
    assert condition,(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
check('backgrounds_are_Gauss_free_and_agree_at_center_and_neighbors',
      not charge(empty) and not charge(blocked) and not ((neighbors|{origin})&set(blocked)))
through=[]
for center in product(range(N),repeat=3):
    for i,j in combinations(range(3),2):
        for species in (0,1):
            for sign in (-1,1):
                event=loop(center,i,j,species,sign)
                if origin in event:through.append(event)
def hazards(background):
    return Counter(event[origin] for event in through if not(set(event)&set(background)))
a,b=hazards(empty),hazards(blocked)
check('all_templates_containing_origin_counted',len(through)==48 and len(a)==12 and set(a.values())=={4})
expected={label:(4 if label[1]==0 else 3) for label in a}
check('source_free_remote_loop_changes_normalized_odds',dict(b)==expected and sum(b.values())==40,
      dict(empty_per_label='1/12',blocked_x_per_label='1/10',blocked_yz_per_label='3/40'))
formula={}
for axis in range(3):
    value=0
    for j in range(3):
        if j==axis:continue
        for sign in (-1,1):
            center=add(origin,unit[j],sign)
            sites=(add(origin,unit[j],2*sign),add(center,unit[axis]),add(center,unit[axis],-1))
            value+=int(not(set(sites)&set(blocked)))
    formula[axis]=value
check('direct_enumeration_matches_single_site_hazard_formula',formula=={0:4,1:3,2:3})
pa={label:Fraction(value,sum(a.values())) for label,value in a.items()}
pb={label:Fraction(value,sum(b.values())) for label,value in b.items()}
total_variation=sum(abs(pa[label]-pb[label]) for label in a)/2
check('difference_survives_any_common_site_rate',total_variation==Fraction(1,15),dict(total_variation=str(total_variation)))
report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Counterexample to nearest-neighbor forming-label odds for the specified equal-rate template birth generator; not a general impossibility theorem.')
(HERE/'LOOP_BIRTH_LOCALITY_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
