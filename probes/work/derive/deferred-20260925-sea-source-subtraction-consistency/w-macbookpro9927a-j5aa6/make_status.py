#!/usr/bin/env python3
"""Write RECOVERY_STATUS.json for J:derive:deferred-20260925-sea-source-subtraction-consistency:a1
(sha256-verified heads of block 147's note)."""
import hashlib
import json
import os
import subprocess

NOTE = ("docs/ADMISSIBILITY_RULE_THE_MEMBERS_ZERO_MODE_TESTS_THE_ZERO_OF_ENERGY_IF_THE_MEMBER_SEES_THE_"
        "HALF_FILLED_SEA_A_CLOSED_LATTICE_BOUNCES_OR_CANNOT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-25.md")
FROZEN = "b88ec3d5f3e7e0494032ead91fa1826af27d9087"
CURRENT = "328ab4891090177ca50a660581cd520ef75873a6"
MAIN = "25b8c1874f2ea657653dbb298bf383c18d81e0b5"
EXPECT = {FROZEN: "a630ce79889b2617387beb892152f4b50856e87b21497b4cbd27a3716630d3d8",
          CURRENT: "ae09658f0a8f172d0bc82e4fb1eb914095fea6595fbbb88a17739af042bba0d5"}


def sha(rev):
    blob = subprocess.run(["git", "show", f"{rev}:{NOTE}"], capture_output=True, check=True).stdout
    return hashlib.sha256(blob).hexdigest()


heads = {}
for rev in (FROZEN, CURRENT):
    h = sha(rev)
    heads[rev] = {"sha256": h, "sha256_verified": h == EXPECT[rev]}
on_main = subprocess.run(["git", "cat-file", "-e", f"{MAIN}:{NOTE}"], capture_output=True).returncode == 0
status = {
    "task": "J:derive:deferred-20260925-sea-source-subtraction-consistency:a1",
    "worker": "w-macbookpro9927a-j5aa6",
    "model": "claude-opus-5-5",
    "origin_main_sha": MAIN,
    "source": {"pr": 9240, "block": 147, "note": NOTE, "on_origin_main": on_main,
               "frozen_head_task": FROZEN, "current_head": CURRENT, "heads": heads},
    "review_corrections_preserved": [
        "current head T1(e): with block 146's pressure the massless sea has p = rho/3 and the massive sea "
        "0 < p/rho < 1/3; an energy constant per unit volume would need p = -rho",
        "current head: every sea quantity counts all eight light species",
        "which zero the member sees stays a reading question for the owner; no vacuum is selected here",
        "free fermions are distinguished from fully occupied hard-core hopping, which is blocked"],
    "obligation_selected": "energy and pressure counterterms for the instantaneous free sea energy and its "
                           "subtraction on an evolving uniformly stretched lattice, and their conservation",
    "proved_or_checked": {
        "K1": "massless sea -I/l: p = rho/3; subtraction counterterm +I/l with p_ct = rho_ct/3; a subtraction "
              "constant in time leaves I/l0 - I/l",
        "K2": "massive mode p/rho = y/(3(mu^2+y)) (block 147 T1(e), restated)",
        "C1": "||[H_l1, H_l2]||^2 = 16 mu^2 |s|^2 (1/l1 - 1/l2)^2 per block; mu = 0 gives H_l = H_1/l",
        "A1": "two-sector reduction; interband element; first-order excitation amplitude nonzero iff mu|s| != 0",
        "M1": "first-order adiabatic dressing equals (1/2) m lamdot^2, m = 2|<+|d h|->|^2/(2E)^3",
        "M2": "m_lam per site = <mu^2 |s|^2 / (4 l^2 E^5)> = 4 x #9259's dilation part at l = 1",
        "N1": "Noether energy of L_sea + L_member conserved",
        "H1": "fully occupied hard-core hopping annihilates the state"},
    "assumed": ["leading-order adiabatic expansion (asymptotic in lamdot for smooth histories, gap >= 2 mu > 0)",
                "block 60's crossing-of-bonds premise (hopping / l, staggered mass unscaled) and block 146's "
                "first law dm/dlam = -3 p l^3, as supplied by block 147",
                "the half-filled free sea (exclusion supplied, block 128's exchange sign)"],
    "result": "massless: the instantaneous sea energy is exact for every history and its subtraction is "
              "consistent with an l-dependent counterterm (p = rho/3); massive: neither is the evolving sea's "
              "energy at any finite rate; at leading adiabatic order the consistent conditional prescription "
              "adds the cranking term (1/2) m_lam lamdot^2",
    "first_unresolved_step": "beyond leading adiabatic order: irreversible pair creation for a given history "
                             "(exponentially small for analytic histories, Landau-Zener type) and its "
                             "back-reaction on the zero mode; the member's own reading of which zero it sees",
    "remaining_obligations": [
        "the sea's inertia added to the member's zero mode: the effective kinetic coefficient c_k + m_lam/l^3 "
        "and whether it changes block 147 T2's bounce and threshold",
        "the half-filled hard-core sea with the staggered mass (non-commuting as well; exact small cases)",
        "non-uniform stretches (shear) for the massive sea"],
    "related_prior_work": {"#9259": "the cranking inertia of the same sea (dilation part reused here)",
                           "#9198": "the massless sea's energy constant I = <|s|>"},
    "related_tasks": {"J:derive:deferred-20260925-nonlinear-moving-source-completion:a1": "distinct; released "
                      "by this worker as broad; not duplicated"},
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RECOVERY_STATUS.json")
with open(out, "w") as fh:
    json.dump(status, fh, indent=1)
print("wrote", out, "verified:", all(v["sha256_verified"] for v in heads.values()), "on_main:", on_main)
