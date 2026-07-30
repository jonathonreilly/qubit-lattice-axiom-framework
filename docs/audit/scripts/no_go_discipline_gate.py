#!/usr/bin/env python3
"""Shared No-Go Discipline packet construction and validation.

The gate binds every N1-N8 statement to evidence visible in the restricted
audit packet.  It does not try to prove semantic correctness mechanically; it
does prevent empty prose, synthetic route counting, unsupported prior-authority
claims, unresolved steelmen, and failed checklists from authorizing a clean
negative verdict.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
from itertools import combinations
from pathlib import Path
from typing import Any


RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}

# Publication-strength rank, mirroring compute_effective_status.RANK. This
# module is a leaf import for the whole audit lane (apply, invalidate, queue,
# lint, orchestrators), so it deliberately does not import the pipeline stage
# that owns the canonical table. `test_snapshot_status_rank_matches_pipeline`
# asserts the two tables agree, so the copy cannot drift silently.
SNAPSHOT_STATUS_RANK = {
    "retained": 100,
    "retained_no_go": 100,
    "retained_bounded": 95,
    "retained_pending_chain": 80,
    "open_gate": 40,
    "unaudited": 30,
    "audit_in_progress": 30,
    "meta": 25,
    "audited_decoration": 20,
    "audited_numerical_match": 15,
    "audited_renaming": 10,
    "audited_conditional": 10,
    "audited_failed": 0,
}


def snapshot_status_rank(status: str | None) -> int:
    """Rank a manifest authority's effective_status for drift comparison."""
    if isinstance(status, str) and status.startswith("decoration_under_"):
        return 70
    return SNAPSHOT_STATUS_RANK.get(status or "unaudited", -1)


def snapshot_status_is_chain_satisfying(status: str | None) -> bool:
    """Mirror compute_effective_status.is_chain_satisfying_status.

    Same leaf-module reasoning as SNAPSHOT_STATUS_RANK: this file is imported
    by apply, invalidate, queue, lint and the orchestrators, so it does not
    import the pipeline stage that owns the canonical predicate.
    `test_snapshot_chain_satisfying_matches_pipeline` pins the two together.
    """
    if status in RETAINED_GRADE or status == "meta":
        return True
    return isinstance(status, str) and status.startswith("decoration_under_")


# Authenticated-evidence snapshot contract. The tag and the required entry
# fields must move together: `test_evidence_snapshot_writer_satisfies_reader`
# fails if `build_evidence_snapshot` ever stops emitting a field the reader
# demands. Expanding the required set without that guard is what silently
# voided every stored no-go snapshot on 2026-07-11.
EVIDENCE_SNAPSHOT_SCHEMA = "no_go_evidence_snapshot_v1"
EVIDENCE_SNAPSHOT_ENTRY_REQUIRED_FIELDS = frozenset(
    {
        "roles",
        "content_sha256",
        "verified_locators",
        "verified_values",
        "phrase_occurrences",
        "full_phrase_groups",
    }
)


PRIOR_AUTHORITY_PREMISE_TYPES = {
    "axiom_or_approved_primitive",
}
ROUTE_CLASSES = {
    "algebraic_rearrangement",
    "symmetry_or_representation",
    "alternate_carrier_or_sector",
    "boundary_or_initial_condition",
    "normalization_or_units",
    "dynamical_or_effective_action",
    "lattice_scale_or_limit",
    "numerical_or_finite_case",
    "convention_or_relabeling",
    "alternate_observable_or_readout",
    "topology_or_global_structure",
    "dependency_or_registry_reclassification",
}
ROUTE_CLASS_MARKERS = {
    "algebraic_rearrangement": re.compile(r"\b(?:algebra|identity|rearrang|factor|cancel|solve)\w*\b", re.I),
    "symmetry_or_representation": re.compile(r"\b(?:symmetr|invarian|represent|commut|character|irrep|group)\w*\b", re.I),
    "alternate_carrier_or_sector": re.compile(
        r"\b(?:alternate\s+)?(?:carriers?|sectors?|modules?|spaces?|irreps?)\b",
        re.I,
    ),
    "boundary_or_initial_condition": re.compile(r"\b(?:boundary|initial|background|state|pointwise)\w*\b", re.I),
    "normalization_or_units": re.compile(
        r"\b(?:normaliz\w*|units?|scale\w*|dimensionful\w*)\b", re.I
    ),
    "dynamical_or_effective_action": re.compile(r"\b(?:dynamic|effective|action|evolution|equivariant\s+family)\w*\b", re.I),
    "lattice_scale_or_limit": re.compile(r"\b(?:lattice|continuum|limit|finite[- ]size|asymptotic|approximate)\w*\b", re.I),
    "numerical_or_finite_case": re.compile(r"\b(?:numeric|finite|sample|scan|compute)\w*\b", re.I),
    "convention_or_relabeling": re.compile(r"\b(?:convention|relabel|rename|basis\s+label)\w*\b", re.I),
    "alternate_observable_or_readout": re.compile(r"\b(?:observable|readout|nonlinear|spectrum|eigenvalue)\w*\b", re.I),
    "topology_or_global_structure": re.compile(r"\b(?:topolog|global|bundle|homotop|cohomolog)\w*\b", re.I),
    "dependency_or_registry_reclassification": re.compile(r"\b(?:dependency|registry|reclassif|premise|authority)\w*\b", re.I),
}
DEMOTIONS = {
    "partial-attempt-with-named-untested-routes",
    "partial-narrowing",
    "bounded-with-corrected-wall-count",
    "stretch-attempt-with-honest-residual",
}
NON_CLEAN_VERDICTS = {
    "audited_conditional",
    "audited_renaming",
    "audited_failed",
    "audited_numerical_match",
}
HONESTY_MARKERS = {"ATTEMPTED", "RULED OUT BY PRIOR"}
# The five assertion classes of the no-go-discipline policy's
# "When to invoke" list (docs/ai_methodology/skills/no-go-discipline/
# SKILL.md; registered in docs/repo/controlled_vocabulary.yaml under
# negative_assertion_classes). Every incoming audit must declare which classes
# the artifact ASSERTS (empty list when none). The declaration is the
# auditor's semantic judgment after reading the full note; the regex
# trigger below is only a mechanical floor. Either surface requires the
# N1-N8 packet.
POLICY_NEGATIVE_CLASSES = {
    "no_go_result",
    "stretch_attempt_negative",
    "bounded_with_named_walls",
    "derived_no_go_boundary",
    "conditional_wall_rationale",
}
ROUTE_DISPOSITIONS = {"CLOSED", "OPEN", "UNTESTED"}
W_UNIT_NEAR_MARKER_RE = re.compile(
    r"(?i)W_+unit(?:(?!W_+unit)[^\W_])*"
)
W_UNIT_LITERAL_RE = re.compile(r"W_units?", re.IGNORECASE)


def _is_marker_word_extension(character: str) -> bool:
    """Return whether ``character`` continues a forensic marker token."""
    return character.isalnum() or unicodedata.category(character).startswith("M")


def _has_exact_w_unit_marker(route_semantics: str) -> bool:
    """Match W_unit(s) across separators without admitting pinned lookalikes."""
    for match in W_UNIT_LITERAL_RE.finditer(route_semantics):
        if match.start() and _is_marker_word_extension(route_semantics[match.start() - 1]):
            continue
        if match.end() < len(route_semantics) and _is_marker_word_extension(
            route_semantics[match.end()]
        ):
            continue
        if (
            match.group(0).casefold() == "w_unit"
            and route_semantics[match.end():].casefold().startswith("_post")
        ):
            continue
        return True
    return False


def route_class_marker_matches(route_class: str, route_semantics: str) -> bool:
    """Match documented route markers across prose and identifier tokens."""
    route_semantics = unicodedata.normalize("NFC", route_semantics)
    marker = ROUTE_CLASS_MARKERS[route_class]
    if (
        route_class == "normalization_or_units"
        and _has_exact_w_unit_marker(route_semantics)
    ):
        return True
    if marker.search(route_semantics):
        return True
    separator_text = route_semantics
    if route_class == "normalization_or_units":
        separator_text = W_UNIT_NEAR_MARKER_RE.sub(" ", separator_text)
    marker_text = re.sub(r"[_-]+", " ", separator_text)
    return bool(marker.search(marker_text))

PATH_TRIGGER_RE = re.compile(
    r"(?:^|[\s/._-])(?:no[\s_-]?go|obstruction|firewall|negative[\s_-]?boundary|"
    r"no[\s_-]?uniform[\s_-]?sign|stretch[\s_-]?attempt)(?:$|[\s/._-])",
    re.IGNORECASE,
)
NEGATIVE_ASSERTION_RE = re.compile(
    r"\bno[- ]go\b|\b(?:exact|scoped|structural|finite|standalone)?[ -]?negative boundary\b|"
    r"\b(?:dependency|selector|source)[ -]?firewall\b|"
    r"\bfirewall\b[^\n.;:]{0,80}\b(?:remains?|blocks?|prevents?|boundary)\b|"
    r"structurally (?:closed|undecidable)|no (?:admissible )?route exists|"
    r"no retained primitive(?: supplies)?|requires? (?:a )?new axiom|"
    r"\bno derivation of\b[^\n.;:]{0,160}\b(?:from|under)\b|"
    r"\b(?:absence|nonexistence|impossibility|failure|lack)\s+of\b"
    r"[^\n.;:]{0,160}\b(?:route|derivation|selector|closure|solution|carrier|operator)s?\b|"
    r"\bfailure\s+of\s+(?:every|all)\s+(?:route|attempt|construction)s?\b|"
    r"\b(?:non[- ]?derivability|underdetermination|inability|non[- ]?supply|non[- ]?closure)\b|"
    r"\b(?:every|all)\s+(?:attempted\s+)?(?:routes?|attempts?|constructions?)\s+"
    r"remain(?:s)?\s+(?:open|unclosed|unresolved)\b|"
    r"\b(?:the\s+)?(?:selector|source|carrier|route|construction)\s+"
    r"remain(?:s)?\s+underdetermined\b|"
    r"\b(?:residual|named|independent|unclosed|remaining|unresolved) (?:walls?|admissions?)\b|"
    r"\bno derivation of\b[^\n.;:]{0,160}\b(?:from|under)\b|"
    r"\b(?:absence|nonexistence|impossibility|failure|lack)\s+of\b"
    r"[^\n.;:]{0,160}\b(?:route|derivation|selector|closure|solution|carrier|operator)s?\b|"
    r"\bfailure\s+of\s+(?:every|all)\s+(?:route|attempt|construction)s?\b|"
    r"\b(?:every|all)\s+(?:attempted\s+)?(?:routes?|attempts?|constructions?)\s+"
    r"remain(?:s)?\s+(?:open|unclosed|unresolved)\b|"
    r"(?<!does not )(?<!do not )\brules?\s+out\s+(?:every|all)\s+"
    r"(?:candidate\s+)?(?:routes?|attempts?|constructions?|carriers?|selectors?)\b|"
    r"\bunderdetermin(?:e[sd]?|ed|ation)\b|"
    r"\bno\s+(?:admissible\s+|candidate\s+)?(?:selector|source|carrier|route|construction)\s+"
    r"can\s+(?:produce|derive|supply|select|recover|close)\b|"
    r"\ball\s+(?:candidate\s+)?(?:routes?|attempts?|constructions?)\s+fail\b|"
    r"(?:cannot|can not|is not|are not) (?:be )?deriv(?:ed|able)(?: from)?|"
    r"(?:does not|cannot|fails? to|failed to) lift|"
    r"\bthere\s+(?:still\s+)?(?:remains?|persists?)\s+(?:an?\s+)?"
    r"(?:scoped\s+|residual\s+|unresolved\s+)?(?:wall|admission|obstruction)\b|"
    r"\bfails?\s+to\s+(?:close|resolve|remove|discharge|supply|derive|select)\b|"
    r"\b[^\n.;:]{1,80}\s+(?:is|are|was|were)\s+"
    r"(?:blocked|prevented|precluded)\b[^\n.;:]{0,80}\b"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"\b(?:walls?|admissions?|obstructions?)\b[^\n.;:]{0,80}"
    r"\b(?:blocks?|prevents?|precludes?|rules?\s+out|persists?|remains?)\b|"
    r"bounded with named walls|conditional on [^\n]{0,120}\b(?:walls?|admissions?|"
    r"imported selectors?|supplied selectors?|bridges?)\b|"
    r"\b(?:assumes?|assuming) [^\n]{0,120}\b(?:bridge|selector|sector selection|standard QFT)\b|"
    r"\b(?:scoped|structural|bounded|remaining|unresolved) obstruction\b|"
    r"\bobstruction (?:to|rules out|blocks|precludes|prevents)\b|"
    r"no uniform sign|\b(?:route|attempt|construction)\b[^\n]{0,80}\bdoes not close\b|"
    r"(?:^|\n)\s*(?:walls?|admissions?)\s*:",
    re.IGNORECASE,
)
# Check explicit negated closure phrases before removing affirmative closure
# clauses. This handles adverbial forms ("does not fully close"), negative
# perfect/passive forms, and "fails to resolve" without treating affirmative
# tense variants as no-go assertions.
EXPLICIT_NEGATIVE_CLOSURE_RE = re.compile(
    r"\b(?:(?:(?:does|do|did|has|have|had|is|are|was|were)\s+not)|"
    r"cannot|can\s+not)\s+"
    r"(?:(?:yet|still|fully|completely|entirely|exactly|ever|successfully)\s+){0,4}"
    r"(?:close[sd]?|remove[sd]?|resolve[sd]?|discharge[sd]?|suppl(?:y|ies|ied)|"
    r"retire[sd]?|eliminate[sd]?)\b[^\n.;:]{0,100}\b"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"\bfails?\s+"
    r"(?:(?:yet|still|fully|completely|entirely|exactly|ever|successfully)\s+){0,4}"
    r"to\s+(?:(?:fully|completely|entirely|exactly|successfully)\s+){0,3}"
    r"(?:close|remove|resolve|discharge|supply|retire|eliminate)\b"
    r"[^\n.;:]{0,100}\b(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
NEGATIVE_SUBJECT_CLOSURE_RE = re.compile(
    # "no longer claims/asserts ..." is document-history prose; scientific
    # "no longer" predicates are hard-gated above. "zero" is a zero-count
    # determiner only when a plural noun precedes the closure verb
    # ("zero candidate operators determine..."), never a scalar parameter
    # ("at coupling zero the transfer map...", "a zero eigenvalue
    # determines...").
    r"\b(?:(?:no(?!\s+longer\s+(?:\w+ly\s+)?(?:claims?|asserts?|states?|"
    r"reports?|presents?|carries|includes?))|neither|"
    r"(?<!the )(?<!The )zero"
    r"(?!\s+(?:modes?|eigenmodes?|eigenstates?|eigenfunctions?|eigenvalues?|eigenvectors?|crossings?|energy)\b)"
    r"(?=\s+(?:[\w-]+\s+){0,3}"
    r"(?:(?!(?:fixes|closes|determines|derives|selects|supplies|removes|"
    r"resolves|yields|chooses|decides|gives|produces|maps|sets|takes|"
    r"returns|equals|denotes|defines)\b)[\w-]+s"
    # maps/sets/yields/returns read as plural nouns when a distinct
    # closure predicate follows ("zero candidate maps determine ...").
    r"|(?:maps|sets|yields|returns)(?=\s+(?:[\w-]+\s+){0,2}"
    r"(?:determin|select|fix|constrain|supply|suppl|deriv|clos|recover|"
    r"produc|resolv)))\s))\s+"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10}|"
    r"none\s+of\s+(?:the\s+)?"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10}|"
    r"nothing\s+"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|exists?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){0,8})"
    r"(?:(?:can\s+|is\s+able\s+to\s+|are\s+able\s+to\s+)?"
    # "closed <shape>" noun-phrase readings and "fixed point/locus"
    # compounds are excluded; verb readings still gate.
    r"(?:close(?:s|d(?!(?:[\s-]+forms?\b)|(?:(?:[\s-]+[a-z-]+){1,2}s?\b"
    r"(?=\s+(?:is|are|was|were|appears?|emerges?|arises?|enters?|"
    r"exists?|remains?|follows?|closes?|contributes?|forms?|lies?|sits?)\b))))?|"
    r"remove[sd]?|resolve[sd]?|discharge[sd]?|suppl(?:y|ies|ied)|"
    r"derive[sd]?|select[sd]?|determine[sd]?|"
    r"fix(?:es)?(?!-)|fixed(?!-)(?![\s]+(?:points?|locus|loci|backgrounds?|"
    r"surfaces?|charts?)\b(?!\s+(?:on|in|of|across|under|through|over)\b))(?!(?:[\s-]+[a-z-]+){1,2}s?\b(?=\s+(?:is|are|"
    r"was|were|appears?|emerges?|arises?|enters?|exists?|remains?|"
    r"follows?|contributes?|forms?|lies?|sits?)\b))|retire[sd]?|"
    r"eliminate[sd]?)|succeeds?\s+in\s+"
    r"(?:closing|removing|resolving|discharging|supplying|deriving|selecting|"
    r"determining|fixing|retiring|eliminating))\b",
    re.IGNORECASE,
)
NO_EXISTENCE_ASSERTION_RE = re.compile(
    r"\bno\s+(?!longer\s+(?:\w+ly\s+)?(?:claims?|asserts?|states?|reports?|"
    r"presents?|carries|includes?)\b)(?P<subject>"
    r"(?:(?!(?:because|although|but|while|once|when|after|before|if|and|so|since|as|whereas|"
    r"is|are|was|were|has|have|had|remains?|required?|needed|introduced)\b)"
    r"[\w-]+\s+){1,10})exist(?:s)?\b",
    re.IGNORECASE,
)
BOUNDARY_ABSENCE_SUBJECT_RE = re.compile(
    r"\b(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
INABILITY_CLOSURE_RE = re.compile(
    r"\b(?:is|are|was|were|remains?)\s+"
    r"(?:(?:still|wholly|completely|entirely)\s+){0,3}unable\s+to\s+"
    r"(?:close|remove|resolve|discharge|supply|derive|select|determine|fix|retire|"
    r"eliminate)\b[^\n.;:]{0,100}\b"
    r"(?:walls?|admissions?|obstructions?|selectors?|boundar(?:y|ies))\b",
    re.IGNORECASE,
)
BOUNDARY_SUBJECT_NEGATIVE_RE = re.compile(
    r"\b(?:the\s+|an?\s+|this\s+|that\s+)?"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|selectors?|boundar(?:y|ies))\s+"
    r"(?:(?:cannot|can\s+not)\s+be\s+|"
    r"(?:is|are|was|were|has|have|had)\s+not\s+(?:been\s+)?)"
    r"(?:closed|removed|resolved|discharged|supplied|derived|selected|determined|"
    r"fixed|retired|eliminated)\b",
    re.IGNORECASE,
)
# Remove only clauses that affirmatively close or supply the named boundary.
# This keeps "does not close the remaining obstruction" live while excluding
# "closes the remaining obstruction" and passive equivalents.
POSITIVE_BOUNDARY_CLOSURE_RE = re.compile(
    r"(?<!not )(?<!never )\b(?:closes?|closed|removes?|removed|discharges?|discharged|"
    r"supplies?|supplied|resolves?|resolved|retires?|retired|eliminates?|eliminated|"
    r"answers?|answered|overcomes?|overcame)\b\s+(?:all\s+|every\s+|each\s+|both\s+|its\s+|the\s+|an?\s+|"
    r"explicitly\s+)?(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b|"
    r"(?<!neither )(?<!no )\b(?:all\s+|the\s+|an?\s+)?(?:residual\s+|remaining\s+|scoped\s+|"
    r"unresolved\s+)?(?:walls?|admissions?|obstructions?|boundar(?:y|ies))\b"
    r"[^\n.;:]{0,50}\b(?:is|are|was|were|has\s+been|have\s+been|had\s+been)\s+"
    r"(?:explicitly\s+)?"
    r"(?:closed|removed|discharged|supplied|resolved|retired|eliminated)\b",
    re.IGNORECASE,
)
# ---------------------------------------------------------------------------
# Honest-scoping exemption architecture (trigger-precision repair).
#
# The no-go-discipline policy's "When to invoke" list gates artifacts that
# ASSERT a negative outcome. The mandated honest-scoping template ("this
# note does not derive X - carried by separate rows", "## What this does
# NOT claim" fragments, labeled "Is not:" bullets) states coverage routing,
# not a framework boundary, and is exempt from the bare coverage-verb
# check below - subject to an authority-payload veto: the proposition, not
# the placement, decides. Everything in the hard assertion set above gates
# everywhere, including inside disclaimer surfaces. The regex layer is a
# mechanical floor; the auditor's mandatory negative-class declaration
# (validated in apply_audit) is the semantic authority on assertion.
# ---------------------------------------------------------------------------
NEGATIVE_COVERAGE_VERB_RE = re.compile(
    r"\b(?:cannot|can\s+not|does\s+not|do\s+not)\s+"
    r"(?:select|orient|factor|factorize|derive|supply|"
    r"determine|fix|close|produce|recover)\b",
    re.IGNORECASE,
)
AUTHORITY_PAYLOAD_RE = re.compile(
    r"\b(?:axioms?|primitives?|postulates?|premises?|premise\s+set|"
    r"framework|admissibility|"
    r"baseline\s+(?:structure|postulates?|premises?|axioms?|package|rules?)|"
    r"foundational\s+package|minimal\s+axioms|"
    r"retained\s+(?:axioms?|primitives?|framework|structure|inputs?|"
    r"premises?|postulates?|sector|authority|routes?|surface)|"
    r"records?\s*,?\s+(?:alone|by\s+itself|content|data|order)|"
    r"(?:approved|accepted|baseline|named|supplied|registered|admitted)\s+"
    r"(?:premises?|postulates?|assumptions?|principles?|axioms?|primitives?)|"
    r"(?:qubit|lattice|admissibility|record)(?:\s*,\s*"
    r"(?:qubit|lattice|admissibility|record))*\s+and\s+"
    r"(?:qubit|lattice|admissibility|record)|"
    r"in\s+principle)\b"
    r"|\b(?:from|under|within|using|given|on|with(?:\s+only)?|by\s+use\s+of|"
r"via|through)\s+(?:the\s+|any\s+|all\s+|only\s+|"
    r"every\s+|its\s+|these\s+|those\s+)?(?:[\w-]+\s+){0,4}"
    r"(?:postulates?|premises?|axioms?|primitives?|structure|baseline|"
    r"package|framework|foundations?|assumptions?|principles?)\b",
    re.IGNORECASE,
)
NOTE_SUBJECT_DISCLAIMER_RE = re.compile(
    r"\b(?:this|that|the(?:\s+(?:present|current))?)\s+"
    r"(?:[\w-]+\s+){0,5}"
    r"(?:note|companion|appendix|document|section|table|readme|write-?up)\s+"
    r"(?:alone\s+|by\s+itself\s+|also\s+|deliberately\s+|explicitly\s+|"
    r"intentionally\s+|therefore\s+|thus\s+|still\s+|currently\s+)*"
    r"(?:does\s+not|do\s+not|did\s+not|cannot|can\s+not|will\s+not)\b"
    r"(?:(?!\s+(?:and|but|nor|yet|while|whereas)\s)(?:[^\n.;:,?!\u2014]|\.(?=\d))){0,160}",
    re.IGNORECASE,
)
LABELED_DISCLAIMER_LINE_RE = re.compile(
    r"(?im)^(?P<label>[ \t]*(?:>[ \t]*)?(?:[-*+]|\d+(?:[.):]|\s*[-\u2013\u2014])?(?:\s*[-\u2013\u2014])?)?[ \t]*"
    r"(?:what\s+(?:this|it)\s+is\s+not|is\s+not|does\s+not|not\s+claimed|"
    r"non-?claims?|deliberately\s+not\s+claimed|out\s+of\s+scope)"
    r"\s*[:\u2014-])(?P<payload>[^\n]*)$",
)
DISCLAIMER_HEADING_RE = re.compile(
    r"(?:what\s+this\b.*\bdoes\s+not\b|what\s+this\s+note\b.*\bdoes\s+not\b|"
    r"what\s+remains\b|does\s+not\b|not\s+claimed\b|non-?claims?\b|"
    r"non-?goals?\b|(?:claim\s+)?scope\b|limitations?\b|caveats?\b|"
    r"out[-\s]of[-\s]scope\b|"
    r"honest\b|open\s+(?:items?|questions?|problems?)\b|"
    r"boundar(?:y|ies)\b(?!\s+conditions?)|out\s+of\s+scope\b|safe\s+read\b)",
    re.IGNORECASE,
)
MARKDOWN_HEADING_RE = re.compile(r"(?m)^[ \t]{0,3}(#{1,6})\s+(.*)$")
DISCLAIMER_FRAGMENT_LINE_RE = re.compile(
    r"^[ \t]*(?:(?:[-*+]|\d+(?:[.):]|\s*[-\u2013\u2014])?)[ \t]*)?"
    r"(?:does\s+not|do\s+not|did\s+not|cannot|can\s+not|is\s+not|are\s+not|"
    r"not|no)\b",
    re.IGNORECASE,
)
UNIQUENESS_SUBJECT_RE = re.compile(
    r"\s*(?:[\w-]+\s+){0,5}(?:other|second|additional|alternative|further)\b",
    re.IGNORECASE,
)
AUTHORITY_UNIQUENESS_SUBJECT_RE = re.compile(
    r"(?:routes?|derivations?|attempts?|constructions?|mechanisms?|arguments?|"
    r"ways?|avenues?|strateg(?:y|ies)|approach(?:es)?|procedures?|schemes?|"
    r"options?|"
    r"methods?|paths?|closures?|proofs?|selectors?|carriers?|axioms?|"
    r"primitives?|admissions?|witness(?:es)?|suppliers?|bridges?|lifts?|"
    r"authorit(?:y|ies))",
    re.IGNORECASE,
)
BOUNDARY_REMOVED_TEMPORAL_RE = re.compile(
    r"\b(?:walls?|admissions?|obstructions?)\s+(?:\w+\s+){0,2}no\s+longer\s+"
    r"(?:exists?|remains?|persists?|applies|holds?|blocks?)\b(?:[^.;:,\n]|,(?=\s*(?:but|and|yet)\s))*",
    re.IGNORECASE,
)
CONTRACTION_RE = re.compile(
    r"\b(do|does|did|could|would|should|has|have|had|is|are|was|were|need)"
    r"n[\u2019']t\b",
    re.IGNORECASE,
)
CANT_RE = re.compile(r"\bcan[\u2019']t\b", re.IGNORECASE)
# Explicit negation, withdrawal, denial, and refutation of a negative
# predicate is not a negative assertion. These scrub before the hard-set
# search; affirmative forms ("the phase is underdetermined", "asserts
# that the phase is underdetermined") are untouched.
NEGATED_PREDICATE_PRESCRUBS = (
    re.compile(
        r"\b(?:is|are|was|were)\s+(?:\w+ly\s+)?not\s+(?:\w+ly\s+)?"
        r"(?:underdetermined|undetermined|unspecified|impossible|incapable|"
        r"insufficient|unliftable|unavailable|unobtainable|unclosed)\b",
        re.IGNORECASE,
    ),
    re.compile(r"\b(?:does|do|did)\s+not\s+lack\b"
        r"(?:(?!\s+(?:but|and|nor|yet|while|whereas|although|though|because|since)\s)[^\n.;:]){0,60}",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:claim|assertion|conclusion|reading)\s+that\b"
        r"(?:(?!\s+(?:but|and|nor|yet|while|whereas)\s)[^\n.;:,\u2014]){0,140}"
        r"\b(?:is|was|were|has\s+been|have\s+been)\s+"
        r"(?:refuted|rejected|withdrawn|disproved|overturned|falsified|"
        r"retracted)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:no\s+longer\s+(?:asserts?|claims?|states?|reports?|maintains?|contends?)"
        r"(?:\s+that\b)?|"
        r"(?:explicitly\s+)?den(?:ies|ied)\s+that\b|"
        r"is\s+false\s+that\b|refutes?\s+that\b|"
        r"retract(?:s|ed)?\s+that\b|withdraw(?:s|ed)?\s+that\b)"
        r"(?:(?!\s+(?:but|and|nor|yet|while|whereas|although|though|"
        r"because|since)\s)[^\n.;:,\u2014])*",
        re.IGNORECASE,
    ),
    # Rejection frames scoped to their claim noun or that-complement, in
    # active and passive voice.
    re.compile(
        r"\b(?:rejects?|disproves?|falsif(?:y|ies)|repudiates?|overturns?)\s+"
        r"(?:the\s+)?(?:claim|assertion|reading|conclusion)\s+"
        r"(?:of\s+[\w-]+|that\b(?:(?!\s+(?:but|and|nor|yet|while|whereas)\s)[^\n.;:,\u2014])*)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:claim|assertion|reading|conclusion)\s+of\s+"
        r"(?:underdetermination|impossibility|insufficiency|non[- ]?derivability|"
        r"non[- ]?closure)\b[^\n.;:]{0,50}\b(?:is|was|has\s+been)\s+"
        r"(?:rejected|disproved|refuted|overturned|falsified)\b",
        re.IGNORECASE,
    ),
)
POLARITY_IDIOM_PRESCRUBS = (
    re.compile(
        r"\bby\s+no\s+means\s+(?:\w+ly\s+)?impossible\b", re.IGNORECASE
    ),
    re.compile(r"\b(?:not|never)\s+(?:\w+ly\s+)?impossible\b", re.IGNORECASE),
    re.compile(r"\bby\s+no\s+means\b", re.IGNORECASE),
)


def _exemptable(span: str) -> bool:
    """A disclaimer surface may be scrubbed only when its text asserts
    nothing about a framework authority source."""
    return not AUTHORITY_PAYLOAD_RE.search(span)


def _sentence_around(text: str, start: int, end: int) -> str:
    window_left = max(0, start - 400)
    left = max(text.rfind(ch, window_left, start) for ch in ".!?\n")
    if left < window_left:
        left = window_left - 1
    window_right = min(len(text), end + 400)
    rights = [i for ch in ".!?\n" if (i := text.find(ch, end, window_right)) >= 0]
    return text[left + 1 : min(rights, default=window_right)]


def _strip_disclaimer_sections(text: str) -> str:
    headings = list(MARKDOWN_HEADING_RE.finditer(text))
    if not headings:
        return text
    spans: list[tuple[int, int]] = []
    for index, match in enumerate(headings):
        title = re.sub(
            r"^\s*\d+(?:\.\d+)*(?:[.):]|\s*[-\u2013\u2014])?\s*", "", match.group(2)
        ).strip()
        if not DISCLAIMER_HEADING_RE.match(title):
            continue
        level = len(match.group(1))
        end = len(text)
        for later in headings[index + 1:]:
            if len(later.group(1)) <= level:
                end = later.start()
                break
        spans.append((match.start(), end))
    if not spans:
        return text
    merged: list[tuple[int, int]] = []
    for start, end in sorted(spans):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    pieces: list[str] = []
    cursor = 0
    for start, end in merged:
        pieces.append(text[cursor:start])
        section = text[start:end]
        kept_lines = []
        section_lines = section.split("\n")
        for line_index, line in enumerate(section_lines):
            following = []
            for ln in section_lines[line_index + 1 : line_index + 5]:
                if re.match(r"[ \t]{0,3}#{1,6}\s", ln):
                    break
                following.append(ln)
            rest = " ".join(following)
            stop_match = re.search(r"[;:!?]|\.(?!\d)", rest)
            continuation = rest[: stop_match.start() if stop_match else len(rest)]
            wrapped = line + " " + continuation
            is_heading = bool(re.match(r"[ \t]{0,3}#{1,6}\s", line))
            if is_heading:
                # A heading is presentation; any full-sentence remainder
                # after a "## Scope: <assertion>" colon is judged normally.
                stripped = re.sub(r"^[ \t]{0,3}#{1,6}\s+", "", line)
                title_only = re.sub(r"^\s*\d+(?:\.\d+)*(?:[.):]|\s*[-\u2013\u2014])?\s*", "", stripped).strip()
                parts = re.split(r":|\s*[\u2014\u2013]\s*|\s+-\s+|-(?=[A-Z])", stripped, maxsplit=1)
                remainder = parts[1].strip() if len(parts) == 2 else ""
                if not remainder and not DISCLAIMER_HEADING_RE.match(title_only):
                    # A full-subject assertion used as a heading is prose,
                    # not a disclaimer title.
                    if not DISCLAIMER_FRAGMENT_LINE_RE.match(title_only):
                        kept_lines.append(title_only if _exemptable(line) else line)
                        continue
                if not remainder:
                    kept_lines.append("" if _exemptable(line) else line)
                    continue
                if DISCLAIMER_FRAGMENT_LINE_RE.match(remainder) and _exemptable(
                    remainder
                ):
                    kept_lines.append("")
                    continue
                kept_lines.append(remainder if _exemptable(line) else line)
                continue
            if DISCLAIMER_FRAGMENT_LINE_RE.match(line) and _exemptable(
                _fragment_veto_span(line)
                + (" " + continuation if line and line[-1:] not in ".;:!?" else "")
            ):
                kept_lines.append(_fragment_split(line)[1])
                continue
            kept_lines.append(line)
        pieces.append("\n".join(kept_lines))
        cursor = end
    pieces.append(text[cursor:])
    return "".join(pieces)


def _fragment_split(payload: str) -> tuple[str, str]:
    parts = re.split(r"(;|\.(?=\s|$))", payload, maxsplit=1)
    if len(parts) == 3:
        return parts[0], parts[2]
    return payload, ""


def _fragment_veto_span(payload: str) -> str:
    head, tail = _fragment_split(payload)
    if tail and (
        NEGATIVE_CONTINUATION_RE.match(tail)
        or re.match(r"\s*(?:nor|and\s+no|even)\b", tail, re.IGNORECASE)
    ):
        return payload
    return head


def _scrub_labeled_disclaimer_lines(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        payload = match.group("payload").strip()
        head, rest = _fragment_split(payload)
        tail = match.string[match.end(): match.end() + 400]
        stop_match = re.search(r"[;:!?]|\.(?!\d)", tail)
        stop = stop_match.start() if stop_match else len(tail)
        blank = tail.find("\n\n")
        if 0 <= blank < stop:
            stop = blank
        next_line = tail[:stop].replace("\n", " ")
        # A payload ending mid-claim (no sentence terminator) keeps its
        # soft-wrapped continuation in the veto span; a complete payload
        # followed by independent prose does not.
        wrapped = _fragment_veto_span(payload)
        if payload and payload[-1] not in ".;:!?":
            wrapped = wrapped + " " + next_line
        # Only subjectless template fragments are the disclaimer form; a
        # full-subject payload is judged like ordinary prose. The veto span
        # includes the soft-wrapped continuation line.
        if (
            (not payload or DISCLAIMER_FRAGMENT_LINE_RE.match(payload))
            and _exemptable(wrapped)
        ):
            # Keep any independent continuation after the fragment's own
            # sentence for ordinary matching.
            return rest
        return payload

    return LABELED_DISCLAIMER_LINE_RE.sub(replace, text)


def _scrub_local_scope_exclusions(text: str) -> str:
    """Veto-aware form of the local-scope exclusion: a "this note does not
    derive ..." clause is removed only when its full sentence names no
    framework authority source."""

    def replace(match: re.Match[str]) -> str:
        sentence = _sentence_around(text, match.start(), match.end())
        return "" if _exemptable(sentence) else match.group(0)

    return LOCAL_SCOPE_EXCLUSION_RE.sub(replace, text)


# A continuation that extends the NEGATIVE claim itself (prepositional
# source, "even in principle", nor-coordination, appended negative
# clause) keeps the clause and its continuation in the veto span. An
# affirmative independent clause after the disclaimer ("; the retained
# axioms do derive it") is routing attribution and stays out of the
# veto span.
NEGATIVE_CONTINUATION_RE = re.compile(
    # Prepositional sources, subordinate qualifiers, and appended negative
    # clauses extend the claim; the authority veto then judges the full
    # span. Routing attributions ("because the parent row carries it")
    # extend the span too and stay exempt because they name no authority.
    r"\s*[,\u2014-]?\s*(?:from|under|using|given|within|when|while|"
    r"because|once|unless|if|provided|operating|restricted)\b"
    r"|\s*,?\s*even\b"
    r"|\s*,?\s*nor\b"
    r"|\s*[,;]\s*(?:and\s+)?no(?:t|r)?\b",
    re.IGNORECASE,
)


def _scrub_note_subject_clauses(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        span = match.group(0)
        tail = text[match.end(): match.end() + 200]
        if NEGATIVE_CONTINUATION_RE.match(tail):
            span = _sentence_around(text, match.start(), match.end())
        return "" if _exemptable(span) else match.group(0)

    return NOTE_SUBJECT_DISCLAIMER_RE.sub(replace, text)


def _scrub_removed_boundaries(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        span = match.group(0)
        # A coordinated predicate may still be live; drop only the
        # removal statement and keep the coordinated remainder for the
        # ordinary matchers ("no longer persists and the exact map
        # closes ..." keeps the affirmative tail; "... but blocks the
        # readout channel" keeps the live negative).
        parts = re.split(r"(,?\s(?:but|and|yet)\s)", span, maxsplit=1, flags=re.IGNORECASE)
        if len(parts) == 3:
            tail = parts[2]
            if re.match(
                r"\s*(?:still\s+|also\s+)?(?:no\b|not\b|cannot|never|blocks?|prevents?|"
                r"precludes?|fails?)",
                tail,
                re.IGNORECASE,
            ):
                # The coordinated predicate is live and negative; keep the
                # boundary subject with it.
                noun = re.match(r"\w+", span)
                subject = noun.group(0) + " " if noun else ""
                return subject + parts[1].strip() + " " + tail
            # Affirmative continuation: drop the removal statement only.
            return tail
        return ""

    return BOUNDARY_REMOVED_TEMPORAL_RE.sub(replace, text)

NEGATED_BOUNDARY_RE = re.compile(
    r"\b(?:no|not|never|without)\s+(?:an?\s+|live\s+)?"
    r"(?:residual\s+|remaining\s+|scoped\s+|unresolved\s+)?"
    r"(?:walls?|admissions?|obstructions?)\b",
    re.IGNORECASE,
)
NEGATED_NEGATIVE_ASSURANCE_RE = re.compile(
    r"\b(?:(?:does|do|did)(?:\s+not|n't)\s+(?:require|introduce|add|create|produce)|"
    r"(?:cannot|can't)\s+(?:require|introduce|add|create|produce))\s+"
    r"(?:an?\s+|any\s+|the\s+)?(?:new\s+)?"
    r"(?:axioms?|walls?|admissions?|obstructions?)\b",
    re.IGNORECASE,
)
NEGATED_LABEL_ASSURANCE_RE = re.compile(
    r"\b(?:not|never|without)\s+(?:an?\s+|the\s+)?"
    r"(?:no[- ]go|negative boundary|firewall)\b|"
    r"\b(?:does|do|did)\s+not\s+(?:establish|prove|imply|claim|constitute)\s+"
    r"(?:an?\s+|the\s+)?(?:no[- ]go|negative boundary|firewall)\b|"
    r"\bno\s+(?:current\s+)?no[- ]go\b|"
    r"\b(?:earlier|older|prior|broad)\b[^.;:]{0,80}\bno[- ]go\b"
    r"[^.;:]{0,50}\b(?:is|was|has been)\s+withdrawn\b|"
    r"\bhistorical filename\b[^.;:]{0,80}\bdoes not turn\b"
    r"[^.;:]{0,80}\binto\s+(?:an?\s+)?no[- ]go\b",
    re.IGNORECASE,
)
LOCAL_SCOPE_EXCLUSION_RE = re.compile(
    r"\b(?:is|are|was|were|has|have)\s+not\s+(?:been\s+)?"
    r"(?:derived|established|proved|shown)\s+"
    r"(?:here|in this (?:note|theorem|section|work)|within this (?:note|scope|theorem))\b|"
    r"\b(?:it|this\s+(?:note|runner|script|calculation|result|theorem|lemma))\s+"
    r"(?:still\s+)?does\s+not\s+(?:derive|establish|prove|claim|identify)\b"
    r"[^\n.;:,]*?(?=\s+\b(?:and|but|nor|yet|because|although|though|while|whereas|since|so)\b|[\n.;:,]|$)",
    re.IGNORECASE,
)
SPECTRAL_COUNT = r"(?:\d+|one|two|three|four|five)"
FORCED_SPECTRAL_BOUNDARY_RES = (
    re.compile(
        rf"\b(?:allows?|permits?|has|have|yields?|gives?|forces?|contains?)\s+"
        rf"(?:at\s+most|no\s+more\s+than)\s+{SPECTRAL_COUNT}\s+"
        r"(?:distinct\s+)?(?:eigenvalues?|spectral\s+values?)\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b(?:spectrum|spectral\s+set|eigenvalue\s+set)\s+"
        rf"(?:has|have)\s+cardinality\s+(?:at\s+most|no\s+more\s+than)\s+"
        rf"{SPECTRAL_COUNT}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b(?:at\s+most|no\s+more\s+than)\s+{SPECTRAL_COUNT}\s+"
        r"(?:distinct\s+)?(?:eigenvalues?|spectral\s+values?)\s+"
        r"(?:occur|occurs|appear|appears|are\s+possible|can\s+occur)\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\bthere\s+(?:is|are)\s+(?:at\s+most|no\s+more\s+than)\s+"
        rf"{SPECTRAL_COUNT}\s+(?:distinct\s+)?"
        r"(?:eigenvalues?|spectral\s+values?)\b",
        re.IGNORECASE,
    ),
)
SPECTRAL_EXCLUSION_RE = re.compile(
    r"\b(?:cannot|can\s+not)\s+have\s+(?:\d+|one|two|three|four|five)\s+"
    r"distinct\s+(?:eigenvalues?|spectral\s+values?)\b|"
    r"\bforces?\s+(?:an?\s+)?(?:doubly|two[- ]?fold|triply|three[- ]?fold)"
    r"[- ]degenerate\s+(?:eigenspace|eigenvalue|spectrum)\b",
    re.IGNORECASE,
)
SPECTRAL_NEGATION_PREFIX_RE = re.compile(
    r"\b(?:not|never|cannot|can't|does\s+not|doesn't|do\s+not|don't|"
    r"did\s+not|didn't|is\s+not|isn't|are\s+not|aren't)\b[^,;:.!?]{0,48}$",
    re.IGNORECASE,
)
SPECTRAL_QUESTION_PREFIX_RE = re.compile(
    r"^\s*(?:can|could|does|do|did|is|are|may|might|would|will|should)\b",
    re.IGNORECASE,
)
OUTPUT_BOUNDARY_FIELDS = (
    "claim_scope",
    "load_bearing_step",
    "chain_closure_explanation",
    "verdict_rationale",
)

AXIOM_REGISTRY = "docs/audit/data/axiom_premise_nodes.json"
OBLIGATION_REGISTRY = "docs/audit/data/derivation_obligations.json"
CONTROLLED_VOCABULARY = "docs/repo/controlled_vocabulary.yaml"
ACTIVE_REVIEW_QUEUE = "docs/repo/ACTIVE_REVIEW_QUEUE.md"
PREMISE_CLASSES_CHECKED = {
    "axiom_or_approved_primitive",
    "open_gate",
    "convention_not_accepted",
    "definition_or_scope_reframe",
}
# Validation-only compatibility for packets signed before the 2026-07-11
# authority reset. New packets are always built with PREMISE_CLASSES_CHECKED;
# accepting this exact historical shape does not restore any premise authority.
LEGACY_PREMISE_CLASSES_CHECKED = {
    "axiom_or_approved_primitive",
    "owner_governed_residual",
    "tier_a_derivation_target",
    "tier_a_convention_not_accepted",
    "definition_or_scope_reframe",
}
N3_SCAN_PHRASES = (
    "admission", "ansatz", "axiom", "boundary", "bridge context",
    "by construction", "convention", "initial condition", "normalization",
    "obstruction", "primitive", "as is standard", "naturally", "sector",
    "standard QFT", "wall", "we assume", "the framework provides",
    "background", "obviously", "registered", "canonical",
)
N5_SCAN_PHRASES = (
    "absent", "cannot", "does not", "fails", "impossible", "no nonzero",
    "no-go", "obstruction", "requires a new axiom", "rule out",
    "rules out", "structurally undecidable", "unavailable", "is not", "are not",
)
N5_RESOLUTION_CLASSES = {
    "per_element", "per_site", "per_mode", "per_block", "lattice_wide",
}
# N5 authenticates negative rhetoric about the claim's physics. Administrative
# scope negations assert nothing physical, so they do not need five-resolution
# sweeps. Exclusion is deliberately fail-safe: every N5 occurrence in the
# locator must belong to a recognized administrative clause. Mixed or ambiguous
# locators remain in the authenticated universe in full.
N5_ADMINISTRATIVE_NEGATION_RE = re.compile(
    r"\bdoes\s+not\s+(?:set\s+or\s+predict|"
    r"set\s*,\s*predict\s*,\s*or\s+apply|predict)\s+"
    r"(?:(?:an?|the|this|its|resulting)\s+){0,2}"
    r"(?:audit(?:\s+(?:outcome|status|verdict|result))?|"
    r"(?:effective|retained)\s+status|"
    r"parent(?:'s)?\s+audit\s+outcome|"
    r"parent\s+row(?:'s)?\s+status|"
    r"audit\s+row(?:'s)?\s+status)\b|"
    r"\b(?:is|are)\s+not\s+(?:an?\s+)?citation-graph dependency\b|"
    r"\bthis\s+(?:source\s+)?(?:note|addendum|corollary|packet|template)\s+"
    r"does\s+not\s+(?:execute\s+or\s+request|request\s+or\s+execute)\b|"
    r"\bis\s+not\s+an\s+assertion\b",
    re.IGNORECASE,
)
_N5_PHRASE_NORMS: frozenset[str] = frozenset(
    re.sub(r"\s+", " ", phrase.strip().casefold()) for phrase in N5_SCAN_PHRASES
)
_N5_ADMIN_EXCLUDABLE_PHRASE_NORMS = (
    _N5_PHRASE_NORMS
    - frozenset(
        re.sub(r"\s+", " ", phrase.strip().casefold())
        for phrase in N3_SCAN_PHRASES
    )
)
_N5_SCAN_RES: tuple[tuple[str, re.Pattern[str]], ...] = tuple(
    (
        re.sub(r"\s+", " ", phrase.strip().casefold()),
        re.compile(
            r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b",
            re.IGNORECASE,
        ),
    )
    for phrase in N5_SCAN_PHRASES
)


def n5_administrative_negation(phrase: str, locator: str) -> bool:
    """Whether a locator contains only covered administrative N5 rhetoric.

    The caller supplies an N5 phrase found on the locator. If another N5
    occurrence is outside every administrative match, the whole locator stays
    authenticated. This intentional over-capture prevents a substantive clause
    from being hidden beside boilerplate on one Markdown line.
    """
    normalized = re.sub(r"\s+", " ", str(phrase or "").strip().casefold())
    if normalized not in _N5_ADMIN_EXCLUDABLE_PHRASE_NORMS:
        return False
    text = str(locator or "")
    admin_spans = [match.span() for match in N5_ADMINISTRATIVE_NEGATION_RE.finditer(text)]
    if not admin_spans:
        return False
    requested_spans = [
        match.span()
        for candidate, pattern in _N5_SCAN_RES
        if candidate == normalized
        for match in pattern.finditer(text)
    ]
    if not requested_spans:
        return False
    n5_spans = [
        match.span()
        for _candidate, pattern in _N5_SCAN_RES
        for match in pattern.finditer(text)
    ]
    return bool(n5_spans) and all(
        any(start <= hit_start and hit_stop <= stop for start, stop in admin_spans)
        for hit_start, hit_stop in n5_spans
    )


DOCS_NEGATIVE_RE = re.compile(
    r"structurally undecidable|no retained primitive|requires? (?:a )?new axiom|"
    r"cannot be derived|not derivable|no[- ]go|negative boundary|firewall|"
    r"no admissible route|no uniform sign",
    re.IGNORECASE,
)
_DOCS_NEGATIVE_CORPUS_CACHE: dict[str, tuple[list[Path], list[dict[str, Any]]]] = {}
_LOOP_LEDGER_CORPUS_CACHE: dict[str, tuple[list[Path], list[dict[str, Any]]]] = {}
N8_SOURCE_CORPUS_VERSION = "source-markdown-v2-excludes-generated"


def _is_generated_markdown(path: Path) -> bool:
    """Keep N8 candidate bytes independent of pipeline-generated views."""
    try:
        prefix = path.read_text(encoding="utf-8", errors="replace")[:512]
    except OSError:
        return True
    return "AUTO-GENERATED" in prefix or path.name in {
        "AUDIT_LEDGER.md",
        "AUDIT_QUEUE.md",
        "AUDIT_DISPATCH_QUEUE.md",
        "PUBLICATION_AUDIT_DIVERGENCE.md",
        "FRONT_DOOR_STATUS.md",
    } or path.name.endswith("_EFFECTIVE_STATUS.md")


def _docs_negative_corpus(root: Path) -> tuple[list[Path], list[dict[str, Any]]]:
    key = str(root.resolve())
    if key in _DOCS_NEGATIVE_CORPUS_CACHE:
        return _DOCS_NEGATIVE_CORPUS_CACHE[key]
    paths = [
        path for path in sorted((root / "docs").rglob("*.md"))
        if not _is_generated_markdown(path)
    ]
    records: list[dict[str, Any]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        excerpts = [
            line.strip()[:400]
            for line in text.splitlines()
            if line.strip() and DOCS_NEGATIVE_RE.search(line)
        ]
        if excerpts:
            records.append({
                "path": path,
                "content_sha256": _read_bytes_sha256(
                    root, path.relative_to(root).as_posix()
                ),
                "excerpts": excerpts,
                "search_terms": _search_terms(" ".join(excerpts)),
            })
    _DOCS_NEGATIVE_CORPUS_CACHE[key] = (paths, records)
    return paths, records


def _loop_ledger_corpus(root: Path, pattern: str) -> tuple[list[Path], list[dict[str, Any]]]:
    key = f"{root.resolve()}::{pattern}"
    if key in _LOOP_LEDGER_CORPUS_CACHE:
        return _LOOP_LEDGER_CORPUS_CACHE[key]
    paths = sorted(root.glob(pattern))
    records: list[dict[str, Any]] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            text = f"[could not read loop no-go ledger: {exc}]"
        records.append({
            "path": path,
            "text": text,
            "content_sha256": _read_bytes_sha256(root, path.relative_to(root).as_posix()),
            "search_terms": _search_terms(text),
        })
    _LOOP_LEDGER_CORPUS_CACHE[key] = (paths, records)
    return paths, records


def _read_text(repo_root: Path, path: str | None) -> str:
    if not path:
        return ""
    try:
        return (repo_root / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _read_bytes_sha256(repo_root: Path, path: str | None) -> str:
    if not path:
        return hashlib.sha256(b"").hexdigest()
    try:
        payload = (repo_root / path).read_bytes()
    except OSError:
        payload = b""
    return hashlib.sha256(payload).hexdigest()


def _load_json(repo_root: Path, path: str) -> dict:
    try:
        return json.loads((repo_root / path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _canonical_runner_path(repo_root: Path, raw: str | None) -> str:
    if not raw:
        return ""
    p = Path(raw)
    candidates = []
    if p.is_absolute() or not str(raw).startswith("scripts/"):
        candidates.append(f"scripts/{p.name}")
    candidates.append(str(raw))
    for candidate in candidates:
        if (repo_root / candidate).exists():
            return candidate
    return str(raw)


def _repo_local_helper_runner_path(
    repo_root: Path,
    raw: str | None,
) -> str | None:
    helper = _canonical_runner_path(repo_root, raw)
    relative = Path(helper)
    if (
        relative.is_absolute()
        or not relative.parts
        or relative.parts[0] != "scripts"
        or ".." in relative.parts
    ):
        return None
    try:
        root = repo_root.resolve()
        scripts_root = (root / "scripts").resolve()
        resolved = (root / relative).resolve()
        # Fail closed on symlinked helpers: the resolved target must stay
        # inside BOTH the repo root and the resolved scripts/ directory, so a
        # lexically valid scripts/ entry cannot point elsewhere in the repo.
        resolved.relative_to(root)
        resolved.relative_to(scripts_root)
    except (OSError, ValueError):
        return None
    if not resolved.is_file():
        return None
    return helper


def premise_type_for_id(repo_root: Path, claim_id: str) -> str | None:
    axioms = _load_json(repo_root, AXIOM_REGISTRY)
    if claim_id in set(axioms.get("canonical_ids") or []):
        return "axiom_or_approved_primitive"
    return None


def _add_evidence(
    manifest: dict[str, dict],
    *,
    path: str,
    role: str,
    text: str,
    effective_status: str | None = None,
    premise_type: str | None = None,
) -> None:
    if not path:
        return
    entry = manifest.setdefault(
        path,
        {
            "path": path,
            "roles": [],
            "text": text,
            "effective_status": effective_status,
            "accepted_premise_type": premise_type,
        },
    )
    if role not in entry["roles"]:
        entry["roles"].append(role)
    if text and not entry.get("text"):
        entry["text"] = text
    if effective_status:
        entry["effective_status"] = effective_status
    if premise_type:
        entry["accepted_premise_type"] = premise_type


def set_packet_evidence(
    manifest: dict[str, dict],
    *,
    path: str,
    role: str,
    text: str,
    effective_status: str | None = None,
    premise_type: str | None = None,
    invocation_bound_rendered_text: bool = False,
) -> None:
    """Insert or replace one exact rendered packet surface."""
    _add_evidence(
        manifest,
        path=path,
        role=role,
        text=text,
        effective_status=effective_status,
        premise_type=premise_type,
    )
    if path in manifest:
        manifest[path]["text"] = text
        if invocation_bound_rendered_text:
            manifest[path]["invocation_bound_rendered_text"] = True


# Per-kind N8 candidate caps. Prior cycles and open gates remain uncapped.
# Repository-wide similarity/scan kinds are capped by
# the declared relevance order (kind priority, shared-term count descending)
# with an authenticated omitted-tail summary in the index, so corpus hiding
# remains impossible while the disposition set stays reviewable at audit
# scale. 2026-07-12 repair: uncapped scan kinds produced ~1,700-candidate
# packets on common-vocabulary foundational rows (infeasible to disposition
# honestly in one session), and together with snapshot set-identity
# invalidation they decayed every clean audit within hours of landing.
N8_KIND_CANDIDATE_LIMITS: dict[str, int | None] = {
    "prior_audit_cycle": None,
    "open_gate": None,
    "similar_negative_boundary": 20,
    "repo_negative_phrase_hit": 20,
    "physics_loop_no_go_ledger": 20,
}

N6_CANDIDATE_LIMITS = {
    "controlled_vocabulary": 5,
    "meta_reframe": 5,
    "claim_reframe": 10,
    "in_flight_reframe": 5,
}


def _compact_text(value: Any, limit: int = 360) -> str:
    """Return one deterministic single-line evidence excerpt for an index row."""
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return re.sub(r"\s+", " ", text).strip()[:limit]


def _semantic_text_values(value: Any) -> list[str]:
    """Extract substantive text in a stable, schema-aware preference order."""
    if isinstance(value, str):
        text = _compact_text(value)
        return [text] if text else []
    if isinstance(value, list):
        values: list[str] = []
        for item in value:
            values.extend(_semantic_text_values(item))
        return values
    if not isinstance(value, dict):
        return []
    preferred_keys = (
        "target", "note", "text", "claim_scope", "label",
        "self_liquidation_condition", "definition", "use", "description",
    )
    values = []
    for key in preferred_keys:
        if key in value:
            values.extend(_semantic_text_values(value[key]))
    if values:
        return values
    for key in sorted(value):
        values.extend(_semantic_text_values(value[key]))
    return values


def _semantic_boilerplate(text: str) -> bool:
    return bool(
        re.match(r"^#{1,6}\s", text)
        or re.search(
            r"(?:^\*\*(?:date|type|claim type|status|status authority|"
            r"primary runner|runner cache|source-note proposal disclaimer)\b|"
            r"^\*\*claim boundary:\*\*|audit verdict|downstream status|"
            r"source-note proposal)",
            text,
            re.IGNORECASE,
        )
    )


def _best_semantic_excerpt(value: Any) -> str:
    """Prefer an argumentative body line over headings or transport metadata."""
    values = _semantic_text_values(value)
    if not values:
        return ""

    def score(text: str) -> tuple[int, int, int, int, int]:
        heading = bool(re.match(r"^#{1,6}\s", text))
        boilerplate = _semantic_boilerplate(text)
        mechanism_terms = bool(
            re.search(
                r"\b(?:derive|entail|select|require|supply|obstruction|residual|"
                r"countermodel|theorem|readout|action|normalization|bridge)\b",
                text,
                re.IGNORECASE,
            )
        )
        return (
            int(not boilerplate), int(not heading), int(mechanism_terms),
            int(len(text) >= 40), len(text),
        )

    return max(values, key=score)


def _negative_boundary_values(value: Any) -> list[str]:
    """Return lines that state a scientific negative/residual mechanism."""
    negative_re = re.compile(
        r"(?:\b(?:does not|do not|cannot|fails?|unentailed|underdetermin\w*|"
        r"not select\w*|not supply\w*|not derive\w*|obstruction|residual)\b|"
        r"\bno\s+(?:retained|physical|admissible|theorem|bridge|selector|route)\b)",
        re.IGNORECASE,
    )
    return [
        text
        for text in _semantic_text_values(value)
        if not _semantic_boilerplate(text)
        and (DOCS_NEGATIVE_RE.search(text) or negative_re.search(text))
    ]


def _compact_cross_cycle_candidate(
    candidate: dict[str, Any], repo_root: str | Path | None = None,
) -> dict[str, Any]:
    """Keep every listed N8 identity while removing repeated bulk prose.

    The auditor needs one substantive indexed mechanism per candidate, its
    lifecycle, and an authenticated source locator/hash. Full candidate-ID
    universes remain in the trusted manifest rather than the model prompt.
    """
    record = candidate.get("record")
    kind = candidate.get("kind")
    excerpts = candidate.get("matched_excerpts") or candidate.get("content") or []
    canonical_negative_excerpts = _negative_boundary_values(excerpts)
    note_path = candidate.get("note_path")
    matching_terms = set(candidate.get("matching_terms") or [])
    needs_full_note_scan = (
        kind == "similar_negative_boundary"
        or not canonical_negative_excerpts
    )
    if repo_root is not None and note_path and matching_terms and needs_full_note_scan:
        full_note = _read_text(Path(repo_root), str(note_path))
        full_matches = [
            line.strip()
            for line in full_note.splitlines()
            if line.strip()
            and matching_terms.intersection(_search_terms(line))
        ]
        if full_matches:
            excerpts = [*_semantic_text_values(excerpts), *full_matches]
    if kind in {
        "similar_negative_boundary", "repo_negative_phrase_hit",
        "physics_loop_no_go_ledger",
    }:
        negative_excerpts = (
            _negative_boundary_values(excerpts)
            if kind == "similar_negative_boundary"
            else canonical_negative_excerpts or _negative_boundary_values(excerpts)
        )
        if negative_excerpts:
            excerpts = negative_excerpts
    excerpt = _best_semantic_excerpt(excerpts)
    mechanism = candidate.get("claim_scope")
    if not mechanism and isinstance(record, dict):
        mechanism = record.get("target")
    mechanism = (
        mechanism
        or excerpt
        or candidate.get("invalidation_reason")
        or candidate.get("candidate_id")
        or "indexed cross-cycle candidate"
    )
    compact = {
        "candidate_id": candidate.get("candidate_id"),
        "kind": candidate.get("kind"),
        "mechanism": _compact_text(mechanism),
        "lifecycle_state": candidate.get("lifecycle_state"),
        "retired": candidate.get("retired"),
        "applicable": None,
    }
    source = candidate.get("note_path") or candidate.get("source_claim_id")
    if source:
        compact["source"] = source
    if candidate.get("content_sha256"):
        compact["content_sha256"] = candidate["content_sha256"]
    return compact


def _compact_partial_closure_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """Keep the N6 identity and strongest indexed basis in compact form."""
    basis = _best_semantic_excerpt(
        candidate.get("content") or candidate.get("candidate_id")
    )
    kind = candidate.get("kind")
    if kind == "claim_scope_reframe":
        kind = "definition_refactor"
    compact = {
        "candidate_id": candidate.get("candidate_id"),
        "kind": kind,
        "source_path": candidate.get("source_path"),
        "accepted_premise_type": candidate.get("accepted_premise_type"),
        "basis": basis,
    }
    if candidate.get("content_sha256"):
        compact["content_sha256"] = candidate["content_sha256"]
    return compact


def cross_cycle_index_path(claim_id: str) -> str:
    return f"audit-packet://cross-cycle-index/{claim_id}"


def partial_closure_index_path(claim_id: str) -> str:
    return f"audit-packet://partial-closure-index/{claim_id}"


def runner_stdout_evidence_path(claim_id: str) -> str:
    return f"audit-packet://runner-stdout/{claim_id}"


def independent_runner_stdout_evidence_path(
    claim_id: str,
    runner_path: str,
) -> str:
    canonical_path = str(runner_path).replace("\\", "/")
    path_digest = hashlib.sha256(canonical_path.encode("utf-8")).hexdigest()[:16]
    return (
        f"audit-packet://runner-stdout-independent/{claim_id}/"
        f"{Path(canonical_path).stem}-{path_digest}"
    )


def blind_reaudit_control_path(claim_id: str) -> str:
    return f"audit-packet://blind-reaudit-control/{claim_id}"


BLIND_REAUDIT_PRIOR_SCOPE = "WITHHELD_FOR_FRESH_CONTEXT"
LEGACY_BACKFILL_SCOPE_PREFIX = (
    "Legacy audit row backfilled during scope-aware classification migration"
)
BLIND_REAUDIT_WITHHELD_ROW_FIELDS = {
    "audit_status", "auditor", "auditor_family", "auditor_model",
    "audit_date", "claim_scope", "claim_type", "effective_status",
    "independence", "previous_audits", "verdict_rationale",
}


def blind_reaudit_row_projection(row: dict[str, Any]) -> dict[str, Any]:
    """Return the one canonical target-row view used by blind dispatches."""
    return {
        key: value
        for key, value in row.items()
        if key not in BLIND_REAUDIT_WITHHELD_ROW_FIELDS
    }


def manifest_has_blind_reaudit_control(
    manifest: dict[str, dict] | None,
) -> bool:
    return any(
        "blind_reaudit_control" in set(entry.get("roles") or [])
        for entry in (manifest or {}).values()
    )


SEARCH_STOPWORDS = {
    "about", "after", "against", "before", "bounded", "claim", "clean",
    "conditional", "current", "derived", "framework", "note", "result",
    "route", "scope", "supplied", "theorem", "their", "there", "these",
    "this", "under", "using", "with", "without",
}


def _search_terms(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9_]{5,}", text.casefold())
        if token not in SEARCH_STOPWORDS
    }


def _row_search_terms(
    row: dict[str, Any], repo_root: str | Path | None = None
) -> set[str]:
    stable_basis = " ".join(
        str(row.get(field) or "")
        for field in ("claim_id", "note_path", "title", "claim_scope")
    )
    if repo_root is not None and row.get("note_path"):
        stable_basis += " " + _read_text(Path(repo_root), str(row["note_path"]))
    return _search_terms(re.sub(r"[_/.-]+", " ", stable_basis))


def build_cross_cycle_index(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> str:
    """Render the orchestrator-owned N8 search surface supplied to the auditor."""
    candidates: list[dict[str, Any]] = []
    cid = str(row.get("claim_id") or "")
    root = Path(repo_root)
    current_terms = _row_search_terms(row, root)

    obligations = _load_json(root, OBLIGATION_REGISTRY)
    for obligation_id, record in sorted((obligations.get("nodes") or {}).items()):
        candidates.append(
            {
                "candidate_id": f"open_gate:{obligation_id}",
                "kind": "open_gate",
                "source_claim_id": obligation_id,
                "record": record,
                "lifecycle_state": "active",
                "retired": False,
                "applicable": None,
            }
        )

    docs_markdown_paths, docs_negative_records = _docs_negative_corpus(root)
    current_note_path = str(row.get("note_path") or "")
    for record in docs_negative_records:
        path = record["path"]
        relative_path = path.relative_to(root).as_posix()
        if relative_path == current_note_path:
            continue
        overlap = sorted(current_terms.intersection(record["search_terms"]))
        if len(overlap) < 2:
            continue
        candidates.append(
            {
                "candidate_id": f"repo_negative_scan:{relative_path}",
                "kind": "repo_negative_phrase_hit",
                "note_path": relative_path,
                "content_sha256": record["content_sha256"],
                "matched_excerpts": record["excerpts"][:5],
                "matching_terms": overlap,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )

    loop_ledger_glob = ".claude/science/physics-loops/**/NO_GO_LEDGER.md"
    loop_ledger_paths, loop_ledger_records = _loop_ledger_corpus(root, loop_ledger_glob)
    for record in loop_ledger_records:
        ledger_path = record["path"]
        ledger_text = record["text"]
        relative_path = ledger_path.relative_to(root).as_posix()
        matching_terms = sorted(current_terms.intersection(record["search_terms"]))
        if len(matching_terms) < 2:
            continue
        ledger_excerpts = [
            line.strip()[:400]
            for line in ledger_text.splitlines()
            if line.strip() and (
                current_terms.intersection(_search_terms(line))
                or DOCS_NEGATIVE_RE.search(line)
            )
        ][:10]
        candidates.append(
            {
                "candidate_id": f"physics_loop_no_go_ledger:{relative_path}",
                "kind": "physics_loop_no_go_ledger",
                "source_claim_id": relative_path,
                "note_path": relative_path,
                "content_sha256": record["content_sha256"],
                "content": ledger_excerpts,
                "content_truncated": len("\n".join(ledger_excerpts)) < len(ledger_text),
                "matching_terms": matching_terms,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )

    no_go_universe = [
        {
            "claim_id": other_id,
            "note_path": str(other.get("note_path") or ""),
            "note_sha256": _read_bytes_sha256(
                root, str(other.get("note_path") or "")
            ),
        }
        for other_id, other in sorted(ledger_rows.items())
        if other_id != cid and str(other.get("claim_type") or "") == "no_go"
    ]
    no_go_universe_sha256 = hashlib.sha256(
        json.dumps(no_go_universe, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
    ).hexdigest()

    similar: list[tuple[int, str, dict[str, Any], list[str]]] = []
    for other_id, other in ledger_rows.items():
        if other_id == cid:
            continue
        other_path = str(other.get("note_path") or "")
        if (
            str(other.get("claim_type") or "") != "no_go"
            and not PATH_TRIGGER_RE.search(other_path)
        ):
            continue
        other_note = _read_text(root, other_path)
        other_text = " ".join((other_id, other_path, other_note))
        overlap = sorted(current_terms.intersection(_search_terms(other_text)))
        if len(overlap) < 2:
            continue
        similar.append((len(overlap), other_id, other, overlap))
    for _score, other_id, other, overlap in sorted(
        similar, key=lambda item: (-item[0], item[1])
    ):
        note_path = str(other.get("note_path") or "")
        note_text = _read_text(root, note_path)
        matched_excerpts = [
            line.strip()[:400]
            for line in note_text.splitlines()
            if line.strip() and current_terms.intersection(_search_terms(line))
        ][:5]
        candidates.append(
            {
                "candidate_id": f"similar_negative_boundary:{other_id}",
                "kind": "similar_negative_boundary",
                "source_claim_id": other_id,
                "note_path": note_path,
                "content_sha256": _read_bytes_sha256(root, note_path),
                "matched_excerpts": matched_excerpts,
                "matching_terms": overlap,
                "lifecycle_state": "unknown",
                "retired": None,
                "applicable": None,
            }
        )
    kind_priority = {
        "open_gate": 0,
        "similar_negative_boundary": 1,
        "repo_negative_phrase_hit": 2,
        "physics_loop_no_go_ledger": 3,
    }
    ordered_candidates = sorted(
        candidates,
        key=lambda candidate: (
            kind_priority.get(str(candidate.get("kind")), 9),
            -len(candidate.get("matching_terms") or []),
            str(candidate.get("candidate_id") or ""),
        ),
    )
    # Every LISTED candidate must be dispositioned. High-signal kinds are
    # listed in full; the bulk scan kinds are capped by the declared
    # relevance order with an authenticated omitted-tail summary below, so
    # the corpus remains un-hideable (counts + omitted-id hash are part of
    # the authenticated index) while the disposition set stays reviewable.
    listed_candidates: list[dict[str, Any]] = []
    kind_totals: dict[str, int] = {}
    omitted_by_kind: dict[str, list[str]] = {}
    for candidate in ordered_candidates:
        kind = str(candidate.get("kind"))
        kind_totals[kind] = kind_totals.get(kind, 0) + 1
        limit = N8_KIND_CANDIDATE_LIMITS.get(kind)
        if limit is not None and kind_totals[kind] > limit:
            omitted_by_kind.setdefault(kind, []).append(
                str(candidate.get("candidate_id") or "")
            )
            continue
        listed_candidates.append(candidate)
    candidate_truncation = {
        kind: {
            "limit": N8_KIND_CANDIDATE_LIMITS.get(kind),
            "total_hits": total,
            "listed": total - len(omitted_by_kind.get(kind, [])),
            "omitted_count": len(omitted_by_kind.get(kind, [])),
            "omitted_candidate_ids_sha256": hashlib.sha256(
                json.dumps(
                    omitted_by_kind.get(kind, []), separators=(",", ":")
                ).encode("utf-8")
            ).hexdigest(),
        }
        for kind, total in sorted(kind_totals.items())
    }
    candidate_id_universe = sorted(
        str(candidate.get("candidate_id") or "")
        for candidate in ordered_candidates
    )
    candidates = listed_candidates
    return json.dumps(
        {
            "schema": "no_go_cross_cycle_index_v1",
            "claim_id": cid,
            "search_scope": {
                # Prior audit judgments are deliberately excluded. N8 is a
                # fresh search over source-cycle artifacts, open gates, and
                # governed no-go ledgers, not a replay of earlier verdicts.
                "current_row_audit_history": False,
                "one_hop_authority_audit_history": False,
                "historical_dispositions": True,
                "open_gates": True,
                "candidate_limit": {
                    "per_kind": N8_KIND_CANDIDATE_LIMITS,
                    "policy": (
                        "prior-cycle and open-gate kinds listed in full; "
                        "repository scan kinds capped by declared relevance "
                        "order with an authenticated omitted-tail summary"
                    ),
                },
                "candidate_order": (
                    "kind priority, shared-term count descending, candidate_id"
                ),
                "source_corpus_version": N8_SOURCE_CORPUS_VERSION,
                "docs_markdown_files_scanned": len(docs_markdown_paths),
                "docs_negative_phrase_hits_complete": True,
                "docs_candidate_policy": "negative phrase plus at least two current-row search terms",
                "similar_no_go_rows": {
                    "source": (
                        "all audit-ledger claim_type=no_go rows, union paths "
                        "with explicit no-go/boundary triggers"
                    ),
                    "minimum_shared_terms": 2,
                    "candidate_limit": N8_KIND_CANDIDATE_LIMITS[
                        "similar_negative_boundary"
                    ],
                },
                "physics_loop_no_go_ledgers": {
                    "glob": loop_ledger_glob,
                    "scanned_count": len(loop_ledger_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(
                            [path.relative_to(root).as_posix() for path in loop_ledger_paths],
                            separators=(",", ":"),
                        ).encode("utf-8")
                    ).hexdigest(),
                    "candidate_policy": "at least two current-row search terms; every tracked ledger is scanned",
                },
            },
            "no_go_row_universe": no_go_universe,
            "no_go_row_universe_count": len(no_go_universe),
            "no_go_row_universe_sha256": no_go_universe_sha256,
            # Full IDs are lightweight authenticated metadata, not disposition
            # records. They let the durability sweep report capped-tail growth
            # exactly without restoring the infeasible uncapped packet.
            "candidate_id_universe": candidate_id_universe,
            "candidate_truncation": candidate_truncation,
            "candidates": candidates,
        },
        indent=2,
        sort_keys=True,
    )


def build_partial_closure_index(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> str:
    """Render the orchestrator-owned N6 convention/reframe search surface."""
    root = Path(repo_root)
    cid = str(row.get("claim_id") or "")
    current_terms = _row_search_terms(row, root)
    candidates: list[dict[str, Any]] = []
    candidate_id_universe: set[str] = set()

    def add_candidate(
        *,
        candidate_id: str,
        kind: str,
        source_path: str,
        content: Any,
        matching_terms: list[str] | None = None,
        accepted_premise_type: str | None = None,
        content_sha256: str | None = None,
    ) -> None:
        candidate_id_universe.add(candidate_id)
        candidates.append(
            {
                "candidate_id": candidate_id,
                "kind": kind,
                "source_path": source_path,
                "accepted_premise_type": accepted_premise_type,
                "matching_terms": matching_terms or [],
                "content_sha256": content_sha256,
                "content": content,
            }
        )

    axioms = _load_json(root, AXIOM_REGISTRY)
    for premise_id in sorted(axioms.get("canonical_ids") or []):
        add_candidate(
            candidate_id=f"approved_primitive:{premise_id}",
            kind="approved_primitive",
            source_path=AXIOM_REGISTRY,
            content=(axioms.get("nodes") or {}).get(premise_id, {}),
            accepted_premise_type="axiom_or_approved_primitive",
        )
    obligations = _load_json(root, OBLIGATION_REGISTRY)
    for obligation_id in sorted(obligations.get("canonical_ids") or []):
        add_candidate(
            candidate_id=f"open_gate:{obligation_id}",
            kind="open_gate",
            source_path=OBLIGATION_REGISTRY,
            content=(obligations.get("nodes") or {}).get(obligation_id, {}),
        )
    keyword_re = re.compile(
        r"\b(?:axiom|primitive|convention|definition|label(?:ing)?|meta|ratif\w*|refram\w*)\b",
        re.IGNORECASE,
    )

    def evidence_lines(content: str) -> list[dict[str, Any]]:
        ranked: list[tuple[int, int, int, dict[str, Any]]] = []
        for line_number, line in enumerate(content.splitlines(), 1):
            overlap = sorted(current_terms.intersection(_search_terms(line)))
            if not overlap:
                continue
            keyword_hit = bool(keyword_re.search(line))
            ranked.append(
                (
                    len(overlap),
                    int(keyword_hit),
                    line_number,
                    {
                        "line": line_number,
                        "matching_terms": overlap,
                        "partial_closure_keyword": keyword_hit,
                        "text": line,
                    },
                )
            )
        return [
            item[3]
            for item in sorted(ranked, key=lambda item: (-item[0], -item[1], item[2]))[:5]
        ]

    vocabulary_text = _read_text(root, CONTROLLED_VOCABULARY)
    vocabulary_hits: list[tuple[int, int, str, list[str]]] = []
    for line_number, line in enumerate(vocabulary_text.splitlines(), 1):
        overlap = sorted(current_terms.intersection(_search_terms(line)))
        if overlap and keyword_re.search(line):
            vocabulary_hits.append((len(overlap), line_number, line, overlap))
    ordered_vocabulary_hits = sorted(
        vocabulary_hits, key=lambda item: (-item[0], item[1])
    )
    candidate_id_universe.update(
        f"controlled_vocabulary:{line_number}"
        for _score, line_number, _line, _overlap in ordered_vocabulary_hits
    )
    for _score, line_number, line, overlap in ordered_vocabulary_hits[
        :N6_CANDIDATE_LIMITS["controlled_vocabulary"]
    ]:
        add_candidate(
            candidate_id=f"controlled_vocabulary:{line_number}",
            kind="definition_refactor",
            source_path=CONTROLLED_VOCABULARY,
            content=line,
            matching_terms=overlap,
        )

    meta_paths = sorted(
        {
            str(other.get("note_path"))
            for other in ledger_rows.values()
            if other.get("claim_type") == "meta" and other.get("note_path")
        }
    )
    meta_hits: list[tuple[int, str, str, list[str]]] = []
    for path in meta_paths:
        content = _read_text(root, path)
        overlap = sorted(current_terms.intersection(_search_terms(content)))
        if len(overlap) >= 2 and keyword_re.search(content):
            meta_hits.append((len(overlap), path, content, overlap))
    ordered_meta_hits = sorted(meta_hits, key=lambda item: (-item[0], item[1]))
    candidate_id_universe.update(
        f"meta_reframe:{path}"
        for _score, path, _content, _overlap in ordered_meta_hits
    )
    for _score, path, content, overlap in ordered_meta_hits[
        :N6_CANDIDATE_LIMITS["meta_reframe"]
    ]:
        add_candidate(
            candidate_id=f"meta_reframe:{path}",
            kind="definition_refactor",
            source_path=path,
            content=evidence_lines(content),
            matching_terms=overlap,
            content_sha256=hashlib.sha256(content.encode("utf-8")).hexdigest(),
        )

    claim_rows = [
        other
        for other in ledger_rows.values()
        if other.get("claim_type") in {
            "positive_theorem", "bounded_theorem", "open_gate", "no_go"
        }
        and other.get("note_path")
        and other.get("note_path") != row.get("note_path")
    ]
    claim_paths = sorted({str(other["note_path"]) for other in claim_rows})
    claim_hits: list[tuple[int, str, str, list[str]]] = []
    for other in claim_rows:
        identity_overlap = current_terms.intersection(_row_search_terms(other))
        if len(identity_overlap) < 2:
            continue
        path = str(other["note_path"])
        content = _read_text(root, path)
        overlap = sorted(current_terms.intersection(_search_terms(content)))
        if len(overlap) >= 2 and keyword_re.search(content):
            claim_hits.append((len(overlap), path, content, overlap))
    ordered_claim_hits = sorted(claim_hits, key=lambda item: (-item[0], item[1]))
    candidate_id_universe.update(
        f"claim_reframe:{path}"
        for _score, path, _content, _overlap in ordered_claim_hits
    )
    for _score, path, content, overlap in ordered_claim_hits[
        :N6_CANDIDATE_LIMITS["claim_reframe"]
    ]:
        add_candidate(
            candidate_id=f"claim_reframe:{path}",
            kind="claim_scope_reframe",
            source_path=path,
            content=evidence_lines(content),
            matching_terms=overlap,
            content_sha256=hashlib.sha256(content.encode("utf-8")).hexdigest(),
        )

    reframe_globs = (
        ".claude/science/physics-loops/**/HANDOFF.md",
        ".claude/science/physics-loops/**/BRANCH_HANDOFF.md",
        ".claude/science/physics-loops/**/CLAIM_STATUS_CERTIFICATE*.md",
    )
    reframe_paths = {ACTIVE_REVIEW_QUEUE}
    for pattern in reframe_globs:
        reframe_paths.update(path.relative_to(root).as_posix() for path in root.glob(pattern))
    reframe_hits: list[tuple[int, str, str, list[str]]] = []
    for path in sorted(reframe_paths):
        content = _read_text(root, path)
        overlap = sorted(current_terms.intersection(_search_terms(content)))
        if len(overlap) >= 2 and keyword_re.search(content):
            reframe_hits.append((len(overlap), path, content, overlap))
    ordered_reframe_hits = sorted(
        reframe_hits, key=lambda item: (-item[0], item[1])
    )
    candidate_id_universe.update(
        f"in_flight_reframe:{path}"
        for _score, path, _content, _overlap in ordered_reframe_hits
    )
    for _score, path, content, overlap in ordered_reframe_hits[
        :N6_CANDIDATE_LIMITS["in_flight_reframe"]
    ]:
        add_candidate(
            candidate_id=f"in_flight_reframe:{path}",
            kind="definition_refactor",
            source_path=path,
            content=evidence_lines(content),
            matching_terms=overlap,
            content_sha256=hashlib.sha256(content.encode("utf-8")).hexdigest(),
        )

    return json.dumps(
        {
            "schema": "no_go_partial_closure_index_v1",
            "claim_id": cid,
            "search_scope": {
                "foundation_registry": AXIOM_REGISTRY,
                "open_obligation_registry": OBLIGATION_REGISTRY,
                "controlled_vocabulary": {
                    "path": CONTROLLED_VOCABULARY,
                    "content_sha256": hashlib.sha256(vocabulary_text.encode("utf-8")).hexdigest(),
                    "minimum_shared_terms": 1,
                    "candidate_limit": N6_CANDIDATE_LIMITS["controlled_vocabulary"],
                },
                "meta_notes": {
                    "scanned_count": len(meta_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(meta_paths, separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "minimum_shared_terms": 2,
                    "candidate_limit": N6_CANDIDATE_LIMITS["meta_reframe"],
                    "evidence_line_limit_per_candidate": 5,
                },
                "claim_notes": {
                    "scanned_count": len(claim_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(claim_paths, separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "minimum_shared_terms": 2,
                    "candidate_limit": N6_CANDIDATE_LIMITS["claim_reframe"],
                    "evidence_line_limit_per_candidate": 5,
                },
                "repository_visible_in_flight_reframes": {
                    "queue_path": ACTIVE_REVIEW_QUEUE,
                    "globs": list(reframe_globs),
                    "scanned_count": len(reframe_paths),
                    "scanned_paths_sha256": hashlib.sha256(
                        json.dumps(sorted(reframe_paths), separators=(",", ":")).encode("utf-8")
                    ).hexdigest(),
                    "minimum_shared_terms": 2,
                    "candidate_limit": N6_CANDIDATE_LIMITS["in_flight_reframe"],
                    "evidence_line_limit_per_candidate": 5,
                },
            },
            # Candidate records remain capped above; full IDs are authenticated
            # solely so post-authentication growth is observable exactly.
            "candidate_id_universe": sorted(candidate_id_universe),
            "candidates": candidates,
        },
        indent=2,
        sort_keys=True,
    )


def build_evidence_manifest(
    row: dict[str, Any],
    ledger_rows: dict[str, dict],
    repo_root: str | Path,
) -> dict[str, dict]:
    """Build the exact source/runner/authority universe visible to the auditor."""
    root = Path(repo_root)
    manifest: dict[str, dict] = {}
    note_path = str(row.get("note_path") or "")
    _add_evidence(
        manifest,
        path=note_path,
        role="source",
        text=_read_text(root, note_path),
    )

    runner_path = _canonical_runner_path(root, row.get("runner_path"))
    _add_evidence(
        manifest,
        path=runner_path,
        role="runner",
        text=_read_text(root, runner_path),
    )
    for helper_raw in row.get("helper_runner_paths") or []:
        helper = _repo_local_helper_runner_path(root, helper_raw)
        if helper is None:
            continue
        _add_evidence(
            manifest,
            path=helper,
            role="helper",
            text=_read_text(root, helper),
        )

    for dep_id in row.get("deps") or []:
        dep = ledger_rows.get(dep_id, {})
        dep_path = str(dep.get("note_path") or "")
        _add_evidence(
            manifest,
            path=dep_path,
            role="authority",
            text=_read_text(root, dep_path),
            effective_status=dep.get("effective_status"),
            premise_type=premise_type_for_id(root, dep_id),
        )

    for registry_path, premise_type in (
        (AXIOM_REGISTRY, "axiom_or_approved_primitive"),
    ):
        registry = _load_json(root, registry_path)
        _add_evidence(
            manifest,
            path=registry_path,
            role="premise_registry",
            text=_read_text(root, registry_path),
            premise_type=premise_type,
        )
        for claim_id in registry.get("canonical_ids") or []:
            node = (registry.get("nodes") or {}).get(claim_id, {})
            current_path = str(node.get("current_path") or "")
            _add_evidence(
                manifest,
                path=current_path,
                role="framework_premise",
                text=_read_text(root, current_path),
                premise_type=premise_type,
            )

    _add_evidence(
        manifest,
        path=OBLIGATION_REGISTRY,
        role="open_obligation_registry",
        text=_read_text(root, OBLIGATION_REGISTRY),
    )
    cross_path = cross_cycle_index_path(str(row.get("claim_id") or ""))
    canonical_cross = build_cross_cycle_index(row, ledger_rows, root)
    cross_payload = json.loads(canonical_cross)
    cross_payload["canonical_index_sha256"] = hashlib.sha256(
        canonical_cross.encode("utf-8")
    ).hexdigest()
    cross_universe = cross_payload.pop("candidate_id_universe", [])
    # The complete no-go row set is authenticated by count and digest. The
    # verbose row list is transport metadata rather than auditor evidence.
    cross_no_go_rows = cross_payload.pop("no_go_row_universe", [])
    cross_payload["candidates"] = [
        _compact_cross_cycle_candidate(candidate, root)
        for candidate in cross_payload.get("candidates", [])
    ]
    _add_evidence(
        manifest,
        path=cross_path,
        role="cross_cycle_index",
        text=json.dumps(cross_payload, sort_keys=True, separators=(",", ":")),
    )
    manifest[cross_path]["cross_cycle_candidate_id_universe"] = cross_universe
    manifest[cross_path]["cross_cycle_no_go_row_universe"] = cross_no_go_rows

    partial_path = partial_closure_index_path(str(row.get("claim_id") or ""))
    canonical_partial = build_partial_closure_index(row, ledger_rows, root)
    partial_payload = json.loads(canonical_partial)
    partial_payload["canonical_index_sha256"] = hashlib.sha256(
        canonical_partial.encode("utf-8")
    ).hexdigest()
    partial_universe = partial_payload.pop("candidate_id_universe", [])
    partial_payload["candidates"] = [
        _compact_partial_closure_candidate(candidate)
        for candidate in partial_payload.get("candidates", [])
    ]
    _add_evidence(
        manifest,
        path=partial_path,
        role="partial_closure_index",
        text=json.dumps(partial_payload, sort_keys=True, separators=(",", ":")),
    )
    manifest[partial_path]["partial_closure_candidate_id_universe"] = partial_universe
    attach_full_scan_authentication(manifest, root)
    return manifest


def render_evidence_manifest(manifest: dict[str, dict]) -> str:
    visible = []
    for path in sorted(manifest):
        entry = manifest[path]
        visible.append(
            {
                "path": path,
                "roles": entry.get("roles") or [],
                "effective_status": entry.get("effective_status"),
                "accepted_premise_type": entry.get("accepted_premise_type"),
                "full_content_sha256": entry.get("full_content_sha256"),
                "full_phrase_groups": entry.get("full_phrase_groups") or [],
            }
        )
    return json.dumps(visible, indent=2, sort_keys=True)


def render_framework_premise_context(manifest: dict[str, dict]) -> str:
    blocks = []
    for path in sorted(manifest):
        entry = manifest[path]
        roles = set(entry.get("roles") or [])
        if not roles.intersection({"premise_registry", "framework_premise"}):
            continue
        blocks.append(
            f"=== BEGIN FRAMEWORK PREMISE CONTEXT: {path} ===\n"
            f"accepted_premise_type: {entry.get('accepted_premise_type')}\n"
            f"{entry.get('text') or '[missing registry/source content]'}\n"
            f"=== END FRAMEWORK PREMISE CONTEXT: {path} ==="
        )
    return "\n\n".join(blocks)


def _evidence_references(value: Any) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    if isinstance(value, dict):
        path = value.get("evidence_path")
        locator = value.get("evidence_locator")
        if _text(path) and _text(locator):
            refs.append((path, locator))
        for child in value.values():
            refs.extend(_evidence_references(child))
    elif isinstance(value, list):
        for child in value:
            refs.extend(_evidence_references(child))
    return refs


def _string_leaves(value: Any) -> set[str]:
    leaves: set[str] = set()
    if isinstance(value, str) and value.strip():
        leaves.add(value)
    elif isinstance(value, dict):
        for child in value.values():
            leaves.update(_string_leaves(child))
    elif isinstance(value, list):
        for child in value:
            leaves.update(_string_leaves(child))
    return leaves


def _index_candidates(
    entry: dict[str, Any], *, schema: str, stored_field: str,
    stored_records_field: str,
) -> dict[str, dict[str, Any]] | None:
    stored_records = entry.get(stored_records_field)
    if isinstance(stored_records, list):
        candidates = stored_records
    else:
        candidates = None
    stored = entry.get(stored_field)
    if candidates is None and isinstance(stored, list) and all(_text(item) for item in stored):
        return {str(item): {} for item in stored}
    if candidates is None:
        try:
            parsed = json.loads(str(entry.get("text") or ""))
        except json.JSONDecodeError:
            return None
        if not isinstance(parsed, dict):
            return None
        if parsed.get("schema") != schema:
            return None
        candidates = parsed.get("candidates")
    if not isinstance(candidates, list):
        return None
    mapped = {
        str(candidate.get("candidate_id")): candidate
        for candidate in candidates
        if isinstance(candidate, dict) and _text(candidate.get("candidate_id"))
    }
    if len(mapped) != len(candidates):
        return None
    return mapped


def _index_candidate_id_universe(
    entry: dict[str, Any], *, schema: str, universe_field: str,
    stored_field: str, stored_records_field: str,
) -> set[str] | None:
    """Return every candidate ID, including IDs omitted from capped records.

    Legacy snapshots predate ``candidate_id_universe``. Their listed IDs are
    the best available fallback (and legacy N8 snapshots were uncapped).
    """
    stored_universe = entry.get(universe_field)
    stored_set: set[str] | None = None
    if stored_universe is not None:
        if (
            not isinstance(stored_universe, list)
            or not all(_text(item) for item in stored_universe)
        ):
            return None
        stored_set = {str(item) for item in stored_universe}
        if len(stored_set) != len(stored_universe):
            return None
    rendered_text = str(entry.get("text") or "")
    parsed = None
    if rendered_text:
        try:
            parsed = json.loads(rendered_text)
        except json.JSONDecodeError:
            return None
        if not isinstance(parsed, dict) or parsed.get("schema") != schema:
            return None
    if isinstance(parsed, dict):
        rendered_universe = parsed.get("candidate_id_universe")
        if "candidate_id_universe" in parsed:
            if not isinstance(rendered_universe, list):
                return None
            if not all(_text(item) for item in rendered_universe):
                return None
            universe = {str(item) for item in rendered_universe}
            if len(universe) != len(rendered_universe):
                return None
            if stored_set is not None and stored_set != universe:
                return None
            return universe
    if stored_set is not None:
        return stored_set
    candidates = _index_candidates(
        entry,
        schema=schema,
        stored_field=stored_field,
        stored_records_field=stored_records_field,
    )
    return set(candidates) if candidates is not None else None


def _cross_cycle_candidate_ids(entry: dict[str, Any]) -> set[str] | None:
    candidates = _index_candidates(
        entry,
        schema="no_go_cross_cycle_index_v1",
        stored_field="cross_cycle_candidate_ids",
        stored_records_field="cross_cycle_candidates",
    )
    return set(candidates) if candidates is not None else None


def _cross_cycle_no_go_universe(entry: dict[str, Any]) -> tuple[int, str] | None:
    count = entry.get("no_go_row_universe_count")
    digest = entry.get("no_go_row_universe_sha256")
    if count is None or digest is None:
        try:
            payload = json.loads(str(entry.get("text") or ""))
        except json.JSONDecodeError:
            return None
        if not isinstance(payload, dict):
            # Fail closed: a JSON scalar/array in the fallback text cannot
            # carry the universe metadata; refusing here keeps callers from
            # aborting on a malformed index entry.
            return None
        count = payload.get("no_go_row_universe_count")
        digest = payload.get("no_go_row_universe_sha256")
    if (
        not isinstance(count, int)
        or count < 0
        or not isinstance(digest, str)
        or not re.fullmatch(r"[0-9a-f]{64}", digest)
    ):
        return None
    return count, digest


def _partial_closure_candidates(
    entry: dict[str, Any],
) -> dict[str, dict[str, Any]] | None:
    return _index_candidates(
        entry,
        schema="no_go_partial_closure_index_v1",
        stored_field="partial_closure_candidate_ids",
        stored_records_field="partial_closure_candidates",
    )


def build_evidence_snapshot(
    packet: dict[str, Any], manifest: dict[str, dict]
) -> dict[str, Any]:
    """Persist exact locators authenticated against the rendered packet."""
    grouped: dict[str, set[str]] = {}
    for path, locator in _evidence_references(packet):
        grouped.setdefault(path, set()).add(locator)
    entries: dict[str, dict[str, Any]] = {}
    packet_strings = _string_leaves(packet)
    for path, entry in sorted(manifest.items()):
        locators = grouped.get(path, set())
        text = str(entry.get("text") or "")
        snapshot_entry: dict[str, Any] = {
            "path": path,
            "roles": list(entry.get("roles") or []),
            "effective_status": entry.get("effective_status"),
            "accepted_premise_type": entry.get("accepted_premise_type"),
            "content_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "full_content_sha256": entry.get("full_content_sha256"),
            "full_phrase_groups": entry.get("full_phrase_groups") or [],
            "invocation_bound_rendered_text": bool(
                entry.get("invocation_bound_rendered_text")
            ),
            "verified_locators": sorted(locators),
            "verified_values": sorted(
                value for value in packet_strings if _norm(value) in _norm(text)
            ),
        }
        phrase_occurrences = required_phrase_occurrences(
            {path: entry},
            {"source", "authority"},
            tuple(dict.fromkeys((*N3_SCAN_PHRASES, *N5_SCAN_PHRASES))),
        )
        snapshot_entry["phrase_occurrences"] = [
            {
                "phrase": phrase,
                "occurrence_index": occurrence_index,
                "locator": locator,
            }
            for (_path, phrase, occurrence_index), locator
            in sorted(phrase_occurrences.items())
        ]
        if "cross_cycle_index" in set(entry.get("roles") or []):
            candidates = _index_candidates(
                entry, schema="no_go_cross_cycle_index_v1",
                stored_field="cross_cycle_candidate_ids",
                stored_records_field="cross_cycle_candidates",
            )
            if candidates is None:
                raise ValueError("cross-cycle index is not orchestrator-authenticated")
            snapshot_entry["cross_cycle_candidate_ids"] = sorted(candidates)
            snapshot_entry["cross_cycle_candidates"] = [
                candidates[candidate_id] for candidate_id in sorted(candidates)
            ]
            candidate_id_universe = _index_candidate_id_universe(
                entry,
                schema="no_go_cross_cycle_index_v1",
                universe_field="cross_cycle_candidate_id_universe",
                stored_field="cross_cycle_candidate_ids",
                stored_records_field="cross_cycle_candidates",
            )
            if (
                candidate_id_universe is None
                or not set(candidates).issubset(candidate_id_universe)
            ):
                raise ValueError(
                    "cross-cycle candidate-ID universe is not orchestrator-authenticated"
                )
            snapshot_entry["cross_cycle_candidate_id_universe"] = sorted(
                candidate_id_universe
            )
            try:
                cross_payload = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValueError("cross-cycle index JSON is malformed") from exc
            snapshot_entry["no_go_row_universe_count"] = cross_payload.get(
                "no_go_row_universe_count"
            )
            snapshot_entry["no_go_row_universe_sha256"] = cross_payload.get(
                "no_go_row_universe_sha256"
            )
            for field in (
                "transport_bounded_full_content_sha256",
                "transport_bounded_full_candidate_count",
                "transport_bounded_rendered_candidate_count",
                "transport_bounded_rendered_candidate_ids",
            ):
                if field in entry:
                    snapshot_entry[field] = entry[field]
        if "partial_closure_index" in set(entry.get("roles") or []):
            candidates = _partial_closure_candidates(entry)
            if candidates is None:
                raise ValueError("partial-closure index is not orchestrator-authenticated")
            snapshot_entry["partial_closure_candidate_ids"] = sorted(candidates)
            snapshot_entry["partial_closure_candidates"] = [
                candidates[candidate_id] for candidate_id in sorted(candidates)
            ]
            candidate_id_universe = _index_candidate_id_universe(
                entry,
                schema="no_go_partial_closure_index_v1",
                universe_field="partial_closure_candidate_id_universe",
                stored_field="partial_closure_candidate_ids",
                stored_records_field="partial_closure_candidates",
            )
            if (
                candidate_id_universe is None
                or not set(candidates).issubset(candidate_id_universe)
            ):
                raise ValueError(
                    "partial-closure candidate-ID universe is not orchestrator-authenticated"
                )
            snapshot_entry["partial_closure_candidate_id_universe"] = sorted(
                candidate_id_universe
            )
        entries[path] = snapshot_entry
    return {"schema": EVIDENCE_SNAPSHOT_SCHEMA, "entries": entries}


def evidence_snapshot_schema_defect(packet: dict[str, Any]) -> str | None:
    """Name the reason a snapshot cannot be read, distinguishing shapes.

    `evidence_manifest_from_snapshot` returns a bare None from ~25 validation
    points, so a snapshot written by an older writer and a genuinely corrupt
    one were indistinguishable in the invalidation reason. On 2026-07-11 the
    reader's required entry-field set was expanded under an unchanged schema
    tag; every snapshot already on disk became unreadable, and the resulting
    `no_go_discipline_packet_invalid` reason gave no way to tell a schema
    migration from evidence tampering. This reports the difference.
    """
    if not isinstance(packet, dict):
        return "packet is not an object"
    snapshot = packet.get("evidence_snapshot")
    if not isinstance(snapshot, dict):
        return "evidence_snapshot is absent or not an object"
    if snapshot.get("schema") != EVIDENCE_SNAPSHOT_SCHEMA:
        return f"evidence_snapshot schema is {snapshot.get('schema')!r}"
    raw_entries = snapshot.get("entries")
    if not isinstance(raw_entries, dict):
        return "evidence_snapshot entries is absent or not an object"
    for path in sorted(raw_entries):
        stored = raw_entries[path]
        if not isinstance(stored, dict):
            return f"entries[{path!r}] is not an object"
        absent = sorted(EVIDENCE_SNAPSHOT_ENTRY_REQUIRED_FIELDS - set(stored))
        if absent:
            return (
                f"entries[{path!r}] predates the current entry shape; "
                f"required fields absent: {', '.join(absent)}"
            )
    return None


def evidence_manifest_from_snapshot(packet: dict[str, Any]) -> dict[str, dict] | None:
    if not isinstance(packet, dict):
        return None
    snapshot = packet.get("evidence_snapshot")
    if not isinstance(snapshot, dict) or snapshot.get("schema") != EVIDENCE_SNAPSHOT_SCHEMA:
        return None
    raw_entries = snapshot.get("entries")
    if not isinstance(raw_entries, dict):
        return None
    manifest: dict[str, dict] = {}
    for path, stored in raw_entries.items():
        if not _text(path) or not isinstance(stored, dict):
            return None
        locators = stored.get("verified_locators")
        if not isinstance(locators, list) or not all(_text(x) for x in locators):
            return None
        values = stored.get("verified_values")
        if not isinstance(values, list) or not all(_text(x) for x in values):
            return None
        roles = stored.get("roles")
        if not isinstance(roles, list) or not all(_text(role) for role in roles):
            return None
        content_sha256 = stored.get("content_sha256")
        if not isinstance(content_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", content_sha256):
            return None
        phrase_occurrences = stored.get("phrase_occurrences")
        if not isinstance(phrase_occurrences, list):
            return None
        for occurrence in phrase_occurrences:
            if (
                not isinstance(occurrence, dict)
                or not _text(occurrence.get("phrase"))
                or not isinstance(occurrence.get("occurrence_index"), int)
                or occurrence["occurrence_index"] <= 0
                or not _text(occurrence.get("locator"))
            ):
                return None
        full_content_sha256 = stored.get("full_content_sha256")
        if full_content_sha256 is not None and (
            not isinstance(full_content_sha256, str)
            or not re.fullmatch(r"[0-9a-f]{64}", full_content_sha256)
        ):
            return None
        full_phrase_groups = stored.get("full_phrase_groups")
        if not isinstance(full_phrase_groups, list):
            return None
        for group in full_phrase_groups:
            if (
                not isinstance(group, dict)
                or not _text(group.get("phrase"))
                or not isinstance(group.get("occurrence_group_id"), str)
                or not re.fullmatch(r"[0-9a-f]{16}", group["occurrence_group_id"])
                or not isinstance(group.get("occurrence_count"), int)
                or group["occurrence_count"] < 1
                or not isinstance(group.get("occurrence_locator_sha256"), str)
                or not re.fullmatch(
                    r"[0-9a-f]{64}", group["occurrence_locator_sha256"]
                )
                or not _text(group.get("evidence_locator"))
            ):
                return None
        invocation_bound_rendered_text = stored.get(
            "invocation_bound_rendered_text", False
        )
        if not isinstance(invocation_bound_rendered_text, bool):
            return None
        for field in ("cross_cycle_candidates", "partial_closure_candidates"):
            if stored.get(field) is not None and not isinstance(stored[field], list):
                return None
        for field in (
            "cross_cycle_candidate_id_universe",
            "partial_closure_candidate_id_universe",
        ):
            universe_values = stored.get(field)
            if universe_values is not None and (
                not isinstance(universe_values, list)
                or not all(_text(item) for item in universe_values)
                or len(set(universe_values)) != len(universe_values)
            ):
                return None
        role_set = set(roles)
        for role, universe_field, schema, listed_field, records_field in (
            (
                "cross_cycle_index",
                "cross_cycle_candidate_id_universe",
                "no_go_cross_cycle_index_v1",
                "cross_cycle_candidate_ids",
                "cross_cycle_candidates",
            ),
            (
                "partial_closure_index",
                "partial_closure_candidate_id_universe",
                "no_go_partial_closure_index_v1",
                "partial_closure_candidate_ids",
                "partial_closure_candidates",
            ),
        ):
            stored_universe = stored.get(universe_field)
            if role not in role_set or stored_universe is None:
                continue
            listed_candidates = _index_candidates(
                stored,
                schema=schema,
                stored_field=listed_field,
                stored_records_field=records_field,
            )
            if (
                listed_candidates is None
                or not set(listed_candidates).issubset(set(stored_universe))
            ):
                return None
        universe_count = stored.get("no_go_row_universe_count")
        universe_sha256 = stored.get("no_go_row_universe_sha256")
        transport_full_sha = stored.get("transport_bounded_full_content_sha256")
        transport_full_count = stored.get("transport_bounded_full_candidate_count")
        transport_rendered_count = stored.get(
            "transport_bounded_rendered_candidate_count"
        )
        transport_rendered_ids = stored.get(
            "transport_bounded_rendered_candidate_ids"
        )
        if "cross_cycle_index" in set(roles):
            if not isinstance(universe_count, int) or universe_count < 0:
                return None
            if not isinstance(universe_sha256, str) or not re.fullmatch(
                r"[0-9a-f]{64}", universe_sha256
            ):
                return None
            transport_values = (
                transport_full_sha,
                transport_full_count,
                transport_rendered_count,
                transport_rendered_ids,
            )
            if any(value is not None for value in transport_values):
                if not (
                    isinstance(transport_full_sha, str)
                    and re.fullmatch(r"[0-9a-f]{64}", transport_full_sha)
                    and isinstance(transport_full_count, int)
                    and transport_full_count >= 0
                    and isinstance(transport_rendered_count, int)
                    and 0 <= transport_rendered_count <= transport_full_count
                    and isinstance(transport_rendered_ids, list)
                    and len(transport_rendered_ids) == transport_rendered_count
                    and all(_text(item) for item in transport_rendered_ids)
                    and len(set(transport_rendered_ids))
                    == len(transport_rendered_ids)
                ):
                    return None
        manifest[path] = {
            "path": path,
            "roles": list(roles),
            "text": "",
            "verified_locators": list(locators),
            "verified_values": list(values),
            "effective_status": stored.get("effective_status"),
            "accepted_premise_type": stored.get("accepted_premise_type"),
            "content_sha256": content_sha256,
            "full_content_sha256": full_content_sha256,
            "full_phrase_groups": full_phrase_groups,
            "invocation_bound_rendered_text": invocation_bound_rendered_text,
            "cross_cycle_candidate_ids": stored.get("cross_cycle_candidate_ids"),
            "cross_cycle_candidates": stored.get("cross_cycle_candidates"),
            "cross_cycle_candidate_id_universe": stored.get(
                "cross_cycle_candidate_id_universe"
            ),
            "no_go_row_universe_count": universe_count,
            "no_go_row_universe_sha256": universe_sha256,
            "transport_bounded_full_content_sha256": transport_full_sha,
            "transport_bounded_full_candidate_count": transport_full_count,
            "transport_bounded_rendered_candidate_count": transport_rendered_count,
            "transport_bounded_rendered_candidate_ids": transport_rendered_ids,
            "partial_closure_candidate_ids": stored.get("partial_closure_candidate_ids"),
            "partial_closure_candidates": stored.get("partial_closure_candidates"),
            "partial_closure_candidate_id_universe": stored.get(
                "partial_closure_candidate_id_universe"
            ),
            "phrase_occurrences": phrase_occurrences,
        }
    return manifest


def _transport_bounded_cross_cycle_error(
    stored: dict[str, Any], current: dict[str, Any]
) -> str | None:
    """Reauthenticate a rendered N8 prefix against the current full index."""
    full_text = str(current.get("text") or "")
    if hashlib.sha256(full_text.encode("utf-8")).hexdigest() != stored.get(
        "transport_bounded_full_content_sha256"
    ):
        return "transport-bounded N8 full index content drifted"
    try:
        payload = json.loads(full_text)
    except json.JSONDecodeError:
        return "transport-bounded N8 current full index is malformed"
    candidates = payload.get("candidates") if isinstance(payload, dict) else None
    if not isinstance(candidates, list):
        return "transport-bounded N8 current full index lacks candidates"
    candidate_ids = [
        str(candidate.get("candidate_id"))
        for candidate in candidates
        if isinstance(candidate, dict) and _text(candidate.get("candidate_id"))
    ]
    if len(candidate_ids) != len(candidates) or len(set(candidate_ids)) != len(candidate_ids):
        return "transport-bounded N8 current candidate ids are malformed"
    full_count = stored.get("transport_bounded_full_candidate_count")
    rendered_count = stored.get("transport_bounded_rendered_candidate_count")
    rendered_ids = stored.get("transport_bounded_rendered_candidate_ids")
    if full_count != len(candidates):
        return "transport-bounded N8 full candidate count drifted"
    if rendered_ids != candidate_ids[:rendered_count]:
        return "transport-bounded N8 rendered ids are not the authenticated prefix"
    stored_candidates = _index_candidates(
        stored,
        schema="no_go_cross_cycle_index_v1",
        stored_field="cross_cycle_candidate_ids",
        stored_records_field="cross_cycle_candidates",
    )
    expected_candidates = {
        candidate_ids[index]: candidates[index]
        for index in range(rendered_count)
    }
    if stored_candidates != expected_candidates:
        return "transport-bounded N8 rendered candidate records drifted"
    bounded_payload = dict(payload)
    bounded_payload["candidates"] = candidates[:rendered_count]
    bounded_text = json.dumps(bounded_payload, indent=2, sort_keys=True)
    if hashlib.sha256(bounded_text.encode("utf-8")).hexdigest() != stored.get(
        "content_sha256"
    ):
        return "transport-bounded N8 rendered prefix hash drifted"
    current_universe = _cross_cycle_no_go_universe(current)
    stored_universe = _cross_cycle_no_go_universe(stored)
    if current_universe != stored_universe:
        return "transport-bounded N8 no-go universe digest drifted"
    return None


def evidence_snapshot_current_error(
    packet: dict[str, Any],
    current_manifest: dict[str, dict],
    *,
    dynamic_index_drift_invalidates: bool = False,
) -> str | None:
    """Reauthenticate stable file-backed snapshot entries against current bytes.

    Dynamic-index (N6/N8) universes grow with every landed note, loop ledger,
    and vocabulary row, so by default their drift is NOT an invalidation —
    growth is re-audit signal (see evidence_snapshot_index_growth), never
    retroactive deletion of an authenticated verdict. Apply-time REPLAY
    rejection is the one caller that opts back in with
    dynamic_index_drift_invalidates=True: a stale replayed prompt manifest is
    rejected there precisely because the live indexes have moved on.
    2026-07-12 repair: the unconditional set-identity comparison decayed
    every clean audit within hours in an active repo, including
    doubly-confirmed cross-family cleans."""
    stored_manifest = evidence_manifest_from_snapshot(packet)
    if stored_manifest is None:
        defect = evidence_snapshot_schema_defect(packet)
        return (
            "evidence_snapshot is malformed or predates the current "
            f"authenticated schema ({defect or 'entry failed field validation'})"
        )
    stable_roles = {
        "source", "authority", "runner", "helper", "premise_registry",
        "framework_premise",
    }
    stored_stable_paths = {
        path for path, entry in stored_manifest.items()
        if stable_roles.intersection(set(entry.get("roles") or []))
    }
    current_stable_paths = {
        path for path, entry in current_manifest.items()
        if stable_roles.intersection(set(entry.get("roles") or []))
    }
    if stored_stable_paths != current_stable_paths:
        return "evidence_snapshot stable evidence path universe changed"
    for path, stored in stored_manifest.items():
        roles = set(stored.get("roles") or [])
        dynamic_index = bool(
            {"cross_cycle_index", "partial_closure_index"}.intersection(roles)
        )
        if not dynamic_index and not stable_roles.intersection(roles):
            # Live runner stdout is invocation-bound by the trusted transport
            # envelope, not reconstructed from repository state.
            continue
        current = current_manifest.get(path)
        if current is None:
            return f"evidence_snapshot path {path!r} is absent from the current packet"
        if dynamic_index and not dynamic_index_drift_invalidates:
            continue
        transport_bounded_cross = bool(
            dynamic_index
            and "cross_cycle_index" in roles
            and stored.get("transport_bounded_full_content_sha256")
        )
        if transport_bounded_cross:
            error = _transport_bounded_cross_cycle_error(stored, current)
            if error:
                return error
            continue
        if dynamic_index:
            current_text_hash = hashlib.sha256(
                str(current.get("text") or "").encode("utf-8")
            ).hexdigest()
            if current_text_hash != stored.get("content_sha256"):
                return f"evidence_snapshot rendered content drifted for {path!r}"
            if "cross_cycle_index" in roles:
                current_candidates = _index_candidates(
                    current, schema="no_go_cross_cycle_index_v1",
                    stored_field="cross_cycle_candidate_ids",
                    stored_records_field="cross_cycle_candidates",
                )
                stored_candidates = _index_candidates(
                    stored, schema="no_go_cross_cycle_index_v1",
                    stored_field="cross_cycle_candidate_ids",
                    stored_records_field="cross_cycle_candidates",
                )
            else:
                current_candidates = _partial_closure_candidates(current)
                stored_candidates = _partial_closure_candidates(stored)
            if current_candidates != stored_candidates:
                return f"evidence_snapshot candidate set drifted for {path!r}"
            continue
        if not stored.get("invocation_bound_rendered_text"):
            current_text_hash = hashlib.sha256(
                str(current.get("text") or "").encode("utf-8")
            ).hexdigest()
            if current_text_hash != stored.get("content_sha256"):
                return f"evidence_snapshot rendered content drifted for {path!r}"
        if not stable_roles.intersection(roles):
            continue
        if stored.get("full_content_sha256") is not None:
            if current.get("full_content_sha256") != stored.get("full_content_sha256"):
                return f"evidence_snapshot raw content hash drifted for {path!r}"
        if set(current.get("roles") or []) != roles:
            return f"evidence_snapshot roles drifted for {path!r}"
        if current.get("accepted_premise_type") != stored.get("accepted_premise_type"):
            return f"evidence_snapshot accepted_premise_type drifted for {path!r}"
        # Status churn BELOW the chain-satisfying line is not evidence decay.
        # A cited authority moving unaudited -> audit_in_progress, or between
        # terminal non-clean verdicts, changes nothing the packet reasoned
        # about, yet strict equality deleted the citing no-go verdict every
        # time the audit lane touched a dependency. Among non-chain-satisfying
        # statuses this now invalidates on rank DECREASE only, matching the
        # development tier (invalidate_stale_audits.detect_invalidation).
        #
        # Crossing the chain-satisfying line is different, and deliberately
        # still invalidates in BOTH directions. A no-go packet's N3 sorted
        # every scanned occurrence into retained_authority / hidden_admission /
        # non_load_bearing against the authority statuses of the day; once a
        # cited authority becomes retained-grade (or meta, or a decoration of a
        # retained parent) that sort is stale, because a now-retained authority
        # may already resolve the very wall the packet declares. Equal rank is
        # not safety either: retained -> retained_no_go and
        # decoration_under_A -> decoration_under_B both change which authority
        # the packet is standing on. Forcing re-audit there is the forensic
        # tier working, not the throughput defect this repair targets.
        stored_status = stored.get("effective_status")
        current_status = current.get("effective_status")
        if current_status != stored_status:
            touches_chain_line = snapshot_status_is_chain_satisfying(
                stored_status
            ) or snapshot_status_is_chain_satisfying(current_status)
            if touches_chain_line:
                return (
                    "evidence_snapshot effective_status moved at or across "
                    f"the chain-satisfying line for {path!r}: "
                    f"{stored_status} -> {current_status}"
                )
            if snapshot_status_rank(current_status) < snapshot_status_rank(
                stored_status
            ):
                return (
                    f"evidence_snapshot effective_status weakened for {path!r}: "
                    f"{stored_status} -> {current_status}"
                )
    return None


def evidence_snapshot_index_growth(
    packet: dict[str, Any], current_manifest: dict[str, dict]
) -> dict[str, list[str]]:
    """Non-invalidating evidence-universe changes needing targeted re-audit.

    Dynamic N6/N8 candidate growth and a scan-policy-only N5 group change are
    dispatch signals. Neither retroactively invalidates the authenticated
    verdict; stable source-byte drift is handled separately by
    :func:`evidence_snapshot_current_error`.
    """
    stored_manifest = evidence_manifest_from_snapshot(packet)
    growth: dict[str, list[str]] = {}
    if stored_manifest is None:
        return growth
    for path, stored in stored_manifest.items():
        roles = set(stored.get("roles") or [])
        current_entry = current_manifest.get(path)
        # A path absent from the current manifest is evidence LOSS, not
        # growth. Reading it as `{}` would make effective_status None, which
        # snapshot_status_rank maps to the unaudited default (30) and would
        # fabricate `authority_strengthened` for anything stored below that.
        # `evidence_snapshot_current_error` rejects absent stable paths before
        # the one production caller reaches here; this keeps the function
        # honest when called on its own.
        if current_entry is None:
            continue
        # A cited authority that gained strength below the chain-satisfying
        # line is recorded as a targeted re-audit candidate rather than
        # deleting the verdict (see `evidence_snapshot_current_error`).
        # NOTE: `no_go_index_growth_targets.json` is written by
        # invalidate_stale_audits but no dispatcher stage consumes it yet, so
        # this is a recorded artifact, not a wired re-audit trigger. Do not
        # rely on it as a safety backstop.
        stored_status = stored.get("effective_status")
        current_status = current_entry.get("effective_status")
        if current_status != stored_status and snapshot_status_rank(
            current_status
        ) > snapshot_status_rank(stored_status):
            growth.setdefault(path, []).append(
                f"authority_strengthened:{stored_status}->{current_status}"
            )
        if "source" in roles and (
            stored.get("full_content_sha256")
            == current_entry.get("full_content_sha256")
        ):
            def n5_groups(entry: dict[str, Any]) -> set[tuple[str, str, str]]:
                return {
                    (
                        phrase,
                        group_id,
                        str(group.get("occurrence_locator_sha256") or ""),
                    )
                    for (_path, phrase, group_id), group in required_phrase_groups(
                        {path: entry}, {"source"}, N5_SCAN_PHRASES
                    ).items()
                }

            stored_groups = n5_groups(stored)
            current_groups = n5_groups(current_entry)
            scan_changes = [
                f"n5_group_removed:{phrase}:{group_id}:{digest[:12]}"
                for phrase, group_id, digest in sorted(stored_groups - current_groups)
            ] + [
                f"n5_group_added:{phrase}:{group_id}:{digest[:12]}"
                for phrase, group_id, digest in sorted(current_groups - stored_groups)
            ]
            if scan_changes:
                # extend, not assign: a plain assignment here discards any
                # signal already recorded for this path earlier in the loop.
                growth.setdefault(path, []).extend(scan_changes)
        if "cross_cycle_index" in roles:
            current_candidates = _index_candidate_id_universe(
                current_entry,
                schema="no_go_cross_cycle_index_v1",
                universe_field="cross_cycle_candidate_id_universe",
                stored_field="cross_cycle_candidate_ids",
                stored_records_field="cross_cycle_candidates",
            )
            stored_candidates = _index_candidate_id_universe(
                stored,
                schema="no_go_cross_cycle_index_v1",
                universe_field="cross_cycle_candidate_id_universe",
                stored_field="cross_cycle_candidate_ids",
                stored_records_field="cross_cycle_candidates",
            )
        elif "partial_closure_index" in roles:
            current_candidates = _index_candidate_id_universe(
                current_entry,
                schema="no_go_partial_closure_index_v1",
                universe_field="partial_closure_candidate_id_universe",
                stored_field="partial_closure_candidate_ids",
                stored_records_field="partial_closure_candidates",
            )
            stored_candidates = _index_candidate_id_universe(
                stored,
                schema="no_go_partial_closure_index_v1",
                universe_field="partial_closure_candidate_id_universe",
                stored_field="partial_closure_candidate_ids",
                stored_records_field="partial_closure_candidates",
            )
        else:
            continue
        new_ids = sorted(
            set(current_candidates or set()) - set(stored_candidates or set())
        )
        if new_ids:
            growth.setdefault(path, []).extend(new_ids)
    return growth


def _has_governed_no_existence(text: str) -> bool:
    def governed(subject: str) -> bool:
        if BOUNDARY_ABSENCE_SUBJECT_RE.search(subject):
            return False
        if UNIQUENESS_SUBJECT_RE.match(subject):
            # "no other/second X exists" is a positive uniqueness clause
            # when X is a mathematical object. The object before the first
            # preposition decides: "no other route through the premise set"
            # gates on route; "no other representation of the path algebra"
            # stays positive even though "path" appears as a modifier.
            tokens = subject.strip().split()
            for index, token in enumerate(tokens):
                if token.lower() in {
                    "of", "for", "to", "through", "from", "under",
                    "in", "within", "using", "given", "between",
                }:
                    tokens = tokens[:index]
                    break
            while tokens and tokens[-1].lower() in {"whatsoever", "at", "all"}:
                tokens.pop()
            head = tokens[-1] if tokens else ""
            if not AUTHORITY_UNIQUENESS_SUBJECT_RE.fullmatch(head):
                return False
        return True

    for match in NO_EXISTENCE_ASSERTION_RE.finditer(text):
        tail = text[match.end(): match.end() + 60]
        span = match.group(0) + tail
        if re.search(
            r"\b(?:for|to)\s+(?:deriv|produc|obtain|reach|suppl|select|"
            r"clos|recover|construct)",
            span,
            re.IGNORECASE,
        ):
            # "no other X exists for deriving Y" asserts route absence
            # whatever noun names the route.
            return True
        if governed(match.group("subject")):
            return True
    return False


def _has_forced_spectral_boundary(text: str) -> bool:
    """Detect affirmative spectral-cardinality bounds, not questions/denials."""
    for pattern in FORCED_SPECTRAL_BOUNDARY_RES:
        for match in pattern.finditer(text):
            clause_start = max(
                text.rfind(mark, 0, match.start()) for mark in "\n.;:!?"
            ) + 1
            clause_end_candidates = [
                index for mark in "\n.;:!?"
                if (index := text.find(mark, match.end())) >= 0
            ]
            clause_end = min(clause_end_candidates, default=len(text))
            clause = text[clause_start:clause_end]
            prefix = text[clause_start:match.start()]
            prefix = re.split(
                r"\b(?:and|but|yet|because|although|though|while|whereas|since|so)\b",
                prefix,
                flags=re.IGNORECASE,
            )[-1]
            if "?" in text[clause_start:clause_end + 1]:
                continue
            if SPECTRAL_QUESTION_PREFIX_RE.search(clause):
                continue
            if SPECTRAL_NEGATION_PREFIX_RE.search(prefix):
                continue
            return True
    return False


def _has_negative_boundary_assertion(text: str) -> bool:
    # Inline Markdown/TeX delimiters are presentation, not grammar. Removing
    # them lets `kappa_EW`, `$Z$`, and route labels such as `(S1)-(S3)` use the
    # same governed subject rules as plain prose.
    prose = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    prose = re.sub(
        r"`[^`\n]*(?:[/_.]|\.(?:py|md|json|txt))[^`\n]*`", "", prose
    )
    prose = re.sub(
        r"\b[\w./-]*(?:firewall|no[-_]?go)[\w./-]*\.(?:py|md|json|txt)\b",
        "",
        prose,
        flags=re.IGNORECASE,
    )
    prose = re.sub(r"(?m)^\s*[^\n.!?]*\?\s*$", "", prose)
    prose = re.sub(
        r"(?im)^\s*(?:see|refer\s+to|compare|cf\.)\b[^\n:;.!?]*"
        r"\b(?:no[- ]?go|obstruction|firewall)\b[^\n:;.!?]*[.!]?\s*$",
        "",
        prose,
    )
    prose = re.sub(
        r"(?im)^\s*(?:the\s+)?(?:runner|script|implementation|renderer|tool)\s+"
        r"(?:does\s+not|cannot|fails?\s+to)\s+"
        r"(?:produce|render|write|emit|plot|display)\s+"
        r"(?:plots?|figures?|charts?|files?|artifacts?|logs?|output|stdout|stderr|"
        r"markdown|json|images?|tables?|labels?|links?)\b[^\n:;.!?]*[.!]?\s*$",
        "",
        prose,
    )
    normalized = re.sub(r"[`*_~$(){}\[\]]", "", prose)
    normalized = CONTRACTION_RE.sub(lambda m: m.group(1) + " not", normalized)
    normalized = CANT_RE.sub("can not", normalized)
    normalized = re.sub(r"\bwon[\u2019']t\b", "will not", normalized, flags=re.IGNORECASE)
    for idiom in POLARITY_IDIOM_PRESCRUBS:
        normalized = idiom.sub("certainly", normalized)
    for negated in NEGATED_PREDICATE_PRESCRUBS:
        normalized = negated.sub("", normalized)
    cleaned = NEGATED_NEGATIVE_ASSURANCE_RE.sub("", normalized)
    cleaned = NEGATED_LABEL_ASSURANCE_RE.sub("", cleaned)
    cleaned = _scrub_local_scope_exclusions(cleaned)
    cleaned = _scrub_removed_boundaries(cleaned)
    if (
        EXPLICIT_NEGATIVE_CLOSURE_RE.search(cleaned)
        or NEGATIVE_SUBJECT_CLOSURE_RE.search(cleaned)
        or _has_forced_spectral_boundary(cleaned)
        or SPECTRAL_EXCLUSION_RE.search(cleaned)
        or _has_governed_no_existence(cleaned)
        or INABILITY_CLOSURE_RE.search(cleaned)
        or BOUNDARY_SUBJECT_NEGATIVE_RE.search(cleaned)
    ):
        return True
    cleaned = POSITIVE_BOUNDARY_CLOSURE_RE.sub("", cleaned)
    cleaned = NEGATED_BOUNDARY_RE.sub("", cleaned)
    if NEGATIVE_ASSERTION_RE.search(cleaned):
        return True
    # Only the bare coverage-verb class remains. Remove the honest-scoping
    # surfaces the policy does not gate — canonical disclaimer sections,
    # labeled disclaimer payloads, and note-subject coverage clauses — each
    # subject to the authority-payload veto, then re-check. Soft-wrapped
    # lines are joined so a clause cannot hide its authority source behind
    # a line break.
    scrubbed = _strip_disclaimer_sections(cleaned)
    scrubbed = _scrub_labeled_disclaimer_lines(scrubbed)
    scrubbed = re.sub(r"(?<!\n)\n(?!\n)", " ", scrubbed)
    scrubbed = _scrub_note_subject_clauses(scrubbed)
    return bool(NEGATIVE_COVERAGE_VERB_RE.search(scrubbed))


def forensic_mode() -> bool:
    """Freeze/certification runs force the forensic tier lane-wide.

    Two-tier assurance (2026-07-12, owner-approved): the development tier
    binds verdicts to claim content (hashes, structural packet validation,
    two independent passes) so working assurance survives repo growth; the
    forensic tier (heavyweight N1-N8 with authenticated evidence surfaces)
    is mandatory for no-go rows — where foreclosure is permanent — and for
    freeze/certification runs over a whole lane at a pinned commit.
    """
    return str(os.environ.get("AUDIT_FORENSIC_MODE") or "").strip().lower() in {
        "1", "true", "yes",
    }


def source_is_no_go_artifact(
    note_path: str | None,
    note_body: str | None,
    claim_type_hint: str | None,
) -> bool:
    body = note_body or ""
    metadata = "\n".join(body.splitlines()[:80])
    metadata = re.sub(r"[`*~]", "", metadata)
    explicit_type = re.search(
        r"(?:Type|Claim type)\s*:\s*`?([a-z_]+)`?", metadata, re.IGNORECASE
    )
    explicit_claim_type = explicit_type.group(1).casefold() if explicit_type else None
    if claim_type_hint == "no_go" or explicit_claim_type == "no_go":
        return True
    path_text = re.sub(r"[_-]+", " ", note_path or "")
    if PATH_TRIGGER_RE.search(path_text):
        # Filename-level no-go authority is always forensic.  A source may
        # explain that an older reading was withdrawn, but that prose cannot
        # silently downgrade the assurance tier of the no-go-named artifact.
        return True
    return False


def source_requires_no_go_discipline(
    note_path: str | None,
    note_body: str | None,
    claim_type_hint: str | None,
) -> bool:
    body = note_body or ""
    if source_is_no_go_artifact(note_path, body, claim_type_hint):
        return True
    # Wall-naming positive/bounded rows carry the mandatory heavy packet only
    # in the forensic tier; in the development tier the auditor still applies
    # the no-go discipline as judgment (skill rule) and any supplied packet is
    # validated structurally.
    if forensic_mode():
        return _has_negative_boundary_assertion(body)
    return False


def output_requires_no_go_discipline(audit: dict[str, Any]) -> bool:
    if audit.get("claim_type") == "no_go":
        return True
    boundary = "\n".join(str(audit.get(field) or "") for field in OUTPUT_BOUNDARY_FIELDS)
    if _has_negative_boundary_assertion(boundary):
        return True
    return _has_negative_boundary_assertion(
        str(audit.get("notes_for_re_audit_if_any") or "")
    )


def packet_requirement_binds(
    audit: dict[str, Any], *, source_required: bool = False
) -> bool:
    """Whether a triggered structured-packet demand binds this verdict.

    No-go artifacts (source-required rows, no_go claim-type judgments) and
    forensic-tier runs carry the mandatory packet for every verdict. In the
    development tier, the wall-naming output/declaration trigger binds only
    claim-cementing `audited_clean` verdicts: non-clean verdicts are the
    repair queue — they foreclose nothing and re-enter fresh audit — so the
    wall-naming judgment stays in the verdict prose there, and a supplied
    packet is still validated structurally.
    """
    if source_required or audit.get("claim_type") == "no_go" or forensic_mode():
        return True
    verdict = audit.get("verdict") or audit.get("audit_status")
    return verdict == "audited_clean"


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _list(value: Any) -> bool:
    return isinstance(value, list)


def _norm(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def _semantic_norm(value: str) -> str:
    normalized = re.sub(
        r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|first|second|third|fourth|fifth)\b|\d+",
        " ",
        value.casefold(),
    )
    normalized = re.sub(r"[^a-z]+", " ", normalized)
    return _norm(normalized)


def _entry_contains(entry: dict[str, Any], value: str) -> bool:
    if _norm(value) in _norm(str(entry.get("text") or "")):
        return True
    return any(
        _norm(value) == _norm(candidate)
        for candidate in entry.get("verified_values") or []
        if _text(candidate)
    ) or any(
        _norm(value) in {
            _norm(str(group.get("phrase") or "")),
            _norm(str(group.get("evidence_locator") or "")),
        }
        for group in entry.get("full_phrase_groups") or []
        if isinstance(group, dict)
    )


def _accepted_premise_entry(entry: dict[str, Any]) -> bool:
    return entry.get("accepted_premise_type") in PRIOR_AUTHORITY_PREMISE_TYPES


def n3_scan_paths(manifest: dict[str, dict] | None) -> set[str]:
    """Return source/ordinary-authority paths requiring hidden-wall review.

    Axiom and approved-primitive texts are explicit accepted premises and are
    separately guarded by premise purity. Their premise vocabulary is not a
    hidden admission in the audited claim, so N3 does not enumerate it again.
    """
    if manifest is None:
        return set()
    return {
        path
        for path, entry in manifest.items()
        if {"source", "authority"}.intersection(set(entry.get("roles") or []))
        and not _accepted_premise_entry(entry)
    }


def required_n3_phrase_groups(
    manifest: dict[str, dict] | None,
) -> dict[tuple[str, str, str], dict[str, Any]]:
    if manifest is None:
        return {}
    groups = required_phrase_groups(
        manifest, {"source", "authority"}, N3_SCAN_PHRASES
    )
    paths = n3_scan_paths(manifest)
    return {key: value for key, value in groups.items() if key[0] in paths}


def _scan_coverage_error(
    section: dict[str, Any],
    manifest: dict[str, dict] | None,
    roles: set[str],
    label: str,
    *,
    exclude_accepted_premises: bool = False,
) -> str | None:
    scanned = section.get("scanned_evidence_paths")
    if not isinstance(scanned, list) or not all(_text(path) for path in scanned):
        return f"{label}.scanned_evidence_paths must be a list of packet paths"
    if len(set(scanned)) != len(scanned):
        return f"{label}.scanned_evidence_paths contains duplicates"
    if manifest is None:
        return None
    required = {
        path
        for path, entry in manifest.items()
        if roles.intersection(set(entry.get("roles") or []))
        and not (
            exclude_accepted_premises and _accepted_premise_entry(entry)
        )
    }
    if set(scanned) != required:
        return f"{label}.scanned_evidence_paths must exactly cover {sorted(required)}"
    return None


def required_phrase_occurrences(
    manifest: dict[str, dict] | None,
    roles: set[str],
    phrases: tuple[str, ...],
) -> dict[tuple[str, str, int], str]:
    """Return every orchestrator-visible phrase occurrence and exact locator."""
    if manifest is None:
        return {}
    required: dict[tuple[str, str, int], str] = {}
    for path, entry in manifest.items():
        if not roles.intersection(set(entry.get("roles") or [])):
            continue
        text = str(entry.get("text") or "")
        if not text and isinstance(entry.get("phrase_occurrences"), list):
            for occurrence in entry["phrase_occurrences"]:
                if not isinstance(occurrence, dict):
                    continue
                phrase = occurrence.get("phrase")
                index = occurrence.get("occurrence_index")
                locator = occurrence.get("locator")
                if phrase in phrases and isinstance(index, int) and index > 0 and _text(locator):
                    # Stored occurrences are authenticated forensic evidence.
                    # Never reinterpret an archived snapshot under a newer
                    # scan policy; calibration applies only to fresh text.
                    required[(path, _norm(phrase), index)] = locator
            continue
        lines = text.splitlines()
        for phrase in phrases:
            pattern = r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b"
            occurrence_index = 0
            for line_index, line in enumerate(lines):
                for _match in re.finditer(pattern, line, re.IGNORECASE):
                    occurrence_index += 1
                    locator = line.strip()
                    if len(_norm(locator)) < 12:
                        start = max(0, line_index - 1)
                        stop = min(len(lines), line_index + 2)
                        locator = " ".join(
                            part.strip() for part in lines[start:stop] if part.strip()
                        )
                    # Administrative scope negations are not negative rhetoric
                    # about the physics; keep positional indices stable but do
                    # not authenticate them into the N5 universe.
                    if n5_administrative_negation(phrase, locator):
                        continue
                    required[(path, _norm(phrase), occurrence_index)] = locator[:400]
    return required


def required_phrase_groups(
    manifest: dict[str, dict], roles: set[str], phrases: tuple[str, ...]
) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Group only occurrences with identical normalized local context."""
    authenticated: dict[tuple[str, str, str], dict[str, Any]] = {}
    requested = {_norm(phrase) for phrase in phrases}
    for path, entry in manifest.items():
        if not roles.intersection(set(entry.get("roles") or [])):
            continue
        groups = entry.get("full_phrase_groups")
        if not isinstance(groups, list):
            continue
        for group in groups:
            if not isinstance(group, dict) or _norm(str(group.get("phrase") or "")) not in requested:
                continue
            phrase = _norm(str(group["phrase"]))
            group_id = str(group.get("occurrence_group_id") or "")
            if not group_id:
                continue
            authenticated[(path, phrase, group_id)] = {
                "occurrence_group_id": group_id,
                "occurrence_count": group.get("occurrence_count"),
                "occurrence_locator_sha256": group.get("occurrence_locator_sha256"),
                "evidence_locator": group.get("evidence_locator"),
            }
    if authenticated:
        return authenticated

    occurrences = required_phrase_occurrences(manifest, roles, phrases)
    grouped: dict[tuple[str, str, str], list[tuple[int, str]]] = {}
    for (path, phrase, occurrence_index), locator in occurrences.items():
        context_digest = hashlib.sha256(_norm(locator).encode("utf-8")).hexdigest()
        group_id = context_digest[:16]
        grouped.setdefault((path, phrase, group_id), []).append(
            (occurrence_index, locator)
        )
    result: dict[tuple[str, str, str], dict[str, Any]] = {}
    for key, items in grouped.items():
        ordered = sorted(items)
        digest_payload = json.dumps(ordered, ensure_ascii=False, separators=(",", ":"))
        result[key] = {
            "occurrence_group_id": key[2],
            "occurrence_count": len(ordered),
            "occurrence_locator_sha256": hashlib.sha256(
                digest_payload.encode("utf-8")
            ).hexdigest(),
            "evidence_locator": ordered[0][1],
        }
    return result


def attach_full_scan_authentication(
    manifest: dict[str, dict], repo_root: str | Path
) -> None:
    """Bind stable file evidence to raw bytes before any display clipping."""
    root = Path(repo_root)
    phrases = tuple(dict.fromkeys((*N3_SCAN_PHRASES, *N5_SCAN_PHRASES)))
    for path, entry in manifest.items():
        roles = set(entry.get("roles") or [])
        if not roles.intersection({
            "source", "authority", "runner", "helper", "premise_registry",
            "framework_premise",
        }):
            continue
        text = str(entry.get("text") or "")
        entry["full_content_sha256"] = _read_bytes_sha256(root, path)
        if not {"source", "authority"}.intersection(roles):
            entry["full_phrase_groups"] = []
            continue
        groups = required_phrase_groups(
            {path: {**entry, "full_phrase_groups": None}},
            {"source", "authority"},
            phrases,
        )
        entry["full_phrase_groups"] = [
            {
                "phrase": phrase,
                **group,
            }
            for (_path, phrase, _group_id), group in sorted(groups.items())
        ]


def _unknown_fields(value: dict[str, Any], allowed: set[str], label: str) -> str | None:
    unknown = set(value) - allowed
    if unknown:
        return f"{label} contains unknown fields {sorted(unknown)}"
    return None


def _scope_tokens(value: str) -> set[str]:
    stop = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with"}
    return {
        token
        for token in re.findall(r"[a-z0-9_]+", value.casefold())
        if token not in stop
    }


LOGICAL_SCOPE_TOKENS = {
    "all", "any", "cannot", "except", "no", "none", "not", "only",
    "unless", "without", "fail", "fails", "failed", "unable", "insufficient",
    "impossible", "never", "absence", "nonexistence", "impossibility",
    "failure", "lack",
    "non", "derivability", "underdetermination", "inability", "supply", "closure",
}


def _none_found_error(section: dict, items: list[Any], label: str) -> str | None:
    if items:
        return None
    if not _text(section.get("none_found_reason")):
        return f"{label} requires an explicit none_found_reason when its result list is empty"
    return None


def _locator_error(
    evidence_path: Any,
    evidence_locator: Any,
    manifest: dict[str, dict] | None,
    label: str,
) -> str | None:
    if not _text(evidence_path) or not _text(evidence_locator):
        return f"{label} requires non-empty evidence_path and evidence_locator"
    if len(_norm(evidence_locator)) < 12:
        return f"{label} evidence_locator must contain at least 12 normalized characters"
    if manifest is None:
        return None
    entry = manifest.get(evidence_path)
    if not entry:
        return f"{label} evidence_path {evidence_path!r} is outside the restricted packet"
    if not _entry_contains(entry, evidence_locator):
        return f"{label} evidence_locator is not present in {evidence_path!r}"
    return None


def _unresolved_error(section: dict, label: str, status: str) -> str | None:
    unresolved = section.get("unresolved")
    if not _list(unresolved) or not all(_text(item) for item in unresolved):
        return f"{label}.unresolved must be a list of non-empty strings"
    if status == "PASS" and unresolved:
        return f"No-Go Discipline PASS requires {label}.unresolved to be empty"
    return None


def _validate_n1(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    routes = packet.get("N1_alternative_routes")
    if not _list(routes):
        return "N1_alternative_routes must be a list"
    route_ids: set[str] = set()
    route_classes: set[str] = set()
    for index, route in enumerate(routes, 1):
        if not isinstance(route, dict):
            return f"N1 route {index} must be an object"
        error = _unknown_fields(
            route,
            {
                "route_id", "route_class", "mechanism", "attempt", "outcome",
                "honesty_marker", "disposition", "prior_witness_id",
                "evidence_path", "evidence_locator",
            },
            f"N1 route {index}",
        )
        if error:
            return error
        for field in (
            "route_id",
            "route_class",
            "mechanism",
            "attempt",
            "outcome",
            "honesty_marker",
            "disposition",
        ):
            if not _text(route.get(field)):
                return f"N1 route {index}.{field} must be non-empty"
        route_id = _norm(route["route_id"])
        route_class = route["route_class"].strip()
        if route_id in route_ids:
            return f"N1 route_id {route['route_id']!r} is duplicated"
        if route_class not in ROUTE_CLASSES:
            return f"N1 route {index}.route_class must be one of {sorted(ROUTE_CLASSES)}"
        route_semantics = " ".join(
            str(route.get(field) or "") for field in ("mechanism", "attempt", "outcome")
        )
        if not route_class_marker_matches(route_class, route_semantics):
            return (
                f"N1 route {index}.route_class={route_class!r} is not supported "
                "by its evidenced mechanism/attempt/outcome vocabulary"
            )
        marker = route["honesty_marker"].strip().upper()
        disposition = route["disposition"].strip().upper()
        if marker not in HONESTY_MARKERS:
            return f"N1 route {index}.honesty_marker is invalid"
        if disposition not in ROUTE_DISPOSITIONS:
            return f"N1 route {index}.disposition is invalid"
        error = _locator_error(
            route.get("evidence_path"), route.get("evidence_locator"), manifest, f"N1 route {index}"
        )
        if error:
            return error
        if manifest is not None:
            entry = manifest[route["evidence_path"]]
            for field in ("mechanism", "attempt", "outcome"):
                if not _entry_contains(entry, route[field]):
                    return f"N1 route {index}.{field} is not evidenced at evidence_path"
            if marker == "ATTEMPTED" and "runner_stdout" not in set(
                entry.get("roles") or []
            ):
                return (
                    f"N1 route {index} ATTEMPTED must cite current-cycle "
                    "live runner_stdout evidence"
                )
        if manifest is not None and marker == "RULED OUT BY PRIOR":
            entry = manifest[route["evidence_path"]]
            roles = set(entry.get("roles") or [])
            if not roles.intersection({"authority", "framework_premise", "premise_registry"}):
                return (
                    f"N1 route {index} RULED OUT BY PRIOR must cite a retained "
                    "one-hop authority or registered accepted premise"
                )
            if (
                entry.get("effective_status") not in RETAINED_GRADE
                and entry.get("accepted_premise_type") not in PRIOR_AUTHORITY_PREMISE_TYPES
            ):
                return f"N1 route {index} prior authority is not retained-grade or an accepted premise"
            if not _text(route.get("prior_witness_id")):
                return f"N1 route {index} RULED OUT BY PRIOR requires prior_witness_id"
        if status == "PASS" and disposition != "CLOSED":
            return f"No-Go Discipline PASS cannot contain N1 route {index} disposition={disposition}"
        route_ids.add(route_id)
        route_classes.add(route_class)
    if status == "PASS" and len(route_classes) < 5:
        return "No-Go Discipline PASS requires at least 5 distinct route_class values"
    mechanisms = [_semantic_norm(route["mechanism"]) for route in routes]
    attempts = [_semantic_norm(route["attempt"]) for route in routes]
    if not all(mechanisms) or not all(attempts):
        return "N1 mechanisms and attempts must contain semantic content beyond numbering"
    if len(set(mechanisms)) != len(mechanisms):
        return "N1 routes must name distinct mechanisms, not numbered paraphrases"
    if len(set(attempts)) != len(attempts):
        return "N1 routes must record distinct attempts, not duplicate prose"
    return None


def _section(packet: dict, field: str) -> tuple[dict | None, str | None]:
    value = packet.get(field)
    if not isinstance(value, dict):
        return None, f"{field} must be an object"
    return value, None


def _validate_n2(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N2_wall_independence")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"walls", "pairwise_checks", "collapsed_wall_set", "unresolved", "evidence_path", "evidence_locator"},
        "N2",
    )
    if error:
        return error
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N2")
    if error:
        return error
    walls = section.get("walls")
    collapsed = section.get("collapsed_wall_set")
    checks = section.get("pairwise_checks")
    if not _list(walls) or not all(_text(w) for w in walls) or len({_norm(w) for w in walls}) != len(walls):
        return "N2.walls must be a list of distinct non-empty strings"
    if manifest is not None:
        entry = manifest.get(section["evidence_path"])
        if entry is None or any(not _entry_contains(entry, wall) for wall in walls):
            return "N2.walls must each be evidenced at N2.evidence_path"
    if not _list(collapsed) or not all(_text(w) for w in collapsed):
        return "N2.collapsed_wall_set must be a list of non-empty strings"
    wall_map = {_norm(w): w for w in walls}
    if any(_norm(w) not in wall_map for w in collapsed):
        return "N2.collapsed_wall_set must be a subset of walls"
    if not _list(checks):
        return "N2.pairwise_checks must be a list"
    expected_pairs = {frozenset((_norm(a), _norm(b))) for a, b in combinations(walls, 2)}
    seen_pairs = set()
    dependent_walls: set[str] = set()
    directional_edges: list[tuple[str, str]] = []
    equivalent_pairs: list[tuple[str, str]] = []
    closure_relation: dict[tuple[str, str], bool] = {}
    for index, check in enumerate(checks, 1):
        if not isinstance(check, dict) or not _text(check.get("left")) or not _text(check.get("right")):
            return f"N2 pairwise check {index} must name left and right walls"
        error = _unknown_fields(
            check,
            {
                "left", "right", "left_closes_right", "right_closes_left",
                "independent", "rationale", "evidence_path", "evidence_locator",
            },
            f"N2 pairwise check {index}",
        )
        if error:
            return error
        pair = frozenset((_norm(check["left"]), _norm(check["right"])))
        if pair not in expected_pairs or pair in seen_pairs:
            return f"N2 pairwise check {index} is duplicate or names unknown walls"
        for field in ("left_closes_right", "right_closes_left", "independent"):
            if not isinstance(check.get(field), bool):
                return f"N2 pairwise check {index}.{field} must be boolean"
        expected_independent = not check["left_closes_right"] and not check["right_closes_left"]
        if check["independent"] != expected_independent:
            return f"N2 pairwise check {index}.independent is inconsistent"
        left_wall = _norm(check["left"])
        right_wall = _norm(check["right"])
        closure_relation[(left_wall, right_wall)] = check["left_closes_right"]
        closure_relation[(right_wall, left_wall)] = check["right_closes_left"]
        if not _text(check.get("rationale")) or len(_norm(check["rationale"])) < 40:
            return f"N2 pairwise check {index}.rationale must explain the directional test"
        if _norm(check["left"]) not in _norm(check["rationale"]) or _norm(check["right"]) not in _norm(check["rationale"]):
            return f"N2 pairwise check {index}.rationale must name both walls"
        error = _locator_error(
            check.get("evidence_path"), check.get("evidence_locator"), manifest,
            f"N2 pairwise check {index}",
        )
        if error:
            return error
        if manifest is not None and not _entry_contains(
            manifest[check["evidence_path"]], check["rationale"]
        ):
            return f"N2 pairwise check {index}.rationale is not evidenced at evidence_path"
        if check["left_closes_right"] and check["right_closes_left"]:
            equivalent_pairs.append((_norm(check["left"]), _norm(check["right"])))
        elif check["left_closes_right"]:
            dependent_walls.add(_norm(check["right"]))
            directional_edges.append((_norm(check["left"]), _norm(check["right"])))
        elif check["right_closes_left"]:
            dependent_walls.add(_norm(check["left"]))
            directional_edges.append((_norm(check["right"]), _norm(check["left"])))
        seen_pairs.add(pair)
    if seen_pairs != expected_pairs:
        return "N2.pairwise_checks must cover every unordered wall pair"
    parent = {wall: wall for wall in wall_map}

    def find(wall: str) -> str:
        while parent[wall] != wall:
            parent[wall] = parent[parent[wall]]
            wall = parent[wall]
        return wall

    def union(left: str, right: str) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[max(left_root, right_root)] = min(left_root, right_root)

    for left, right in equivalent_pairs:
        union(left, right)
    components: dict[str, list[str]] = {}
    for wall in wall_map:
        components.setdefault(find(wall), []).append(wall)
    for root, members in components.items():
        for left, right in combinations(members, 2):
            if not (
                closure_relation[(left, right)]
                and closure_relation[(right, left)]
            ):
                return (
                    "N2 mutually closing walls must form a complete, "
                    "transitive equivalence component"
                )
        for outside in wall_map:
            if find(outside) == root:
                continue
            signatures = {
                (
                    closure_relation[(member, outside)],
                    closure_relation[(outside, member)],
                )
                for member in members
            }
            if len(signatures) != 1:
                return (
                    "N2 mutually closing walls must have congruent closure "
                    "relations with every third wall"
                )
    graph: dict[str, set[str]] = {find(wall): set() for wall in wall_map}
    dependent_components: set[str] = set()
    for source, target in directional_edges:
        source_root, target_root = find(source), find(target)
        if source_root == target_root:
            continue
        graph[source_root].add(target_root)
        dependent_components.add(target_root)
    visiting: set[str] = set()
    visited: set[str] = set()

    def has_cycle(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        if any(has_cycle(target) for target in graph[node]):
            return True
        visiting.remove(node)
        visited.add(node)
        return False

    if any(has_cycle(wall) for wall in graph):
        return "N2 directional closure relation must be acyclic"
    expected_collapsed = {
        sorted(members)[0]
        for root, members in components.items()
        if root not in dependent_components
    }
    if status == "PASS" and not expected_collapsed:
        return "No-Go Discipline PASS must retain at least one evidenced N2 wall"
    if {_norm(wall) for wall in collapsed} != expected_collapsed:
        return (
            "N2.collapsed_wall_set must retain exactly the walls not closed "
            "by a directional pairwise result"
        )
    return _unresolved_error(section, "N2", status)


def _validate_n3(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N3_hidden_wall_scan")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "hits", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N3",
    )
    if error:
        return error
    error = _scan_coverage_error(
        section,
        manifest,
        {"source", "authority"},
        "N3",
        exclude_accepted_premises=True,
    )
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N3.scan_scope must name the phrases and packet surfaces checked"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N3 scan")
    if error:
        return error
    hits = section.get("hits")
    if not _list(hits):
        return "N3.hits must be a list"
    error = _none_found_error(section, hits, "N3")
    if error:
        return error
    walls = {_norm(w) for w in packet["N2_wall_independence"].get("walls") or []}
    observed_hits: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, hit in enumerate(hits, 1):
        if not isinstance(hit, dict) or not _text(hit.get("phrase")):
            return f"N3 hit {index} must name a phrase"
        error = _unknown_fields(
            hit,
            {
                "phrase", "occurrence_group_id", "occurrence_count",
                "occurrence_locator_sha256",
                "classification", "promoted_wall",
                "rationale", "evidence_path", "evidence_locator",
            },
            f"N3 hit {index}",
        )
        if error:
            return error
        classification = hit.get("classification")
        if not isinstance(classification, str):
            return f"N3 hit {index}.classification is invalid"
        if classification not in {"retained_authority", "hidden_admission", "non_load_bearing"}:
            return f"N3 hit {index}.classification is invalid"
        if classification == "non_load_bearing" and (
            not _text(hit.get("rationale"))
            or len(_norm(hit["rationale"])) < 40
        ):
            return f"N3 hit {index}.rationale must explain why the occurrence is non-load-bearing"
        error = _locator_error(hit.get("evidence_path"), hit.get("evidence_locator"), manifest, f"N3 hit {index}")
        if error:
            return error
        if not isinstance(hit.get("occurrence_count"), int) or hit["occurrence_count"] <= 0:
            return f"N3 hit {index}.occurrence_count must be a positive integer"
        if not isinstance(hit.get("occurrence_group_id"), str) or not re.fullmatch(
            r"[0-9a-f]{16}", hit["occurrence_group_id"]
        ):
            return f"N3 hit {index}.occurrence_group_id must be a 16-hex context digest"
        if not isinstance(hit.get("occurrence_locator_sha256"), str) or not re.fullmatch(
            r"[0-9a-f]{64}", hit["occurrence_locator_sha256"]
        ):
            return f"N3 hit {index}.occurrence_locator_sha256 must be a SHA-256 digest"
        hit_key = (
            str(hit["evidence_path"]), _norm(hit["phrase"]),
            hit["occurrence_group_id"],
        )
        if hit_key in observed_hits:
            return f"N3 hit {index} duplicates a path/phrase occurrence disposition"
        observed_hits[hit_key] = {
            "occurrence_group_id": hit["occurrence_group_id"],
            "occurrence_count": hit["occurrence_count"],
            "occurrence_locator_sha256": hit["occurrence_locator_sha256"],
            "evidence_locator": hit["evidence_locator"],
        }
        if manifest is not None and not _entry_contains(
            manifest[hit["evidence_path"]], hit["phrase"]
        ):
            return f"N3 hit {index}.phrase is not evidenced at evidence_path"
        if manifest is not None and classification == "retained_authority":
            entry = manifest[hit["evidence_path"]]
            roles = set(entry.get("roles") or [])
            supported = (
                entry.get("effective_status") in RETAINED_GRADE
                or entry.get("accepted_premise_type") in PRIOR_AUTHORITY_PREMISE_TYPES
            )
            if not roles.intersection({"authority", "framework_premise", "premise_registry"}) or not supported:
                return f"N3 retained_authority hit {index} is not retained or accepted in the manifest"
        if classification == "hidden_admission":
            if not _text(hit.get("promoted_wall")) or _norm(hit["promoted_wall"]) not in walls:
                return f"N3 hidden admission {index} must be promoted into N2.walls"
    if manifest is not None:
        required_hits = required_n3_phrase_groups(manifest)
        if set(observed_hits) != set(required_hits):
            missing = sorted(set(required_hits) - set(observed_hits))
            extra = sorted(set(observed_hits) - set(required_hits))
            return f"N3.hits must exactly disposition orchestrator phrase scan; missing={missing}, extra={extra}"
        for hit_key, observed in observed_hits.items():
            if observed != required_hits[hit_key]:
                return f"N3 hit {hit_key} must match its authenticated occurrence group"
    return _unresolved_error(section, "N3", status)


def _validate_n4(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N4_residual_matching")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "witnesses", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N4",
    )
    if error:
        return error
    error = _scan_coverage_error(section, manifest, {"authority"}, "N4")
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N4.scan_scope must name the witness/residual surfaces checked"
    witnesses = section.get("witnesses")
    if not _list(witnesses):
        return "N4.witnesses must be a list"
    error = _none_found_error(section, witnesses, "N4")
    if error:
        return error
    witness_ids: set[str] = set()
    witness_routes: dict[str, str] = {}
    for index, witness in enumerate(witnesses, 1):
        if not isinstance(witness, dict):
            return f"N4 witness {index} must be an object"
        error = _unknown_fields(
            witness,
            {
                "witness_id", "route_id", "witness_residual", "claim_residual",
                "witness_residual_id", "claim_residual_id", "match",
                "evidence_path", "evidence_locator", "claim_evidence_path",
                "claim_evidence_locator",
            },
            f"N4 witness {index}",
        )
        if error:
            return error
        for field in (
            "witness_id", "route_id", "witness_residual", "claim_residual",
            "witness_residual_id", "claim_residual_id",
        ):
            if not _text(witness.get(field)):
                return f"N4 witness {index}.{field} must be non-empty"
        for field in ("witness_residual_id", "claim_residual_id"):
            if not re.fullmatch(r"residual:[a-z0-9_.:-]{6,128}", witness[field], re.I):
                return f"N4 witness {index}.{field} must be a stable residual:<id>"
        witness_id = _norm(witness["witness_id"])
        route_id = _norm(witness["route_id"])
        if witness_id in witness_ids:
            return f"N4 witness_id {witness['witness_id']!r} is duplicated"
        route_ids = {_norm(route.get("route_id") or "") for route in packet.get("N1_alternative_routes") or []}
        if route_id not in route_ids:
            return f"N4 witness {index}.route_id does not name an N1 route"
        if not isinstance(witness.get("match"), bool):
            return f"N4 witness {index}.match must be boolean"
        error = _locator_error(witness.get("evidence_path"), witness.get("evidence_locator"), manifest, f"N4 witness {index}")
        if error:
            return error
        error = _locator_error(
            witness.get("claim_evidence_path"),
            witness.get("claim_evidence_locator"),
            manifest,
            f"N4 witness {index} claim residual",
        )
        if error:
            return error
        if manifest is not None:
            witness_entry = manifest[witness["evidence_path"]]
            claim_entry = manifest[witness["claim_evidence_path"]]
            if "authority" not in set(witness_entry.get("roles") or []):
                return f"N4 witness {index} witness residual must cite an authority"
            if "source" not in set(claim_entry.get("roles") or []):
                return f"N4 witness {index} claim residual must cite the source"
            if not _entry_contains(witness_entry, witness["witness_residual"]):
                return f"N4 witness {index}.witness_residual is not evidenced at its path"
            if not _entry_contains(witness_entry, witness["witness_residual_id"]):
                return f"N4 witness {index}.witness_residual_id is not evidenced at its path"
            if not _entry_contains(claim_entry, witness["claim_residual"]):
                return f"N4 witness {index}.claim_residual is not evidenced in the source"
            if not _entry_contains(claim_entry, witness["claim_residual_id"]):
                return f"N4 witness {index}.claim_residual_id is not evidenced in the source"
        expected_match = (
            _norm(witness["witness_residual_id"]) == _norm(witness["claim_residual_id"])
            and _norm(witness["witness_residual"]) == _norm(witness["claim_residual"])
        )
        if witness["match"] != expected_match:
            return f"N4 witness {index}.match is inconsistent with the residual comparison"
        if status == "PASS" and not witness["match"]:
            return f"No-Go Discipline PASS cannot retain mismatched N4 witness {index}"
        witness_ids.add(witness_id)
        witness_routes[witness_id] = route_id
    for index, route in enumerate(packet.get("N1_alternative_routes") or [], 1):
        if str(route.get("honesty_marker") or "").strip().upper() != "RULED OUT BY PRIOR":
            continue
        witness_id = _norm(str(route.get("prior_witness_id") or ""))
        if witness_id not in witness_routes:
            return f"N1 route {index} prior_witness_id does not name an N4 witness"
        if witness_routes[witness_id] != _norm(str(route.get("route_id") or "")):
            return f"N1 route {index} prior_witness_id is linked to a different route"
        witness = next(
            item for item in witnesses
            if _norm(str(item.get("witness_id") or "")) == witness_id
        )
        if witness.get("evidence_path") != route.get("evidence_path"):
            return f"N1 route {index} prior witness must bind the same authority path"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N4 scan")
    return error or _unresolved_error(section, "N4", status)


def _validate_n5(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N5_rhetoric_audit")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "scanned_evidence_paths", "statements", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N5",
    )
    if error:
        return error
    error = _scan_coverage_error(section, manifest, {"source"}, "N5")
    if error:
        return error
    if not _text(section.get("scan_scope")):
        return "N5.scan_scope must name the negative rhetoric checked"
    statements = section.get("statements")
    if not _list(statements):
        return "N5.statements must be a list"
    error = _none_found_error(section, statements, "N5")
    if error:
        return error
    observed_statements: dict[tuple[str, str, str], dict[str, Any]] = {}
    for index, statement in enumerate(statements, 1):
        if not isinstance(statement, dict) or not _text(statement.get("phrase")):
            return f"N5 statement {index} must name a phrase"
        error = _unknown_fields(
            statement,
            {
                "phrase", "occurrence_group_id", "occurrence_count",
                "occurrence_locator_sha256",
                "resolution_classes_checked",
                "tested_resolutions", "untested_resolutions", "evidence_path",
                "evidence_locator", "resolution_evidence_path",
                "resolution_evidence_locator",
            },
            f"N5 statement {index}",
        )
        if error:
            return error
        if not _list(statement.get("tested_resolutions")) or not all(_text(x) for x in statement["tested_resolutions"]):
            return f"N5 statement {index}.tested_resolutions must be non-empty"
        classes = statement.get("resolution_classes_checked")
        if (
            not isinstance(classes, list)
            or not all(_text(item) for item in classes)
            or set(classes) != N5_RESOLUTION_CLASSES
        ):
            return (
                f"N5 statement {index}.resolution_classes_checked must equal "
                f"{sorted(N5_RESOLUTION_CLASSES)}"
            )
        if len(statement["tested_resolutions"]) != len(N5_RESOLUTION_CLASSES):
            return f"N5 statement {index} must record one tested resolution per required class"
        for resolution_class in N5_RESOLUTION_CLASSES:
            if not any(
                _norm(resolution).startswith(_norm(resolution_class))
                and len(_norm(resolution)) >= 40
                for resolution in statement["tested_resolutions"]
            ):
                return f"N5 statement {index} lacks a substantive {resolution_class} tested resolution"
        if not _list(statement.get("untested_resolutions")) or not all(_text(x) for x in statement["untested_resolutions"]):
            return f"N5 statement {index}.untested_resolutions must be a list of non-empty strings"
        error = _locator_error(statement.get("evidence_path"), statement.get("evidence_locator"), manifest, f"N5 statement {index}")
        if error:
            return error
        error = _locator_error(
            statement.get("resolution_evidence_path"),
            statement.get("resolution_evidence_locator"), manifest,
            f"N5 statement {index} resolution test",
        )
        if error:
            return error
        if manifest is not None:
            resolution_entry = manifest[statement["resolution_evidence_path"]]
            if "runner_stdout" not in set(resolution_entry.get("roles") or []):
                return f"N5 statement {index} resolution tests must cite current-cycle execution evidence"
            resolution_text = str(resolution_entry.get("text") or "")
            verified_resolutions = {
                str(candidate)
                for candidate in resolution_entry.get("verified_values") or []
                if _text(candidate)
            }
            for resolution in statement["tested_resolutions"]:
                if (
                    resolution not in resolution_text
                    and resolution not in verified_resolutions
                ):
                    return f"N5 statement {index} tested resolution is not evidenced at resolution_evidence_path"
        if not isinstance(statement.get("occurrence_count"), int) or statement["occurrence_count"] <= 0:
            return f"N5 statement {index}.occurrence_count must be a positive integer"
        if not isinstance(statement.get("occurrence_locator_sha256"), str) or not re.fullmatch(
            r"[0-9a-f]{64}", statement["occurrence_locator_sha256"]
        ):
            return f"N5 statement {index}.occurrence_locator_sha256 must be a SHA-256 digest"
        if not isinstance(statement.get("occurrence_group_id"), str) or not re.fullmatch(
            r"[0-9a-f]{16}", statement["occurrence_group_id"]
        ):
            return f"N5 statement {index}.occurrence_group_id must be a 16-hex context digest"
        statement_key = (
            str(statement["evidence_path"]), _norm(statement["phrase"]),
            statement["occurrence_group_id"],
        )
        if statement_key in observed_statements:
            return f"N5 statement {index} duplicates a path/phrase disposition"
        observed_statements[statement_key] = {
            "occurrence_group_id": statement["occurrence_group_id"],
            "occurrence_count": statement["occurrence_count"],
            "occurrence_locator_sha256": statement["occurrence_locator_sha256"],
            "evidence_locator": statement["evidence_locator"],
        }
        if manifest is not None and not _entry_contains(
            manifest[statement["evidence_path"]], statement["phrase"]
        ):
            return f"N5 statement {index}.phrase is not evidenced at evidence_path"
        if status == "PASS" and statement["untested_resolutions"]:
            return f"No-Go Discipline PASS cannot retain untested N5 resolutions for statement {index}"
    if manifest is not None:
        required_statements = required_phrase_groups(
            manifest, {"source"}, N5_SCAN_PHRASES
        )
        if set(observed_statements) != set(required_statements):
            missing = sorted(set(required_statements) - set(observed_statements))
            extra = sorted(set(observed_statements) - set(required_statements))
            return f"N5.statements must exactly disposition orchestrator rhetoric scan; missing={missing}, extra={extra}"
        for statement_key, observed in observed_statements.items():
            if observed != required_statements[statement_key]:
                return f"N5 statement {statement_key} must match its authenticated occurrence group"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N5 scan")
    return error or _unresolved_error(section, "N5", status)


def _validate_n6(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N6_partial_closure_scan")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {"scan_scope", "premise_classes_checked", "candidates", "none_found_reason", "unresolved", "evidence_path", "evidence_locator"},
        "N6",
    )
    if error:
        return error
    error = _locator_error(
        section.get("evidence_path"),
        section.get("evidence_locator"),
        manifest,
        "N6 scan",
    )
    if error:
        return error
    indexed_candidates: dict[str, dict[str, Any]] | None = None
    if manifest is not None:
        index_entry = manifest.get(section.get("evidence_path"))
        if not index_entry or "partial_closure_index" not in set(index_entry.get("roles") or []):
            return "N6 must cite the orchestrator-owned partial_closure_index surface"
        indexed_candidates = _partial_closure_candidates(index_entry)
        if indexed_candidates is None:
            return "N6 partial-closure index is malformed or not orchestrator-authenticated"
    if not _text(section.get("scan_scope")):
        return "N6.scan_scope must name the primitive/reframe surfaces checked"
    checked = section.get("premise_classes_checked")
    if (
        not _list(checked)
        or not all(_text(item) for item in checked)
    ):
        return f"N6.premise_classes_checked must equal {sorted(PREMISE_CLASSES_CHECKED)}"
    checked_set = set(checked)
    if checked_set not in (PREMISE_CLASSES_CHECKED, LEGACY_PREMISE_CLASSES_CHECKED):
        return f"N6.premise_classes_checked must equal {sorted(PREMISE_CLASSES_CHECKED)}"
    candidates = section.get("candidates")
    if not _list(candidates):
        return "N6.candidates must be a list"
    error = _none_found_error(section, candidates, "N6")
    if error:
        return error
    allowed_kinds = {"approved_primitive", "open_gate", "convention_reframe", "definition_refactor"}
    if checked_set == LEGACY_PREMISE_CLASSES_CHECKED:
        allowed_kinds.add("owner_governed")
    seen_candidate_ids: set[str] = set()
    for index, candidate in enumerate(candidates, 1):
        if (
            not isinstance(candidate, dict)
            or not isinstance(candidate.get("kind"), str)
            or candidate.get("kind") not in allowed_kinds
        ):
            return f"N6 candidate {index}.kind is invalid"
        error = _unknown_fields(
            candidate,
            {
                "candidate_id", "kind", "indexed_basis", "affected_wall", "closure_mechanism",
                "could_close_wall", "addressed", "disposition",
                "evidence_path", "evidence_locator",
            },
            f"N6 candidate {index}",
        )
        if error:
            return error
        if not _text(candidate.get("candidate_id")):
            return f"N6 candidate {index}.candidate_id must be non-empty"
        candidate_id = str(candidate["candidate_id"])
        if candidate_id in seen_candidate_ids:
            return f"N6 candidate {index}.candidate_id is duplicated"
        indexed = indexed_candidates.get(candidate_id) if indexed_candidates is not None else None
        if indexed_candidates is not None and indexed is None:
            return f"N6 candidate {index}.candidate_id is absent from the partial-closure index"
        if indexed and indexed.get("kind") and candidate.get("kind") != indexed.get("kind"):
            return f"N6 candidate {index}.kind does not match the partial-closure index"
        if not _text(candidate.get("indexed_basis")) or len(_norm(candidate["indexed_basis"])) < 20:
            return f"N6 candidate {index}.indexed_basis must quote substantive indexed content"
        indexed_basis = indexed.get("basis") if indexed is not None else None
        indexed_basis_surface = (
            indexed_basis
            if _text(indexed_basis)
            else json.dumps(indexed, sort_keys=True)
        )
        if indexed is not None and _norm(candidate["indexed_basis"]) not in _norm(
            indexed_basis_surface
        ):
            return f"N6 candidate {index}.indexed_basis is not present in its indexed candidate"
        for field in ("could_close_wall", "addressed"):
            if not isinstance(candidate.get(field), bool):
                return f"N6 candidate {index}.{field} must be boolean"
        if not _text(candidate.get("disposition")):
            return f"N6 candidate {index}.disposition must be non-empty"
        if not _text(candidate.get("affected_wall")):
            return f"N6 candidate {index}.affected_wall must name an N2 wall"
        walls = {
            _norm(wall)
            for wall in packet.get("N2_wall_independence", {}).get("walls") or []
        }
        if _norm(candidate["affected_wall"]) not in walls:
            return f"N6 candidate {index}.affected_wall does not name an N2 wall"
        if (
            not _text(candidate.get("closure_mechanism"))
            or len(_norm(candidate["closure_mechanism"])) < 40
        ):
            return f"N6 candidate {index}.closure_mechanism must explain the partial-closure test"
        if _norm(candidate["indexed_basis"]) not in _norm(candidate["closure_mechanism"]):
            return f"N6 candidate {index}.closure_mechanism must use its indexed_basis"
        if _norm(candidate["affected_wall"]) not in _norm(candidate["disposition"]):
            return f"N6 candidate {index}.disposition must name its affected_wall"
        error = _locator_error(candidate.get("evidence_path"), candidate.get("evidence_locator"), manifest, f"N6 candidate {index}")
        if error:
            return error
        if manifest is not None:
            entry = manifest[candidate["evidence_path"]]
            if "partial_closure_index" in set(entry.get("roles") or []):
                seen_candidate_ids.add(candidate_id)
                if status == "PASS" and candidate["could_close_wall"] and not candidate["addressed"]:
                    return f"No-Go Discipline PASS leaves N6 candidate {index} unaddressed"
                continue
            expected_type = {
                "approved_primitive": "axiom_or_approved_primitive",
                "convention_reframe": "convention_not_accepted",
            }.get(candidate["kind"])
            if expected_type and entry.get("accepted_premise_type") != expected_type:
                return (
                    f"N6 candidate {index} kind={candidate['kind']!r} does not "
                    f"match manifest premise type {entry.get('accepted_premise_type')!r}"
                )
            if candidate["kind"] == "definition_refactor" and not set(entry.get("roles") or []).intersection(
                {"source", "authority", "runner", "helper"}
            ):
                return f"N6 definition_refactor candidate {index} must cite a source or code surface"
        if status == "PASS" and candidate["could_close_wall"] and not candidate["addressed"]:
            return f"No-Go Discipline PASS leaves N6 candidate {index} unaddressed"
        seen_candidate_ids.add(candidate_id)
    if indexed_candidates is not None and seen_candidate_ids != set(indexed_candidates):
        missing = sorted(set(indexed_candidates) - seen_candidate_ids)
        return f"N6.candidates must disposition every partial-closure candidate; missing {missing[:3]}"
    return _unresolved_error(section, "N6", status)


def _validate_n7(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N7_steelman")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {
            "route_id", "argument", "resolution", "resolved", "evidence_path",
            "evidence_locator", "resolution_evidence_path",
            "resolution_evidence_locator",
        },
        "N7",
    )
    if error:
        return error
    if not _text(section.get("route_id")) or not _text(section.get("argument")) or not _text(section.get("resolution")):
        return "N7.route_id, N7.argument, and N7.resolution must be non-empty"
    if not isinstance(section.get("resolved"), bool):
        return "N7.resolved must be boolean"
    if len(_norm(section["argument"])) < 80 or len(_norm(section["resolution"])) < 80:
        return "N7.argument and N7.resolution must each contain at least 80 normalized characters"
    error = _locator_error(section.get("evidence_path"), section.get("evidence_locator"), manifest, "N7")
    if error:
        return error
    error = _locator_error(
        section.get("resolution_evidence_path"),
        section.get("resolution_evidence_locator"), manifest,
        "N7 independent resolution",
    )
    if error:
        return error
    routes = {
        _norm(str(route.get("route_id") or "")): route
        for route in packet.get("N1_alternative_routes") or []
    }
    steelman_route = routes.get(_norm(section["route_id"]))
    if not steelman_route:
        return "N7.route_id must name an evidenced N1 route"
    if section.get("evidence_path") != steelman_route.get("evidence_path"):
        return "N7 must cite the same evidence_path as its steelmanned N1 route"
    if section.get("resolution_evidence_path") == section.get("evidence_path"):
        return "N7 independent resolution must cite a different packet surface from its N1 route"
    if manifest is not None:
        argument_entry = manifest.get(section["evidence_path"])
        if argument_entry is None or not _entry_contains(
            argument_entry, section["argument"]
        ):
            return "N7.argument is not evidenced at its N1 execution path"
        resolution_entry = manifest.get(section["resolution_evidence_path"])
        if resolution_entry is None:
            return "N7 independent resolution evidence is absent"
        resolution_roles = set(resolution_entry.get("roles") or [])
        accepted_authority = (
            resolution_roles.intersection(
                {"authority", "framework_premise", "premise_registry"}
            )
            and (
                resolution_entry.get("effective_status") in RETAINED_GRADE
                or resolution_entry.get("accepted_premise_type")
                in PRIOR_AUTHORITY_PREMISE_TYPES
            )
            and isinstance(resolution_entry.get("full_content_sha256"), str)
        )
        # The authenticated independent-execution role only grants authority
        # when it is not contradicted by a failed or suppressed sibling role on
        # the same surface. If a producer attaches both (for example a duplicate
        # helper declaration whose second invocation fails after the first
        # exits zero), the entry text can be a markerless failure/suppressed
        # tail; require the roles to be mutually exclusive so incomplete or
        # failed execution output cannot authenticate an N7 resolution.
        independent_execution = (
            "runner_stdout_independent" in resolution_roles
            and not resolution_roles.intersection(
                {
                    "runner_stdout_independent_failed",
                    "runner_stdout_independent_suppressed",
                }
            )
        )
        if not (accepted_authority or independent_execution):
            return (
                "N7 independent resolution must cite authenticated independent "
                "execution or retained/accepted authority"
            )
        if not _entry_contains(resolution_entry, section["resolution"]):
            return "N7.resolution is not evidenced at resolution_evidence_path"
    if _norm(str(steelman_route.get("mechanism") or "")) not in _norm(section["argument"]):
        return "N7.argument must name the steelmanned route mechanism"
    if _norm(str(steelman_route.get("attempt") or "")) not in _norm(section["argument"]):
        return "N7.argument must name the steelmanned route attempt"
    walls = packet.get("N2_wall_independence", {}).get("walls") or []
    if not any(_norm(wall) in _norm(section["resolution"]) for wall in walls):
        return "N7.resolution must name at least one evidenced N2 wall"
    if status == "PASS" and str(steelman_route.get("disposition") or "").upper() != "CLOSED":
        return "No-Go Discipline PASS requires the N7 steelman route to be CLOSED"
    if status == "PASS" and not section["resolved"]:
        return "No-Go Discipline PASS requires the N7 steelman to be resolved"
    return None


def _validate_n8(packet: dict, status: str, manifest: dict[str, dict] | None) -> str | None:
    section, error = _section(packet, "N8_cross_cycle_echo")
    if error:
        return error
    assert section is not None
    error = _unknown_fields(
        section,
        {
            "packet_complete", "echoes", "none_found_reason", "unresolved",
            "evidence_path", "evidence_locator", "no_go_row_universe_count",
            "no_go_row_universe_sha256",
        },
        "N8",
    )
    if error:
        return error
    error = _locator_error(
        section.get("evidence_path"),
        section.get("evidence_locator"),
        manifest,
        "N8 search",
    )
    if error:
        return error
    candidate_ids: set[str] | None = None
    candidate_records: dict[str, dict[str, Any]] | None = None
    if manifest is not None:
        entry = manifest.get(section.get("evidence_path"))
        if not entry:
            return "N8 evidence path is outside the restricted packet"
        if "cross_cycle_index" not in set(entry.get("roles") or []):
            return "N8 must cite the orchestrator-owned cross_cycle_index surface"
        candidate_records = _index_candidates(
            entry, schema="no_go_cross_cycle_index_v1",
            stored_field="cross_cycle_candidate_ids",
            stored_records_field="cross_cycle_candidates",
        )
        candidate_ids = set(candidate_records) if candidate_records is not None else None
        if candidate_records is None:
            return "N8 cross-cycle index is malformed or not orchestrator-authenticated"
        universe = _cross_cycle_no_go_universe(entry)
        if universe is None:
            return "N8 cross-cycle index lacks the complete no-go row universe digest"
        universe_count, universe_sha256 = universe
        if section.get("no_go_row_universe_count") != universe_count:
            return "N8.no_go_row_universe_count contradicts the authenticated index"
        if section.get("no_go_row_universe_sha256") != universe_sha256:
            return "N8.no_go_row_universe_sha256 contradicts the authenticated index"
    if not isinstance(section.get("packet_complete"), bool):
        return "N8.packet_complete must be boolean"
    echoes = section.get("echoes")
    if not _list(echoes):
        return "N8.echoes must be a list"
    error = _none_found_error(section, echoes, "N8")
    if error:
        return error
    seen_candidate_ids: set[str] = set()
    for index, echo in enumerate(echoes, 1):
        if not isinstance(echo, dict) or not _text(echo.get("candidate_id")) or not _text(echo.get("mechanism")):
            return f"N8 echo {index} must name candidate_id and mechanism"
        mechanism_tokens = re.findall(r"[a-z0-9_]+", _norm(echo["mechanism"]))
        if len(_norm(echo["mechanism"])) < 24 or len(mechanism_tokens) < 3:
            return f"N8 echo {index}.mechanism must identify a substantive indexed mechanism"
        error = _unknown_fields(
            echo,
            {
                "candidate_id", "mechanism", "retired", "applicable",
                "addressed", "disposition", "evidence_path", "evidence_locator",
            },
            f"N8 echo {index}",
        )
        if error:
            return error
        candidate_id = str(echo["candidate_id"])
        if candidate_id in seen_candidate_ids:
            return f"N8 echo {index}.candidate_id is duplicated"
        if candidate_ids is not None and candidate_id not in candidate_ids:
            return f"N8 echo {index}.candidate_id is absent from the cross-cycle index"
        if not isinstance(echo.get("addressed"), bool):
            return f"N8 echo {index}.addressed must be boolean"
        if not _text(echo.get("disposition")) or len(_norm(echo["disposition"])) < 40:
            return f"N8 echo {index}.disposition must explain the applicability decision"
        if _norm(echo["mechanism"]) not in _norm(echo["disposition"]):
            return f"N8 echo {index}.disposition must name its indexed mechanism"
        if candidate_records is not None:
            candidate_record = candidate_records[candidate_id]
            indexed_mechanism = candidate_record.get("mechanism")
            candidate_text = (
                indexed_mechanism
                if _text(indexed_mechanism)
                else json.dumps(candidate_record, sort_keys=True)
            )
            if _norm(echo["mechanism"]) not in _norm(candidate_text):
                return f"N8 echo {index}.mechanism is not evidenced in its indexed candidate"
            lifecycle = candidate_record.get("lifecycle_state")
            if lifecycle not in {"active", "retired", "unknown"}:
                return f"N8 indexed candidate {candidate_id!r} lacks valid lifecycle_state"
            if lifecycle == "unknown":
                if echo.get("retired") is not None:
                    return (
                        f"N8 echo {index} must preserve unknown retirement as null "
                        "until an authenticated registry/history record decides it"
                    )
            else:
                if not isinstance(candidate_record.get("retired"), bool):
                    return f"N8 indexed candidate {candidate_id!r} lacks orchestrator retired state"
                if not isinstance(echo.get("retired"), bool):
                    return f"N8 echo {index}.retired must be boolean for known lifecycle"
                if echo["retired"] != candidate_record["retired"]:
                    return f"N8 echo {index}.retired contradicts its indexed candidate"
            if status == "PASS" and not isinstance(echo.get("applicable"), bool):
                return (
                    f"No-Go Discipline PASS requires N8 echo {index}.applicable "
                    "to be decided independently of lifecycle"
                )
            if isinstance(candidate_record.get("addressed"), bool) and echo["addressed"] != candidate_record["addressed"]:
                return f"N8 echo {index}.addressed contradicts its indexed candidate"
        error = _locator_error(echo.get("evidence_path"), echo.get("evidence_locator"), manifest, f"N8 echo {index}")
        if error:
            return error
        if status == "PASS" and echo.get("applicable") is True and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves applicable N8 echo {index} unaddressed"
        if status == "PASS" and not echo["addressed"]:
            return f"No-Go Discipline PASS leaves N8 echo {index} unaddressed"
        seen_candidate_ids.add(candidate_id)
    if candidate_ids is not None and seen_candidate_ids != candidate_ids:
        missing = sorted(candidate_ids - seen_candidate_ids)
        return f"N8.echoes must disposition every cross-cycle candidate; missing {missing[:3]}"
    if status == "PASS" and not section["packet_complete"]:
        return "No-Go Discipline PASS requires packet_complete=true for N8"
    return _unresolved_error(section, "N8", status)


def validate_no_go_discipline(
    audit: dict[str, Any],
    *,
    source_required: bool = False,
    evidence_manifest: dict[str, dict] | None = None,
    prior_claim_scope: str | None = None,
    require_declaration: bool = False,
    structural_only: bool = False,
) -> str | None:
    declared = audit.get("negative_assertion_classes")
    if require_declaration:
        if not isinstance(declared, list) or not all(
            isinstance(item, str) for item in declared
        ):
            return (
                "negative_assertion_classes must be a list (possibly empty) "
                "of policy classes; the auditor declares every negative "
                "assertion class the artifact makes"
            )
        unknown = sorted(set(declared) - POLICY_NEGATIVE_CLASSES)
        if unknown:
            return (
                "negative_assertion_classes contains unknown classes "
                f"{unknown}; allowed: {sorted(POLICY_NEGATIVE_CLASSES)}"
            )
    declared_requires = bool(declared) if isinstance(declared, list) else False
    required = (
        source_required
        or output_requires_no_go_discipline(audit)
        or declared_requires
    ) and packet_requirement_binds(audit, source_required=source_required)
    packet = audit.get("no_go_discipline")
    if not required:
        if packet is None:
            return None
        if not isinstance(packet, dict):
            return "no_go_discipline must be an object or null"
    elif not isinstance(packet, dict):
        return "No-Go Discipline N1-N8 packet is required for this audit"
    if packet is None:
        return None
    if structural_only:
        evidence_manifest = None
    elif evidence_manifest is None:
        evidence_manifest = evidence_manifest_from_snapshot(packet)
    error = _unknown_fields(
        packet,
        {
            "required", "status", "N1_alternative_routes", "N2_wall_independence",
            "N3_hidden_wall_scan", "N4_residual_matching", "N5_rhetoric_audit",
            "N6_partial_closure_scan", "N7_steelman", "N8_cross_cycle_echo",
            "failures", "demotion", "prior_claim_scope", "narrowed_claim_scope",
            "corrected_wall_set", "next_route", "evidence_snapshot",
        },
        "no_go_discipline",
    )
    if error:
        return error
    if packet.get("required") is not True:
        return "no_go_discipline.required must be true"
    status = packet.get("status")
    if not isinstance(status, str):
        return "no_go_discipline.status must be PASS or FAIL"
    if status not in {"PASS", "FAIL"}:
        return "no_go_discipline.status must be PASS or FAIL"
    if audit.get("verdict") == "audited_clean" and status != "PASS":
        return "audited_clean is forbidden when No-Go Discipline status is not PASS"

    for validator in (_validate_n1, _validate_n2, _validate_n3, _validate_n4, _validate_n5, _validate_n6, _validate_n7, _validate_n8):
        error = validator(packet, status, evidence_manifest)
        if error:
            return error

    failures = packet.get("failures")
    if not _list(failures) or not all(_text(item) for item in failures):
        return "no_go_discipline.failures must be a list of non-empty strings"
    if status == "PASS":
        if failures:
            return "No-Go Discipline PASS cannot carry failure items"
        if audit.get("verdict") == "audited_clean" and audit.get("chain_closes") is not True:
            return "audited_clean with No-Go Discipline PASS requires chain_closes=true"
        if audit.get("verdict") != "audited_clean" and audit.get("chain_closes") is True:
            return "non-clean verdict cannot carry chain_closes=true"
    else:
        if not failures:
            return "No-Go Discipline FAIL requires at least one failure item"
        if not all(re.match(r"^N[1-8]\s*:", failure.strip()) for failure in failures):
            return "No-Go Discipline FAIL failures must identify the failing N1-N8 checks"
        if audit.get("verdict") not in NON_CLEAN_VERDICTS:
            return "No-Go Discipline FAIL requires a conservative non-clean verdict"
        if audit.get("chain_closes") is not False:
            return "No-Go Discipline FAIL requires chain_closes=false"
        if packet.get("demotion") not in DEMOTIONS:
            return f"No-Go Discipline FAIL demotion must be one of {sorted(DEMOTIONS)}"
        if not _text(packet.get("narrowed_claim_scope")):
            return "No-Go Discipline FAIL requires narrowed_claim_scope"
        if packet["narrowed_claim_scope"] != str(audit.get("claim_scope") or ""):
            return "No-Go Discipline FAIL narrowed_claim_scope must equal the applied claim_scope"
        if not _text(packet.get("prior_claim_scope")):
            return "No-Go Discipline FAIL requires prior_claim_scope"
        blind_reaudit = manifest_has_blind_reaudit_control(evidence_manifest)
        if blind_reaudit:
            if packet["prior_claim_scope"] != BLIND_REAUDIT_PRIOR_SCOPE:
                return (
                    "blind re-audit prior_claim_scope must use the authenticated "
                    "WITHHELD_FOR_FRESH_CONTEXT marker"
                )
            narrowed_tokens = _scope_tokens(packet["narrowed_claim_scope"])
            prior_tokens = _scope_tokens(prior_claim_scope or "")
            legacy_backfill = bool(
                prior_claim_scope
                and prior_claim_scope.casefold().startswith(
                    LEGACY_BACKFILL_SCOPE_PREFIX.casefold()
                )
            )
            if prior_tokens and not legacy_backfill:
                if not narrowed_tokens or not narrowed_tokens < prior_tokens:
                    return (
                        "blind No-Go Discipline FAIL narrowed_claim_scope must "
                        "privately narrow the pre-audit ledger scope"
                    )
                if (
                    prior_tokens.intersection(LOGICAL_SCOPE_TOKENS)
                    != narrowed_tokens.intersection(LOGICAL_SCOPE_TOKENS)
                ):
                    return (
                        "blind No-Go Discipline FAIL narrowing must preserve "
                        "the hidden scope's logical polarity"
                    )
            elif legacy_backfill or not prior_tokens:
                source_text = " ".join(
                    str(entry.get("text") or "")
                    for entry in (evidence_manifest or {}).values()
                    if "source" in set(entry.get("roles") or [])
                )
                source_tokens = _scope_tokens(source_text)
                if not narrowed_tokens or not narrowed_tokens <= source_tokens:
                    return (
                        "blind No-Go Discipline FAIL without a usable prior scope "
                        "must be lexically grounded in current source evidence"
                    )
        else:
            if prior_claim_scope is None:
                return "No-Go Discipline FAIL requires an authentic pre-audit ledger scope"
            if packet["prior_claim_scope"] != prior_claim_scope:
                return "No-Go Discipline FAIL prior_claim_scope must equal the pre-audit ledger scope"
            if _norm(packet["prior_claim_scope"]) == _norm(packet["narrowed_claim_scope"]):
                return "No-Go Discipline FAIL must actually narrow the pre-audit claim scope"
            prior_tokens = _scope_tokens(packet["prior_claim_scope"])
            narrowed_tokens = _scope_tokens(packet["narrowed_claim_scope"])
            if not narrowed_tokens or not narrowed_tokens < prior_tokens:
                return (
                    "No-Go Discipline FAIL narrowed_claim_scope must be a strict lexical "
                    "subset of prior_claim_scope"
                )
            if (
                prior_tokens.intersection(LOGICAL_SCOPE_TOKENS)
                != narrowed_tokens.intersection(LOGICAL_SCOPE_TOKENS)
            ):
                return (
                    "No-Go Discipline FAIL narrowing must preserve logical polarity "
                    "tokens such as no/not/without/only/all"
                )
        if not _list(packet.get("corrected_wall_set")) or not all(_text(x) for x in packet["corrected_wall_set"]):
            return "No-Go Discipline FAIL corrected_wall_set must be a list of non-empty strings"
        collapsed = packet.get("N2_wall_independence", {}).get("collapsed_wall_set") or []
        if {_norm(x) for x in packet["corrected_wall_set"]} != {_norm(x) for x in collapsed}:
            return "No-Go Discipline FAIL corrected_wall_set must equal N2.collapsed_wall_set"
        next_route = packet.get("next_route")
        if not isinstance(next_route, dict):
            return "No-Go Discipline FAIL next_route must be an object"
        error = _unknown_fields(next_route, {"route_id", "reason_untested"}, "next_route")
        if error:
            return error
        if not _text(next_route.get("route_id")) or not _text(next_route.get("reason_untested")):
            return "No-Go Discipline FAIL next_route requires route_id and reason_untested"
        routes = {
            _norm(str(route.get("route_id") or "")): route
            for route in packet.get("N1_alternative_routes") or []
        }
        queued = routes.get(_norm(next_route["route_id"]))
        if not queued or str(queued.get("disposition") or "").upper() not in {"OPEN", "UNTESTED"}:
            return "No-Go Discipline FAIL next_route must identify an OPEN or UNTESTED N1 route"

    return None
