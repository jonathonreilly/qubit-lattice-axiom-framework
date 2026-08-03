"""Cycle 875 independent check: an attempt to REFUTE the B-AXIS second-leg
discharge certificate.

The Cycle-875 primary is BLOCKLISTED.  It is read as text and AST only; none
of its code runs in this process and none of its helpers is imported.  Every
number this file checks is re-derived here by a DIFFERENT route than the
primary used (regex where it used AST, explicit loops where it used library
calls, the original git objects where it used its committed copies).

ATTACK SURFACE.  The primary makes four kinds of claim, and each is attacked:

  A1 QUOTE_TAMPER        the quoted premise and leg texts are checked against
                         the ORIGINAL git blobs, not the committed copies, so
                         a doctored copy that still hashes to a doctored pin
                         is caught.  Quotes are also checked for truncation
                         that would drop a scope qualifier.
  A2 PIN_FORGERY         every declared (commit, path, blob) triple is
                         resolved through git and cross-checked against the
                         bytes on disk in both directions.
  A3 OVERCLAIM           the discharge map is audited for statuses stronger
                         than their evidence, for a premise standing that
                         claims discharge while obligations are open, and for
                         claim-type drift away from SUPPORT.
  A4 HEADLINE_LAUNDERING the 869 across-key headline is a pair-clock figure.
                         The primary says so; this file verifies that the
                         OPEN obligation is priced to the larger full-corpus
                         residue and not quietly to the headline.
  A5 MASK_ABUSE          the primary compares a live 869 re-run to its cache
                         under two masks.  This file rebuilds that comparison
                         and feeds it a mutated stream to prove the masks
                         cannot swallow a substantive change.
  A6 FAMILY_INVENTION    the declared candidate family is re-extracted from
                         the pinned sources by regex and compared.
  A7 NONDETERMINISM      the primary is run twice and its stdout compared
                         under the same audited masks.

VERDICT.  Each attack returns CORROBORATED or REFUTED.  This file exits
non-zero if any attack REFUTES, or if any of its own controls fail.  It is
not a second opinion; it is an adversary that failed.
"""
from __future__ import annotations

import ast
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

PRIMARY = "scripts/frontier_cycle875_baxis_second_leg_certificate_2026_07_28.py"
PREMISE_DOC = "docs/ANOMALY_FORCES_TIME_THEOREM.md"
PRIMARY_869 = "scripts/frontier_cycle869_clock_relation_2026_07_28.py"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
EV = "outputs/cycle875_pinned_evidence"

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle875_baxis_second_leg_certificate_2026_07_28.py",
    "docs/ANOMALY_FORCES_TIME_THEOREM.md",
    "scripts/frontier_cycle869_clock_relation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
    "outputs/cycle875_pinned_evidence/arc_note_863_865.md",
    "outputs/cycle875_pinned_evidence/cache_863_865_arc_check.txt",
    "outputs/cycle875_pinned_evidence/cache_864_laws_in_record_time.txt",
    "outputs/cycle875_pinned_evidence/cache_865_offset_law.txt",
    "outputs/cycle875_pinned_evidence/cache_866_scaled_banks.txt",
    "outputs/cycle875_pinned_evidence/src_863_865_arc_check.py",
    "outputs/cycle875_pinned_evidence/src_866_scaled_banks.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

BLOCKLISTED_MODULES = (
    "frontier_cycle875_baxis_second_leg_certificate_2026_07_28",
    "frontier_cycle869_clock_relation_2026_07_28",
    "frontier_cycle866_scaled_banks_2026_07_28",
    "frontier_cycle863_865_arc_independent_check_2026_07_28",
)

STATIONS = 19
CORROBORATED = "CORROBORATED"
REFUTED = "REFUTED"

# Independently restated here, NOT read from the primary: the checker must be
# able to disagree about what the sources say.
EXPECTED_LEG_TEXT = (
    "(i) the landed temporal laws restate in record-time coordinates "
    "(certificates A/B here), and (ii) the axis admits no second record-clock"
)
SCOPE_QUALIFIERS = ("untested here and remains the open leg",
                    "needs the scaled-bank construction")
TIMING_FIELD = re.compile(
    r'"(runtime_seconds|elapsed_seconds|runtime|elapsed)":\s*-?[0-9]+(\.[0-9]+)?'
)
SELFSIZE_FIELD = re.compile(r'"(stdout_bytes)":\s*[0-9]+')


def compact(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def git_blob(payload: bytes) -> str:
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


def mask(text: str) -> str:
    text = TIMING_FIELD.sub(lambda m: f'"{m.group(1)}":T', text)
    return SELFSIZE_FIELD.sub(lambda m: f'"{m.group(1)}":S', text)


def git(*args) -> bytes | None:
    try:
        proc = subprocess.run(("git",) + args, capture_output=True,
                              cwd=str(ROOT), timeout=60)
    except (OSError, subprocess.SubprocessError):
        return None
    return proc.stdout if proc.returncode == 0 else None


def cache_stdout(text: str) -> str:
    head = "----- stdout -----\n"
    start = text.index(head) + len(head)
    return text[start:text.index("\n----- stderr -----", start)]


def cert_of(stdout: str, name: str):
    for line in stdout.splitlines():
        for prefix in (f"CERTIFICATE {name} PASS ", f"CERTIFICATE {name} FAIL ",
                       f"PASS {name} :: ", f"FAIL {name} :: "):
            if line.startswith(prefix):
                return json.loads(line[len(prefix):])
    return None


def run_primary():
    started = time.monotonic()
    proc = subprocess.run([sys.executable, str(ROOT / PRIMARY)],
                          capture_output=True, cwd=str(ROOT), timeout=900)
    return proc, round(time.monotonic() - started, 3)


class Unresolved:
    """Sentinel for an expression this evaluator declines to evaluate."""


def _eval(node, ns):
    """A deliberately small expression evaluator over the primary's AST.

    ast.literal_eval is not enough: the primary keys its tables by module
    constants and builds paths with f-strings, so a bare literal_eval silently
    returns None and every downstream check becomes a no-op that passes.  This
    evaluator resolves names and f-strings itself and NEVER executes code.
    """
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return ns.get(node.id, Unresolved)
    if isinstance(node, (ast.Tuple, ast.List)):
        items = [_eval(e, ns) for e in node.elts]
        if any(i is Unresolved for i in items):
            return Unresolved
        return tuple(items) if isinstance(node, ast.Tuple) else items
    if isinstance(node, ast.Dict):
        out = {}
        for k, v in zip(node.keys, node.values):
            key, val = _eval(k, ns), _eval(v, ns)
            if key is Unresolved or val is Unresolved:
                return Unresolved
            out[key] = val
        return out
    if isinstance(node, ast.JoinedStr):
        parts = []
        for piece in node.values:
            if isinstance(piece, ast.Constant):
                parts.append(str(piece.value))
            elif isinstance(piece, ast.FormattedValue):
                value = _eval(piece.value, ns)
                if value is Unresolved:
                    return Unresolved
                parts.append(str(value))
            else:
                return Unresolved
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Mult)):
        left, right = _eval(node.left, ns), _eval(node.right, ns)
        if left is Unresolved or right is Unresolved:
            return Unresolved
        return left + right if isinstance(node.op, ast.Add) else left * right
    return Unresolved


def module_namespace(tree):
    ns = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            value = _eval(node.value, ns)
            if value is Unresolved:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name):
                    ns[target.id] = value
    return ns


def primary_literal(ns, name):
    value = ns.get(name, Unresolved)
    return None if value is Unresolved else value


# ==================================================================== attacks
def a1_quote_tamper(ns, provenance):
    """Check every quote against the ORIGINAL git object, not the copy."""
    quotes = primary_literal(ns, "QUOTES")
    rows = []
    for label, path, text in quotes or ():
        local = (ROOT / path).read_bytes().decode()
        origin = None
        if path in provenance:
            commit, original_path, _blob = provenance[path]
            raw = git("cat-file", "blob", f"{commit}:{original_path}")
            origin = raw.decode() if raw is not None else None
        rows.append({
            "label": label,
            "source": path,
            "in_committed_copy": local.find(text) >= 0,
            "origin_reachable": origin is not None,
            "in_original_git_object": (origin.find(text) >= 0
                                       if origin is not None else None),
            "occurrences_in_source": local.count(text),
        })
    leg = next((r for r in rows if r["label"] == "LEG_STATEMENT_864D"), None)
    leg_text = next((t for label, _p, t in (quotes or ())
                     if label == "LEG_STATEMENT_864D"), "")
    truncation = {
        "expected_two_leg_core_present": EXPECTED_LEG_TEXT in leg_text,
        "scope_qualifier_retained": any(q in leg_text for q in SCOPE_QUALIFIERS),
        "quote_does_not_stop_before_leg_ii": "(ii)" in leg_text,
    }
    failures = [r["label"] for r in rows if not r["in_committed_copy"]
                or r["in_original_git_object"] is False]
    if not rows:
        failures.append("NO_QUOTES_EXTRACTED_FROM_PRIMARY")
    if len(rows) < 7:
        failures.append(f"ONLY_{len(rows)}_QUOTES_DECLARED")
    if not truncation["expected_two_leg_core_present"]:
        failures.append("LEG_STATEMENT_864D:CORE_TEXT_ABSENT")
    if not truncation["scope_qualifier_retained"]:
        failures.append("LEG_STATEMENT_864D:SCOPE_QUALIFIER_DROPPED")
    result = {
        "attack": "A1_QUOTE_TAMPER",
        "quotes_checked": len(rows),
        "rows": tuple(rows),
        "truncation_audit": truncation,
        "leg_quote_present": bool(leg and leg["in_committed_copy"]),
        "failures": failures,
    }
    result["verdict"] = REFUTED if failures else CORROBORATED
    return result


def a2_pin_forgery(ns):
    """Resolve every pin through git and cross-check the bytes on disk."""
    provenance = primary_literal(ns, "PINNED_PROVENANCE") or {}
    expected = primary_literal(ns, "EXPECTED_SHA256") or {}
    rows = []
    for path, (commit, original, blob) in provenance.items():
        raw = (ROOT / path).read_bytes()
        resolved = git("rev-parse", f"{commit}:{original}")
        resolved = resolved.decode().strip() if resolved is not None else None
        rows.append({
            "path": path,
            "declared_commit": commit,
            "declared_original_path": original,
            "declared_blob": blob,
            "git_resolved_blob": resolved,
            "declared_blob_matches_git": (resolved == blob
                                          if resolved else None),
            "disk_bytes_hash_to_declared_blob": git_blob(raw) == blob,
            "disk_sha256_matches_declared": (
                sha256(raw).hexdigest() == expected.get(path)),
        })
    live = []
    for path in ("docs/ANOMALY_FORCES_TIME_THEOREM.md", PRIMARY_869, CACHE_869):
        raw = (ROOT / path).read_bytes()
        live.append({
            "path": path,
            "sha256": sha256(raw).hexdigest(),
            "matches_declared": sha256(raw).hexdigest() == expected.get(path),
        })
    failures = [r["path"] for r in rows
                if not r["disk_bytes_hash_to_declared_blob"]
                or r["declared_blob_matches_git"] is False
                or not r["disk_sha256_matches_declared"]]
    failures += [r["path"] for r in live if not r["matches_declared"]]
    if not rows:
        failures.append("NO_PINNED_PROVENANCE_EXTRACTED_FROM_PRIMARY")
    if not expected:
        failures.append("NO_EXPECTED_SHA256_TABLE_EXTRACTED_FROM_PRIMARY")
    result = {
        "attack": "A2_PIN_FORGERY",
        "pinned_rows": tuple(rows),
        "worktree_rows": tuple(live),
        "note": ("A pin is only worth the object it names.  Each triple is "
                 "resolved by git AND recomputed from the bytes, so a copy "
                 "that was edited to match a doctored pin still fails the "
                 "git-side resolution."),
        "failures": failures,
    }
    result["verdict"] = REFUTED if failures else CORROBORATED
    return result, provenance


def a3_overclaim(dmap, summary):
    """Audit the discharge map for statuses stronger than their evidence."""
    obligations = dmap["obligations"]
    discharged = [o for o in obligations
                  if o["status"] == "DISCHARGED_AT_SCOPE"]
    open_rows = [o for o in obligations
                 if o["status"] != "DISCHARGED_AT_SCOPE"]
    problems = []

    # Every discharged row must name a scope; an unscoped discharge is a
    # promotion in disguise.
    for row in discharged:
        if not row.get("scope") or row["scope"].strip().lower() in ("", "all"):
            problems.append(f"{row['id']}:DISCHARGED_WITHOUT_SCOPE")
        if not row.get("artifact_sha256"):
            problems.append(f"{row['id']}:DISCHARGED_WITHOUT_ARTIFACT_SHA")

    # The standing must not claim discharge while any obligation is open.
    standing = dmap["premise_standing"]
    if open_rows and "NOT_DISCHARGED" not in standing:
        problems.append("STANDING_CLAIMS_DISCHARGE_WITH_OPEN_OBLIGATIONS")
    if not open_rows and "NOT_DISCHARGED" in standing:
        problems.append("STANDING_CLAIMS_OPEN_WITH_NO_OPEN_OBLIGATIONS")

    # The claim type must stay SUPPORT and the premise must not be promoted.
    if summary.get("claim_type") != "SUPPORT":
        problems.append("CLAIM_TYPE_DRIFTED_FROM_SUPPORT")
    forbidden = ("B-AXIS is derived", "premise is discharged",
                 "B_AXIS_DISCHARGED", "no longer a premise")
    text = compact(dmap)
    for phrase in forbidden:
        if phrase in text:
            problems.append(f"PROMOTION_LANGUAGE:{phrase}")

    # Family closure must be carried and must never be discharged.
    closure = next((o for o in obligations if o["id"] == "O10_FAMILY_CLOSURE"),
                   None)
    if closure is None:
        problems.append("FAMILY_CLOSURE_OBLIGATION_MISSING")
    elif closure["status"] != "PERMANENTLY_OPEN":
        problems.append("FAMILY_CLOSURE_NOT_PERMANENTLY_OPEN")

    # The B=4 leg must be present and open.
    b4 = next((o for o in obligations if "B4" in o["id"]), None)
    if b4 is None:
        problems.append("B4_OBLIGATION_MISSING")
    elif b4["status"] == "DISCHARGED_AT_SCOPE":
        problems.append("B4_OBLIGATION_CLAIMED_DISCHARGED")

    result = {
        "attack": "A3_OVERCLAIM",
        "obligation_count": len(obligations),
        "discharged": [o["id"] for o in discharged],
        "open": [o["id"] for o in open_rows],
        "standing": standing,
        "problems": problems,
    }
    result["verdict"] = REFUTED if problems else CORROBORATED
    return result


def a4_headline_laundering(dmap, witnesses):
    """The 869 across-key headline is pair-clock only.  Verify the pricing."""
    across = cert_of(cache_stdout((ROOT / CACHE_869).read_text()),
                     "F_ACROSS_KEYS")
    verdict = cert_of(cache_stdout((ROOT / CACHE_869).read_text()),
                      "G_RELATION_VERDICT")
    # Independent re-derivation: explicit loops, no comprehension over the
    # primary's grouping.
    pair_edges = bank_edges = 0
    pair_outside = bank_outside = 0
    full_nonzero = full_zero = 0
    for label, payload in across["pair_clocks"].items():
        pair_edges += payload["F1_edges_to_class_representative"]
        pair_outside += (payload["sounding_keys"]
                         - payload["keys_in_nontrivial_F1_class"])
    for label, payload in across["bank_clocks"].items():
        bank_edges += payload["F1_edges_to_class_representative"]
        bank_outside += (payload["sounding_keys"]
                         - payload["keys_in_nontrivial_F1_class"])
    for family in ("bank_clocks", "pair_clocks"):
        for payload in across[family].values():
            full_nonzero += payload["F1_edges_with_nonzero_offset"]
            full_zero += payload["F1_edges_with_zero_offset_identical_cadences"]
    full_edges = pair_edges + bank_edges
    full_outside = pair_outside + bank_outside

    o7 = next(o for o in dmap["obligations"] if o["id"] == "O7_CROSS_KEY_UNCOVERED_KEYS")
    headline_outside = verdict["across_key_keys_outside_any_nontrivial_F1_class"]
    problems = []
    if verdict["across_key_F1_edges"] != pair_edges:
        problems.append("HEADLINE_EDGES_NOT_PAIR_CLOCK_TOTAL")
    if headline_outside != pair_outside:
        problems.append("HEADLINE_OUTSIDE_NOT_PAIR_CLOCK_TOTAL")
    if str(full_outside) not in o7["evidence"]:
        problems.append("O7_NOT_PRICED_TO_FULL_CORPUS_RESIDUE")
    leading = re.match(r"\s*([0-9]+)", o7["evidence"])
    if not leading or int(leading.group(1)) != full_outside:
        problems.append("O7_LEADING_FIGURE_IS_NOT_THE_FULL_CORPUS_RESIDUE")
    if witnesses["across_key_full_corpus"]["keys_outside_any_nontrivial_F1_class"] != full_outside:
        problems.append("PRIMARY_FULL_CORPUS_RESIDUE_DISAGREES")
    if witnesses["across_key_full_corpus"]["F1_edges"] != full_edges:
        problems.append("PRIMARY_FULL_CORPUS_EDGES_DISAGREE")
    if full_zero != 0 or full_nonzero != full_edges:
        problems.append("NOT_EVERY_F1_EDGE_MOVES_THE_ORIGIN")
    result = {
        "attack": "A4_HEADLINE_LAUNDERING",
        "headline_F1_edges": verdict["across_key_F1_edges"],
        "headline_keys_outside": headline_outside,
        "recomputed_pair_clock_edges": pair_edges,
        "recomputed_pair_clock_outside": pair_outside,
        "recomputed_bank_clock_edges": bank_edges,
        "recomputed_bank_clock_outside": bank_outside,
        "recomputed_full_corpus_edges": full_edges,
        "recomputed_full_corpus_outside": full_outside,
        "full_corpus_zero_offset_F1_edges": full_zero,
        "finding": (
            f"The 869 G-certificate headline reports {verdict['across_key_F1_edges']} "
            f"across-key F1 edges and {headline_outside} uncovered keys.  Both "
            f"are PAIR-CLOCK totals.  Over the full corpus the figures are "
            f"{full_edges} edges and {full_outside} uncovered keys.  Every one "
            f"of the {full_edges} edges carries a nonzero offset, so the "
            f"single-time reading survives; the uncovered residue does not "
            f"shrink to the headline."
        ),
        "problems": problems,
    }
    result["verdict"] = REFUTED if problems else CORROBORATED
    return result


def a5_mask_abuse(live_stdout):
    """Prove the primary's masks cannot swallow a substantive change."""
    pinned = cache_stdout((ROOT / CACHE_869).read_text())
    proc = subprocess.run([sys.executable, str(ROOT / PRIMARY_869)],
                          capture_output=True, cwd=str(ROOT), timeout=600)
    fresh = proc.stdout.decode()
    honest_pass = mask(fresh) == mask(pinned)

    # Mutate a substantive number and confirm the masked comparison rejects it.
    mutations = []
    for target, replacement in (
        ('"across_key_F1_edges":632', '"across_key_F1_edges":633'),
        ('"substantive_pairs_of_clocks":480', '"substantive_pairs_of_clocks":481'),
        ('"every_nondegenerate_period_is_whole_orbits":true',
         '"every_nondegenerate_period_is_whole_orbits":false'),
    ):
        if target not in pinned:
            mutations.append({"target": target, "present": False,
                              "rejected_by_mask": None})
            continue
        mutated = pinned.replace(target, replacement, 1)
        mutations.append({
            "target": target, "present": True,
            "rejected_by_mask": mask(mutated) != mask(pinned),
        })
    # And confirm a pure wall-clock change IS absorbed (the mask must not be
    # so tight that it fails for the wrong reason).
    timing_only = TIMING_FIELD.sub(lambda m: f'"{m.group(1)}":0.001', pinned)
    problems = []
    if not honest_pass:
        problems.append("HONEST_RERUN_NOT_MASK_EQUAL")
    if not all(row["rejected_by_mask"] for row in mutations
               if row["present"]):
        problems.append("MASK_SWALLOWED_A_SUBSTANTIVE_MUTATION")
    if mask(timing_only) != mask(pinned):
        problems.append("MASK_FAILS_ON_PURE_TIMING_DRIFT")
    result = {
        "attack": "A5_MASK_ABUSE",
        "honest_rerun_mask_equal": honest_pass,
        "rerun_exit_code": proc.returncode,
        "mutations": tuple(mutations),
        "pure_timing_drift_absorbed": mask(timing_only) == mask(pinned),
        "note": ("The masks cover wall-clock fields and the runner's own "
                 "stdout_bytes self-report only.  Three substantive mutations "
                 "are injected and must all survive the mask as differences."),
        "problems": problems,
    }
    result["verdict"] = REFUTED if problems else CORROBORATED
    return result


def a6_family_invention(family):
    """Re-extract the declared family from the pinned sources by regex."""
    arc_src = (ROOT / f"{EV}/src_863_865_arc_check.py").read_text()
    src869 = (ROOT / PRIMARY_869).read_text()
    src866 = (ROOT / f"{EV}/src_866_scaled_banks.py").read_text()

    # 865 pair pool, by regex over the source block, then C(n,2) by loop.
    block = re.search(r"pair_pool\s*=\s*\[(.*?)\]", arc_src, re.S)
    pool = re.findall(r'"([a-z0-9_]+)"', block.group(1)) if block else []
    pairs = 0
    for i in range(len(pool)):
        for _j in range(i + 1, len(pool)):
            pairs += 1

    # 869 family member codes, by regex over the FAMILY block.
    fblock = re.search(r"FAMILY\s*=\s*\((.*?)\n\)\n", src869, re.S)
    found = re.findall(r'"(F[0-9][A-Z]{0,2})\s+([A-Z][A-Z_]{4,})',
                       fblock.group(1)) if fblock else []
    members = []
    for code, _label in found:
        if code not in members:
            members.append(code)

    # 866 bank counts, by regex.
    bc = re.search(r"BANK_COUNTS\s*=\s*\(([0-9,\s]+)\)", src866)
    bank_counts = [int(x) for x in re.findall(r"[0-9]+", bc.group(1))] if bc else []

    f865 = family["candidate_family_865_predictors"]
    f866 = family["candidate_family_866_sync_cadences"]
    f869 = family["relation_family_869_clock_dictionary"]
    problems = []
    if f865["pairs_claimed"] != pairs:
        problems.append("865_PAIR_COUNT_DISAGREES")
    if f865["pair_pool_size_from_source"] != len(pool):
        problems.append("865_PAIR_POOL_SIZE_DISAGREES")
    if sorted(f869["F_members"]) != sorted(members):
        problems.append("869_FAMILY_MEMBERS_DISAGREE")
    if f866["bank_counts_from_source"] != bank_counts:
        problems.append("866_BANK_COUNTS_DISAGREE")
    if f865["singles_claimed"] != 29 or pairs != 28:
        problems.append("865_FAMILY_NOT_THE_DECLARED_29_PLUS_28")
    result = {
        "attack": "A6_FAMILY_INVENTION",
        "regex_pair_pool": pool,
        "regex_pair_count_C_n_2": pairs,
        "regex_869_family_members": members,
        "regex_866_bank_counts": bank_counts,
        "primary_865_singles": f865["singles_claimed"],
        "primary_865_pairs": f865["pairs_claimed"],
        "primary_869_members": f869["F_members"],
        "problems": problems,
    }
    result["verdict"] = REFUTED if problems else CORROBORATED
    return result


# The primary's E_LIVE_REDERIVATION certificate re-runs another runner and
# discloses that run's raw hash and its wall-clock accounting.  Those fields
# CANNOT be stable, so they are excised by name and the two runs' certificates
# are compared on every remaining key.  Nothing else in the primary's stdout
# is permitted to move.
LIVE_RUN_VARYING = (
    "elapsed_seconds", "live_stdout_sha256", "raw_differing_lines",
    "differing_lines_explained_by_mask", "timing_length_delta",
    "raw_length_delta", "selfsize_delta",
)


def a7_nondeterminism(first_stdout):
    proc, elapsed = run_primary()
    second = proc.stdout.decode()
    problems = []
    if proc.returncode != 0:
        problems.append("SECOND_RUN_NONZERO_EXIT")

    first_lines = mask(first_stdout).splitlines()
    second_lines = mask(second).splitlines()
    if len(first_lines) != len(second_lines):
        problems.append("STDOUT_LINE_COUNT_MOVED")
    differing = [i for i, (a, b) in enumerate(zip(first_lines, second_lines))
                 if a != b]
    live_line = next((i for i, line in enumerate(first_lines)
                      if line.startswith("CERTIFICATE E_LIVE_REDERIVATION")), -1)
    unexpected = [i for i in differing if i != live_line]
    if unexpected:
        problems.append("A_LINE_OTHER_THAN_E_LIVE_REDERIVATION_MOVED")

    a = cert_of(first_stdout, "E_LIVE_REDERIVATION") or {}
    b = cert_of(second, "E_LIVE_REDERIVATION") or {}
    stable_keys = sorted(set(a) | set(b) - set(LIVE_RUN_VARYING))
    stable_keys = [k for k in stable_keys if k not in LIVE_RUN_VARYING]
    disagreeing = [k for k in stable_keys if a.get(k) != b.get(k)]
    if disagreeing:
        problems.append("E_LIVE_REDERIVATION_STABLE_FIELD_MOVED")
    for key in ("pass", "masked_identical", "line_counts_equal",
                "unexplained_differing_lines", "pinned_masked_sha256"):
        if key not in stable_keys:
            problems.append(f"LOAD_BEARING_FIELD_EXCUSED:{key}")

    result = {
        "attack": "A7_NONDETERMINISM",
        "second_run_exit_code": proc.returncode,
        "second_run_seconds": elapsed,
        "masked_differing_lines": differing,
        "e_live_rederivation_line_index": live_line,
        "unexpected_moving_lines": unexpected,
        "declared_run_varying_fields": list(LIVE_RUN_VARYING),
        "stable_fields_compared": stable_keys,
        "stable_fields_disagreeing": disagreeing,
        "note": ("Only the live-rerun certificate may move, and only in its "
                 "declared run-varying fields.  Its verdict, its masked "
                 "hashes and its unexplained-difference list are all held "
                 "stable and compared."),
        "problems": problems,
    }
    result["verdict"] = REFUTED if problems else CORROBORATED
    return result


def b_leg_witnesses():
    """One cheap witness per leg, re-derived here from first principles."""
    c864 = (ROOT / f"{EV}/cache_864_laws_in_record_time.txt").read_text()
    c869 = cache_stdout((ROOT / CACHE_869).read_text())
    c866 = (ROOT / f"{EV}/cache_866_scaled_banks.txt").read_text()
    arc = (ROOT / f"{EV}/cache_863_865_arc_check.txt").read_text()

    # LEG (i): 864's own summary, re-parsed, and its D-certificate self-report.
    summary864 = json.loads(
        re.search(r"^SUMMARY_JSON (.*)$", cache_stdout(c864), re.M).group(1))
    d864 = cert_of(cache_stdout(c864), "D_B_AXIS_CONTACT")
    leg_i = {
        "verdict_A": summary864["verdict_A"],
        "verdict_B": summary864["verdict_B"],
        "864_D_pass": d864["pass"],
        "864_D_names_leg_ii_as_untested": "untested here" in d864["discharge_condition"],
        "reading": ("leg (i)'s own evidence carries verdict_B=MIXED, so the "
                    "(i) leg is itself scoped, not clean"),
    }

    # LEG (ii) witness 1: the single tick-moving within-key dictionary is a
    # whole-orbit lag.  Re-derived by long division, not by modulo library use.
    d = cert_of(c869, "D_WITHIN_KEY_PAIR_OF_PAIRS")
    hist = d["witness_parameter_histogram"]
    moving = {k: v for k, v in hist.items() if k.startswith("F3:")
              and k.split("d=")[1] != "0"}
    orbits = {}
    for k in moving:
        lag = abs(int(k.split("d=")[1]))
        q, r = divmod(lag, STATIONS)
        orbits[k] = {"lag": lag, "orbits": q, "remainder": r}

    # LEG (ii) witness 2: 866's pair-cadence signature counts, recomputed by
    # tuple identity rather than json serialization.
    sig = {}
    for B in (3, 4):
        payload = json.loads(
            c866.split(f"CERTIFICATE B{B}_RESULTS PASS ")[1].splitlines()[0])
        gaps = payload["second_clock"]["pair_dominant_gaps"]
        seen = []
        for value in gaps.values():
            key = tuple(tuple(pair) for pair in value)
            if key not in seen:
                seen.append(key)
        sig[str(B)] = {
            "pairs": len(gaps), "distinct_signatures": len(seen),
            "claimed": payload["second_clock"]["distinct_pair_cadence_signatures"],
            "birth_datum_record_native":
                payload["birth_datum"]["native_pattern_functional"],
        }

    # LEG (ii) witness 3: the 865 hunt selected nothing at the 29+28 family.
    hunt = cert_of(cache_stdout(arc), "THE_INTRINSIC_PREDICTOR_HUNT")
    leg_ii = {
        "tick_moving_within_key_dictionaries": orbits,
        "all_tick_moving_lags_are_whole_orbits":
            all(v["remainder"] == 0 for v in orbits.values()),
        "866_pair_cadence_signatures": sig,
        "866_signature_counts_agree":
            all(v["distinct_signatures"] == v["claimed"] for v in sig.values()),
        "865_selected_predictor": hunt["selected_predictor"],
        "865_verdict": hunt["verdict"],
        "reading": (
            "866 finds a DISTINCT dominant-gap signature for every bank pair "
            "at both B=3 (3/3) and B=4 (6/6).  That is signature distinctness, "
            "not clock identity: it neither supplies nor denies a second "
            "clock, and it is the only B=4 evidence that exists."
        ),
    }
    problems = []
    if not leg_ii["all_tick_moving_lags_are_whole_orbits"]:
        problems.append("TICK_MOVING_LAG_NOT_WHOLE_ORBITS")
    if not leg_ii["866_signature_counts_agree"]:
        problems.append("866_SIGNATURE_COUNTS_DISAGREE")
    if not leg_i["864_D_names_leg_ii_as_untested"]:
        problems.append("864_D_DOES_NOT_NAME_LEG_II_UNTESTED")
    result = {
        "check": "B_LEG_WITNESSES",
        "leg_i": leg_i,
        "leg_ii": leg_ii,
        "problems": problems,
    }
    result["pass"] = not problems
    return result


def controls(started):
    rows = []
    for path in AUDIT_INPUT_PATHS:
        raw = (ROOT / path).read_bytes()
        rows.append({
            "path": path,
            "exists": (ROOT / path).is_file(),
            "worktree_relative": not Path(path).is_absolute(),
            "sha256": sha256(raw).hexdigest(),
            "git_blob": git_blob(raw),
            "access": ("PRIMARY_TEXT_AST_ONLY_BLOCKLISTED" if path == PRIMARY
                       else "READ_ONLY_EVIDENCE"),
        })
    runtime = round(time.monotonic() - started, 3)
    result = {
        "check": "CONTROLS",
        "inputs": tuple(rows),
        "declared_input_paths_are_literal": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklist_violations": [n for n in BLOCKLISTED_MODULES
                                 if n in sys.modules],
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_budget": runtime < AUDIT_TIMEOUT_SEC,
    }
    result["pass"] = bool(
        all(r["exists"] and r["worktree_relative"] for r in rows)
        and result["declared_input_paths_are_literal"]
        and not result["blocklist_violations"]
        and result["runtime_under_budget"]
    )
    return result


def main() -> int:
    started = time.monotonic()
    tree = ast.parse((ROOT / PRIMARY).read_bytes(), filename=PRIMARY)

    proc, first_seconds = run_primary()
    first = proc.stdout.decode()
    if proc.returncode != 0 and not first:
        raise AssertionError(("primary produced no stdout", proc.returncode))
    summary = json.loads(
        re.search(r"^SUMMARY_JSON (.*)$", first, re.M).group(1))
    dmap = cert_of(first, "F_DISCHARGE_MAP")
    witnesses = cert_of(first, "D_WITNESS_REDERIVATION")
    family = cert_of(first, "B_FAMILY_DECLARATION")

    ns = module_namespace(tree)
    pins, provenance = a2_pin_forgery(ns)
    attacks = {
        "A1_QUOTE_TAMPER": a1_quote_tamper(ns, provenance),
        "A2_PIN_FORGERY": pins,
        "A3_OVERCLAIM": a3_overclaim(dmap, summary),
        "A4_HEADLINE_LAUNDERING": a4_headline_laundering(dmap, witnesses),
        "A5_MASK_ABUSE": a5_mask_abuse(first),
        "A6_FAMILY_INVENTION": a6_family_invention(family),
        "A7_NONDETERMINISM": a7_nondeterminism(first),
    }
    legs = b_leg_witnesses()
    ctl = controls(started)

    refutations = [name for name, row in attacks.items()
                   if row["verdict"] == REFUTED]
    checks = {name: row["verdict"] == CORROBORATED
              for name, row in attacks.items()}
    checks["B_LEG_WITNESSES"] = legs["pass"]
    checks["CONTROLS"] = ctl["pass"]
    checks["PRIMARY_EXIT_ZERO"] = proc.returncode == 0

    findings = [
        attacks["A4_HEADLINE_LAUNDERING"]["finding"],
        legs["leg_ii"]["reading"],
        legs["leg_i"]["reading"],
        (f"The certificate leaves {len(dmap['open_obligations'])} obligations "
         f"open ({', '.join(dmap['open_obligations'])}) and reports standing "
         f"{dmap['premise_standing']}.  This checker found no basis to move "
         f"any of them, and no attempt to move them was made by the primary."),
    ]
    out_summary = {
        "cycle": 875,
        "role": "INDEPENDENT_CHECK_SPECD_TO_REFUTE",
        "checks": checks,
        "refutations": refutations,
        "primary_summary_pass": summary["pass"],
        "primary_standing": summary["premise_standing"],
        "primary_first_run_seconds": first_seconds,
        "findings": findings,
        "runtime_seconds": ctl["runtime_seconds"],
        "pass": all(checks.values()),
    }

    lines = ["CYCLE875_BAXIS_INDEPENDENT_CHECK",
             "PRIMARY_IS_BLOCKLISTED_TEXT_AND_AST_ONLY"]
    for name in ("A1_QUOTE_TAMPER", "A2_PIN_FORGERY", "A3_OVERCLAIM",
                 "A4_HEADLINE_LAUNDERING", "A5_MASK_ABUSE",
                 "A6_FAMILY_INVENTION", "A7_NONDETERMINISM"):
        lines.append(f"ATTACK {name} {attacks[name]['verdict']} "
                     + compact(attacks[name]))
    lines.append("CHECK B_LEG_WITNESSES "
                 + ("PASS " if legs["pass"] else "FAIL ") + compact(legs))
    lines.append("CHECK CONTROLS " + ("PASS " if ctl["pass"] else "FAIL ")
                 + compact(ctl))
    lines.append("SUMMARY_JSON " + compact(out_summary))
    lines.append("CYCLE875_BAXIS_INDEPENDENT_CHECK_"
                 + ("PASS" if out_summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if out_summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
