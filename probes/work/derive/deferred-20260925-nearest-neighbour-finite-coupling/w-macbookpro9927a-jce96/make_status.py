#!/usr/bin/env python3
"""Write RECOVERY_STATUS.json for J:derive:deferred-20260925-nearest-neighbour-finite-coupling:a1
(sha256-verified source revisions of block 142 and its landing review record)."""
import hashlib
import json
import os
import subprocess

NOTE = ("docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_PAIRS_BOUND_AS_NEIGHBOURS_HAVE_HALF_THE_WALKERS_SPEED_"
        "SQUARED_ON_A_LINE_AND_NEVER_ITS_SPEED_IN_EVERY_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-25.md")
REVIEW = "probes/work/deferred-science-20260925/unit-29.json"
FROZEN = "5c7c52847eeb03489813c0ddf3094759f9bd7a9c"
LANDING = "25b8c1874f2ea657653dbb298bf383c18d81e0b5"
MAIN = "78db61c32a39234bab16034c57361bf0c418c0b1"
EXPECT = {FROZEN: "350fd6eb1acedfe933d08d444617d59c9c9e5bd3b273d49df807548688f596ea",
          MAIN: "fb9b11df679056a0c94dd05d8b9a3661679b28c71318fdf2aa485917d54c0b9e"}
EXPECT_REVIEW = "5e36b2d69c898914c0bbe5d336df2f1de6e59676901879e01fa2bf465d80088a"


def sha_rev(rev, path):
    blob = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
    return hashlib.sha256(blob).hexdigest()


heads = {}
for rev in (FROZEN, LANDING, MAIN):
    h = sha_rev(rev, NOTE)
    heads[rev] = {"sha256": h, "sha256_verified": h == EXPECT.get(rev, EXPECT[MAIN])}
root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
rh = hashlib.sha256(open(os.path.join(root, REVIEW), "rb").read()).hexdigest()
status = {
    "task": "J:derive:deferred-20260925-nearest-neighbour-finite-coupling:a1",
    "worker": "w-macbookpro9927a-jce96",
    "model": "claude-opus-5-5",
    "origin_main_sha": MAIN,
    "source": {"pr": 9227, "block": 142, "note": NOTE, "frozen_head_task": FROZEN, "landing_commit": LANDING,
               "note_heads": heads, "note_landed_equals_main": heads[LANDING]["sha256"] == heads[MAIN]["sha256"],
               "review_record": REVIEW, "review_record_sha256": rh, "review_record_verified": rh == EXPECT_REVIEW},
    "review_corrections_preserved": [
        "claim_scope as landed: exact line branches need V nonzero and |b(K)/V| < 1; in three dimensions only the "
        "second-order effective generator at a fixed nonzero isolated bond eigenvalue with fixed gaps as |g| -> infinity",
        "not an all-coupling speed, stability or fall theorem; curvatures are not established physical speeds, "
        "inertial stability or passive fall coefficients",
        "zero bond eigenvalues and gaps shrinking with g stay outside the statement"],
    "obligation_selected": "controlled finite-coupling corrections for the coin-blind bond term (M = 1): exact "
                           "Feshbach control of the levels and the first correction to the energy-squared curvature",
    "proved_or_checked": {
        "R1": "block 142's same-bond law reproduced exactly; no link between a bond's two ends at orders 2 and 4; "
              "odd orders empty",
        "R2": "coin-blind rest levels and leading axis sums equal block 142 T3(c)'s rows",
        "F1": "window, contraction and tail constants for |g| >= 20: |E_j - E_j^(4)| <= 1856/(|g|-1)^5",
        "X1": "E^2/2 - g^2/2 = spectrum of L2 + (L4 - L2^2/2)/g^2 to O(g^-4)",
        "N1": "[L2(0), Delta(0)] = 0; level shifts delta; first-order K terms vanish",
        "N2": "O(g^-2) axis-sum corrections per level (exact)",
        "I1": "inertial K^2-form of E at rest = W/E0 at every order",
        "C1": "[float] box diagonalisation at g = 20 agrees with the expansion to 2.5e-5 (leading order: >= 8.7e-4)"},
    "assumed": ["none beyond block 142's supplied model (walk, exclusion, coin-blind neighbour term)"],
    "result": "the axis-sum bound 3/2 is a leading-order statement: at next order two fermion states of the coin-blind "
              "3/2 level reach 3/2 + 3/(2g^2); all corrections exact; levels controlled for |g| >= 20",
    "first_unresolved_step": "the curvature remainder at O(g^-4) with explicit constants (the energies are "
                             "controlled; the K^2-forms are analytic in 1/g^2 but not bounded explicitly here)",
    "remaining_obligations": [
        "the covariant non-coin-blind shifts (ray, spin +-1 plane): extra mixing through the other bond eigenspaces "
        "enters at the same order",
        "moderate coupling |g| < 20 and the predicted merging of the fermion rest levels 4 and 5 near g^2 = 15.5 "
        "(from the truncated shifts, not a claim)",
        "passive (fall) response under block 115's conditional ray model"],
    "related_tasks": {"J:derive:deferred-20260925-charge-threshold-and-transport:a1": "distinct; not duplicated"},
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RECOVERY_STATUS.json")
with open(out, "w") as fh:
    json.dump(status, fh, indent=1)
print("wrote", out, "verified:", all(v["sha256_verified"] for v in heads.values()), rh == EXPECT_REVIEW)
