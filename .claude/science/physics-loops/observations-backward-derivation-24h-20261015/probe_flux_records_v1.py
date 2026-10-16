"""Exact author controls for a supplied real-transport/threshold candidate."""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as s

AUDIT_TIMEOUT_SEC = 120
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
REPO_INPUTS = [
    ".claude/science/physics-loops/observations-backward-derivation-24h-20261015/NETWORK_EVOLUTION_BLOCK02_v1.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
]
checks = []


def check(name, condition, detail):
    checks.append({"name": name, "pass": bool(condition), "detail": detail})


def rotation(t):
    return s.Matrix([[s.cos(t), -s.sin(t)], [s.sin(t), s.cos(t)]])


def transport_controls():
    a, b = s.symbols('a b', real=True)
    u = s.Matrix([s.Rational(3, 5), s.Rational(4, 5)])
    h = s.Matrix([[1, 1], [1, -1]]) / s.sqrt(2)
    splitter = s.kronecker_product(h, s.eye(2))
    phase = s.diag(rotation(a), rotation(b))
    output = splitter * phase * splitter * s.Matrix.vstack(u, s.zeros(2, 1))
    e0 = s.trigsimp(s.expand_trig(output[:2, :].dot(output[:2, :])))
    e1 = s.trigsimp(s.expand_trig(output[2:, :].dot(output[2:, :])))
    check("real_network_two_fluxes", s.trigsimp(e0-(1+s.cos(a-b))/2) == 0
          and s.trigsimp(e1-(1-s.cos(a-b))/2) == 0,
          {"flux0": str(e0), "flux1": str(e1), "origin": "four-dimensional real matrix propagation"})
    check("total_flux_conserved", s.simplify(e0+e1) == 1, str(s.simplify(e0+e1)))
    common = s.symbols('common', real=True)
    check("common_frame_invariance", s.simplify(e0.subs({a:a+common,b:b+common}, simultaneous=True)-e0) == 0,
          "same rotation on both paths leaves flux fractions unchanged")
    parity_rows=[]
    for x,y in itertools.product((0,1), repeat=2):
        value=s.simplify(e0.subs({a:s.pi*x,b:s.pi*y}))
        parity_rows.append({"x":x,"y":y,"flux0":str(value)})
    check("fresh_binary_settings_control", all(F(row['flux0']) == 1-(row['x'] ^ row['y']) for row in parity_rows), parity_rows)
    # Positive, continuous radial q that obeys only the balanced single-input law.
    mp.mp.dps=60
    def q(r):
        return r*r*(1+mp.mpf('0.5')*mp.sin(4*mp.pi*mp.log(r,2))) if r else mp.mpf(0)
    balanced=[abs(q(r)-2*q(r/mp.sqrt(2))) for r in map(mp.mpf,('0.3','1','2.7'))]
    unequal=q(1)-q(mp.mpf('0.5'))-q(mp.sqrt(3)/2)
    check("one_splitter_angle_insufficient", max(balanced)<mp.mpf('1e-55') and abs(unequal)>mp.mpf('0.1'),
          {"balanced_residual":str(max(balanced)),"unequal_residual":str(unequal),
           "counterexample":"q(r)=r^2[1+0.5 sin(4 pi log_2 r)], q(0)=0"})
    wrong=(1+s.cos(2*(a-b)))/2
    check("wrong_fringe_harmonic_rejected", s.simplify((wrong-e0).subs({a:s.pi/2,b:0})) != 0,
          {"correct_at_pi_over_2":str(e0.subs({a:s.pi/2,b:0})),"wrong":str(wrong.subs({a:s.pi/2,b:0}))})


def step(r0,r1,p):
    z0=int(r0+p>=1)
    z1=int(r1+1-p>1)
    return r0+p-z0,r1+1-p-z1,z0,z1


def counter_controls():
    all_valid=True
    max_discrepancy=F(0)
    steps=0
    for initial in (F(0),F(1,7),F(1,2),F(6,7)):
        for seq in ([F(0)]*32,[F(1)]*32,[F(1,2)]*32,[F(1,3)]*32,
                    [F((7*i+3)%21,20) for i in range(101)]):
            r0,r1=initial,1-initial
            total=F(0); count=0
            for p in seq:
                r0,r1,z0,z1=step(r0,r1,p)
                total+=p; count+=z0; steps+=1
                all_valid &= z0+z1==1 and r0+r1==1 and 0<=r0<1 and 0<r1<=1
                all_valid &= count==total+initial-r0 and abs(count-total)<1
                max_discrepancy=max(max_discrepancy,abs(count-total))
    check("arbitrary_flux_exact_balance_and_complementarity",all_valid,
          {"step_cases":steps,"max_count_flux_discrepancy":str(max_discrepancy)})
    balanced=[]
    for initial in (F(0),F(1,7),F(1,2),F(6,7)):
        r0,r1=initial,1-initial; outputs=[]
        for _ in range(100):
            r0,r1,z0,z1=step(r0,r1,F(1,2));outputs.append(z0)
        balanced.append({"initial_residue":str(initial),"count0":sum(outputs),"first_ten":outputs[:10]})
        assert all(a != b for a,b in zip(outputs,outputs[1:]))
    check("half_flux_alternates_for_every_checked_initial_residue",all(r['count0']==50 for r in balanced),balanced)
    # A wrong strict/weak tie choice creates two records from one incident unit.
    wrong_tie=(int(F(1,2)+F(1,2)>=1),int(F(1,2)+F(1,2)>=1))
    check("symmetric_weak_tie_failure_preserved",sum(wrong_tie)==2,
          {"wrong_output":wrong_tie,"scope":"the explicit asymmetric tie convention is required at equality"})
    rows=[]
    for p in (F(1,4),F(2,5),F(1,2),F(3,4)):
        counts={0:0,1:0,2:0}
        for i,j in itertools.product(range(20),repeat=2):
            _,_,z0,z1=step(F(2*i+1,40),F(2*j+1,40),p)
            counts[z0+z1]+=1
        rows.append({"p":str(p),"zero":str(F(counts[0],400)),"two":str(F(counts[2],400)),
                     "exact_expected_both":str(p*(1-p))})
    check("independent_residue_initialization_loses_exclusivity",
          all(row['zero']==row['two']==row['exact_expected_both'] for row in rows),rows)
    p=F(1,2); reset_each_time=[step(F(1,4),F(3,4),p)[2] for _ in range(20)]
    check("unjustified_fixed_reset_destroys_flux_frequency",sum(reset_each_time)==0,
          {"port0_records":sum(reset_each_time),"total_port0_flux":"10"})


def loss_controls():
    a,b=s.symbols('a b',positive=True)
    d=a+b-a*b
    transition=s.Matrix([[a*(1-b),b],[a,b*(1-a)]])/d
    stationary=s.Matrix([[a/(a+b),b/(a+b)]])
    check("loss_transition_normalization_and_stationarity",
          all(s.simplify(sum(transition[i,j] for j in range(2))-1)==0 for i in range(2))
          and all(s.simplify(v)==0 for v in stationary*transition-stationary),
          {"transition":str(transition),"stationary":str(stationary)})
    eigen=s.simplify(transition.trace()-1)
    check("loss_nontrivial_eigenvalue",s.simplify(eigen+a*b/d)==0,{"eigenvalue":str(eigen)})
    # Direct sum of physical missed-pair strings, bounded by their exact remainder.
    for ea,eb in ((s.Rational(1,4),s.Rational(3,4)),(s.Rational(4,5),s.Rational(4,5)),(s.S.One,s.S.One)):
        cycle=(1-ea)*(1-eb); limit=20
        direct=s.Matrix([[sum(ea*(1-eb)*cycle**k for k in range(limit)),sum(eb*cycle**k for k in range(limit))],
                         [sum(ea*cycle**k for k in range(limit)),sum(eb*(1-ea)*cycle**k for k in range(limit))]])
        exact=transition.subs({a:ea,b:eb})
        residual=exact-direct
        check("missed_pair_geometric_sum_"+str(ea)+'_'+str(eb),
              all(v>=0 for v in residual) and all(s.simplify(residual[i,j]-exact[i,j]*cycle**limit)==0 for i,j in itertools.product(range(2),repeat=2)),
              {"tail_factor":str(cycle**limit),"exact_transition":str(exact)})
    eta,n=s.symbols('eta n',positive=True)
    threshold=n*eta*(1-eta)/2
    bernoulli=n*(eta/2)*(1-eta/2)
    check("heralded_even_bin_variance_difference",s.simplify(bernoulli-threshold-n*eta**2/4)==0,
          {"threshold":str(threshold),"Bernoulli_comparator":str(bernoulli),"difference":str(n*eta**2/4)})
    check("equal_efficiency_lag_one",s.simplify(eigen.subs({a:eta,b:eta})+eta/(2-eta))==0,
          {"lag_one":"-eta/(2-eta)"})


def main():
    transport_controls();counter_controls();loss_controls()
    identities={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in REPO_INPUTS}
    identities[str(Path(__file__).resolve().relative_to(ROOT))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result={"status":"author synthetic development controls","empirical_validation":False,
            "independent_check":False,"sources_sha256":identities,"checks":checks,
            "total":{"pass":sum(c['pass'] for c in checks),"fail":sum(not c['pass'] for c in checks)}}
    (HERE/'FLUX_RECORD_CONTROLS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['total']['fail']==0 else 1)


if __name__=='__main__':
    main()
