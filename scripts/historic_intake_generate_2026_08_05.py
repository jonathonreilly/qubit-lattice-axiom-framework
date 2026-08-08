#!/usr/bin/env python3
"""Historic-science intake wrapper generator (2026-08-05 triage, both parts).

Merged, deterministic regeneration of the 781 historic-intake objects
(780 ordinary wrappers + 1 Octopus-era registry), the hazards memo, the two
intake manifests and the two intake indexes, plus the byte-exact archive of
every pinned original under archive_unlanded/historic_intake_originals/.

This is the reproducible generator for PR #6018 after review-loop iteration 1
(Sol, 2026-08-08, FIX_THEN_PROCEED). It merges the two original assembly
scripts (part 1: march/recovery/branch01-08 + octopus; part 2: branch09 +
packsci01-05) and applies the review fixes:

  F1  every wrapper header carries a canonical `Claim type:` the live audit
      pipeline recognizes (positive_theorem | bounded_theorem | no_go |
      open_gate | decoration | meta), mapped deterministically from the
      extraction's historic taxonomy; the original historic_<x> string is
      preserved inside the audit-fields yaml as `historic_claim_class`.
  F2  the pinned original of every wrapper is fetched by ref:path,
      sha256-verified against the shipped manifest pin (fail-closed), and
      archived byte-exact under archive_unlanded/historic_intake_originals/;
      each wrapper's Provenance section links to its archived original.
  F3/F6 the "Why pulled" section is retitled "(supervisor triage decision of
      2026-08-05, provenance not authority)" and carries a fixed disclaimer
      sentence; decision reasons themselves are untouched (their sha256 is
      re-verified against the manifests).
  F4  historic runner names are rendered as inert code text ("historic runner
      (unpinned, not in this packet):", extension split off as "(.py)") so the
      citation-graph runner extractor cannot bind them to same-named files in
      the current tree; no markdown link is emitted for them.
  F5  attach/cross references that name another PULLED wrapper are rendered as
      relative markdown links to that wrapper file; references to non-pulled
      items stay plain text.
  F7  the Octopus-era registry keeps ONE note, typed `meta`; its evidence base
      (octopus_era.jsonl + octopus_era_claims.md) is archived byte-exact and
      linked from the note.
  F8  the hazards memo gains a header block (Claim type: meta; explicit
      "routing guidance, non-evidentiary" status line); its body is unchanged.
  F9/F10/F11 the three affected packsci01 wrappers (idx 10259, 10256, 10254)
      gain a "## Review flags (review-loop 2026-08-08)" section quoting the
      findings in compressed form; the pinned originals/runners are immutable
      history and the wrapper claims stay registration-only.
  F13 wrapper H1 titles containing bare route/axiom codes gain an explicit
      subject line under the title (mechanical; codes already expanded by a
      parenthetical in the title are left alone).

Inputs (frozen, read-only): the 2026-08-05 triage decision/extraction/manifest
JSONL under TRIAGE, and the shared git object store reachable from CENSUS.
The shipped intake manifests are treated as the pin authority: regeneration
FAILS if any re-fetched ref/blob/sha256/filename/reason-hash differs from the
shipped manifest row, so pins can never drift silently.

Usage: python3 scripts/historic_intake_generate_2026_08_05.py [check|build]
"check" performs every fetch, verification and render without writing.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

TRIAGE = "/Users/jonBridger/Toy Physics/.claude/worktrees/c5-census-full/triage_2026-08-05"
CENSUS = "/Users/jonBridger/Toy Physics/.claude/worktrees/c5-census-full"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "docs/historic_intake")
ARCH = os.path.join(REPO, "archive_unlanded/historic_intake_originals")
ARCH_REL_FROM_WRAPPER = "../../archive_unlanded/historic_intake_originals"

# (stratum, decision files, extracted file, triage manifest, part)
STRATA = [
    ("march", ["march_decisions.jsonl"], "march.jsonl", "march.json", 1),
    ("recovery", ["recovery_decisions.jsonl"], "recovery.jsonl", "recovery.json", 1),
    ("branch01", ["branch01_decisions_part1.jsonl", "branch01_decisions_part2.jsonl", "branch01_decisions_part3.jsonl"], "branch01.jsonl", "branch01.json", 1),
    ("branch02", ["branch02_decisions_part1.jsonl", "branch02_decisions_part2.jsonl", "branch02_decisions_part3.jsonl"], "branch02.jsonl", "branch02.json", 1),
    ("branch03", ["branch03_decisions.jsonl"], "branch03.jsonl", "branch03.json", 1),
    ("branch04", ["branch04_decisions.jsonl"], "branch04.jsonl", "branch04.json", 1),
    ("branch05", ["branch05_decisions.jsonl"], "branch05.jsonl", "branch05.json", 1),
    ("branch06", ["branch06_decisions.jsonl"], "branch06.jsonl", "branch06.json", 1),
    ("branch07", ["branch07_decisions.jsonl"], "branch07.jsonl", "branch07.json", 1),
    ("branch08", ["branch08_decisions.jsonl"], "branch08.jsonl", "branch08.json", 1),
    ("branch09", ["branch09_decisions.jsonl"], "branch09.jsonl", "branch09.json", 2),
    ("packsci01", ["packsci01_decisions.jsonl"], "packsci01.jsonl", "packsci01.json", 2),
    ("packsci02", ["packsci02_decisions.jsonl"], "packsci02.jsonl", "packsci02.json", 2),
    ("packsci03", ["packsci03_decisions.jsonl"], "packsci03.jsonl", "packsci03.json", 2),
    ("packsci04", ["packsci04_decisions.jsonl"], "packsci04.jsonl", "packsci04.json", 2),
    ("packsci05", ["packsci05_decisions.jsonl"], "packsci05.jsonl", "packsci05.json", 2),
]

STATUS = """Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status."""

WHY_PULLED_HEADER = "## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)"
WHY_PULLED_DISCLAIMER = ("The reasons below are the supervisor's selection rationale; they carry no "
                         "claim status and are not evidence about the original's validity.")

# ---------------------------------------------------------------------------
# F1 — canonical claim typing.
#
# The live pipeline (docs/audit/scripts/build_citation_graph.py CLAIM_TYPES,
# docs/audit/README.md "Claim typing at authoring time") recognizes exactly:
# positive_theorem, bounded_theorem, no_go, open_gate, decoration, meta.
# Every historic_<x> taxonomy value maps deterministically to the nearest
# recognized class; the historic string is preserved as historic_claim_class
# in the audit-fields yaml, and the auditor always owns the final value.
#
# Mapping principles (documented for review):
# - registries/ledgers/route lists-tables-maps/logs/status notes/scoreboards/
#   checkpoints/process-governance-audit-review records -> meta (navigational
#   or record-about-claims; carries no claim a dependent should consume).
# - substantive status CERTIFICATES (claim_status_certificate etc.) -> NOT
#   meta: they certify era claim states a dependent could consume as evidence
#   and must stay auditable -> bounded_theorem.
# - "bounded" anywhere -> bounded_theorem (checked before no_go so mixed
#   "bounded theorem plus scoped no-go" objects stay bounded).
# - no_go / negative / refutation / impossibility -> no_go.
# - open_gate / conjecture / proposal / brainstorm / recommendation /
#   research-target identification -> open_gate.
# - explicit positive_theorem / retained / unconditional -> positive_theorem.
# - everything else substantive (theorem/analysis/measurement/correction/
#   retraction/erratum/support/closure/derived/prediction/partial/exercise)
#   -> bounded_theorem: an era-scoped result awaiting audit (matches the
#   review guidance historic_theorem -> bounded_theorem; never blanket
#   positive_theorem).
CANONICAL_CLAIM_TYPES = {"positive_theorem", "bounded_theorem", "no_go", "open_gate", "decoration", "meta"}

CLAIM_TYPE_OVERRIDES = {
    # record-about-claims with a no_go/positive token that would mis-route
    "historic_authority_surface": "meta",
    "historic_no_go_chain_with_an_audit_failure_record": "no_go",
    "historic_retained_positive_structural_support_theorem_responding_to_a_codex_review": "positive_theorem",
    # substantive certificates and measurements that must stay auditable
    "historic_claim_status_certificate": "bounded_theorem",
    "historic_status_certificate": "bounded_theorem",
    "historic_registry_integrity_measurement": "bounded_theorem",
    # primary object is the exact/counting theorem, negative token is context
    "historic_exact_combinatorial_theorem_and_next_derivation_program_after_the_constant_lift_no_go": "bounded_theorem",
    "historic_exact_beyond_retained_stack_source_principle_theorem": "bounded_theorem",
    "historic_science_only_direct_counting_theorem_plus_sharp_retained_residual": "bounded_theorem",
    "historic_science_only_classification_theorem_sharp_no_go_on_same_surface_boundary_vacuum_references": "bounded_theorem",
    "historic_gate": "open_gate",
    "historic_registry": "meta",  # the octopus-era registry (F7)
}

_META_TOKEN_PHRASES = [
    ("registry",), ("ledger",), ("log", "like"), ("route", "list"),
    ("route", "table"), ("route", "map"), ("scoreboard",), ("checkpoint",),
    ("atlas",), ("dossier",), ("status", "note"), ("status", "summary"),
    ("countermodel", "list"), ("route", "memory"), ("table",),
    ("decision", "to", "abandon"), ("decision", "aid"), ("tooling",),
    ("governance",), ("process",), ("audit",), ("review",), ("verdict",),
    ("finding",), ("meta",),
]
_NOGO_TOKENS = [("no", "go"), ("negative",), ("refutation",), ("impossibility",)]
_OPEN_TOKENS = [("open", "gate"), ("conjecture",), ("proposal",), ("brainstorm",),
                ("target", "identification"), ("recommendation",)]
_POS_TOKENS = [("positive", "theorem"), ("retained",), ("unconditional",)]


def _has_phrase(tokens, phrase):
    n = len(phrase)
    return any(tuple(tokens[i:i + n]) == phrase for i in range(len(tokens) - n + 1))


def canonical_claim_type(historic_field):
    """Deterministic historic_<x> -> canonical claim-type mapping (F1)."""
    if historic_field in CLAIM_TYPE_OVERRIDES:
        return CLAIM_TYPE_OVERRIDES[historic_field]
    if not historic_field.startswith("historic_"):
        raise SystemExit("unmapped claim-type field (not historic_*): %r" % historic_field)
    tokens = historic_field[len("historic_"):].split("_")
    for group, label in (
        (_META_TOKEN_PHRASES, "meta"),
        ([("bounded",)], "bounded_theorem"),
        (_NOGO_TOKENS, "no_go"),
        (_OPEN_TOKENS, "open_gate"),
        (_POS_TOKENS, "positive_theorem"),
    ):
        for phrase in group:
            if _has_phrase(tokens, phrase):
                return label
    # substantive fallback: an era-scoped result awaiting audit.
    return "bounded_theorem"


# ---------------------------------------------------------------------------
# F9/F10/F11 — review flags for the future auditor (registration-only).
REVIEW_FLAGS = {
    ("packsci01", 10259): [
        ("F9 (BUG, pinned-runner integrity, quoted from review): the pinned runner's "
         "headline PASS hard-codes its load-bearing lemma and tests group elements "
         "instead of the claimed generated algebra. It enumerates the 24 permutation "
         "matrices and checks that no two matrices in that finite set anticommute, "
         "while the claim concerns every Hermitian element of the generated "
         "sub-*-algebra including linear combinations; the weight-preserving-A_min-"
         "operators-inside-the-S4-permutation-algebra inclusion is set to literal "
         "True citing prose; the \"4-dim\" algebra PASSes are hard-coded although the "
         "span of the 24 natural 4-by-4 permutation matrices has dimension 10; the "
         "headline verification flag follows from the finite-set check plus "
         "rank(P_A)=4 alone. The historic PASS count must not be presented as "
         "theorem verification."),
        ("F11 (NO_GO_OVERCLAIM, quoted from review): the universal-impossibility "
         "reading fails the structured no-go gate (N1-N8) at the wrapper/original "
         "handoff. The composition covers nine historical attack frames and the "
         "pinned original itself admits a counterexample could lie outside them "
         "(\"hard\" is not an exhaustiveness lemma). This intake row registers a "
         "PROPOSED universal no-go with an unclosed exhaustiveness obligation; any "
         "eventual audit must set the no-go gate and include the nine premises plus "
         "the full generated-algebra obligation."),
    ],
    ("packsci01", 10256): [
        ("F10 (EQUIVALENT_STRENGTH_GAP, quoted from review): the pinned runner "
         "inserts z=0 rather than deriving it. Its dependency \"verification\" is "
         "mostly substring presence; every chain piece is marked available with "
         "literal True; the algebra derives the conditional identity "
         "Q(z)=2/[3(1+z)] and evaluates the descent only at the already selected "
         "value z=0. The unproved target-strength bridge is (i) that the physical "
         "charged-lepton source/background lies in the restricted local source "
         "domain and (ii) that the allowed descent forces its reduced traceless "
         "coordinate to vanish. The historic PASS=29 FAIL=0 is algebra-only "
         "support, not chain closure."),
    ],
    ("packsci01", 10254): [
        ("F10 (EQUIVALENT_STRENGTH_GAP, shared with the block-01 chain wrapper, "
         "quoted from review): the pinned runner behind this certified chain "
         "evaluates the descent only at the inserted value z=0 and marks chain "
         "availability with literal True flags; the certificate itself names the "
         "strict-locality inference and physical-lepton-domain membership as "
         "hostile-review pressure points. The V8 seven-criteria PASS record is "
         "algebra-only support, not closure of those obligations."),
    ],
}
REVIEW_FLAGS_FOOTER = ("These flags quote review-loop iteration 1 findings (Sol, 2026-08-08) for the "
                       "future auditor. History is immutable: the pinned original and its runner are "
                       "unchanged; this wrapper remains registration-only.")

# ---------------------------------------------------------------------------
# F13 — bare route/axiom codes in H1 titles (mechanical).
# Letters that form era-local workstream/route codes when followed by 1-3
# digits. C/D/I/U/Z/S^n etc. are excluded: bare C3/D3/U1/Z3/I3/S3 are
# canonical mathematical-object names per docs/repo/CONTROLLED_VOCABULARY.md.
TITLE_CODE_RE = re.compile(r"\b(?:EX|[ABEFGHNOPQRSTVWXY])[0-9]{1,3}\b")


def title_codes_needing_expansion(title):
    codes = []
    for m in TITLE_CODE_RE.finditer(title):
        before = title[:m.start()].rstrip()
        after = title[m.end():].lstrip()
        # already the parenthesized legacy alias, or already expanded by a
        # parenthetical right after the code -> leave alone
        if before.endswith("("):
            continue
        if after.startswith(")") or after.startswith("("):
            continue
        if m.group(0) not in codes:
            codes.append(m.group(0))
    return codes


def explicit_subject_line(title, headline, scope):
    codes = title_codes_needing_expansion(title)
    if not codes:
        return None
    src = headline or scope or "see the pinned original"
    sentence = src.split(". ")[0].strip()
    if len(sentence) > 280:
        sentence = sentence[:280].rsplit(" ", 1)[0] + " ..."
    if not sentence.endswith((".", "!", "?", "...")):
        sentence += "."
    return ("Explicit subject: %s (The bare code%s %s in the title %s era-local historic "
            "shorthand preserved verbatim from the original; the pinned original defines %s.)"
            % (sentence, "s" if len(codes) > 1 else "",
               ", ".join("`%s`" % c for c in codes),
               "are" if len(codes) > 1 else "is",
               "them" if len(codes) > 1 else "it"))


# ---------------------------------------------------------------------------
# F4 — inert rendering of historic runner names.
def inert_runner(name):
    """Render a historic runner name so the live citation-graph runner
    extractor (docs/audit/scripts/build_citation_graph.py RUNNER_PATH_RE)
    cannot bind it to a same-named file in the current tree: the .py
    extension is split off as "(.py)" so no `*.py` token appears."""
    shown = name[:-3] + "(.py)" if name.endswith(".py") else name
    return "historic runner (unpinned, not in this packet): `%s`" % shown


def runners_field(runner_list):
    if not runner_list:
        return "none"
    return "; ".join(inert_runner(r) for r in runner_list)


# ---------------------------------------------------------------------------
def jl(path):
    out = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def idx_of(row):
    return row["idx_pos"] if "idx_pos" in row else row["idx"]


def claim_type_field(ct):
    if not ct:
        return "historic_claim"
    s = str(ct).lower()
    s = s.split(" (")[0]
    s = s.split(";")[0]
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return "historic_" + (s or "claim")


def slug_of(path):
    stem = os.path.basename(path)
    if "." in stem:
        stem = stem[: stem.rindex(".")]
    return re.sub(r"[^A-Za-z0-9]+", "_", stem).upper().strip("_")


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def md_target(rel):
    return rel.replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def audit_yaml(historic_field):
    return ("```yaml\n"
            "audit_required_before_effective_retained: true\n"
            "bare_retained_allowed: false\n"
            "historic_intake: true\n"
            "historic_claim_class: %s\n"
            "intake_directive: owner_2026-08-05\n"
            "```" % historic_field)


# ---------------- fetch (unchanged fallback ladder from the part-1 script) --
def git_show(ref, path):
    spec = "%s:%s" % (ref, path)
    p = subprocess.run(["git", "-C", CENSUS, "show", spec], capture_output=True)
    if p.returncode != 0:
        return None, None
    q = subprocess.run(["git", "-C", CENSUS, "rev-parse", spec],
                       capture_output=True, text=True)
    blob = q.stdout.strip() if q.returncode == 0 else None
    return p.stdout, blob


def fetch(man):
    """Returns (bytes, blob, ref_used, note). bytes None => unresolved."""
    path = man.get("path")
    tried = []
    ref = man.get("ref")
    if ref:
        b, blob = git_show(ref, path)
        if b is not None:
            return b, blob, ref, None
        tried.append("ref %s" % ref[:12])
    pr = man.get("pr_number")
    if pr:
        for cand in ("refs/pull-cache/%d" % pr, "refs/pull-cache/%d^{commit}" % pr):
            b, blob = git_show(cand, path)
            if b is not None:
                return b, blob, "refs/pull-cache/%d" % pr, None
        tried.append("refs/pull-cache/%d" % pr)
    resc = man.get("rescued_to")
    if resc:
        full = os.path.join(CENSUS, resc)
        if os.path.exists(full):
            b = open(full, "rb").read()
            q = subprocess.run(["git", "hash-object", full], capture_output=True, text=True)
            return b, (q.stdout.strip() or None), "worktree:%s" % resc, None
        tried.append("rescue %s" % resc)
    if man.get("in_origin_main_history"):
        b, blob = git_show("origin/main", path)
        if b is not None:
            return b, blob, "origin/main", None
        tried.append("origin/main")
    q = subprocess.run(["git", "-C", CENSUS, "log", "--all", "--diff-filter=A",
                        "--format=%H", "-1", "--", path], capture_output=True, text=True)
    sha = q.stdout.strip().splitlines()
    if sha:
        b, blob = git_show(sha[0], path)
        if b is not None:
            return b, blob, sha[0], None
        tried.append("path-history %s" % sha[0][:12])
    else:
        tried.append("path-history (no adding commit found)")
    return None, None, ref, "; ".join(tried) if tried else "no ref, no pr_number, no rescue path in manifest"


def global_index():
    g = {}
    for fn in sorted(os.listdir(os.path.join(TRIAGE, "manifests"))):
        if not fn.endswith(".json"):
            continue
        for r in json.load(open(os.path.join(TRIAGE, "manifests", fn))):
            g.setdefault(r["idx_pos"], (fn[:-5], r.get("path")))
    return g


# ---------------------------------------------------------------------------
def render(d):
    L = []
    L.append("# Historic intake: %s" % d["title"])
    subject = explicit_subject_line(d["title"], d["raw_headline"], d["raw_scope"])
    if subject:
        L.append("")
        L.append(subject)
    L.append("")
    L.append("Date: 2026-08-05")
    L.append("Authority: none")
    L.append("Audit: unset")
    L.append("Claim type: %s" % d["ctype"])
    L.append("Stratum: %s" % d["stratum"])
    L.append("Era: %s" % d["era"])
    L.append("")
    L.append(STATUS)
    L.append("")
    L.append("## The claim (as stated by the original, supervisor-compressed)")
    L.append("")
    L.append(d["headline"])
    L.append("")
    L.append("Original verdict: %s" % d["verdict"])
    L.append("Scope: %s" % d["scope"])
    L.append(("Escape conditions (negative claims): %s" % d["escape"]) if d["escape"] else "")
    L.append("")
    L.append(WHY_PULLED_HEADER)
    L.append("")
    L.append(WHY_PULLED_DISCLAIMER)
    L.append("")
    L.append(d["reason"])
    L.append("")
    L.append("## Provenance (pinned)")
    L.append("")
    L.append("- Original path: `%s`" % d["orig_path"])
    L.append("- Source commit: `%s`" % d["ref"])
    L.append("- git blob: `%s`" % d["blob"])
    L.append("- sha256: `%s`" % d["sha"])
    L.append("- Archived original (byte-exact, sha256-verified at generation): [%s](%s)"
             % (d["arch_rel"], md_target(d["arch_rel"])))
    L.append("- Lines: %s; runners named: %s" % (d["n_lines"], d["runners"]))
    L.append("")
    L.append("## Attached evidence (registered with, not as, this claim)")
    L.append("")
    L.extend(d["attached"] if d["attached"] else ["- none"])
    if d["cross"]:
        L.append("")
        L.append("## Cross-stratum flags")
        L.append("")
        L.extend(d["cross"])
    L.append("")
    L.append("## Flags carried")
    L.append("")
    L.append(d["flags"])
    if d["review_flags"]:
        L.append("")
        L.append("## Review flags (review-loop 2026-08-08)")
        L.append("")
        for f in d["review_flags"]:
            L.append("- %s" % f)
        L.append("")
        L.append(REVIEW_FLAGS_FOOTER)
    L.append("")
    L.append("## Audit fields")
    L.append("")
    L.append(audit_yaml(d["historic_field"]))
    L.append("")
    L.append("Independent audit still required.")
    L.append("")
    return "\n".join(L)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    build = mode == "build"

    # shipped manifests are the pin authority (fail-closed against drift)
    old_p1 = json.load(open(os.path.join(OUT, "INTAKE_MANIFEST_2026-08-05.json")))
    old_p2 = json.load(open(os.path.join(OUT, "INTAKE_MANIFEST_PART2_2026-08-05.json")))
    old_by_key = {}
    for r in old_p1 + old_p2:
        old_by_key[(r["stratum"], r["idx"])] = r
    pulled_file = {}   # (stratum, idx) -> shipped wrapper filename, for F5 links
    for (s, i), r in old_by_key.items():
        pulled_file[(s, i)] = r["file"]

    GIDX = global_index()

    # cross rows per part (part scoping preserved from the original two-script run)
    cross_rows = {1: [], 2: []}
    for stratum, decfiles, _e, _m, part in STRATA:
        for f in decfiles:
            for r in jl(os.path.join(TRIAGE, "decisions", f)):
                if r.get("attach_to_cross") is not None:
                    cross_rows[part].append((stratum, idx_of(r), r.get("path"),
                                             r["attach_to_cross"], r.get("decision"), r.get("reason", "")))
    incoming = {1: {}, 2: {}}
    for part in (1, 2):
        for src_s, src_i, src_p, tgt, dec_, reason in cross_rows[part]:
            incoming[part].setdefault(tgt, []).append((src_s, src_i, src_p, dec_, reason))

    def link_if_pulled(stratum_guess, idx):
        """Return shipped wrapper filename if (stratum, idx) is a pulled wrapper."""
        return pulled_file.get((stratum_guess, idx))

    manifest_rows = {1: [], 2: []}
    counts = {}
    ct_dist = {}
    used_slugs = {}
    written = []
    errors = []
    pending = []  # (absolute path, bytes) — nothing is written until ALL checks pass

    for stratum, decfiles, extfile, manfile, part in STRATA:
        dec = []
        for f in decfiles:
            dec.extend(jl(os.path.join(TRIAGE, "decisions", f)))
        ext = {r["idx_pos"]: r for r in jl(os.path.join(TRIAGE, "extracted", extfile))}
        man = {r["idx_pos"]: r for r in json.load(open(os.path.join(TRIAGE, "manifests", manfile)))}

        att, cross = {}, {}
        for r in dec:
            if r.get("attach_to") is not None:
                att.setdefault(r["attach_to"], []).append(r)
            if r.get("attach_to_cross") is not None:
                cross.setdefault(idx_of(r), []).append(r)

        pulls = sorted([r for r in dec if r.get("decision") == "PULL"], key=idx_of)
        counts[stratum] = len(pulls)

        for p in pulls:
            idx = idx_of(p)
            e = ext.get(idx) or {}
            m = man.get(idx, {})
            orig_path = p.get("path") or e.get("path") or m.get("path")
            old = old_by_key.get((stratum, idx))
            if old is None:
                errors.append("no shipped manifest row for %s idx %s" % (stratum, idx))
                continue
            mm = dict(m)
            mm.setdefault("path", orig_path)

            b, blob, ref_used, note = fetch(mm)
            if b is None:
                errors.append("UNRESOLVED fetch %s idx %s (%s)" % (stratum, idx, note))
                continue
            sha = sha256(b)
            # fail-closed pin verification against the shipped manifest (F2)
            for field, got in (("ref", ref_used), ("git_blob", blob), ("sha256", sha),
                               ("original_path", orig_path)):
                if old.get(field) != got:
                    errors.append("PIN DRIFT %s idx %s field %s: shipped %r != refetched %r"
                                  % (stratum, idx, field, old.get(field), got))

            # archived original (F2)
            arch_name = "%s_%s" % (idx, os.path.basename(orig_path))
            arch_rel = "%s/%s/%s" % (ARCH_REL_FROM_WRAPPER, stratum, arch_name)
            pending.append((os.path.join(ARCH, stratum, arch_name), b))

            # attached-evidence lines (F5: link items that are themselves pulled)
            alines = []
            if part == 1:
                akey = lambda r: ((r.get("path") or (ext.get(idx_of(r)) or {}).get("path")
                                   or (man.get(idx_of(r)) or {}).get("path") or ""), idx_of(r))
            else:
                akey = lambda r: ((r.get("path") or ""), idx_of(r))
            for a in sorted(att.get(idx, []), key=akey):
                ai = idx_of(a)
                if part == 1:
                    apath = (a.get("path") or (ext.get(ai) or {}).get("path")
                             or (man.get(ai) or {}).get("path")
                             or "(path not recorded; idx %s)" % ai)
                else:
                    apath = a.get("path") or (ext.get(ai) or {}).get("path") or "(idx %s)" % ai
                fn = link_if_pulled(stratum, ai)
                if fn:
                    alines.append("- [`%s`](%s) — %s" % (apath, md_target(fn), a.get("reason", "")))
                else:
                    alines.append("- `%s` — %s" % (apath, a.get("reason", "")))

            # cross-stratum lines (F5: link targets/sources that are pulled wrappers)
            clines = []
            for c in cross.get(idx, []):
                tgt = c["attach_to_cross"]
                ts, tp = GIDX.get(tgt, ("unknown_stratum", None))
                fn = link_if_pulled(ts, tgt)
                if fn:
                    clines.append("- Attaches across strata to [idx %s](%s) (`%s`, stratum %s) — %s"
                                  % (tgt, md_target(fn), tp or "(path not recorded)", ts, c.get("reason", "")))
                else:
                    clines.append("- Attaches across strata to idx %s (`%s`, stratum %s) — %s"
                                  % (tgt, tp or "(path not recorded)", ts, c.get("reason", "")))
            for src_s, src_i, src_p, dec_, reason in incoming[part].get(idx, []):
                if src_s == stratum and src_i == idx:
                    continue
                sp = src_p or GIDX.get(src_i, (None, None))[1]
                fn = link_if_pulled(src_s, src_i)
                if fn:
                    clines.append("- Cross-stratum reference from %s [idx %s](%s) (`%s`, decision %s) — %s"
                                  % (src_s, src_i, md_target(fn), sp or "(path not recorded)", dec_, reason))
                else:
                    clines.append("- Cross-stratum reference from %s idx %s (`%s`, decision %s) — %s"
                                  % (src_s, src_i, sp or "(path not recorded)", dec_, reason))

            runners = e.get("runner_paths") or []
            historic_field = claim_type_field(e.get("claim_type"))
            ctype = canonical_claim_type(historic_field)
            if ctype not in CANONICAL_CLAIM_TYPES:
                raise SystemExit("mapping produced unrecognized claim type %r" % ctype)
            ct_dist[ctype] = ct_dist.get(ctype, 0) + 1

            d = {
                "title": e.get("title") or os.path.basename(orig_path),
                "raw_headline": e.get("headline"),
                "raw_scope": e.get("scope"),
                "ctype": ctype,
                "historic_field": historic_field,
                "stratum": e.get("stratum") or m.get("stratum") or stratum,
                "era": e.get("axioms_era") or "unknown",
                "headline": e.get("headline") or "(no extraction row available; original bytes are pinned below)",
                "verdict": e.get("verdict") or "none recorded",
                "scope": e.get("scope") or "none recorded",
                "escape": e.get("nogo_escape"),
                "reason": p.get("reason", ""),
                "orig_path": orig_path,
                "ref": ref_used,
                "blob": blob,
                "sha": sha,
                "arch_rel": arch_rel,
                "n_lines": e.get("n_lines", "unknown"),
                "runners": runners_field(runners),
                "attached": alines,
                "cross": clines,
                "flags": e.get("red_flags") or "none recorded",
                "review_flags": REVIEW_FLAGS.get((stratum, idx)),
            }
            body = render(d)

            slug = slug_of(orig_path)
            if slug in used_slugs:
                slug = "%s_B%s" % (slug, idx)
            used_slugs[slug] = (stratum, idx)
            fname = "HISTORIC_%s_INTAKE_NOTE_2026-08-05.md" % slug
            if fname != old["file"]:
                errors.append("FILENAME DRIFT %s idx %s: shipped %s != regenerated %s"
                              % (stratum, idx, old["file"], fname))

            reason_sha = hashlib.sha256(p.get("reason", "").encode("utf-8")).hexdigest()
            if reason_sha != old["decision_reason_sha256"]:
                errors.append("REASON DRIFT %s idx %s" % (stratum, idx))
            if len(alines) != old["n_attached"]:
                errors.append("ATTACH-COUNT DRIFT %s idx %s: shipped %d != %d"
                              % (stratum, idx, old["n_attached"], len(alines)))

            pending.append((os.path.join(OUT, fname), body.encode("utf-8")))
            written.append(fname)

            manifest_rows[part].append({
                "file": fname,
                "stratum": stratum,
                "idx": idx,
                "original_path": orig_path,
                "ref": ref_used,
                "git_blob": blob,
                "sha256": sha,
                "n_attached": len(alines),
                "decision_reason_sha256": reason_sha,
            })

    if errors:
        for x in errors[:40]:
            print("ERROR:", x, file=sys.stderr)
        raise SystemExit("FAIL-CLOSED: %d verification errors; nothing shipped." % len(errors))

    # ---------- octopus era registry (F7) ----------
    odec = jl(os.path.join(TRIAGE, "decisions", "octopus_decisions.jsonl"))[0]
    src = os.path.join(TRIAGE, "extracted", "octopus_era_claims.md")
    body = open(src, "rb").read()
    body_sha = sha256(body)
    q = subprocess.run(["git", "hash-object", src], capture_output=True, text=True)
    body_blob = q.stdout.strip() or "UNRESOLVED"
    old_oct = old_by_key[("octopus", None)]
    if (body_sha != old_oct["sha256"]) or (body_blob != old_oct["git_blob"]):
        raise SystemExit("FAIL-CLOSED: octopus registry payload pin drift")
    jsonl_src = os.path.join(TRIAGE, "extracted", "octopus_era.jsonl")
    jsonl_bytes = open(jsonl_src, "rb").read()
    pending.append((os.path.join(ARCH, "octopus", "octopus_era_claims.md"), body))
    pending.append((os.path.join(ARCH, "octopus", "octopus_era.jsonl"), jsonl_bytes))
    title = body.decode("utf-8").splitlines()[0].lstrip("# ").strip()
    H = []
    H.append("# Historic intake: %s" % title)
    H.append("")
    H.append("Date: 2026-08-05")
    H.append("Authority: none")
    H.append("Audit: unset")
    H.append("Claim type: meta")
    H.append("Stratum: %s" % odec.get("stratum", "octopus_era_commits"))
    H.append("Era: octopus_era — the pre-note era (2026-03-13..2026-04-16), which exists only in commits")
    H.append("")
    H.append(STATUS)
    H.append("")
    H.append(WHY_PULLED_HEADER)
    H.append("")
    H.append(WHY_PULLED_DISCLAIMER)
    H.append("")
    H.append(odec.get("reason", ""))
    H.append("")
    H.append("## Provenance (pinned)")
    H.append("")
    H.append("- Original path: `triage_2026-08-05/%s`" % odec.get("object", "extracted/octopus_era_claims.md").split("triage_2026-08-05/")[-1])
    H.append("- Source commit: `n/a (triage-assembled registry; content pinned by hash below)`")
    H.append("- git blob: `%s`" % body_blob)
    H.append("- sha256: `%s`" % body_sha)
    H.append("- Archived original (byte-exact, sha256-verified at generation): [%s/octopus/octopus_era_claims.md](%s/octopus/octopus_era_claims.md)"
             % (ARCH_REL_FROM_WRAPPER, ARCH_REL_FROM_WRAPPER))
    H.append("- Lines: %d; runners named: none" % len(body.decode("utf-8").splitlines()))
    H.append("")
    H.append("## Attached evidence (registered with, not as, this claim)")
    H.append("")
    H.append("- [`triage_2026-08-05/extracted/octopus_era.jsonl`](%s/octopus/octopus_era.jsonl) — the registry's evidence base: 3179 per-commit rows, one per distinct (date, subject) group; no per-claim wrappers were made. Byte-exact copy archived at the linked path (sha256 `%s`)."
             % (ARCH_REL_FROM_WRAPPER, sha256(jsonl_bytes)))
    H.append("")
    H.append("## Flags carried")
    H.append("")
    H.append("none recorded")
    H.append("")
    H.append("## Audit fields")
    H.append("")
    H.append(audit_yaml("historic_registry"))
    H.append("")
    H.append("Independent audit still required.")
    H.append("")
    H.append("---")
    H.append("")
    ofname = "HISTORIC_OCTOPUS_ERA_CLAIM_REGISTRY_2026-08-05.md"
    pending.append((os.path.join(OUT, ofname), ("\n".join(H)).encode("utf-8") + body))
    written.append(ofname)
    manifest_rows[1].append({
        "file": ofname,
        "stratum": "octopus",
        "idx": None,
        "original_path": "triage_2026-08-05/extracted/octopus_era_claims.md",
        "ref": None,
        "git_blob": body_blob,
        "sha256": body_sha,
        "n_attached": 1,
        "decision_reason_sha256": hashlib.sha256(odec.get("reason", "").encode("utf-8")).hexdigest(),
    })
    counts["octopus"] = 1
    ct_dist["meta"] = ct_dist.get("meta", 0) + 1

    # ---------- hazards memo (F8) ----------
    haz_src = os.path.join(TRIAGE, "decisions", "packsci_hazards_for_audit_lane.md")
    haz = open(haz_src, "r").read().splitlines()
    haz_header = [
        "",
        "Date: 2026-08-05 (part-2 ship 2026-08-06; header added by review-loop regeneration 2026-08-08)",
        "Authority: none",
        "Audit: unset",
        "Claim type: meta",
        "Status: routing guidance, non-evidentiary. This memo carries supervisor triage",
        "hazard notes for the audit lane about rows NOT pulled into intake. It asserts",
        "no claim, confers no verdict, demotion, or effective status, and must not be",
        "consumed as evidence; each entry is provenance pointing at the named surface,",
        "and substantive corrections require their own auditable claim rows.",
    ]
    haz_out = "\n".join([haz[0]] + haz_header + haz[1:]) + "\n"
    pending.append((os.path.join(OUT, "HISTORIC_INTAKE_PART2_HAZARDS_2026-08-05.md"),
                    haz_out.encode("utf-8")))

    # ---------- manifests (must be byte-identical to the shipped pins) ----------
    rows1 = sorted(manifest_rows[1], key=lambda r: (r["stratum"], -1 if r["idx"] is None else r["idx"]))
    rows2 = sorted(manifest_rows[2], key=lambda r: (r["stratum"], r["idx"]))
    new1 = json.dumps(rows1, indent=1, sort_keys=True) + "\n"
    new2 = json.dumps(rows2, indent=1, sort_keys=True) + "\n"
    shipped1 = open(os.path.join(OUT, "INTAKE_MANIFEST_2026-08-05.json")).read()
    shipped2 = open(os.path.join(OUT, "INTAKE_MANIFEST_PART2_2026-08-05.json")).read()
    if new1 != shipped1 or new2 != shipped2:
        raise SystemExit("FAIL-CLOSED: regenerated manifest differs from shipped manifest pins")
    pending.append((os.path.join(OUT, "INTAKE_MANIFEST_2026-08-05.json"), new1.encode("utf-8")))
    pending.append((os.path.join(OUT, "INTAKE_MANIFEST_PART2_2026-08-05.json"), new2.encode("utf-8")))

    # ---------- indexes ----------
    regen_note = [
        "",
        "## Review-loop regeneration (2026-08-08)",
        "",
        "Every wrapper in this intake was regenerated through the corrected template",
        "after review-loop iteration 1 (Sol, FIX_THEN_PROCEED): canonical `Claim type:`",
        "headers with the historic taxonomy preserved as `historic_claim_class` (F1);",
        "byte-exact archived originals under `archive_unlanded/historic_intake_originals/`",
        "linked from each wrapper and sha256-verified fail-closed (F2); the Why-pulled",
        "section marked provenance-not-authority with a non-evidentiary disclaimer",
        "(F3/F6); historic runner names rendered inert and unlinked (F4); attach/cross",
        "references to pulled wrappers rendered as relative links (F5); the Octopus",
        "registry typed meta with its evidence base archived (F7); the hazards memo",
        "given a meta header (F8); review flags added to the three affected packsci01",
        "wrappers (F9/F10/F11); explicit subject lines under bare-code titles (F13).",
        "Both manifests are byte-identical to the originally shipped pins; decision",
        "reasons are untouched (sha256-verified). Generator:",
        "`scripts/historic_intake_generate_2026_08_05(.py)` (extension split per the",
        "F4 inert-name convention; this index is a meta surface and names no runner).",
    ]

    part1_counts = {k: v for k, v in counts.items()
                    if k in ("march", "recovery", "octopus") or k.startswith("branch0") and k != "branch09"}
    I = []
    I.append("# Historic intake index — 2026-08-05")
    I.append("")
    I.append("Claim type: meta")
    I.append("")
    I.append("Assembly of the 2026-08-05 historic-science triage PULL decisions into intake")
    I.append("wrapper notes. Every wrapper is DATA: it carries the supervisor's decision reason")
    I.append("verbatim, the extraction's own claim compression, and a byte-exact provenance pin.")
    I.append("No keep/discard judgment was made or altered during assembly.")
    I.append("")
    I.append("- Wrapper notes written: %d" % len([r for r in rows1 if r["stratum"] != "octopus"]))
    I.append("- Era registries written: %d" % len([r for r in rows1 if r["stratum"] == "octopus"]))
    I.append("- Machine manifest: `INTAKE_MANIFEST_2026-08-05.json`")
    I.append("")
    I.append("## Counts per stratum")
    I.append("")
    I.append("| Stratum | Wrappers |")
    I.append("|---|---|")
    for k in sorted(part1_counts):
        I.append("| %s | %d |" % (k, part1_counts[k]))
    I.append("| **total** | **%d** |" % sum(part1_counts.values()))
    I.append("")
    I.append("## UNRESOLVED pins")
    I.append("")
    I.append("none — original bytes were fetched and hashed for every wrapper.")
    I.append("")
    I.append("## Slug collisions")
    I.append("")
    I.append("none — every pull produced a distinct slug.")
    I.append("")
    I.append("## Decision rows with no matching extraction row")
    I.append("")
    I.append("none — every PULL decision matched an extraction row.")
    I.append("")
    I.append("## Cross-stratum flags")
    I.append("")
    for src_s, src_i, src_p, tgt, dec_, reason in cross_rows[1]:
        ts, tp = GIDX.get(tgt, ("unknown_stratum", None))
        I.append("- %s idx %s (`%s`, decision %s) -> idx %s (`%s`, stratum %s)"
                 % (src_s, src_i, src_p or (GIDX.get(src_i, (None, None))[1] or "(path not recorded)"),
                    dec_, tgt, tp or "(path not recorded)", ts))
    I.extend(regen_note)
    I.append("")
    I.append("Independent audit still required for every note listed here.")
    I.append("")
    pending.append((os.path.join(OUT, "INTAKE_INDEX_2026-08-05.md"), "\n".join(I).encode("utf-8")))

    part2_counts = {k: v for k, v in counts.items()
                    if k == "branch09" or k.startswith("packsci")}
    J = []
    J.append("# Historic intake index, part 2 — branch09 + pack-family strata")
    J.append("")
    J.append("Claim type: meta")
    J.append("")
    J.append("Part 2 of the 2026-08-05 historic-science triage intake (part 1:")
    J.append("`INTAKE_INDEX_2026-08-05.md`, 622 wrappers). Same mechanism, same template,")
    J.append("same audit fields. Every wrapper is DATA: the supervisor's decision reason")
    J.append("verbatim, the extraction's claim compression, and a byte-exact provenance pin.")
    J.append("")
    J.append("- Wrapper notes written: %d" % sum(part2_counts.values()))
    J.append("- Machine manifest: `INTAKE_MANIFEST_PART2_2026-08-05.json`")
    J.append("- Audit-lane hazards from these strata (not wrappers):")
    J.append("  `triage decisions/packsci_hazards_for_audit_lane.md` (in the census worktree),")
    J.append("  shipped alongside as `HISTORIC_INTAKE_PART2_HAZARDS_2026-08-05.md`.")
    J.append("")
    J.append("## Counts per stratum")
    J.append("")
    J.append("| Stratum | Wrappers |")
    J.append("|---|---|")
    for k in sorted(part2_counts):
        J.append("| %s | %d |" % (k, part2_counts[k]))
    J.append("| **total** | **%d** |" % sum(part2_counts.values()))
    J.append("")
    J.append("## UNRESOLVED pins")
    J.append("")
    J.append("none — original bytes were fetched and hashed for every wrapper.")
    J.extend(regen_note)
    J.append("")
    pending.append((os.path.join(OUT, "INTAKE_INDEX_PART2_2026-08-05.md"), "\n".join(J).encode("utf-8")))

    # ---------- write phase: only reached with zero verification errors ----------
    if build:
        for path, data in pending:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as fh:
                fh.write(data)
        # post-write archive verification: every archived original byte-matches its pin
        for r in rows1 + rows2:
            if r["stratum"] == "octopus":
                ap = os.path.join(ARCH, "octopus", "octopus_era_claims.md")
            else:
                ap = os.path.join(ARCH, r["stratum"], "%s_%s" % (r["idx"], os.path.basename(r["original_path"])))
            if sha256(open(ap, "rb").read()) != r["sha256"]:
                raise SystemExit("FAIL-CLOSED: archived original mismatch: %s" % ap)

    print(json.dumps({
        "mode": mode,
        "wrappers_written": len(written),
        "counts": counts,
        "claim_type_distribution": ct_dist,
        "manifest_byte_identity": True,
        "archived_originals": len([1 for p, _ in pending if p.startswith(ARCH)]),
        "errors": 0,
    }, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
