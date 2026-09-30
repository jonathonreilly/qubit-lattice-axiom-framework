#!/usr/bin/env python3
"""Exact one-coefficient GC obstruction, from the literal position energy.

Shares only source stencil construction with position_check.py, not the
Laurent/homotopy code. The mathematical proof is also in REPORT.md.
"""
from position_check import energy,plus,minus,unit,addterm
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json
P=Path(__file__).resolve().parent
E=energy();results=[]
for j in range(3):
    mixed=defaultdict(F)
    # -i[J_j,E_N], J_j=-P_j=i(T_j^2-T_j^-2)/4.
    for (a,r,b,s,i),v in E.items():
        for sign in [-1,1]:
            addterm(mixed,(minus(a,unit(j,2*sign)),r,b,s,i),v*F(sign,4))
            addterm(mixed,(a,r,plus(b,unit(j,2*sign)),s,i),-v*F(sign,4))
    moment=defaultdict(F)
    zero=defaultdict(F)
    for (a,r,b,s,i),v in mixed.items():
        addterm(moment,(minus(b,a),r,s,i),-a[j]*v)
        addterm(zero,(minus(b,a),r,s,i),v)
    assert not zero # the uniform-lapse mixed bracket is zero
    # sigma_j z_j^3 is absent from every scalar multiple of H.
    if j==0:key=(unit(j,3),0,1,1);expected=F(-1,4)
    elif j==1:key=(unit(j,3),0,1,0);expected=F(-1,4)
    else:key=(unit(j,3),0,0,1);expected=F(-1,4)
    assert moment[key]==expected
    results.append({'axis':j,'matrix_key':key,'coefficient':str(moment[key]),'uniform_bracket_zero':True,'first_lapse_moment_terms':len(moment)})
# Verify separately that all six actual r stencils have zero total/first moments.
rs=[]
for j in range(3):
    r=defaultdict(int)
    for k in range(3):
        if k!=j:r[(0,0,0)]+=2;r[unit(k)]-=1;r[unit(k,-1)]-=1
    rs.append(r)
for i,j in [(0,1),(0,2),(1,2)]:rs.append({(0,0,0):2,unit(i):-2,unit(j):-2,plus(unit(i),unit(j)):2})
for r in rs:
    assert sum(r.values())==0
    for j in range(3):assert sum(a[j]*v for a,v in r.items())==0
data={'axis_certificates':results,'all_six_curvature_stencils_zero_through_first_lapse_moment':True,'exact_scalar_U_contradiction':'nonzero sigma_j z_j^3 coefficient = 0'}
(P/'mixed_results.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
