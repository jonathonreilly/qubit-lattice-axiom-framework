from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json
from operators import birth_paths, add_shift
D=Path(__file__).resolve().parent
edges=[(x,x^(1<<a)) for x in range(8) for a in range(3) if x<(x^(1<<a))]
q0=tuple(1 if x in (0,3,5,6) else 0 for x in range(8));zero=(0,)*12
loop=(0,1,-1,0,0,0,1,0,0,-1,0,0)


def apply(vector,e,c):
    out=defaultdict(complex)
    for (q,E),a in vector.items():
        for qq,dE,b in birth_paths(q,edges,e,c):
            out[qq,add_shift(E,dE)]+=a*b
    return dict(out)


def norm(vector):
    return sum(abs(a)**2 for a in vector.values())


rows=[]
for label,field,normfield in [('zero_flux',{zero:1},1),
                            ('loop_plus',{zero:1,loop:1},2),
                            ('loop_minus',{zero:1,loop:-1},2),
                            ('loop_i',{zero:1,loop:1j},2)]:
    initial={(q0,E):a for E,a in field.items()}
    for firstc,normfirst in [(1,2),(-1,2),(None,4)]:
        first=apply(initial,edges.index((0,1)),firstc)
        assert norm(first)==normfield*normfirst
        marked=[]
        for e,edge in enumerate(edges):
            rates=[norm(apply(first,e,c))/(normfield*normfirst) for c in (-1,1)]
            coherent=norm(apply(first,e,None))/(normfield*normfirst)
            assert coherent==sum(rates)
            marked.append({'edge':edge,'resolved_rates_without_kappa':rates,
                           'coherent_rate_without_kappa':coherent})
        total=sum(sum(r['resolved_rates_without_kappa']) for r in marked)
        expected={'zero_flux':8,'loop_plus':9,'loop_minus':7,'loop_i':8}[label]
        assert total==expected
        rows.append({'field':label,'first_charge':firstc,'total_rate_without_kappa':total,
                     'all_marked_rates':marked})
out={'loop_shift':loop,'normalizable_field_controls':rows,
     'scope':'Direct norms of finite-support physical output wavefunctions. Values are immediate rates, not waiting-law parameters.'}
(D/'CUBE_FIELD_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
