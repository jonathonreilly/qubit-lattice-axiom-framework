#!/usr/bin/env python3
"""Author diagnostics; no infinite-volume or proof-assistant claim."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/INTEGRATED_BOOST_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_BOOST_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MICROSCOPIC_JOINT_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    ".claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

import argparse
import cmath
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mutation', choices=['none', 'reverse_boost', 'drop_beta',
                    'double_spatial_beta', 'forward_spectral_set', 'energy_phase'],
                    default='none')
    ap.add_argument('--output', default=None)
    args = ap.parse_args()
    rows = []
    phase = Q(2, 7) if args.mutation == 'energy_phase' else Q(0)

    def add(name, success, details):
        rows.append({'name': name, 'pass': bool(success), 'details': details})
        print(('PASS ' if success else 'FAIL ') + name + ' ' + json.dumps(details))

    def shifted(r, a):
        return r*a if args.mutation == 'reverse_boost' else r/a

    def values(k, m, r):
        return m*(r+1/r)/2 + phase, k*m*(r-1/r)/2

    def coeff(k, a):
        c, d = (a+1/a)/2, (a-1/a)/(2*k)
        beta_effective = Q(1) if args.mutation == 'drop_beta' else k*k
        return c, -d, -beta_effective*d, c

    def f(r):
        return r**4/(1+r)**8

    fixtures = [(Q(2),Q(1),Q(2)), (Q(3,2),Q(5,4),Q(3,5)),
                (Q(1,2),Q(2,3),Q(5,2))]
    radii = [Q(2,5),Q(1),Q(7,3)]
    for fi,(k,m,a) in enumerate(fixtures):
        beta = k*k
        mh, mp, ph, pp = coeff(k,a)
        for ri,r in enumerate(radii):
            tag = f'f{fi}.r{ri}'
            h,p = values(k,m,r)
            hs,ps = values(k,m,shifted(r,a))
            eh,ep = mh*h+mp*p,ph*h+pp*p
            add(tag+'.energy_shift',hs==eh,{'actual':str(hs),'mixed':str(eh)})
            add(tag+'.current_shift',ps==ep,{'actual':str(ps),'mixed':str(ep)})
            inv, invs = h*h-p*p/beta, hs*hs-ps*ps/beta
            add(tag+'.mass_invariant',inv==invs,{'before':str(inv),'after':str(invs)})

            # Actual differential products on f; neither uses the proposed
            # conjugation matrix or its derivative.
            fr = f(r)
            df = 4*r**4*(1-r)/(1+r)**9  # r*d/dr f(r)
            dh = m*(r-1/r)/2
            dp = k*m*(r+1/r)/2
            sign = -1 if args.mutation == 'reverse_boost' else 1
            ihb = sign*k*((dh*fr+h*df)-h*df)
            ipb = sign*k*((dp*fr+p*df)-p*df)
            add(tag+'.local_lie',ihb==p*fr and ipb==beta*h*fr,
                {'iHB':str(ihb),'P_f':str(p*fr),'iPB':str(ipb),'betaH_f':str(beta*h*fr)})

        # Explicit composition of actual function actions on a true L2 vector.
        def W(a0,fn):
            return lambda r0: fn(shifted(r0,a0))

        def U(t0,fn):
            return lambda r0: cmath.exp(1j*float(t0)*float(values(k,m,r0)[0]))*fn(r0)

        def V(u0,fn):
            return lambda r0: cmath.exp(1j*float(u0)*float(values(k,m,r0)[1]))*fn(r0)

        def T(t0,y0,fn):
            divisor = beta*beta if args.mutation == 'double_spatial_beta' else beta
            return U(t0,V(-y0/divisor,fn))

        t,u,y=Q(2,7),Q(-3,11),Q(5,13)
        leftH=W(a,U(t,W(1/a,f)))
        rightH=U(mh*t,V(mp*t,f))
        leftP=W(a,V(u,W(1/a,f)))
        rightP=U(ph*u,V(pp*u,f))
        c,d=(a+1/a)/2,(a-1/a)/(2*k)
        leftT=W(a,T(t,y,W(1/a,f)))
        rightT=T(c*t+d*y,beta*d*t+c*y,f)
        for label,left,right in [('unitary_H',leftH,rightH),('unitary_P',leftP,rightP),
                                  ('negative_spatial_clock',leftT,rightT)]:
            errs=[abs(left(r)-right(r)) for r in radii]
            add(f'f{fi}.{label}',max(errs)<1e-11,{'max_abs_error':max(errs),'tolerance':1e-11})

        # Fourth-order finite difference of the actual shifted multiplier.
        eps=1e-4
        r0=Q(7,5)
        def at(offset):
            return values(float(k),float(m),shifted(float(r0),float(a)*math.exp(float(k)*offset)))
        points={j:at(j*eps) for j in [-2,-1,1,2]}
        ds=[(-points[2][j]+8*points[1][j]-8*points[-1][j]+points[-2][j])/(12*eps)
            for j in [0,1]]
        hv,pv=values(k,m,shifted(r0,a))
        errs=[abs(ds[0]+float(pv)),abs(ds[1]+float(beta*hv))]
        add(f'f{fi}.actual_C1_derivative',max(errs)<1e-8,
            {'energy_residual':errs[0],'current_residual':errs[1],'tolerance':1e-8,'step':eps})

        # Both exact clock choices satisfy a group law; this is deliberately
        # not a discriminatory test of the sign.
        a2=Q(5,4)
        comp=all(shifted(shifted(r,a),a2)==shifted(r,a*a2) for r in radii)
        add(f'f{fi}.boost_group_law',comp,{'a':str(a),'a2':str(a2)})

    # Spectral projection: S={p>0}; compute the left side by the actual shift,
    # the right by the stated map on spectral points.
    k,m,a=Q(2),Q(1),Q(2)
    for r in [Q(3,4),Q(1),Q(3,2),Q(3)]:
        lhs=values(k,m,shifted(r,a))[1]>0
        map_a=1/a if args.mutation=='forward_spectral_set' else a
        mh,mp,ph,pp=coeff(k,map_a)
        h,p=values(k,m,r)
        rhs=ph*h+pp*p>0
        add('spectral_preimage.r'+str(r),lhs==rhs,{'actual':lhs,'candidate':rhs})

    # Exact positive-cone inequalities, including the two null rays.
    k,beta=Q(2),Q(4)
    for e,p in [(Q(1),Q(0)),(Q(1),Q(2)),(Q(1),Q(-2)),(Q(3),Q(4))]:
        for a in [Q(1,10),Q(10)]:
            c,d=(a+1/a)/2,(a-1/a)/(2*k)
            energy=c*e-d*p
            low,high=min(a,1/a)*e,max(a,1/a)*e
            add('positive_cone.'+str((e,p,a)),low<=energy<=high,
                {'energy':str(energy),'lower':str(low),'upper':str(high)})
    for p,a in [(Q(3),Q(10)),(Q(-3),Q(1,10))]:
        e=Q(1);c,d=(a+1/a)/2,(a-1/a)/(2*k);energy=c*e-d*p
        add('relaxed_cone_fails.'+str(p),p*p<=beta*beta*e*e and energy<0,
            {'admitted_by_wrong_beta_squared':True,'boosted_energy':str(energy)})

    # Exact partial-sum certificates accompany the written infinite-series
    # domain witness. These finite samples alone do not prove divergence.
    c,d=Q(5,4),Q(3,8)
    for n in [1,4,16,64]:
        norm=sum((Q(1,j*j) for j in range(1,n+1)),Q(0))
        hnorm=sum(((Q(j)*Q(1,j))**2 for j in range(1,n+1)),Q(0))
        gnorm=sum(((c*Q(j)-d*Q(10,3)*j)*Q(1,j))**2 for j in range(1,n+1))
        add('domain_cutoff.N'+str(n),norm<=2 and hnorm==n and gnorm==0,
            {'vector_norm_squared':str(norm),'H_norm_squared':str(hnorm),'G_norm_squared':str(gnorm)})

    mass_values=[]
    for m in [Q(1),Q(2)]:
        h,p=values(Q(2),m,Q(3))
        mass_values.append(h*h-p*p/Q(4))
    add('multiple_mass_scope',mass_values==[Q(1),Q(4)],{'mass_squared':[str(v) for v in mass_values]})
    vacuum=cmath.exp(1j*float(Q(2,7)*phase))
    add('canonical_vacuum_fixed',abs(vacuum-1)<1e-11,
        {'energy_shift':str(phase),'vacuum_residual':abs(vacuum-1)})

    passed=sum(r['pass'] for r in rows)
    failed=len(rows)-passed
    result={'mutation':args.mutation,'scope':'author arithmetic/function-action/domain diagnostics; no infinite-volume proof',
            'passed':passed,'failed':failed,'rows':rows}
    # Publication suppresses the named-result write only; the complete result and all active mutation branches remain computed.
    print(f'TOTAL: PASS={passed} FAIL={failed}')
    print('per_element: rational spectral mixing and actual multiplier/shift compositions are checked with the original sign and beta gates.')
    print('per_site: checked and not executed — these abstract representation diagnostics do not construct a finite-range spin density or state.')
    print('per_mode: finite abstract spectral fixtures and a written domain witness are checked; no physical particle or fixed mass is inferred.')
    print('per_block: actual unitary, clock and projection fixtures retain every original insensitive row and active CLI variant.')
    print('lattice_wide: checked and not executed — full integration and maximal domains use the conditional rapid almost-local analytic proof.')
    print('SCOPE: Original finite controls only; documented mutation survivors and insensitive rows remain. Counts do not prove the analytic theorem or a physical model.')
    return int(failed!=0)


if __name__=='__main__':
    raise SystemExit(main())
