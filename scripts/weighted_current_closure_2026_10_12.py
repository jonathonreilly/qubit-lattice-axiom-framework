#!/usr/bin/env python3
"""Exact finite author controls; no scientific status is encoded in this runner."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/WEIGHTED_CURRENT_CLOSURE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_JOINT_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    ".claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from fractions import Fraction as F
from pathlib import Path
from itertools import product
import datetime, hashlib, json, sys

MOMENT_SIGN = -1
CURRENT_FACTOR = F(1, 2)
PAD_RADIUS = 8
TEST_AXES = ('X', 'Y', 'Z')
IGNORE_ORBIT_SUM = False

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))
def gq(a): return a if isinstance(a, tuple) else (F(a), F(0))
def gadd(a,b): return (a[0]+b[0], a[1]+b[1])
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,z):
    z=gq(z)
    return {w:c for w,x in a.items() if (c:=gmul(x,z)) != ZERO}
def add(*args):
    out={}
    for a in args:
        for w,c in a.items():
            out[w]=gadd(out.get(w,ZERO),c)
            if out[w]==ZERO: del out[w]
    return out
def sub(a,b): return add(a,scale(b,-1))
def site(x): return (x,) if isinstance(x,int) else tuple(x)
def word(mapping, coeff=1):
    return {tuple(sorted((site(x),l) for x,l in mapping.items() if l!='I')):gq(coeff)}
TABLE={('X','Y'):('Z',I),('Y','Z'):('X',I),('Z','X'):('Y',I),
       ('Y','X'):('Z',(F(0),F(-1))),('Z','Y'):('X',(F(0),F(-1))),
       ('X','Z'):('Y',(F(0),F(-1)))}
def wmul(a,b):
    out=dict(a);phase=ONE
    for x,v in b:
        if x not in out:out[x]=v
        elif out[x]==v:del out[x]
        else:
            out[x],z=TABLE[out[x],v];phase=gmul(phase,z)
    return tuple(sorted(out.items())),phase
def mul(a,b):
    out={}
    for wa,ca in a.items():
        for wb,cb in b.items():
            w,phase=wmul(wa,wb);c=gmul(gmul(ca,cb),phase)
            out[w]=gadd(out.get(w,ZERO),c)
            if out[w]==ZERO:del out[w]
    return out
def comm(a,b):return sub(mul(a,b),mul(b,a))
def translate(a,v):
    v=site(v)
    return {tuple((tuple(s+t for s,t in zip(x,v)),l) for x,l in w):c for w,c in a.items()}
def support(a):return {x for w in a for x,l in w}
def centers(a,b):return sorted({tuple(yj-xj for xj,yj in zip(x,y)) for x in support(a) for y in support(b)})
def delta(g,a,axis=None):
    return add(*(scale(comm(translate(g,x),a),I if axis is None else gmul(I,gq(x[axis]))) for x in centers(g,a)))
def current(h,axis=0):
    return add(*(scale(comm(h,translate(h,r)),gmul(I,gq(CURRENT_FACTOR*r[axis]))) for r in centers(h,h)))
def deriv_comm(p,h,a,axis=0):
    return sub(delta(p,delta(h,a,axis)),delta(h,delta(p,a),axis))
def canonical(w):
    anchor=w[0][0]
    return tuple((tuple(xj-aj for xj,aj in zip(x,anchor)),l) for x,l in w),anchor
def groups(q,reverse=False):
    out={}
    for w,c in sorted(q.items(),reverse=reverse):
        if not w:continue
        key,pos=canonical(w)
        if key not in out:out[key]=[w,pos,[]]
        ref,anchor,rows=out[key]
        rows.append((tuple(p-a for p,a in zip(pos,anchor)),c))
    return out
def decompose(q,axis=0,reverse=False,require_conserved=True):
    t={};s={};table=[]
    for key,(ref,anchor,rows) in groups(q,reverse).items():
        sm=ZERO;moment=ZERO
        for v,c in rows:
            sm=gadd(sm,c);moment=gadd(moment,gmul(gq(v[axis]),c))
        if sm!=ZERO:s[ref]=sm
        d=gmul(gq(MOMENT_SIGN),moment)
        if d!=ZERO:t[ref]=d
        table.append(dict(reference=fmt_word(ref),orbit_sum=fmt_coeff(sm),moment=fmt_coeff(moment),rows=[dict(v=v,c=fmt_coeff(c)) for v,c in rows]))
    if require_conserved and s and not IGNORE_ORBIT_SUM:raise ValueError('nonzero orbit sum')
    return t,s,table
def aggregate(q):
    out={}
    for w,c in q.items():
        key=canonical(w)[0] if w else ()
        out[key]=gadd(out.get(key,ZERO),c)
        if out[key]==ZERO:del out[key]
    return out
def primitives(q):
    d=len(next(iter(support(q)))) if support(q) else 1
    a=[{} for _ in range(d)]
    for key,(ref,anchor,rows) in groups(q).items():
        if sum((c[0] for v,c in rows),F(0))!=0 or sum((c[1] for v,c in rows),F(0))!=0:raise ValueError('nonzero orbit sum')
        for v,c in rows:
            u=[0]*d
            for axis,n in enumerate(v):
                direction=1 if n>=0 else -1
                for _ in range(abs(n)):
                    if direction==1:
                        a[axis]=add(a[axis],scale(translate({ref:ONE},u),gmul(gq(-1),c)))
                        u[axis]+=1
                    else:
                        u[axis]-=1
                        a[axis]=add(a[axis],scale(translate({ref:ONE},u),c))
    return a
def divergence(a):
    d=len(a)
    return add(*(sub(q,translate(q,tuple(int(i==b) for i in range(d)))) for b,q in enumerate(a)))
def full_basis_zero(q):
    d=len(next(iter(support(q)))) if support(q) else 1
    return all(not delta(q,word({(0,)*d:a})) for a in TEST_AXES)
def fmt_coeff(c):return [str(c[0]),str(c[1])]
def fmt_word(w):return ' '.join(l+'@'+','.join(map(str,x)) for x,l in w) or 'I'
def fmt(q):return [dict(word=fmt_word(w),coefficient=fmt_coeff(c)) for w,c in sorted(q.items())]
def l1(q):return str(sum((abs(c[0])+abs(c[1]) for c in q.values()),F(0)))

ROWS=[]
def check(name,passed,**detail):
    row=dict(name=name,passed=bool(passed),**detail);ROWS.append(row);print(json.dumps(row,sort_keys=True))
def eq(name,a,b):check(name,a==b,defect_terms=len(sub(a,b)),defect_l1=l1(sub(a,b)))

def main():
    artifacts={}
    # A nonzero divergence and its scalar padding never use energy conservation.
    z=word({0:'Z'});q=sub(z,translate(z,1));t,s,tab=decompose(q)
    check('nonzero_divergence_is_not_zero_density',bool(q),density=fmt(q))
    eq('divergence_moment_is_Z0',aggregate(t),z)
    check('divergence_full_basis_zero',full_basis_zero(q))
    for x in (0,3):
        for axis in ('X','Y','Z'):
            a=word({x:axis});eq(f'divergence_weighted_reduction_{x}_{axis}',delta(q,a,0),delta(t,a))
    qscalar=add(q,word({},7));ts,ss,_=decompose(qscalar)
    eq('scalar_part_does_not_change_moment',ts,t)
    eq('scalar_part_does_not_change_weighted_action',delta(qscalar,word({0:'X'}),0),delta(q,word({0:'X'}),0))
    # Complete one-site basis matters, even for a one-site density.
    check('selected_Z_test_is_nondiscriminating',not delta(z,word({0:'Z'})))
    check('full_basis_rejects_Z_density',not full_basis_zero(z),X_action=fmt(delta(z,word({0:'X'}))))
    # Genuine two-direction divergence with coordinate-axis discrimination.
    a1=add(word({(0,0):'X',(1,0):'Z'}),word({(0,1):'Y'}))
    a2=word({(0,0):'Z',(0,1):'X'},2)
    q2=divergence([a1,a2]);ps=primitives(q2)
    eq('two_dimensional_primitive_reconstructs',divergence(ps),q2)
    k=word({(0,0):'Y',(1,1):'Z'})
    alternatives=[add(ps[0],sub(k,translate(k,(0,1))),word({},5)),sub(ps[1],sub(k,translate(k,(1,0))))]
    eq('curl_and_scalar_primitive_change_reconstructs',divergence(alternatives),q2)
    for b in (0,1):
        tb,sb,_=decompose(q2,b);tr,sr,_=decompose(q2,b,reverse=True)
        for axis in ('X','Y','Z'):
            a=word({(0,0):axis})
            eq(f'two_dimensional_moment_axis{b}_{axis}',delta(q2,a,b),delta(tb,a))
            eq(f'representative_independence_axis{b}_{axis}',delta(tb,a),delta(tr,a))
            eq(f'primitive_independence_axis{b}_{axis}',delta(tb,a),delta(alternatives[b],a))
    # Canonical XX current: positive energy-current conservation control.
    f=add(word({0:'X',1:'X'}),word({0:'Y',1:'Y'}))
    long=add(word({0:'X',1:'Z',2:'Z',3:'X'}),word({0:'Y',1:'Z',2:'Z',3:'Y'}))
    p=current(f);r=delta(p,f);tx,sx,xtable=decompose(r,require_conserved=False)
    artifacts['XX']=dict(h=fmt(f),p=fmt(p),r=fmt(r),t=fmt(tx),t_orbit_aggregate=fmt(aggregate(tx)),orbits=xtable)
    check('XX_r_nonzero',bool(r),terms=len(r))
    check('XX_energy_current_conserved_orbits',not sx,nonzero_sums=fmt(sx))
    check('XX_energy_current_conserved_full_basis',full_basis_zero(r))
    eq('XX_t_equals_minus8_h_minus8_long_mod_translation',aggregate(tx),scale(add(f,long),-8))
    # [f_0,f_1]=2i(XZY-YZX), so i/2 times it is YZX-XZY.
    expectedp=add(word({0:'X',1:'Z',2:'Y'},-1),word({0:'Y',1:'Z',2:'X'}),word({-1:'X',0:'Z',1:'Y'},-1),word({-1:'Y',0:'Z',1:'X'}))
    eq('XX_current_formula_independent_Pauli_multiplication',p,expectedp)
    psx=primitives(r)
    eq('XX_nonzero_divergence_primitive_reconstructs',divergence(psx),r)
    for x in (0,2):
        for axis in ('X','Y','Z'):
            a=word({x:axis});direct=deriv_comm(p,f,a)
            eq(f'XX_weighted_Jacobi_{x}_{axis}',direct,delta(r,a,0))
            eq(f'XX_moment_reduction_{x}_{axis}',direct,delta(tx,a))
            eq(f'XX_primitive_reduction_{x}_{axis}',direct,delta(psx[0],a))
    a=word({0:'X'});rho=PAD_RADIUS
    P=add(*(translate(p,x) for x in range(-rho,rho+1)))
    B=add(*(scale(translate(f,x),x) for x in range(-rho,rho+1)))
    padded=scale(comm(comm(P,B),a),-1)
    eq('XX_finite_padded_Jacobi',padded,deriv_comm(p,f,a))
    for beta in (F(1),F(-8)):
        kbeta=sub(tx,scale(f,beta));check('XX_requested_beta_'+str(beta)+'_criterion_rejects',not full_basis_zero(kbeta),orbit_residual=fmt(aggregate(kbeta)))
    # Fixed nonconserved fixture; conservation is a gate, not an inferred fact.
    h=add(word({0:'Z',1:'Z'}),word({0:'X'}));pg=current(h);rg=delta(pg,h)
    tg,sg,gtable=decompose(rg,require_conserved=False)
    artifacts['nonconserving']=dict(h=fmt(h),p=fmt(pg),r=fmt(rg),t=fmt(tg),residual_density=fmt(sg),orbits=gtable)
    check('nonconserved_fixture_fails_full_basis',not full_basis_zero(rg),nonzero_sums=fmt(sg))
    rejected=False
    try:decompose(rg)
    except ValueError:rejected=True
    check('reduction_requires_conservation',rejected)
    a=word({0:'Z'})
    C=deriv_comm(pg,h,a);eq('nonconserved_weighted_Jacobi',C,delta(rg,a,0))
    eq('nonconserved_residual_is_retained',C,add(delta(tg,a),delta(sg,a,0)))
    check('discarding_nonconserved_residual_is_detected',C!=delta(tg,a),defect=fmt(sub(C,delta(tg,a))))
    shifted=translate(a,2)
    covariance=sub(deriv_comm(pg,h,shifted),translate(C,2))
    eq('nonconserved_covariance_residual_sign',covariance,scale(delta(rg,shifted),2))
    check('nonconserved_covariance_residual_nonzero',bool(covariance),defect_l1=l1(covariance))
    # Degenerate scalar/on-site and beta scaling cases.
    for name,h0 in [('scalar',word({},4)),('onsite',add(word({0:'X'}),word({0:'Z'},2)))]:
        p0=current(h0);r0=delta(p0,h0);t0,_,_=decompose(r0)
        check(name+'_current_and_reduction_zero',not p0 and not r0 and not t0)
    lam=F(3,2);hscaled=scale(f,lam);pscaled=current(hscaled);rscaled=delta(pscaled,hscaled);tscaled,_,_=decompose(rscaled)
    eq('energy_rescaling_current_quadratic',pscaled,scale(p,lam**2))
    eq('energy_rescaling_reduction_cubic',aggregate(tscaled),scale(aggregate(tx),lam**3))
    # Formal weighted origin offsets cancel only because the XX r derivation is zero.
    for origin in (-4,5):
        eq('conserved_origin_shift_'+str(origin),add(delta(r,a,0),scale(delta(r,a),origin)),delta(tx,a))
    output=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),python=sys.version,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),rows=ROWS,computed_densities=artifacts,summary=dict(passed=sum(x['passed'] for x in ROWS),failed=sum(not x['passed'] for x in ROWS)))
    # Publication suppresses the adjacent-result write only; the complete result and source self-hash remain computed.
    print('TOTAL: PASS='+str(output['summary']['passed'])+' FAIL='+str(output['summary']['failed']))
    print('per_element: exact sparse coefficient moments, residuals and weighted Jacobi fixtures are checked against the original gates.')
    print('per_site: complete finite Pauli site tests and padding controls are checked; no intended-model conservation is asserted.')
    print('per_mode: checked and not executed — no physical particle spectrum, beta determination or continuum mode is inferred.')
    print('per_block: finite XX and nonconserving fixtures retain all original defect and insensitive rows.')
    print('lattice_wide: checked and not executed — local algebraic closure and the optional supplied-operator corollary require the analytic hypotheses.')
    print('SCOPE: Original finite controls only; documented mutation survivors and insensitive rows remain. Counts do not prove the analytic theorem or a physical model.')
    return int(bool(output['summary']['failed']))
if __name__=='__main__':sys.exit(main())
