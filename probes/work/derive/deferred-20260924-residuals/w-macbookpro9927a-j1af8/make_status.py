#!/usr/bin/env python3
"""Write RECOVERY_STATUS.json for J:derive:deferred-20260924-residuals:a1 (first bounded pass over batch 15)."""
import hashlib
import json
import os
import subprocess

MAIN = "78db61c32a39234bab16034c57361bf0c418c0b1"
LANDED = "1cb2a082bfa4cebc01c0f61b4e366a6daa48a82d"
BATCH = "probes/work/deferred-science-20260924/batch-15.json"
REUSED = {
    "docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md":
        "072d6024923f05c00f5fd1e80e1dc3952a77c773b48886bd59b7be97adc28133",
    "docs/ACTUAL_BIRTH_ROTOR_ENERGY_HAS_AN_ALGEBRAIC_LOWER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-24.md":
        "7f6f2dbb4444f69dcc29c29b812e517074ebde65c4725317ccf2f0f2f4ea8d28",
    "scripts/mobile_rotor_exact_tail_control_20260924.py":
        "531700691e8bac82cd2a0b48b53b32eb4eff37fcf4ece12e178c3b1f118b147f",
}


def sha_rev(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True)
    return hashlib.sha256(r.stdout).hexdigest() if r.returncode == 0 else None


root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
batch = json.load(open(os.path.join(root, BATCH)))
batch_sha = hashlib.sha256(open(os.path.join(root, BATCH), "rb").read()).hexdigest()
reused = {p: {"expected": h, "landed": sha_rev(LANDED, p), "main": sha_rev(MAIN, p)} for p, h in REUSED.items()}
for p in reused:
    reused[p]["verified"] = reused[p]["landed"] == reused[p]["main"] == reused[p]["expected"]
manifest_checks = {}
for src in batch["sources"]:
    if str(src.get("pr")) in ("8957", "8958"):
        got = sha_rev(src["head"], src["path"])
        manifest_checks.setdefault(str(src["pr"]), []).append(got == src["sha256"])
status = {
    "task": "J:derive:deferred-20260924-residuals:a1",
    "worker": "w-macbookpro9927a-j1af8",
    "model": "claude-opus-5-5",
    "origin_main_sha": MAIN,
    "batch": {"path": BATCH, "sha256": batch_sha},
    "frozen_heads": {pr: batch["prs"][pr]["head"] for pr in ("8957", "8958", "8960")},
    "manifest_sha256_verified_at_frozen_heads": {pr: {"files": len(v), "all_match": all(v)}
                                                  for pr, v in manifest_checks.items()},
    "reused_landed_sources": reused,
    "dispositions": {
        "8960": {"disposition": "active-elsewhere / overlapping this worker's own prior units; not recovered here",
                 "evidence": ["internal-hop-energy-and-the-two-masses a1 (w-macbookpro90c72-jdb03, issue #8732), cited "
                              "by #8960 itself for the stress identification",
                              "bending-over-fall-at-strong-field (w-macbookpro9927a-j7735; w-jonathonsmac4f50-j3a05; "
                              "referee_w-macbookpro90c72-jb56c)",
                              "p-equals-q-for-compact-and-strong-bodies: no attempts (open)"],
                 "open_residuals": ["unsupported GR mass/stress identification (deferred by review)",
                                    "unproved lattice-error order (deferred by review)"]},
        "8957/8958": {"disposition": "recovered (this unit): the exact decay exponent of the actual-birth fast "
                                     "energy, partial",
                      "result": "dark half-period phases exactly 8, non-degenerate, input overlaps per kernel "
                                "dimension; exact exponent 5/2 conditional on no off-lattice dark phase"},
        "8950": "open (not inspected in this pass; review finding: strict whole-zone threshold, landed)",
        "8648": "historical planning graph (landed as supplied graph; no science residual taken)",
        "8033": "open (not inspected; landed with explicit connected endpoints)",
        "8968": "open (not inspected; landed with divergence-free unit fields hypothesis)"},
    "review_corrections_preserved": [
        "strong versus uniform decay kept explicit (#8957: ||V(tau)|| = 1 for every tau)",
        "lower bound versus exact exponent kept explicit (#8958); the exact exponent here is conditional",
        "joint compact-fast-time limit first; no fixed laboratory-time or physical selection conclusion"],
    "proved_or_checked": {
        "S1": "source invariants reproduced",
        "H1": "8 dark half-period phases, kernel dims 1,1,2,1,1,2,4,2",
        "H2": "full-rank pencils: non-degenerate second-order dissipation on every dark kernel",
        "H3": "input overlaps 1/12, 1/12, 1/6 per kernel dimension",
        "G1": "20 unit pivots, 52x4 residual, factored minor",
        "G2": "last-column branch gives only (-1,-1,1,1,-1)"},
    "assumed": ["#8957/#8958's premises as landed (fibre representation L2(T5; C96), the source's compact-fast-time "
                "reduction, the actual first-mark vectors)"],
    "first_unresolved_step": "off-lattice exclusion in the rank-deficient-block branch: common torus zeros of the "
                             "4x3 block's minors in the sub-cases z1 z3 = -1, z2^3 = z4^3 z5, z2^3 z5 = z4^3, "
                             "together with the remaining 48 residual rows",
    "remaining_ranked_source_groups": ["8960 lattice-error order (distinct from the stress identification)",
                                       "8950 endpoint classification beyond the landed threshold",
                                       "8968 sampler/thermodynamic statements", "8033"],
    "existing_task_log_links": {
        "internal-hop-energy-and-the-two-masses": "logs/probes/J:derive:internal-hop-energy-and-the-two-masses:a1/",
        "bending-over-fall-at-strong-field": "logs/probes/J:derive:bending-over-fall-at-strong-field:*",
    },
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RECOVERY_STATUS.json")
json.dump(status, open(out, "w"), indent=1)
print("wrote", out, "reused verified:", all(v["verified"] for v in reused.values()),
      "manifest:", status["manifest_sha256_verified_at_frozen_heads"])
