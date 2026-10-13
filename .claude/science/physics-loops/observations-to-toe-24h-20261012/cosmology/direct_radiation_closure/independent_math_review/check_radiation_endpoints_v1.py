#!/usr/bin/env python3
"""Independent high-precision coordinate quadrature and corrected-source check."""
from pathlib import Path
import datetime
import hashlib
import itertools
import json
import mpmath as mp
import sympy as sy

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90
CHECKS=[]
ROWS=[]


def check(name,passed,**details):
    CHECKS.append(dict(name=name,passed=bool(passed),**details))


def functions(a,b,L):
    def radiation(S):return b*S**(mp.mpf(4)/3)
    def U(S):return L+a*S/2+a*radiation(S)/3
    def F(S):
        R=radiation(S)
        return 6*((1+a)*(S+R)+L)*S*S/(a*(S+4*R/3))
    def curvature(S):return F(S)*mp.diff(U,S,2)+mp.diff(F,S)*mp.diff(U,S)/2
    def transverse(S):return a*F(S)/curvature(S)+a*S*S/U(S)
    return radiation,U,F,curvature,transverse


# The coordinate integral uses S=y^6: its integrand is analytic at y=0,
# unlike direct integration of S^-1/2. No truncated endpoint series is used.
def coordinate_q(S,a,b,L):
    ymax=S**(mp.mpf(1)/6)
    return 3*ymax**3*mp.quad(lambda t:t*t*mp.sqrt(1+4*b*ymax*ymax*t*t/3)
                            /mp.sqrt(1+(1+a)*(ymax**6*t**6+b*ymax**8*t**8)/L),[0,1])


couplings=['0.000001',str(1/2499),'0.01']
for astr,bstr,Lstr in itertools.product(couplings,['0.1','1','10'],['0.7','3']):
    a,b,L=map(mp.mpf,[astr,bstr,Lstr])
    radiation,U,F,curvature,transverse=functions(a,b,L)
    errors=[]
    for exp in [-9,-18,-30]:
        S=mp.mpf(10)**exp
        q=coordinate_q(S,a,b,L)
        values=dict(S=(S-q*q)/q**(mp.mpf(8)/3),
                    U=(U(S)-L-a*q*q/2)/q**(mp.mpf(8)/3),
                    M=(transverse(S)-4*q*q)/q**(mp.mpf(8)/3))
        expected=dict(S=-4*b/5,U=-a*b/15,M=-mp.mpf(992)*b/135)
        relative={k:abs(values[k]/expected[k]-1) for k in values}
        errors.append(relative)
        label=f'{astr}_{bstr}_{Lstr}_{exp}'
        check('positive_mass_and_curvature_'+label,transverse(S)>0 and curvature(S)>0)
        determinant=transverse(S)*curvature(S)-a*F(S)
        target=a*S*S*curvature(S)/U(S)
        check('positive_determinant_'+label,determinant>0 and abs(determinant/target-1)<mp.mpf('1e-35'),
              relative_residual=str(abs(determinant/target-1)))
        for scaled_u in [-10,-1,0,1,10]:
            u=scaled_u*mp.sqrt(a)
            V=U(S)-mp.sqrt(a)*S*u+transverse(S)*u*u/2
            check('global_bound_sample_'+label+'_'+str(scaled_u),V>=U(S)/2)
        ROWS.append(dict(a=astr,b=bstr,L=Lstr,S=str(S),q=str(q),
                         endpoint_coefficients={k:str(v) for k,v in values.items()},
                         relative_coefficient_errors={k:str(v) for k,v in relative.items()}))
    for key in ['S','U','M']:
        check(f'endpoint_coefficient_limit_{astr}_{bstr}_{Lstr}_{key}',errors[-1][key]<mp.mpf('2e-7'),
              relative_error=str(errors[-1][key]),tolerance='2e-7')
        check(f'endpoint_convergence_{astr}_{bstr}_{Lstr}_{key}',errors[1][key]<errors[0][key]/20 and errors[2][key]<errors[1][key]/20)

# Full-potential endpoint coefficients: C2 regularity, not merely U regularity.
a,b,u,q,beta=sy.symbols('a b u q beta',positive=True)
q2=a/2-sy.sqrt(a)*u+2*u*u
qfrac=-a*b/15+4*sy.sqrt(a)*b*u/5-sy.Rational(496,135)*b*u*u
square=-sy.Rational(496,135)*b*(u-27*sy.sqrt(a)/248)**2-sy.Rational(43,1860)*a*b
check('fractional_coefficient_strictly_negative_for_all_real_u',sy.simplify(qfrac-square)==0,
      completed_square=str(square))
check('leading_vacuum_curvature_positive_for_all_real_u',sy.simplify(2*q2-(4*(u-sy.sqrt(a)/4)**2+3*a/4))==0)
Uthird=(-beta)**3*sy.diff(-a*b*q**sy.Rational(8,3)/15,q,3)
check('one_sided_U_third_derivative_diverges',sy.simplify(Uthird-sy.Rational(16,81)*a*b*beta**3*q**(-sy.Rational(1,3)))==0)

# Full coordinate equations follow from the canonical proper-time equation.
g,gx,p,pp,H,h,Vx=sy.symbols('g gx p pp H h Vx',positive=True)
chix=-sy.sqrt(g);chixx=-gx/(2*sy.sqrt(g))
chi_dot=H*chix*p
chi_ddot=H*H*(chix*pp+chixx*p*p+h*chix*p)
canonical=(chi_ddot+3*H*chi_dot+Vx/chix)/(H*H*chix)
coordinate=pp+(3+h)*p+gx*p*p/(2*g)+Vx/(g*H*H)
check('full_x_equation_chain_rule',sy.simplify(canonical-coordinate)==0)

# Narrow source correction: exact bytes, no changed potential or slope.
old=(ROOT/'source_snapshot/HAND_DERIVATION_v1.md').read_text()
new=(ROOT/'affected_v2/HAND_DERIVATION_v2.md').read_text()
check('only_dust_speed_text_changed',new==old.replace('sqrt(3/(1+a)) in dust domination','sqrt(3/(2(1+a))) in dust domination'))
correction=json.loads((ROOT/'affected_v2/DUST_SPEED_CORRECTION_v2.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check('correction_v1_hash',correction['v1_sha256']==sha(ROOT/'source_snapshot/HAND_DERIVATION_v1.md'))
check('correction_v2_hash',correction['v2_sha256']==sha(ROOT/'affected_v2/HAND_DERIVATION_v2.md'))
for metadata in ['INPUT_FREEZE_v1.json','affected_v2/PINS.json']:
    for row in json.loads((ROOT/metadata).read_text())['files']:
        check('source_and_snapshot_unchanged_'+Path(row['path']).name,sha(Path(row['path']))==row['sha256']==sha(Path(row['snapshot'])))
first=json.loads((ROOT/'ALGEBRA_RESULTS_v1.json').read_text())
fail=[c for c in first['checks']if not c['passed']]
check('original_failed_dust_assertion_preserved',len(fail)==1 and fail[0]['name']=='dust_velocity_squared_handwritten')
check('corrected_dust_assertion_already_independently_verified',next(c for c in first['checks']if c['name']=='dust_velocity_squared_corrected')['passed'])

out=dict(created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),checks_count=len(CHECKS),all_passed=all(c['passed'] for c in CHECKS),checks=CHECKS,quadrature_rows=ROWS,
         scope='Synthetic exact-coordinate and source checks only. No parent implementation or empirical arrays used.')
(ROOT/'ENDPOINT_RESULTS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks_count=len(CHECKS),all_passed=out['all_passed'],failures=[c for c in CHECKS if not c['passed']])))
raise SystemExit(0 if out['all_passed'] else 1)
