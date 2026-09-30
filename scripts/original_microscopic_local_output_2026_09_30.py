#!/usr/bin/env python3
"""Exact finite controls for the original microscopic output theorem.

These controls test actual source words and their original mark/register
conventions, elementary normalized-spin bounds, and the required electric
halo. They do not simulate a torus, estimate a physical constant, establish
an infinite-volume theorem, or execute historical campaign runners. Expected
values are independently derived in CONTROL_DERIVATIONS.md. Only the literal
source paths below are read, for identity binding; the fixtures are defined
here. All arithmetic is integer or Fraction, including radical comparisons.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/ORIGINAL_MICROSCOPIC_LOCAL_OUTPUT_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/proofs/original_microscopic_output_2026_09_30/normal_form_and_moments.md",
    "docs/proofs/original_microscopic_output_2026_09_30/original_gain_and_history.md",
    "docs/proofs/original_microscopic_output_2026_09_30/local_trajectory_and_rotor_limit.md",
    "docs/proofs/original_microscopic_output_2026_09_30/neutral_dissipator_and_linear_field_gain.md",
    "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
]
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/original_microscopic_local_output_2026_09_30.json"

# Mutations are applied only to isolated scratch copies, never to a live cache.
BIRTH_SHIFT_SIGN = 1
COHERENT_AMPLITUDE = Q(1)
DROP_SPIN_BOUNDARY = False
OUTSIDE_ZERO = True
OVERFLOW_LOSS = True
UPDATE_ALL_WORDS = True
INCLUDE_INCIDENT_LINKS = True
LINEAR_SHIFT_BUDGET = 2
WORD_ERROR_FACTOR = 2

RESULTS = {}
FAILURES = []


def check(name, condition, evidence):
    ok = bool(condition)
    RESULTS[name] = {"pass": ok, "evidence": evidence}
    print(("PASS " if ok else "FAIL ") + name + " " + json.dumps(evidence, sort_keys=True))
    if not ok:
        FAILURES.append(name)


def norm2(v):
    return sum((x*x for x in v.values()), Q(0))


def spin_squared(S, m, shift):
    if abs(m) > S:
        return Q(0) if OUTSIDE_ZERO else Q(1)
    if abs(m+shift) > S:
        return Q(1) if DROP_SPIN_BOUNDARY else Q(0)
    return Q(1)-Q(m*(m+shift), S*(S+1))


def radical_error_leq(g2, bound):
    """Decide (1-sqrt(g2))^2 <= bound exactly by sign then squaring."""
    if g2 < 0 or bound < 0:
        return False
    left = 1+g2-bound
    return left <= 0 or left*left <= 4*g2


OMEGA = (1, (0,)*6, (0,)*6)


def hop(state, d, S):
    qa, bs, es = state
    if qa == 0 or bs[d] != 0:
        return None
    shift = -qa  # local link orientation is A -> B
    amp2 = spin_squared(S, es[d], shift)
    if not amp2:
        return None
    b = list(bs); e = list(es)
    b[d] = qa; e[d] += shift
    return (0, tuple(b), tuple(e)), amp2


def birth(state, b, sign, S):
    qa, bs, es = state
    if qa != 0 or bs[b] != 0:
        return None
    shift = BIRTH_SHIFT_SIGN*sign
    amp2 = spin_squared(S, es[b], shift)
    if not amp2:
        return None
    q = list(bs); e = list(es)
    q[b] = -sign; e[b] += shift
    return (sign, tuple(q), tuple(e)), amp2


def gauss(state):
    qa, bs, es = state
    return (sum(es)-(qa-1),) + tuple(-es[d]-bs[d] for d in range(6))


def source_vector(S, b, signs):
    out = {}
    for d in range(6):
        h = hop(OMEGA, d, S)
        if h is None:
            continue
        mid, h2 = h
        for sign in signs:
            j = birth(mid, b, sign, S)
            if j is None:
                continue
            state, j2 = j
            # These specific zero-field paths have exact unit amplitudes.
            if h2*j2 != 1:
                raise AssertionError("Omega source branch is not unit weighted")
            amplitude = COHERENT_AMPLITUDE if len(signs)==2 else Q(1)
            out[state] = out.get(state,Q(0))+amplitude
    return out


def word_controls():
    distinct = set(); marked = set(); field_bad = 0; residual = 0
    counts = []
    for S in (1,2,5):
        for b in range(6):
            v = source_vector(S,b,(-1,1))
            vp = source_vector(S,b,(1,)); vm = source_vector(S,b,(-1,))
            counts.append((norm2(vp),norm2(vm),norm2(v)))
            for state in v:
                distinct.add(state); marked.add((b,state))
                residual = max(residual,*map(abs,gauss(state)))
                field_bad += int(max(map(abs,state[2]))>S)
    check("original_source_words", all(c==(5,5,10) for c in counts)
          and len(distinct)==45 and len(marked)==60 and residual==0 and field_bad==0,
          {"spins":[1,2,5],"marked_branches":len(marked),"physical_states":len(distinct),
           "resolved_and_coherent_norm2":[str(x) for x in counts[0]],
           "max_gauss_residual":residual,"invalid_spin_outputs":field_bad})
    v=source_vector(1,1,(-1,1)); vp=source_vector(1,1,(1,)); vm=source_vector(1,1,(-1,))
    plus=next(iter(vp)); minus=next(iter(vm))
    cross=v.get(plus,0)*v.get(minus,0)
    resolved_cross=vp.get(plus,0)*vp.get(minus,0)+vm.get(plus,0)*vm.get(minus,0)
    weighted=sum((Q(1+sum(map(abs,s[2])))*a*a for s,a in v.items()),Q(0))
    check("coherent_original_gain_and_linear_weight", cross==1 and resolved_cross==0
          and weighted==30 and all(sum(map(abs,s[2]))<=LINEAR_SHIFT_BUDGET for s in v),
          {"coherent_cross_entry":str(cross),"resolved_cross_entry":str(resolved_cross),
           "linear_weighted_gain":str(weighted),"declared_shift_budget":LINEAR_SHIFT_BUDGET})


def spin_controls():
    count=0; worst=Q(0); failures=[]; outside=[]; minima=[]
    for S in (1,2,3,5,8,12):
        vals=[]
        for m in range(-S-2,S+3):
            for shift in (-1,1):
                g2=spin_squared(S,m,shift)
                count+=1
                if not radical_error_leq(g2,Q(abs(m),S)):
                    failures.append([S,m,shift])
                if abs(m)>S:
                    outside.append(g2==0)
            if abs(m)<=S:
                total=spin_squared(S,m,1)+spin_squared(S,m,-1)
                vals.append(total)
                expected=2*(Q(1)-Q(m*m,S*(S+1)))
                worst=max(worst,abs(total-expected))
        minima.append((min(vals),Q(2,S+1)))
    check("spin_boundary_and_common_carrier", not failures and worst==0
          and all(outside) and all(x==y for x,y in minima),
          {"elementary_cases":count,"max_loss_identity_error":str(worst),
           "failed_inequalities":failures[:5],"outside_box_zero":all(outside),
           "minimum_losses":[str(x) for x,y in minima]})
    count=0; bad=[]; legal=0
    # The two links of j_b F_d are distinct. Right-letter shifts do not
    # change the field entering the other letter.
    for S in (1,2,3,5):
        for m,n in itertools.product(range(-S-1,S+2),repeat=2):
            for q,sign in itertools.product((-1,1),repeat=2):
                h2=spin_squared(S,m,-q); j2=spin_squared(S,n,sign)
                amp2=h2*j2
                bound=Q(WORD_ERROR_FACTOR,S)*(abs(m)+abs(n))
                count+=1
                if not radical_error_leq(amp2,bound):
                    bad.append([S,m,n,q,sign])
                if amp2:
                    legal+=1
                    if abs(abs(m-q)+abs(n+sign)-abs(m)-abs(n))>LINEAR_SHIFT_BUDGET:
                        bad.append(["displacement",S,m,n,q,sign])
    check("actual_two_link_source_word_bound", not bad,
          {"branch_cases":count,"nonzero_branches":legal,"failed_cases":bad[:5],
           "bound":"2(|m|+|n|)/S; exact radical sign-and-square evaluation"})


def register_controls():
    # The input is the actual physical one-hole word F_0 Omega. The mark
    # is the original coherent birth at a different edge 1, with two
    # unit-amplitude outputs, preserving their same-mark coherence.
    mid=hop(OMEGA,0,1)[0]
    v={birth(mid,1,sg,1)[0]:COHERENT_AMPLITUDE for sg in (-1,1)}
    rate=norm2(v)
    states=[(),((0,1),),((1,1),),"overflow"]
    probabilities=[Q(1,10),Q(2,10),Q(3,10),Q(4,10)]
    g=[0,3,5,7]
    gain=[Q(0)]*4; loss=[Q(0)]*4; cross=[Q(0)]*4
    for z in range(4):
        new=1 if z==0 else 3
        if UPDATE_ALL_WORDS or z!=3:
            gain[new]+=rate*probabilities[z]
            cross[new]+=list(v.values())[0]*list(v.values())[1]*probabilities[z]
        if OVERFLOW_LOSS or z!=3:
            loss[z]+=rate*probabilities[z]
    drift=sum((g[z]*(gain[z]-loss[z]) for z in range(4)),Q(0))
    check("original_register_gain_loss_and_overflow", rate==2 and sum(gain)==2
          and sum(gain)-sum(loss)==0 and drift==Q(17,5)
          and gain[3]==Q(9,5) and cross[3]==Q(9,10),
          {"original_bare_jump_rate":str(rate),"total_gain":str(sum(gain)),
           "total_gain_minus_loss":str(sum(gain)-sum(loss)),"test_drift":str(drift),
           "overflow_gain":str(gain[3]),"same_mark_overflow_cross":str(cross[3]),
           "input_gauss":list(gauss(mid)),"word_count":len(states)})


def electric_controls():
    # X contains only a B matter site. Its adjacent electric coefficient
    # does not commute with the occupancy-flipping test on that site.
    b=(1,0,0)
    directions=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    incident={tuple(sorted((b,tuple(b[i]+d[i] for i in range(3))))) for d in directions}
    halo=incident if INCLUDE_INCIDENT_LINKS else set()
    maxima=[]
    for R in (1,2,5):
        # In occupancy basis, D=diag(E(E-1),0) and O swaps the two
        # occupancy states. The commutator's off-diagonal coefficient
        # gives its exact singular value, computed directly here.
        entries=[]
        O=((0,1),(1,0))
        for m in range(-R,R+1):
            D=((m*(m-1),0),(0,0))
            comm=[[sum(D[i][k]*O[k][j]-O[i][k]*D[k][j] for k in range(2))
                   for j in range(2)] for i in range(2)]
            assert comm[0][0]==comm[1][1]==0 and comm[0][1]==-comm[1][0]
            entries.append(abs(comm[0][1]))
        maxima.append(max(entries))
    check("electric_occupancy_halo", len(halo)==6 and maxima==[2,6,30],
          {"incident_edges":len(incident),"cutoff_halo_edges":len(halo),
           "commutator_norms_R_1_2_5":maxima,
           "scope":"local tensor operator control; not a physical state preparation"})


def main():
    bindings={path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
              for path in AUDIT_INPUT_PATHS}
    word_controls(); spin_controls(); register_controls(); electric_controls()
    result={"scope":"exact finite controls; analytic theorem and source selection not numerically certified",
            "inputs":bindings,"runner_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "arithmetic":"integer/Fraction; radical inequality reduced exactly by sign and squaring",
            "checks":RESULTS,"failures":FAILURES,"pass_count":len(RESULTS)-len(FAILURES),
            "fail_count":len(FAILURES)}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(f"TOTAL: PASS={result['pass_count']} FAIL={result['fail_count']}")
    return int(bool(FAILURES))


if __name__=="__main__":
    raise SystemExit(main())
