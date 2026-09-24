"""Own released-source primitive check and author-result correspondence.

Reads the released result as explicit input data; never imports or executes
the author builder. No full dynamics or timing-quadrature reproduction.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
from fractions import Fraction
import hashlib, json, math

ROOT=Path(__file__).resolve().parent
AUTHOR=ROOT/'post_sources/author'
result=json.loads((AUTHOR/'PREPARED_PROBE_RESULTS.json').read_text())
checks=[];certificates=[]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def check(name,condition,**details):
    assert condition,(name,details)
    row=dict(name=name,verified=True,**details);checks.append(row)
    print(json.dumps(row,sort_keys=True))
def add(*args):
    out=defaultdict(int)
    for factor,word in args:
        for key,value in word.items():out[key]+=factor*value
    return {key:value for key,value in out.items() if value}
def key(word):return tuple(sorted(word.items()))
def flow_json(word):return [[list(a),list(b),value] for (a,b),value in sorted(word.items())]
def div(word):
    out=defaultdict(int)
    for (a,b),value in word.items():out[a]+=value;out[b]-=value
    return {v:value for v,value in out.items() if value}

L=6;vertices=list(product(range(L),repeat=3));A={v for v in vertices if sum(v)%2==0}
def adjacent(v):
    out=[]
    for axis in range(3):
        for sign in (-1,1):
            w=list(v);w[axis]=(w[axis]+sign)%L;out.append(tuple(w))
    return out
def increment(x,y):
    assert y in adjacent(x)
    return {(x,y):1} if x in A else {(y,x):-1}
def deviation(charges):
    return {v:charges.get(v,0)-int(v in A) for v in vertices if charges.get(v,0)!=int(v in A)}
def physical(charges,word):return div(word)==deviation(charges)
a=(0,0,0);d=(1,1,0);h=(2,2,0)
c=(1,0,0);e=(0,1,0);b=(5,0,0)
blockers=[(0,5,0),(0,0,1),(0,0,5)]
common={(tuple(x),tuple(y)):value for x,y,value in result['primitive']['common_flow']}
expected_div={d:-1,h:-2,**{v:1 for v in blockers}}
route_flow={}
for route,source,target in zip(result['primitive']['common_flow_paths'],[d,h,h],blockers):
    route=list(map(tuple,route));assert route[0]==source and route[-1]==target
    for x,y in zip(route,route[1:]):route_flow=add((1,route_flow),(-1,increment(x,y)))
check('root_common_flow',route_flow==common and div(common)==expected_div,
      links=len(common),common_flow=flow_json(common),divergence=[[list(v),value] for v,value in sorted(div(common).items())])
loop=add((1,increment(a,c)),(-1,increment(d,c)),(1,increment(d,e)),(-1,increment(a,e)))
check('plaquette_divergence',div(loop)=={},loop=flow_json(loop))

initial_count=0;hop_count=0;final_count=0;root_rows=[];zero_outputs={-1:[],1:[]}
for sigma in [-1,1]:
    for branch,(occupied,empty,phase) in enumerate([(c,e,1),(e,c,-1)]):
        charges={v:1 for v in A};charges[d]=charges[h]=-1
        charges.update({v:1 for v in blockers+[occupied]})
        base=add((1,common),(-1,increment(d,occupied)))
        retained_at_zero=[]
        for flux in [-2,-1,0,1,2]:
            field=add((1,base),(flux,loop))
            assert physical(charges,field);initial_count+=1
            attempts=[]
            for destination in adjacent(a):
                if charges.get(destination,0):continue
                after=dict(charges);old_charge=after.pop(a);after[destination]=old_charge
                intermediate=add((1,field),(-old_charge,increment(a,destination)))
                assert physical(after,intermediate);hop_count+=1
                legal=not after.get(b,0)
                row=dict(destination=list(destination),birth_legal=legal,
                         intermediate_deviation=[[list(v),q] for v,q in sorted(deviation(after).items())],
                         intermediate_field=flow_json(intermediate))
                if legal:
                    after[a]=sigma;after[b]=-sigma
                    final=add((1,intermediate),(sigma,increment(a,b)))
                    assert physical(after,final) and len(after)==114 and sum(after.values())==108
                    assert all(v in after for v in A);final_count+=1
                    row.update(final_deviation=[[list(v),q] for v,q in sorted(deviation(after).items())],final_field=flow_json(final))
                    if flux==0:retained_at_zero.append((key(after),final,phase,branch))
                attempts.append(row)
            assert len(attempts)==2 and sum(x['birth_legal'] for x in attempts)==1
            certificates.append(dict(sigma=sigma,branch=branch,reference_loop_flux=flux,
                                     initial_deviation=[[list(v),q] for v,q in sorted(deviation(charges).items())],
                                     initial_field=flow_json(field),attempts=attempts))
        assert len(retained_at_zero)==1
        zero_outputs[sigma]+=retained_at_zero
        root_rows.append(dict(sigma=sigma,initial_occupied_variable=list(occupied),initial_records=len(charges),
                              output_records=len(dict(retained_at_zero[0][0])),retained_paths=1,
                              outward_to_birth_site_rejected=1,physical_flux_cases_checked=5))
check('actual_root_preparation_primitive_gauss',initial_count==20 and hop_count==40 and final_count==20,
      physical_initials=initial_count,physical_intermediates=hop_count,physical_successful_outputs=final_count,
      serialized_cases=len(certificates),author_rows_equal=root_rows==result['primitive']['rows'])
assert root_rows==result['primitive']['rows']

def gram(paths,dephased=False):
    polynomial=defaultdict(Fraction)
    for x,y in product(paths,repeat=2):
        if x[0]!=y[0] or (dephased and x[3]!=y[3]):continue
        polynomial[key(add((1,y[1]),(-1,x[1])))]+=Fraction(x[2]*y[2],2)
    return {word:value for word,value in polynomial.items() if value}
expected={():Fraction(1),key(loop):Fraction(-1,2),key(add((-1,loop))):Fraction(-1,2)}
effects=[]
for sigma in [-1,1]:
    paths=zero_outputs[sigma]
    assert paths[0][0]==paths[1][0]
    dark=gram(paths);dephased=gram(paths,True)
    assert dark==expected and dephased=={():Fraction(1)}
    # Mutation discriminators: incorrect path deletion or relative sign cannot
    # retain the claimed effect. Missing A charge compensation violates Gauss.
    deleted=gram(paths[:1]);flipped=list(paths)
    x=flipped[1];flipped[1]=(x[0],x[1],-x[2],x[3])
    assert deleted!=expected and gram(flipped)!=expected
    effects.append(dict(sigma=sigma,dark=[dict(shift=flow_json(dict(word)),coefficient=str(value)) for word,value in dark.items()],
                        dephased_identity=str(dephased[()]),dephased_nonconstant_terms=0,
                        dropped_path_changes_effect=True,reversed_relative_sign_changes_effect=True))
check('root_resolved_effects_and_dephasing',len(effects)==2,effects=effects)
bad_charges={v:1 for v in A};bad_charges[h]=-1;bad_charges.update({v:1 for v in blockers+[c]})
bad_field=add((1,common),(-1,increment(d,c)))
check('missing_compensating_A_sign_is_detected',not physical(bad_charges,bad_field))

# The original coherent channel is the union of sign outputs. Distinct matter
# words make their cross terms zero, while the same-sign branches interfere.
coherent=gram(zero_outputs[-1]+zero_outputs[1])
check('root_coherent_initial_effect',coherent=={word:2*value for word,value in expected.items()},
      final_matter_words=len({x[0] for x in zero_outputs[-1]+zero_outputs[1]}))

arithmetic_rows=[]
for row in result['separate_timing']['rows']:
    g=row['g'];bwin=row['window'];norm=bwin*g*g
    assert math.isclose(bwin,g**row['window_exponent'],rel_tol=1e-14)
    assert 0<=row['vacuum_probability']<row['one_probability']<=1
    for numerator,denominator_name in [('vacuum_probability','vacuum_over_b_g2'),('one_probability','one_over_b_g2')]:
        assert math.isclose(row[numerator]/norm,row[denominator_name],rel_tol=1e-14)
    assert math.isclose((row['one_probability']-row['vacuum_probability'])/norm,row['excess_over_b_g2'],rel_tol=1e-14)
    arithmetic_rows.append(row)
assert len(arithmetic_rows)==10
small=arithmetic_rows[-2];large=arithmetic_rows[-1]
assert round(small['vacuum_over_b_g2'],7)==.5165821
assert round(small['excess_over_b_g2'],7)==.9996747
assert round(large['vacuum_over_b_g2'],2)==872.39
assert result['separate_timing']['maximum_scaled_quadrature_refinement']<5.23e-8
check('author_timing_result_arithmetic_only',True,rows=arithmetic_rows,
      quadrature_reported_scaled_change=result['separate_timing']['maximum_scaled_quadrature_refinement'],
      author_timing_rerun=False,scope='Arithmetic and prose correspondence only; no independent quadrature or dynamics reproduction.')

execution=json.loads((AUTHOR/'EXECUTION.json').read_text())
check('author_execution_hash_bindings',execution['code_sha256']==sha(AUTHOR/'prepared_probe_controls.py')
      and execution['result_sha256']==sha(AUTHOR/'PREPARED_PROBE_RESULTS.json')
      and execution['exit_code']==0 and execution['stderr_bytes']==0 and (AUTHOR/'CONTROL.stderr').stat().st_size==0,
      external_elapsed_seconds=execution['elapsed_seconds'],internal_elapsed_seconds=result['elapsed_seconds'],
      execution_claim_is_author_evidence=True)

(ROOT/'POST_PATH_CERTIFICATES.json').write_text(json.dumps(certificates,indent=2)+'\n')
output=dict(scope='Own POST primitive/Gauss check of the separately released root preparation and arithmetic evidence review; no author code executed.',
            script_sha256=sha(Path(__file__)),author_result_sha256=sha(AUTHOR/'PREPARED_PROBE_RESULTS.json'),
            check_count=len(checks),checks=checks,path_certificate_sha256=sha(ROOT/'POST_PATH_CERTIFICATES.json'))
(ROOT/'POST_CONTROL_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print('TOTAL',len(checks),'bounded POST checks completed; author controls not rerun')
