#!/usr/bin/env python3
"""Finite author controls for the supplied uniform local autonomous construction.

Exact integer/rational word, support and clock-prefix controls; small floating
matrix checks of the generic dilation/positive-controller identities. The latter
are not a physical calibration or a simulation of the whole rotor process.
No finite control proves the analytic all-volume/all-tolerance theorem.
Scientific inputs are the literal source files in AUDIT_INPUT_PATHS, read only
for source binding. Mathematical fixtures are specified here. Integrity reads
also include this runner for its hash. No old output or campaign report is read.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/UNIFORM_AUTONOMOUS_RESOURCE_DENSITY_FOR_ORIGINAL_ROTOR_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md",
]
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/uniform_autonomous_original_record_resource_density_2026_09_30.json"

# Literal switches are changed only in scratch mutation copies, never in a cache.
BIRTH_SHIFT = 1
COHERENT_FACTOR = 1.0
COPY_SIGN = False
COMPRESS_INTERNAL = False
COLOR_RADIUS = 2
RESET_ON_NOEVENT = False
CLOCK_BAND_SLACK = 0
WRAP_CLOCK = False
INCLUDE_INTERACTION = True

RESULTS: dict[str, dict] = {}
FAILURES: list[str] = []


def check(name, condition, evidence):
    ok = bool(condition)
    RESULTS[name] = {"pass": ok, "evidence": evidence}
    print(("PASS " if ok else "FAIL ") + name + " " + json.dumps(evidence, sort_keys=True))
    if not ok:
        FAILURES.append(name)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def adjoint(a):
    return a.conj().T


def trace_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())


def elementary_birth(aq, bs, b, d, sigma):
    """Execute actual F then j on occupation and oriented electric shifts."""
    if bs[d] or bs[b] or d == b:
        return None
    matter = list(bs)
    field = [0] * 6
    matter[d] = aq
    field[d] -= aq
    a_after_f = 0
    assert a_after_f == 0
    matter[b] = -sigma
    field[b] += BIRTH_SHIFT * sigma
    return sigma, tuple(matter), tuple(field)


def words():
    paths = 0
    worst_gauss = 0
    wrong_gain = 0
    by_o = {o: set() for o in range(7)}
    for aq in (-1, 1):
        for bs in itertools.product((-1, 0, 1), repeat=6):
            count = 0
            for b, d in itertools.permutations(range(6), 2):
                for sigma in (-1, 1):
                    out = elementary_birth(aq, bs, b, d, sigma)
                    if out is None:
                        continue
                    qa, qs, es = out
                    # Independent charge-divergence check, not the word formula.
                    residual = [sum(es) - (qa-aq)]
                    residual.extend(-es[j] - (qs[j]-bs[j]) for j in range(6))
                    worst_gauss = max(worst_gauss, max(map(abs, residual)))
                    assert sum(q != 0 for q in qs) == sum(q != 0 for q in bs)+2
                    assert sum(map(abs, es)) == 2
                    paths += 1
                    count += 1
            empty = bs.count(0)
            wrong_gain += count != 2*empty*(empty-1)
            by_o[6-empty].add(count)
    check("original_words_and_gain", worst_gauss == 0 and wrong_gain == 0,
          {"matter_inputs": 2*3**6, "nonzero_words": paths,
           "max_gauss_residual": worst_gauss,
           "basis_gain_counts_by_occupied": {str(o): sorted(v) for o,v in by_o.items()}})


def star(center):
    ans = set()
    for axis in range(3):
        for sign in (-1, 1):
            p = list(center)
            p[axis] += sign
            ans.add(tuple(p))
    return ans


def geom_and_compression():
    zero = (0, 0, 0)
    offsets = [p for p in itertools.product(range(-2,3), repeat=3)
               if sum(map(abs,p)) == 2]
    overlap = [p for p in offsets if star(zero) & star(p)]
    axial = star(zero) | star((2,0,0))
    diag = star(zero) | star((1,1,0))
    ball = [p for p in itertools.product(range(-4,5), repeat=3)
            if sum(map(abs,p)) <= 4]
    # Greedy coloring on an L=8 torus; test against the true overlap graph.
    side = 8
    centers = [p for p in itertools.product(range(side),repeat=3) if sum(p)%2 == 0]
    colors = {}
    for p in centers:
        nbr = {tuple((p[j]+v[j])%side for j in range(3)) for v in offsets
               if sum(map(abs,v)) <= COLOR_RADIUS}
        used = {colors[v] for v in nbr if v in colors}
        colors[p] = next(c for c in range(19) if c not in used)
    conflicts = sum(colors[p] == colors[tuple((p[j]+v[j])%side for j in range(3))]
                    for p in centers for v in overlap)
    check("local_geometry_and_colors", len(overlap)==18 and len(ball)==129 and
          len(axial)==11 and len(diag)==10 and conflicts==0,
          {"overlap_degree": len(overlap), "radius_four_cells":len(ball),
           "axial_B_cells":len(axial), "diagonal_B_cells":len(diag),
           "L8_colors_used":len(set(colors.values())), "directed_conflicts":conflicts})
    # Actual outward two-center words, starting at zero fields and plus charges.
    # The axial pair shares one B. Distinct destinations give independent shifts.
    out = {}
    for b in star(zero):
        for d in star((2,0,0)):
            if b == d:
                continue
            field = tuple(sorted(((zero,b,-1),((2,0,0),d,-1))))
            out[field] = out.get(field,0)+1
    norm_squared = sum(v*v for v in out.values())
    complete_R0_diagonal = -2*norm_squared
    selected = 0 if COMPRESS_INTERNAL else complete_R0_diagonal
    check("whole_magnetic_compression", selected == -70,
          {"actual_S_outputs":len(out), "norm_squared":norm_squared,
           "whole_A_Omega_diagonal_delta1":selected,
           "separately_clipped_F_at_R0_diagonal":0})


def copied_original_marks():
    # Omega and its 60 ORIGINAL source-plus-edge-mark birth branches.
    # Source states may coincide across different original edge labels.
    branches = [(b,s,d) for b in range(6) for s in (-1,1) for d in range(6) if d!=b]
    outputs = [elementary_birth(1,(0,)*6,b,d,s) for b,s,d in branches]
    source_states = {out: i+1 for i,out in enumerate(dict.fromkeys(outputs))}
    assert len(source_states) == 45
    assert len({(out,b) for out,(b,s,d) in zip(outputs,branches)}) == 60
    tau = 1/240
    # Original coherent edge b=0: sum both sigma, 5 destinations each.
    chosen = [i for i,(b,s,d) in enumerate(branches) if b == 0]
    dim_source = len(source_states)+1
    physical_chosen = [source_states[outputs[i]] for i in chosen]
    amp = np.zeros(dim_source, complex)
    amp[physical_chosen] = COHERENT_FACTOR*math.sqrt(tau)
    expected = np.zeros((dim_source,dim_source), complex)
    expected[np.ix_(physical_chosen,physical_chosen)] = tau
    got = np.outer(amp,amp.conj())
    if COPY_SIGN:
        for i in chosen:
            for j in chosen:
                if branches[i][1] != branches[j][1]:
                    got[source_states[outputs[i]],source_states[outputs[j]]] = 0
    mark_error = trace_norm(got-expected)
    # Fractional Julia pulse within its only nontrivial Omega/image plane.
    # e0 is blank Omega; e1 is the normalized sum of the original branches,
    # each paired with its matching physical flag and copy.
    theta = math.asin(math.sqrt(60*tau))
    sy = np.array([[0,-1j],[1j,0]],complex)
    G = math.pi*np.eye(2)+(theta-math.pi)*sy
    eig, vec = np.linalg.eigh(G)
    U = (vec*np.exp(-1j*eig))@adjoint(vec)
    ideal = np.array([[math.cos(theta),-math.sin(theta)],
                      [math.sin(theta),math.cos(theta)]],complex)
    # Build the actual original-branch vector in source x edge-flag x copy.
    # Execute the rank-two fractional Julia operator BEFORE modular copying.
    # No dense 46*7*7 unitary is needed; its nonidentity plane is computed above.
    pulse_errors = []
    copied_offdiagonal = []
    matched_leakage = []
    for area in (0,0.2,0.7,1):
        v = (vec*np.exp(-1j*area*eig))@adjoint(vec)@np.array([1,0])
        p_blank, p_event = map(float,abs(v)**2)
        pulse_errors.append(abs(p_blank+p_event-1))
        pre = np.zeros((dim_source,7,7),complex)
        pre[0,0,0]=v[0]
        for j,(b,s,d) in enumerate(branches):
            pre[source_states[outputs[j]],b+1,0]+=v[1]/math.sqrt(60)
        post=np.empty_like(pre)
        for f in range(7):
            post[:,f,:]=np.roll(pre[:,f,:],f,axis=1)
        leakage=sum(float(np.vdot(post[:,f,e],post[:,f,e]).real)
                    for f in range(7) for e in range(7) if f!=e)
        off=max(np.linalg.norm(post[:,f,:]@adjoint(post[:,g,:]))
                for f in range(7) for g in range(7) if f!=g)
        matched_leakage.append(leakage); copied_offdiagonal.append(float(off))
    check("original_coherent_copy_and_Julia", mark_error<2e-13 and
          np.linalg.norm(U-ideal)<2e-13 and min(eig)>=0 and max(eig)<=2*math.pi
          and max(matched_leakage)<2e-13 and max(copied_offdiagonal)<2e-13,
          {"distinct_physical_source_states":len(source_states),
           "distinct_original_source_mark_branches":len(branches),
           "coherent_original_edge_trace":float(np.trace(got).real),
           "coherent_map_trace_error":mark_error,
           "Julia_blank_event_probability":float(abs(U[1,0])**2),
           "expected_original_total_gain":60*tau,
           "positive_log_spectrum":eig.tolist(),
           "fractional_pulse_normalization_error":max(pulse_errors),
           "fractional_matched_code_leakage":max(matched_leakage),
           "flag_crossblock_after_copy_trace":max(copied_offdiagonal)})


def append_register():
    # One scalar source gain, two preexisting word values and overflow value.
    # This tests the near-identity extension, including coherent proof inputs.
    tau, g = 1/1000, 3.0
    v = np.array([1,1,0],complex)/math.sqrt(2)
    rho = np.outer(v,v.conj())
    append = (1,2,2)
    gain = np.zeros((3,3),complex)
    for w in range(3):
        gain[append[w],append[w]] += g*rho[w,w]
    noevent = (1-tau*g)*rho
    if RESET_ON_NOEVENT:
        noevent = np.diag([(1-tau*g),0,0]).astype(complex)
    out = noevent+tau*gain
    distance = trace_norm(out-rho)
    # Kraus adjoint products of append-with-overflow, explicitly accumulated.
    gram = np.zeros((3,3))
    for w in range(3):
        k = np.zeros((3,3)); k[append[w],w]=math.sqrt(g)
        gram += k.T@k
    overflow = np.diag([0,0,1]).astype(complex)
    overflow_after = (1-tau*g)*overflow + tau*g*overflow
    check("per_center_append_near_identity", distance<=3*g*tau+1e-14 and
          np.max(abs(gram-g*np.eye(3)))<1e-14 and
          np.max(abs(overflow_after-overflow))<1e-14,
          {"coherent_word_input_trace_distance":distance, "bound":3*g*tau,
           "gain_loss_gram_error":float(np.max(abs(gram-g*np.eye(3)))),
           "overflow_keeps_physical_gain_rate":g})


def add(out, key, value):
    if value:
        out[key] = out.get(key,Q(0))+value
        if not out[key]:
            del out[key]


def rational_h(vector, cap):
    # Two degree-one positive Fourier clocks and noncommuting positive payloads.
    # Common scalar positive shifts are removed in BOTH sides of this prefix test.
    Gs = (((Q(1),Q(1,2)),(Q(1,2),Q(1))),
          ((Q(2),Q(0)),(Q(0),Q(1))))
    out = {}
    for (m1,m2,q),v in vector.items():
        add(out,(m1,m2,q),v*(m1+m2+2*q))
        for c,G in enumerate(Gs):
            for shift,weight in ((-1,1),(0,2),(1,1)):
                ms=[m1,m2]; ms[c]+=shift
                if abs(ms[c])>cap:
                    if not WRAP_CLOCK:
                        continue
                    ms[c]= -cap if ms[c]>cap else cap
                for p in range(2):
                    add(out,(ms[0],ms[1],p),v*weight*G[p][q])
    return out


def clock_prefix():
    k0, degree, order = 1,1,4
    init = {(i,j,0):Q(1) for i in range(-k0,k0+1) for j in range(-k0,k0+1)}
    cap=k0+degree*order+CLOCK_BAND_SLACK
    v,w,small=init,init,init
    equal=[]; boundary=[]
    for j in range(order+1):
        equal.append(v==w)
        boundary.append(v==small)
        v=rational_h(v,8); w=rational_h(w,cap); small=rational_h(small,2)
    # Direct absent matrix element separates Toeplitz from cyclic compression.
    edge=rational_h({(cap,0,0):Q(1)},cap)
    wrap_element=edge.get((-cap,0,0),Q(0))
    check("finite_clock_prefix_and_Toeplitz", all(equal) and not all(boundary)
          and wrap_element==0,
          {"k0":k0,"degree":degree,"prefix_order":order,"selected_Kc":cap,
           "exact_prefix_equalities":equal,"Kc2_equalities":boundary,
           "cyclic_boundary_element":str(wrap_element),"largest_sparse_vector":len(v)})


def controller_ledger():
    # Universal finite apparatus identity, not a rotor-energy calibration.
    # A source qubit and matched flag/copy code use the actual Julia angle for
    # the original Omega gain 60 at tau=1/240; two positive local clocks drive it.
    Kc=1; cd=2*Kc+1; pd=8
    shift=np.diag(np.ones(cd-1),1)
    f1=2*np.eye(cd)+shift+shift.T
    f2=2*np.eye(cd)+0.5j*shift-0.5j*shift.T
    theta=math.asin(0.5)
    sy=np.array([[0,-1j],[1j,0]])
    gsmall=math.pi*np.eye(2)+(theta-math.pi)*sy
    G=np.zeros((pd,pd),complex); G[np.ix_([0,7],[0,7])]=gsmall
    G2=0.7*G
    hp=np.diag([0]*4+[1]*4)
    cp=np.diag(np.arange(cd,dtype=float))
    eye=np.eye(cd)
    hs=np.kron(np.eye(cd*cd),hp)
    hc=np.kron(np.kron(cp,eye)+np.kron(eye,cp),np.eye(pd))
    V=np.kron(np.kron(f1,eye),G)+np.kron(np.kron(eye,f2),G2)
    H=hs+hc+V
    beta=np.zeros(cd); beta[Kc]=1
    psi=np.kron(np.kron(beta,beta),np.eye(pd)[:,0]).astype(complex)
    e,u=np.linalg.eigh(H)
    final=u@(np.exp(-0.137j*e)*(adjoint(u)@psi))
    mean=lambda a,v:float(np.vdot(v,a@v).real)
    ds=mean(hs,final)-mean(hs,psi)
    dc=mean(hc,final)-mean(hc,psi)
    dv=mean(V,final)-mean(V,psi)
    residual=dc+ds+(dv if INCLUDE_INTERACTION else 0)
    rho=np.outer(final,final.conj())
    # Read the middle payload bit (flag), retaining source and clock unchanged.
    masks=[np.array([(j//2)%2==b for j in range(pd)]) for b in (0,1)]
    projectors=[np.kron(np.eye(cd*cd),np.diag(m.astype(float))) for m in masks]
    read=sum(p@rho@p for p in projectors)
    envelope=2*math.pi*np.kron(np.kron(f1,eye)+np.kron(eye,f2),np.eye(pd))
    before=float(np.trace(rho@V).real); after=float(np.trace(read@V).real)
    env_before=float(np.trace(rho@envelope).real)
    env_after=float(np.trace(read@envelope).real)
    free_read=float(np.trace((read-rho)@(hs+hc)).real)
    ok=(min(np.linalg.eigvalsh(f1))>=-1e-12 and min(e)>=-1e-12 and
        abs(residual)<2e-11 and abs(ds+dc)>1e-4 and abs(free_read)<1e-12 and
        abs(env_before-env_after)<1e-11 and
        -1e-12<=before<=env_before+1e-11 and -1e-12<=after<=env_after+1e-11)
    check("positive_controller_and_postread_ledger",ok,
          {"dimension":len(H),"min_total_eigenvalue":float(min(e)),
           "min_Fourier_compression_eigenvalue":float(min(np.linalg.eigvalsh(f1))),
           "source_delta":ds,"clock_delta":dc,"interaction_delta":dv,
           "complete_mean_ledger_residual":residual,
           "omitting_interaction_residual":ds+dc,"read_free_energy_change":free_read,
           "pre_read_interaction":before,"post_read_interaction":after,
           "pre_read_clock_envelope":env_before,"post_read_clock_envelope":env_after})


def main():
    for f in (words,geom_and_compression,copied_original_marks,append_register,
              clock_prefix,controller_ledger):
        try:
            f()
        except Exception as exc:
            check(f.__name__+"_execution",False,{"exception":repr(exc)})
    packet={"scope":"finite author corroboration; analytic uniform theorem is in source",
            "numpy_version":np.__version__,"runner_sha256":sha(Path(__file__)),
            "declared_source_bindings":{p:sha(ROOT/p) for p in AUDIT_INPUT_PATHS},
            "results":RESULTS,"failures":FAILURES}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n")
    print("Scientific source bindings are distinct from the runner self-integrity read.")
    print(f"TOTAL: PASS={sum(r['pass'] for r in RESULTS.values())} FAIL={len(FAILURES)}")
    return bool(FAILURES)


if __name__ == "__main__":
    raise SystemExit(main())
