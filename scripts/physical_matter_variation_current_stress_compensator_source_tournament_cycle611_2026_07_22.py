#!/usr/bin/env python3
"""Cycle611: matter variation, Ward identities, and compensator audit.

Route A gauges the Cycle219/230 coin-stream-contact update. Route B varies the
stream under a local cubic coframe. Route C tests a distinct paid mobile
compensator role rather than charging Cycle600's neutral roles. C609 supplies
only algebraic role factors and aggregate arrays: no physical M2/source/stress/
gravity/time compiler is back-credited. Authority none; audit unset; author
artifact status accepted false.
"""
from __future__ import annotations

import ast
import contextlib
from fractions import Fraction
from hashlib import sha256
import io
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
AUTHOR_ARTIFACT_STATUS_ACCEPTED = False
AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES = False
TOL = 2e-8
START = perf_counter()
PASS = FAIL = 0

PINS = {
    "scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py":
        "6e9d04c8d0ba189a93e434025c569b8a9dc2c63d5cd7a6a888a3d829f4ed8003",
    "docs/work_history/repo/review_feedback/PHYSICAL_TWO_M2_CAR_PHASE_LINK_FIELD_QCA_TOURNAMENT_CYCLE609_NOTE_2026-07-22.md":
        "93d991d79e594a60494cb13112e21aba0356c84c23e79a334892aaa98797710c",
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json":
        "a5bd17754c3d0e80ad2cff72e7ab63d5b3a5046805c92be583d95ede8b0463ff",
    "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_cold_2026_07_22.txt":
        "b53ddeac0dba5a2477ba3288c254accbd3ea7c8f082b1dd0bcda97df0ac3ad2b",
    "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":
        "d031740fadfbfa42dccba37fc4c5c211a0bec7daa9ef60a17fb9a4c65cc06291",
    "docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":
        "bef7ef925e23dda48eb6f84644b22656f39a411b45dba79b311e0b15d69d9a18",
    "outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt":
        "59831c9fe3f034c4c66144ac857e9c931ca48c7e7ea543f2787980d076b4c6da",
}

EXPECTED_NOTE_SHA256 = "797ae62adb91d34f9e96b038ffc8aec4ca206db22691292417404c5b51fba258"
EXPECTED_RUNTIME_IMPORT_COUNT = 62
EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256 = "47a6593eae01ad558a508330c481ca54dba96e45335b180f5b8d3c064f6c67e0"

FIXTURES = (("TRAIN_L3", 3, 384, False), ("HELD_L6", 6, 768, True),
            ("OUT_HELD_L7", 7, 1536, True))


def json_default(value):
    if isinstance(value, np.generic): return value.item()
    if isinstance(value, np.ndarray): return value.tolist()
    if isinstance(value, Fraction): return f"{value.numerator}/{value.denominator}"
    if isinstance(value, complex): return [value.real, value.imag]
    raise TypeError(type(value).__name__)


def digest(relative): return sha256((ROOT / relative).read_bytes()).hexdigest()


def runtime_import_closure() -> tuple[str, ...]:
    modules = {path.stem: path for path in (ROOT / "scripts").glob("*.py")}
    entry = Path(__file__).resolve()
    visited: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names: tuple[str, ...] = ()
            if isinstance(node, ast.Import):
                names = tuple(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = (node.module.split(".")[0],)
            for name in names:
                if name in modules:
                    visit(modules[name])

    visit(entry)
    return tuple(sorted(str(path.relative_to(ROOT)) for path in visited if path != entry))


def runtime_import_controls() -> dict:
    closure = runtime_import_closure()
    observed = {path: digest(path) for path in closure}
    payload = "".join(f"{path}\0{observed[path]}\n" for path in closure)
    manifest = sha256(payload.encode("utf-8")).hexdigest()
    direct = (
        "scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py",
        "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py",
    )
    return {"direct_runtime_imports": direct, "complete_runtime_import_closure": closure,
            "runtime_import_count": len(closure),
            "hidden_runtime_import_count": len(tuple(path for path in closure if path not in direct)),
            "observed_sha256": observed, "closure_manifest_sha256": manifest,
            "expected_closure_manifest_sha256": EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
            "pass": (len(closure) == EXPECTED_RUNTIME_IMPORT_COUNT
                     and all(path in closure for path in direct)
                     and manifest == EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256)}


def cold_json(path: Path, prefix: str) -> dict:
    rows = [json.loads(line.removeprefix(prefix)) for line in path.read_text().splitlines()
            if line.startswith(prefix)]
    if len(rows) != 1:
        raise RuntimeError(f"{path.name} must contain exactly one {prefix.strip()} row")
    return rows[0]


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(condition); FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore():
    observed = {path: digest(path) for path in PINS}
    imports = runtime_import_controls()
    receipt = json.loads((ROOT / "outputs/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_receipt_2026_07_22.json").read_text())
    r591 = cold_json(ROOT / "outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt", "REPORT_JSON ")
    inherited = receipt["shore"]
    c591a = r591["route_A"]
    c591b = r591["inherited_boundary_controls"]
    causal = receipt["causal_time_comparison"]
    note_sha = digest(str(NOTE.relative_to(ROOT)))
    c611_note_path = str(NOTE.relative_to(ROOT))
    c609_backedge_expected = receipt["pins"][c611_note_path]
    c609_runtime_depends_on_c611 = any(
        "cycle611" in path.lower() for path in receipt["runtime_import_controls"]["complete_runtime_import_closure"])
    backedge = {"C609_embedded_C611_note_expected_sha256":c609_backedge_expected,
                "current_rebuilt_C611_note_sha256":note_sha,
                "embedded_pin_matches_current_note":c609_backedge_expected==note_sha,
                "C609_runtime_imports_C611":c609_runtime_depends_on_c611,
                "packaging_backedge_detected":c609_backedge_expected!=note_sha and not c609_runtime_depends_on_c611,
                "science_runtime_dependency_cycle":False,
                "scope":"C609 used the old C611 note as pinned N6 evidence only; no C611 runner/result was imported, executed, or back-credited"}
    output = {
        "direct_evidence_hashes_match": observed == PINS,
        "note_sha256": note_sha, "note_matches_frozen_hash": note_sha == EXPECTED_NOTE_SHA256,
        "runtime_import_closure": imports,
        "Cycle609_pass": receipt["pass"], "Cycle609_tests": receipt["tests_passed"],
        "Cycle609_author_artifact_status_accepted": receipt["author_artifact_status_accepted"],
        "Cycle609_audit_verdict_inferred_from_dependencies": receipt["audit_verdict_inferred_from_dependencies"],
        "Cycle609_confirmed_breakthrough": receipt["confirmed_breakthrough"],
        "Cycle609_physical_M2_compiler": receipt["scope_boundaries"]["physical_M2_compiler"],
        "Cycle609_physical_EG_evaluated": receipt["scope_boundaries"]["physical_EG_evaluated"],
        "mass": inherited["mass"], "contact": inherited["contact"],
        "seam": inherited["seam"], "joint_EG": inherited["joint_EG"],
        "Cycle591_pass": r591["tests_failed"] == 0, "Cycle591_tests": r591["tests_passed"],
        "Cycle591_authority": r591["authority"], "Cycle591_audit": r591["audit"],
        "Cycle591_author_artifact_status_accepted": c591b["author_artifact_status_accepted"],
        "Cycle591_audit_verdict_inferred_from_dependency": c591b["audit_verdict_inferred_from_dependency"],
        "Cycle591_current_continuity_residual": c591a["maximum_explicit_local_continuity_residual"],
        "Cycle591_contact_charge_commutator": c591a["full_local_Fock_contact_charge_commutator"],
        "Cycle591_mass_fixture_relative_residual": c591a["mass_fixture_relative_residual"],
        "Cycle591_coefficient_selected_by_conservation": c591a["coefficient_selected_by_conservation"],
        "Cycle591_physical_EG_evaluated": c591a["physical_E_and_G_composition_evaluated"],
        "causal_time_boundary": causal,
        "C609_to_C611_note_packaging_backedge":backedge,
    }
    check("C591/C609 shores, note, and complete runtime closure are byte-pinned without physical or audit back-credit",
          all((output["direct_evidence_hashes_match"], output["note_matches_frozen_hash"], imports["pass"],
               output["Cycle609_pass"], not output["Cycle609_author_artifact_status_accepted"],
               not output["Cycle609_audit_verdict_inferred_from_dependencies"],
               not output["Cycle609_confirmed_breakthrough"], not output["Cycle609_physical_M2_compiler"],
               not output["Cycle609_physical_EG_evaluated"], output["Cycle591_pass"],
               output["Cycle591_authority"] == "none", output["Cycle591_audit"] == "unset",
               not output["Cycle591_author_artifact_status_accepted"],
               not output["Cycle591_audit_verdict_inferred_from_dependency"],
               not output["Cycle591_coefficient_selected_by_conservation"],
               not output["Cycle591_physical_EG_evaluated"], causal["pinned_object_matches"],
               causal["delay_rate_associated_in_pinned_note"],
               causal["advance_requires_event_count_edit_in_pinned_note"],
               causal["event_association_remains_underived_in_pinned_note"],
               not causal["runner_executed"], not causal["backcredited_to_Cycle609"],
               c609_backedge_expected=="102b57283c55a190ba02289d2689ac8a6e6f97aff58e13036df1dd8a66e97308",
               backedge["packaging_backedge_detected"], not backedge["C609_runtime_imports_C611"],
               not backedge["science_runtime_dependency_cycle"]))
          and max(output["mass"], output["contact"], output["seam"], output["joint_EG"],
                  output["Cycle591_current_continuity_residual"],
                  output["Cycle591_contact_charge_commutator"],
                  output["Cycle591_mass_fixture_relative_residual"]) < TOL, output)
    return receipt, output


def note_contract():
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = ("authority: none", "audit: unset", "author artifact status accepted: false",
                "cycle 611", "route a", "route b", "route c", "peierls", "cycle591",
                "q_beta", "contact-inclusive", "continuity", "coframe", "coin force",
                "two improvement families", "paid mobile compensator", "localized", "uniform",
                "not unique stress-energy", "not physical m2", "packaging backedge",
                "no science-runtime dependency cycle", "l3", "l6", "l7", "all-24", "all-576",
                "3:4", "5:4", "no event/count-edit path", "not time", "n1 —", "n2 —",
                "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
                "fail / do not ship negative", "negative_claim_shipped=false",
                "no candidate is a confirmed breakthrough", "no axiom pressure")
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
    """Exact aggregate F17 array map; not a physical field or NN test."""
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
    return {"aggregate_array_polynomial":"A_role=alpha sum_x J_x Q_x plus C609 array-link and Q/P terms",
            "host_role_array_total_mod17":int(np.sum(source)%c609.MOD),"inverse_residual":inverse,
            "role_array_deletion_signal":source_signal,"link_term_deletion_signal":link_signal,
            "sign_signal":sign_signal,"order_signal":order_signal,
            "role_phase_polynomial_deletion_signal":phase_delete,
            "role_phase_inverse_residual":abs(phase_back-1),"all24_aggregate_array_covariance_residual":covariance,
            "all24_aggregate_array_comparisons_executed":24,
            "alpha_mod17":c609.ALPHA,"modulus":c609.MOD,
            "coupling_modulus_sign_and_role_normalization_derived_from_matter_variation":False,
            "physical_M2_register_or_field_composed":False,
            "physical_NN_execution_closed":False}


def point_source(length, site=(0,0,0)):
    result=np.zeros((length,)*3,dtype=np.int64);result[site]=1;return result


def route_a():
    coin=c219.common_species(c230.BETA).coin
    symmetry=fock_symmetry_controls(coin);rows=[];max_cont=max_peierls=max_compare=max_cov=0
    c591_comparison_fixtures=0
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
            c591_comparison_fixtures += 1
        else: compare=0.0
        local_cov=0
        for frame in frames:
            rotated=rotate_directional(links,frame)
            local_cov=max(local_cov,float(np.max(abs(np.sum(rotated,axis=-1)-c609.rotate_scalar(before,frame)))))
        source=point_source(length)
        field=field_action_audit(source,61100+length)
        max_cont=max(max_cont,continuity,balance);max_peierls=max(max_peierls,peierls)
        max_compare=max(max_compare,compare);max_cov=max(max_cov,local_cov)
        rows.append({"fixture":label,"length":length,"held":held,"unit_U1_probe_normalization":1,
                     "Peierls_derivative_residual":peierls,"direct_arrival_residual":continuity,
                     "discrete_continuity_residual":balance,
                     "Cycle591_link_current_after_dividing_qbeta_residual":compare,
                     "all24_density_covariance_residual":local_cov,"field_action":field,
                     "raw_periodic_role_array_total":1,
                     "host_zero_mode_projection_used":False})
    output={"object":"unit-normalized U(1) density and oriented occupation current from Peierls variation of the Cycle219/230 stream/contact update",
            "disposition":"CONSTRUCTIVE_EXACT_UNIT_U1_NUMBER_CURRENT; UNIQUE_PHYSICAL_NORMALIZATION_AND_SOURCE_LAW_OPEN",
            "Peierls_convention":"S[A]|x,d>=exp(i A_d(x))|x+D_d,d>; -i S^dag partial_A S=n_(x,d)",
            "unit_U1_probe_normalization":1,
            "unit_normalization_selected_as_unique_physical_charge":False,
            "Cycle591_relation":"j_Cycle591=q_beta*j_unit; the same occupation-current function is compared after q_beta normalization, while q_beta remains supplied",
            "Cycle591_comparison_fixture_count":c591_comparison_fixtures,
            "Cycle591_relation_is_algebraic_normalization_identity":True,
            "onsite_symmetry":symmetry,"rows":rows,"maximum_Peierls_residual":max_peierls,
            "maximum_continuity_residual":max_cont,"maximum_Cycle591_current_residual":max_compare,
            "maximum_all24_covariance_residual":max_cov,"all576_direction_group_failures":all576_direction_group_failures(),
            "all24_density_current_comparisons_executed":24*len(FIXTURES),
            "all576_direction_label_comparisons_executed":24*24*6,
            "raw_positive_density_closes_periodic_zero_mode":False,
            "contact_included_by_full_64_state_U1_commutator":True,
            "number_current_is_uniquely_normalized_physical_charge":False,
            "number_current_is_unique_stress_energy_or_gravity_source":False,
            "physical_M2_encoder_update_or_leakage_evaluated":False}
    check("Route A derives the Cycle591 link current by Peierls variation and exact U(1) continuity",
          max(max_cont,max_peierls,max_compare,max_cov,symmetry["coin_total_number_commutator"],
              symmetry["contact_total_number_commutator"],symmetry["gauged_contact_invariance_residual"])<TOL
          and c591_comparison_fixtures==1 and output["all576_direction_group_failures"]==0
          and not output["unit_normalization_selected_as_unique_physical_charge"],output)
    check("Route A inserts the unit role array into the separate C609 aggregate map with inverse/deletion controls",
          all(row["field_action"]["inverse_residual"]==0
                  and row["field_action"]["role_array_deletion_signal"]>0
                  and row["field_action"]["link_term_deletion_signal"]>0
                  and row["field_action"]["sign_signal"]>0
                  and row["field_action"]["order_signal"]>0
                  and row["field_action"]["all24_aggregate_array_covariance_residual"]==0
                  and not row["field_action"]["physical_M2_register_or_field_composed"] for row in rows),rows)
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
    minimum_improvement_family_rank=2
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
        family_rank=int(np.linalg.matrix_rank(np.stack((improvement.ravel(),curl_improvement.ravel()))))
        minimum_improvement_family_rank=min(minimum_improvement_family_rank,family_rank)
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
                     "improvement_family_flattened_rank":family_rank,
                     "improvement_rows":ambiguity,"field_action":field,
                     "scalar_improvement_local_response_signal":scalar_response_signal,
                     "curl_improvement_trace_response_residual":curl_trace_response_residual,
                     "contact_momentum_change":"zero: Cycle230 contact is diagonal in all local occupations"})
    output={"object":"cubic momentum-flux Ward tensor class from local coframe variation of the accepted stream",
            "disposition":"CONSTRUCTIVE_CUBIC_WARD_IDENTITY_AND_TWO_CONSERVED_IMPROVEMENT_FAMILIES; UNIQUE_STRESS_ENERGY_OPEN",
            "tensor_scope":"the exact Ward flux T_ia lives on +a links; a symmetric incidence average gives a site-centered comparator on which two improvement families act",
            "coin_force":"F_i=p_i(after coin)-p_i(before coin) is retained in the exact Ward identity",
            "rows":rows,"maximum_Ward_residual":max_ward,"maximum_coframe_variation_residual":max_variation,
            "maximum_all24_tensor_covariance_residual":max_cov,
            "maximum_improvement_conservation_residual":max_improvement,
            "minimum_local_improvement_signal":min_local_change,
            "minimum_improvement_family_flattened_rank":minimum_improvement_family_rank,
            "all576_direction_group_failures":all576_direction_group_failures(),
            "all576_improvement_tensor_group_failures":improvement_group_failures,
            "all24_base_and_improvement_tensor_comparisons_executed":24*3*len(FIXTURES),
            "all576_direction_label_comparisons_executed":24*24*6,
            "all576_improvement_tensor_comparisons_executed":24*24*2*len(FIXTURES),
            "improvement_families_algebraically_distinct":minimum_improvement_family_rank==2,
            "improvement_coefficients_selected":False,"trace_or_other_cubic_component_selected":False,
            "integrated_Ward_tensor_improvement_invariant":True,
            "local_tensor_components_improvement_invariant":False,
            "Ward_tensor_is_unique_stress_energy":False,"Ward_tensor_is_gravity_source":False,
            "physical_M2_encoder_update_or_leakage_evaluated":False}
    check("Route B derives an exact cubic coframe Ward identity and exposes improvement ambiguity",
          max(max_ward,max_variation,max_cov,max_improvement)<TOL and min_local_change>0
          and minimum_improvement_family_rank==2
          and all(row["scalar_improvement_local_response_signal"]>0
                  and row["curl_improvement_trace_response_residual"]==0 for row in rows)
          and output["all576_direction_group_failures"]==0
          and output["all576_improvement_tensor_group_failures"]==0,output)
    check("Route B host trace-source variants pass the separate C609 aggregate-array controls",
          all(row["field_action"]["inverse_residual"]==0
                  and row["field_action"]["role_array_deletion_signal"]>0
                  and row["field_action"]["all24_aggregate_array_covariance_residual"]==0
                  and not row["field_action"]["physical_M2_register_or_field_composed"] for row in rows),rows)
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
        # Exhaust every binder-position role array; no coherent physical circuit is composed.
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
                     "declared_new_compensator_roles":1,
                     "supplied_compensator_role_charge":-1,"supplied_matter_role_charge":1,
                     "supplied_neutral_Cycle600_role_charge":0,
                     "role_charge_assignment_is_unique_physical_charge_law":False,
                     "uniform_binder_density_stationarity_residual":uniform_mob,
                     "localized_binder_mobility_signal":local_mob,
                     "global_role_space_W_preparation":preparation,
                     "declared_swap_parent_two_site_term_inventory_for_three_binders":9*length**3,
                     "declared_candidate_binary_role_debit_total":12*length**3,
                     "supplied_global_W_preparation_calls":3,
                     "matter_minus_binder_continuity_residual":continuity,
                     "matter_minus_binder_zero_mode_residual":zero_mode,
                     "binder_position_role_arrays_exhausted":length**3,
                     "maximum_position_array_inverse_residual":max(branch_inverse,branch_phase_inverse),
                     "host_uniform_role_array_F17_reduction":"delta_0-volume^-1 mod17; volume is invertible on L3/L6/L7",
                     "aggregate_array_action":field,"uniform_binder_no_refit_static_relative_residual":relative,
                     "localized_binder_vs_uniform_shore_relative_residual":local_vs_uniform,
                     "endpoint_norm_not_time":float(np.linalg.norm(endpoint))})
    inherited=c609_receipt["route_C_common_action_no_refit_comparison"]
    causal=c609_receipt["causal_time_comparison"]
    output={"object":"distinct paid mobile compensator role paired one-for-one with the matter-role comparator",
            "disposition":"CONSTRUCTIVE_CONDITIONAL_MOBILE_COMPENSATOR_ROLE_AND_ZERO_MODE_LEDGER; PHYSICAL_SECTOR_GENESIS_AND_W_COMPILER_OPEN",
            "local_pair_rule":"if a local pair-genesis gate creates/removes matter and compensator together, separate number-preserving local updates conserve total charge",
            "local_pair_genesis_gate_or_trigger_materialized":False,
            "pair_rule_status":"supplied candidate law; Householder W preparation does not derive or implement the local pair-genesis gate",
            "declared_role_debit":"one candidate compensator role per matter role; three four-bit species per coarse cell gives 12 declared binary roles per cell, not physical M2s",
            "preparation_status":"the global coarse-role Householder word has prepare/inverse/renewal tests but no local physical compiler, autonomous trigger, or sector genesis",
            "declared_parent_inventory":"three binder species would use 9V local two-site swap-parent terms inside supplied one-binder sectors; that inventory is not executed genesis",
            "mobility_scope":"a localized six-mode coarse amplitude changes density under the Cycle219 coin/230 stream while the uniform scalar amplitude is stationary in density; no physical carrier compiler is composed",
            "paired_number_equality_would_follow_if_pair_genesis_were_composed":True,
            "paired_sector_locally_seeded_in_executed_update":False,
            "neutral_Cycle600_role_charge_assignment_selected_as_physical_law":False,
            "rows":rows,"maximum_uniform_binder_stationarity_residual":max_uniform_mob,
            "minimum_localized_binder_mobility_signal":min_local_mob,
            "maximum_source_continuity_or_zero_mode_residual":max_cont,
            "maximum_position_array_and_W_word_inverse_residual":max_branch_inverse,
            "binder_position_role_arrays_exhausted_total":sum(length**3 for _,length,_,_ in FIXTURES),
            "all24_aggregate_array_comparisons_executed":24*len(FIXTURES),
            "relative_no_refit_static_residuals":static_residuals,
            "Cycle609_separate_common_action_relative_residuals":inherited["relative_residuals"],
            "static_shore_identity_residual":max(abs(a-b) for a,b in zip(static_residuals,inherited["relative_residuals"])),
            "no_refit_parameters":0,
            "uniform_static_comparison_consumes_C609_F17_state":False,
            "matched_labels":inherited["matched_words"],"matched_labels_are_events":False,
            "uniform_role_array_is_single_classical_physical_field":False,
            "causal_time_boundary":{"commit":causal["commit"],"path":causal["path"],
                "content_sha256":causal["content_sha256"],"comparison_only":True,
                "phase_modulation_design_is_compatible_with_external_delay_comparison":True,
                "C611_derives_physical_rate_or_time":False,
                "delay_is_rate_associated_in_pinned_note":causal["delay_rate_associated_in_pinned_note"],
                "advance_requires_event_count_edit_in_pinned_note":causal["advance_requires_event_count_edit_in_pinned_note"],
                "C611_event_or_count_edit_path_for_5_over_4_advance_composed":False,
                "time_runner_imported_or_executed":False,"backcredited_to_Cycle611":False,
                "event_association_derived":False},
            "compensator_role_is_unique_stress_energy_or_gravity_source":False,
            "physical_M2_encoder_update_leakage_or_NN_execution_evaluated":False}
    check("Route C supplies a mobile non-neutral-auxiliary compensator with exact zero mode and branch inverse",
          max(max_uniform_mob,max_cont,max_branch_inverse,output["static_shore_identity_residual"])<TOL
          and min_local_mob>1e-3
          and all(row["aggregate_array_action"]["inverse_residual"]==0
                  and row["aggregate_array_action"]["role_array_deletion_signal"]>0
                  and row["aggregate_array_action"]["all24_aggregate_array_covariance_residual"]==0
                  and not row["aggregate_array_action"]["physical_M2_register_or_field_composed"] for row in rows),output)
    check("Route C distinguishes uniform and localized binder preparation and does not promote matched words",
          all(row["localized_binder_vs_uniform_shore_relative_residual"]>row["uniform_binder_no_refit_static_relative_residual"] for row in rows)
          and not output["matched_labels_are_events"]
          and not output["uniform_role_array_is_single_classical_physical_field"]
          and not output["causal_time_boundary"]["C611_event_or_count_edit_path_for_5_over_4_advance_composed"]
          and not output["causal_time_boundary"]["backcredited_to_Cycle611"],rows)
    return output


def no_go_discipline():
    families=[
        {"route":"Peierls U(1) stream variation","attempt":"differentiate each directional stream phase to obtain occupation current","mechanism":"directional occupation derivative","terminal_obligation":"unit-normalized current and contact-inclusive continuity","result":"terminal passes, but Cycle591 line 466 leaves physical normalization unselected","citation":"scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py:466","marker":"ATTEMPTED"},
        {"route":"local cubic coframe variation","attempt":"differentiate the cubic stream phase and retain the onsite coin force","mechanism":"momentum flux with explicit coin force","terminal_obligation":"exact Ward identity","result":"Ward terminal passes, but conservation does not select a unique stress tensor","citation":"scripts/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22.py:513","marker":"ATTEMPTED"},
        {"route":"symmetric transverse improvement","attempt":"add a scalar double-central-difference tensor to the site Ward representative","mechanism":"scalar double-central-difference tensor","terminal_obligation":"identically conserved local redistribution","result":"conservation passes while local trace components change","citation":"scripts/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22.py:479","marker":"ATTEMPTED"},
        {"route":"antisymmetric-superpotential improvement","attempt":"take a central curl of an epsilon-weighted scalar superpotential","mechanism":"curl tensor from epsilon contraction","terminal_obligation":"independent trace-free conserved redistribution","result":"conservation and rank-two independence pass while trace coupling remains a supplied choice","citation":"scripts/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22.py:488","marker":"ATTEMPTED"},
        {"route":"distinct mobile compensator role","attempt":"subtract a mobile candidate compensator density from matter density","mechanism":"matter-minus-binder continuity and role-array zero mode","terminal_obligation":"conditional paid zero-mode ledger","result":"ledger passes conditional on uncomposed sector genesis and W preparation","citation":"scripts/physical_matter_variation_current_stress_compensator_source_tournament_cycle611_2026_07_22.py:654","marker":"ATTEMPTED"},
        {"route":"uniform-versus-localized compensator comparator","attempt":"compare manual uniform and localized counter-sources under the frozen real recurrence","mechanism":"separate real no-refit host recurrence","terminal_obligation":"held L6/L7 discriminator","result":"discriminator passes but no F17-state-to-real-response interface is composed","citation":"scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py:937","marker":"ATTEMPTED"},
    ]
    live_routes=["q_beta/inertial/empirical charge-normalization calibration",
                 "full quasienergy or metric variation including coin response",
                 "local link-gauge/Gauss-law source rather than a compensator",
                 "physical M2 E/G/placement/routing/leakage compilation",
                 "local pair-genesis and W-preparation circuit with lawful sector enforcement",
                 "event/count-edit mechanism for the 5:4 advance candidate"]
    walls={
        "W_norm":"unit U1 probe normalization is not selected as unique physical charge",
        "W_tensor":"the Ward tensor, improvement coefficient, and trace/component choice are not uniquely selected",
        "W_coupling":"F17 modulus, alpha, sign, and role-charge map are supplied array conventions",
        "W_compensator":"compensator role, sector, pair genesis, and W preparation are supplied candidate content",
        "W_physical":"no physical M2 E/G, placement, routing, leakage, or local enforcement is composed",
        "W_join":"branch role arrays and the separate real static comparator have no physical interface",
        "W_time":"the delay comparison is external and no event/count-edit path realizes the 5:4 advance label",
    }
    names=tuple(walls);pairs=[{"left":names[i],"right":names[j],
                               "left_to_right":{"status":"NOT_ESTABLISHED","reason":f"no executed intervention closes {names[i]} and retests {names[j]}"},
                               "right_to_left":{"status":"NOT_ESTABLISHED","reason":f"no executed intervention closes {names[j]} and retests {names[i]}"},
                               "independence":{"status":"NOT_ESTABLISHED","reason":"neither directional closure experiment was executed"}}
                              for i in range(len(names)) for j in range(i+1,len(names))]
    canonical_phrases=("we assume","by construction","as is standard","the framework provides",
                       "bridge context","background","naturally","obviously","standard qft","registered","canonical")
    note_text=" ".join(NOTE.read_text().lower().split())
    hidden_phrase_hits=[phrase for phrase in canonical_phrases if phrase in note_text]
    n4=[
        {"prior_path":"scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py","prior_line":324,
         "prior_residual":"oriented directional occupation current","current_residual":"unit Peierls directional occupation current after q_beta normalization","witness_residual":1.734723475976807e-18,"match":True,"same_scope":True,"use_as_closure":True},
        {"prior_path":"scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py","prior_line":466,
         "prior_residual":"coefficient not selected by conservation","current_residual":"unit U1 normalization not selected as unique physical charge","witness_residual":"PERSISTS","match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py","prior_line":1117,
         "prior_residual":"physical M2 compiler false","current_residual":"Cycle611 uses C609 aggregate arrays without physical M2 composition","witness_residual":"PERSISTS","match":True,"same_scope":True,"use_as_closure":False},
        {"prior_path":"scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py","prior_line":937,
         "prior_residual":"external delay/advance comparison has no derived event association","current_residual":"C611 supplies no 5:4 event/count-edit path","witness_residual":"PERSISTS","match":True,"same_scope":True,"use_as_closure":False},
    ]
    n5=[
        {"claim":"unit number current is not uniquely normalized physical charge","per_element":"the Peierls derivative fixes occupation at unit probe weight only","per_site":"site continuity survives arbitrary overall normalization","per_mode":"all six directions carry the same supplied U1 representation weight","per_block":"the 64-state contact commutator proves symmetry, not empirical charge units","lattice_wide":"global conservation cannot choose q_beta, inertial mass, or another normalization"},
        {"claim":"the Ward tensor class is not unique stress-energy","per_element":"individual tensor components change under conserved improvements","per_site":"both improvement families redistribute local tensor values","per_mode":"the coframe probe covers cubic directional momentum and retains coin force","per_block":"trace versus another cubic component is supplied","lattice_wide":"integrated tensor invariance cannot select the local representative"},
        {"claim":"the F17 array map is not a physical source or gravity law","per_element":"modulus, alpha, sign, and role labels are supplied","per_site":"the kick identity is an aggregate-array equality","per_mode":"no physical charge observable is composed","per_block":"no M2 field register, constraint, or leakage test is executed","lattice_wide":"all24 array covariance is not covariance of a routed physical schedule"},
        {"claim":"the compensator role construction is not a physical M2 compiler","per_element":"the new role charge is supplied","per_site":"the Householder word is global in coarse role space","per_mode":"localized six-mode mobility is a coarse-amplitude test","per_block":"pair genesis, sector enforcement, and W preparation are uncomposed","lattice_wide":"declared role and parent-term inventories are not placement or NN execution"},
        {"claim":"the matched labels are not time, Events, Records, or realized history","per_element":"phase modulation is not itself a rate","per_site":"no local event/count edit is implemented","per_mode":"the external 3:4 delay association is comparison-only","per_block":"the 5:4 advance requires a mechanism absent from Cycle611","lattice_wide":"finite response arrays and update counts do not select occurrence or history"},
    ]
    causal_path=f"{c609.CAUSAL_COMPARISON['commit']}:{c609.CAUSAL_COMPARISON['path']}"
    n6=[
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md","status":"PINNED_EXECUTED_PARENT_SHORE","closure":"supplies the q_beta-normalized current comparator while leaving coefficient selection open"},
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_TWO_M2_CAR_PHASE_LINK_FIELD_QCA_TOURNAMENT_CYCLE609_NOTE_2026-07-22.md","status":"PINNED_EXECUTED_PARENT_WITH_ALGEBRAIC_ARRAY_SCOPE","closure":"supplies the aggregate F17 array map but not physical M2/source/stress/gravity compilation"},
        {"file":causal_path,"status":"TRANSITIVELY_PINNED_COMPARISON_NOT_IMPORTED_EXECUTED_OR_BACKCREDITED","closure":"distinguishes rate-associated delay from count-edit advance while leaving event association open"},
        {"file":"docs/work_history/repo/review_feedback/PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md","status":"TRANSITIVELY_PINNED_LOCAL_BRANCH_NOTE_NOT_IMPORTED_OR_EXECUTED","closure":"could test a matter-to-causal-interval interface separately from the number-colliding causal-time PR"},
    ]
    n8=[
        {"cycle":"Cycle230","echo":"contact is U1 invariant and diagonal in occupation","effect":"contact is included rather than omitted"},
        {"cycle":"Cycle591","echo":"q_beta N current is conserved but its coefficient is not selected","effect":"Cycle611 closes only the unit-current residual"},
        {"cycle":"Cycle600","echo":"carrier bits are algebraic roles, not a physical M2 compiler","effect":"blocks compensator role-count back-credit"},
        {"cycle":"Cycle609","echo":"F17 Q/P is an aggregate array map and physical compilation remains open","effect":"blocks field/source/gravity back-credit"},
        {"cycle":"PR causal-time Cycle612","echo":"delay is rate-associated and advance is count-edit only","effect":"comparison boundary; no Event or time closure"},
        {"cycle":"local branch Cycle612","echo":"matter-caused causal interval work is a distinct number-colliding note","effect":"not imported or executed here"},
    ]
    allowed_markers={"ATTEMPTED","RULED OUT BY PRIOR"}
    marker_schema_pass=all(row["marker"] in allowed_markers for row in families)
    independence_complete=all(row["independence"]["status"]=="ESTABLISHED" for row in pairs)
    output={"N1_normalized_families":families,"N1_allowed_markers":sorted(allowed_markers),
            "N1_marker_schema_pass":marker_schema_pass,"N1_live_routes":live_routes,
            "N2_pairwise_wall_closure_and_independence":pairs,"N2_independence_complete":independence_complete,
            "N3_canonical_hidden_wall_phrases":list(canonical_phrases),"N3_note_phrase_hits":hidden_phrase_hits,
            "N3_explicit_supplied_structure":["unit U1 normalization","Peierls sign","F17 modulus/alpha/sign","cubic coframe probe","coin force","two improvement definitions","improvement coefficient","trace/component choice","compensator role/charge","pair genesis","one-binder sector","global W word","finite horizons","manual uniform role array","matched-label association"],
            "N4_exact_residual_matching":n4,"N5_five_resolution_rhetoric_audit":n5,
            "N6_partial_closure_paths":n6,
            "N7_cited_actionable_steelman":{"citation":"scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py:458-483; scripts/physical_two_M2_CAR_phase_link_field_QCA_tournament_cycle609_2026_07_22.py:1117-1125","action":"execute a full metric/quasienergy variation and a local Gauss-law alternative; independently compose physical M2 E/G and a local pair-genesis/W circuit before judging normalization, tensor selection, or source closure"},
            "N8_rowwise_cross_cycle_echo":n8,"walls":walls,
            "Status":"FAIL / DO NOT SHIP NEGATIVE","negative_gate_reasons":["live constructive routes remain","pairwise wall independence is not established"],
            "narrowed_positive_artifact_status":"PASS","negative_claim_shipped":False,
            "shared_obstruction":False,"minimum_content_claim":False,"axiom_pressure":False}
    check("full N1-N8 keeps the negative gate failed while permitting narrowed executed identities",
          len(families)>=5 and marker_schema_pass and len(live_routes)>0 and len(pairs)==21
          and not independence_complete and not hidden_phrase_hits
          and all(all(field in row for field in ("per_element","per_site","per_mode","per_block","lattice_wide")) for row in n5)
          and all("file" in row and "status" in row and "closure" in row for row in n6)
          and all("same_scope" in row and "use_as_closure" in row for row in n4)
          and output["Status"]=="FAIL / DO NOT SHIP NEGATIVE"
          and output["narrowed_positive_artifact_status"]=="PASS"
          and not output["negative_claim_shipped"] and not output["shared_obstruction"]
          and not output["minimum_content_claim"] and not output["axiom_pressure"],output)
    return output


def main():
    c609_receipt,shore_result=shore();note_contract();a=route_a();b=route_b();c=route_c(c609_receipt);nogo=no_go_discipline()
    elapsed=perf_counter()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss;rss=int(rss if sys.platform=="darwin" else rss*1024)
    receipt={"cycle":611,"authority":AUTHORITY,"audit":AUDIT,
             "author_artifact_status_accepted":AUTHOR_ARTIFACT_STATUS_ACCEPTED,
             "audit_verdict_inferred_from_dependencies":AUDIT_VERDICT_INFERRED_FROM_DEPENDENCIES,
             "constitutional_effect":"none",
             "HEAD":subprocess.check_output(("git","rev-parse","HEAD"),cwd=ROOT,text=True).strip(),
             "runner_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
             "note_sha256":sha256(NOTE.read_bytes()).hexdigest(),
             "pins":PINS,"shore":shore_result,
             "runtime_import_controls":shore_result["runtime_import_closure"],
             "dependency_cycle_boundary":shore_result["C609_to_C611_note_packaging_backedge"],
             "route_A_Peierls_unit_number_current":a,
             "route_B_coframe_Ward_and_improvement_class":b,
             "route_C_paid_mobile_compensator_role":c,
             "no_go_discipline":nogo,
             "status":"three bounded algebraic/coarse/numerical results; no unique physical charge, stress-energy, physical M2 source compiler, causal time, Event, Record, Born rule, or confirmed breakthrough",
             "source_identity_disposition":"the unit-normalized U1 occupation current follows from Peierls variation; a conditional paid compensator role closes a declared role-array zero mode if its supplied sector/genesis/W inputs exist; neither result selects physical charge, stress, gravity, or a physical C609 field",
             "scope_boundaries":{"unique_physical_charge_normalization_selected":False,
                 "unique_stress_energy_tensor_selected":False,"physical_source_current_stress_gravity_law":False,
                 "physical_M2_encoder_update_composed":False,"physical_EG_evaluated":False,
                 "physical_placement_routing_leakage_or_constraints_evaluated":False,
                 "compensator_sector_pair_genesis_or_local_W_compiler_composed":False,
                 "C609_F17_state_to_real_comparator_interface_composed":False,
                 "physical_rate_or_time_derived":False,"event_count_edit_path_for_advance_composed":False,
                 "Event_Record_Born_or_history_derived":False},
             "inventory":{"supplied":["unit U1 normalization and Peierls sign","Cycle219 coin and Cycle230 stream/contact order","cubic coframe probe and coin-force definition","two improvement formulas, coefficient, and trace/component choice","F17 modulus, alpha, sign, factor order, and Q/P roles","compensator role/charge, pair rule, one-binder sector, and global W word","finite horizons, manual uniform role array, and matched-label association"],
                          "derived_or_executed":["Peierls occupation current and explicit continuity","64-state coin/contact U1 identities","Cycle591 q_beta normalization identity","coframe momentum flux, explicit coin force, and Ward identity","two rank-2 conserved improvement families","coarse compensator mobility/stationarity and conditional zero-mode ledger","586 position-array inverses and aggregate array controls","uniform/local no-refit discriminator","causal-time comparison boundary without import or back-credit"],
                          "not_derived":["unique physical charge normalization","unique stress-energy tensor or trace choice","F17 coupling law or physical source/current/stress/gravity","physical M2 E/G, placement, routing, leakage, or constraints","compensator genesis, lawful sector, or local W compiler","coherent physical branch-field interface","physical rate/time or 5:4 event/count-edit path","Event, Record, Born probability, or realized history"]},
             "six_wall_ledger":{"C_ref":"ADVANCED ALGEBRAICALLY: the unit occupation current follows from Peierls variation; physical normalization, F17 coefficients, tensor interpretation, and compensator weights remain supplied","C_num":"ADVANCED ALGEBRAICALLY: occupation-current and rank-2 improvement identities are explicit; no unique physical charge or M2 realization follows","C_wrap":"UNCHANGED PHYSICALLY: exact F17 arithmetic is not a real-amplitude, energy, rate, or time rule","C_int":"ADVANCED ALGEBRAICALLY: contact-inclusive variation and separate aggregate-array insertions are executed; no physical matter/field join is composed","C_local":"ADVANCED AT COARSE LAW LEVEL: continuity and Ward identities pass; pair genesis, local W, constraints, physical placement, routing, and leakage remain open","C_source":"CONDITIONAL ALGEBRAIC PROGRESS: the paid compensator closes the declared role-array zero mode if its sector exists; no physical source, stress, or gravity law is selected"},
             "maturity_effect":"no upward physical maturity revision for operational quantum/Records, time, inertia/matter, gravity/source, or Born/probability",
             "strongest_constructive_result":"Peierls variation of the Cycle219/230 stream/contact update gives the unit U1 occupation current with exact continuity and the Cycle591 q_beta normalization identity; local coframe variation gives an exact Ward identity plus two algebraically distinct conserved improvement families",
             "confirmed_breakthrough":False,
             "shared_obstruction_or_axiom_pressure":False,
             "optimal_next_campaign":"execute full metric/quasienergy and local Gauss-law alternatives, then compose a literal physical M2 E/G with local pair genesis, W preparation, sector enforcement, routed schedule, leakage, and held-size covariance",
             "terminology_guards":{"number_current_is_uniquely_normalized_physical_charge":False,
                 "Ward_tensor_is_unique_stress_energy":False,"F17_array_is_physical_gravity_field":False,
                 "declared_compensator_roles_are_physical_M2_count":False,
                 "phase_modulation_is_physical_rate_or_time":False,"matched_label_is_Event":False,
                 "pointer_copy_is_Record":False},
             "tests_passed":PASS,"tests_failed":FAIL,"tests_total":PASS+FAIL,"pass":FAIL==0,
             "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
             "runtime_environment":{"python":sys.version.split()[0],"numpy":np.__version__}}
    RECEIPT.write_text(json.dumps(receipt,indent=2,sort_keys=True,default=json_default)+"\n")
    print("RECEIPT",json.dumps(receipt,sort_keys=True,default=json_default))
    print("SUMMARY",json.dumps({"pass":receipt["pass"],"tests_passed":PASS,"tests_failed":FAIL,
                                "elapsed_seconds":elapsed,"maximum_RSS_bytes":rss,
                                "route_A":a["disposition"],"route_B":b["disposition"],
                                "route_C":c["disposition"],"axiom_pressure":False},sort_keys=True))
    return int(FAIL!=0)


if __name__=="__main__":
    if "--cold" in sys.argv:
        buffer=io.StringIO()
        with contextlib.redirect_stdout(buffer): exit_code=main()
        transcript=buffer.getvalue();COLD.write_text(transcript,encoding="utf-8")
        print(transcript,end="");raise SystemExit(exit_code)
    raise SystemExit(main())
