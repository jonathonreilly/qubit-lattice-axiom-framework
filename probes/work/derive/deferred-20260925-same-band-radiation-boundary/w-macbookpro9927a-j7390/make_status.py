#!/usr/bin/env python3
"""Write RECOVERY_STATUS.json for J:derive:deferred-20260925-same-band-radiation-boundary:a1 (sha256-verified heads)."""
import hashlib
import json
import subprocess

NOTE = ("docs/ADMISSIBILITY_RULE_A_FREE_WALKER_NEVER_EMITS_OR_ABSORBS_ONE_OF_THE_MEMBERS_TRAVELLING_DISTURBANCES_"
        "ITS_ENERGIES_STAY_INSIDE_THE_MEMBERS_CONE_BOUNDED_THEOREM_NOTE_2026-09-25.md")
FROZEN = "bea8e806aa67aed2657544d7820cc7fcaec67b0a"
CURRENT = "5aacd93e4b1b48ad8d8e2122698498555234d83a"
MAIN = "25b8c1874f2ea657653dbb298bf383c18d81e0b5"
EXPECT = {FROZEN: "a39555970c359e1692e4ea77e93a52165b61ee03df6724fd22c909797596abca",
          CURRENT: "27f9b2b9969627e71257d35af925c10924ecd6d05dbc4027bbf1b833df412263"}


def sha(rev):
    blob = subprocess.run(["git", "show", f"{rev}:{NOTE}"], capture_output=True, check=True).stdout
    return hashlib.sha256(blob).hexdigest()


heads = {}
for rev in (FROZEN, CURRENT):
    h = sha(rev)
    heads[rev] = {"sha256": h, "sha256_verified": h == EXPECT[rev]}
on_main = subprocess.run(["git", "cat-file", "-e", f"{MAIN}:{NOTE}"], capture_output=True).returncode == 0
status = {
    "task": "J:derive:deferred-20260925-same-band-radiation-boundary:a1",
    "worker": "w-macbookpro9927a-j7390",
    "model": "claude-opus-5-5",
    "origin_main_sha": MAIN,
    "source": {"pr": 9242, "block": 149, "note": NOTE, "on_origin_main": on_main,
               "frozen_head_task": FROZEN, "current_head": CURRENT, "heads": heads},
    "review_corrections_preserved": [
        "the universal kinematic no-go is refuted: interband (pair-creation) energy/momentum resonances exist "
        "(block 149 current head T5); T1-T4 are within-one-band statements only",
        "block 149 T5 computes no rate; this pass computes one amplitude, not a rate",
        "the member's disturbances as quanta of energy |p(q)| is an explicit supplied assumption, not derived"],
    "obligation_selected": "an actual transition matrix element and occupation constraint for one interband resonance "
                           "with the stress coupling (1/2) Theta_ij h_ij of block 136 and a TT disturbance",
    "proved_or_checked": {
        "S1": "plane-wave form factor of block 136's K_a^j and Theta_ij (Laurent identity, exact)",
        "S2": "stress and energy vertices vanish exactly at every symmetric resonance k = q/2 + pi nu",
        "S3": "exact non-symmetric resonance: algebraic root of a degree-8 polynomial, genuine after squaring",
        "S4": "nonzero TT amplitude there (rigorous interval arithmetic), both site conventions, both polarizations"},
    "assumed": ["single-quantum energy |p(q)| for one member disturbance (explicit)",
                "the supplied coupling (1/2) sum Theta_ij h_ij and block 120's stress as the vertex",
                "the half-filled sea (exclusion supplied, block 128's exchange sign)"],
    "result": "nonzero allowed single-quantum interband amplitude (pair creation from the filled sea) at an exact "
              "non-symmetric resonance; exact suppression at the symmetric resonances",
    "first_unresolved_step": "the rate: the phase-space integral of |amplitude|^2 over the resonance surface "
                             "(near the symmetric saddle the vertex vanishes linearly) and the member quantum's "
                             "normalization (a quantization of the member not supplied by the landed notes)",
    "remaining_obligations": [
        "rate and threshold behaviour (the channel closes for |p(q)| < 2 mu with the staggered mass, block 149 T5)",
        "the clock (energy-density) coupling and the shift coupling at non-symmetric resonances",
        "whether any supplied selection rule suppresses the non-symmetric resonances (none found here)"],
    "related_tasks": {"J:derive:deferred-20260925-nonlinear-moving-source-completion:a1": "distinct; not duplicated"},
}
with open("RECOVERY_STATUS.json", "w") as fh:
    json.dump(status, fh, indent=1)
print("heads verified:", all(v["sha256_verified"] for v in heads.values()), "on main:", on_main)
