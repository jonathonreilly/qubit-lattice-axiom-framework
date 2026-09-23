"""Post-PRE comparison; no author builders imported or executed.

Authenticate the frozen sources, compare all saved scientific result fields,
and independently check the added initial-sector/count composition.  Existing
independent operator and scalar-clock definitions retain their PRE identities.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import ast, cmath, hashlib, json, math
import numpy as np
import sympy as sp
from operators import (hops, add_shift, birth_paths, charge_basis,
                       hopping_matrix, birth_matrix, ring_operators)

D = Path(__file__).resolve().parent
A = D.parent / 'second_event_author'
ROOT = D.parent.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def identity(p):
    return {'path': str(p), 'bytes': p.stat().st_size, 'sha256': sha(p)}
PRE = 'e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734'
AUTHOR = '47868fa10d852a2c6e57b5600b0f761ccbed01969867c87f53e4cefb71850610'
assert sha(D/'PRE_COMPARISON_SEAL.json') == PRE
assert sha(A/'AUTHOR_SEAL.json') == AUTHOR
pre = json.loads((D/'PRE_COMPARISON_SEAL.json').read_text())
for row in pre['sources'] + pre['artifacts']:
    p = Path(row['path'])
    assert sha(p) == row['sha256'] and p.stat().st_size == row['bytes'], p
seal = json.loads((A/'AUTHOR_SEAL.json').read_text())
bindings = []
for name, expected in seal['files'].items():
    p = A/name
    assert sha(p) == expected, p
    bindings.append(identity(p))
for name, expected in seal['dependencies'].items():
    p = ROOT/name
    assert sha(p) == expected, p
    bindings.append(identity(p))

receipts = []
for prefix, script, result, expected in (
    ('PROBE','second_event_probe.py','SECOND_EVENT_PROBE_RESULTS.json',0),
    ('VALIDATION','second_event_validation.py','SECOND_EVENT_VALIDATION_RESULTS.json',0),
    ('REFINEMENT','quadrature_refinement.py','QUADRATURE_REFINEMENT_RESULTS.json',0),
    ('RESOLUTION_FAILURE_REPRODUCTION','quadrature_resolution_failure.py',None,1)):
    r = json.loads((A/(prefix+'_RUN_RECEIPT.json')).read_text())
    assert r['source_sha256'] == sha(A/script) and r['exit_code'] == expected
    if result:
        assert (A/(prefix+'.stdout.log')).read_bytes() == (A/result).read_bytes()
        assert not (A/(prefix+'.stderr.log')).read_bytes()
        assert json.loads((A/result).read_text())['source_sha256'] == sha(A/script)
    else:
        assert 'AssertionError' in (A/(prefix+'.stderr.log')).read_text()
        assert not (A/(prefix+'.stdout.log')).read_bytes()
    receipts.append({'prefix':prefix, **r})

# Reuse only the independently sealed scalar definitions, without executing
# their result-writing top level.  This is not a new blind reconstruction.
tree = ast.parse((D/'ring_survival_repaired.py').read_text())
defs = ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef)],type_ignores=[])
env = {'cmath':cmath, 'math':math}
exec(compile(defs, 'sealed_independent_scalar_definitions', 'exec'),env)
formula = env['formula']

def gram(paths):
    sectors = defaultdict(lambda:defaultdict(int))
    for q, shift, amp in paths: sectors[q][shift] += amp
    result = defaultdict(int)
    for terms in sectors.values():
        for x,a in terms.items():
            for y,b in terms.items(): result[tuple(v-u for u,v in zip(x,y))] += a*b
    return {s:c for s,c in result.items() if c}

# Complete integer-shift paths, rather than angular sampling, establish the
# newly reviewed first-sector H2/H4 constants and all first-mark Grams.
edges = [(x,(x+1)%8) for x in range(8)]
aset = set(range(0,8,2)); q0 = tuple(int(x in aset) for x in range(8)); zero=(0,)*8
one = list(hops(q0,edges)); two=[]
for q,s,a in one:
    for out,z,b in hops(q,edges):
        if sum(not out[x] for x in aset)==2: two.append((out,add_shift(s,z),a*b))
assert gram(one)=={zero:8} and gram(two)=={zero:80}
first_grams=[]
for edge in range(8):
    for charge in (-1,1,None):
        g=gram(list(birth_paths(q0,edges,edge,charge)))
        assert g=={zero:2 if charge is None else 1}
        first_grams.append({'edge':list(edges[edge]),'charge':charge,'constant_Gram':g[zero]})
first_sector={'one_hop_paths':len(one),'two_hop_paths':len(two),
              'A_dagger_A':8,'Z_dagger_Z':80,'H2':-8,'H4':24,
              'all_first_mark_grams':first_grams}

all_mark_weights=[]
for theta in (.193,.877,2.091):
    basis,H2,H4,G,_,_=ring_operators(4,theta)
    ev,vec=np.linalg.eigh(H2); flat=vec[:,abs(ev+4)<1e-9]
    assert flat.shape[1]==12
    phases=np.zeros(8);phases[-1]=theta
    rows=[]
    for edge in range(8):
        for charge in (-1,1,None):
            psi=birth_matrix([q0],basis,edges,phases,edge,charge)[:,0]
            psi/=np.linalg.norm(psi)
            weight=float(np.linalg.norm(flat.conj().T@psi)**2)
            assert abs(weight-.5)<3e-12
            rows.append({'edge':list(edges[edge]),'charge':charge,'flat_weight':weight})
    all_mark_weights.append({'theta':theta,'marks':rows})

k,t,s=sp.symbols('k t s',positive=True)
S=(sp.exp(-2*k*s)+sp.exp(-4*k*s))/2
P4=sp.exp(-16*k*t)
P6=sp.integrate(16*k*sp.exp(-16*k*(t-s))*S,(s,0,t))
claimed6=sp.Rational(4,7)*sp.exp(-2*k*t)+sp.Rational(2,3)*sp.exp(-4*k*t)-sp.Rational(26,21)*sp.exp(-16*k*t)
claimed8=1-sp.Rational(4,7)*sp.exp(-2*k*t)-sp.Rational(2,3)*sp.exp(-4*k*t)+sp.Rational(5,21)*sp.exp(-16*k*t)
assert sp.simplify(P6-claimed6)==0 and sp.simplify(P4+claimed6+claimed8-1)==0
count_control={'P4':str(P4),'P6_from_convolution':str(sp.simplify(P6)),
               'P8':str(claimed8),'normalization_exact':True}

probe=json.loads((A/'SECOND_EVENT_PROBE_RESULTS.json').read_text())
validation=json.loads((A/'SECOND_EVENT_VALIDATION_RESULTS.json').read_text())
refinement=json.loads((A/'QUADRATURE_REFINEMENT_RESULTS.json').read_text())
extra=json.loads((A/'ADDITIONAL_ALGEBRA_PROBES.json').read_text())

# Exact author Laurent coefficients are compared with our frozen independent
# normalized coefficients, including signs, every nonzero mark, and zeros.
owncube=json.loads((D/'CUBE_GRAM_RESULTS.json').read_text())
assert probe['cube_exact_composition']['edges']==owncube['edge_order']
cube_poly_rows=[]
for r in probe['cube_exact_composition']['rows']:
    own=next(x for x in owncube['rows'] if x['first_instrument']==('first_coherent' if r['coherent_first'] else 'first_plus'))
    norm=r['first_norm_squared'];assert norm==own['first_norm_squared']
    raw={(tuple(x['edge']),x['sigma']):x for x in r['marked']}
    checked=0
    for x in own['second_marked_grams']:
        if x['new_charge_at_tail']=='coherent':continue
        a=raw.get((tuple(x['edge']),x['new_charge_at_tail']))
        p={} if a is None else {tuple(v['electric_shift']):Fraction(v['coefficient'],norm) for v in a['raw_two_mark_norm_polynomial']}
        q={tuple(v['field_shift']):Fraction(v['coefficient']) for v in x['gram']}
        assert p==q,(x,p,q);checked+=1
    actual={tuple(v['electric_shift']):Fraction(v['coefficient'],norm) for v in r['raw_total_norm_polynomial']}
    independent={tuple(v['field_shift']):Fraction(v['coefficient']) for v in own['total_gram']}
    assert actual==independent and r['predicted_polynomial_equal']
    cube_poly_rows.append({'coherent_first':r['coherent_first'],'all_resolved_marks_checked':checked,
                          'exact_total_equal':True,'normalized_total':{str(s):str(c) for s,c in actual.items()}})

# All saved ring-survival numbers, not merely the PASS status, compared with
# the exact independent scalar formula.  Scalar formula needs no averaging.
ring_rows=[];max_scalar_error=0.
for r in probe['ring_controls']:
    theta=r['theta'];basis,H2,H4,G,_,_=ring_operators(4,theta)
    vals,vec=np.linalg.eigh(H2); groups=[]
    for i,v in enumerate(vals):
        if not groups or abs(v-vals[groups[-1][0]])>1e-8:groups.append([i])
        else:groups[-1].append(i)
    flat=vec[:,abs(vals+4)<1e-8];P0=flat@flat.conj().T
    Gbar=sum((vec[:,g]@(vec[:,g].conj().T@G@vec[:,g])@vec[:,g].conj().T for g in groups),start=np.zeros_like(G))
    Bocc=[[j for j in range(4) if q[2*j+1]] for q in basis]
    Qadj=np.diag([int((b[1]-b[0])%4 in (1,3)) for b in Bocc])
    assert abs(np.linalg.norm(G-4*Qadj)-r['Gamma_identity_error'])<1e-10
    assert len(groups)==r['distinct_energy_count'] and flat.shape[1]==r['flat_dimension']
    serr=float(np.linalg.norm(Gbar-2*np.eye(36)-2*P0))
    assert abs(serr-r['secular_Gamma_proposed_error'])<1e-10
    for x in r['outputs']:
        coherent=x['coherent']; exceptional=flat.shape[1]!=12
        b=(1+math.cos(theta))/6 if coherent else 1/6
        weight=.5+(b/4 if exceptional else 0)
        assert abs(weight-x['flat_weight'])<1e-10 and abs(x['initial_hazard_over_kappa']-4)<1e-11
        for row in x['rows']:
            time=row['t'];averaged=weight*math.exp(-2.8*time)+(1-weight)*math.exp(-1.4*time)
            mixture=.5*(math.exp(-2.8*time)+math.exp(-1.4*time))
            assert abs(averaged-row['averaged_survival'])<3e-11
            assert abs(mixture-row['proposed_survival'])<3e-14
            for y in row['finite_eta']:
                exact=formula(theta,y['eta'],1.3,.7,time,coherent)
                error=abs(exact-y['survival']);max_scalar_error=max(max_scalar_error,error)
                assert error<3e-11,(theta,coherent,time,y,error)
                ring_rows.append({'theta':theta,'coherent':coherent,'time':time,'eta':y['eta'],
                                  'author':y['survival'],'independent_exact_formula':exact,'error':error})

fields={'integer_flux_0':lambda x:1.,'plus_adjacent_flux':lambda x:1+math.cos(x),'minus_adjacent_flux':lambda x:1-math.cos(x)}
quad_rows=[];max_quad_error=0.
for r in validation['quadrature_rows']:
    values=[fields[r['normalizable_field']](x)*formula(x,r['eta'],1.3,.7,r['t'],r['coherent_first'])
            for x in 2*math.pi*(np.arange(r['grid'])+.5)/r['grid']]
    exact=float(np.mean(values)); error=abs(exact-r['survival']);max_quad_error=max(max_quad_error,error)
    limit=.5*(math.exp(-1.4*r['t'])+math.exp(-2.8*r['t']))
    assert error<3e-11 and abs(limit-r['limiting_survival'])<1e-14
    assert abs(abs(exact-limit)-r['error'])<3e-11
    quad_rows.append({**r,'independent_same_grid':exact,'reconstruction_error':error})
for r in validation['first_sector']:
    assert r['H2']==-8 and abs(r['H4']-24)<1e-12 and r['resolved_first_total_loss_over_kappa']==16
assert validation['generic_ring_angles']==[r['theta'] for r in probe['ring_controls'] if r['flat_dimension']==12]
assert validation['exceptional_ring_angles_preserved']==[r['theta'] for r in probe['ring_controls'] if r['flat_dimension']==14]
refined=[]
for r in refinement['rows']:
    vals=[]
    for coherent in (False,True):
        vals.append([float(np.mean([density(x)*formula(x,320,1.3,.7,.7,coherent)
                    for x in 2*math.pi*(np.arange(r['grid'])+.5)/r['grid']])) for density in fields.values()])
    error=float(np.max(abs(np.array(vals)-r['survivals'])))
    assert error<3e-11
    refined.append({'grid':r['grid'],'author':r['survivals'],'independent':vals,'max_error':error})
assert (refinement['eta'],refinement['t'],refinement['delta'],refinement['kappa'])==(320,.7,1.3,.7)
assert refinement['instrument_order']==['resolved','coherent'] and refinement['field_order']==list(fields)
rdiff=float(np.max(abs(np.array(refinement['rows'][0]['survivals'])-refinement['rows'][1]['survivals'])))
assert rdiff==refinement['max_grid_difference'] and rdiff<refinement['declared_resolution_tolerance']==1e-8
bad=[]
for r in validation['quadrature_rows']:
    if r['grid']!=256:continue
    old=next(x for x in validation['quadrature_rows'] if x['grid']==128 and all(x[k]==r[k] for k in ('coherent_first','eta','t','normalizable_field')))
    diff=abs(r['survival']-old['survival'])
    if diff>=1e-8:bad.append({'instrument':r['coherent_first'],'eta':r['eta'],'time':r['t'],'field':r['normalizable_field'],'difference':diff})
assert bad

# Independent generic legal-hop construction also checks every saved cube
# exploratory scalar; these checks confer no ordinary-time cube theorem.
cube_edges=[(u,v) for u in range(8) for v in range(u+1,8) if (u^v).bit_count()==1]
cube_A={0,3,5,6};bases=[charge_basis(8,cube_A,6,4,w) for w in range(3)]
terminal=charge_basis(8,cube_A,8,4,0);initial=tuple(int(x in cube_A) for x in range(8));cube_rows=[]
for r in probe['cube_controls']:
    phases=np.zeros(12);phases[cube_edges.index((0,2))]=r['phi']
    hop=hopping_matrix(bases[0],bases[1],cube_edges,phases)
    Z=hopping_matrix(bases[1],bases[2],cube_edges,phases)@hop
    M=hop.conj().T@hop;H2=-M;H4=M@M-Z.conj().T@Z/2
    jumps=[birth_matrix(bases[0],terminal,cube_edges,phases,e,c) for e in range(12) for c in (-1,1)]
    G=sum((x.conj().T@x for x in jumps),start=np.zeros_like(H2))
    vals,vec=np.linalg.eigh(H2);groups=[]
    for i,v in enumerate(vals):
        if not groups or abs(v-vals[groups[-1][0]])>1e-8:groups.append([i])
        else:groups[-1].append(i)
    Gbar=sum((vec[:,g]@(vec[:,g].conj().T@G@vec[:,g])@vec[:,g].conj().T for g in groups),start=np.zeros_like(G))
    assert [len(g) for g in groups]==r['block_dimensions'] and len(groups)==r['distinct_energy_count']
    comm=float(np.linalg.norm(H2@H4-H4@H2));assert abs(comm-r['commutator_H2_H4_norm'])<1e-10
    outs=[]
    for x in r['outputs']:
        psi=birth_matrix([initial],bases[0],cube_edges,phases,0,None if x['coherent'] else 1)[:,0]
        psi/=np.linalg.norm(psi)
        calc={'hazard':float(np.vdot(psi,G@psi).real),'proposed_hazard':8+2*math.cos(r['phi']),
              'averaged_initial_hazard':float(np.vdot(psi,Gbar@psi).real),'H2_mean':float(np.vdot(psi,H2@psi).real),
              'Gamma_extrema':np.linalg.eigvalsh(G)[[0,-1]].tolist(),
              'secular_Gamma_extrema':np.linalg.eigvalsh(Gbar)[[0,-1]].tolist()}
        err=max(float(np.max(abs(np.array(v)-x[key]))) for key,v in calc.items())
        assert err<2e-9,(r['phi'],x,calc,err)
        outs.append({'coherent':x['coherent'],'independent':calc,'max_author_difference':err})
    cube_rows.append({'phi':r['phi'],'block_dimensions':[len(g) for g in groups],
                      'commutator_H2_H4_norm':comm,'outputs':outs})

rejected=[]
for theta in (0.,.37,1.19):
    _,H2,H4,_,_,_=ring_operators(4,theta)
    rejected.append({'theta':theta,'commutator_norm':float(np.linalg.norm(H2@H4-H4@H2)),
                     'rejected_linear_ansatz_residual':float(np.linalg.norm(H4+4*H2+4*np.eye(36)))})
assert all(r['commutator_norm']<1e-10 and abs(r['rejected_linear_ansatz_residual']-math.sqrt(96))<1e-10 for r in rejected)
assert extra['rejected_guess']=='H4 = -4 H2 - 4 I'
assert abs(extra['residual_Frobenius_norm_at_0_and_0.37']-math.sqrt(96))<1e-11
assert extra['H4_diagonal']==12 and max(extra['ring8_H2_H4_commutator_norms'].values())<1e-10

out={'status':'bounded post-source comparison; no author builder executed, no audit status',
     'PRE_sha256':PRE,'PRE_source_rows':len(pre['sources']),'PRE_artifact_rows':len(pre['artifacts']),
     'author_seal_sha256':AUTHOR,'authenticated_author_sources_and_dependencies':bindings,
     'author_execution_receipts':receipts,
     'author_status_and_scope_text':{'probe_status':probe['status'],'probe_scope':probe['scope'],
                                    'validation_status':validation['status'],'refinement_scope':refinement['scope'],
                                    'additional_probes':extra},
     'first_sector_exact_paths':first_sector,'all_first_mark_projector_controls':all_mark_weights,
     'count_convolution':count_control,'cube_exact_polynomial_comparison':cube_poly_rows,
     'ring_finite_eta_saved_values':ring_rows,'max_ring_formula_difference':max_scalar_error,
     'all_author_original_quadrature_rows':quad_rows,'max_quadrature_formula_difference':max_quad_error,
     'refined_quadrature_comparison':refined,'author_refinement_grid_difference':rdiff,
     'preserved_underresolution_cases':bad,'cube_exploratory_scalars':cube_rows,
     'rejected_H4_ansatz_independently_recomputed':rejected,
     'limits':['Saved outputs are authenticated and independently recomputed selectively, not author production reruns.',
               'Author averaging claim is compact-time, fixed normalizable input; independent PRE exact finite-eta, all-time, and mean extensions are separate.',
               'Cube exploratory fiber results are not a normalizable ordinary-time waiting/readout theorem.',
               'No finite-spin packet, checkpoint, plans, or external literature was opened for this comparison.']}
target=D/'COMPARISON_RESULTS.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
