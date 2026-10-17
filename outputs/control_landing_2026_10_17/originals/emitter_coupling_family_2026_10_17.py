"""Portable author-checker replay for the conditional emitter coupling family.

Review, qualification and execution status are recorded in the paired input
packet. Importing this module executes no scientific body and changes no CPU
limit. Only main() starts the declared shared CPU20/wall30 calculation.
Historical evidence remains historical; scalar replay is not analytical or
independent review of the theorem. No parent scientific programs are imported.
"""
from pathlib import Path
import hashlib
import json
import resource
import time

AUDIT_TIMEOUT_SEC = 30
REPO = Path(__file__).resolve().parents[1]
INPUT_ROOT = REPO / 'outputs/emitter_coupling_family_2026_10_17_inputs'

class FrozenInputs:
    """Resolve only declared logical identities to hash-checked local bytes.

    Historical absolute strings are lookup keys, never filesystem fallbacks.
    read_text decodes the exact checked bytes as UTF-8. The class has no write
    method, no network access and no directory or undeclared-path fallback.
    """

    def __init__(self, repo, table_path):
        self.repo = Path(repo).resolve()
        self.table = json.loads(Path(table_path).read_text(encoding='utf-8'))
        self.reads = []

    def read_bytes(self, role, logical):
        row = self.table['roles'][role]['aliases'][str(logical)]
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts and rel.as_posix() == row['path']
        path = self.repo / rel
        assert path.is_file() and not path.is_symlink(), row['path']
        assert not any(parent.is_symlink() for parent in path.parents if parent != self.repo and self.repo in parent.parents)
        path.resolve().relative_to(self.repo)
        raw = path.read_bytes()
        assert len(raw) == row['bytes'], row['path']
        assert hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']
        self.reads.append({'role': role, 'logical_identity': str(logical), 'path': row['path'], 'sha256': row['sha256']})
        return raw

    def read_text(self, role, logical):
        return self.read_bytes(role, logical).decode('utf-8')

    def original_program_bytes(self, role):
        return self.read_bytes(role, '__original_program__')

    def shared_limits(self):
        return {'cpu_soft_hard_seconds': list(resource.getrlimit(resource.RLIMIT_CPU)),
                'external_wall_cap_seconds': AUDIT_TIMEOUT_SEC,
                'wall_enforcement': 'Required canonical runner_cache execution; this class does not enforce wall time.'}

    def execution_metadata(self, role):
        return {'source_role': role,
                'historical_source_run_limits': self.table['roles'][role]['historical_limits'],
                'actual_shared_process_limits': self.shared_limits(),
                'source_statement_scope': 'Original report scope/limitations strings retain their historical scientific meaning. This is a portable replay, not a new review.',
                'original_program_sha256': self.table['roles'][role]['aliases']['__original_program__']['sha256']}


def verify_artifacts():
    manifest = json.loads((INPUT_ROOT / 'ARTIFACT_MANIFEST.json').read_text())
    for row in manifest['files']:
        rel = Path(row['path'])
        assert not rel.is_absolute() and '..' not in rel.parts
        path = REPO / rel
        assert path.is_file() and not path.is_symlink(), row['path']
        path.resolve().relative_to(REPO)
        raw = path.read_bytes()
        assert len(raw) == row['bytes'] and hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']


def run_family_author(inputs):
    'Exact scalar corroboration for a proposed increased-kappa emitter family.\n\nThis is author evidence, not an independent review or an interval proof by\nsampling. Every parameter-dependent comparison is made with a declared\nmonotone majorant at KMAX; the proof must justify those majorants. No parent\nscientific program is imported. There is no quadrature, matrix or dynamics.\n'

    from pathlib import Path

    from fractions import Fraction as F

    import hashlib, json, os, platform, resource, sys, time

    START=time.monotonic()

    import sympy as sp

    checks=[]

    def show(x):
        x=F(x)
        return {'rational':str(x),'display_only':float(x)}

    def lt(name,left,right):
        left,right=F(left),F(right)
        assert left<right, (name,str(left),str(right))
        checks.append({'name':name,'left':show(left),'relation':'<','right':show(right)})

    def eq(name,left,right):
        assert left==right,(name,left,right)
        checks.append({'name':name,'relation':'=','value':str(left)})

    data=json.loads(inputs.read_text('family_author', 'inputs/interval.json'))

    p={k:F(v) for k,v in data['exact_parameters'].items()}

    J=p['J']

    cs=p['cos_k']

    sn=p['sin_k']

    E0=p['epsilon']

    eq('rational_center_circle',cs*cs+sn*sn,F(1))

    eq('rational_center_energy',E0,2*J*(1-cs))

    lo=F(1,10**12)

    hi=F(1,10**8)

    sigma=F(1,10**6)

    h=sigma/2

    v=F(1,40)

    r=F(1,7)

    rp=F(1,24)

    gap=F(9,50)

    L=12

    sin2=2*sn*cs

    cos2=cs*cs-sn*sn

    lt('band_in_larger_certified_band',sigma,F(1,1000))

    lt('positive_emitter_onsite_entire_family',2*hi,E0)

    lt('emitter_energy_below_bulk_width',E0,4*J)

    lt('bulk_band_width_below_old_splitting',4*J,2)

    lt('source_gap_covers_old_release_and_entire_band',2+4*J,min(p['DeltaA'],p['DeltaB']))

    lt('velocity_on_larger_inherited_band',v,2*J*(sn-F(1,1000)))

    lt('curvature_over_velocity',2*J/v,F(5,2))

    am=2*sigma

    bm=2*sin2-2*sigma

    bM=F(2)

    eta=am/bm

    delta=(1+r*r)*r**(L-1)

    wc=16*(1+r*r)*r**(L-2)

    wc1=(700*(1+r*r)+32*r*rp)*r**(L-2)+16*(L-2)*(1+r*r)*rp*r**(L-3)

    R0=F(166)

    A0=F(40)

    A1=F(100)

    T0=F(206)

    T1=F(2000)

    M16p=2*J/(1-r*r)

    R1=R0*R0*M16p

    lt('closed_transfer_smaller_than_open_envelope',delta,am)

    lt('open_formfactor_nonzero',F(3,2),bm)

    lt('tail_resolvent_derivative',R1,1710)

    lt('response_derivative',R1+A1,T1)

    gamma0=bm*bm/(4*J)

    lt('optical_lower_factor',19,gamma0)

    Sqq=2*(1+r*r)/gap+delta*delta*T0

    lt('closed_emitter_inverse_gap',F(1,6),gap-hi*hi*Sqq)

    sPQ=am*T0*delta

    sQP=delta*T0*bM

    xi_c=hi*hi*sPQ*6*sQP/gamma0

    xi=2*eta+xi_c

    lt('schur_imaginary_lower_factor',19,gamma0*(1-xi))

    lt('relative_denominator_below_one',xi,1)

    De_scaled=(1+6*hi*hi*sPQ)*(1+6*hi*hi*sQP)/19+6*hi*hi

    lt('full_emitter_inverse_scaled',De_scaled,F(1,18))

    lt('old_matching_inverse_in_diagonal_max',R0*hi*hi,F(1,18))

    aug_scaled=(1+R0*hi*bM)*(1+R0*hi*am)/18

    lt('augmented_matching_inverse_scaled',aug_scaled,F(1,17))

    eta_p=(eta+hi*hi*sPQ*6*wc/bm+xi)/(1-xi)

    lt('diagonal_common_profile_relative_error',eta_p,F(4,10**6))

    off=6*hi*wc+6*hi*hi*delta*T0*bM*(1+eta_p)

    lt('full_seed_off_diagonal_entry',off,F(1,10**14))

    m=F(1,10**8)

    M=F(1,10**7)

    G=F(52)

    G1=F(560)

    log_bound=80

    lt('cos_phase_and_cos_twok_above_three_fifths',F(3,5),cos2-2*sigma)

    lt('gamma_upper_from_trigonometric_enclosure',F(32,25)/v,G)

    lt('a_derivative_factor_positive',hi*hi*cos2/(J*J),F(1,2))

    lt('cos_phase_positive',0,cos2)

    lt('negative_endpoint_is_left_of_minus_m',m,v*h-160*hi*hi)

    lt('positive_endpoint_is_right_of_m',m,v*h-160*hi*hi)

    lt('whole_inner_interval_abs_x_below_M',2*J*h+160*hi*hi,M)

    log_argument=1+(M/(19*lo*lo))**2

    lt('log_bound_from_e_greater_than_8_over_3',log_argument,F(8,3)**log_bound)

    phase_deficit=2*hi*hi*G/m

    integral_deficit=2*hi*hi*G1*log_bound/v

    lt('arctan_lower_bracket_positive',phase_deficit+integral_deficit,3)

    eta_inner=h/(sin2-h)

    mass_loss=(phase_deficit+integral_deficit)/3+eta_inner*eta_inner

    mass_ceiling=F(7,20_000_000)

    lt('new_reference_mass_loss',mass_loss,mass_ceiling)

    lt('normalization_N_above_point99',F(99,100)**2,1-mass_ceiling)

    lt('normalization_sqrt_2pi_N_above_2_using_12_over_5',2,F(12,5)*F(99,100))

    seed_sq=2*(mass_ceiling+eta_p+off)

    seed_coarse=2*(mass_ceiling+F(4,10**6)+F(1,10**14))

    lt('complete_seed_overlap_squared',seed_sq,F(3,1000)**2)

    lt('simple_complete_seed_overlap_squared',seed_coarse,F(3,1000)**2)

    naive_variance=2*hi*hi/(v*h)**2

    eq('preserved_failed_naive_variance_substitution',naive_variance,F(32,25))

    eq('old_point_projection_variance_ceiling_at_hi',2*hi/(v*sigma),F(4,5))

    closed_reflection=6*hi*hi*T0*delta*wc+6*hi*hi*delta*delta*T0*T0*bM*(1+eta_p)*(4*J/bm)

    phase_error=2*eta+2*(1+eta)*eta_p+closed_reflection+4*eta*eta

    lt('complete_reflection_added_phase',phase_error,F(11,10**6))

    lt('free_transmission_nonvanishing',4*eta*eta,F(1,4))

    target_residual=F(176,10**15)

    gate_band_error=target_residual+702*sigma

    lt('complete_common_reflection_comparison',gate_band_error+phase_error,F(714,10**6))

    Sigma1=560+24*T0*bM+am*T1*bM+am*T0*24

    lt('Sigma_derivative',Sigma1,11000)

    De1=2*J+11000*hi*hi

    d=F(61,1000)

    lt('emitter_denominator_derivative',De1,d)

    diag1=2*J+hi*hi*(560+24*A0*bM+am*A1*bM+am*A0*24)

    lt('augmented_matching_derivative',max(M16p,diag1)+24*hi,F(63,1000))

    lt('drive_norm',bM+am+wc,3)

    lt('drive_derivative',2*L+2+700*am+(L*am+2)+wc1,30)

    lt('emitter_coordinate_norm_scaled',F(3,18),1)

    lt('emitter_coordinate_derivative_scaled',3*d/(18**2)+30*hi*hi/18,1)

    tail0=2*A0+T0*bM

    tail1=2*A1+2*A0+(L+1)*T0*bM+T1*bM+T0*24

    brow1=(L+2)*tail0+tail1

    contact1=2*1710+R0*24

    finite_row1=2*A1+2*L*A0+L*T0*bM+T1*bM+T0*24

    lt('finite_row_derivative',finite_row1,16000)

    lt('closed_tail_square_sum_root',1/(1-r*r),F(1011,1000)**2)

    lt('closed_tail_derivative_square_sum_root',(1+r*r)/(1-r*r)**3,F(21,20)**2)

    K0=R0*bM+2*tail0+L*(tail0+tail0)+tail0*F(1011,1000)

    K1=contact1+tail0+2*brow1+L*(16000+(L+1)*tail0+brow1)+tail1*F(1011,1000)+tail0*rp*F(21,20)

    lt('full_localized_K0',K0,20000)

    lt('full_localized_K1',K1,10**6)

    lt('complete_C0_scaled_by_kappa',31*hi+1+20000*hi,2)

    lt('complete_C1_scaled_by_kappa_cubed',(2700+10**6)*hi**3+1+20000*hi,2)

    lt('complete_Rprime_scaled_by_kappa_squared',700*hi*hi+brow1*hi*hi+tail0,1000)

    Df1=2*J+560*hi*hi

    lt('reference_denominator_derivative',Df1,d)

    lt('reference_profile_norm_scaled',F(2,19),1)

    lt('reference_profile_derivative_scaled',F(2*L+2,19)*hi*hi+2*d/(19**2),1)

    lt('F0_from_normalization_and_band_measure',2*sigma,F(1,500)**2)

    lt('outgoing_phase_t_derivative_scaled',F(720,19)*hi*hi+160*d/(19**2),1)

    lt('rho_derivative_scaled',2*hi*hi+4,5)

    rank_factor=(1+6*hi*hi*sPQ)*(1+6*hi*hi*sQP)/(1-xi)

    lt('rank_one_plus_closed_inverse_factor',rank_factor,2)

    lt('monotone_denominator_integral_hypothesis',560*hi*hi,v/2)

    lt('I2_scaled_integral',8/(19*v),17)

    lt('I3_scaled_integral',4/(361*v),F(1,2))

    lt('I1_Cauchy_Schwarz_scaled',34*sigma,1)

    a1=2/sigma+13

    F0=F(1,500)

    lt('F1_weighted_scaled',a1*hi+17*d,2)

    lt('incoming_A0_scaled',a1*hi+17*d+F(5,2)*F0*hi,3)

    phase_weighted_scaled=2*F0*hi+48960*hi*hi+320*d

    lt('outgoing_B0_scaled',a1*hi+17*d+phase_weighted_scaled+F(5,2)*F0*hi,23)

    lt('weighted_yprime_constant',3*d*36+180,187)

    lt('weighted_yprime_U',3*d*24+60,65)

    lt('weighted_yprime_U_squared',3*d*4,1)

    lt('weighted_localized_prefactor',1+20000*hi,2)

    lt('weighted_C0_constant_rounding',36*hi,1)

    lt('weighted_C1_constant_rounding',374*hi+18*10**6*hi*hi,1)

    lt('weighted_C1_U_rounding',6*10**6*hi,1)

    Dj_scaled=(236*a1+5518)*hi*hi+544*d*hi+6*d+1

    lt('weighted_localized_Dj_scaled',Dj_scaled,F(3,2))

    lt('two_columns_in_one_parity_square_sum',2*Dj_scaled**2,9)

    lt('sqrt_I2_scaled',17,25)

    lt('sqrt_I4_scaled',4/(v*19**3),F(4,25)**2)

    lt('sqrt_I6_scaled',3/(v*19**5),F(7,1000)**2)

    f2_scaled=5*a1*hi*hi+F(4,25)*d

    frho2_scaled=f2_scaled+(2+2880*F(4,25))*hi*hi+640*d*F(7,1000)

    lt('actual_f_L2_derivative_scaled',f2_scaled,F(1,100))

    lt('actual_f_rho_L2_derivative_scaled',frho2_scaled,F(3,10))

    time_scale=F(10**6)

    qin=F(1,100)/(v*time_scale)+2*J*sigma/v

    qout=F(3,10)/(v*time_scale)+2*J*sigma/v

    local=3/(F(12,5)*v*time_scale)

    moment_remainder=qin+qout+local

    complete=F(3,1000)+F(714,10**6)+moment_remainder

    lt('outgoing_normalization_at_family_onset',qout,F(1,2))

    lt('infinite_complete_error',complete,F(1,250))

    lt('finite_complete_error',complete+F(1,1000),F(1,200))

    T_hi=time_scale/(hi*hi)

    T_lo=time_scale/(lo*lo)

    M_hi=50*T_hi

    M_lo=50*T_lo

    lt('vT_condition_at_smallest_onset',1,v*T_hi)

    lt('finite_clock_distance_margin_at_smallest_clock',9,M_hi-L-1-19*(2*T_hi)*F(6,5))

    lt('elementary_boundary_exponential_ceiling',F(32,5)*F(3,8)**9,F(1,1000))

    Vmax=F(data['finite_horizon']['Vmax']['rational'])

    lt('old_gate_radius_from_full_internal_bounds',2*J+F(19,2)+Vmax,18)

    lt('emitter_decoupled_radius_about_same_center',F(19,2)+2*J,18)

    lt('coupled_radius_using_sqrt_two_less_two',18+2*hi,19)

    weighted_remainder=F(26,270000)+3/(F(12,5)*v*10**12)

    lt('weighted_fallback_normalization',F(23,270000),F(1,2))

    lt('weighted_fallback_complete',F(3,1000)+F(714,10**6)+weighted_remainder,F(1,250))

    k,c,j,kap=sp.symbols('k c j kap', real=True, nonzero=True)

    Sigma=-sp.I*(2-2*c*sp.exp(2*sp.I*k))/(2*j*sp.sin(k))

    re_sigma=sp.simplify(sp.re(sp.expand_complex(Sigma)))

    eq('exact_real_selfenergy_identity',sp.trigsimp(re_sigma+2*c*sp.cos(k)/j),0)

    gamma=sp.simplify(-sp.im(sp.expand_complex(Sigma)))

    eq('exact_optical_density_identity',sp.trigsimp(gamma-(2-2*c*sp.cos(2*k))/(2*j*sp.sin(k))),0)

    xp=sp.diff(2*j*(1-sp.cos(k))-kap**2*re_sigma,k)

    eq('constant_derivative_factor_identity',sp.trigsimp(xp-2*j*sp.sin(k)*(1-kap**2*c/j**2)),0)

    x,y,xp0,yp=sp.symbols('x y xp yp', real=True, nonzero=True)

    theta_prime=(xp0*y-x*yp)/(x*x+y*y)

    eq('arctan_density_identity',sp.cancel(theta_prime+x*yp/(x*x+y*y)-xp0*y/(x*x+y*y)),0)

    wrong=sp.cancel(theta_prime-x*yp/(x*x+y*y)-xp0*y/(x*x+y*y))

    assert wrong!=0

    u,b=sp.symbols('u b',positive=True)

    eq('positive_log_primitive',sp.simplify(sp.diff(sp.log(1+(u/b)**2)/2,u)-u/(u*u+b*b)),0)

    U,kk,aa,dd=sp.symbols('U kk aa dd',positive=True)

    expanded=sp.expand(kk*(aa*U+dd*U**2)*(32+12*kk*U)+kk*U*(2701+131*kk*U+2*kk*U**2)+sp.Rational(5,2)*kk*U*(32+12*kk*U))

    target=kk*(32*aa+2781)*U+(kk*kk*(12*aa+161)+32*kk*dd)*U**2+kk*kk*(12*dd+2)*U**3

    eq('complete_weighted_product_coefficients',sp.expand(expanded-target),0)

    loads={'old1':2*p['gA'],'old2':2*p['gB'],'source_A':F('20.332662089993454'),'source_B':F('17.078839343776311'),'c0':F('8.015120691541701'),'c1':F('6.730044773026091'),'ordinary_clock':4*J,'emitter_at_hi':E0+2*hi,'each_attachment_addition_at_hi':3*hi,'each_attachment_total_at_hi':4*J+3*hi,'old_existing_edge_additional':F(3)}

    lt('old1_added_incident_cap',loads['old1'],2)

    lt('old2_added_incident_cap',loads['old2'],2)

    report={
     'status':'Author scalar certificate passed; analytic parameter-family proof remains separately reviewable',
     'parameters':{'kappa_min':str(lo),'kappa_max':str(hi),'sigma':str(sigma),'L':L,'exact_ladder_parameters':{k:str(v0) for k,v0 in p.items()}},
     'uniformity_method':'Fixed kappa_max majorants for nonnegative polynomial numerators and fixed positive denominator lower bounds; log argument uses kappa_min. No parameter or momentum samples.',
     'new_reference_mass':{'m':str(m),'M':str(M),'gamma_upper':str(G),'gamma_prime_upper':str(G1),'log_upper':log_bound,'phase_deficit':show(phase_deficit),'integral_deficit':show(integral_deficit),'mass_loss':show(mass_loss),'mass_loss_ceiling':str(mass_ceiling),'seed_squared':show(seed_sq),'seed_squared_simple_ceiling':show(seed_coarse)},
     'inherited_identity_new_bounds':{'xi_majorant':show(xi),'relative_profile_majorant':show(eta_p),'off_diagonal_overlap':show(off),'phase_correction':show(phase_error),'target_residual_ceiling':str(target_residual),'Kloc':show(K0),'Kloc_prime':show(K1),'weighted_Dj_times_kappa_squared':show(Dj_scaled),'f_L2prime_times_kappa_squared':show(f2_scaled),'frho_L2prime_times_kappa_squared':show(frho2_scaled)},
     'budgets':{'T_formula':'10^6/kappa^2','T_at_max_kappa':str(T_hi),'T_at_min_kappa':str(T_lo),'M_formula':'ceil(50*T)','M_at_max_kappa':str(M_hi),'M_at_min_kappa':str(M_lo),'q_in':show(qin),'q_out':show(qout),'localized':show(local),'moment_remainder':show(moment_remainder),'complete_infinite':show(complete),'complete_finite':show(complete+F(1,1000)),'weighted_fallback_T_formula':'10^12/kappa^2','weighted_fallback_remainder':show(weighted_remainder)},
     'physical_loads':{name:show(value) for name,value in loads.items()},
     'preserved_failed_shortcut':{'naive_variance_mass_upper':show(naive_variance),'old_point_projection_variance_upper':show(F(4,5)),'meaning':'The old variance estimate cannot certify the new normalization; a bound larger than one is not physical mass greater than one. Old 8e-5 point-amplitude claim is not inherited. Complete seed overlap instead covers point spectrum below .003.'},
     'wrong_arctan_correction_sign_residual':str(wrong),
     'checks':checks,
     'actual_resources':{'python':platform.python_version(),'sympy':sp.__version__,'matrix_dimension':0,'parameter_grid_points':0,'quadrature_calls':0,'optimizer_calls':0,'time_evolution_calls':0,'cpu_soft_hard_seconds':list(resource.getrlimit(resource.RLIMIT_CPU)),'wall_cap_external_seconds':inputs.shared_limits()['external_wall_cap_seconds'],'program_wall_seconds':time.monotonic()-START},
     'limitations':'This program corroborates scalar algebra and inequalities. The spectral theorem, analytic density, arctan integration, monotone-majorant applicability, noncommuting Schur structure, exact packet normalization and physical premise chain require the written argument and independent review.'
    }

    report['_canonical_execution'] = inputs.execution_metadata('family_author')
    return report


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    started = time.monotonic()
    verify_artifacts()
    inputs = FrozenInputs(REPO, INPUT_ROOT / 'INPUT_MAP.json')
    report = run_family_author(inputs)
    output = {
        'scope': 'Portable replay of one source-exposed author scalar body. The complete analytical proof, family review and qualification remain separate.',
        'report': report,
        'actual_shared_process_limits': inputs.shared_limits(),
        'elapsed_seconds': time.monotonic() - started,
        'input_sha256': {name: hashlib.sha256((REPO / name).read_bytes()).hexdigest() for name in AUDIT_INPUT_PATHS},
        'resolved_reads': inputs.reads,
        'limitations': 'Exact-ladder family only; no joint/calibration extension, native supply, arbitrary accuracy or independent retained audit.'}
    (REPO / 'outputs/emitter_coupling_family_2026_10_17.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'scope': output['scope'], 'function_bodies_completed': 1,
                      'scalar_comparisons': len(report['checks']),
                      'complete_infinite': report['budgets']['complete_infinite'],
                      'complete_finite': report['budgets']['complete_finite'],
                      'actual_shared_process_limits': output['actual_shared_process_limits']}, indent=2))


AUDIT_INPUT_PATHS = (
    'docs/EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/PRODUCT_SEED_EMITTER_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'docs/ai_methodology/SCIENCE_WORKFLOW.md',
    'docs/ai_methodology/skills/physics-loop/SKILL.md',
    'outputs/emitter_coupling_family_2026_10_17_inputs/ARTIFACT_MANIFEST.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/INPUT_MAP.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/PROOF_BODY_MAP.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/PUBLICATION_STATUS.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/REPRODUCTION_PLAN.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/SOURCE_MAP.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/TRANSPORT_EDIT_LEDGER.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/CANDIDATE.md.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/EVIDENCE_READOUT.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/FILE_MANIFEST.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/FREEZE.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/MATCHING_PREMISE_SEARCH.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/READ_FAILURES.md.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/RESOURCE_PLAN.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/RESOURCE_PLAN_BEFORE_MOMENT.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/RUN_SUMMARY.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/SOURCE_MANIFEST.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/SOURCE_MANIFEST_BEFORE_MOMENT.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/SOURCE_RECHECK.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/add_moment_dependency.py',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/PRELAUNCH.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/RECEIPT.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/check_family.py',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/stderr.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/attempt_01/stdout.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/capture_sources.py',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/check_family.py',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/finalize_packet.py',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/inputs/moment.md.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/inputs/moment_acceptance.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/inputs/moment_freeze.json',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/inputs/moment_qualification.md.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/inputs/moment_review.md.txt',
    'outputs/emitter_coupling_family_2026_10_17_inputs/frozen_family/launch_check.py',
    'outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.json',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/ROUTE.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/inputs/THEOREM_V2.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/CANDIDATE.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__CANDIDATE.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__CERTIFICATE.json',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__inputs__rational_point_certificate.json',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/REPORT.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/ACCEPTANCE.json',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/QUALIFICATION.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_root_qualification/QUALIFICATION.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/CANDIDATE.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/REPORT.md.txt',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/ACCEPTANCE.json',
    'outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/QUALIFICATION.md.txt',
    'scripts/product_seed_emitter_2026_10_17.py',
)

if __name__ == '__main__':
    main()
