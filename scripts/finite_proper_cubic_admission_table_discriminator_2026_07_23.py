#!/usr/bin/env python3
"""Finite proper-cubic admission-table discriminator.

Five explicitly supplied shell tables and one explicitly supplied port grammar
define the complete finite domain of this runner.  The runner constructs a
discriminating observable plus a blinded held-corpus protocol which, given only
well-typed port-readout streams, identifies which supplied table generated a
stream or refuses with a witness (off-family, covariance violation,
non-determinism, malformed grammar, or insufficient coverage).

The theorem is about this declared table family and grammar only.  It does not
claim that the framework selects one of these tables, that the family exhausts
admissible physical laws, or that any stream is physically formed.

Firewalls (interpretation guards; also written to the receipt):
- The five candidate tables and port grammar are supplied finite inputs. Their
  relationship to the framework's fixed Admissibility rule remains open.
- occurrence / MEMBER / LAW_RECEIPT are field names in the supplied grammar;
  no objective actuality or framework-Record identification is claimed.
- Acceptance profiles are Boolean; no frequency, weight, grade, or Born
  probability is computed or interpreted.
- The reference emitters are synthetic stream generators for harness self-test
  only; they are NOT formation routes, and the emitter's winner convention is
  supplied bookkeeping the decoder never reads beyond grammar well-formedness.
- Refusal verdicts about imposter streams are statements about those synthetic
  streams, not about any physical channel; no gravity content.

A future physical route may call ``discriminate`` only after an independent
theorem proves that its output matches the supplied grammar.  No such bridge is
claimed here, so the synthetic refusal rows have no physical-route semantics.

Preregistered falsifiers (each maps to named check rows):
- P-F1 (rows 5, 6): any blinded in-family stream misidentified -> the
  discriminator is unsound; harness FAILS; do not ship a positive.
- P-F2 (row 11): the mimic survives the held corpus without retraction -> the
  held protocol carries no content; FAIL.
- P-F3 (rows 2, 3): the independently recomputed family census / separator
  catalog disagrees with the frozen supplied fixture -> the implementation
  does not match its declared finite input; FAIL.

Pure Python stdlib only (no numpy). Python 3.11+.
"""

import hashlib
import inspect
import json
import sys
import time
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path

# ---- header constants (frozen)
FROZEN_CONTRACT_SHA256 = "23415f9ce9d54c7b78a5bceeffc7fe6396347bda62f45566399e8a88146b3743"
DATE = "2026-07-23"
AUTHORITY = "none"
AUDIT = "unset"

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "outputs" / (
    "finite_proper_cubic_admission_table_discriminator_receipt_2026_07_23.json"
)
WORKER_GRID_PATH = ROOT / "outputs" / (
    "finite_proper_cubic_admission_table_discriminator_"
    "independent_grid_2026_07_23.json"
)
BLIND_SEED = "finite-proper-cubic-admission-table-discriminator-blind-2026-07-23"

# ---- candidate family (frozen)
RULES = {
    "unique_quorum": frozenset((1,)),
    "odd_shells": frozenset((1, 3, 5)),
    "nonempty": frozenset((1, 2, 3, 4, 5, 6)),
    "low_density": frozenset((1, 2)),
    "even_nonzero": frozenset((2, 4, 6)),
}
LAW_ORDER = ("unique_quorum", "odd_shells", "nonempty", "low_density", "even_nonzero")
TRAIN_MAX_WEIGHT = 3  # train: sum(w) <= 3 ; held: sum(w) >= 4


def accepts(rule_shells, word):
    """Extensional admission test: shell membership of the word weight."""
    return int(sum(word) in rule_shells)


# Digest of the explicitly supplied five-table family.
candidate_relation_digest = hashlib.sha256(
    json.dumps(
        {name: sorted(rule) for name, rule in RULES.items()},
        sort_keys=True,
    ).encode()
).hexdigest()

# The 64 six-neighbor words; slot d carries the bit for DIRECTIONS[d].
WORDS = tuple(tuple((index >> slot) & 1 for slot in range(6)) for index in range(64))
TRAIN_WORDS = tuple(w for w in WORDS if sum(w) <= TRAIN_MAX_WEIGHT)  # 42 words
HELD_WORDS = tuple(w for w in WORDS if sum(w) >= 4)  # 22 words

# ---- generator-kind roster (fixed labels; stream_roster in the contract)
GENERATOR_KINDS = tuple(
    [f"in_family_full:{law}" for law in LAW_ORDER]
    + [f"in_family_train:{law}" for law in LAW_ORDER]
    + [f"in_family_ext:{law}" for law in LAW_ORDER]
    + ["starved_uq", "starved_even", "mimic_train", "mimic_full",
       "antipodal", "axis", "noisy"]
)

# ---- pass/fail harness
PASS = 0
FAIL = 0


def check(label, condition, detail):
    """Record one assertion; prints 'PASS <label> :: <detail>' or the FAIL form."""
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")
    return bool(condition)


# ---- finite proper-cubic geometry
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def determinant(matrix):
    """Exact-integer 3x3 determinant by cofactor expansion."""
    (a, b, c), (d, e, f), (g, h, i) = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def proper_cubic_frames():
    """All signed permutation matrices with det +1 -> the 24 proper cubic frames."""
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                frames.append(matrix)
    return frames


def matvec(matrix, vector):
    """Matrix times column vector, exact ints."""
    return tuple(sum(matrix[r][c] * vector[c] for c in range(3)) for r in range(3))


def rotate_six(word, frame):
    """Permute a six-neighbor word by a cubic frame acting on DIRECTIONS."""
    output = [0] * 6
    for direction, bit in enumerate(word):
        output[DIRECTIONS.index(matvec(frame, DIRECTIONS[direction]))] = bit
    return tuple(output)


# ---- orbit machinery (derived)
def orbits(words, frames):
    """Partition words into orbits under rotate_six."""
    seen = set()
    result = []
    for word in words:
        if word in seen:
            continue
        orbit = frozenset(rotate_six(word, frame) for frame in frames)
        seen |= orbit
        result.append(orbit)
    return result


def orbit_census(words, frames):
    """Sorted (shell, size, lex-min representative) triples over the orbits."""
    census = []
    for orbit in orbits(words, frames):
        representative = min(orbit)
        census.append((sum(representative), len(orbit), representative))
    return sorted(census)


# ---- port readout tuple (supplied finite lane-zero grammar)
@dataclass(frozen=True)
class PortTuple:
    archive: tuple      # 6 bits - copied six-candidate word
    losers: tuple       # 6 bits - copied loser mask
    ready: int          # 1 bit
    spent: int          # 1 bit
    edge: int           # 1 bit
    member: tuple       # 5 bits - lane-zero one-hot MEMBER
    receipt: tuple      # 5 bits - lane-zero LAW_RECEIPT
    snapshot: tuple     # 12 bits - supplied lane-zero output tuple
    #                     snapshot[0]=PRECOMMIT, [1]=OCCURRENCE, [2]=ATOM_FLAG,
    #                     [3:]=label-zero content (zero)


def _bits_ok(values, arity):
    return len(values) == arity and all(bit in (0, 1) for bit in values)


def port_well_formed(port):
    """Return (bool, reason). Clauses checked in order; first failure names it."""
    # W-bits: every field has the stated arity and bits in {0,1}
    if not (
        _bits_ok(port.archive, 6)
        and _bits_ok(port.losers, 6)
        and port.ready in (0, 1)
        and port.spent in (0, 1)
        and port.edge in (0, 1)
        and _bits_ok(port.member, 5)
        and _bits_ok(port.receipt, 5)
        and _bits_ok(port.snapshot, 12)
    ):
        return (False, "W-bits")
    # W-occ: occ := snapshot[1]
    occ = port.snapshot[1]
    # W-snapshot-consistency: PRECOMMIT == OCCURRENCE == ATOM_FLAG and tail zero
    if not (
        port.snapshot[0] == port.snapshot[1] == port.snapshot[2]
        and port.snapshot[3:] == (0,) * 9
    ):
        return (False, "W-snapshot-consistency")
    # W-member: one-hot MEMBER carries occ in slot 0
    if port.member != (occ, 0, 0, 0, 0):
        return (False, "W-member")
    # W-receipt: LAW_RECEIPT equals MEMBER
    if port.receipt != port.member:
        return (False, "W-receipt")
    # W-edge: edge follows occ
    if port.edge != occ:
        return (False, "W-edge")
    # W-resource: ready/spent rails are the occ complement/copy
    if not (port.ready == 1 - occ and port.spent == occ):
        return (False, "W-resource")
    # W-losers0: with no occurrence the loser mask equals the archive
    if occ == 0 and port.losers != port.archive:
        return (False, "W-losers0")
    # W-losers1: with an occurrence the winner is a single archived bit cleared
    if occ == 1:
        winner = tuple(a ^ l for a, l in zip(port.archive, port.losers))
        if sum(winner) != 1:
            return (False, "W-losers1")
        set_bit = winner.index(1)
        if port.archive[set_bit] != 1:
            return (False, "W-losers1")
        cleared = tuple(0 if slot == set_bit else port.archive[slot] for slot in range(6))
        if port.losers != cleared:
            return (False, "W-losers1")
    return (True, "ok")


def emit(accept_bit, word):
    """SUPPLIED synthetic bookkeeping for self-test streams - NOT a formation route.

    occ = accept_bit. On occ == 1 the winner is the LOWEST-INDEX set bit of word
    (supplied convention, not law content); loser mask / rails / lane-zero fields
    follow the grammar equations. Raises on occ == 1 with an empty word (the port
    grammar cannot express a memberless admission).
    """
    occ = int(accept_bit)
    archive = tuple(word)
    if occ == 1:
        if sum(word) == 0:
            raise ValueError("emit: occ=1 requires a candidate (sum(word) > 0)")
        winner_bit = word.index(1)
        losers = tuple(0 if slot == winner_bit else word[slot] for slot in range(6))
    else:
        losers = archive
    member = (occ, 0, 0, 0, 0)
    return PortTuple(
        archive=archive,
        losers=losers,
        ready=1 - occ,
        spent=occ,
        edge=occ,
        member=member,
        receipt=member,
        snapshot=(occ, occ, occ, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    )


def supplied_port_expected(word):
    """Expected supplied grammar tuple at the unique-quorum anchor."""
    admit = int(sum(word) == 1)
    direction = word.index(1) if admit else None
    losers = tuple(bit ^ int(direction == index) for index, bit in enumerate(word))
    return {
        "admit": admit,
        "archive": word,
        "losers": losers,
        "ready": 1 - admit,
        "spent": admit,
        "member": (admit, 0, 0, 0, 0),
        "receipt": (admit, 0, 0, 0, 0),
        "snapshot": (admit, admit, admit, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    }
    # edge follows P_ADMIT through the extension schedule: edge == admit.


# ---- the discriminating observable (the decoder)
def discriminate(stream, tables, frames):
    """Identify which candidate admission law a port-readout stream implements,
    or refuse with a witness. Pure function of (stream, tables, frames).

    tables maps law name -> frozenset of accepted shells (the PUBLIC family;
    publishing the family is not a disclosure violation - WHICH law drove a stream
    is what is withheld). frames is the 24 proper cubic matrices. Tiers, in order:
    (1) grammar, (2) determinism, (3) covariance, (4) family match. Verdicts are
    canonical: the lexicographically smallest witness word (or pair) is chosen.
    """
    accept = lambda shells, word: int(sum(word) in shells)

    # tier 1: grammar - every tuple well-formed
    for index, port in enumerate(stream):
        ok, reason = port_well_formed(port)
        if not ok:
            return {"kind": "refuse_malformed", "index": index, "reason": reason}

    # profile P: word -> occ, from (archive, occ) pairs
    profile = {}
    contradictions = set()
    for port in stream:
        word = tuple(port.archive)
        occ = port.snapshot[1]
        if word in profile:
            if profile[word] != occ:
                contradictions.add(word)
        else:
            profile[word] = occ

    # tier 2: determinism - any word carrying both occ values
    if contradictions:
        return {"kind": "refuse_contradiction", "word": min(contradictions)}

    observed = sorted(profile)

    def canonical(word):
        return min(rotate_six(word, frame) for frame in frames)

    # tier 3: covariance - two observed same-orbit words with differing occ
    for left in range(len(observed)):
        for right in range(left + 1, len(observed)):
            w_one, w_two = observed[left], observed[right]
            if profile[w_one] != profile[w_two] and canonical(w_one) == canonical(w_two):
                return {"kind": "refuse_covariance", "witness": [w_one, w_two]}

    # tier 4: family match
    consistent = [
        name for name in sorted(tables)
        if all(profile[w] == accept(tables[name], w) for w in observed)
    ]

    def first_disagreement(name):
        for w in observed:
            if profile[w] != accept(tables[name], w):
                return w
        return None

    if len(consistent) == 1:
        law = consistent[0]
        witnesses = {
            other: first_disagreement(other)
            for other in sorted(tables) if other != law
        }
        return {"kind": "identified", "law": law, "witnesses": witnesses}

    if len(consistent) == 0:
        witnesses = {name: first_disagreement(name) for name in sorted(tables)}
        return {"kind": "off_family", "witnesses": witnesses}

    # len(consistent) >= 2: ambiguous - report minimum shell sets that would
    # complete the identification. Completing shells are the unobserved shells
    # (no observed word of that weight); a subset S completes when the consistent
    # laws are pairwise distinct restricted to S.
    present = {sum(w) for w in observed}
    unobserved = [shell for shell in range(7) if shell not in present]

    def completes(subset):
        for left_law, right_law in combinations(consistent, 2):
            if all((s in tables[left_law]) == (s in tables[right_law]) for s in subset):
                return False
        return True

    completing = []
    for size in range(len(unobserved) + 1):
        found = sorted(
            sorted(subset) for subset in combinations(unobserved, size) if completes(subset)
        )
        if found:
            completing = found
            break

    return {
        "kind": "ambiguous",
        "consistent": sorted(consistent),
        "completing_shell_sets": completing,
    }


# ---- blinding mechanics (deterministic PRNG from the frozen seed; no `random`)
def det_stream(seed, label):
    """Yield 64-bit uints from sha256(seed:label:counter)."""
    counter = 0
    while True:
        digest = hashlib.sha256(f"{seed}:{label}:{counter}".encode()).digest()
        yield int.from_bytes(digest[:8], "big")
        counter += 1


def det_shuffle(items, seed, label):
    """Fisher-Yates shuffle driven by det_stream."""
    source = det_stream(seed, label)
    array = list(items)
    for i in range(len(array) - 1, 0, -1):
        j = next(source) % (i + 1)
        array[i], array[j] = array[j], array[i]
    return array


# ---- frozen supplied fixture (finite theorem input; no inherited authority)
SUPPLIED_FIXTURE = {
    "family_census": {
        "accepted_truth_rows": {
            "unique_quorum": 6, "odd_shells": 32, "nonempty": 63,
            "low_density": 21, "even_nonzero": 31,
        },
        "train_accepts": {
            "unique_quorum": 6, "odd_shells": 26, "nonempty": 41,
            "low_density": 21, "even_nonzero": 15,
        },
        "held_accepts": {
            "unique_quorum": 0, "odd_shells": 6, "nonempty": 22,
            "low_density": 0, "even_nonzero": 16,
        },
        "candidate_relation_digest":
            "c724243216bffdd804d69106872486ee92efd71adfb23b0d1f5821778ed14b34",
        # (left, right, train, held, total), combinations order over LAW_ORDER
        "pairwise": [
            ["unique_quorum", "odd_shells", 20, 6, 26],
            ["unique_quorum", "nonempty", 35, 22, 57],
            ["unique_quorum", "low_density", 15, 0, 15],
            ["unique_quorum", "even_nonzero", 21, 16, 37],
            ["odd_shells", "nonempty", 15, 16, 31],
            ["odd_shells", "low_density", 35, 6, 41],
            ["odd_shells", "even_nonzero", 41, 22, 63],
            ["nonempty", "low_density", 20, 22, 42],
            ["nonempty", "even_nonzero", 26, 6, 32],
            ["low_density", "even_nonzero", 6, 16, 22],
        ],
    },
}


# ---- analytic helpers (census, separators, orbit-structured observables)
ANTIPODAL_PAIRS = ((0, 1), (2, 3), (4, 5))  # antipodal direction slots


def antipodal_accept(word):
    """Covariant orbit law: accept a weight-2 word iff its bits are antipodal."""
    if sum(word) != 2:
        return 0
    bits = tuple(slot for slot, bit in enumerate(word) if bit)
    return int(bits in ANTIPODAL_PAIRS)


def shell_profiles():
    """Per-law shell acceptance vector over shells 0..6."""
    return {law: [int(shell in RULES[law]) for shell in range(7)] for law in LAW_ORDER}


def truth_counts(words):
    """Per-law accepted count over the given words."""
    return {law: sum(accepts(RULES[law], w) for w in words) for law in LAW_ORDER}


def separator_counts(left, right):
    """(train, held, total) words where the two laws disagree."""
    train = held = total = 0
    for w in WORDS:
        if accepts(RULES[left], w) != accepts(RULES[right], w):
            total += 1
            if sum(w) <= TRAIN_MAX_WEIGHT:
                train += 1
            else:
                held += 1
    return train, held, total


def pairwise_separators():
    """Separator catalog in combinations order over LAW_ORDER."""
    rows = []
    for left, right in combinations(LAW_ORDER, 2):
        train, held, total = separator_counts(left, right)
        rows.append([left, right, train, held, total])
    return rows


def min_separating_shell_sets(law_names, shell_pool):
    """Minimum-size shell subsets making the named laws pairwise distinct.

    Returns (size, sorted list of sorted subsets). Computation only - not
    hardcoded; callers assert against whatever this yields.
    """
    pool = list(shell_pool)

    def separates(subset):
        for left, right in combinations(law_names, 2):
            if all((s in RULES[left]) == (s in RULES[right]) for s in subset):
                return False
        return True

    for size in range(len(pool) + 1):
        found = sorted(sorted(sub) for sub in combinations(pool, size) if separates(sub))
        if found:
            return size, found
    return None, []


def consistent_laws_for_shells(accepted_shells):
    """Laws consistent with 'accept iff shell in accepted_shells' on those shells."""
    observed = set(accepted_shells)
    return [
        law for law in LAW_ORDER
        if all((shell in RULES[law]) == (shell in observed) for shell in observed)
    ]


def mimic_odd_disagreements():
    """Train/held split of the words where the shell-{1,3} imposter differs from
    odd_shells, with the distinct Hamming weights of the held witnesses."""
    imposter = frozenset((1, 3))
    target = RULES["odd_shells"]
    train = held = 0
    held_weights = set()
    for w in WORDS:
        if accepts(imposter, w) != accepts(target, w):
            if sum(w) <= TRAIN_MAX_WEIGHT:
                train += 1
            else:
                held += 1
                held_weights.add(sum(w))
    return {"train": train, "held": held,
            "held_witness_weights": sorted(held_weights)}


def antipodal_summary(frames):
    """Structured facts about the antipodal orbit law for the worker-grid row."""
    accepted = [w for w in WORDS if antipodal_accept(w)]
    shell2 = [w for w in WORDS if sum(w) == 2]
    orbit_constant = all(
        len({antipodal_accept(member) for member in orbit}) == 1
        for orbit in orbits(WORDS, frames)
    )
    is_shell_function = all(
        len({antipodal_accept(w) for w in WORDS if sum(w) == shell}) == 1
        for shell in range(7)
    )
    return {
        "accepted_count": len(accepted),
        # W1-grid schema: [accepted within shell 2, total shell-2 words]
        "shell2_accept_reject": [
            sum(antipodal_accept(w) for w in shell2),
            len(shell2),
        ],
        "is_shell_function": is_shell_function,
        "orbit_constant": orbit_constant,
    }


def antipodal_same_shell_witness():
    """Lex-min pair of shell-2 words with differing antipodal occ (same shell,
    different orbit) - the extensional (non-covariance) off-family witness."""
    shell2 = sorted(w for w in WORDS if sum(w) == 2)
    for i in range(len(shell2)):
        for j in range(i + 1, len(shell2)):
            if antipodal_accept(shell2[i]) != antipodal_accept(shell2[j]):
                return [shell2[i], shell2[j]]
    return None


# ---- fixed catalogs (frozen; surfaced in the contract)
NOISY_REPEAT_WORD = min(w for w in WORDS if sum(w) == 1)  # lex-min shell-1 word

MALFORMED_CATALOG = {
    "m_member_without_occ": "W-member",
    "m_receipt_mismatch": "W-receipt",
    "m_snapshot_equation": "W-snapshot-consistency",
    "m_snapshot_tail": "W-snapshot-consistency",
    "m_resource_rail": "W-resource",
    "m_loser_mask": "W-losers0",
    "m_winner_not_onehot": "W-losers1",
    "m_edge": "W-edge",
}

EXPECTED_VERDICTS = {
    "starved_uq": "ambiguous",
    "starved_even": "identified:even_nonzero",
    "mimic_train": "identified:odd_shells",
    "mimic_full": "off_family",
    "antipodal": "off_family",
    "axis": "refuse_covariance",
    "noisy": "refuse_contradiction",
}

CHECK_LABELS = (
    "port_grammar_anchor",
    "family_census_fixture_crosscheck",
    "separator_catalog",
    "worker_grid_agreement",
    "blinded_full_identification",
    "train_prefix_held_no_refit",
    "coverage_starved_refusal",
    "off_family_covariant_imposter",
    "non_covariant_imposter",
    "non_deterministic_imposter",
    "held_corpus_retraction",
    "malformed_port_refusals",
    "verdict_frame_invariance",
    "decoder_blindness_discipline",
)


# ---- synthetic stream roster (self-test generators; NOT formation routes)
def build_base_streams():
    """The stream roster in FIXED construction order (unblinded tuple order).

    in_family_ext = the law's train stream (a prefix) + its 22 held words.
    """
    imposter = frozenset((1, 3))  # train-consistent / held-inconsistent shell law
    shell1 = [w for w in WORDS if sum(w) == 1]
    base = {}
    for law in LAW_ORDER:
        base[f"in_family_full:{law}"] = [emit(accepts(RULES[law], w), w) for w in WORDS]
        train = [emit(accepts(RULES[law], w), w) for w in TRAIN_WORDS]
        held = [emit(accepts(RULES[law], w), w) for w in HELD_WORDS]
        base[f"in_family_train:{law}"] = train
        base[f"in_family_ext:{law}"] = train + held
    base["starved_uq"] = [emit(accepts(RULES["unique_quorum"], w), w) for w in shell1]
    base["starved_even"] = [emit(accepts(RULES["even_nonzero"], w), w) for w in shell1]
    base["mimic_train"] = [emit(accepts(imposter, w), w) for w in TRAIN_WORDS]
    base["mimic_full"] = [emit(accepts(imposter, w), w) for w in WORDS]
    base["antipodal"] = [emit(antipodal_accept(w), w) for w in WORDS]
    base["axis"] = [emit(word[0], word) for word in WORDS]
    uq_full = [emit(accepts(RULES["unique_quorum"], w), w) for w in WORDS]
    base["noisy"] = uq_full + [emit(0, NOISY_REPEAT_WORD)]  # one contradictory repeat
    return base


def generate_blinded_streams():
    """Assign blind labels (shuffled) to the roster and shuffle each word order.

    Returns (blinded, manifest, streams_by_kind): blinded is [(label, stream)]
    sorted by label; manifest maps label -> ground-truth generator kind; the
    manifest is consulted only by the unblind section of main().
    """
    base = build_base_streams()
    kinds = list(GENERATOR_KINDS)  # fixed construction order
    labels = [f"stream_{i:02d}" for i in range(len(kinds))]
    order = det_shuffle(list(range(len(kinds))), BLIND_SEED, "assignment")
    manifest = {}
    streams_by_kind = {}
    for position, label in enumerate(labels):
        kind = kinds[order[position]]
        tuples = det_shuffle(base[kind], BLIND_SEED, label)
        manifest[label] = kind
        streams_by_kind[kind] = tuples
    blinded = sorted(((label, streams_by_kind[manifest[label]]) for label in labels),
                     key=lambda pair: pair[0])
    return blinded, manifest, streams_by_kind


def build_malformed_streams():
    """Eight single-tuple streams, each breaking exactly one grammar clause.

    Each is a well-formed tuple with one field broken by direct PortTuple
    construction (bypassing the emitter's validation).
    """
    return {
        # occ=0 but MEMBER carries a bit -> W-member
        "m_member_without_occ": [PortTuple(
            (0,) * 6, (0,) * 6, 1, 0, 0, (1, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0,) * 12)],
        # occ=1 with LAW_RECEIPT zeroed -> W-receipt
        "m_receipt_mismatch": [PortTuple(
            (1, 0, 0, 0, 0, 0), (0,) * 6, 0, 1, 1, (1, 0, 0, 0, 0), (0, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))],
        # PRECOMMIT/OCCURRENCE/ATOM_FLAG differ -> W-snapshot-consistency
        "m_snapshot_equation": [PortTuple(
            (0,) * 6, (0,) * 6, 1, 0, 0, (0, 0, 0, 0, 0), (0, 0, 0, 0, 0),
            (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))],
        # nonzero label-zero tail -> W-snapshot-consistency
        "m_snapshot_tail": [PortTuple(
            (1, 0, 0, 0, 0, 0), (0,) * 6, 0, 1, 1, (1, 0, 0, 0, 0), (1, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0))],
        # occ=1 but ready/spent rails not flipped -> W-resource
        "m_resource_rail": [PortTuple(
            (1, 0, 0, 0, 0, 0), (0,) * 6, 1, 0, 1, (1, 0, 0, 0, 0), (1, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))],
        # occ=0 but loser mask != archive -> W-losers0
        "m_loser_mask": [PortTuple(
            (1, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), 1, 0, 0, (0, 0, 0, 0, 0),
            (0, 0, 0, 0, 0), (0,) * 12)],
        # occ=1, weight-3 archive, loser mask clears two bits -> W-losers1
        "m_winner_not_onehot": [PortTuple(
            (1, 1, 1, 0, 0, 0), (0, 0, 1, 0, 0, 0), 0, 1, 1, (1, 0, 0, 0, 0),
            (1, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))],
        # occ=1 but edge low -> W-edge
        "m_edge": [PortTuple(
            (1, 0, 0, 0, 0, 0), (0,) * 6, 0, 1, 0, (1, 0, 0, 0, 0), (1, 0, 0, 0, 0),
            (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0))],
    }


# ---- frozen contract
def contract():
    """The frozen contract: only JSON-native types (no timestamps, no env)."""
    return {
        "date": DATE,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "family": {name: sorted(RULES[name]) for name in LAW_ORDER},
        "law_order": list(LAW_ORDER),
        "train_max_weight": TRAIN_MAX_WEIGHT,
        "blind_seed": BLIND_SEED,
        "port_grammar": {
            "version": "finite lane-zero readout, winner-generalized, v1",
            "clauses": ["W-bits", "W-snapshot-consistency", "W-member", "W-receipt",
                        "W-edge", "W-resource", "W-losers0", "W-losers1"],
            "emitter_winner_convention":
                "lowest-index set candidate bit (supplied bookkeeping, not law content)",
        },
        "stream_roster": sorted(GENERATOR_KINDS),
        "imposters": {
            "mimic_shells": [1, 3],
            "antipodal_pairs": [list(pair) for pair in ANTIPODAL_PAIRS],
            "axis_slot": 0,
            "noisy_repeat_word": list(NOISY_REPEAT_WORD),
        },
        "malformed_catalog": dict(MALFORMED_CATALOG),
        "expected_verdicts": dict(EXPECTED_VERDICTS),
        "worker_grid_file": WORKER_GRID_PATH.name,
        "supplied_fixture": SUPPLIED_FIXTURE,
        "check_labels": list(CHECK_LABELS),
    }


def contract_sha():
    return hashlib.sha256(
        json.dumps(contract(), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


# ---- small shared helpers
def verdict_tag(verdict):
    """Compact tag; matches the EXPECTED_VERDICTS vocabulary."""
    if verdict["kind"] == "identified":
        return f"identified:{verdict['law']}"
    return verdict["kind"]


def rotate_stream(stream, frame):
    """Rotate archive and losers by a frame; scalars and lane-zero fields unchanged."""
    return [
        PortTuple(
            archive=rotate_six(port.archive, frame),
            losers=rotate_six(port.losers, frame),
            ready=port.ready, spent=port.spent, edge=port.edge,
            member=port.member, receipt=port.receipt, snapshot=port.snapshot,
        )
        for port in stream
    ]


def normalize(obj):
    """Recursively turn tuples into lists so computed values compare to loaded JSON."""
    if isinstance(obj, (list, tuple)):
        return [normalize(item) for item in obj]
    if isinstance(obj, dict):
        return {key: normalize(value) for key, value in obj.items()}
    return obj


def load_worker_grid():
    if not WORKER_GRID_PATH.exists():
        return None, None
    payload = WORKER_GRID_PATH.read_bytes()
    return json.loads(payload.decode()), hashlib.sha256(payload).hexdigest()


# ---- main
def main(argv):
    # --print-contract-sha: print the digest and exit without running anything.
    if "--print-contract-sha" in argv:
        print(contract_sha())
        return 0

    start = time.time()

    # Contract self-assert is the FIRST act; drift is not a physics FAIL (exit 2).
    computed_sha = contract_sha()
    if FROZEN_CONTRACT_SHA256 != computed_sha:
        print(
            "ABORT contract drift :: frozen "
            f"{FROZEN_CONTRACT_SHA256} != computed {computed_sha}",
            file=sys.stderr,
        )
        return 2

    frames = proper_cubic_frames()
    receipt = {}

    # ---- 1. port-grammar anchor at the unique-quorum point
    anchor_fields = ("archive", "losers", "ready", "spent", "member", "receipt", "snapshot")
    anchor_ok = 0
    for word in WORDS:
        produced = emit(accepts(RULES["unique_quorum"], word), word)
        expected = supplied_port_expected(word)
        if (all(getattr(produced, name) == expected[name] for name in anchor_fields)
                and produced.edge == expected["admit"]):
            anchor_ok += 1
    check(f"01 {CHECK_LABELS[0]}", anchor_ok == 64,
          f"generalized emitter == supplied port fixture on {anchor_ok}/64 words, edge==admit")

    # ---- 2. family census + frozen supplied-fixture cross-check (P-F3)
    census = SUPPLIED_FIXTURE["family_census"]
    truth_rows = truth_counts(WORDS)
    train_rows = truth_counts(TRAIN_WORDS)
    held_rows = truth_counts(HELD_WORDS)
    check(f"02 {CHECK_LABELS[1]}/truth_rows", truth_rows == census["accepted_truth_rows"],
          f"accepted truth rows {truth_rows}")
    check(f"02 {CHECK_LABELS[1]}/train_accepts", train_rows == census["train_accepts"],
          f"train accepts {train_rows}")
    check(f"02 {CHECK_LABELS[1]}/held_accepts", held_rows == census["held_accepts"],
          f"held accepts {held_rows}")
    covariance_failures = 0
    for law in LAW_ORDER:
        for word in WORDS:
            base_bit = accepts(RULES[law], word)
            for frame in frames:
                if accepts(RULES[law], rotate_six(word, frame)) != base_bit:
                    covariance_failures += 1
    check(f"02 {CHECK_LABELS[1]}/covariance",
          len(frames) == 24 and covariance_failures == 0,
          f"{5 * 64 * 24} comparisons, {covariance_failures} covariance failures")
    nonconstant = all({accepts(RULES[law], w) for w in WORDS} == {0, 1} for law in LAW_ORDER)
    check(f"02 {CHECK_LABELS[1]}/nonconstant", nonconstant, "both outputs occur per law")
    check(f"02 {CHECK_LABELS[1]}/digest",
          candidate_relation_digest == census["candidate_relation_digest"],
          f"candidate_relation_digest {candidate_relation_digest}")

    # ---- 3. separator catalog + orbit census + minimal separating shell sets (P-F3)
    computed_pairwise = pairwise_separators()
    check(f"03 {CHECK_LABELS[2]}/pairwise", computed_pairwise == census["pairwise"],
          f"{len(computed_pairwise)} pairwise separator rows match supplied fixture")
    census_triples = orbit_census(WORDS, frames)
    orbit_total = sum(size for _, size, _ in census_triples)
    check(f"03 {CHECK_LABELS[2]}/orbits",
          len(census_triples) == 10 and orbit_total == 64,
          f"{len(census_triples)} orbits, sizes sum to {orbit_total}")
    separating_size, separating_sets = min_separating_shell_sets(LAW_ORDER, range(7))

    def family_distinct_on(subset):
        vectors = {tuple(int(s in RULES[law]) for s in subset) for law in LAW_ORDER}
        return len(vectors) == len(LAW_ORDER)

    separating_ok = (
        bool(separating_sets)
        and all(len(s) == separating_size for s in separating_sets)
        and all(family_distinct_on(s) for s in separating_sets)
    )
    check(f"03 {CHECK_LABELS[2]}/min_separating_sets", separating_ok,
          f"min size {separating_size}, {len(separating_sets)} sets, restricted profiles distinct")

    receipt["orbit_census"] = normalize(census_triples)
    receipt["shell_profiles"] = shell_profiles()
    receipt["separator_catalog"] = {
        "pairwise": computed_pairwise,
        "minimal_separating_shell_sets": {"size": separating_size, "sets": separating_sets},
    }

    # ---- 4. independent worker-grid agreement
    def consistent_for(profile_map):
        return sorted(
            law for law in LAW_ORDER
            if all(int(s in RULES[law]) == bit for s, bit in profile_map.items())
        )

    scenario_consistent_sets = {
        "starved_uq": consistent_for({1: 1}),
        "starved_even": consistent_for({1: 0}),
    }
    unobserved_after_shell1 = [s for s in range(7) if s != 1]
    _, completing_after_shell1_uq = min_separating_shell_sets(
        scenario_consistent_sets["starved_uq"], unobserved_after_shell1)

    # The independent grid's frozen schema (the W1 spec shapes): orbit census and
    # pairwise rows as dicts, scenario keys spelled out, mimic as train/held split.
    train_only_identifiable = {}
    for law in LAW_ORDER:
        consistent_with_train = [
            other for other in LAW_ORDER
            if all(accepts(RULES[other], w) == accepts(RULES[law], w)
                   for w in TRAIN_WORDS)
        ]
        train_only_identifiable[law] = consistent_with_train == [law]

    grid_expected = {
        "orbit_census": [
            {"shell": shell, "size": size, "representative": list(rep)}
            for shell, size, rep in census_triples
        ],
        "shell_profiles": shell_profiles(),
        "pairwise_separators": [
            {"left": left, "right": right, "train": train, "held": held, "total": total}
            for left, right, train, held, total in computed_pairwise
        ],
        "minimal_separating_shell_sets": normalize(separating_sets),
        "scenario_consistent_sets": {
            "shell1_stream_labeled_by_unique_quorum": scenario_consistent_sets["starved_uq"],
            "shell1_stream_labeled_by_even_nonzero": scenario_consistent_sets["starved_even"],
        },
        "completing_sets_after_shell1_uq": normalize(completing_after_shell1_uq),
        "mimic_odd_disagreements": mimic_odd_disagreements(),
        "antipodal": antipodal_summary(frames),
        "train_only_identifiable": train_only_identifiable,
    }
    grid, grid_sha = load_worker_grid()
    agreement = {}
    if grid is None:
        for field in grid_expected:
            agreement[field] = False
        check(f"04 {CHECK_LABELS[3]}", False,
              f"worker grid missing at {WORKER_GRID_PATH}")
    else:
        mismatches = []
        for field, value in grid_expected.items():
            same = normalize(grid.get(field)) == normalize(value)
            agreement[field] = same
            if not same:
                mismatches.append(field)
        check(f"04 {CHECK_LABELS[3]}", not mismatches,
              "worker grid agrees on all fields" if not mismatches
              else f"worker grid mismatches: {sorted(mismatches)}")
    receipt["worker_grid_agreement"] = {
        "fields": agreement,
        "grid_path": str(WORKER_GRID_PATH.relative_to(ROOT)),
        "grid_sha256": grid_sha,
    }

    # ---- blinded stream generation + blind decode (manifest not consulted yet)
    blinded, manifest, streams_by_kind = generate_blinded_streams()
    blinded_verdicts = {
        label: discriminate(stream, RULES, frames) for label, stream in blinded
    }
    # unblind: manifest consulted ONLY here, after all verdicts collected
    verdict_by_kind = {
        manifest[label]: blinded_verdicts[label] for label in manifest
    }

    # ---- 5. blinded full-coverage identification (P-F1)
    full_ok = 0
    for law in LAW_ORDER:
        verdict = verdict_by_kind[f"in_family_full:{law}"]
        if (verdict["kind"] == "identified" and verdict["law"] == law
                and set(verdict.get("witnesses", {})) == set(LAW_ORDER) - {law}):
            full_ok += 1
    check(f"05 {CHECK_LABELS[4]}", full_ok == 5,
          f"{full_ok}/5 in-family FULL streams identified blind with complete witnesses")

    # ---- 6. train-prefix identification + held no-refit (P-F1)
    train_ok = 0
    ext_ok = 0
    for law in LAW_ORDER:
        train_v = verdict_by_kind[f"in_family_train:{law}"]
        ext_v = verdict_by_kind[f"in_family_ext:{law}"]
        if train_v["kind"] == "identified" and train_v["law"] == law:
            train_ok += 1
        if (ext_v["kind"] == train_v["kind"] and ext_v.get("law") == train_v.get("law")
                and ext_v["kind"] == "identified" and ext_v["law"] == law):
            ext_ok += 1
    check(f"06 {CHECK_LABELS[5]}/train", train_ok == 5, f"{train_ok}/5 train streams identified")
    check(f"06 {CHECK_LABELS[5]}/held_no_refit", ext_ok == 5,
          f"{ext_ok}/5 extensions identical to train verdict (zero retractions)")

    # ---- 7. coverage-starved refusal semantics
    starved_uq_v = verdict_by_kind["starved_uq"]
    starved_uq_ok = (
        starved_uq_v["kind"] == "ambiguous"
        and starved_uq_v["consistent"] == sorted(
            ["low_density", "nonempty", "odd_shells", "unique_quorum"])
        and normalize(starved_uq_v["completing_shell_sets"])
        == normalize(completing_after_shell1_uq)
    )
    check(f"07 {CHECK_LABELS[6]}/starved_uq", starved_uq_ok,
          f"starved_uq -> {verdict_tag(starved_uq_v)}, "
          f"consistent={starved_uq_v.get('consistent')}, "
          f"completing={starved_uq_v.get('completing_shell_sets')}")
    starved_even_v = verdict_by_kind["starved_even"]
    check(f"07 {CHECK_LABELS[6]}/starved_even",
          starved_even_v["kind"] == "identified" and starved_even_v["law"] == "even_nonzero",
          f"starved_even -> {verdict_tag(starved_even_v)}")

    # ---- 8. off-family covariant imposter (antipodal FULL)
    antipodal_v = verdict_by_kind["antipodal"]

    def same_shell_pair_from_stream(stream):
        occ_of = {tuple(p.archive): p.snapshot[1] for p in stream}
        shell2 = sorted(w for w in occ_of if sum(w) == 2)
        for i in range(len(shell2)):
            for j in range(i + 1, len(shell2)):
                if occ_of[shell2[i]] != occ_of[shell2[j]]:
                    return [shell2[i], shell2[j]]
        return None

    antipodal_pair = same_shell_pair_from_stream(streams_by_kind["antipodal"])
    antipodal_ok = (
        antipodal_v["kind"] == "off_family"
        and antipodal_v["kind"] != "refuse_covariance"
        and set(antipodal_v.get("witnesses", {})) == set(LAW_ORDER)
        and antipodal_pair is not None
    )
    check(f"08 {CHECK_LABELS[7]}", antipodal_ok,
          f"antipodal -> {verdict_tag(antipodal_v)} (covariance scan passed); "
          f"same-shell witness pair {antipodal_pair}")

    # ---- 9. non-covariant imposter (axis)
    axis_v = verdict_by_kind["axis"]

    def canonical_word(word):
        return min(rotate_six(word, frame) for frame in frames)

    axis_witness_ok = False
    if axis_v["kind"] == "refuse_covariance":
        pair = [tuple(w) for w in axis_v["witness"]]
        occ_of = {tuple(p.archive): p.snapshot[1] for p in streams_by_kind["axis"]}
        axis_witness_ok = (
            len(pair) == 2
            and canonical_word(pair[0]) == canonical_word(pair[1])
            and occ_of.get(pair[0]) != occ_of.get(pair[1])
        )
    check(f"09 {CHECK_LABELS[8]}", axis_v["kind"] == "refuse_covariance" and axis_witness_ok,
          f"axis -> {verdict_tag(axis_v)}, witness={axis_v.get('witness')} (same orbit, occ differs)")

    # ---- 10. non-deterministic imposter (noisy)
    noisy_v = verdict_by_kind["noisy"]
    noisy_ok = (noisy_v["kind"] == "refuse_contradiction"
                and tuple(noisy_v["word"]) == NOISY_REPEAT_WORD)
    check(f"10 {CHECK_LABELS[9]}", noisy_ok,
          f"noisy -> {verdict_tag(noisy_v)}, repeated word={noisy_v.get('word')}")

    # ---- 11. held-corpus retraction (mimic) (P-F2)
    mimic_train_v = verdict_by_kind["mimic_train"]
    mimic_full_v = verdict_by_kind["mimic_full"]
    mimic_train_ok = (mimic_train_v["kind"] == "identified"
                      and mimic_train_v["law"] == "odd_shells")
    retract_witness = mimic_full_v.get("witnesses", {}).get("odd_shells")
    mimic_full_ok = (mimic_full_v["kind"] == "off_family"
                     and retract_witness is not None and sum(retract_witness) == 5)
    check(f"11 {CHECK_LABELS[10]}/train", mimic_train_ok,
          f"mimic train -> {verdict_tag(mimic_train_v)} (train-consistent)")
    check(f"11 {CHECK_LABELS[10]}/full_retract", mimic_full_ok,
          f"mimic full -> {verdict_tag(mimic_full_v)}, held witness {retract_witness} (weight 5)")

    # ---- 12. malformed-port refusals
    malformed_streams = build_malformed_streams()
    malformed_ok = 0
    malformed_rows = {}
    for label in sorted(MALFORMED_CATALOG):
        verdict = discriminate(malformed_streams[label], RULES, frames)
        got_reason = verdict.get("reason")
        row_ok = verdict["kind"] == "refuse_malformed" and got_reason == MALFORMED_CATALOG[label]
        malformed_ok += int(row_ok)
        malformed_rows[label] = {
            "kind": verdict["kind"], "reason": got_reason,
            "expected": MALFORMED_CATALOG[label], "ok": row_ok,
        }
    check(f"12 {CHECK_LABELS[11]}", malformed_ok == 8,
          f"{malformed_ok}/8 malformed streams refused with the expected reason")

    # ---- 13. verdict frame-invariance
    invariance_ok = 0
    frame_invariance_summary = {}
    for kind in ("in_family_full:unique_quorum", "antipodal"):
        base_stream = streams_by_kind[kind]
        base_verdict = discriminate(base_stream, RULES, frames)
        matches = 0
        for frame in frames:
            rotated_verdict = discriminate(rotate_stream(base_stream, frame), RULES, frames)
            if (rotated_verdict["kind"] == base_verdict["kind"]
                    and rotated_verdict.get("law") == base_verdict.get("law")
                    and rotated_verdict.get("consistent") == base_verdict.get("consistent")):
                matches += 1
        invariance_ok += int(matches == 24)
        frame_invariance_summary[kind] = {
            "frames": 24, "matches": matches, "kind": base_verdict["kind"],
            "law": base_verdict.get("law"),
        }
    check(f"13 {CHECK_LABELS[12]}", invariance_ok == 2,
          f"{invariance_ok}/2 streams frame-invariant across all 24 frames")

    # ---- 14. decoder blindness discipline
    signature_params = list(inspect.signature(discriminate).parameters)
    decoder_source = inspect.getsource(discriminate).lower()
    forbidden_tokens = ("manifest", "blind", "emit", "imposter", "mimic", "rules", "seed", "generate")
    tokens_present = [token for token in forbidden_tokens if token in decoder_source]
    check(f"14 {CHECK_LABELS[13]}",
          signature_params == ["stream", "tables", "frames"] and not tokens_present,
          f"signature={signature_params}, forbidden-tokens-present={tokens_present}")

    # ---- receipt assembly (written even on FAIL)
    def expected_tag_for(kind):
        if kind.split(":", 1)[0] in ("in_family_full", "in_family_train", "in_family_ext"):
            return f"identified:{kind.split(':', 1)[1]}"
        return EXPECTED_VERDICTS.get(kind)

    identification_table = {}
    for kind, verdict in sorted(verdict_by_kind.items()):
        tag = verdict_tag(verdict)
        expected = expected_tag_for(kind)
        identification_table[kind] = {
            "verdict": tag, "expected": expected, "correct": tag == expected,
        }

    firewalls = [
        "The five candidate tables and port grammar are supplied finite inputs; "
        "identifying a table does not identify nature's fixed Admissibility rule.",
        "occurrence / MEMBER / LAW_RECEIPT are supplied grammar fields; no objective "
        "actuality or framework-Record identification is claimed for any stream element.",
        "Acceptance profiles are Boolean; no frequency, weight, grade, or Born probability is "
        "computed or interpreted.",
        "The reference emitters are synthetic stream generators for harness self-test only; "
        "they are NOT formation routes, and the emitter's winner convention is supplied "
        "bookkeeping the decoder never reads beyond grammar well-formedness.",
        "Refusal verdicts about imposter streams are statements about those synthetic streams, "
        "not about any physical channel; no gravity content.",
    ]
    receipt.update({
        "date": DATE,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "breakthrough": False,
        "constitutional_effect": "none",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "contract": contract(),
        "blinded_verdicts": {label: normalize(v) for label, v in blinded_verdicts.items()},
        "unblind_manifest": dict(manifest),
        "identification_table": identification_table,
        "retraction_row": {
            "mimic_train": normalize(mimic_train_v),
            "mimic_full": normalize(mimic_full_v),
        },
        "refusal_rows": {
            "axis": normalize(axis_v),
            "noisy": normalize(noisy_v),
            "malformed": malformed_rows,
        },
        "frame_invariance": frame_invariance_summary,
        "interpretation_firewall": firewalls,
        "elapsed_seconds": round(time.time() - start, 3),
        "pass_count": PASS,
        "fail_count": FAIL,
        "pass": FAIL == 0,
    })

    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    print(
        "RESULT", PASS, FAIL, "OK" if FAIL == 0 else "FAIL",
        str(RECEIPT_PATH.relative_to(ROOT)),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
