"""Exact original-mark compression of full H4 to prebirth rotor sector.
Columns are grouped by actual final matter; their electric shifts are retained.
This computes an operator Laurent polynomial, not a field-angle evaluation.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from pathlib import Path
import json
import birth_work_exact as b

def shift_difference(e,f):
    z=Counter(dict(e))
    for k,v in f:z[k]-=v
    return tuple(sorted((k,v) for k,v in z.items() if v))

def gram_laurent(vec):
    groups=defaultdict(list)
    for (q,e),v in vec.items():groups[q].append((e,v))
    out=Counter()
    for group in groups.values():
        for e,u in group:
            for f,v in group:out[shift_difference(e,f)]+=u*v
    return out

def work_laurent(vec,halo=0):
    n=b.norm2(vec);out=Counter()
    for a,c in b.candidate_pairs(vec,halo):
        for z,v in gram_laurent(b.apply_pair(vec,a,c)).items():out[z]-=Fraction(2*v,n)
        for z,v in gram_laurent(b.apply_pair({b.OMEGA:1},a,c)).items():out[z]+=2*v
    return {z:v for z,v in out.items() if v}

def main():
    result={}
    for name,sigmas in [('minus',(-1,)),('plus',(1,)),('coherent',(-1,1))]:
        vec=b.birth(b.ORIGIN,(1,0,0),sigmas)
        poly=work_laurent(vec)
        # Every term is an actual closed Gauss-law circulation, and Hermitian.
        for z,v in poly.items():
            inv=tuple((ab,-c) for ab,c in z)
            assert poly.get(inv)==v
            assert b.gauss(((),z))
        scalar=poly[()]
        assert scalar==b.energy_change(vec)[0]
        nonconstant=sum(abs(v) for z,v in poly.items() if z)
        assert work_laurent(vec,halo=1)==poly
        result[name]={'constant':str(scalar),'nonconstant_l1':str(nonconstant),
                      'flat_angle_value':str(sum(poly.values())),
                      'number_nonconstant_words':len(poly)-1,
                      'actual_wait_uniform_bound_numerator':str(3072+32*nonconstant),
                      'positivity_sufficient_R':str((3072+32*nonconstant)/scalar),
                      'terms':[{'shift':z,'coefficient':str(v)} for z,v in sorted(poly.items())]}
        print(name,{k:v for k,v in result[name].items() if k!='terms'},flush=True)
    # Coherent versus resolved magnetic operator equality is tested, not assumed.
    coherent=work_laurent(b.birth(b.ORIGIN,(1,0,0),(-1,1)))
    minus=work_laurent(b.birth(b.ORIGIN,(1,0,0),(-1,)))
    plus=work_laurent(b.birth(b.ORIGIN,(1,0,0),(1,)))
    cross={z:coherent.get(z,0)-(minus.get(z,0)+plus.get(z,0))/2 for z in set(coherent)|set(minus)|set(plus)}
    cross={z:v for z,v in cross.items() if v}
    result['coherent_minus_resolved_average_terms']=[{'shift':z,'coefficient':str(v)} for z,v in sorted(cross.items())]
    print('coherent-minus-resolved-average operator terms',len(cross))
    print('TOTAL: PASS=4 FAIL=0 (exact local polynomial; Gauss/Hermiticity; direct constant; locality halo)')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
