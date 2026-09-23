"""Exact field-translation Grams after a specified first cube-edge mark."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json
from operators import birth_paths, add_shift
D=Path(__file__).resolve().parent
edges=[(x,x^(1<<a)) for x in range(8) for a in range(3) if x<(x^(1<<a))]
A={0,3,5,6};q0=tuple(1 if x in A else 0 for x in range(8));zero=(0,)*len(edges)
first_edge=edges.index((0,1))


def divergence(shift):
    d=[0]*8
    for (x,y),v in zip(edges,shift):d[x]+=v;d[y]-=v
    return tuple(d)


def apply_birth(paths,e,c):
    out=defaultdict(int)
    for (q,oldshift),amp in paths.items():
        for qq,shift,val in birth_paths(q,edges,e,c):
            newshift=add_shift(oldshift,shift)
            assert divergence(newshift)==tuple(qq[x]-q0[x] for x in range(8))
            out[qq,newshift]+=amp*val
    return dict(out)


def gram(paths,normalization=1):
    byword=defaultdict(list)
    for (q,s),a in paths.items():byword[q].append((s,a))
    result=defaultdict(Fraction)
    for group in byword.values():
        for s,a in group:
            for t,b in group:
                delta=tuple(y-x for x,y in zip(s,t))
                assert divergence(delta)==(0,)*8
                result[delta]+=Fraction(a*b,normalization)
    return {s:a for s,a in result.items() if a}


def add_poly(polys):
    out=defaultdict(Fraction)
    for poly in polys:
        for s,v in poly.items():out[s]+=v
    return {s:v for s,v in out.items() if v}


def encode(poly):
    return [{'field_shift':list(s),'coefficient':str(a)} for s,a in sorted(poly.items())]


rows=[]
for name,c,norm in [('first_plus',1,2),('first_minus',-1,2),('first_coherent',None,4)]:
    first=apply_birth({(q0,zero):1},first_edge,c)
    assert gram(first)=={zero:Fraction(norm)}
    marked=[];resolved=[];coherent=[]
    for e,edge in enumerate(edges):
        percharge=[]
        for d in (-1,1):
            second=apply_birth(first,e,d)
            g=gram(second,norm);resolved.append(g);percharge.append(g)
            marked.append({'edge':edge,'new_charge_at_tail':d,'histories_after_combining':len(second),
                           'gram':encode(g)})
        gc=gram(apply_birth(first,e,None),norm);coherent.append(gc)
        assert gc==add_poly(percharge)
        marked.append({'edge':edge,'new_charge_at_tail':'coherent','gram':encode(gc)})
    total=add_poly(resolved)
    assert total==add_poly(coherent)
    rows.append({'first_instrument':name,'first_norm_squared':norm,
                 'first_output_branches':[
                     {'q':q,'field_shift':s,'coefficient':a} for (q,s),a in first.items()],
                 'second_marked_grams':marked,'total_gram':encode(total)})
out={'edge_order':edges,'A':sorted(A),'first_edge':(0,1),
     'interpretation':'Each polynomial sum c_s T_s acts on the initial divergence-zero physical rotor field. Multiply by kappa for conditional instantaneous second-event rates. Exact integer path counts divided by the exact first-mark norm; no time evolution inferred.',
     'rows':rows}
(D/'CUBE_GRAM_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
