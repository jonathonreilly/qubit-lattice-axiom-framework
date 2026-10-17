#!/usr/bin/env python3
"""Exact local corroboration for PR9667 preparation calibration, not endpoint setup.

No proof of Duhamel, trace contractivity, global monotonicity, whole-output
scattering or physical implementation is computed. Polynomial identities and
finite rational checks support the separately reviewed analytical arguments.
Import is inert; external envelope owns source pins, resource caps and caches.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    'outputs/preparation_calibration_2026_10_17_inputs/ARTIFACT_MANIFEST.json',
    'outputs/preparation_calibration_2026_10_17_inputs/reviews/calibration_bookkeeping_independent_check/REPORT.md',
    'outputs/preparation_calibration_2026_10_17_inputs/reviews/calibration_runner_draft/ADAPTATION_REVIEW.md',
    'outputs/preparation_calibration_2026_10_17_inputs/reviews/preparation_calibration_publication_draft/INTEGRATION.md',
    'outputs/preparation_calibration_2026_10_17_inputs/reviews/preparation_calibration_publication_draft/SOURCE_IDENTITY_AND_DEPENDENCIES.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/00_bounded_followup_root_review_ACCEPTANCE.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/01_real_control_calibration_corrected_CANDIDATE_V2.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/02_real_control_calibration_corrected_CORRECTIONS.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/03_real_control_calibration_review_REPORT.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/04_real_control_calibration_candidate_PROPOSAL.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/05_real_control_calibration_candidate_SOURCE_MAP.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/06_real_coupling_halt_route_ROUTE.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/07_real_coupling_preparation_candidate_CANDIDATE.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/08_real_control_root_review_ACCEPTANCE.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/09_real_control_root_review_QUALIFICATION.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/10_docs_REAL_CONTROL_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/11_real_control_autonomous_output_2026_10_17_inputs_TRANSPORT_EDIT_LEDGER.json',
    'outputs/preparation_calibration_2026_10_17_inputs/sources/12_preparation_calibration_publication_draft_THEOREM_NOTE.md',
)


def read_regular(repo, rel):
    p = Path(rel)
    if p.is_absolute() or not p.parts or '..' in p.parts or p.as_posix() != rel:
        raise ValueError('invalid path: '+rel)
    cur = repo
    for part in p.parts:
        cur = cur / part
        if cur.is_symlink():
            raise ValueError('symlink file/ancestor: '+rel)
    if not cur.is_file():
        raise ValueError('not regular: '+rel)
    return cur.read_bytes()


def verify_inputs(repo):
    manifest = json.loads(read_regular(repo, AUDIT_INPUT_PATHS[0]))
    rows = manifest['files']
    seen = set()
    for row in rows:
        rel = row['path']
        if rel in seen or rel not in AUDIT_INPUT_PATHS[1:]:
            raise ValueError('duplicate/undeclared manifest path: '+rel)
        seen.add(rel)
        raw = read_regular(repo, rel)
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('input integrity mismatch: '+rel)
    if not seen or seen != set(AUDIT_INPUT_PATHS[1:]):
        raise ValueError('manifest closure incomplete')
    return sorted(seen)


def padd(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    while len(c)>1 and c[-1]==0: c.pop()
    return c


def pscale(a,k): return [k*x for x in a]


def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c


def peval(a,x):
    y=F(0)
    for c in reversed(a): y=y*x+c
    return y


def pdiff(a): return [i*a[i] for i in range(1,len(a))] or [F(0)]


def pint01(a): return sum((F(c,i+1) for i,c in enumerate(a)),F(0))


def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]


def madd(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def mscale(a,c): return [[c*x for x in r] for r in a]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def outer(v): return [[x*y for y in v] for x in v]


def check_arithmetic():
    count=0
    def check(name,ok):
        nonlocal count
        if not ok: raise AssertionError(name)
        count+=1
        print('PASS arithmetic: '+name,flush=True)
    def eq(name,a,b): check(name,a==b)
    def lt(name,a,b): check(name,a<b)
    def le(name,a,b): check(name,a<=b)

    I=[[F(1),F(0)],[F(0),F(1)]]
    n=[[F(0),F(0)],[F(0),F(1)]]
    a=[[F(0),F(1)],[F(0),F(0)]]
    ad=[[F(0),F(0)],[F(1),F(0)]]
    I4=kron(I,I)
    eta=F(1,10**5);epsilon=F(1,10**9)
    lt('whole-block scaling positive throughout error box',0,1-eta)
    # Both signs, with unequal nonunit magnitudes, test the literal local operator.
    for h in [F(3,7),F(-5,11)]:
        Q=madd(mscale(madd(kron(n,I),kron(I,n)),abs(h)),
               mscale(madd(kron(ad,a),kron(a,ad)),h))
        sign=1 if h>0 else -1
        gram=madd(mscale(outer([0,1,sign,0]),abs(h)),
                  mscale(outer([0,0,0,1]),2*abs(h)))
        eq('full local Q Gram '+str(h),Q,gram)
        comp=madd(mscale(I4,2*abs(h)),mscale(Q,-1))
        compgram=madd(mscale(outer([0,1,-sign,0]),abs(h)),
                      mscale(outer([1,0,0,0]),2*abs(h)))
        eq('full complement Gram '+str(h),comp,compgram)
        eq('Q identity coefficient '+str(h),tr(Q)/4,abs(h))
        eq('complement identity coefficient '+str(h),tr(comp)/4,abs(h))
        for xi in [-eta,eta]:
            scaled=mscale(comp,1+xi)
            eq('whole complement scaling '+str((h,xi)),
               madd(scaled,mscale(comp,-1)),mscale(comp,xi))
            eq('scaled identity included '+str((h,xi)),tr(scaled)/4,(1+xi)*abs(h))
    eq('occupation identity coefficient',tr(n)/2,F(1,2))

    # General rank-one projection difference has entries [[0,b],[b,d]],
    # b^2=d(1-d). Work in Q[d]; this is not sampling d to prove the identity.
    d=[F(0),F(1)];one_minus_d=[F(1),F(-1)]
    b_squared=pmul(d,one_minus_d)
    determinant=pscale(b_squared,-1)
    trace=d
    discriminant=padd(pmul(trace,trace),pscale(determinant,-4))
    eq('rank-one discriminant polynomial',discriminant,[0,4,-3])
    monotone_difference=padd(discriminant,pscale(pmul([-2,3],[-2,3]),-1))
    eq('complete g monotonicity polynomial factorization',monotone_difference,
       pscale(pmul([1,-1],[-1,3]),4))
    # Independent actual rational normalized vector tests matrix realization.
    v=[F(3,5),F(4,5)];rho=outer(v);projected=[[rho[0][0],F(0)],[F(0),F(0)]]
    diff=madd(rho,mscale(projected,-1));actual_d=rho[1][1]
    eq('projection matrix trace',tr(diff),actual_d)
    det=diff[0][0]*diff[1][1]-diff[0][1]*diff[1][0]
    eq('projection matrix discriminant',tr(diff)**2-4*det,peval(discriminant,actual_d))
    # Positivity of factors on [2/3,1] is analytical; endpoint values corroborate.
    eq('monotonicity endpoint one',peval(monotone_difference,F(1)),0)
    lt('isolated projection counterexample squared',peval(discriminant,F(1)),
       peval(discriminant,F(2,3)))
    eq('counterexample d two thirds radicand',peval(discriminant,F(2,3)),F(4,3))

    ramp=[0,0,3,-2];pulse=[0,0,30,-60,30]
    eq('isolation area',2*pint01(ramp)+3,4)
    eq('pulse unit area',pint01(pulse),1)
    for x in [F(0),F(1)]:
        eq('pulse endpoint value '+str(x),peval(pulse,x),0)
        eq('pulse endpoint slope '+str(x),peval(pdiff(pulse),x),0)
        eq('ramp endpoint slope '+str(x),peval(pdiff(ramp),x),0)
    eq('pulse midpoint value',peval(pulse,F(1,2)),F(15,8))
    # This finite polynomial calculation does not prove the global peak/slope.
    eq('pulse derivative factored',pdiff(pulse),pmul([0,60],pmul([1,-1],[1,-2])))

    J=F('0.030021107107032');q0=F('4.510351185997098')
    C=(q0*q0-1)/(q0*q0+1);S=2*q0/(q0*q0+1)
    c=C*C-S*S;s=2*C*S;E0=2*J*(1-C);kap=F(1,10**8)
    lt('double angle c positive',0,c);lt('double angle s positive',0,s)
    lt('pin positive at largest coupling',kap,E0)
    # Eight edge complements and one pin, assembled channel by channel.
    edge_magnitudes=[kap,kap,kap*c,kap*c,kap*s,kap*s,J,J]
    Aiso=sum(2*h for h in edge_magnitudes)+E0-kap
    eq('isolation norm sum from local channels',Aiso,4*J+4*kap*(1+c+s)+E0-kap)
    identity_sum=sum(edge_magnitudes)+(E0-kap)/2
    eq('isolation identity from channel traces',identity_sum,Aiso/2)
    lt('isolation coupling slope positive',0,4*(1+c+s)-1)
    lt('isolation ceiling throughout coupling interval',Aiso,F(1,7))
    # Pulse areas in units of pi; norms from the full local blocks above.
    areas=[F(1,4),F(1,4),F(1,2),F(1,2),F(1,2)]
    norms=[2,1,2,1,1];identities=[1,F(1,2),1,F(1,2),F(1,2)]
    area_norm=sum(x*y for x,y in zip(areas,norms))
    area_identity=sum(x*y for x,y in zip(areas,identities))
    eq('integrated pulse norm coefficient',area_norm,F(11,4))
    eq('integrated pulse identity coefficient',area_identity,F(11,8))
    pi_upper=F(22,7)
    bracket=4*F(1,7)+area_norm*pi_upper
    lt('Duhamel calibration scalar ceiling',bracket,10)
    le('zero calibration non-strict endpoint',F(0)*bracket,F(0)*10)
    pulse_peaks=[norm*area*F(15,8) for norm,area in zip(norms,areas)]
    # The three pulse windows do not overlap: pair, pair, singleton.
    peak=max(sum(pulse_peaks[:2]),sum(pulse_peaks[2:4]),pulse_peaks[4])
    lt('added control peak bound',F(1,7)+peak*pi_upper,9)
    work=2*F(1,7)+2*sum(pulse_peaks)*pi_upper
    lt('modeled work variation bound',work,33)
    # Squared positive bound checks 10*pi*sqrt(3)/3<20 without float sqrt.
    lt('incident pulse slew squared',(10*pi_upper/3)**2*3,20**2)
    lt('isolation ramp slew',F(3,2)*F(1,7),20)
    for nominal,ceiling in [(9,F('9.001')),(20,F('20.001')),(33,F('33.001'))]:
        lt('scaled resource ceiling '+str(nominal),nominal*(1+eta),ceiling)
    lt('nominal preparation correction squared',2*kap**2,F('0.00000002')**2)
    operator=F('.00483202')+10*eta
    eq('calibrated operator ceiling arithmetic',operator,F('.00493202'))
    eq('pure-seed trace ceiling arithmetic',2*operator,F('.00986404'))
    lt('seed trace contribution squared',9*epsilon,F('0.0001')**2)
    eq('complete trace ceiling arithmetic',2*operator+F('.0001'),F('.00996404'))
    lt('complete trace comparison target',2*operator+F('.0001'),F('.01'))
    T=1/(kap*kap);M=(50*T.numerator+T.denominator-1)//T.denominator
    eq('finite resource M at largest coupling',M,5*10**17)
    eq('finite qubit count at largest coupling',2*M+6,10**18+6)
    runtime=2*M+28;channels=runtime+9+len(norms)
    eq('fourteen preparation channels resource sum',channels,2*M+42)
    # All-occupied clock contribution: both rails and four endpoint occupations.
    eq('all-occupied clock energy',2*(M-1)*2*J+4*J,4*J*M)
    return count


def main():
    print('SCOPE: local exact algebra and rational ceilings for the supplied PR9667 setup.')
    print('BOUNDARY: Duhamel, trace contractivity, full-domain monotonicity and runtime/output theorem are analytical premises, not computed proofs.')
    print('BOUNDARY: no dynamics, quadrature, huge device, cooling, native supplier or general impossibility result is computed.')
    try:
        integrity=verify_inputs(Path(__file__).resolve().parents[1])
        print('PASS integrity: frozen package bytes; not mathematical acceptance.')
        count=check_arithmetic()
        print(json.dumps({'arithmetic_checks':count,'scientific_data_reads':[],
                          'package_integrity_reads':[AUDIT_INPUT_PATHS[0]]+integrity,
                          'source_self_integrity_reads':[], 'largest_dense_dimension':4},sort_keys=True))
    except Exception as exc:
        print('TOTAL FAIL: '+str(exc),flush=True)
        return 1
    print('TOTAL PASS: declared integrity and scoped local corroboration only.',flush=True)
    return 0


if __name__=='__main__':
    raise SystemExit(main())
