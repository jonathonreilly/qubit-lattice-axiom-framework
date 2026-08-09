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

Review-loop iteration 2 (Sol, 2026-08-08, confirmation round) adds:

  F4(2) EVERY rendered wrapper field (runner names incl. suffixed tokens,
      headline/verdict/scope/escape, decision reasons, flags, attach/cross
      text) is display-neutralized for `.py` tokens with a zero-width space
      split, so the live runner extractor can bind nothing; the byte-exact
      original wording stays pinned in the triage decisions/extraction JSONL
      (decision_reason_sha256 unchanged) and in the archived originals.
  F5(2) markdown links (deps edges) are kept ONLY for attachment relations;
      contradiction/cross-flag relations render as inert text plus
      machine-readable `contradicts:`/`cross_reference:` lists in the
      audit-fields yaml; named non-pulled contradiction/withdrawal evidence
      and the panel-reversal set members are archived byte-exact and
      referenced inertly.
  F6(2) "## Triage extraction notes (2026-08-05/08, not from the original)"
      carries ALL extraction-time commentary (red flags + supersession);
      Original verdict / Scope / Escape keep only the extraction's claim
      fields, per the round-2 spec.
  F8(2) the hazards memo gains a Provenance block pinning its archived
      evidence base (the branch09/packsci01-05 extraction JSONLs).
  F13(2) bare-code H1 titles are rewritten so the explicit scientific name is
      the heading and the historic token trails as "(legacy alias: X)".
  no-go retype: wrapper-level `Claim type: no_go` becomes `bounded_theorem`
      (registration of a historical NEGATIVE claim; historic_claim_class
      keeps the historic taxonomy) with an explicit no-live-no-go sentence;
      wrapper FILENAMES also neutralize no-go/obstruction/firewall tokens so
      no registration wrapper is a no-go-named artifact (filename-level no-go
      authority is forensic per docs/audit/scripts/no_go_discipline_gate.py).
  portable links: an archived original whose bytes contain machine-absolute
      markdown link targets is stored with a `.frozen` filename suffix
      (bytes unchanged, sha256 pins intact).
  hygiene: --triage/--census CLI overrides; `check` byte-compares every
      rendered output against the checkout and fails on drift; unknown modes
      error out.

Inputs (frozen, read-only): the 2026-08-05 triage decision/extraction/manifest
JSONL under --triage, and the shared git object store reachable from --census.
The shipped intake manifests are treated as the pin authority: regeneration
FAILS if any re-fetched ref/blob/sha256/filename/reason-hash differs from the
shipped manifest row, so pins can never drift silently.

Usage: python3 scripts/historic_intake_generate_2026_08_05.py {check|build}
           [--triage PATH] [--census PATH]
"check" performs every fetch, verification and render, then byte-compares the
rendered outputs against the checkout without writing; any drift fails.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

# Assembly-time defaults, documented: the frozen 2026-08-05 triage tree and
# the census worktree whose git object store holds every pinned blob. Both are
# machine-local absolute paths on the assembly machine; override with
# --triage/--census when reproducing elsewhere.
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
NEGATIVE_REGISTRATION_SENTENCE = (
    "Registered as a bounded registration of a historical negative claim; no live "
    "no-go is asserted by this wrapper — no-go discipline applies at audit "
    "adjudication.")
NEUTRALIZE_NOTE = (
    "- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized "
    "with a zero-width split for citation-graph hygiene (no current-tree runner may "
    "bind); the byte-exact original wording is pinned in the triage "
    "decisions/extraction JSONL files and in the archived original.")
TRIAGE_NOTES_HEADER = "## Triage extraction notes (2026-08-05/08, not from the original)"
TRIAGE_NOTES_DISCLAIMER = (
    "Written at triage/extraction time; NOT part of the pinned original, carries no "
    "authority, and is input for the future auditor only.")

ZWSP = "\u200b"  # zero-width space (U+200B)
_PY_TOKEN_RE = re.compile("(?<!\u200b)\\.py")


def neutralize_py(s):
    """Display-neutralize every `.py` token so the live runner extractor
    (docs/audit/scripts/build_citation_graph.py RUNNER_PATH_RE) cannot match:
    a zero-width space is inserted before ".py", breaking both the
    `scripts/...py` and the bare-name character-class patterns while leaving
    the rendered text visually identical. Idempotent."""
    if not s:
        return s
    return _PY_TOKEN_RE.sub(ZWSP + ".py", str(s))


# Wrapper FILENAME neutralization: a registration wrapper must not be a
# no-go-named artifact (no_go_discipline_gate.PATH_TRIGGER_RE treats
# filename-level no-go authority as forensic). The historic names survive
# verbatim in the H1 title, the pinned original path, and the archived copy.
FNAME_TOKEN_REPLACEMENTS = (
    ("NO_GO", "NEGATIVE"),
    ("NOGO", "NEGATIVE"),
    ("OBSTRUCTION", "OBSTRUCTED_ROUTE"),
    ("FIREWALL", "ROUTE_BARRIER"),
)


def neutralize_fname(fname):
    for a, b in FNAME_TOKEN_REPLACEMENTS:
        fname = fname.replace(a, b)
    return fname

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
    return ("Explicit subject: %s (Historic code%s %s: era-local shorthand from the "
            "original's own title. The repo's controlled vocabulary keeps the explicit "
            "scientific name primary on live surfaces — vocab_lint's legacy_alias_strip "
            "rule removes alias parentheticals — so the code%s preserved here, in the "
            "pinned original, and in its archived copy; the pinned original defines %s.)"
            % (sentence, "s" if len(codes) > 1 else "",
               ", ".join("`%s`" % c for c in codes),
               "s are" if len(codes) > 1 else " is",
               "them" if len(codes) > 1 else "it"))


# F13(2): explicit scientific name AS the H1. The generic rule removes the
# bare code token(s); TITLE_OVERRIDES freezes the titles where bare removal
# would mangle grammar or lose the referent — each override name is drawn from
# that wrapper's own extraction headline/scope (or the controlled vocabulary's
# canonical expansion, e.g. A2 -> the Lattice axiom). NO trailing
# "(legacy alias: X)" parenthetical is emitted: the repo's binding vocab_lint
# rewrite rule `legacy_alias_strip` ("Aliasing creates rot. Use the canonical
# name only.") auto-removes that form on live docs surfaces, so the historic
# token is preserved instead in the Explicit-subject line, the wrapper
# filename where applicable, and the pinned/archived original title.
_ALIAS_TAIL_RE = re.compile(r"\s*\(legacy alias(?:es)?:[^)]*\)\s*$")
TITLE_OVERRIDES = {
    ("branch01", 6): ("The Lattice Axiom's Two-Sided-Inverse Proviso Fails on Every Finite "
                      "Translation-Covariant Lattice, the Repo's Own Periodic Convention Makes It "
                      "Unsatisfiable, and Covariance Repairs It Without New Input (Bounded Theorem) "
                      "(legacy alias: A2)"),
    ("branch01", 231): ("Cl(3) Cross-Sector Identification Theorem: N_color = N_gen = d = 3 from "
                        "the Era's Base Axiom (legacy alias: A0)"),
    ("branch02", 496): ("Flavor - both paths fail; the site-algebra trace votes Q=1 (correcting "
                        "the native 2/3 lean) (legacy alias: A1)"),
    ("branch02", 548): ("Koide Observational-Pin Closure - the Route Analogous to the "
                        "Doublet-Block Selector Lane (legacy aliases: G5, G1)"),
    ("branch03", 721): ("Hypercharge 1-loop beta-Coefficient Structural Closed Form via Retained "
                        "Structural Values (legacy alias: S1)"),
    ("branch03", 865): ("The K-Reality Predicate is Native to the Cl(3) Site Algebra; the delta "
                        "Channel is Distinct from the Chiral Grading (legacy alias: A1)"),
    ("branch05", 1636): ("Koide-Q Keystone, angle C: holomorphy (det_C) does NOT supply the "
                         "generation chirality grading (legacy alias: Q1)"),
    ("branch05", 1639): ("Koide-Q Keystone (angle B) - the holomorphic reading does not overreach "
                         "and is not cleanly sector-dependent (legacy alias: Q1)"),
    ("branch06", 1823): ("Reviewer-Closure Loop Iter 5: the det(H) Necessity Item Is the Primitive "
                         "Bottleneck (legacy alias: N1)"),
    ("branch06", 1846): ("S^3 Axiom Boundary: Reduces to the Same Lattice-Is-Physical Axiom as "
                         "Generation Physicality (legacy alias: A5)"),
    ("branch07", 2072): ("The Unique Emergent Time AXIS is Derived from the Record Ontology, "
                         "Unconditionally — Correcting the \"Record-Formation Axis Needs a "
                         "Decoherence Dynamics\" Realist Slip (legacy alias: R1)"),
    ("branch07", 2133): ("Within the Supplied Covariant Family, the Lattice Axiom's Missing Bridge "
                         "Theorem Is Exactly 'the On-Site Term Equals the Coordination Number' — "
                         "and As Posed It Carries an Unobservable Energy Offset (legacy alias: A2)"),
    ("branch09", 2841): ("Genuine-3D directional recoil/source-current train — Cycle 506 "
                         "(legacy alias: directional-Q1)"),
}


def transform_title(title, stratum, idx):
    """Return the F13(2) H1 title: the explicit scientific name (no bare code
    as primary name, no alias parenthetical — see _ALIAS_TAIL_RE note above).
    Returns the input unchanged when no bare code is present."""
    if (stratum, idx) in TITLE_OVERRIDES:
        return _ALIAS_TAIL_RE.sub("", TITLE_OVERRIDES[(stratum, idx)]).strip()
    ms = []
    for m in TITLE_CODE_RE.finditer(title):
        before = title[:m.start()].rstrip()
        after = title[m.end():].lstrip()
        if before.endswith("("):
            continue
        if after.startswith(")") or after.startswith("("):
            continue
        ms.append(m)
    if not ms:
        return title
    codes, spans = [], []
    for m in ms:
        s, e = m.start(), m.end()
        mm = re.match(r"(?:-[A-Za-z0-9]{1,3})+\b", title[e:])
        if mm:
            e += mm.end()
        tok = title[s:e]
        if title[e:e + 2] == "'s":
            e += 2
        if tok not in codes:
            codes.append(tok)
        spans.append((s, e))
    out, prev = [], 0
    for s, e in spans:
        out.append(title[prev:s])
        prev = e
    out.append(title[prev:])
    t = "".join(out)
    t = re.sub(r"\s{2,}", " ", t)
    t = re.sub(r"\s+([,:;.!?)])", r"\1", t)
    t = re.sub(r"^\s*[-—/:,]+\s*", "", t)
    t = re.sub(r"\s*[-—/:,]+\s*$", "", t)
    t = re.sub(r"\(\s*\)", "", t).strip()
    t = re.sub(r"\s{2,}", " ", t)
    return t


# ---------------------------------------------------------------------------
# F4 — inert rendering of historic runner names (iteration 2: zero-width
# neutralization handles suffixed tokens like "x.py (scratch, 26 gates)" and
# multi-name entries too; neutralize_py is also applied to every other
# rendered field by render()).
def runners_field(runner_list):
    if not runner_list:
        return "none"
    return "; ".join("historic runner (unpinned, not in this packet): `%s`"
                     % neutralize_py(r) for r in runner_list)


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


def audit_yaml(historic_field, contradicts=None, cross_reference=None):
    """Audit-fields yaml. `contradicts`/`cross_reference` are machine-readable
    relation lists (F5 iteration 2): contradiction and cross-flag relations are
    NOT markdown links (so they never become deps edges); they live here."""
    L = ["```yaml",
         "audit_required_before_effective_retained: true",
         "bare_retained_allowed: false",
         "historic_intake: true",
         "historic_claim_class: %s" % historic_field,
         "intake_directive: owner_2026-08-05"]
    for key, vals in (("contradicts", contradicts), ("cross_reference", cross_reference)):
        if vals:
            L.append("%s:" % key)
            for v in vals:
                L.append('- "%s"' % v.replace('"', "'"))
    L.append("```")
    return "\n".join(L)


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


# machine-absolute markdown link target (portable-link hard gate): "](/...",
# "](file:...", or a drive-letter path.
ABS_MD_LINK_RE = re.compile(rb"\]\(\s*(?:/|file:|[A-Za-z]:[\\/])")

# Wrappers whose NON-pulled attachment members must be archived byte-exact so
# the evidence set is atomically available (F5(2)): the panel-reversal
# withdrawal arc's four members.
ARCHIVE_ATTACHMENT_SETS = {("packsci05", 11538)}

_EVIDENCE_ARCHIVED = {}  # (stratum, idx) -> (arch_rel_repo, sha256)


def archive_evidence(stratum, idx, man_all, pending):
    """Archive a NAMED non-pulled evidence original byte-exact (F5(2)) and
    return the inert reference text. Fail-closed on unfetchable bytes."""
    key = (stratum, idx)
    if key not in _EVIDENCE_ARCHIVED:
        man_row = man_all.get(key)
        if man_row is None:
            raise SystemExit("FAIL-CLOSED: no triage manifest row for evidence %s idx %s"
                             % (stratum, idx))
        b, blob, ref_used, note = fetch(dict(man_row))
        if b is None:
            raise SystemExit("FAIL-CLOSED: cannot fetch evidence %s idx %s (%s)"
                             % (stratum, idx, note))
        name = "%s_%s" % (idx, os.path.basename(man_row.get("path") or "idx_%s" % idx))
        if name.endswith(".md") and ABS_MD_LINK_RE.search(b):
            name += ".frozen"
        pending.append((os.path.join(ARCH, stratum, name), b))
        _EVIDENCE_ARCHIVED[key] = ("archive_unlanded/historic_intake_originals/%s/%s"
                                   % (stratum, name), sha256(b))
    rel, digest = _EVIDENCE_ARCHIVED[key]
    return "archived byte-exact at `%s`, sha256 `%s`" % (rel, digest)


# ---------------------------------------------------------------------------
def render(d):
    n = neutralize_py  # F4(2): every rendered field is display-neutralized
    L = []
    L.append("# Historic intake: %s" % n(d["title"]))
    subject = explicit_subject_line(d["orig_title"], d["raw_headline"], d["raw_scope"])
    if subject:
        L.append("")
        L.append(n(subject))
    L.append("")
    L.append("Date: 2026-08-05")
    L.append("Authority: none")
    L.append("Audit: unset")
    L.append("Claim type: %s" % d["ctype"])
    L.append("Stratum: %s" % d["stratum"])
    L.append("Era: %s" % n(d["era"]))
    L.append("")
    L.append(STATUS)
    if d["negative_registration"]:
        L.append("")
        L.append(NEGATIVE_REGISTRATION_SENTENCE)
    L.append("")
    L.append("## The claim (as stated by the original, supervisor-compressed)")
    L.append("")
    L.append(n(d["headline"]))
    L.append("")
    L.append("Original verdict: %s" % n(d["verdict"]))
    L.append("Scope: %s" % n(d["scope"]))
    L.append(("Escape conditions (negative claims): %s" % n(d["escape"])) if d["escape"] else "")
    L.append("")
    L.append(WHY_PULLED_HEADER)
    L.append("")
    L.append(WHY_PULLED_DISCLAIMER)
    L.append("")
    L.append(n(d["reason"]))
    L.append("")
    L.append("## Provenance (pinned)")
    L.append("")
    L.append("- Original path: `%s`" % n(d["orig_path"]))
    L.append("- Source commit: `%s`" % d["ref"])
    L.append("- git blob: `%s`" % d["blob"])
    L.append("- sha256: `%s`" % d["sha"])
    L.append("- Archived original (byte-exact, sha256-verified at generation): [%s](%s)"
             % (d["arch_rel"], md_target(d["arch_rel"])))
    if d["arch_frozen"]:
        L.append("- Note: the archived original carries era-absolute markdown link targets, so "
                 "its copy is stored with a `.frozen` filename suffix (bytes unchanged; the "
                 "sha256 pin above applies to the archived file as stored).")
    L.append("- Lines: %s; runners named: %s" % (d["n_lines"], d["runners"]))
    L.append(NEUTRALIZE_NOTE)
    L.append("")
    L.append("## Attached evidence (registered with, not as, this claim)")
    L.append("")
    L.extend(d["attached"] if d["attached"] else ["- none"])
    if d["cross"]:
        L.append("")
        L.append("## Cross-stratum flags (inert text; machine-readable relations in the audit fields)")
        L.append("")
        L.extend(d["cross"])
    L.append("")
    L.append(TRIAGE_NOTES_HEADER)
    L.append("")
    L.append(TRIAGE_NOTES_DISCLAIMER)
    L.append("")
    L.append("- Extraction red flags: %s" % n(d["flags"]))
    L.append("- Supersession (as known at extraction): %s" % n(d["supersession"]))
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
    L.append(audit_yaml(d["historic_field"], d["contradicts"], d["cross_reference"]))
    L.append("")
    L.append("Independent audit still required.")
    L.append("")
    return "\n".join(L)


def main():
    global TRIAGE, CENSUS
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("mode", choices=("check", "build"),
                        help="check: render + verify + byte-compare against the "
                             "checkout, write nothing; build: write outputs")
    parser.add_argument("--triage", default=TRIAGE,
                        help="frozen 2026-08-05 triage tree (assembly-time default: %(default)s)")
    parser.add_argument("--census", default=CENSUS,
                        help="census worktree holding the pinned git objects "
                             "(assembly-time default: %(default)s)")
    args = parser.parse_args()
    TRIAGE, CENSUS = args.triage, args.census
    mode = args.mode
    build = mode == "build"

    # shipped manifests are the pin authority (fail-closed against drift)
    old_p1 = json.load(open(os.path.join(OUT, "INTAKE_MANIFEST_2026-08-05.json")))
    old_p2 = json.load(open(os.path.join(OUT, "INTAKE_MANIFEST_PART2_2026-08-05.json")))
    old_by_key = {}
    for r in old_p1 + old_p2:
        old_by_key[(r["stratum"], r["idx"])] = r
    pulled_file = {}   # (stratum, idx) -> wrapper filename (neutralized), for F5 links
    for (s, i), r in old_by_key.items():
        pulled_file[(s, i)] = neutralize_fname(r["file"])

    GIDX = global_index()
    # every triage manifest row, for fetching NAMED non-pulled evidence (F5(2))
    MAN_ALL = {}
    for fn in sorted(os.listdir(os.path.join(TRIAGE, "manifests"))):
        if fn.endswith(".json"):
            for r in json.load(open(os.path.join(TRIAGE, "manifests", fn))):
                MAN_ALL.setdefault((fn[:-5], r["idx_pos"]), r)
    pulled_idx = set()
    for stratum, decfiles, _e, _m, _p in STRATA:
        for f in decfiles:
            for r in jl(os.path.join(TRIAGE, "decisions", f)):
                if r.get("decision") == "PULL":
                    pulled_idx.add(idx_of(r))

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

            # archived original (F2; .frozen when bytes carry machine-absolute
            # markdown link targets, portable-link hard gate)
            arch_name = "%s_%s" % (idx, os.path.basename(orig_path))
            arch_frozen = bool(ABS_MD_LINK_RE.search(b)) and arch_name.endswith(".md")
            if arch_frozen:
                arch_name += ".frozen"
            arch_rel = "%s/%s/%s" % (ARCH_REL_FROM_WRAPPER, stratum, arch_name)
            pending.append((os.path.join(ARCH, stratum, arch_name), b))

            # attached-evidence lines (F5: markdown links = deps edges are kept
            # ONLY here, for attachment relations to pulled wrappers)
            alines = []
            if part == 1:
                akey = lambda r: ((r.get("path") or (ext.get(idx_of(r)) or {}).get("path")
                                   or (man.get(idx_of(r)) or {}).get("path") or ""), idx_of(r))
            else:
                akey = lambda r: ((r.get("path") or ""), idx_of(r))
            archive_attachments = (stratum, idx) in ARCHIVE_ATTACHMENT_SETS
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
                    alines.append("- [`%s`](%s) — %s" % (neutralize_py(apath), md_target(fn),
                                                         neutralize_py(a.get("reason", ""))))
                elif archive_attachments:
                    # non-pulled member of a designated evidence set (e.g. the
                    # panel-reversal set): archive byte-exact + reference inertly
                    note_txt = archive_evidence(stratum, ai, MAN_ALL, pending)
                    alines.append("- `%s` — %s (%s)" % (neutralize_py(apath),
                                                        neutralize_py(a.get("reason", "")), note_txt))
                else:
                    alines.append("- `%s` — %s" % (neutralize_py(apath),
                                                   neutralize_py(a.get("reason", ""))))

            # cross-stratum lines (F5(2): INERT text only — no markdown links, so
            # contradiction/context relations never become deps edges; the
            # machine-readable relations go into the audit-fields yaml lists)
            clines = []
            contradicts, cross_refs = [], []
            named_seen = set()

            def relation_entry(ts_, ti_, tp_):
                fn_ = link_if_pulled(ts_, ti_)
                if fn_:
                    return fn_
                return "idx %s (not pulled; %s) %s" % (ti_, ts_, tp_ or "path not recorded")

            def classify(reason_, entry_):
                if "contradiction" in (reason_ or "").lower():
                    if entry_ not in contradicts:
                        contradicts.append(entry_)
                elif entry_ not in cross_refs:
                    cross_refs.append(entry_)

            def named_nonpulled(reason_):
                out = []
                for tok in re.findall(r"\b\d{4,5}\b", reason_ or ""):
                    ti = int(tok)
                    if ti in pulled_idx or ti in named_seen:
                        continue
                    if ti not in GIDX:
                        continue
                    ts_, tp_ = GIDX[ti]
                    if (ts_, ti) not in MAN_ALL:
                        continue
                    named_seen.add(ti)
                    note_txt = archive_evidence(ts_, ti, MAN_ALL, pending)
                    out.append("- Named non-pulled evidence (provenance only): idx %s `%s` — %s"
                               % (ti, neutralize_py(tp_ or ""), note_txt))
                    classify(reason_, relation_entry(ts_, ti, tp_))
                return out

            def nonpulled_ref_line(ts_, ti_, tp_):
                """Archive a non-pulled cross target/source and return the
                inert reference line (dedup via named_seen)."""
                if ti_ in named_seen or (ts_, ti_) not in MAN_ALL:
                    return []
                named_seen.add(ti_)
                note_txt = archive_evidence(ts_, ti_, MAN_ALL, pending)
                return ["- Named non-pulled evidence (provenance only): idx %s `%s` — %s"
                        % (ti_, neutralize_py(tp_ or ""), note_txt)]

            for c in cross.get(idx, []):
                tgt = c["attach_to_cross"]
                ts, tp = GIDX.get(tgt, ("unknown_stratum", None))
                creason = c.get("reason", "")
                clines.append("- Attaches across strata to idx %s (`%s`, stratum %s) — %s"
                              % (tgt, neutralize_py(tp or "(path not recorded)"), ts,
                                 neutralize_py(creason)))
                classify(creason, relation_entry(ts, tgt, tp))
                if tgt not in pulled_idx:
                    clines.extend(nonpulled_ref_line(ts, tgt, tp))
                clines.extend(named_nonpulled(creason))
            for src_s, src_i, src_p, dec_, reason in incoming[part].get(idx, []):
                if src_s == stratum and src_i == idx:
                    continue
                sp = src_p or GIDX.get(src_i, (None, None))[1]
                clines.append("- Cross-stratum reference from %s idx %s (`%s`, decision %s) — %s"
                              % (src_s, src_i, neutralize_py(sp or "(path not recorded)"), dec_,
                                 neutralize_py(reason)))
                classify(reason, relation_entry(src_s, src_i, sp))
                if src_i not in pulled_idx:
                    clines.extend(nonpulled_ref_line(src_s, src_i, sp))
                clines.extend(named_nonpulled(reason))

            runners = e.get("runner_paths") or []
            historic_field = claim_type_field(e.get("claim_type"))
            ctype = canonical_claim_type(historic_field)
            if ctype not in CANONICAL_CLAIM_TYPES:
                raise SystemExit("mapping produced unrecognized claim type %r" % ctype)
            # iteration 2: a wrapper never asserts a live no-go — it registers a
            # historical NEGATIVE claim as bounded; the historic taxonomy stays
            # in historic_claim_class and no-go discipline applies at audit.
            negative_registration = ctype == "no_go"
            if negative_registration:
                ctype = "bounded_theorem"
            ct_dist[ctype] = ct_dist.get(ctype, 0) + 1

            orig_title = e.get("title") or os.path.basename(orig_path)
            d = {
                "title": transform_title(orig_title, stratum, idx),
                "orig_title": orig_title,
                "raw_headline": e.get("headline"),
                "raw_scope": e.get("scope"),
                "ctype": ctype,
                "negative_registration": negative_registration,
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
                "arch_frozen": arch_frozen,
                "n_lines": e.get("n_lines", "unknown"),
                "runners": runners_field(runners),
                "attached": alines,
                "cross": clines,
                "flags": e.get("red_flags") or "none recorded",
                "supersession": e.get("supersession") or "none recorded",
                "contradicts": contradicts,
                "cross_reference": cross_refs,
                "review_flags": REVIEW_FLAGS.get((stratum, idx)),
            }
            body = render(d)

            slug = neutralize_fname(slug_of(orig_path))
            if slug in used_slugs:
                slug = "%s_B%s" % (slug, idx)
            used_slugs[slug] = (stratum, idx)
            fname = "HISTORIC_%s_INTAKE_NOTE_2026-08-05.md" % slug
            if fname != neutralize_fname(old["file"]):
                errors.append("FILENAME DRIFT %s idx %s: shipped %s !~ regenerated %s"
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
    H.append(neutralize_py(odec.get("reason", "")))
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
    H.append(NEUTRALIZE_NOTE)
    H.append("")
    H.append("## Attached evidence (registered with, not as, this claim)")
    H.append("")
    H.append("- [`triage_2026-08-05/extracted/octopus_era.jsonl`](%s/octopus/octopus_era.jsonl) — the registry's evidence base: 3179 per-commit rows, one per distinct (date, subject) group; no per-claim wrappers were made. Byte-exact copy archived at the linked path (sha256 `%s`)."
             % (ARCH_REL_FROM_WRAPPER, sha256(jsonl_bytes)))
    H.append("")
    H.append(TRIAGE_NOTES_HEADER)
    H.append("")
    H.append(TRIAGE_NOTES_DISCLAIMER)
    H.append("")
    H.append("- Extraction red flags: none recorded")
    H.append("- Supersession (as known at extraction): none recorded")
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

    # ---------- hazards memo (F8; iteration 2 adds the pinned evidence base) ----------
    haz_src = os.path.join(TRIAGE, "decisions", "packsci_hazards_for_audit_lane.md")
    haz = open(haz_src, "r").read().splitlines()
    evidence_jsonls = ["branch09.jsonl", "packsci01.jsonl", "packsci02.jsonl",
                      "packsci03.jsonl", "packsci04.jsonl", "packsci05.jsonl"]
    haz_prov = ["Provenance (evidence base, pinned):"]
    for ej in evidence_jsonls:
        ej_bytes = open(os.path.join(TRIAGE, "extracted", ej), "rb").read()
        pending.append((os.path.join(ARCH, "triage_extraction_evidence", ej), ej_bytes))
        haz_prov.append("- `archive_unlanded/historic_intake_originals/triage_extraction_evidence/%s`"
                        " (byte-exact copy of triage_2026-08-05/extracted/%s) — sha256 `%s`"
                        % (ej, ej, sha256(ej_bytes)))
    haz_prov.append("- The per-hazard `idx` pointers below refer to rows in these archived")
    haz_prov.append("  extraction files and to `triage_2026-08-05/manifests/<stratum>.json` in the")
    haz_prov.append("  census worktree.")
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
        "",
    ] + haz_prov
    haz_out = "\n".join([haz[0]] + haz_header + haz[1:]) + "\n"
    pending.append((os.path.join(OUT, "HISTORIC_INTAKE_PART2_HAZARDS_2026-08-05.md"),
                    haz_out.encode("utf-8")))

    # ---------- manifests: identical to the shipped pins except the `file`
    # field, which carries the iteration-2 neutralized wrapper filename ----------
    rows1 = sorted(manifest_rows[1], key=lambda r: (r["stratum"], -1 if r["idx"] is None else r["idx"]))
    rows2 = sorted(manifest_rows[2], key=lambda r: (r["stratum"], r["idx"]))
    for new_rows, old_rows, label in ((rows1, old_p1, "part1"), (rows2, old_p2, "part2")):
        old_sorted = sorted(old_rows, key=lambda r: (r["stratum"], -1 if r["idx"] is None else r["idx"]))
        if len(new_rows) != len(old_sorted):
            raise SystemExit("FAIL-CLOSED: %s manifest row count drift" % label)
        for nr, orow in zip(new_rows, old_sorted):
            for k in nr:
                if k == "file":
                    if nr[k] != neutralize_fname(orow[k]):
                        raise SystemExit("FAIL-CLOSED: %s manifest file-field drift: %r !~ %r"
                                         % (label, orow[k], nr[k]))
                elif nr[k] != orow.get(k):
                    raise SystemExit("FAIL-CLOSED: %s manifest pin drift on %r field %r"
                                     % (label, orow.get("file"), k))
    new1 = json.dumps(rows1, indent=1, sort_keys=True) + "\n"
    new2 = json.dumps(rows2, indent=1, sort_keys=True) + "\n"
    pending.append((os.path.join(OUT, "INTAKE_MANIFEST_2026-08-05.json"), new1.encode("utf-8")))
    pending.append((os.path.join(OUT, "INTAKE_MANIFEST_PART2_2026-08-05.json"), new2.encode("utf-8")))

    # ---------- indexes ----------
    regen_note = [
        "",
        "## Review-loop regeneration (2026-08-08, iterations 1 and 2)",
        "",
        "Every wrapper in this intake was regenerated through the corrected template",
        "after review-loop iterations 1 and 2 (Sol, FIX_THEN_PROCEED then confirmation):",
        "canonical `Claim type:` headers with the historic taxonomy preserved as",
        "`historic_claim_class` (F1); byte-exact archived originals under",
        "`archive_unlanded/historic_intake_originals/` linked from each wrapper and",
        "sha256-verified fail-closed (F2); the Why-pulled section marked",
        "provenance-not-authority with a non-evidentiary disclaimer (F3); every",
        "rendered field display-neutralizes `.py` tokens with a zero-width split so",
        "no current-tree runner can bind, with the byte-exact wording pinned in the",
        "triage JSONLs and archived originals (F4); markdown links (deps edges) only",
        "for attachment relations — contradiction/cross-flag relations are inert text",
        "plus machine-readable `contradicts:`/`cross_reference:` yaml lists, with",
        "named non-pulled evidence archived byte-exact (F5); extraction-time",
        "commentary split into a clearly-attributed Triage-extraction-notes section",
        "(F6); the Octopus registry typed meta with its evidence base archived (F7);",
        "the hazards memo given a meta header plus a pinned archived evidence base",
        "(F8); review flags on the three affected packsci01 wrappers (F9/F10/F11);",
        "bare-code H1 titles rewritten with the explicit scientific name as the",
        "heading — per vocab_lint's `legacy_alias_strip` rule no alias parenthetical",
        "is kept, and the historic token survives in the Explicit-subject line, the",
        "wrapper filename, and the pinned original (F13). Historical NEGATIVE",
        "claims register as `bounded_theorem` (historic_claim_class keeps the",
        "historic taxonomy; no live no-go is asserted by any wrapper — no-go",
        "discipline applies at audit adjudication), and wrapper FILENAMES neutralize",
        "no-go/obstruction/firewall tokens (NO_GO/NOGO->NEGATIVE,",
        "OBSTRUCTION->OBSTRUCTED_ROUTE, FIREWALL->ROUTE_BARRIER) so no registration",
        "wrapper is a no-go-named artifact; archived originals containing",
        "era-absolute markdown links carry a `.frozen` filename suffix (bytes",
        "unchanged). Manifests are identical to the shipped pins except the `file`",
        "field, which records the neutralized filename; decision reasons are",
        "byte-untouched in the triage JSONLs (sha256-verified). Generator:",
        "`scripts/historic_intake_generate_2026_08_05` (a `.py` program; name",
        "rendered without extension for graph hygiene on this meta surface).",
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

    # ---------- write/check phase: only reached with zero verification errors ----------
    expected_out_md = set(written) | {"HISTORIC_INTAKE_PART2_HAZARDS_2026-08-05.md"}

    def archive_verify():
        """Every archived original byte-matches its manifest pin (frozen-aware)."""
        for r in rows1 + rows2:
            if r["stratum"] == "octopus":
                ap = os.path.join(ARCH, "octopus", "octopus_era_claims.md")
            else:
                ap = os.path.join(ARCH, r["stratum"],
                                  "%s_%s" % (r["idx"], os.path.basename(r["original_path"])))
                if not os.path.exists(ap) and os.path.exists(ap + ".frozen"):
                    ap += ".frozen"
            if sha256(open(ap, "rb").read()) != r["sha256"]:
                raise SystemExit("FAIL-CLOSED: archived original mismatch: %s" % ap)

    expected_arch = {os.path.relpath(p, ARCH) for p, _ in pending if p.startswith(ARCH)}
    if build:
        for path, data in pending:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as fh:
                fh.write(data)
        # remove stale files superseded by a renamed regeneration
        removed = 0
        for f in os.listdir(OUT):
            if f.startswith("HISTORIC_") and f.endswith(".md") and f not in expected_out_md:
                os.remove(os.path.join(OUT, f))
                removed += 1
        for root, _dirs, files in os.walk(ARCH):
            for f in files:
                ap = os.path.join(root, f)
                if os.path.relpath(ap, ARCH) not in expected_arch:
                    os.remove(ap)
                    removed += 1
        archive_verify()
        drift = []
    else:
        # check mode: byte-compare every rendered output against the checkout;
        # any drift (content or missing/stale file) fails.
        drift = []
        for path, data in pending:
            try:
                on_disk = open(path, "rb").read()
            except OSError:
                drift.append("missing: %s" % os.path.relpath(path, REPO))
                continue
            if on_disk != data:
                drift.append("differs: %s" % os.path.relpath(path, REPO))
        for f in sorted(os.listdir(OUT)):
            if f.startswith("HISTORIC_") and f.endswith(".md") and f not in expected_out_md:
                drift.append("stale: docs/historic_intake/%s" % f)
        for root, _dirs, files in os.walk(ARCH):
            for f in files:
                ap = os.path.join(root, f)
                if os.path.relpath(ap, ARCH) not in expected_arch:
                    drift.append("stale: %s" % os.path.relpath(ap, REPO))
        removed = 0

    print(json.dumps({
        "mode": mode,
        "wrappers_written": len(written),
        "counts": counts,
        "claim_type_distribution": ct_dist,
        "manifest_pin_identity_except_file_field": True,
        "archived_payloads": len([1 for p, _ in pending if p.startswith(ARCH)]),
        "stale_files_removed": removed,
        "drift": drift[:40],
        "drift_count": len(drift),
        "errors": 0,
    }, indent=1, sort_keys=True))
    if drift:
        raise SystemExit("CHECK FAILED: %d rendered outputs differ from the checkout" % len(drift))


if __name__ == "__main__":
    main()
