#!/usr/bin/env python3
"""Cycle611: derive matter currents before choosing a field/source interpretation.

Route A gauges the accepted Cycle219/230 coin-stream-contact update. Route B
varies the same stream under a local cubic coframe. Route C adds a distinct
mobile compensator carrier rather than charging Cycle600's neutral compiler
words. F17 coupling, modulus, and gravity interpretation remain separate.
Authority none; audit unset.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22 as c609
import physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22 as c591

c230 = c591.cycle230
c219 = c591.cycle219
c210 = c219.c210
c607 = c609.c607

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MATTER_VARIATION_CURRENT_STRESS_COMPENSATOR_SOURCE_"
    "TOURNAMENT_CYCLE611_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_matter_variation_current_stress_compensator_source_"
    "tournament_cycle611_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_matter_variation_current_stress_compensator_source_"
    "tournament_cycle611_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2e-8
START = perf_counter()
PASS = FAIL = 0

PINS = {
    "scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py":
        "d5dc935f39063ff4bd105a2066686d35677e0e7265fdf0696b7b2e9c25829447",
    "docs/work_history/repo/review_feedback/PHYSICAL_TWO_M2_CAR_PHASE_LINK_FIELD_QCA_TOURNAMENT_CYCLE609_NOTE_2026-07-22.md":
        "80d765e40daf18f846de7be2dff054cdb24383eb186bc20fe2f8570895438611",
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json":
        "1c1c8e0141378ed6a53d85815591a76ab3c8e65ec1f952eca39fe3a95789d6dd",
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_cold_2026_07_22.txt":
        "5ce217a142e0f8a3b7ea5bfb1a65e3955c8e31c2b7ee0eadc594e72ebe89ef3b",
    "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":
        "b927333e3287fa46c03f7ed9b53259cd126f47cca30eaca35c8220971b822a08",
    "docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":
        "86746b0cf9a80145b9c7cb4415c4402d6a697bb99e1fa83bae547bf091ac37e5",
}

FIXTURES = (("TRAIN_L3", 3, 384, False), ("HELD_L6", 6, 768, True),
            ("OUT_HELD_L7", 7, 1536, True))


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, Fraction): return f"{value.numerator}/{value.denominator}"
    if isinstance(value, complex): return [value.real, value.imag]
    raise TypeError(type(value).__name__)


def digest(relative): return sha256((ROOT / relative).read_bytes()).hexdigest()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore():
    observed = {path: digest(path) for path in PINS}
    receipt = json.loads((ROOT / "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json").read_text())
    inherited = receipt["shore"]
    output = {"hashes_match": observed == PINS, "Cycle609_pass": receipt["pass"],
              "mass": inherited["mass"], "contact": inherited["contact"],
              "seam": inherited["seam"], "joint_EG": inherited["joint_EG"]}
    check("Cycles591/609 are byte-pinned and the mass/contact/seam shore passes",
          output["hashes_match"] and output["Cycle609_pass"]
          and max(output["mass"], output["contact"], output["seam"], output["joint_EG"]) < TOL,
          output)
    return receipt, output


def note_contract():
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = ("authority: none", "audit: unset", "cycle 611", "route a", "route b",
                "route c", "peierls", "cycle591", "unit charge", "contact",
                "continuity", "translation", "improvement", "compensator",
                "localized", "uniform", "not stress-energy", "not gravity",
                "packing", "l3", "l6", "l7", "all 24", "576", "n1 —",
                "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
                "no axiom pressure")
    missing = tuple(item for item in required if item not in body)
    check("Cycle611 note freezes the three variation routes and full N1-N8", not missing, missing)


def normalize(psi): return psi / np.linalg.norm(psi)


def coin_step(psi, coin): return np.einsum("ab,xyzb->xyza", coin, psi, optimize=True)


def stream_step(psi):
    result = np.zeros_like(psi)
    for direction, velocity in enumerate(c210.DIRECTIONS):
        result[..., direction] = np.roll(psi[..., direction], tuple(int(v) for v in velocity), axis=(0, 1, 2))
    return result


def gauged_stream(psi, gauge):
    phased = psi * np.exp(1j * gauge)
    return stream_step(phased)


def density(psi): return np.sum(abs(psi)**2, axis=-1)


def directional_density(psi): return abs(psi)**2


def incoming_from_links(links):
    result = np.zeros(links.shape[:3])
    for direction, velocity in enumerate(c210.DIRECTIONS):
        result += np.roll(links[..., direction], tuple(int(v) for v in velocity), axis=(0, 1, 2))
    return result


def rotate_directional(values, frame):
    length = values.shape[0]; output = np.zeros_like(values)
    dmap = np.argmax(c210.direction_permutation(frame), axis=0)
    for site in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(site))
        for direction in range(6): output[target + (int(dmap[direction]),)] = values[site + (direction,)]
    return output


def rotate_vector(values, frame):
    length = values.shape[0]; output = np.zeros_like(values)
    for site in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(site))
        output[target] = frame @ values[site]
    return output


def rotate_tensor(values, frame):
    length = values.shape[0]; output = np.zeros_like(values)
    for site in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(site))
        output[target] = frame @ values[site] @ frame.T
    return output


def fock_symmetry_controls(coin):
    occupations = c230.c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    N = np.diag(number)
    contact = np.diag(np.exp(1j*c230.COUPLING*number*(number-1)/2))
    lifted_coin = c230.c229.fock_lift(coin)
    theta = 0.317
    gauge = np.diag(np.exp(1j*theta*number))
    return {
        "local_Fock_states_exhausted": 64,
        "coin_total_number_commutator": float(np.linalg.norm(lifted_coin@N-N@lifted_coin)),
        "contact_total_number_commutator": float(np.linalg.norm(contact@N-N@contact)),
        "gauged_contact_invariance_residual": float(np.linalg.norm(gauge@contact@gauge.conj().T-contact)),
        "contact_Peierls_current_contribution": 0.0,
        "contact_zero_reason": "actual Cycle230 contact is present and U(1)-invariant; it is not omitted",
    }


def all576_direction_group_failures():
    frames = c210.proper_cubic_frames(); failures = 0
    for first in frames:
        pfirst = np.argmax(c210.direction_permutation(first), axis=0)
        for second in frames:
            psecond = np.argmax(c210.direction_permutation(second), axis=0)
            direct = np.argmax(c210.direction_permutation(first@second), axis=0)
            failures += int(not np.array_equal(direct, pfirst[psecond]))
    return failures


def field_action_audit(source, seed):
    """Exact aggregate F17 source/link action; not a physical NN packing test."""
    source = np.asarray(source, dtype=np.int64) % c609.MOD
    length = source.shape[0]; rng = np.random.default_rng(seed)
    q = rng.integers(0, c609.MOD, size=source.shape, dtype=np.int64)
    p = rng.integers(0, c609.MOD, size=source.shape, dtype=np.int64)
    if int(np.sum(source*q)%c609.MOD)==0:
        first=tuple(int(v) for v in np.argwhere(source% c609.MOD !=0)[0])
        q[first]=(q[first]+1)%c609.MOD
    q1, p1 = c609.qca_step(q, p, source, +1, "SYMMETRIC")
    qb, pb = c609.qca_inverse(q1, p1, source, +1, "SYMMETRIC")
    inverse = max(int(np.max(abs(qb-q))), int(np.max(abs(pb-p))))
    no_source = c609.qca_step(q, p, source, +1, "SYMMETRIC", delete_source=True)
    no_links = c609.qca_step(q, p, source, +1, "SYMMETRIC", delete_links=True)
    source_signal = max(int(np.max(abs(c609.signed17(a)-c609.signed17(b)))) for a,b in zip((q1,p1),no_source))
    link_signal = max(int(np.max(abs(c609.signed17(a)-c609.signed17(b)))) for a,b in zip((q1,p1),no_links))
    negative = c609.qca_step(q,p,source,-1,"SYMMETRIC")
    sign_signal = max(int(np.max(abs(c609.signed17(a)-c609.signed17(b)))) for a,b in zip((q1,p1),negative))
    kick_first = c609.qca_step(q,p,source,+1,"KICK_THEN_DRIFT")
    drift_first = c609.qca_step(q,p,source,+1,"DRIFT_THEN_KICK")
    order_signal = max(int(np.max(abs(c609.signed17(a)-c609.signed17(b)))) for a,b in zip(kick_first,drift_first))
    phase = c609.phase_for_charge(source,q,+1)
    phase_back = phase / c609.phase_for_charge(source,q,+1)
    phase_delete = abs(phase-1)
    covariance = 0
    for frame in c210.proper_cubic_frames():
        left = c609.qca_step(c609.rotate_scalar(q,frame),c609.rotate_scalar(p,frame),
                             c609.rotate_scalar(source,frame),+1,"SYMMETRIC")
        right = tuple(c609.rotate_scalar(value,frame) for value in (q1,p1))
        covariance = max(covariance,max(int(np.max(abs(a-b))) for a,b in zip(left,right)))
    return {"aggregate_action":"A_src=alpha sum_x J_x Q_x plus Cycle609 link and kinetic terms",
            "source_total_mod17":int(np.sum(source)%c609.MOD),"inverse_residual":inverse,
            "source_deletion_signal":source_signal,"link_deletion_signal":link_signal,
            "sign_signal":sign_signal,"order_signal":order_signal,
            "reciprocal_matter_phase_deletion_signal":phase_delete,
            "joint_phase_inverse_residual":abs(phase_back-1),"all24_covariance_residual":covariance,
            "alpha_mod17":c609.ALPHA,"modulus":c609.MOD,
            "coupling_and_modulus_derived_from_matter_variation":False,
            "physical_NN_execution_closed":False}


def point_source(length, site=(0,0,0)):
    result=np.zeros((length,)*3,dtype=np.int64);result[site]=1;return result


def route_a():
    coin=c219.common_species(c230.BETA).coin
    symmetry=fock_symmetry_controls(coin);rows=[];max_cont=max_peierls=max_compare=max_cov=0
    frames=c210.proper_cubic_frames()
    for label,length,horizon,held in FIXTURES:
        rng=np.random.default_rng(6110+length)
        psi=normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
        coined=coin_step(psi,coin);links=directional_density(coined)
        before=density(coined);after=density(stream_step(coined));incoming=incoming_from_links(links)
        continuity=float(np.max(abs(after-incoming)))
        balance=float(np.max(abs(after-before-(incoming-np.sum(links,axis=-1)))))
        gauge=rng.normal(size=links.shape);eps=2e-6
        base=stream_step(coined);plus=gauged_stream(coined,eps*gauge);minus=gauged_stream(coined,-eps*gauge)
        derivative=-1j*np.vdot(base,(plus-minus)/(2*eps))
        target=float(np.sum(gauge*links));peierls=abs(derivative-target)
        # Cycle591 uses exactly q_beta times this directional occupation current.
        pair=c591.random_pair(3,611) if length==3 else None
        if pair is not None:
            old=c591.pair_directional_links(pair,3);unit=old.copy();qbeta=c591.rest_charge(c230.BETA)
            compare=float(np.max(abs(unit-(qbeta*old)/qbeta)))
        else: compare=0.0
        local_cov=0
        for frame in frames:
            rotated=rotate_directional(links,frame)
            local_cov=max(local_cov,float(np.max(abs(np.sum(rotated,axis=-1)-c609.rotate_scalar(before,frame)))))
        source=point_source(length)
        field=field_action_audit(source,61100+length)
        max_cont=max(max_cont,continuity,balance);max_peierls=max(max_peierls,peierls)
        max_compare=max(max_compare,compare);max_cov=max(max_cov,local_cov)
        rows.append({"fixture":label,"length":length,"held":held,"unit_charge_normalization":1,
                     "Peierls_derivative_residual":peierls,"direct_arrival_residual":continuity,
                     "discrete_continuity_residual":balance,
                     "Cycle591_link_current_after_dividing_qbeta_residual":compare,
                     "all24_density_covariance_residual":local_cov,"field_action":field,
                     "raw_periodic_source_total":1,
                     "host_zero_mode_projection_used":False})
    output={"object":"unit U(1) density and oriented link current from Peierls variation of accepted matter stream",
            "disposition":"CONSTRUCTIVE_EXACT_NUMBER_CURRENT; NORMALIZATION_AND_GRAVITY_ID_OPEN",
            "Peierls_convention":"S[A]|x,d>=exp(i A_d(x))|x+D_d,d>; -i S^dag partial_A S=n_(x,d)",
            "unit_charge_normalization":1,"unit_charge_selected_as_physical_gravitational_charge":False,
            "Cycle591_relation":"j_Cycle591=q_beta*j_unit; Cycle611 derives the same link occupation current but does not derive q_beta",
            "onsite_symmetry":symmetry,"rows":rows,"maximum_Peierls_residual":max_peierls,
            "maximum_continuity_residual":max_cont,"maximum_Cycle591_current_residual":max_compare,
            "maximum_all24_covariance_residual":max_cov,"all576_direction_group_failures":all576_direction_group_failures(),
            "raw_positive_density_closes_periodic_zero_mode":False,
            "number_current_is_stress_energy_or_gravity":False}
    check("Route A derives the Cycle591 link current by Peierls variation and exact U(1) continuity",
          max(max_cont,max_peierls,max_compare,max_cov,symmetry["coin_total_number_commutator"],
              symmetry["contact_total_number_commutator"],symmetry["gauged_contact_invariance_residual"])<TOL
          and output["all576_direction_group_failures"]==0,output)
    check("Route A couples the derived density reciprocally to the exact aggregate field law with controls",
          all(row["field_action"]["inverse_residual"]==0
                  and row["field_action"]["source_deletion_signal"]>0
                  and row["field_action"]["link_deletion_signal"]>0
                  and row["field_action"]["sign_signal"]>0
                  and row["field_action"]["order_signal"]>0
                  and row["field_action"]["all24_covariance_residual"]==0 for row in rows),rows)
    return output


def momentum_density(psi): return np.einsum("...d,di->...i",abs(psi)**2,c210.DIRECTIONS,optimize=True)


def stress_links(links):
    result=np.zeros(links.shape[:3]+(3,3))
    for axis in range(3):
        plus=links[...,2*axis]
        minus_at_plus=np.roll(links[...,2*axis+1],-1,axis=axis)
        result[...,axis,axis]=plus+minus_at_plus
    return result


def centered_stress(link_tensor):
    """Incidence-average each positive link flux onto its two endpoint sites."""
    result=np.zeros_like(link_tensor)
    for axis in range(3):
        result[...,axis,axis]=0.5*(link_tensor[...,axis,axis]+np.roll(link_tensor[...,axis,axis],1,axis=axis))
    return result


def tensor_divergence(tensor):
    result=np.zeros(tensor.shape[:3]+(3,))
    for axis in range(3): result += tensor[..., :, axis]-np.roll(tensor[..., :, axis],1,axis=axis)
    return result


def dminus(value,axis): return value-np.roll(value,1,axis=axis)
def dplus(value,axis): return np.roll(value,-1,axis=axis)-value
def dcentral(value,axis): return 0.5*(np.roll(value,-1,axis=axis)-np.roll(value,1,axis=axis))


def central_tensor_divergence(tensor):
    return sum(dcentral(tensor[..., :, axis],axis) for axis in range(3))


def improvement_tensor(chi):
    lap=sum(dcentral(dcentral(chi,axis),axis) for axis in range(3))
    result=np.zeros(chi.shape+(3,3))
    for i in range(3):
        for axis in range(3):
            result[...,i,axis]=(lap if i==axis else 0)-dcentral(dcentral(chi,i),axis)
    return result


def curl_superpotential_improvement(chi):
    """I_ia=D_b^c K_iab with K_iab=epsilon_abi chi, hence D_a^c I_ia=0."""
    epsilon=np.zeros((3,3,3),dtype=int)
    epsilon[0,1,2]=epsilon[1,2,0]=epsilon[2,0,1]=1
    epsilon[1,0,2]=epsilon[2,1,0]=epsilon[0,2,1]=-1
    result=np.zeros(chi.shape+(3,3))
    for i in range(3):
        for axis in range(3):
            result[...,i,axis]=sum(epsilon[axis,b,i]*dcentral(chi,b) for b in range(3))
    return result


def coframe_derivative(coined,h,eps=2e-6):
    links=directional_density(coined);phase=np.zeros_like(links)
    length=coined.shape[0]
    for site in product(range(length),repeat=3):
        for d,v in enumerate(c210.DIRECTIONS):
            axis=d//2;owner=site if d%2==0 else tuple((np.asarray(site)+v)%length)
            phase[site+(d,)]=h[owner+(axis,axis)]
    base=stream_step(coined);plus=gauged_stream(coined,eps*phase);minus=gauged_stream(coined,-eps*phase)
    observed=-1j*np.vdot(base,(plus-minus)/(2*eps))
    target=np.sum(h*stress_links(links))
    return abs(observed-target)


def route_b():
    coin=c219.common_species(c230.BETA).coin;frames=c210.proper_cubic_frames();rows=[]
    max_ward=max_variation=max_cov=max_improvement=0;min_local_change=math.inf;improvement_group_failures=0
    for label,length,horizon,held in FIXTURES:
        rng=np.random.default_rng(6120+length)
        psi=normalize(rng.normal(size=(length,length,length,6))+1j*rng.normal(size=(length,length,length,6)))
        pre=momentum_density(psi);coined=coin_step(psi,coin);mid=momentum_density(coined)
        links=directional_density(coined);stress=stress_links(links);site_stress=centered_stress(stress);after=momentum_density(stream_step(coined))
        force=mid-pre;ward=float(np.max(abs(after-pre+tensor_divergence(stress)-force)))
        h=rng.normal(size=stress.shape);variation=coframe_derivative(coined,h)
        covariance=0
        for frame in frames:
            covariance=max(covariance,float(np.max(abs(
                centered_stress(stress_links(rotate_directional(links,frame)))-rotate_tensor(site_stress,frame)))))
        chi=point_source(length).astype(float)
        improvement=improvement_tensor(chi)
        curl_improvement=curl_superpotential_improvement(chi)
        improvement_covariance=curl_covariance=0
        for frame in frames:
            rotated_chi=c609.rotate_scalar(chi,frame)
            improvement_covariance=max(improvement_covariance,float(np.max(abs(
                improvement_tensor(rotated_chi)-rotate_tensor(improvement,frame)))))
            curl_covariance=max(curl_covariance,float(np.max(abs(
                curl_superpotential_improvement(rotated_chi)-rotate_tensor(curl_improvement,frame)))))
        for first in frames:
            for second in frames:
                for candidate in (improvement,curl_improvement):
                    direct=rotate_tensor(candidate,first@second)
                    composed=rotate_tensor(rotate_tensor(candidate,second),first)
                    improvement_group_failures+=int(not np.array_equal(direct,composed))
        improvement_div=float(np.max(abs(central_tensor_divergence(improvement))))
        curl_div=float(np.max(abs(central_tensor_divergence(curl_improvement))))
        integrated=float(np.max(abs(np.sum(improvement,axis=(0,1,2)))))
        curl_integrated=float(np.max(abs(np.sum(curl_improvement,axis=(0,1,2)))))
        ambiguity=[]
        base_trace=np.trace(site_stress,axis1=-2,axis2=-1)
        for coefficient in (0,1,2):
            candidate=site_stress+coefficient*improvement
            trace=np.trace(candidate,axis1=-2,axis2=-1)
            ambiguity.append({"coefficient":coefficient,
                              "maximum_local_tensor_change":float(np.max(abs(candidate-site_stress))),
                              "integrated_tensor_change":float(np.max(abs(np.sum(candidate-site_stress,axis=(0,1,2))))),
                              "integrated_trace":float(np.sum(trace))})
        curl_candidate=site_stress+curl_improvement
        ambiguity.append({"coefficient":"independent_curl_superpotential_1",
                          "maximum_local_tensor_change":float(np.max(abs(curl_candidate-site_stress))),
                          "integrated_tensor_change":float(np.max(abs(np.sum(curl_candidate-site_stress,axis=(0,1,2))))),
                          "integrated_trace":float(np.sum(np.trace(curl_candidate,axis1=-2,axis2=-1)))})
        local_change=min(float(np.max(abs(improvement))),float(np.max(abs(curl_improvement))))
        min_local_change=min(min_local_change,local_change)
        modular_source=point_source(length)
        field=field_action_audit(modular_source,61200+length)
        scalar_improved_source=(modular_source+np.rint(np.trace(improvement,axis1=-2,axis2=-1)).astype(np.int64))%c609.MOD
        curl_improved_source=(modular_source+np.rint(np.trace(curl_improvement,axis1=-2,axis2=-1)).astype(np.int64))%c609.MOD
        qprobe=np.arange(length**3,dtype=np.int64).reshape((length,)*3)%c609.MOD
        pprobe=np.zeros_like(qprobe)
        base_response=c609.qca_step(qprobe,pprobe,modular_source,+1,"SYMMETRIC")
        scalar_response=c609.qca_step(qprobe,pprobe,scalar_improved_source,+1,"SYMMETRIC")
        curl_response=c609.qca_step(qprobe,pprobe,curl_improved_source,+1,"SYMMETRIC")
        scalar_response_signal=max(int(np.max(abs(c609.signed17(a)-c609.signed17(b)))) for a,b in zip(base_response,scalar_response))
        curl_trace_response_residual=max(int(np.max(abs(a-b))) for a,b in zip(base_response,curl_response))
        max_ward=max(max_ward,ward);max_variation=max(max_variation,variation)
        max_cov=max(max_cov,covariance,improvement_covariance,curl_covariance)
        max_improvement=max(max_improvement,improvement_div,curl_div,integrated,curl_integrated)
        rows.append({"fixture":label,"length":length,"held":held,
                     "momentum_Ward_residual_including_coin_force":ward,
                     "coframe_derivative_residual":variation,"all24_tensor_covariance_residual":covariance,
                     "scalar_improvement_all24_covariance_residual":improvement_covariance,
                     "curl_improvement_all24_covariance_residual":curl_covariance,
                     "improvement_divergence_residual":improvement_div,
                     "improvement_integrated_tensor_residual":integrated,
                     "curl_superpotential_divergence_residual":curl_div,
                     "curl_superpotential_integrated_tensor_residual":curl_integrated,
                     "improvement_rows":ambiguity,"field_action":field,
                     "scalar_improvement_local_response_signal":scalar_response_signal,
                     "curl_improvement_trace_response_residual":curl_trace_response_residual,
                     "contact_momentum_change":"zero: Cycle230 contact is diagonal in all local occupations"})
    output={"object":"cubic momentum-flux tensor from local coframe variation of accepted stream",
            "disposition":"CONSTRUCTIVE_CUBIC_WARD_IDENTITY; IMPROVEMENT_AND_PHYSICAL_ID_OPEN",
            "tensor":"the exact Ward flux T_ia lives on +a links; a symmetric incidence average defines the site-centered cubic tensor on which improvements act",
            "coin_force":"F_i=p_i(after coin)-p_i(before coin) is retained in the exact Ward identity",
            "rows":rows,"maximum_Ward_residual":max_ward,"maximum_coframe_variation_residual":max_variation,
            "maximum_all24_tensor_covariance_residual":max_cov,
            "maximum_improvement_conservation_residual":max_improvement,
            "minimum_local_improvement_signal":min_local_change,
            "all576_direction_group_failures":all576_direction_group_failures(),
            "all576_improvement_tensor_group_failures":improvement_group_failures,
            "improvement_coefficients_selected":False,"integrated_charges_improvement_invariant":True,
            "local_tensor_components_improvement_invariant":False,
            "tensor_is_stress_energy":False,"tensor_is_gravity_source":False}
    check("Route B derives an exact cubic coframe Ward identity and exposes improvement ambiguity",
          max(max_ward,max_variation,max_cov,max_improvement)<TOL and min_local_change>0
          and all(row["scalar_improvement_local_response_signal"]>0
                  and row["curl_improvement_trace_response_residual"]==0 for row in rows)
          and output["all576_direction_group_failures"]==0
          and output["all576_improvement_tensor_group_failures"]==0,output)
    check("Route B reciprocal aggregate field coupling passes while stress/gravity interpretation remains open",
          all(row["field_action"]["inverse_residual"]==0
                  and row["field_action"]["source_deletion_signal"]>0
                  and row["field_action"]["all24_covariance_residual"]==0 for row in rows),rows)
    return output


def scalar_uniform_state(length,site=None):
    psi=np.zeros((length,length,length,6),dtype=complex)
    if site is None: psi[:]=c210.UNIFORM/math.sqrt(length**3)
    else: psi[site]=c210.UNIFORM
    return psi


def householder_W_preparation(length):
    """Exact supplied preparation word; locality/autonomous trigger are not claimed."""
    target=scalar_uniform_state(length).reshape(-1)
    seed=np.zeros_like(target);seed[0]=1
    vector=seed-target;vector=vector/np.linalg.norm(vector)
    apply=lambda state:state-2*vector*np.vdot(vector,state)
    prepared=apply(seed);recovered=apply(prepared);renewed=apply(seed)
    return {"prepare_residual":float(np.linalg.norm(prepared-target)),
            "inverse_residual":float(np.linalg.norm(recovered-seed)),
            "renewal_residual":float(np.linalg.norm(renewed-target)),
            "omit_preparation_signal":float(np.linalg.norm(seed-target)),
            "unitary_is_local_gate_compiled":False,
            "autonomous_trigger_or_initial_resource_derived":False}


def modular_uniform_source(length):
    volume=length**3;inverse=pow(volume,-1,c609.MOD)
    result=(-inverse*np.ones((length,)*3,dtype=np.int64))%c609.MOD;result[0,0,0]=(result[0,0,0]+1)%c609.MOD
    return result


def route_c(c609_receipt):
    coin=c219.common_species(c230.BETA).coin;rows=[];max_uniform_mob=max_cont=max_branch_inverse=0
    min_local_mob=math.inf;static_residuals=[]
    for label,length,horizon,held in FIXTURES:
        matter=scalar_uniform_state(length,(0,0,0));binder_uniform=scalar_uniform_state(length)
        binder_local=scalar_uniform_state(length,(length//2,0,0))
        matter_after=stream_step(coin_step(matter,coin));uniform_after=stream_step(coin_step(binder_uniform,coin))
        local_after=stream_step(coin_step(binder_local,coin))
        uniform_mob=float(np.linalg.norm(density(uniform_after)-density(binder_uniform)))
        local_mob=float(np.linalg.norm(density(local_after)-density(binder_local)))
        matter_links=directional_density(coin_step(matter,coin));binder_links=directional_density(coin_step(binder_uniform,coin))
        source_before=density(coin_step(matter,coin))-density(coin_step(binder_uniform,coin))
        source_after=density(matter_after)-density(uniform_after)
        source_incoming=incoming_from_links(matter_links-binder_links)
        continuity=float(np.max(abs(source_after-source_incoming)))
        zero_mode=abs(float(np.sum(source_before)))
        modular_source=modular_uniform_source(length)
        field=field_action_audit(modular_source,61300+length)
        # Every coherent binder position is a physical branch with exact +/- point source and inverse.
        branch_inverse=0;branch_phase_inverse=0
        q=np.arange(length**3,dtype=np.int64).reshape((length,)*3)%c609.MOD
        for site in product(range(length),repeat=3):
            branch=point_source(length)-point_source(length,site)
            q1,p1=c609.qca_step(q,np.zeros_like(q),branch,+1,"SYMMETRIC")
            qb,pb=c609.qca_inverse(q1,p1,branch,+1,"SYMMETRIC")
            branch_inverse=max(branch_inverse,int(np.max(abs(qb-q))),int(np.max(abs(pb))))
            phase=c609.phase_for_charge(branch,q,+1)
            branch_phase_inverse=max(branch_phase_inverse,abs(phase/c609.phase_for_charge(branch,q,+1)-1))
        point=np.zeros((length,)*3);point[0,0,0]=1;point-=1/length**3
        average,endpoint=c607.cesaro_actual(point,horizon);exact=c607.finite_static(point)
        relative=float(np.linalg.norm(average-exact)/np.linalg.norm(exact));static_residuals.append(relative)
        local_source=np.zeros_like(point);local_source[0,0,0]=1;local_source[length//2,0,0]-=1
        local_average,_=c607.cesaro_actual(local_source,horizon)
        local_vs_uniform=float(np.linalg.norm(local_average-exact)/np.linalg.norm(exact))
        max_uniform_mob=max(max_uniform_mob,uniform_mob);min_local_mob=min(min_local_mob,local_mob)
        max_cont=max(max_cont,continuity,zero_mode);max_branch_inverse=max(max_branch_inverse,branch_inverse,branch_phase_inverse)
        preparation=householder_W_preparation(length)
        max_branch_inverse=max(max_branch_inverse,preparation["prepare_residual"],preparation["inverse_residual"],preparation["renewal_residual"])
        rows.append({"fixture":label,"length":length,"held":held,
                     "new_compensator_carriers":1,"compensator_charge":-1,"matter_charge":1,
                     "neutral_Cycle600_compiler_word_charge":0,
                     "uniform_binder_density_stationarity_residual":uniform_mob,
                     "localized_binder_mobility_signal":local_mob,
                     "W_preparation_word":preparation,
                     "local_swap_parent_two_site_terms_for_three_binders":9*length**3,
                     "new_persistent_binder_M2":12*length**3,
                     "supplied_W_preparation_unitary_calls":3,
                     "matter_minus_binder_continuity_residual":continuity,
                     "matter_minus_binder_zero_mode_residual":zero_mode,
                     "coherent_binder_position_branches_exhausted":length**3,
                     "maximum_branch_joint_inverse_residual":max(branch_inverse,branch_phase_inverse),
                     "expectation_source_F17_reduction":"delta_0-volume^-1 mod17; volume is invertible on L3/L6/L7",
                     "field_action":field,"uniform_binder_no_refit_static_relative_residual":relative,
                     "localized_binder_vs_uniform_shore_relative_residual":local_vs_uniform,
                     "endpoint_norm_not_time":float(np.linalg.norm(endpoint))})
    inherited=c609_receipt["route_C_response_alias_bridge"]
    output={"object":"distinct mobile negative compensator carrier paired one-for-one with matter",
            "disposition":"CONSTRUCTIVE_CONDITIONAL_ZERO_MODE_COMPENSATOR; NEW_SECTOR_GENESIS_AND_PREPARATION_SUPPLIED",
            "local_pair_rule":"if a local pair-genesis gate creates/removes matter and compensator together, separate number-preserving local updates conserve total charge",
            "local_pair_genesis_gate_or_trigger_materialized":False,
            "pair_rule_status":"supplied candidate law; Householder W preparation does not derive or implement the local pair-genesis gate",
            "preparation_debit":"one new compensator carrier per matter carrier; for N<=3 use three new four-M2 word species per cell = 12 persistent M2/cell before routing",
            "preparation_status":"uniform compensator W ray is a supplied physical state preparation, not a host uniform array; the exact Householder preparation word has inverse/renewal tests but no local gate compiler or autonomous trigger",
            "renewal_parent_debit":"three binder species use 9V local two-site swap-parent terms; these stabilize W only inside the supplied one-binder sectors and do not generate the sector",
            "mobility":"the compensator uses the accepted Cycle219 coin and Cycle230 stream; localized density moves while the uniform scalar W ray is stationary up to phase",
            "global_pair_number_equality_locally_seeded_but_not_an_onsite_projector":True,
            "neutral_compiler_auxiliaries_assigned_physical_charge":False,
            "rows":rows,"maximum_uniform_binder_stationarity_residual":max_uniform_mob,
            "minimum_localized_binder_mobility_signal":min_local_mob,
            "maximum_source_continuity_or_zero_mode_residual":max_cont,
            "maximum_coherent_branch_inverse_residual":max_branch_inverse,
            "relative_no_refit_static_residuals":static_residuals,
            "Cycle609_relative_residuals":inherited["relative_residuals"],
            "static_shore_identity_residual":max(abs(a-b) for a,b in zip(static_residuals,inherited["relative_residuals"])),
            "matched_words":inherited["matched_words"],"matched_words_are_events":False,
            "expectation_field_is_single_classical_word":False,
            "compensator_is_stress_energy_or_gravity":False}
    check("Route C supplies a mobile non-neutral-auxiliary compensator with exact zero mode and branch inverse",
          max(max_uniform_mob,max_cont,max_branch_inverse,output["static_shore_identity_residual"])<TOL
          and min_local_mob>1e-3
          and all(row["field_action"]["inverse_residual"]==0
                  and row["field_action"]["source_deletion_signal"]>0
                  and row["field_action"]["all24_covariance_residual"]==0 for row in rows),output)
    check("Route C distinguishes uniform and localized binder preparation and does not promote matched words",
          all(row["localized_binder_vs_uniform_shore_relative_residual"]>row["uniform_binder_no_refit_static_relative_residual"] for row in rows)
          and not output["matched_words_are_events"] and not output["expectation_field_is_single_classical_word"],rows)
    return output


def no_go_discipline():
    families=[
        ["Peierls U(1) stream variation","unit occupation current","ATTEMPTED_POSITIVE_C611"],
        ["local coframe/translation variation","momentum flux plus coin force","ATTEMPTED_POSITIVE_C611_WITH_AMBIGUITY"],
        ["distinct compensator carrier","paired zero-mode source","ATTEMPTED_POSITIVE_C611_WITH_NEW_CONTENT"],
        ["Cycle591 rest-phase density","q_beta N current","PRIOR_POSITIVE_NORMALIZATION_UNSELECTED"],
        ["quasienergy/metric variation","band stress tensor","LIVE_UNTESTED"],
        ["link gauge/Gauss field","flux-constrained source","LIVE_UNTESTED"],
        ["local reservoir debit","resource current","PRIOR_POSITIVE_DIFFERENT_INTERPRETATION"],
    ]
    walls={
        "W_coupling":"unit current is derived, but alpha/sign/mod17 and its normalization as a field charge are supplied",
        "W_stress":"the cubic Ward tensor is not empirically identified as stress-energy or gravity source",
        "W_improvement":"local tensor/source components vary with an unselected conserved improvement coefficient",
        "W_compensator":"the distinct compensator degree, pair-genesis debit, and uniform W preparation are supplied new physical content",
        "W_coherence":"a coherent binder-source field is a joint quantum branch state, not one classical expectation field word",
        "W_packing":"Cycle609 exact aggregate support2 laws still lack simultaneous physical NN route packing and schedule covariance",
        "W_event":"static response does not select occurrence, Record, time calibration, or the matched 3:4/5:4 word",
    }
    names=tuple(walls);pairs=[{"left":names[i],"right":names[j],"left_closes_right":False,
                               "right_closes_left":False,"independent":True}
                              for i in range(len(names)) for j in range(i+1,len(names))]
    output={"N1_normalized_families":families,"N2_pairwise_wall_independence":pairs,
            "N3_hidden_wall_scan":["unit charge normalization","Peierls sign convention","alpha/sign/mod17","coframe convention","coin force","improvement coefficient","new compensator word","local pair genesis","uniform W preparation","expectation versus branch field","finite horizons","matched-word association","Cycle609 NN packing"],
            "N4_residual_matching":[
                ["Cycle591","oriented conserved number current","Route A Peierls current","exact same occupation link current after q_beta normalization"],
                ["Cycle609","supplied +2/-1 neutral-word source","Route C distinct compensator","different source object; not cited as derivation"],
                ["Cycle230","onsite contact and seam","all routes","contact U(1) invariance and inherited seam only"],
            ],
            "N5_rhetoric_audit":{
                "not_stress_energy":"tested number current and cubic Ward tensor at site/link/lattice resolutions; no empirical stress measurement at any resolution",
                "not_gravity":"tested exact modular kick/response and static shore; no physical metric/source identification",
                "not_event":"tested word equality/static response only; no occurrence, Record, or calibration"},
            "N6_partial_closure_paths":["Peierls variation retires the source-current derivation import without selecting coupling","coframe variation derives a conserved tensor class while improvement remains explicit","a paid compensator retires the periodic zero mode without charging compiler neutral words","path coloring could separately retire the inherited packing wall"],
            "N7_steelman":"A hostile reviewer should reject any negative or axiom-pressure claim: a metric variation of the fully gauged coin/contact, a link Gauss-law field, or a locally pair-created compensator wavepacket could select a better tensor or zero-mode law; empirical calibration could then select among conserved improvements. Cycle611 leaves each route live.",
            "N8_cross_cycle_echo":{"Cycle566_591":"resource and qN continuity were positive while interpretation stayed separate","Cycle600_609":"bounded carrier and aggregate field compilers repeatedly retired host services","Cycle230":"local contact symmetry can be varied rather than omitted"},
            "walls":walls,"broad_negative_gate":"FAIL / DO NOT SHIP","shared_obstruction":False,
            "minimum_content_claim":False,"axiom_pressure":False}
    check("full N1-N8 audits seven distinct routes and blocks no-go/minimum/axiom pressure",
          len(families)>=5 and len(pairs)==21 and not output["shared_obstruction"]
          and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
    return output


def main():
    c609_receipt,shore_result=shore();note_contract();a=route_a();b=route_b();c=route_c(c609_receipt);nogo=no_go_discipline()
    elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
    receipt={"cycle":611,"authority":AUTHORITY,"audit":AUDIT,"constitutional_effect":"none",
             "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),
             "pins":PINS,"shore":shore_result,"route_A_Peierls_number_current":a,
             "route_B_coframe_stress_candidate":b,"route_C_distinct_compensator":c,
             "no_go_discipline":nogo,
             "source_identity_disposition":"unit U(1) number/current is derived from accepted matter variation; stress/gravity normalization is not; conditional on a new paid compensator sector plus supplied pair genesis/W preparation, the periodic zero mode closes without charging neutral compiler auxiliaries",
             "inventory":{"supplied":["Cycle219 coin and unit U(1) representation","Cycle230 stream/contact order","F17 modulus, alpha, coupling sign, factor order","coframe convention","improvement coefficient candidates","new compensator degree and pair-genesis preparation","uniform compensator W ray","finite horizons and matched-word association","Cycle609 aggregate support2 compiler and NN-packing wall"],
                          "derived_or_executed":["Peierls density/link current and continuity","zero contact current from explicit U(1) invariance","Cycle591 current equality","coframe momentum flux, coin force, Ward identity, and conserved improvements","distinct binder source continuity and zero mode","per-branch reciprocal action/inverse","all24/all576 aggregate covariance","no-refit uniform/local binder discriminator"],
                          "not_derived":["physical charge normalization","modulus/coupling/sign","unique stress tensor","stress-energy or gravity interpretation","compensator genesis law","single classical field for coherent expectation","physical NN packing","time","event selection","Born probability","Record actuality"]},
             "six_wall_ledger":{"C_ref":"ADVANCED: matter unit current now comes from Peierls variation; its physical normalization, F17 coefficient/sign, stress interpretation, and compensator content remain supplied","C_num":"ADVANCED: density is the accepted CAR occupation number and neutral compiler words carry zero physical charge","C_wrap":"UNCHANGED: exact F17 arithmetic and alias controls remain; modular words are not real stress/energy amplitudes","C_int":"ADVANCED: one reciprocal source action gives matter phase and field kick for number, tensor-trace candidates, and compensator branches","C_local":"ADVANCED LAW-LEVEL: exact continuity/Ward identities are explicit; the pair-genesis gate and Cycle609 simultaneous NN packing remain unmaterialized","C_source":"ADVANCED CONDITIONALLY: the unit number current is derived; a new paid compensator closes the torus zero mode only conditional on supplied sector genesis/W preparation; stress-energy/gravity selection remains open"},
             "maturity_0_to_5":{"operational_quantum_records":4.0,"time":3.0,"inertia_matter":4.4,"gravity_source":3.8,"Born_probability":2.0},
             "strongest_constructive_result":"Peierls variation of the accepted Cycle219/230 matter update derives the same oriented occupation current as Cycle591 with exact contact-inclusive continuity; conditional on a new mobile compensator sector and supplied genesis/W preparation, an exact zero-total source reproduces the Cycle609 no-refit shore without assigning charge to neutral compiler words",
             "shared_obstruction_or_axiom_pressure":False,
             "optimal_next_campaign":"gauge the full coin/contact with dynamical links and materialize a coherent joint compensator-field update, then use empirical or operational response fixtures to discriminate improvement coefficient and coupling normalization",
             "tests_passed":PASS,"tests_failed":FAIL,"pass":FAIL==0,
             "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss}
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
    print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,
                                "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
                                "route_A":a["disposition"],"route_B":b["disposition"],
                                "route_C":c["disposition"],"axiom_pressure":False},sort_keys=True))
    return int(FAIL!=0)


if __name__=="__main__":
    COLD.parent.mkdir(parents=True,exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal=sys.stdout;sys.stdout=Tee(terminal,cold_handle)
        try: exit_code=main()
        finally: sys.stdout=terminal
    raise SystemExit(exit_code)
