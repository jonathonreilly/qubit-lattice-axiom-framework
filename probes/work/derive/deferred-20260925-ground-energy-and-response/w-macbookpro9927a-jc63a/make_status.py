#!/usr/bin/env python3
"""Write RECOVERY_STATUS.json for J:derive:deferred-20260925-ground-energy-and-response:a1."""
import hashlib
import json
import os
import subprocess

NOTE = "docs/ORIGINAL_FORMATION_AND_FIELD_RESPONSE_BUDGET_BOUNDED_THEOREM_NOTE_2026-09-25.md"
FROZEN = "a4cb43ee996adcc63b13da4fe7501e11643eddeb"
LANDING = "6b414efff904b7958b5a407686f5b0885d9a1dd7"
MAIN = "78db61c32a39234bab16034c57361bf0c418c0b1"
EXPECT = {FROZEN: "fb7e648244754b469504f08aa4cd251148d3736740af4f55c7e5c63675c23d14",
          LANDING: "558196a13e1f273fda420e39906fde3bf544ff73b66f773dab6b081049a07071",
          MAIN: "558196a13e1f273fda420e39906fde3bf544ff73b66f773dab6b081049a07071"}
PRE = "probes/work/deferred-science-20260925/sources/e02c3983ce098b6af566a03a603b8c484f17bd50626181851c3895e27101fcda"
REVIEW = "probes/work/deferred-science-20260925/unit-28.json"
EXPECT_REVIEW = "f67dca42a90443b320a91c41a7f44b89dcddbf704bda6e9187a8d13dbac256cc"


def sha_rev(rev, path):
    return hashlib.sha256(subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True,
                                         check=True).stdout).hexdigest()


root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
heads = {r: {"sha256": sha_rev(r, NOTE)} for r in (FROZEN, LANDING, MAIN)}
for r in heads:
    heads[r]["sha256_verified"] = heads[r]["sha256"] == EXPECT[r]
pre_sha = hashlib.sha256(open(os.path.join(root, PRE), "rb").read()).hexdigest()
rev_sha = hashlib.sha256(open(os.path.join(root, REVIEW), "rb").read()).hexdigest()
status = {
    "task": "J:derive:deferred-20260925-ground-energy-and-response:a1",
    "worker": "w-macbookpro9927a-jc63a",
    "model": "claude-opus-5-5",
    "origin_main_sha": MAIN,
    "disposition_group": {"name": "ground-energy-and-response", "prs": [9199, 9206, 9208]},
    "source": {"pr": 9208, "note": NOTE, "frozen_head_task": FROZEN, "landing_commit": LANDING,
               "note_heads": heads,
               "review_PRE_source": PRE, "review_PRE_sha256": pre_sha,
               "review_PRE_verified": pre_sha == PRE.rsplit("/", 1)[1],
               "review_record": REVIEW, "review_record_sha256": rev_sha,
               "review_record_verified": rev_sha == EXPECT_REVIEW},
    "review_corrections_preserved": [
        "the response is an initial-lag slope at finite preparation time; no finite-lag kernel, attenuation law, "
        "stationary spectrum or microscopic derivative transfer follows",
        "fixed finite graph and couplings; no volume-uniform bound",
        "the probe is a mathematical kick of the supplied dynamics, not an implemented source or detector",
        "#9199: cyclic support, variational infimum, filling and instantaneous activity stay distinct; "
        "#9206: residence bounds with returns, no monotone energy or thermal reading"],
    "obligation_selected": "the normal-state moment-free initial-lag response of #9208 (the 'moment-free response' "
                           "historical claim): proof and validation of the review PRE's bounded strong-quotient route",
    "proved_or_checked": {
        "D1": "mixed second difference of the gated electric term = 2 eps tau v n^2 per edge",
        "D2": "A_p = 2(v_b1 + v_b2) <= 4 on every elementary plaquette",
        "C1": "exact commutator identity [U_u(W^eps), W^tau] on a single-edge rotor",
        "L1": "strong limit and explicit slope operators; R_XX + R_YY = 2KA = F",
        "S1": "a quartic electric term has an unbounded mixed difference: the route fails there"},
    "assumed": ["the parents' fixed-graph facts as supplied in #9208: self-adjoint h on the multiplication domain of "
                "D, bounded H4 and formation channels, the trace-preserving CP semigroup built by the bounded-"
                "perturbation Dyson series"],
    "result": "for every normal initial density the lag slope exists and equals Tr rho_t [Q_b,[KD,Q_a]]; the "
              "quadrature sum is Tr rho_t F_nu; the landed note's fourth-moment hypothesis is not needed for its "
              "(3)-(5); validated independently of the review PRE (same route)",
    "first_unresolved_step": "#9199's and #9206's stronger historical claims (filling/activity; late-time "
                             "budget), not attempted here",
    "remaining_obligations": [
        "#9199: whether any ground eigenvector exists on the native graph and relates variational infimum to "
        "filling or activity",
        "#9206: a late-time formation budget without returns in the residence bounds",
        "volume-uniform control of the response (the bounds depend on the fixed graph)"],
    "related_tasks": {"J:derive:deferred-20260925-energy-moments-and-apparatus:a1": "distinct; not duplicated"},
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RECOVERY_STATUS.json")
json.dump(status, open(out, "w"), indent=1)
print("wrote", out, all(h["sha256_verified"] for h in heads.values()), status["source"]["review_PRE_verified"],
      status["source"]["review_record_verified"])
