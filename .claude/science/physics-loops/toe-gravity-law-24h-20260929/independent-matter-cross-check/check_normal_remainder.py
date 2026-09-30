#!/usr/bin/env python3
"""Compare data serialization with independent position/Taylor coefficients."""
from check_matter import *

def read_pauli(name,denom):
    out={}
    for ex,p,im,val in json.loads((AUTHOR/name).read_text())[0]:
        n=F(val)*denom;assert n.denominator==1
        out[(tuple(ex),p,im)]=int(n)
    return out

def main():
    budget();start=time.time();denom=49152
    energy,currents=source_operators();defect,literal=flat_defect(energy,currents,denom)
    imported={}
    for (ex,p,im),val in read_pauli('defect.json',denom).items():
        a,b,c=ex[:3],ex[3:6],ex[6:]
        v=(val,0) if not im else (0,val)
        for (i,j),m in PAULI[p].items():
            put(imported,(minus(b,a),neg(a),i,minus(c,a),j),gmul(v,m))
    assert imported==defect
    jets=first_jets(literal);expanded={}
    for (z,a,b,i,j),v in jets.items():
        xa=[(ZERO,1)] if a<0 else [(unit(a),1),(ZERO,-1)]
        yb=[(ZERO,1)] if b<0 else [(unit(b),1),(ZERO,-1)]
        for x,cx in xa:
            for y,cy in yb:put(expanded,(x+y+z,i,j),gscale(v,cx*cy))
    pauli={}
    for ex in {k[0] for k in expanded}:
        a=expanded.get((ex,0,0),GCZERO);b=expanded.get((ex,0,1),GCZERO)
        c=expanded.get((ex,1,0),GCZERO);d=expanded.get((ex,1,1),GCZERO)
        coefficients=[gscale(gadd(a,d),F(1,2)),gscale(gadd(b,c),F(1,2)),
                      gscale(gmul((0,1),gadd(b,gscale(c,-1))),F(1,2)),
                      gscale(gadd(a,gscale(d,-1)),F(1,2))]
        for p,v in enumerate(coefficients):
            for im,value in enumerate(v):
                if value:pauli[(ex,p,im)]=value
    expected=read_pauli('literal_plus_J_normal.json',denom)
    assert pauli==expected,(len(pauli),len(expected))
    result={'defect_serialization_matches_independent_position_result':True,
            'literal_plus_J_Taylor_matrix_entries':len(jets),
            'literal_plus_J_expanded_Pauli_terms':len(pauli),
            'literal_plus_J_normal_serialization_matches':True,
            'elapsed_seconds':time.time()-start}
    (HERE/'normal_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
