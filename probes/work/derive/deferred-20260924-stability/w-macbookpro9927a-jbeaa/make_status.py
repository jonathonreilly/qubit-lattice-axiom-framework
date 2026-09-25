#!/usr/bin/env python3
"""Generate RECOVERY_STATUS.json for J:derive:deferred-20260924-stability:a1 (worker w-macbookpro9927a-jbeaa).
Re-verifies the SHA256 of every batch-09 source of the four U9-R2 PRs against the manifest (git show <frozen head>:<path>),
records origin/main and the landed canonical notes, and ranks the remaining source groups.  Run from the repository root."""
import hashlib, json, subprocess, sys

HERE = "probes/work/derive/deferred-20260924-stability/w-macbookpro9927a-jbeaa"
BATCH = json.load(open("probes/work/deferred-science-20260924/batch-09.json"))
TARGET = ("8652", "8657", "8665", "8678")
USED = {  # sources read and used in this pass (path suffix -> role)
    "RESULTS_block88.md": "read: executed endpoint scan and thresholds (historical numbers only)",
    "CHECKER_block88_findings.md": "read: 'endpoint property executed, not proved'; log-rate corrigendum",
    "GOAL_block88.md": "read: question and boundaries (single-axis and traceless modes, linear order)",
    "supervisor_control_block88_two_instabilities.py": "read: definition of the single-axis response chi~(q) and the endpoint scan",
    "supervisor_control_block88_two_instabilities.out.txt": "read: ring values of chi~(q), used only as a float comparison",
    "RESULTS_block84.md": "read: alternation balance (landed T3 supersedes)",
    "CHECKER_block84_findings.md": "read: endpoint-crossing claims deferred by review",
    "GOAL_block84.md": "read: contract",
    "supervisor_control_block84_bond_rate_alternation.py": "read: float control (not reused)",
    "supervisor_control_block84_bond_rate_alternation.out.txt": "read: historical numbers (not reused)",
}
NOTES = {
    "84": "docs/ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "85": "docs/ADMISSIBILITY_RULE_THE_CROWD_UNDER_EXCLUSION_ALSO_GAINS_FROM_AN_ALTERNATION_OF_THE_BOND_RATES_ITS_GROUND_ENERGY_NEVER_RISES_THE_JAM_IS_BLIND_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "88": "docs/ADMISSIBILITY_RULE_THE_TWO_INSTABILITIES_OF_THE_UNIFORM_BOND_RATES_THE_ALTERNATION_BREAKS_TRANSLATION_BELOW_ALPHA_PLUS_2BETA_THE_ANISOTROPY_BREAKS_ROTATION_BELOW_BETA_ALONE_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "89": "docs/ADMISSIBILITY_RULE_THE_UNIT_OF_RATE_DECIDES_THE_ALTERNATIONS_THRESHOLDS_IN_LOG_RATES_AN_EXACT_MASS_A_CONVEXITY_TERM_AND_NO_GLOBAL_MINIMUM_UNDER_A_QUADRATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-23.md",
}


def git(*a):
    return subprocess.run(["git", *a], capture_output=True).stdout


def main():
    main_sha = git("rev-parse", "origin/main").decode().strip()
    landed = BATCH["prs"]["8665"]["landed_commit"]
    notes = {}
    for blk, path in NOTES.items():
        a, b = git("show", f"origin/main:{path}"), git("show", f"{landed}:{path}")
        notes[blk] = {"path": path, "sha256_origin_main": hashlib.sha256(a).hexdigest(),
                      "identical_to_landed_commit": a == b and len(a) > 0}
    groups, bad = [], 0
    for s in BATCH["sources"]:
        if str(s["pr"]) not in TARGET:
            continue
        blob = git("show", f"{s['head']}:{s['path']}")
        ok = hashlib.sha256(blob).hexdigest() == s["sha256"]
        bad += not ok
        leaf = s["path"].split("/")[-1]
        if leaf in USED and str(s["pr"]) in ("8665", "8652"):
            disp = "recovered-and-used: " + USED[leaf]
        elif s["category"] == "historical-evidence":
            disp = "historical: kept on its branch, not fresh evidence"
        elif s["category"] == "process-context":
            disp = "process-context: not used as evidence"
        else:
            disp = "open: not read in this pass (same-topic block file; landed note supersedes its claims)"
        groups.append({"pr": s["pr"], "head": s["head"], "path": s["path"], "sha256": s["sha256"], "sha256_verified": ok,
                       "category": s["category"], "content_group": s["content_group"], "disposition": disp})
    remaining = [
        {"rank": 1, "finding": "U9-R2 (rest)", "prs": [8665], "obligation":
         "unexamined directions: single-axis modulations at intermediate q. The frozen block 88 'endpoint property' (0/301 "
         "alphas, float) holds for all alpha >= 0 iff chi~(q) <= chi~(0) + (chi~(pi) - chi~(0))(1 - cos q)/2 on [0, pi] "
         "(chord lemma, ATTEMPT step 7), with chi~(q) = <sin^2(k1+q/2) G(sin k1, sin(k1+q); m)> (exact zone integral); "
         "prove the chord inequality or exhibit an interior q"},
        {"rank": 2, "finding": "U9-R2 (rest)", "prs": [8652, 8678], "obligation":
         "zero Hessian equality of the log-rate alternation (block 89 T2): the integrand -sqrt(S + 3 sinh^2 delta) is even in "
         "delta; its quartic coefficient involves <S^(-3/2)>, which diverges in 3D, so the equality case needs a "
         "non-analytic (delta^4 log) expansion"},
        {"rank": 3, "finding": "U9-R2 (rest)", "prs": [8657], "obligation": "crowd-threshold bounds (block 85): deferred by review; not inspected"},
        {"rank": 4, "finding": "U9-R3", "prs": [8660, 8662], "obligation": "wall spectra: parity-product compatibility, imbalanced-domain zero modes, six-ring spectral rule"},
        {"rank": 5, "finding": "U9-R1", "prs": [8626, 8628, 8632], "obligation": "gas/symmetry examples: reflection-positive parameter conditions, large-field gaps, corner zeros, reach-three strain"},
        {"rank": 6, "finding": "U9-R4/U9-R5", "prs": [8692, 8696, 8703, 8710], "obligation": "excluded update clause; stationary identities vs temporal memory; beta-zero and alias exceptions"},
    ]
    status = {
        "task": "J:derive:deferred-20260924-stability:a1", "worker": "w-macbookpro9927a-jbeaa", "model": "claude-opus-5-5",
        "batch": 9, "pass": "first bounded pass; not an exhaustion of batch 9",
        "origin_main_sha": main_sha, "landing_snapshot": "c288aa9cfeea8fd2256fe4b71a60c401d64f7ce6", "batch_landed_commit": landed,
        "frozen_heads": {n: BATCH["prs"][n]["head"] for n in TARGET},
        "canonical_notes": notes,
        "review_findings_touched": {
            "U9-R2": "worked: 'zero Hessian equality' of the traceless anisotropy in both supplied constraints (arithmetic mean, "
                     "block 88; mean log rate, block 89); 'unexamined directions' reduced (chord lemma) and left open",
            "U9-R6": "preserved: historical scans stay historical; the float window below is labelled numerical"},
        "review_demotions_preserved": [
            "no complete instability classification; two path Hessians do not classify all perturbations (block 88 N1)",
            "no physical transition, formation or dynamics is inferred from a path energy",
            "restricted linear-rate sufficiency (block 84 T3) is untouched; finite-grid cusps are not used"],
        "residual_worked": {
            "source": "block 88 T3 ('a zero anisotropy coefficient alone does not settle a minimum; higher orders can matter') and "
                      "block 89 T2/T3 ('at equality higher-order analysis is needed'); frozen PR8665 CHECKER item 5 and W3",
            "statement": "cubic coefficient of the sea energy along the traceless anisotropy path: (3/2)<sum_i u_i(u_j-u_k)^2/|s|^5> > 0 "
                         "(arithmetic mean) and -<(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5)> < 0 (mean log rate); consequences at "
                         "the quadratic thresholds",
            "status_in_this_pass": "exact formulas and signs; rigorous interval above chi_a/72 with a point below the uniform energy; "
                                   "float window for the path's global minimum",
            "first_failing_step": "none for the stated residual; the global window beta* ~ 0.02715 is float only",
            "disposition": "recovered and sharpened; the full-direction stability question stays open"},
        "related_work": {
            "the-anisotropic-state a1 (w-macbookpro90c72-j5081, same model family, refereed by grok-4.6 in "
            "logs/probes/J:confirm:J-derive-the-anisotropic-state-a1/)": "log-rate path: convexity, F''(0), runaway, walk; its "
            "executed E_sea'''(0) = -6.94 is reproduced here as the exact -2<(s1^3 + 9 s1 s2/2 + 81 s3/2)/|s|^5> = -6.9362",
            "the-record-gas-chessboard-threshold a2 (#9034), the-two-wall-level-rule-on-every-ring a2 (#8763), "
            "the-reach-three-coupling-beyond-first-order a3 (w-macbookpro90c72-j1638, no HIT)": "same worker; different "
            "questions (U9-R1/R3 topics); not reused"},
        "source_groups_inspected": groups,
        "sha256_failures": bad,
        "remaining_ranked_obligations": remaining,
    }
    json.dump(status, open(f"{HERE}/RECOVERY_STATUS.json", "w"), indent=1)
    print(f"{len(groups)} sources, sha256 failures {bad}; origin/main {main_sha[:12]}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
