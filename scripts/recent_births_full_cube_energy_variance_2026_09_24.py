#!/usr/bin/env python3
"""Finite original source identities and a labeled cascade control.

Independent primitive code is explicitly reused after disclosure; the primary
rerun is not a new independent check. The note supplies the analytic limit.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/RECENT_BIRTHS_FORCE_FULL_CUBE_ENERGY_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib,json,math,time
import numpy as np
from scipy.linalg import expm,solve_continuous_lyapunov
OUTPUT=Path(__file__).resolve().parents[1]/'outputs/recent_birth_full_cube_variance_20260924'
A=(0,3,5,6); B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if (a^b) in (1,2,4))
OMEGA=(tuple(1 if x in A else 0 for x in range(8)),(0,)*12)
INDEPENDENT_PRIMITIVE_SOURCE_SHA='065fc1f5e0a0130d77a2e15a0eb053c1f4d920726ac29a1ca21faf0adb9993a2'
ROOT_TOY_SOURCE_SHA='1d56ded6fa3ee1ef8b739c7117d0be2aeff24c2d28f651aceda6be258ad35fc6'

def clean(v):
    return {k: c for k, c in v.items() if c}


def add(*terms):
    ans = defaultdict(Fraction)
    for scale, v in terms:
        for k, c in v.items():
            ans[k] += scale * c
    return clean(ans)


def hop(v, center=None):
    ans = defaultdict(Fraction)
    for (q, e), c in v.items():
        for k, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            if not q[a] or q[b]:
                continue
            qq, ee = list(q), list(e)
            charge = qq[a]
            qq[a], qq[b], ee[k] = 0, charge, ee[k] - charge
            ans[(tuple(qq), tuple(ee))] += c
    return clean(ans)


def birth(v, edge, sign):
    ans = defaultdict(Fraction)
    k = EDGES.index(edge)
    a, b = edge
    for (q, e), c in v.items():
        if q[a] or q[b]:
            continue
        qq, ee = list(q), list(e)
        qq[a], qq[b], ee[k] = sign, -sign, ee[k] + sign
        ans[(tuple(qq), tuple(ee))] += c
    return clean(ans)


def mark(v, edge, name):
    if name == 'coherent':
        return add((1, birth(v, edge, 1)), (1, birth(v, edge, -1)))
    return birth(v, edge, 1 if name == 'plus' else -1)


def adjoint_product_polynomial(v):
    """Translation polynomial of X*X on arbitrary initial physical fields."""
    ans = defaultdict(Fraction)
    for (q1, e1), c1 in v.items():
        for (q2, e2), c2 in v.items():
            if q1 == q2:
                shift = tuple(y - x for x, y in zip(e1, e2))
                ans[shift] += c1 * c2
    return clean(ans)


def check_gauss(v):
    for q, e in v:
        div = [0] * 8
        for field, (a, b) in zip(e, EDGES):
            div[a] += field
            div[b] -= field
        assert div == [q[x] - int(x in A) for x in range(8)]


def primitive_source_controls():
    omega = {OMEGA: Fraction(1)}
    F1 = hop(omega)
    F2 = hop(F1)
    rows = []
    zero = (0,) * 12
    all_vectors = {}
    for edge in EDGES:
        for name, b, r in [('plus', 2, 4), ('minus', 2, 2), ('coherent', 4, 6)]:
            bv = mark(F1, edge, name)
            rv = add((-1, hop(bv, center=edge[0])))
            direct = add((Fraction(1, 2), mark(F2, edge, name)), (-1, hop(bv)))
            assert rv == direct
            assert adjoint_product_polynomial(bv) == {zero: b}
            assert adjoint_product_polynomial(rv) == {zero: r}
            check_gauss(bv); check_gauss(rv)
            for edge2 in EDGES:
                assert not birth(rv, edge2, 1) and not birth(rv, edge2, -1)
            wrong = add((1, mark(F2, edge, name)), (-1, hop(bv)))
            assert wrong != rv
            rows.append({'edge': edge, 'mark': name, 'B_adjoint_B': b,
                         'R_adjoint_R': r, 'B_word_count': len(bv),
                         'R_word_count': len(rv), 'R_dark': True,
                         'minimal_source_identity': True,
                         'missing_half_coefficient_rejected': True})
            all_vectors[(edge, name)] = rv

    # The complete rotor W=1,N=6 charge labels: five positive and one negative
    # occupied site, with one A vacancy and one B vacancy. The original loss
    # is exactly 2 on adjacent vacancy pairs and 0 on the other pairs.
    losses = []
    for av in A:
        for bv in B:
            occupied = [x for x in range(8) if x not in (av, bv)]
            for negative in occupied:
                q = tuple(0 if x in (av, bv) else (-1 if x == negative else 1)
                          for x in range(8))
                v = {(q, zero): Fraction(1)}
                resolved = sum(sum(c*c for c in birth(v, edge, sign).values())
                               for edge in EDGES for sign in (1, -1))
                coherent = sum(sum(c*c for c in mark(v, edge, 'coherent').values())
                               for edge in EDGES)
                assert resolved == coherent == (2 if (av, bv) in EDGES else 0)
                losses.append(int(resolved))

    # A coherent birth cannot be replaced by a resolved mixture merely because
    # its source norm agrees. The cross-source density on one edge is nonzero.
    edge = EDGES[0]
    rp, rm = all_vectors[(edge, 'plus')], all_vectors[(edge, 'minus')]
    assert not set(rp).intersection(rm)
    normp = sum(c*c for c in rp.values())
    normm = sum(c*c for c in rm.values())
    cross_hs_squared = 2 * normp * normm
    assert cross_hs_squared == 16
    totals = {}
    for instrument in ('resolved', 'coherent'):
        selected = [row for row in rows if (row['mark'] == 'coherent') == (instrument == 'coherent')]
        totals[instrument] = {'sum_B_adjoint_B': sum(row['B_adjoint_B'] for row in selected),
                              'sum_R_adjoint_R': sum(row['R_adjoint_R'] for row in selected)}
        assert totals[instrument] == {'sum_B_adjoint_B': 48, 'sum_R_adjoint_R': 72}

    result = {'status': 'PASS-exact-primitive-source-identities',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'edge_order': EDGES, 'mark_checks': rows, 'instrument_totals': totals,
              'full_first_high_charge_label_count': len(losses),
              'bright_charge_labels': losses.count(2), 'dark_charge_labels': losses.count(0),
              'rotor_loss_maximum': max(losses),
              'coherent_vs_resolved_single_edge_source_difference_HS_squared': int(cross_hs_squared),
              'scope': 'Integer rotor charge/shift words and exact Laurent X*X identities for arbitrary input field. Not finite-spin or dynamical replication; no generator diagonalization or author code.'}
    return result


def subnormalized_fisher(rho,H):
    values,V=np.linalg.eigh((rho+rho.conj().T)/2)
    assert values.min()>-1e-13
    values=np.maximum(values,0);m=V.conj().T@H@V
    denominator=values[:,None]+values[None,:]
    quotient=np.divide((values[:,None]-values[None,:])**2,denominator,
                       out=np.zeros_like(denominator),where=denominator>1e-22)
    return float(2*np.sum(quotient*abs(m)**2))


def controls():
    delta,kappa,g,b,r=1.3,.4,.8,2.,4.
    G=np.array([[0,g],[g,0]],complex)
    bright=np.diag([0.,1.]);dark=np.array([1.,0.],complex)
    D=np.outer(dark,dark.conj());Z=-1j*delta*G-kappa*bright
    X0=solve_continuous_lyapunov(Z,-D)
    assert np.linalg.norm(Z@X0+X0@Z.conj().T+D)<1e-12
    Iinfty=float(np.trace(X0).real)
    age_cap=1.75
    Ecap=expm(age_cap*Z)
    IA=float(np.trace(X0-Ecap@X0@Ecap.conj().T).real)
    assert Iinfty>IA>0
    nodes,weights=np.polynomial.legendre.leggauss(96)
    ages=(nodes+1)*age_cap/2;weights=weights*age_cap/2
    profiles=np.array([expm(tau*Z)@dark for tau in ages])
    quadrature=float(np.dot(weights,np.sum(abs(profiles)**2,axis=1)))
    assert abs(quadrature-IA)<2e-13
    rows=[]
    for t in (.6,1.2):
        q0=math.exp(-kappa*b*t)
        for eps in (.12,.06,.03,.015):
            lam=kappa*(b+eps**2*r);q=math.exp(-lam*t)
            Am=Z+.5*lam*eps**2*np.eye(2)
            X=solve_continuous_lyapunov(Am,-D)
            assert np.linalg.eigvalsh(X).min()>0
            Et=expm((t/eps**2)*Am)
            rh= kappa*eps**4*r*q*(X-Et@X@Et.conj().T)
            rh=(rh+rh.conj().T)/2
            p0=kappa*b*(-math.expm1(-lam*t))/lam
            Kh=-1j*delta*eps**-4*np.eye(2)+eps**-2*Z
            growth=math.exp(lam*t)*np.exp(-1j*delta*t/eps**4)*expm((t/eps**2)*Z)
            cross=kappa*eps*math.sqrt(b*r)*q*np.linalg.solve(lam*np.eye(2)+Kh,(growth-np.eye(2))@dark)
            rho=np.zeros((3,3),complex);rho[0,0]=p0;rho[1:,1:]=rh
            rho[1:,0]=cross;rho[0,1:]=cross.conj()
            terminal=1-q-float(np.trace(rho).real)
            assert terminal>=-1e-12 and np.linalg.eigvalsh(rho).min()>-1e-13
            Hh=delta*eps**-4*(np.eye(2)+eps**2*G)
            H=np.zeros((3,3),complex);H[1:,1:]=Hh
            mean=float(np.trace(H@rho).real)
            second=float(np.trace(H@H@rho).real)
            variance=second-mean**2
            fisher=subnormalized_fisher(rho,H)
            assert variance>0 and 0<=fisher<=4*variance*(1+1e-12)
            scaled_var=eps**4*variance
            target=kappa*delta**2*r*q0*Iinfty

            EA=expm(age_cap*Am)
            rh_recent=kappa*eps**4*r*q*(X-EA@X@EA.conj().T)
            recent_high_probability=float(np.trace(rh_recent).real)
            recent_mean=float(np.trace(Hh@rh_recent).real)
            recent_second=float(np.trace(Hh@Hh@rh_recent).real)
            scaled_within=0.
            Hscaled=delta*(np.eye(2)+eps**2*G)
            for tau,wgt,v in zip(ages,weights,profiles):
                source=kappa*math.exp(-lam*(t-eps**2*tau))
                norm=float(np.vdot(v,v).real)
                mv=float(np.vdot(v,Hscaled@v).real)
                m2=float(np.vdot(Hscaled@v,Hscaled@v).real)
                scaled_within+=wgt*source*(r*m2-eps**2*r*r*mv*mv/(b+eps**2*r*norm))
            recent_target=kappa*delta**2*r*q0*IA
            assert scaled_var>=scaled_within-1e-10
            row={'t':t,'epsilon':eps,'initial_sector_probability':q,
                 'born_low_probability':p0,'born_high_probability':float(np.trace(rh).real),
                 'terminal_probability':terminal,'born_density_min_eigenvalue':float(np.linalg.eigvalsh(rho).min()),
                 'full_mean':mean,'limiting_mean':kappa*delta*r*q0*Iinfty,
                 'eps4_full_variance':scaled_var,'limiting_eps4_variance':target,
                 'relative_scaled_variance_error':abs(scaled_var/target-1),
                 'full_Fisher':fisher,'Fisher_over_four_variance':fisher/(4*variance),
                 'high_low_block_norm_over_eps5':float(np.linalg.norm(cross)/eps**5),
                 'recent_high_probability_over_eps4':recent_high_probability/eps**4,
                 'recent_high_probability_target':kappa*r*q0*IA,
                 'recent_mean':recent_mean,'recent_mean_target':kappa*delta*r*q0*IA,
                 'eps4_recent_second_moment':eps**4*recent_second,
                 'eps4_recent_within_path_variance':scaled_within,
                 'recent_variance_target':recent_target,
                 'field_only_mutant_high_probability':0.}
            rows.append(row)
        block=rows[-4:]
        assert block[-1]['relative_scaled_variance_error']<.002
        assert block[-1]['relative_scaled_variance_error']<.3*block[-2]['relative_scaled_variance_error']
        assert abs(block[-1]['eps4_recent_within_path_variance']/recent_target-1)<.002
        assert block[-1]['Fisher_over_four_variance']<1e-5
    return {'parameters':{'delta':delta,'kappa':kappa,'g':g,'b':b,'r':r,'age_cap':age_cap},
            'fast_integral_infinite':Iinfty,'fast_integral_capped':IA,
            'quadrature_absolute_error':abs(quadrature-IA),'rows':rows,
            'scope':'Exact finite toy cascade and source integration only. Not the cube, its large-spin limit, a microscopic N=4 derivation, or a conserving apparatus. A cube QFI upper bound is not inferred.'}


def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    result={'primitive_sources':primitive_source_controls(),'toy':controls(),
            'elapsed_seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'provenance':{'reused_independent_primitive_source':INDEPENDENT_PRIMITIVE_SOURCE_SHA,'reused_root_toy_source':ROOT_TOY_SOURCE_SHA}}
    text=json.dumps(result,indent=2)+'\n'
    (OUTPUT/'RECENT_BIRTH_FULL_ENSEMBLE_RESULTS.json').write_text(text)
    print(text,end='',flush=True)
    print('TOTAL: PASS=2 FAIL=0',flush=True)

if __name__=='__main__':main()
