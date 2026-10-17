#!/usr/bin/env python3
"""Exact bounded corroboration of a real, positive local preparation route.

This does not import or execute any inherited checker, integrate dynamics,
certify scattering anew, or prove an interval by point sampling. Symbolic
kappa and exact rational coefficients check the new finite local identities.
The all-length and all-time claims have separate analytical proofs.
"""
import hashlib
import json
import platform
import sys
import time
from pathlib import Path

import sympy as sp

START = time.monotonic()
ROOT = Path(__file__).resolve().parent.parent
p = {k: sp.Rational(v) for k, v in json.loads(
    (ROOT / 'inputs/parameters.json').read_text())['exact_parameters'].items()}
kappa = sp.Symbol('kappa', positive=True)
J, E0 = p['J'], p['epsilon']
c = p['cos_k']**2-p['sin_k']**2
s = 2*p['cos_k']*p['sin_k']
d = 1+c+s
nu = -p['mu1']
kp = sp.Rational(1,10**8)
cR = 2*nu+2*kappa*d
cseed = E0+cR
r = 4*J+3*kappa*d
Ciso = cseed+r
beta = E0-kappa
Aiso = 4*J+4*kappa*d+beta
checks = []


def check(name, condition, detail=None):
    assert bool(condition), name
    checks.append({'name': name, 'passed': True, 'detail': detail})


def zero(x):
    if isinstance(x, sp.MatrixBase):
        return all(sp.simplify(v) == 0 for v in x)
    return sp.expand(x) == 0


def clean(a):
    return {key: sp.expand(v) for key, v in a.items() if sp.expand(v) != 0}


def add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0)+value
    return clean(out)


def scale(a, value):
    return clean({key: value*v for key, v in a.items()})


def pauli(*sites):
    return {tuple(sorted(sites)): sp.Integer(1)}


I = {(): sp.Integer(1)}


def number(i):
    return add(scale(I, sp.Rational(1,2)), scale(pauli((i,'Z')), -sp.Rational(1,2)))


def vacancy(i):
    return add(I, scale(number(i), -1))


def hop(i,j):
    return scale(add(pauli((i,'X'),(j,'X')), pauli((i,'Y'),(j,'Y'))), sp.Rational(1,2))


def density(i,j):
    return scale(add(I, scale(pauli((i,'Z')),-1), scale(pauli((j,'Z')),-1),
                     pauli((i,'Z'),(j,'Z'))), sp.Rational(1,4))


def controlled_flip(i,j):
    return scale(add(I, scale(pauli((i,'Z')),-1), pauli((j,'X')),
                     scale(pauli((i,'Z'),(j,'X')),-1)), sp.Rational(1,2))


def qblock(i,j,h,a):
    return add(scale(add(number(i),number(j)),a),scale(hop(i,j),h))


def apply(a, state):
    out = {}
    for word, value in a.items():
        dest, phase = state, sp.Integer(1)
        for index, letter in word:
            bit = (state >> index) & 1
            if letter == 'Z':
                phase *= 1-2*bit
            elif letter == 'X':
                dest ^= 1 << index
            elif letter == 'Y':
                dest ^= 1 << index
                phase *= sp.I*(1-2*bit)
            else:
                raise AssertionError('unknown Pauli')
        out[dest] = out.get(dest,0)+phase*value
    return clean(out)


def overlap(v,w):
    return sp.expand(sum(sp.conjugate(x)*w.get(b,0) for b,x in v.items()))


check('exact_trigonometry', c*c+s*s == 1)
check('positive_c_s_and_d', c>0 and s>0 and d<3)
check('all_family_onsite_coefficients_positive', E0-kp*d>0 and E0-kp>0,
      'affine decreasing in kappa; checked at exact upper endpoint')
check('isolation_norm_sum_less_than_one_seventh', Aiso.subs(kappa,kp)<sp.Rational(1,7))
check('supported_shift_less_than_one_eighth', r.subs(kappa,kp)<sp.Rational(1,8))

# At most four-dimensional dense matrices. Full-qubit positive cells.
X = sp.Matrix([[0,1],[1,0]])
Z = sp.diag(1,-1)
Id2 = sp.eye(2)
K = 2*sp.eye(4)+sp.kronecker_product(Z,Z)
W = ((9+12*sp.I)*sp.eye(4)+(-16+12*sp.I)*sp.kronecker_product(X,X))/25
check('literal_K_W_unitarity_and_commutation', zero(W.H*W-sp.eye(4)) and zero(K*W-W*K))
w, lam = sp.symbols('w lam', positive=True)
cell = sp.Matrix([[0,0,0,0],[0,w,w,0],[0,w,w,0],[0,0,0,2*w]])
cell_minus = cell.copy()
cell_minus[1,2] = cell_minus[2,1] = -w
poly = lam**2*(lam-2*w)**2
check('positive_real_cells_and_complements_full_four_space',
      all(zero((mat-lam*sp.eye(4)).det()-poly)
          for mat in (cell,cell_minus,2*w*sp.eye(4)-cell,2*w*sp.eye(4)-cell_minus)),
      'spectrum 0,0,2w,2w; w>=0')

# Unit-window pulse algebra on the three-position core, basis e0,m,e1.
theta1, theta2, theta3 = sp.pi/4, sp.pi/2, sp.pi/2
E01 = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
E12 = sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])
P1, P2, P3 = sp.eye(3)+E01, sp.eye(3)-E12, sp.diag(0,0,1)
U1 = sp.exp(-sp.I*theta1)*(sp.eye(3)+(sp.cos(theta1)-1)*E01**2-sp.I*sp.sin(theta1)*E01)
U2 = sp.exp(-sp.I*theta2)*(sp.eye(3)+(sp.cos(theta2)-1)*E12**2+sp.I*sp.sin(theta2)*E12)
U3 = sp.diag(1,1,sp.exp(-sp.I*theta3))
seed = sp.Matrix([1,0,0])
chiral = sp.Matrix([1,0,-sp.I])/sp.sqrt(2)
check('three_real_positive_pulses_exact_chiral_state_and_common_phase',
      zero(U3*U2*U1*seed-sp.exp(-3*sp.I*sp.pi/4)*chiral))
check('pulse_generators_positive_on_core',
      sorted(P1.eigenvals()) == [0,1,2] and sorted(P2.eigenvals()) == [0,1,2]
      and sorted(P3.eigenvals()) == [0,1])
wrongU2 = sp.exp(-sp.I*theta2)*(sp.eye(3)+(sp.cos(theta2)-1)*E12**2-sp.I*sp.sin(theta2)*E12)
wrong = sp.simplify(sp.exp(3*sp.I*sp.pi/4)*U3*wrongU2*U1*seed)
check('wrong_exchange_sign_selects_orthogonal_chirality', zero((chiral.H*wrong)[0]) and zero(wrong.H*wrong-sp.eye(1)))
x = sp.Symbol('x', real=True)
q = 30*x*x*(1-x)**2
up = 3*x*x-2*x**3
check('pulse_area_and_C1_endpoints', sp.integrate(q,(x,0,1))==1 and
      all(v.subs(x,j)==0 for v in (q,sp.diff(q,x)) for j in (0,1)))
check('cubic_ramp_areas_and_C1_endpoints', sp.integrate(up,(x,0,1))==sp.Rational(1,2)
      and up.subs(x,0)==0 and up.subs(x,1)==1 and
      all(sp.diff(up,x).subs(x,j)==0 for j in (0,1)))
check('exact_pulse_peak_and_slew', q.subs(x,sp.Rational(1,2))==sp.Rational(15,8)
      and zero(sp.diff(q,x).subs(x,(3-sp.sqrt(3))/6)-10*sp.sqrt(3)/3))
check('ramp_derivative_bound', sp.diff(up,x).subs(x,sp.Rational(1,2))==sp.Rational(3,2))
check('finite_control_load_and_work_ceilings',
      sp.Rational(1,7)+45*sp.Rational(22,7)/16 < 9 and
      10*sp.Rational(22,7)*sp.Rational(7,4)/3 < 20 and
      2*sp.Rational(1,7)+165*sp.Rational(22,7)/16 < 33,
      'uses elementary pi<22/7 and sqrt(3)<7/4, not floating-point ceilings')

fixtures = []
for M in (16,17):
    old1,old2,A,B,e0,e1 = range(6)
    clock = lambda n,q: 6+q*M+n
    m = clock(14,0)
    blocks = []
    loads = {}

    def block(name, op, norm, support):
        blocks.append((name,op,norm,tuple(support)))
        for site in support:
            loads[site] = loads.get(site,0)+norm

    block('DeltaA',scale(number(A),p['DeltaA']),p['DeltaA'],(A,))
    block('DeltaB',scale(number(B),p['DeltaB']),p['DeltaB'],(B,))
    block('source_hop',qblock(A,B,-p['t'],p['t']),2*p['t'],(A,B))
    block('source_density',scale(density(A,B),p['u']),p['u'],(A,B))
    for source,old,g in ((A,old1,p['gA']),(B,old2,p['gB'])):
        block('old_contact',scale(controlled_flip(source,old),g),2*g,(source,old))
    for rail in (0,1):
        for n in range(M-1):
            block('clock_bond',qblock(clock(n,rail),clock(n+1,rail),-J,J),2*J,(clock(n,rail),clock(n+1,rail)))
        for n in (0,M-1):
            block('clock_endpoint',scale(number(clock(n,rail)),J),J,(clock(n,rail),))
        for n,source,lc in ((0,A,p['lambdaA']),(1,B,p['lambdaB'])):
            block('clock_source',scale(controlled_flip(clock(n,rail),source),lc),2*lc,(clock(n,rail),source))
        block('mu0',scale(number(clock(0,rail)),p['mu0']),p['mu0'],(clock(0,rail),))
        block('nu_vacancy',scale(vacancy(clock(1,rail)),nu),nu,(clock(1,rail),))
    edges = [(e0,clock(12,0),kappa,kappa), (e1,clock(12,1),kappa,kappa),
             (e0,m,-kappa*c,kappa*c), (e1,clock(14,1),-kappa*c,kappa*c),
             (e1,m,kappa*s,kappa*s), (e0,clock(14,1),-kappa*s,kappa*s)]
    for i,j,h,a in edges:
        block('emitter_bond',qblock(i,j,h,a),2*a,(i,j))
    for emit in (e0,e1):
        block('emitter_onsite',scale(number(emit),E0-kappa*d),E0-kappa*d,(emit,))
    for rail in (0,1):
        block('emitter_vacancy12',scale(vacancy(clock(12,rail)),kappa),kappa,(clock(12,rail),))
        block('emitter_vacancy14',scale(vacancy(clock(14,rail)),kappa*(c+s)),kappa*(c+s),(clock(14,rail),))
    oldK = add(scale(I,2),pauli((old1,'Z'),(old2,'Z')))
    HR = add(oldK,*(b[1] for b in blocks))
    isolated_edges = edges+[(m,clock(13,0),-J,J),(m,clock(15,0),-J,J)]
    complements = [add(scale(I,2*a),scale(qblock(i,j,h,a),-1)) for i,j,h,a in isolated_edges]
    R = add(*complements,scale(number(m),beta))
    Hiso = add(HR,R)
    columns = []
    exits = []
    for oldbits in range(4):
        old_energy = 2+(1-2*((oldbits>>old1)&1))*(1-2*((oldbits>>old2)&1))
        for position in (e0,m,e1):
            basis = oldbits | (1<<position)
            result = apply(Hiso,basis)
            check(f'M{M}_core_old{oldbits}_position{position}_full_Pauli_action',
                  clean(add(result,{basis: -old_energy-Ciso})) == {})
            columns.append(basis)
        old_exits = []
        for emit in (e0,e1):
            basis = oldbits | (1<<emit)
            residual = add(apply(HR,basis),{basis:-old_energy-cseed})
            residual_R = add(apply(R,basis),{basis:-r})
            check(f'M{M}_seed_old{oldbits}_emit{emit}_supported_residual',
                  add(residual,residual_R)=={})
            old_exits.append(residual)
        gram = sp.Matrix([[overlap(v,w) for w in old_exits] for v in old_exits])
        check(f'M{M}_old{oldbits}_complete_rail_exit_Gram',zero(gram-2*kappa*kappa*sp.eye(2)))
        exits.append(gram)
    omitted_pin = add(HR,*complements)
    bad = apply(omitted_pin,1<<m)
    check(f'M{M}_omit_pin_nonflat_discriminator', bad.get(1<<m)-(3+Ciso)==-beta)
    alphaR = 2+(p['DeltaA']+p['DeltaB']+p['gA']+p['gB'])/2+p['t']+p['u']/4+2*J*M+p['lambdaA']+p['lambdaB']+p['mu0']+nu+E0+2*kappa*d
    alphaIso = 2*J+2*kappa*d+beta/2
    total_norm = p['DeltaA']+p['DeltaB']+2*p['t']+p['u']+2*(p['gA']+p['gB'])+4*J*M+4*(p['lambdaA']+p['lambdaB'])+2*p['mu0']+2*nu+2*E0+4*kappa*d
    check(f'M{M}_full_space_identity_coefficients',zero(HR[()]-alphaR) and zero(R[()]-alphaIso))
    check(f'M{M}_positive_runtime_block_counts',len(blocks)==2*M+28 and sum(len(b[3])==2 for b in blocks)==2*M+12)
    check(f'M{M}_runtime_positive_norm_sum',zero(sum(b[2] for b in blocks)-total_norm))
    rload = {}
    for i,j,h,a in isolated_edges:
        rload[i] = rload.get(i,0)+2*a
        rload[j] = rload.get(j,0)+2*a
    rload[m] += beta
    check(f'M{M}_isolation_positive_norm_sum',zero(sum(2*a for i,j,h,a in isolated_edges)+beta-Aiso))
    check(f'M{M}_old_source_untouched',all(rload.get(i,0)==0 for i in (old1,old2,A,B)))
    check(f'M{M}_old_added_incident_cap',loads[old1]<2 and loads[old2]<2)
    check(f'M{M}_emitter_runtime_incident_loads',zero(loads[e0]-E0-kappa*d) and zero(loads[e1]-E0-kappa*d))
    check(f'M{M}_mediator_runtime_incident_load',zero(loads[m]-4*J-3*kappa*(c+s)))
    check(f'M{M}_combined_mediator_load',zero(loads[m]+rload[m]-(8*J+E0+5*kappa*(c+s)-kappa)))
    check(f'M{M}_combined_emitter_loads',all(zero(loads[e]+rload[e]-E0-3*kappa*d) for e in (e0,e1)))
    fixtures.append({'clock_sites_per_rail':M,'physical_qubits':2*M+6,
                     'dense_Hilbert_space_allocated':False,'maximum_dense_dimension':4,
                     'core_seed_columns':len(columns),'Pauli_terms_runtime':len(HR),
                     'Pauli_terms_isolator':len(R),'runtime_blocks_excluding_K':len(blocks),
                     'alpha_R':str(alphaR),'alpha_isolator':str(alphaIso),
                     'runtime_block_norm_sum_excluding_K':str(total_norm),
                     'source_A_load':str(loads[A]),'source_B_load':str(loads[B])})

coordinates = {'e0':(8,2,1),'e1':(9,3,1),'m':(9,2,1),
               'c12,0':(8,1,1),'c12,1':(9,3,0),'c14,1':(8,3,1),
               'c13,0':(9,1,1),'c15,0':(10,2,1)}
local_edges = [('e0','c12,0'),('e1','c12,1'),('e0','m'),('e1','c14,1'),
               ('e1','m'),('e0','c14,1'),('m','c13,0'),('m','c15,0')]
check('all_eight_isolation_edges_and_pulse_edges_ordinary_NN',all(
      sum(abs(a-b) for a,b in zip(coordinates[i],coordinates[j]))==1 for i,j in local_edges))
check('eight_local_sites_distinct',len(set(coordinates.values()))==8)
check('five_unit_supported_scalar_phase',zero(2*(cseed+r/2)+3*Ciso-(5*cseed+4*r)))
check('full_identity_integrated_pulse_scalar',sp.Rational(3,2)*(theta1+theta2)+theta3/2==11*sp.pi/8)
check('ramp_error_and_complete_trace_ceiling',2*kp<sp.Rational(2,10**8)+sp.Rational(1,10**30)
      and 2*(sp.Rational(4832,10**6)+2*kp)==sp.Rational(966404,10**8),
      'sqrt(2)*kappa < 2*kappa <= 2e-8; final trace ceiling .00966404')

out = {
  'status':'exact local corroboration passed; conditional theorem still requires separate review',
  'checks':checks,'fixtures':fixtures,
  'exact_constants':{'c':str(c),'s':str(s),'d':str(d),'E0':str(E0),
                     'cR':str(cR),'cseed':str(cseed),'r':str(r),'Ciso':str(Ciso),'Aiso':str(Aiso),
                     'setup_error_upper':'sqrt(2)*kappa',
                     'setup_scalar':'5*cseed+4*r+3*pi/4'},
  'limits':{'cpu_soft_hard_seconds':[20,20],'external_wall_seconds':30,
            'max_dense_dimension':4,'sparse_clock_lengths':[16,17],
            'max_physical_qubits':40,'seed_columns_per_fixture':12,
            'scientific_point_grids':0,'optimizers':0,'quadrature':0,'dynamics_steps':0,
            'inherited_scientific_checker_replays':0,'symbolic_kappa':True},
  'runtime':{'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
             'sympy':sp.__version__,'elapsed_seconds_after_import':time.monotonic()-START},
  'executed_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'scope':'Finite exact corroboration and discriminators; not an independent scattering replay or a substitute for all-M analytical proof.'
}
print(json.dumps(out,indent=2))
