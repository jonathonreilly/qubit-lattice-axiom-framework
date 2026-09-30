"""Postcomparison control with the checker's own frozen elementary operators.

Author coefficients are now disclosed. This corroboration is not a blind test;
the independent PRE/control remains immutable. Price<=5CPU seconds/80MB.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from collections import defaultdict
from itertools import product
from fractions import Fraction
import ast,hashlib,json,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(5,5));start=time.process_time();here=Path(__file__).resolve().parent
src=(here/'check.py').read_bytes()
assert hashlib.sha256(src).hexdigest()=='2376287209496819d10d0e919682bee4f88527cbdda287cebe13f4420fe589a5'
# Load only our pre-frozen definitions. Do not execute its original run or
# overwrite its frozen result. No author module or builder is imported.
tree=ast.parse(src);defs=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))]
env={'__name__':'own_frozen_definitions','dirs':((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))}
exec(compile(ast.Module(body=defs,type_ignores=[]),'own_frozen_definitions','exec'),env)
P=env['Preparation'];ops=env['relative_ops'];add=env['add'];dirs=env['dirs'];default=env['base_charge']
p=P(8)
for y,z in product(range(8),repeat=2):
    parity=(1-y-z)%2
    for j in range(2):
        a=((parity+4*j+1)%8,y,z)
        if a!=(2,0,0):p.birth_pair(a)
p.move((2,0,0),(1,0,0),'out');p.move((4,0,0),(3,0,0),'out')
assert p.births==127 and p.unit
move,gamma,gauss,walk,holes=ops(p);zero=((),());h0=holes(zero)
assert h0=={(2,0,0),(4,0,0)} and gamma(zero)==0
neighbors=lambda v:[p.wrap(add(v,d)) for d in dirs]
def charge(key,v):return dict(key[0]).get(v,p.charge(v))
def field(key,a,b):return {(c,d):e for c,d,e in key[1]}.get((a,b),p.E.get((a,b),0))
rows=[]
for spin_one in (False,True):
    out=defaultdict(int)
    for a in h0:
        for b in neighbors(a):
            middle,u1=move(zero,a,b,'in')
            for c in neighbors(b):
                final=move(middle,c,b,'out')
                if final is not None and (not spin_one or (u1 and final[1])):out[final[0]]+=1
    assert all(gauss(k) and gamma(k)==0 and len(holes(k))==2 for k in out)
    proj=sum(v*v for k,v in out.items() if field(k,(2,0,0),(1,0,0))==0)
    assert proj==5
    rows.append({'carrier':'spin_one' if spin_one else 'rotor','FFdagger_words':len(out),'projected_norm_squared':proj,'second_derivative':2*proj})
paths=[];channel_states={}
for a in h0:
    for b in neighbors(a):
        before=field(zero,a,b);step=charge(zero,b);A=before*(before+step)
        middle,_=move(zero,a,b,'in')
        for c in holes(middle):
            if b not in neighbors(c):continue
            for sigma in (-1,1):
                result=move(middle,c,b,'birth',sigma)
                if result is None:continue
                after,_=result;before2=field(middle,c,b);B=before2*(before2+sigma)
                assert not holes(after) and gauss(after)
                label=(c,b,sigma);assert label not in channel_states
                channel_states[label]=after
                paths.append({'refill_A':a,'shared_B':b,'original_birth_A':c,'birth_sign':sigma,'spin_squared_weight_factors_numerators':[A,B]})
assert len(paths)==4 and sorted(tuple(x['spin_squared_weight_factors_numerators']) for x in paths)==[(0,0),(0,0),(0,0),(0,2)]
for c,b,_ in channel_states:
    assert channel_states[c,b,-1]!=channel_states[c,b,1]
rates=[]
for S in (1,2,3,4,8):
    C=S*(S+1);rate=sum((1-Fraction(v['spin_squared_weight_factors_numerators'][0],C))*(1-Fraction(v['spin_squared_weight_factors_numerators'][1],C)) for v in paths)
    assert rate==4-Fraction(2,C)
    rates.append({'S':S,'exact_rate_in_units_kappa':str(rate)})
result={'scope':'Postcomparison independent implementation of author displayed word; author results disclosed before this control. No author code imported.','field_witness':rows,'actual_original_first_dressed_jump_paths':paths,'exact_spin_rates':rates,'resolved_and_coherent_edge_losses_equal_on_this_input':True,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<5 and result['peak_rss_bytes']<80*1024**2
(here/'AUTHOR_WORD_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
