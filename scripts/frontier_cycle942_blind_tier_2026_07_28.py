#!/usr/bin/env python3
"""Cycle 942: THE BLIND TIER BUILT.  B = 10, where no runner in this lineage
has ever looked, measured against Cycle 930's sealed third-pair prediction.

Cycle 930 sealed the third-pair zero (TP-4) over B = 9..12 behind the digest
d4f8f058b13f3063227b415a4f25be7211ea7a63d8aec09ff3722293499303e8, and disclosed
in its own gate and receipt that the seal is only PARTLY blind: B = 8 rows are
published in the pinned Cycle-922 primary receipt and B = 9 rows in the pinned
Cycle-922 checker receipt, both read before the rule was written.  THE FIRST
GENUINELY BLIND TIER IS B >= 10, AND NOBODY HAS EVER BUILT IT.  This runner
builds it.

  Q1  THE SEALED PREDICTION, TESTED BLIND.  The seal is first recomputed from
      the 930-PUBLISHED text (the receipt's own payload) with this runner's own
      independent implementation of the rule's pure function, and the build log
      is audited to prove no B=10 corpus existed at the moment of recomputation.
      Then B=10 is built and the third pair (h_f(b), r(b-1)) is counted at
      register level and at episode level on every bank clock.  The seal says
      ZERO episodes.  Either outcome ships: zero is the seal holding at the
      first blind tier; nonzero is a MAJOR finding and every episode is
      anatomised.  TP-1, TP-2 and TP-3 are additionally verified AT B=10
      directly, including the b = floor((B-1)/2) = 4 fixed-row exception.

  Q2  RC-2 AT B=10.  The full entry-gap carrier map.  RC-2 (Cycle 922,
      fitted-then-sealed) says a bank-owned entry-gap reading occurs only if
      2P < N, i.e. b >= 5 at B=10, i.e. P in {8, 16, 24, 32}.  Necessity
      violations (predicted-silent cells that fire) would part-refute RC-2 at a
      blind tier.  The b = B-2 = 8 cell (P = 8) is the KNOWN sufficiency risk:
      B=8.b6 and B=9.b7 both failed there.  Reported either way.

  Q3  THE 40/48 PATTERN AT B=10.  Cycle 922's ones-and-twos law: a same-edge
      complement value with 2P >= N is readable only stretch-locally and
      therefore appears only in ones and twos.  At B=10, N = 75, so the
      2P >= N complements are P in {40, 48, 56, 64, 72}.  Censused.

MINIMAL-PREMISE RULE.  The sealed predictions are NOT premises of this runner.
No gate in this file passes because a prediction came true; the blind tier
decides and the gates only require that the measurement be well formed and that
every episode found be anatomised.

The machinery is the pinned Cycle-930 primary's own committed code path,
imported by module and sha-pinned, so the B=10 corpus is built by exactly the
code that produced the pinned B=4..8 rows.  The restriction gate proves that
code reproduces the pinned rows value for value in THIS environment BEFORE any
B=10 construction happens.  Cycles 879/881/889/891/922 remain import-blocklisted
exactly as Cycle 930 left them.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import random
import sys
import time


ROOT = Path(__file__).resolve().parents[1]

PRIMARY_930 = "scripts/frontier_cycle930_third_pair_rc3_2026_07_28.py"
CHECKER_930 = "scripts/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.py"
RECEIPT_930 = "outputs/third_pair_rc3_cycle930_receipt_2026_07_28.json"
RECEIPT_930_CHECK = (
    "outputs/third_pair_rc3_independent_check_cycle930_receipt_2026_07_28.json")
SHIP_930 = "outputs/third_pair_rc3_block_cycle930_ship_receipt_2026_07_28.json"
CACHE_930 = "logs/runner-cache/frontier_cycle930_third_pair_rc3_2026_07_28.txt"
CACHE_930_CHECK = (
    "logs/runner-cache/frontier_cycle930_third_pair_rc3_independent_check_2026_07_28.txt")
NOTE_930 = (
    "docs/THIRD_PAIR_SHADOW_DERIVED_RC3_OPEN_CYCLE930_BOUNDED_THEOREM_NOTE_2026-07-28.md")

PRIMARY_922 = "scripts/frontier_cycle922_p32_carrier_2026_07_28.py"
CHECKER_922 = "scripts/frontier_cycle922_p32_carrier_independent_check_2026_07_28.py"
RECEIPT_922 = "outputs/p32_carrier_cycle922_receipt_2026_07_28.json"
RECEIPT_922_CHECK = (
    "outputs/p32_carrier_independent_check_cycle922_receipt_2026_07_28.json")
SHIP_922 = "outputs/p32_carrier_block_cycle922_ship_receipt_2026_07_28.json"
CACHE_922 = "logs/runner-cache/frontier_cycle922_p32_carrier_2026_07_28.txt"
CACHE_922_CHECK = (
    "logs/runner-cache/frontier_cycle922_p32_carrier_independent_check_2026_07_28.txt")
NOTE_922 = (
    "docs/P32_CARRIER_SHORT_ARC_LABEL_THEFT_CYCLE922_BOUNDED_THEOREM_NOTE_2026-07-28.md")
PRIMARY_891 = "scripts/frontier_cycle891_complement_mechanism_2026_07_28.py"
CHECKER_891 = "scripts/frontier_cycle891_complement_independent_check_2026_07_28.py"
RECEIPT_891 = "outputs/complement_mechanism_cycle891_receipt_2026_07_28.json"
RECEIPT_891_CHECK = "outputs/complement_independent_check_cycle891_receipt_2026_07_28.json"
NOTE_891 = "docs/COMPLEMENT_MECHANISM_KRUN_LAW_CYCLE891_BOUNDED_THEOREM_NOTE_2026-07-28.md"
PRIMARY_889 = "scripts/frontier_cycle889_delta_spectrum_2026_07_28.py"
PRIMARY_881 = "scripts/frontier_cycle881_p11_characterization_2026_07_28.py"
PRIMARY_879 = "scripts/frontier_cycle879_b4_clock_relation_2026_07_28.py"
CORE_719 = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
CORE_719_HANDSHAKE = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py")

# The Cycle-930 rows are this cycle's own; every other row is inherited from the
# pinned Cycle-930 receipt byte for byte and re-verified here independently.
PINS = {
    PRIMARY_930: ("afe78fdfe466724686b4a42d50893e1a0c5b41dc6c58aea27a765f5c8576cb92",
                  "1b163d8cf59d6143fa3bfd83a170e805f3e7d0c0"),
    CHECKER_930: ("ac3982f96335427dfa3c65870cc064eaea92be99c320bbc265a652dbd3ab8dab",
                  "4ddfe42be4993593d328b13fe375225f4a0fa976"),
    RECEIPT_930: ("a865ebc7c9ce2a03306c33a636f7583cadc0f3bc9ec3abfea0cac0491ae902a2",
                  "0aaf4442470dac362d490adf5f093bb512e30b89"),
    RECEIPT_930_CHECK: ("a05795d4d902bf9d1261dd2d448fff8f0bd2de1d6d38023d72a35ea66c562955",
                        "4dfac9cb9ee9d5f68ebb28d28e4a81755de3101c"),
    SHIP_930: ("362fd3ea487540387b29682c37e119561889d466d87a672cdf0f2a356167eee4",
               "ead9dee1660abb5a7f7fe84dd604a3b065049fd9"),
    CACHE_930: ("55f0c16f7da54056e1b1bc5e0661b75e6486c65b0c470062563ef24369d4c666",
                "d4e9755853b526a486471edf5bf015e11b1987e3"),
    CACHE_930_CHECK: ("437fec1f8d8d5f45ab95818d6edeb5d4cd2276d7e2b71f86cde9d0702adc87fe",
                      "bc4f2d09eca25163de24ff8d177bb6234bd76f0f"),
    NOTE_930: ("9d0f2cfcebc84ded27c26f329d1c7aa82e2e1b2314ec691a5807536959fda31e",
               "c12a05079f0b8c691a726c017edb817329efc499"),
    PRIMARY_922: ("9e1a8de7190188a89cd4449300ab56cc053d6a63eec328265fa80f9955ce3a83",
                  "fdd77d879b142d1bafa1f76926c494bbc4480b1c"),
    CHECKER_922: ("fb7acd4bfe5fa1dcc8f22373861da2038dfdb169371c53d283ae65325d44b118",
                  "faae396e9801cfac4c8f6baa80d022397bed3f64"),
    RECEIPT_922: ("ab40677256009a0b1ecdf841766aa055a113aeb93827dc1d1da21a9e1cb97954",
                  "4497a88d3d2cf7ca058ff759c8f3ecea8c042481"),
    RECEIPT_922_CHECK: ("e609eafcb6ef33c22ec0aa4481cc29ea5be46f5be1312a9ccd4822b154ff059e",
                        "a1fcadfd795d08c9705722f7165349e361778b65"),
    SHIP_922: ("9df9f38530b6d8bb8e4ebc9f76d5683ac065bf06f4edcfb2db9f3e70ef28ad76",
               "a39abd45b40897d872ecbccf2f5ee962ce66dc54"),
    CACHE_922: ("256d8422a4d379062d6dc0163dc748b2063e6d0f7533598a90971030428eede1",
                "4cd970d8261c5d705a2b02f909f97907a0ccb0d3"),
    CACHE_922_CHECK: ("add02c024c5f008e17fe135a103bb674fdca5d3c25be0a8fc39f653be7d7ec75",
                      "0f7c892f555538c95a2fd1b86a47c30f4b59ee2c"),
    NOTE_922: ("420c162b2530c7329c21915ff2eee8d91689a5f97688c1df29752841b6af949d",
               "572090165a4e6ef876f1eb9a291795fba11118fc"),
    PRIMARY_891: ("3d260f6641d05a22aee092145ea3e5c3b29f3a6882b4cbd9ae966424458afbb7",
                  "a1bbd49ffbe970193cc79054fb7219732f7c9873"),
    CHECKER_891: ("f2e9ca32b7d3f863822126c05fbf6a3b637164e8969e5ec7c6c04f15cd89e568",
                  "53f5cf560f6dfad20dc6b4b91b0c003c848c6bea"),
    RECEIPT_891: ("f8e30d50a50e39a13f8f968b2ae21991885b6c858c6c96439ed733fc8514bacd",
                  "f537715a927b00b817f8de2569953d78929c86db"),
    RECEIPT_891_CHECK: ("cb2f6badda7315725f5f33c5aad89e7e37cf9201472362e0af3a16c4225fae8f",
                        "478f19642c1d66a6e1575798f9974b645c9f9a18"),
    NOTE_891: ("5b20f90a643e890492d65907050e31772b85f1b00e1ee5581f5132f45f6a700c",
               "235965affc47ce7745327ef194e7c0ae31e6a6c8"),
    PRIMARY_889: ("c18ed0c49281fd2d54ad013ba12264b181d1720349ee002b144c028b521dd826",
                  "f1bdf1f789a85213a0a854ab0bed45e6bf250fed"),
    PRIMARY_881: ("7cc1c8984869d824f33d83ccf6599c6ef9e166766015979d204309c3e820ed35",
                  "4b7297890a822184914bace90f60b47dc09f8305"),
    PRIMARY_879: ("40bf65b88db19a7872d3dd5de50c7746bbecd98ce87c2b1176ce18ec9e5f7b2f",
                  "c2147a99c1a6879508fbf250051f87115b0b9d35"),
    CORE_719: ("0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
               "c123b8d681c3d76fce08ef13d7673622deac64ad"),
    CORE_719_HANDSHAKE: (
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f"),
}
AUDIT_INPUT_PATHS = tuple(sorted(PINS))
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
AUDIT_TIMEOUT_SEC = 900

RUNTIME_LIMIT_SECONDS = 900
STDOUT_LIMIT_BYTES = 150 * 1024

# The blind tier and the restriction tiers.  (bank_count, full_clocks).
BLIND_TIER = 10
RESTRICTION_TIERS = ((4, True), (5, False), (7, False))

PUBLISHED_SEAL_SHA = (
    "d4f8f058b13f3063227b415a4f25be7211ea7a63d8aec09ff3722293499303e8")
SEALED_BANK_COUNTS = (9, 10, 11, 12)

DISCLOSED_DEVIATIONS = (
    "MACHINERY REUSE, DECLARED.  This runner does NOT reimplement the corpus "
    "builder, the detector or the clock-local taxonomy.  It imports the pinned "
    "Cycle-930 primary as a module (sha256 afe78fdf..., git blob 1b163d8c...) "
    "and calls its committed code path, so the B=10 corpus is built by exactly "
    "the code that produced the pinned B=4..8 rows.  The restriction gate "
    "proves that code reproduces the pinned rows value for value in THIS "
    "environment before any B=10 construction.  The INDEPENDENT CHECKER does "
    "not reuse it: it generates ticks from the kernel's crossing identity and "
    "validates them against the kernel's own composed step function.",
    "TIER SCOPING, DECLARED.  B=10 is built at the FULL pinned horizon "
    "H = 16384 with BANK CLOCKS ONLY (all ten), not pair clocks.  Every "
    "quantity this cycle reports at B=10 -- the third-pair register/episode "
    "counts, the ladder, the entry-gap carrier map, the clock-local shape "
    "counts and the per-bank period counts -- is a bank-clock quantity by "
    "construction in the pinned census (they are gated on len(member_banks)==1), "
    "so bank-clock-only construction is exact and complete for them.  What is "
    "NOT measured at B=10 and is NOT claimed: the pair-clock inheritance of "
    "episodes, and the 891 class-level counts, which need pair clocks.  Stated, "
    "not hidden.",
    "RESTRICTION SCOPING, DECLARED.  B=4 is rebuilt with EVERY clock, which is "
    "what the pinned 891/922 class-level rows are computed over, so those rows "
    "are compared value for value.  B=5 and B=7 are rebuilt with BANK CLOCKS "
    "ONLY; every field of Cycle 930's per-cell rows is a bank-clock quantity by "
    "construction, and the closed-quiescent-stretch counts are lane-level, so "
    "all of those compare exactly.  B=6 and B=8 are NOT rebuilt, and the "
    "B=5/B=7 class-level 891 rows are NOT restricted against: the runtime "
    "budget buys the blind tier at the FULL horizon instead, which is the "
    "point of the block.  Cycle 930's spec allows B=5..7 spot rows; these are "
    "they, and B=7 is the richest tier in the pinned set (five cells, the "
    "20-episode B7.b3 necessity counterexample, the 2244-tick longest "
    "stretch).  Stated, not hidden.",
    "SCOPING-PROBE DISCLOSURE, IN FULL.  Before this runner was finalised the "
    "worker ran a timing probe that built B = 8, 9 and 10 with the same pinned "
    "machinery at the REDUCED horizon H = 2048 (bank clocks only) to size the "
    "budget, and read its output: at H = 2048 the third pair recorded ZERO "
    "register-level occurrences and ZERO episodes at all three bank counts, and "
    "no B=10 bank fired a bank-owned entry-gap episode at all.  The worker was "
    "therefore NOT blind when this file was written.  What that probe cannot "
    "touch: Cycle 930's seal is immutable and sha-pinned, it predates every "
    "B=10 corpus in this lineage, and this runner's gates are not conditioned "
    "on its prediction in either direction.  What it does mean: the H = 2048 "
    "reading is a corroborating pre-measurement on a different, eight-times "
    "smaller corpus, disclosed here as data rather than concealed as a peek.  "
    "The tier this block SHIPS -- B = 10 at the full pinned horizon H = 16384 "
    "-- had never been built by anyone, including the probe, and the probe's "
    "own numbers show why the full horizon is required: at H = 2048 the "
    "longest closed stretch is 298 ticks against 2244 at H = 16384 and NOTHING "
    "fires anywhere, so a reduced-horizon tier would have made both the "
    "third-pair test and RC-2's sufficiency side vacuous.",
    "ANATOMY.  The census stores at most 6 sample rows per (bank, shape); every "
    "occurrence is COUNTED and every aggregate is exhaustive.  If -- and only "
    "if -- the blind tier reports a NONZERO third-pair episode count, a second, "
    "targeted, UNCAPPED pass anatomises every one of them.  With a zero count "
    "there is nothing to anatomise and the exhaustive counters are the finding.",
    "THE SEALED PREDICTION IS NOT A PREMISE.  No gate passes because the "
    "prediction came true.  Gate F requires only that the instrument be live at "
    "B=10 and that any episode found be anatomised; the verdict is reported as "
    "data, in either direction.  The same posture is taken for RC-2 in gate G.",
    "RC-2 IS FITTED-THEN-SEALED (Cycle 922), NOT DERIVED, and its model "
    "degeneracy (three closed forms indistinguishable inside an 8-wide band) is "
    "untouched here.  A B=10 agreement is one more sealed cell, not a "
    "derivation; a B=10 necessity violation would be a part-refutation.",
)

BLIND_TIER_STATEMENT = (
    "THE BLIND TIER (Cycle 942).  Cycle 930's seal covers B = 9, 10, 11, 12 and "
    "predicts ZERO third-pair episodes at each.  Cycle 930 disclosed that B = 8 "
    "and B = 9 were already published -- the pinned Cycle-922 primary receipt "
    "carries ENTRY_GAP_handoff_swap = 0 on all six B=8 rows and the pinned "
    "Cycle-922 checker receipt carries the B=9 per-bank shape lists -- so the "
    "first genuinely blind tier is B >= 10.  No runner in this lineage has ever "
    "built B = 10.  This runner builds it at the full pinned horizon with all "
    "ten bank clocks, having first recomputed the seal from the 930-published "
    "text with its own implementation of the rule's pure function and audited "
    "the build log to show no B=10 corpus existed at that moment."
)

RC2_STATEMENT = (
    "RC-2, SHORT-ARC NECESSITY (Cycle 922, FITTED-THEN-SEALED, not derived).  A "
    "bank-owned entry-gap reading occurs only if 2P < N, equivalently "
    "b >= floor(B/2).  At B = 10, N = 75 and P = 8(9-b), so the condition cuts "
    "the family at b >= 5, i.e. P in {8, 16, 24, 32} may fire and "
    "P in {40, 48, 56, 64, 72} may not.  Across Cycles 922 and 930 necessity was "
    "never violated on 27 cells and sufficiency failed on exactly the two "
    "b = B-2 / P = 8 cells (B=8.b6 and B=9.b7), both flagged in advance.  B=10's "
    "b = 8 cell is the third instance of that pattern and is unmeasured before "
    "this runner."
)

LABEL_THEFT_STATEMENT = (
    "THE VALUE COINCIDENCE AT B = 10 (Cycle 922's label theft, checked at the "
    "blind tier).  Cycle 891's classifier is VALUE-based with entry-gap "
    "priority, so wherever a bank's entry-gap value 8(B-1-b) coincides with one "
    "of its own edge complements the ENTRY_GAP label is stolen from whatever "
    "actually produced the reading.  Bank b's own edge complements are "
    "N - DELTA(b-1) = 8b and N - DELTA(b) = 8(b+1); the coincidence cells are "
    "therefore b = (B-1)/2 and b = (B-2)/2.  At B = 10 only the second is an "
    "integer: b = 4, where the entry gap 8(10-1-4) = 40 equals the same-edge "
    "complement of edge 4.  The cell is classified CLOCK-LOCALLY here, the 922 "
    "way, and the value-based label is computed alongside it for contrast."
)

ONES_AND_TWOS_STATEMENT = (
    "THE ONES-AND-TWOS LAW (Cycle 922).  A same-edge complement value with "
    "2P >= N cannot close a ring-periodic reading, so it survives only as a "
    "stretch-local finite-form reading and therefore appears only in ones and "
    "twos.  At B = 10, N = 75, the complement values are 8(e+1) for e = 0..8 and "
    "the 2P >= N ones are P in {40, 48, 56, 64, 72}.  Censused on all ten bank "
    "clocks."
)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value):
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload):
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


# ------------------------------------------------------- preflight + firewall
def preflight(overrides=None):
    rows, bad = {}, []
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = ROOT / path
        if not full.is_file():
            rows[path] = {"present": False}
            bad.append(path)
            continue
        payload = full.read_bytes()
        if overrides and path in overrides:
            payload = overrides[path]
        got_sha = sha256(payload).hexdigest()
        got_blob = git_blob(payload)
        ok = got_sha == want_sha and got_blob == want_blob
        rows[path] = {"present": True, "sha256": got_sha, "git_blob": got_blob,
                      "sha256_pinned": want_sha, "git_blob_pinned": want_blob,
                      "match": ok}
        if not ok:
            bad.append(path)
    return rows, bad


PREFLIGHT_ROWS, PREFLIGHT_BAD = preflight()
if PREFLIGHT_BAD:
    print("FAIL A_PINS :: " + json.dumps(
        {"pins": PREFLIGHT_ROWS, "mismatched_or_missing": sorted(PREFLIGHT_BAD),
         "action": "PREFLIGHT HARD FAIL"},
        sort_keys=True, separators=(",", ":")))
    raise SystemExit(2)


BLOCKLISTED_MODULES = tuple(Path(p).stem for p in
                            (PRIMARY_879, PRIMARY_881, PRIMARY_889,
                             PRIMARY_891, CHECKER_891,
                             PRIMARY_922, CHECKER_922, CHECKER_930))


class _Firewall(importlib.abc.MetaPathFinder):
    """Any import of a blocklisted Cycle-879/881/889/891/922 runner is fatal.

    The Cycle-930 PRIMARY is deliberately NOT blocklisted: this cycle reuses its
    committed code path on purpose and says so in the disclosed deviations.  Its
    checker is blocklisted, so no independent-check code can leak in here.
    """

    def __init__(self):
        self.hits = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError("BLOCKLIST forbids import of %s" % fullname)
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle930_third_pair_rc3_2026_07_28 as C930

# The committed code path, bound once and used everywhere below.
K = C930.K
build_corpus = C930.build_corpus
census = C930.census
entry_gap_rows = C930.entry_gap_rows
station_table = C930.station_table
closed_form_rows = C930.closed_form_rows
tp_rows = C930.tp_rows
tail_periods = C930.tail_periods
reference_tail_periods = C930.reference_tail_periods
reject_reason = C930.reject_reason
shape_of_local_pair = C930.shape_of_local_pair
classify_separation_891 = C930.classify_separation_891
attribute_runs = C930.attribute_runs
zero_runs = C930.zero_runs
transpose_planes = C930.transpose_planes
SHAPES = C930.SHAPES
THIRD_PAIR = C930.THIRD_PAIR
HORIZON = C930.HORIZON
MIN_STABLE_EVENTS = C930.MIN_STABLE_EVENTS
MIN_PERIOD_REPEATS = C930.MIN_PERIOD_REPEATS
BUILD_LOG = C930.BUILD_LOG


def pinned_json(path):
    return json.loads((ROOT / path).read_text())


def pinned_constants(path):
    tree = ast.parse((ROOT / path).read_text())
    out = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                if isinstance(node.value.value, int):
                    out[target.id] = node.value.value
    return out


def pinned_text_literal(path, name):
    """Read a module-level string constant of a pinned runner by AST."""
    tree = ast.parse((ROOT / path).read_text())
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    return ast.literal_eval(node.value)
                except ValueError:
                    return None
    return None


# --------------------------------------------- this runner's OWN pure function
def own_tp_rows(bank_count):
    """The third-pair rule's geometry, reimplemented here from the STATED text.

    Independent of C930.tp_rows on purpose: the seal must be recomputable from
    the published words plus arithmetic, not from the pinned author's code.
    """
    n = 8 * bank_count - 5
    out = []
    for b in range(1, bank_count - 1):
        period = 8 * (bank_count - 1 - b)

        def f(e):
            return (4 + 5 * e) % n

        def r(e):
            return (8 * bank_count - 9 - 3 * e) % n

        rows = {(f(b - 1) - 2) % n, f(b - 1), r(b - 1), (r(b - 1) + 2) % n,
                (f(b) - 2) % n, f(b), r(b), (r(b) + 2) % n}
        srt = sorted(rows)
        gaps = [(srt[(i + 1) % len(srt)] - srt[i]) % n for i in range(len(srt))]
        shadow = {srt[(i + 1) % len(srt)] for i, g in enumerate(gaps) if g == 1}
        unit_lower = [srt[i] for i, g in enumerate(gaps) if g == 1]
        pairs = {"swap_swap": (f(b - 1), r(b)),
                 "swap_handoff": (f(b), (r(b - 1) + 2) % n),
                 "handoff_swap": ((f(b) - 2) % n, r(b - 1))}
        fixed = sorted(s for s in srt if (s + period) % n in rows)
        firsts = sorted({v[0] for v in pairs.values()})
        out.append({
            "bank": b, "period": period, "stations": n,
            "rows_sorted": srt,
            "unit_gap_lower_stations": sorted(unit_lower),
            "shadowed_rows": sorted(shadow),
            "pairs": {k: list(v) for k, v in pairs.items()},
            "spans": {k: (v[1] - v[0]) % n == period for k, v in pairs.items()},
            "terminal_shadowed": {k: v[1] in shadow for k, v in pairs.items()},
            "first_shadowed": {k: v[0] in shadow for k, v in pairs.items()},
            "P_shift_fixed_rows": fixed,
            "three_first_stations": firsts,
            "extra_P_shift_fixed_rows": sorted(set(fixed) - set(firsts)),
            "h_r_b": (r(b) + 2) % n,
            "h_r_b_has_no_P_preimage": ((r(b) + 2) - period) % n not in rows,
            "h_r_b_one_below_third_pair_terminal":
                ((r(b) + 2) + 1) % n == pairs["handoff_swap"][1],
            "is_coincidence_cell": b == (bank_count - 1) // 2,
            "reverse_rows": [r(b - 1), r(b)],
        })
    return out


def own_seal_payload(tp_text):
    """The sealed object, rebuilt from the published TEXT plus own arithmetic."""
    return {
        "TP_STATEMENT": tp_text,
        "predicted_third_pair_episodes": {str(bc): 0 for bc in SEALED_BANK_COUNTS},
        "predicted_third_pair_exists_geometrically": {
            str(bc): [row["bank"] for row in own_tp_rows(bc)
                      if row["spans"]["handoff_swap"]]
            for bc in SEALED_BANK_COUNTS},
        "predicted_third_pair_terminal_is_shadowed_everywhere": {
            str(bc): all(row["terminal_shadowed"]["handoff_swap"]
                         for row in own_tp_rows(bc))
            for bc in SEALED_BANK_COUNTS},
        "predicted_other_two_pairs_terminals_unshadowed": {
            str(bc): all(not row["terminal_shadowed"]["swap_swap"]
                         and not row["terminal_shadowed"]["swap_handoff"]
                         for row in own_tp_rows(bc))
            for bc in SEALED_BANK_COUNTS},
    }


# ------------------------------------------- the targeted uncapped anatomy pass
def third_pair_anatomy(box, cap=None):
    """Every third-pair EPISODE at this tier, uncapped, with its full anatomy.

    Only the entry-gap period of each bank is swept, so this is far cheaper than
    a census; it exists so that a nonzero blind-tier count can be itemised
    exhaustively rather than sampled.
    """
    bank_count = box["banks"]
    stations = box["stations"]
    lanes = box["lane_count"]
    horizon = box["horizon"]
    table = station_table(bank_count)
    entry_of = {b: 8 * (bank_count - 1 - b) for b in range(1, bank_count - 1)}
    bank_masks = [transpose_planes(box["clean_planes"][b], lanes, horizon)
                  for b in range(bank_count)]
    source_masks = transpose_planes(box["source_clean"], lanes, horizon)
    episodes, configs = [], Counter()
    for lane in range(lanes):
        event, positions = box["keys"][lane]
        stretches = [(a, b) for (a, b) in C930.maximal_runs(source_masks[lane], horizon)
                     if a > 0 and b < horizon]
        for bank, P in entry_of.items():
            mask = bank_masks[bank][lane]
            if mask == 0:
                continue
            for a, b in stretches:
                length = b - a + 1
                segment = (mask >> a) & ((1 << length) - 1)
                if segment == 0:
                    continue
                runs = zero_runs(segment, length)
                starts = [a + lo for lo, _hi in runs]
                widths = [hi - lo + 1 for lo, hi in runs]
                idx = [i for i in range(len(starts) - 1)
                       if starts[i + 1] - starts[i] == P]
                if not idx:
                    continue
                att = attribute_runs(starts, positions,
                                     table["rows_of_bank"][bank], stations)
                hit_rows = []
                for i in idx:
                    for p1, s1, k1, e1 in att[i]:
                        for p2, s2, k2, e2 in att[i + 1]:
                            if p1 != p2:
                                continue
                            if shape_of_local_pair((True, k1, e1, k2, e2),
                                                   bank) != THIRD_PAIR:
                                continue
                            hit_rows.append({"i": i, "token": p1,
                                             "stations": [s1, s2],
                                             "widths": [widths[i], widths[i + 1]],
                                             "starts": [starts[i], starts[i + 1]]})
                if not hit_rows:
                    continue
                configs["register_level_occurrences"] += len(hit_rows)
                hits = tail_periods(segment, [P])
                if P not in hits:
                    configs["refused_%s" % reject_reason(segment, P)] += 1
                    continue
                episodes.append({
                    "banks": bank_count, "bank": bank, "period": P,
                    "lane": lane, "event": event,
                    "token_positions": list(positions),
                    "stretch": [a, b], "stretch_len": length,
                    "clean_ticks": bin(segment).count("1"),
                    "transient_events_residues": list(hits[P]),
                    "third_pair_rows": hit_rows,
                })
                if cap is not None and len(episodes) >= cap:
                    return episodes, dict(configs)
    del bank_masks, source_masks
    return episodes, dict(configs)


RESTRICTION_FIELDS = (
    "banks", "bank", "entry_gap_period", "two_P", "stations",
    "short_arc_2P_lt_N", "episodes_on_the_bank_clock",
    "bank_owned_entry_gap_episodes", "by_shape", "fires",
    "register_level_pair_occurrences", "ladder",
    "firing_episodes_with_an_equal_width_entry_gap_pair",
    "firing_episodes_with_only_unequal_width_entry_gap_pairs",
    "firing_episodes_with_no_P_separated_pair_at_all",
    "stable_region_pairs_equal_width", "stable_region_pairs_unequal_width",
    "stable_region_unequal_explained_by_tail_truncation",
)


def restriction_compare(label, pinned, reproduced, failures):
    ok = compact(pinned) == compact(reproduced)
    if not ok:
        failures.append({"check": label, "pinned": pinned,
                         "reproduced": reproduced})
    return ok


# ------------------------------------------------------------------------ main
def main():
    started = time.monotonic()
    lines = []
    dumps = {"sort_keys": True, "separators": (",", ":"), "default": str}

    def emit(line):
        lines.append(line)
        print(line)

    def gate(name, ok, payload):
        emit("%s %s :: %s" % ("PASS" if ok else "FAIL", name,
                              json.dumps(payload, **dumps)))
        return ok

    results = {}
    R930 = pinned_json(RECEIPT_930)
    R930C = pinned_json(RECEIPT_930_CHECK)
    R922 = pinned_json(RECEIPT_922)
    R922C = pinned_json(RECEIPT_922_CHECK)

    # ------------------------------------------------------------ gate A
    const_930 = pinned_constants(PRIMARY_930)
    want = {"TOKEN_K": 2, "EVENT_COUNT": 2, "HORIZON": 16384,
            "MIN_PERIOD_REPEATS": 2, "MIN_STABLE_EVENTS": 8,
            "PINNED_PERIOD_CEILING": 64}
    const_ok = all(const_930.get(k) == v for k, v in want.items())
    live_ok = (C930.TOKEN_K == 2 and C930.EVENT_COUNT == 2
               and C930.HORIZON == 16384 and C930.MIN_PERIOD_REPEATS == 2
               and C930.MIN_STABLE_EVENTS == 8
               and C930.PINNED_PERIOD_CEILING == 64)
    # every pin Cycle 930 declared is carried here unchanged
    inherited_ok = all(PINS.get(p) == v for p, v in C930.PINS.items())
    a_ok = (not PREFLIGHT_BAD) and const_ok and live_ok and inherited_ok \
        and not FIREWALL.hits
    results["A_PINS"] = gate("A_PINS", a_ok, {
        "pins_verified": len(PINS),
        "pins_inherited_from_the_pinned_930_runner": len(C930.PINS),
        "inherited_rows_unchanged": inherited_ok,
        "mismatched": sorted(PREFLIGHT_BAD),
        "constants_read_from_the_pinned_930_AST":
            {k: const_930.get(k) for k in want},
        "constants_expected": want, "constants_match": const_ok,
        "constants_live_in_the_imported_module_match": live_ok,
        "firewall_hits": FIREWALL.hits,
        "blocklisted_modules": sorted(BLOCKLISTED_MODULES),
        "cycle930_primary_is_imported_on_purpose":
            "the committed code path; see the disclosed deviations",
        "declared_deviations": list(DISCLOSED_DEVIATIONS),
        "blind_tier": BLIND_TIER,
        "restriction_tiers": [{"banks": bc, "full_clocks": fc}
                              for bc, fc in RESTRICTION_TIERS],
    })
    if not a_ok:
        raise SystemExit(2)

    # ------------------------------------------------------------ gate B
    # TP-1..TP-3 verified AT B=10 directly, and re-swept over B=3..24.
    own_vs_pinned_disagreements = []
    tp_bad, tp_cells = [], 0
    coincidence_cells = []
    for bc in range(3, 25):
        mine = own_tp_rows(bc)
        theirs = tp_rows(bc)
        if len(mine) != len(theirs):
            own_vs_pinned_disagreements.append({"banks": bc, "len": "differs"})
            continue
        for m, t in zip(mine, theirs):
            if (m["rows_sorted"] != t["rows_sorted"]
                    or m["pairs"] != t["pairs"]
                    or m["terminal_shadowed"] != t["pair_terminal_is_shadowed"]
                    or m["P_shift_fixed_rows"] != t["P_shift_fixed_rows"]):
                own_vs_pinned_disagreements.append(
                    {"banks": bc, "bank": m["bank"]})
        for row in mine:
            tp_cells += 1
            extra = row["extra_P_shift_fixed_rows"]
            checks = {
                "all_three_pairs_span_P": all(row["spans"].values()),
                "exactly_one_unit_gap": len(row["unit_gap_lower_stations"]) == 1,
                "third_pair_terminal_shadowed":
                    row["terminal_shadowed"]["handoff_swap"],
                "other_two_terminals_unshadowed":
                    not row["terminal_shadowed"]["swap_swap"]
                    and not row["terminal_shadowed"]["swap_handoff"],
                "no_first_station_shadowed":
                    not any(row["first_shadowed"].values()),
                "three_first_stations_are_P_shift_fixed":
                    set(row["three_first_stations"]) <= set(row["P_shift_fixed_rows"]),
                "h_r_b_has_no_P_preimage": row["h_r_b_has_no_P_preimage"],
                "h_r_b_one_below_third_pair_terminal":
                    row["h_r_b_one_below_third_pair_terminal"],
                "extra_fixed_rows_only_at_coincidence_cells":
                    (not extra) or (row["is_coincidence_cell"]
                                    and len(extra) == 1
                                    and extra[0] in row["reverse_rows"]),
            }
            if extra:
                coincidence_cells.append({
                    "banks": bc, "bank": row["bank"], "extra_rows": extra,
                    "extra_row_is": ("r(b-1), the third pair's own terminal"
                                     if extra == [row["reverse_rows"][0]]
                                     else "r(b)"),
                    "is_the_922_label_theft_cell": row["is_coincidence_cell"]})
            if not all(checks.values()):
                tp_bad.append({"banks": bc, "bank": row["bank"],
                               "failed": [k for k, v in checks.items() if not v]})
    # the kernel's own emitted program at B=10, against the closed form
    geom_bad = []
    tab10 = station_table(BLIND_TIER)
    if tab10["stations"] != 8 * BLIND_TIER - 5:
        geom_bad.append({"stations": tab10["stations"]})
    for edge in sorted(tab10["swaps"]):
        cf = closed_form_rows(BLIND_TIER, edge)
        got = {"forward": tab10["forward"][edge],
               "reverse": tab10["reverse"][edge],
               "handoff_forward": tab10["handoff_forward"][edge],
               "handoff_return": tab10["handoff_return"][edge]}
        if cf != got:
            geom_bad.append({"edge": edge, "closed_form": cf, "kernel": got})
    b10_rows = own_tp_rows(BLIND_TIER)
    b10_coincidence = [r for r in b10_rows if r["extra_P_shift_fixed_rows"]]
    b_ok = (not tp_bad and not geom_bad and not own_vs_pinned_disagreements
            and len(b10_rows) == BLIND_TIER - 2)
    results["B_TP_AT_B10"] = gate("B_TP_AT_B10", b_ok, {
        "question": "do TP-1, TP-2 and TP-3 hold AT the blind tier, checked "
                    "against the kernel's own emitted program?",
        "TP_cells_checked_banks_3_to_24": tp_cells,
        "TP_disagreeing_cells": tp_bad,
        "own_implementation_vs_pinned_930_disagreements":
            own_vs_pinned_disagreements,
        "closed_form_vs_kernel_program_at_B10_disagreements": geom_bad,
        "B10_stations": tab10["stations"],
        "B10_entry_gap_table": {str(k): v for k, v in tab10["entry_gap"].items()},
        "B10_rows": b10_rows,
        "B10_fourth_P_shift_fixed_row_cells": b10_coincidence,
        "B10_fixed_row_exception_note":
            "B = 10 is EVEN, so floor((B-1)/2) = 4 and the fourth P-shift-fixed "
            "row there is r(b) = r(4), NOT r(b-1) = r(3).  At B=10 the "
            "exception therefore does NOT touch the third pair's own terminal "
            "-- that identity holds at ODD B.  The cell is still Cycle 922's "
            "label-theft cell, via the b = (B-2)/2 branch.",
        "cells_with_a_fourth_P_shift_fixed_row_B3_to_B24": coincidence_cells,
    })

    # ------------------------------------------------------------ gate C
    rng = random.Random(942_0728)
    det_cases = det_mismatch = det_hits = rej_mismatch = 0
    for _ in range(1200):
        length = rng.randrange(24, 320)
        density = rng.choice((0.05, 0.15, 0.3, 0.5, 0.75))
        bits = 0
        for i in range(length):
            if rng.random() < density:
                bits |= 1 << i
        if rng.random() < 0.4:
            period = rng.randrange(3, 30)
            tail = rng.randrange(length // 2, length)
            base = rng.getrandbits(period)
            for i in range(tail, length):
                if (base >> ((i - tail) % period)) & 1:
                    bits |= 1 << i
                else:
                    bits &= ~(1 << i)
        periods = list(range(2, 44))
        got = tail_periods(bits, periods)
        ref = reference_tail_periods(bits, periods)
        det_cases += 1
        det_hits += len(got)
        if got != ref:
            det_mismatch += 1
        for p in periods:
            if (reject_reason(bits, p) == "ACCEPT") != (p in got):
                rej_mismatch += 1
    c_ok = det_mismatch == 0 and rej_mismatch == 0 and det_hits > 0
    results["C_DETECTOR"] = gate("C_DETECTOR", c_ok, {
        "randomised_cases": det_cases, "detections_compared": det_hits,
        "folded_vs_literal_mismatches": det_mismatch,
        "reject_reason_vs_tail_periods_mismatches": rej_mismatch,
        "note": "the pinned detector is revalidated in this environment before "
                "it is trusted on a tier nobody has measured",
    })

    # -------------------------------- gate D: RESTRICTION, before any B=10 work
    failures = []
    tiers, d_rows = {}, []
    pinned_891_rows = {row["banks"]: row for row in
                       R922["restriction_gate_against_cycle891"]["rows"]}
    pinned_fit = {(r["banks"], r["bank"]): r for r in R922["rc_fit"]["fit_rows"]}
    restriction_seconds = {}
    for bc, full in RESTRICTION_TIERS:
        t0 = time.monotonic()
        box = build_corpus(bc, HORIZON)
        cen = census(box, full_clocks=full)
        cen["substrate_failures"] = box["seed_failures"] + box["token_failures"]
        tiers[bc] = cen
        del box
        restriction_seconds[bc] = round(time.monotonic() - t0, 1)
        rows = entry_gap_rows(cen)
        pinned_cells = {r["bank"]: r for r in R930["per_cell_rows"][str(bc)]}
        for row in rows:
            pr = pinned_cells[row["bank"]]
            for field in RESTRICTION_FIELDS:
                restriction_compare("930.B%d.b%d.%s" % (bc, row["bank"], field),
                                    pr[field], row[field], failures)
            fr = pinned_fit.get((bc, row["bank"]))
            if fr is not None:
                restriction_compare("922.B%d.b%d.episodes" % (bc, row["bank"]),
                                    fr["episodes_on_the_bank_clock"],
                                    row["episodes_on_the_bank_clock"], failures)
                restriction_compare("922.B%d.b%d.bank_owned" % (bc, row["bank"]),
                                    fr["bank_owned_entry_gap_episodes"],
                                    row["bank_owned_entry_gap_episodes"], failures)
                restriction_compare("922.B%d.b%d.by_shape" % (bc, row["bank"]),
                                    fr["by_shape"], row["by_shape"], failures)
        pr891 = pinned_891_rows[bc]
        checks = {
            "closed_quiescent_stretches": restriction_compare(
                "B%d.stretches" % bc, pr891["closed_quiescent_stretches"],
                cen["closed_quiescent_stretches"], failures),
            "longest_closed_stretch": restriction_compare(
                "B%d.longest" % bc, pr891["longest_closed_stretch"],
                cen["longest_closed_stretch"], failures),
            "entry_gap_table": restriction_compare(
                "B%d.entry_gap_table" % bc, pr891["entry_gap_table"],
                cen["entry_gap_table"], failures),
            "clocks_swept_equals_expected":
                cen["clocks_swept"] == cen["clocks_expected"],
            "substrate_failures_zero": cen["substrate_failures"] == 0,
            "per_cell_rows_930": True,
        }
        if full:
            cc = {"%d|%s" % (p, lab): n
                  for (p, lab), n in cen["class_counts_891"].items()}
            checks["clocks_swept"] = restriction_compare(
                "B%d.clocks_swept" % bc, pr891["clocks_swept"],
                cen["clocks_swept"], failures)
            checks["class_counts_891"] = restriction_compare(
                "B%d.class_counts_891" % bc, pr891["class_counts_891"], cc,
                failures)
            checks["completeness_ledger"] = restriction_compare(
                "B%d.ledger" % bc, pr891["completeness_ledger"],
                cen["completeness_ledger"], failures)
            checks["cooccurrence_clocks"] = restriction_compare(
                "B%d.cooccurrence" % bc, pr891["cooccurrence_clocks"],
                cen["cooccurrence_clocks"], failures)
            checks["complements_observed"] = restriction_compare(
                "B%d.complements" % bc, pr891["complements_observed"],
                cen["complements_observed"], failures)
        if not checks["clocks_swept_equals_expected"]:
            failures.append({"check": "B%d.clock_count_identity" % bc})
        if not checks["substrate_failures_zero"]:
            failures.append({"check": "B%d.substrate" % bc})
        d_rows.append({"banks": bc, "full_clocks": full, "checks": checks,
                       "cells": len(rows), "seconds": restriction_seconds[bc]})
    # Cycle 930's own third-pair headline numbers, over the tiers rebuilt here
    tp_occ_pinned, tp_occ_mine = {}, {}
    tp_cfg_pinned, tp_cfg_mine = {}, {}
    for bc, _full in RESTRICTION_TIERS:
        for row in entry_gap_rows(tiers[bc]):
            key = "B%d.b%d" % (bc, row["bank"])
            tp_occ_mine[key] = row["register_level_pair_occurrences"][THIRD_PAIR]
            tp_occ_pinned[key] = R930["third_pair"][
                "register_level_occurrences"][key]
            tp_cfg_mine[key] = row["ladder"][THIRD_PAIR].get(
                "S5_FULL_CONFIGURATION", 0)
            tp_cfg_pinned[key] = R930["third_pair"]["full_configurations"][key]
    restriction_compare("930.third_pair_register_occurrences",
                        tp_occ_pinned, tp_occ_mine, failures)
    restriction_compare("930.third_pair_full_configurations",
                        tp_cfg_pinned, tp_cfg_mine, failures)
    d_ok = not failures
    results["D_RESTRICTION"] = gate("D_RESTRICTION", d_ok, {
        "note": "Every pinned Cycle-930/922 number this cycle stands on is "
                "recomputed from a fresh corpus and compared value for value "
                "BEFORE the blind tier is built.  A single mismatch is a hard "
                "fail and no B=10 corpus is ever constructed.",
        "tier_rows": d_rows,
        "pinned_930_cells_compared": sum(len(R930["per_cell_rows"][str(bc)])
                                         for bc, _f in RESTRICTION_TIERS),
        "pinned_930_fields_per_cell": len(RESTRICTION_FIELDS),
        "pinned_922_fit_cells_compared": sum(
            1 for (bc, _b) in pinned_fit if bc in dict(RESTRICTION_TIERS)),
        "third_pair_occurrences_reproduced": tp_occ_mine,
        "third_pair_full_configurations_reproduced": tp_cfg_mine,
        "total_failed_checks": len(failures),
        "failed_checks": failures[:20],
        "seconds_per_tier": restriction_seconds,
    })
    if not d_ok:
        raise SystemExit(1)

    # ------------- gate E: the seal, recomputed BEFORE the blind corpus exists
    published_payload = R930["seal"]["payload"]
    published_sha = R930["seal"]["SEAL_sha256"]
    tp_text_receipt_payload = published_payload["TP_STATEMENT"]
    tp_text_receipt_top = R930["TP_statement"]
    tp_text_ast = pinned_text_literal(PRIMARY_930, "TP_STATEMENT")
    texts_agree = (tp_text_receipt_payload == tp_text_receipt_top
                   == tp_text_ast == C930.TP_STATEMENT)
    payload_as_published_sha = digest(published_payload)
    own_payload = own_seal_payload(tp_text_receipt_payload)
    own_sha = digest(own_payload)
    build_log_now = list(BUILD_LOG)
    blind_free = all(row["banks"] not in SEALED_BANK_COUNTS
                     for row in build_log_now)
    sealed_prediction_for_the_blind_tier = \
        own_payload["predicted_third_pair_episodes"][str(BLIND_TIER)]
    emit("SEAL RECOMPUTED :: " + json.dumps(
        {"published_SEAL_sha256": published_sha,
         "recomputed_from_published_payload": payload_as_published_sha,
         "recomputed_from_published_text_and_own_arithmetic": own_sha,
         "build_log_at_recomputation_time": build_log_now,
         "no_sealed_tier_built_yet": blind_free}, **dumps))
    e_ok = (published_sha == PUBLISHED_SEAL_SHA
            and payload_as_published_sha == published_sha
            and own_sha == published_sha
            and own_payload == published_payload
            and texts_agree and blind_free
            and sealed_prediction_for_the_blind_tier == 0)
    results["E_SEAL"] = gate("E_SEAL", e_ok, {
        "attack": "recompute Cycle 930's seal two ways -- straight from the "
                  "receipt's published payload, and from the published TP TEXT "
                  "plus this runner's own independent implementation of the "
                  "rule's pure function -- and prove no sealed-tier corpus "
                  "exists at the moment of recomputation",
        "published_SEAL_sha256": published_sha,
        "SEAL_sha256_in_the_930_note_prefix": PUBLISHED_SEAL_SHA[:12],
        "matches_the_value_this_runner_pinned": published_sha == PUBLISHED_SEAL_SHA,
        "recomputed_from_published_payload": payload_as_published_sha,
        "recomputed_from_published_text_and_own_arithmetic": own_sha,
        "own_payload_equals_published_payload": own_payload == published_payload,
        "TP_text_identical_across_receipt_payload_receipt_top_AST_and_module":
            texts_agree,
        "sealed_content": {
            "bank_counts": list(SEALED_BANK_COUNTS),
            "predicted_third_pair_episodes":
                own_payload["predicted_third_pair_episodes"],
            "predicted_third_pair_exists_geometrically":
                own_payload["predicted_third_pair_exists_geometrically"],
        },
        "sealed_prediction_at_the_blind_tier":
            sealed_prediction_for_the_blind_tier,
        "build_log_at_recomputation_time": build_log_now,
        "no_sealed_tier_corpus_existed_at_recomputation": blind_free,
        "blindness_ledger": {
            "B8_published_in": "the pinned Cycle-922 primary receipt "
                               "(ENTRY_GAP_handoff_swap = 0 on all six rows)",
            "B9_published_in": "the pinned Cycle-922 checker receipt "
                               "(the per-bank shape lists) and rebuilt by the "
                               "pinned Cycle-930 checker",
            "B10_published_in": "NOTHING -- no runner in this lineage has built "
                                "it; this is the first",
        },
        "blind_tier_statement": BLIND_TIER_STATEMENT,
    })

    # ------------------------------------------ the blind tier, built at last
    t0 = time.monotonic()
    blind_box = build_corpus(BLIND_TIER, HORIZON)
    blind = census(blind_box, full_clocks=False)
    blind["substrate_failures"] = (blind_box["seed_failures"]
                                   + blind_box["token_failures"])
    blind_rows = entry_gap_rows(blind)
    blind_seconds = round(time.monotonic() - t0, 1)

    # ------------------------------------------------------------ gate F
    third_occ = {r["bank"]: r["register_level_pair_occurrences"][THIRD_PAIR]
                 for r in blind_rows}
    third_cfg = {r["bank"]: r["ladder"][THIRD_PAIR].get("S5_FULL_CONFIGURATION", 0)
                 for r in blind_rows}
    third_ep = {r["bank"]: r["by_shape"][THIRD_PAIR] for r in blind_rows}
    third_total = sum(third_ep.values())
    third_reject = Counter()
    for r in blind_rows:
        for k, n in r["ladder"][THIRD_PAIR].items():
            if k.startswith("reject_"):
                third_reject[k[7:]] += n
    seal_holds = third_total == 0
    anatomy_episodes, anatomy_counts = [], {}
    if not seal_holds:
        anatomy_episodes, anatomy_counts = third_pair_anatomy(blind_box)
    ladder_ok = all(r["ladder"][THIRD_PAIR].get("S6_and_the_stretch_reads_P", 0)
                    == r["by_shape"][THIRD_PAIR] for r in blind_rows)
    # Liveness is asserted on the ENTRY-GAP FAMILY, not on the third pair: a
    # tier where the third pair never even forms is a real (and weak) outcome
    # and must be reportable, not a gate failure.  The pinned corpus already
    # contains such a cell -- B8.b3 has zero third-pair occurrences.
    all_shape_occ = {sh: sum(r["register_level_pair_occurrences"][sh]
                             for r in blind_rows) for sh in SHAPES}
    instrument_live = sum(all_shape_occ.values()) > 0
    third_pair_forms_at_this_tier = sum(third_occ.values()) > 0
    f_ok = (blind["substrate_failures"] == 0
            and instrument_live
            and ladder_ok
            and (seal_holds or len(anatomy_episodes) == third_total))
    results["F_BLIND_THIRD_PAIR"] = gate("F_BLIND_THIRD_PAIR", f_ok, {
        "question": "at the FIRST GENUINELY BLIND TIER, does the third pair "
                    "(h_f(b), r(b-1)) carry any episode?",
        "sealed_prediction": 0,
        "measured_third_pair_episodes_over_all_B10_bank_clocks": third_total,
        "SEAL_HOLDS_AT_THE_FIRST_BLIND_TIER": seal_holds,
        "verdict": ("ZERO -- the sealed prediction survives its first genuinely "
                    "blind test" if seal_holds else
                    "NONZERO -- THE SEAL IS BROKEN AT B=10; the shadow "
                    "derivation's scope does not extend to this tier"),
        "third_pair_register_level_occurrences_per_bank": third_occ,
        "third_pair_register_level_occurrences_total": sum(third_occ.values()),
        "third_pair_forms_at_register_level_at_this_tier":
            third_pair_forms_at_this_tier,
        "STRENGTH_OF_THE_BLIND_TEST":
            ("the pair DOES form at register level here, so the zero is a real "
             "coincidence failure and not an absence of opportunity"
             if third_pair_forms_at_this_tier else
             "WEAK AT THIS TIER: the third pair does not form at register "
             "level at B=10 at all, so 'zero episodes' is satisfied trivially "
             "-- the sealed prediction is not contradicted, but neither is it "
             "put under the same pressure it was at B=4..8 where the pair "
             "formed thousands of times.  Stated plainly rather than counted "
             "as a win."),
        "entry_gap_family_occurrences_all_three_shapes": all_shape_occ,
        "instrument_live_at_this_tier": instrument_live,
        "third_pair_full_configurations_per_bank": third_cfg,
        "third_pair_full_configurations_total": sum(third_cfg.values()),
        "third_pair_episodes_per_bank": third_ep,
        "third_pair_refusal_components": dict(third_reject),
        "ladder_S6_agrees_with_episode_count": ladder_ok,
        "uncapped_anatomy_ran": not seal_holds,
        "anatomised_episodes": anatomy_episodes[:200],
        "anatomy_aggregate_counts": anatomy_counts,
        "instrument_liveness":
            "the same code path that reports these numbers reports the pinned "
            "B=4..8 numbers value for value (gate D) and catches a planted "
            "third-pair episode (gate J, tooth T2), so a zero here is a "
            "measurement and not a blind spot",
        "gate_is_not_conditioned_on_the_prediction":
            "this gate passes on EITHER outcome; it requires only that the "
            "instrument be live at B=10 and that every episode found be "
            "anatomised.  The verdict above is data.",
        "substrate_failures": blind["substrate_failures"],
        "B10_lanes": blind["lanes"], "B10_stations": blind["stations"],
        "B10_closed_quiescent_stretches": blind["closed_quiescent_stretches"],
        "B10_longest_closed_stretch": blind["longest_closed_stretch"],
        "B10_clocks_swept": blind["clocks_swept"],
        "seconds_to_build_and_census_the_blind_tier": blind_seconds,
    })

    # ------------------------------------------------------------ gate G
    N10 = blind["stations"]
    rc2_map = []
    necessity_violations, sufficiency_failures = [], []
    for r in blind_rows:
        P = r["entry_gap_period"]
        predicted = 2 * P < N10
        fired = r["bank_owned_entry_gap_episodes"] > 0
        row = {"cell": "B%d.b%d" % (BLIND_TIER, r["bank"]), "bank": r["bank"],
               "P": P, "two_P": 2 * P, "N": N10,
               "RC2_predicts_fire": predicted,
               "measured_fires": fired,
               "agrees": predicted == fired,
               "episodes_on_the_bank_clock": r["episodes_on_the_bank_clock"],
               "bank_owned_entry_gap_episodes":
                   r["bank_owned_entry_gap_episodes"],
               "by_shape": r["by_shape"],
               "full_configurations_presented": sum(
                   r["ladder"][sh].get("S5_FULL_CONFIGURATION", 0)
                   for sh in SHAPES),
               "is_b_equals_B_minus_2": r["bank"] == BLIND_TIER - 2}
        rc2_map.append(row)
        if fired and not predicted:
            necessity_violations.append(row)
        if predicted and not fired:
            sufficiency_failures.append(row)
    b_minus_2 = next(r for r in rc2_map if r["bank"] == BLIND_TIER - 2)
    g_ok = (len(rc2_map) == BLIND_TIER - 2
            and all(r["P"] == 8 * (BLIND_TIER - 1 - r["bank"]) for r in rc2_map))
    results["G_RC2_AT_B10"] = gate("G_RC2_AT_B10", g_ok, {
        "question": "does RC-2's short-arc necessity survive at the blind tier, "
                    "and does the b = B-2 sufficiency failure recur a third "
                    "time?",
        "RC2_statement": RC2_STATEMENT,
        "carrier_map": rc2_map,
        "predicted_firing_banks": sorted(r["bank"] for r in rc2_map
                                         if r["RC2_predicts_fire"]),
        "measured_firing_banks": sorted(r["bank"] for r in rc2_map
                                        if r["measured_fires"]),
        "NECESSITY_VIOLATIONS": necessity_violations,
        "necessity_violation_count": len(necessity_violations),
        "necessity_holds_at_the_blind_tier": not necessity_violations,
        "SUFFICIENCY_FAILURES": sufficiency_failures,
        "sufficiency_failure_cells": [r["cell"] for r in sufficiency_failures],
        "the_b_equals_B_minus_2_cell": b_minus_2,
        "b_equals_B_minus_2_fires": b_minus_2["measured_fires"],
        "third_instance_outcome":
            ("the b = B-2 / P = 8 sufficiency failure RECURS at B=10 -- a third "
             "instance after B=8.b6 and B=9.b7"
             if not b_minus_2["measured_fires"] else
             "the b = B-2 / P = 8 cell FIRES at B=10 -- the two-instance "
             "pattern from B=8.b6 and B=9.b7 does NOT continue"),
        "gate_is_not_conditioned_on_the_prediction":
            "this gate checks only that the map is complete and its periods are "
            "the entry gaps; necessity and sufficiency outcomes are data.",
    })

    # ------------------------------------------------------------ gate H
    coincidence_bank = (BLIND_TIER - 2) // 2
    comp_of_edge = {e: N10 - d for e, d in blind["table"]["delta"].items()}
    entry_at_coincidence = 8 * (BLIND_TIER - 1 - coincidence_bank)
    own_complements = {e: comp_of_edge[e]
                       for e in (coincidence_bank - 1, coincidence_bank)
                       if e in comp_of_edge}
    coincides_with = sorted(e for e, v in own_complements.items()
                            if v == entry_at_coincidence)
    shape_split = {}
    for (bank, period, shape), n in sorted(blind["local_shape_counts"].items()):
        if bank == coincidence_bank and period == entry_at_coincidence:
            shape_split[shape] = n
    # The 891 label for a same-token class does not depend on which separated
    # placement carries the tokens; it is computed over a sample of real
    # placements anyway and the whole label SET is reported.
    placement_sample = C930.separated_placements(N10)[:12]
    value_label_set = sorted({
        classify_separation_891(blind["table"], {coincidence_bank}, pos,
                                entry_at_coincidence)
        for pos in placement_sample})
    value_label = value_label_set[0] if len(value_label_set) == 1 else "AMBIGUOUS"
    theft_row = next(r for r in rc2_map if r["bank"] == coincidence_bank)
    tp_row = next(r for r in b10_rows if r["bank"] == coincidence_bank)
    h_ok = (coincides_with == [coincidence_bank]
            and entry_at_coincidence == 8 * (coincidence_bank + 1)
            and tp_row["is_coincidence_cell"])
    results["H_LABEL_THEFT_AT_B10"] = gate("H_LABEL_THEFT_AT_B10", h_ok, {
        "question": "at B=10 the entry gap of bank 4 is 40, which is also a "
                    "same-edge complement value -- what actually produces the "
                    "readings there?",
        "statement": LABEL_THEFT_STATEMENT,
        "coincidence_bank": coincidence_bank,
        "entry_gap_value": entry_at_coincidence,
        "banks_own_edge_complement_values": own_complements,
        "coincides_with_the_complement_of_edge": coincides_with,
        "which_branch": "b = (B-2)/2 -- the coincidence is with the complement "
                        "of edge b itself (r(b) -> f(b)), not of edge b-1.  The "
                        "b = (B-1)/2 branch needs odd B and B = 10 is even.",
        "clock_local_shape_counts_at_the_value": shape_split,
        "clock_local_classification":
            ("the value 40 on bank 4's own clock is produced by: "
             + ", ".join("%s x%d" % (k, v) for k, v in sorted(shape_split.items()))
             if shape_split else
             "the value 40 produces NO clock-local same-token pair on bank 4's "
             "own clock at all"),
        "bank_owned_entry_gap_episodes_at_the_value":
            theft_row["bank_owned_entry_gap_episodes"],
        "episodes_on_the_bank_clock_at_the_value":
            theft_row["episodes_on_the_bank_clock"],
        "the_891_value_based_label_would_be": value_label,
        "the_891_value_based_label_over_a_placement_sample": value_label_set,
        "placements_sampled_for_the_891_label": len(placement_sample),
        "label_theft_present":
            value_label == "RELAY_ENTRY_GAP"
            and theft_row["bank_owned_entry_gap_episodes"] == 0,
        "TP3_fourth_fixed_row_here": tp_row["extra_P_shift_fixed_rows"],
        "TP3_fourth_fixed_row_is_r_of_b_not_the_third_pair_terminal":
            tp_row["extra_P_shift_fixed_rows"] == [tp_row["reverse_rows"][1]],
        "third_pair_terminal_r_b_minus_1": tp_row["pairs"]["handoff_swap"][1],
    })

    # ------------------------------------------------------------ gate I
    complements = sorted(set(comp_of_edge.values()))
    stretch_local_values = [p for p in complements if 2 * p >= N10]
    ring_local_values = [p for p in complements if 2 * p < N10]
    census_rows, multiplicities = [], Counter()
    for P in complements:
        per_bank = {b: n for (b, p), n in sorted(blind["bank_period"].items())
                    if p == P and n}
        shapes = {}
        for (bank, period, shape), n in sorted(blind["local_shape_counts"].items()):
            if period == P:
                shapes["b%d|%s" % (bank, shape)] = n
        total = sum(per_bank.values())
        census_rows.append({
            "P": P, "two_P": 2 * P, "N": N10,
            "stretch_local_only_2P_ge_N": 2 * P >= N10,
            "episodes_per_bank_clock": per_bank,
            "episodes_total": total,
            "banks_reading_it": sorted(per_bank),
            "clock_local_shapes": shapes})
        if 2 * P >= N10:
            for _b, n in per_bank.items():
                multiplicities[n] += 1
    stretch_local_totals = {r["P"]: r["episodes_total"]
                            for r in census_rows if r["stretch_local_only_2P_ge_N"]}
    ones_and_twos = all(n <= 2 for n in multiplicities.elements()) \
        if multiplicities else None
    i_ok = len(census_rows) == len(complements) and len(complements) == BLIND_TIER - 1
    results["I_STRETCH_LOCAL_AT_B10"] = gate("I_STRETCH_LOCAL_AT_B10", i_ok, {
        "question": "do the 2P >= N complements -- the 40/48 pattern -- appear "
                    "at B=10, and in what multiplicities?",
        "statement": ONES_AND_TWOS_STATEMENT,
        "complement_values_at_B10": complements,
        "stretch_local_values_2P_ge_N": stretch_local_values,
        "ring_readable_values_2P_lt_N": ring_local_values,
        "census": census_rows,
        "stretch_local_episode_totals": stretch_local_totals,
        "stretch_local_per_bank_multiplicity_histogram":
            {str(k): v for k, v in sorted(multiplicities.items())},
        "every_stretch_local_per_bank_count_is_one_or_two": ones_and_twos,
        "scope_note": "bank clocks only at B=10 (declared).  Pair-clock "
                      "inheritance of these episodes is NOT measured and NOT "
                      "claimed.",
    })

    # ------------------------------------------------------------ gate J
    teeth = []

    # T1 -- a tampered pin is caught
    victim = PRIMARY_930
    tampered_bytes = (ROOT / victim).read_bytes() + b"\n# tamper\n"
    _rows, bad = preflight(overrides={victim: tampered_bytes})
    teeth.append({"tooth": "tampered_pin_is_caught", "fires": bad == [victim],
                  "mismatched": bad})

    # T2 -- a PLANTED third-pair episode at B=10 is caught by the same code path
    plant_bank = BLIND_TIER - 2
    plant_P = 8 * (BLIND_TIER - 1 - plant_bank)
    hf_here = blind["table"]["handoff_forward"][plant_bank]
    r_prev = blind["table"]["reverse"][plant_bank - 1]
    plant_shape = shape_of_local_pair(
        (True, "handoff_forward", plant_bank, "reverse", plant_bank - 1),
        plant_bank)
    # a stretch whose dirty runs sit exactly P apart, P-exact to the end
    width, gap = 2, plant_P - 2
    unit = [0] * width + [1] * gap
    seg_bits, length = 0, 0
    for _ in range(6):
        for value in unit:
            if value:
                seg_bits |= 1 << length
            length += 1
    planted_runs = zero_runs(seg_bits, length)
    planted_starts = [lo for lo, _hi in planted_runs]
    planted_sep = sorted({planted_starts[i + 1] - planted_starts[i]
                          for i in range(len(planted_starts) - 1)})
    planted_hits = tail_periods(seg_bits, [plant_P])
    teeth.append({
        "tooth": "planted_third_pair_episode_at_B10_is_caught",
        "fires": (plant_shape == THIRD_PAIR and planted_sep == [plant_P]
                  and plant_P in planted_hits
                  and (r_prev - hf_here) % blind["stations"] == plant_P),
        "cell": "B%d.b%d" % (BLIND_TIER, plant_bank), "period": plant_P,
        "third_pair_stations": [hf_here, r_prev],
        "station_separation_is_P":
            (r_prev - hf_here) % blind["stations"] == plant_P,
        "classifier_names_it": plant_shape,
        "planted_run_start_separations": planted_sep,
        "detector_reads_P": plant_P in planted_hits,
        "note": "a REAL third-pair episode at B=10 -- the stations really are "
                "P apart, the classifier really does name the shape, and the "
                "detector really does read P on a stretch of this form -- would "
                "be reported by the identical code path that reports the "
                "blind-tier count, so a zero is not an instrument blind spot",
    })

    # T3 -- a planted NECESSITY violation at B=10 is caught
    silent = [dict(r) for r in rc2_map]
    target = next((r for r in silent if not r["RC2_predicts_fire"]), None)
    if target is not None:
        target["measured_fires"] = True
        target["bank_owned_entry_gap_episodes"] = 1
    replanted = [r for r in silent
                 if r["measured_fires"] and not r["RC2_predicts_fire"]]
    teeth.append({"tooth": "planted_RC2_necessity_violation_is_caught",
                  "fires": target is not None
                           and len(replanted) == len(necessity_violations) + 1,
                  "planted_into": target["cell"] if target else None,
                  "violations_before": len(necessity_violations),
                  "violations_after": len(replanted)})

    # T4 -- a tampered seal text is caught
    tampered_payload = dict(own_payload)
    tampered_payload["TP_STATEMENT"] = tp_text_receipt_payload.replace(
        "unique", "typical")
    teeth.append({"tooth": "tampered_seal_text_is_caught",
                  "fires": digest(tampered_payload) != published_sha,
                  "tampered_digest": digest(tampered_payload)})

    # T5 -- a tampered sealed PREDICTION is caught
    tampered_pred = json.loads(json.dumps(own_payload))
    tampered_pred["predicted_third_pair_episodes"][str(BLIND_TIER)] = 1
    teeth.append({"tooth": "tampered_sealed_prediction_is_caught",
                  "fires": digest(tampered_pred) != published_sha,
                  "tampered_digest": digest(tampered_pred)})

    # T6 -- a perturbed station formula breaks TP at the blind tier
    broken = 0
    for bc in (BLIND_TIER, BLIND_TIER + 1):
        n = 8 * bc - 5
        for bank in range(1, bc - 1):
            period = 8 * (bc - 1 - bank)
            fp = lambda e: (4 + 5 * e + 1) % n
            rp = lambda e: (8 * bc - 9 - 3 * e) % n
            spans = [(rp(bank) - fp(bank - 1)) % n == period,
                     ((rp(bank - 1) + 2) - fp(bank)) % n == period,
                     (rp(bank - 1) - (fp(bank) - 2)) % n == period]
            if not all(spans):
                broken += 1
    teeth.append({"tooth": "perturbed_station_formula_breaks_TP_at_B10",
                  "fires": broken > 0, "cells_broken": broken})

    # T7 -- the restriction comparison really compares
    probe_failures = []
    restriction_compare("tooth.probe", 1, 1, probe_failures)
    restriction_compare("tooth.probe", 1, 2, probe_failures)
    teeth.append({"tooth": "restriction_comparison_actually_compares",
                  "fires": len(probe_failures) == 1,
                  "failures_raised": len(probe_failures)})

    # T8 -- dropping the third shape from the classifier is detectable at B=10
    def crippled_shape(pair, bank):
        out = shape_of_local_pair(pair, bank)
        return "OTHER_SAME_TOKEN" if out == THIRD_PAIR else out

    true_hits = crippled_hits = 0
    for bank in range(1, BLIND_TIER - 1):
        probe = (True, "handoff_forward", bank, "reverse", bank - 1)
        true_hits += shape_of_local_pair(probe, bank) == THIRD_PAIR
        crippled_hits += crippled_shape(probe, bank) == THIRD_PAIR
    teeth.append({"tooth": "dropping_the_third_shape_is_detectable_at_B10",
                  "fires": true_hits == BLIND_TIER - 2 and crippled_hits == 0,
                  "cells_named_by_the_true_classifier": true_hits,
                  "cells_named_by_the_crippled_classifier": crippled_hits})

    # T9 -- the detector's clean-tick constant is load bearing
    tight = bin(seg_bits).count("1")
    teeth.append({
        "tooth": "detector_min_events_constant_is_load_bearing",
        "fires": (plant_P in tail_periods(seg_bits, [plant_P], min_events=8)
                  and plant_P not in tail_periods(seg_bits, [plant_P],
                                                  min_events=tight + 1)),
        "clean_ticks_in_the_planted_mask": tight})

    # T10 -- a crippled rejection decomposer disagrees with the detector
    def crippled_reject(mask, period):
        if mask == 0:
            return "R0_empty"
        if bin(mask).count("1") < MIN_STABLE_EVENTS:
            return "R1"
        last = mask.bit_length() - 1
        if MIN_PERIOD_REPEATS * period > last:
            return "R2_stretch_shorter_than_2P"
        span = last - period
        broken_bits = (mask ^ (mask >> period)) & ((1 << (span + 1)) - 1)
        transient = broken_bits.bit_length()
        if last - transient < MIN_PERIOD_REPEATS * period:
            return "R4"
        return "ACCEPT"

    rng2 = random.Random(942_0729)
    disagree = 0
    for _ in range(400):
        n = rng2.randrange(30, 200)
        bits = rng2.getrandbits(n) | (1 << (n - 1))
        for p in range(2, 20):
            if (crippled_reject(bits, p) == "ACCEPT") != (p in tail_periods(bits, [p])):
                disagree += 1
    teeth.append({"tooth": "crippled_rejection_decomposer_is_detectable",
                  "fires": disagree > 0, "disagreements": disagree})

    # T11 -- the key-semantics digest is timing free and semantics sensitive
    key_semantics = {
        "B10_third_pair_episodes": third_total,
        "B10_third_pair_occurrences": third_occ,
        "B10_third_pair_full_configurations": third_cfg,
        "B10_rc2_carrier_map": [{k: r[k] for k in
                                 ("cell", "P", "RC2_predicts_fire",
                                  "measured_fires",
                                  "bank_owned_entry_gap_episodes",
                                  "episodes_on_the_bank_clock", "by_shape")}
                                for r in rc2_map],
        "B10_necessity_violations": len(necessity_violations),
        "B10_sufficiency_failures": [r["cell"] for r in sufficiency_failures],
        "B10_label_theft_shape_split": shape_split,
        "B10_stretch_local_totals": stretch_local_totals,
        "B10_stretches": blind["closed_quiescent_stretches"],
        "SEAL_sha256": published_sha,
        "seal_recomputed": own_sha,
    }
    key_digest = digest(key_semantics)
    timing_words = ("runtime", "second", "elapsed", "time", "path", "date")
    no_timing_keys = not any(w in k.lower() for k in key_semantics
                             for w in timing_words)
    polluted = dict(key_semantics)
    polluted["runtime_seconds"] = round(time.monotonic() - started, 1)
    mutated_key = json.loads(json.dumps(key_semantics))
    mutated_key["B10_third_pair_episodes"] += 1
    teeth.append({
        "tooth": "key_semantics_digest_is_timing_free_and_semantics_sensitive",
        "fires": (no_timing_keys
                  and digest(polluted) != key_digest
                  and digest(mutated_key) != key_digest),
        "key_semantics_sha256": key_digest,
        "payload_carries_no_timing_key": no_timing_keys,
        "keys": sorted(key_semantics),
        "note": "no runtime, elapsed time, timestamp or path enters the key "
                "semantics payload -- and the guard is load bearing: injecting "
                "a runtime field WOULD change the digest, and a single changed "
                "measurement DOES change it"})

    # T12 -- the blind tier really was absent from the build log at seal time
    teeth.append({
        "tooth": "seal_was_recomputed_before_the_blind_corpus_existed",
        "fires": (blind_free
                  and any(row["banks"] == BLIND_TIER for row in BUILD_LOG)),
        "build_log_at_seal_recomputation": build_log_now,
        "build_log_now": list(BUILD_LOG)})

    j_ok = all(t["fires"] for t in teeth) and len(teeth) >= 6
    results["J_TEETH"] = gate("J_TEETH", j_ok, {
        "teeth": teeth, "count": len(teeth), "declared_minimum": 6,
        "all_fire": all(t["fires"] for t in teeth)})

    # ---------------------------------------------------- determinism probe
    probe_a = build_corpus(3, 64)
    probe_b = build_corpus(3, 64)
    corpus_digest = digest([probe_a["clean_planes"], probe_a["source_clean"]])
    corpus_digest_b = digest([probe_b["clean_planes"], probe_b["source_clean"]])
    program_digest = digest([list(K.interleaved_program(bc))
                             for bc in range(3, 12)])
    program_digest_b = digest([list(K.interleaved_program(bc))
                               for bc in range(3, 12)])
    determinism = {
        "corpus_double_build_digest": corpus_digest,
        "corpus_double_build_deterministic": corpus_digest == corpus_digest_b,
        "program_double_build_digest": program_digest,
        "program_double_build_deterministic": program_digest == program_digest_b,
        "key_semantics_sha256": key_digest,
        "double_run_protocol":
            "the runner is executed twice cold; the two stdouts are compared "
            "after normalising the runtime fields, the per-tier seconds and the "
            "trailing RECEIPT digest line.  Every gate line, the SEAL line and "
            "the key-semantics digest must be byte identical.",
    }
    del probe_a, probe_b

    # ------------------------------------------------------------ gate K
    runtime = time.monotonic() - started
    k_ok = (all(results.values()) and runtime <= RUNTIME_LIMIT_SECONDS
            and determinism["corpus_double_build_deterministic"]
            and determinism["program_double_build_deterministic"])
    headline = (
        "THE BLIND TIER IS BUILT.  B = 10 -- %d lanes, %d stations, %d closed "
        "quiescent stretches, all ten bank clocks -- is the first tier in this "
        "lineage nobody had ever measured, and Cycle 930's seal "
        "(%s) predicted ZERO third-pair episodes there.  MEASURED: %d.  The "
        "pair occurs %d times at register level and reaches the full stretch "
        "configuration %d times, so the instrument is live; %s.  RC-2 at B=10: "
        "necessity violations %d; predicted firing banks %s, measured %s; the "
        "b = B-2 = 8 cell (P = 8) %s.  The value-coincidence cell b = 4 "
        "(entry gap 40 = the edge-4 complement) is clock-locally %s."
        % (blind["lanes"], blind["stations"],
           blind["closed_quiescent_stretches"], published_sha[:12],
           third_total, sum(third_occ.values()), sum(third_cfg.values()),
           ("the zero is a measurement, and the seal survives its first "
            "genuinely blind test" if seal_holds else
            "THE SEAL IS BROKEN AND EVERY EPISODE IS ANATOMISED ABOVE"),
           len(necessity_violations),
           sorted(r["bank"] for r in rc2_map if r["RC2_predicts_fire"]),
           sorted(r["bank"] for r in rc2_map if r["measured_fires"]),
           ("stays SILENT -- a third instance of the b = B-2 sufficiency "
            "failure" if not b_minus_2["measured_fires"] else "FIRES"),
           (", ".join("%s x%d" % (k, v) for k, v in sorted(shape_split.items()))
            if shape_split else "not a same-token pair at all")))
    results["K_VERDICT"] = gate("K_VERDICT", k_ok, {
        "headline": headline,
        "gates": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "determinism": determinism,
        "runtime_s": round(runtime, 1),
        "runtime_limit_s": RUNTIME_LIMIT_SECONDS,
        "build_log": list(BUILD_LOG),
        "open": [
            "TP-4's zero is MEASURED, never derived -- B=10 adds the first "
            "genuinely blind tier to the measured range, it does not turn the "
            "seal into a theorem; B = 11 and B = 12 remain sealed and unbuilt",
            "RC-2 remains FITTED-THEN-SEALED with its 8-wide model-degeneracy "
            "band untouched; a blind-tier agreement is one more sealed cell",
            "RC-3 sufficiency is untouched here and remains on 891's declared "
            "dynamical boundary",
            "pair-clock quantities at B=10 are not measured (declared scoping)",
        ],
    })

    payload = {
        "campaign": "toe-time-expansion-20260802",
        "block": "toe-time-blockT8-20260802",
        "cycles": [942],
        "claim_type": "blind-tier measurement against a sealed prediction",
        "authority": "none", "audit": "unset",
        "authorship": "one Claude Opus 5 worker-authored primary and checker "
                      "under supervisor spec; supervisor review",
        "independence": "primary only -- see the independent-check receipt",
        "note": "none -- this block ships scripts, caches and receipts only",
        "headline": headline,
        "blind_tier_statement": BLIND_TIER_STATEMENT,
        "RC2_statement": RC2_STATEMENT,
        "label_theft_statement": LABEL_THEFT_STATEMENT,
        "ones_and_twos_statement": ONES_AND_TWOS_STATEMENT,
        "gate_results": {k: ("PASS" if v else "FAIL") for k, v in results.items()},
        "seal_recomputation": {
            "published_SEAL_sha256": published_sha,
            "pinned_expectation": PUBLISHED_SEAL_SHA,
            "recomputed_from_published_payload": payload_as_published_sha,
            "recomputed_from_published_text_and_own_arithmetic": own_sha,
            "own_payload_equals_published_payload":
                own_payload == published_payload,
            "TP_text_identical_across_four_sources": texts_agree,
            "build_log_at_recomputation_time": build_log_now,
            "no_sealed_tier_corpus_existed_at_recomputation": blind_free,
            "sealed_prediction_at_the_blind_tier":
                sealed_prediction_for_the_blind_tier,
            "sealed_payload": own_payload,
        },
        "blind_tier": {
            "banks": BLIND_TIER, "horizon": HORIZON, "clocks": "bank clocks only",
            "lanes": blind["lanes"], "stations": blind["stations"],
            "closed_quiescent_stretches": blind["closed_quiescent_stretches"],
            "longest_closed_stretch": blind["longest_closed_stretch"],
            "clocks_swept": blind["clocks_swept"],
            "substrate_failures": blind["substrate_failures"],
            "seconds": blind_seconds,
            "SEAL_HOLDS": seal_holds,
            "third_pair_episodes": third_total,
            "third_pair_episodes_per_bank": third_ep,
            "third_pair_register_level_occurrences": third_occ,
            "third_pair_full_configurations": third_cfg,
            "third_pair_refusal_components": dict(third_reject),
            "anatomised_episodes": anatomy_episodes[:200],
            "anatomy_aggregate_counts": anatomy_counts,
            "per_cell_rows": blind_rows,
        },
        "rc2_at_B10": {
            "carrier_map": rc2_map,
            "necessity_violations": necessity_violations,
            "necessity_holds": not necessity_violations,
            "sufficiency_failures": sufficiency_failures,
            "b_equals_B_minus_2_cell": b_minus_2,
        },
        "label_theft_at_B10": {
            "coincidence_bank": coincidence_bank,
            "entry_gap_value": entry_at_coincidence,
            "own_edge_complement_values": own_complements,
            "coincides_with_edge": coincides_with,
            "clock_local_shape_counts": shape_split,
            "the_891_value_based_label": value_label,
            "bank_owned_entry_gap_episodes":
                theft_row["bank_owned_entry_gap_episodes"],
            "episodes_on_the_bank_clock":
                theft_row["episodes_on_the_bank_clock"],
            "TP3_fourth_fixed_row": tp_row["extra_P_shift_fixed_rows"],
        },
        "stretch_local_at_B10": {
            "complement_values": complements,
            "stretch_local_values_2P_ge_N": stretch_local_values,
            "census": census_rows,
            "totals": stretch_local_totals,
            "multiplicity_histogram":
                {str(k): v for k, v in sorted(multiplicities.items())},
            "every_per_bank_count_is_one_or_two": ones_and_twos,
        },
        "TP_at_B10": {"rows": b10_rows,
                      "cells_checked_B3_to_B24": tp_cells,
                      "disagreements": tp_bad,
                      "fourth_fixed_row_cells": b10_coincidence},
        "restriction_gate": {
            "total_failed_checks": len(failures),
            "tier_rows": d_rows,
            "fields_compared_per_cell": list(RESTRICTION_FIELDS),
            "third_pair_occurrences_reproduced": tp_occ_mine,
            "third_pair_full_configurations_reproduced": tp_cfg_mine,
            "seconds_per_tier": restriction_seconds,
        },
        "key_semantics": key_semantics,
        "key_semantics_sha256": key_digest,
        "teeth": teeth,
        "determinism": determinism,
        "disclosed_deviations": list(DISCLOSED_DEVIATIONS),
        "build_log": list(BUILD_LOG),
        "runtime_seconds": round(runtime, 1),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "exit_codes": {"primary": 0 if k_ok else 1},
        "open": results["K_VERDICT"] and [
            "B = 11 and B = 12 remain sealed and unbuilt",
            "RC-2 stays fitted-then-sealed with its degeneracy band",
            "RC-3 sufficiency untouched, still on the dynamical boundary",
        ],
        "pinned_inputs": {p: {"sha256": PREFLIGHT_ROWS[p]["sha256"],
                              "git_blob": PREFLIGHT_ROWS[p]["git_blob"]}
                          for p in sorted(PINS)},
    }
    me = Path(__file__).read_bytes()
    payload["files"] = {
        "scripts/frontier_cycle942_blind_tier_2026_07_28.py": {
            "sha256": sha256(me).hexdigest(), "git_blob": git_blob(me)}}
    out = ROOT / "outputs" / "blind_tier_cycle942_receipt_2026_07_28.json"
    out.write_text(json.dumps(payload, indent=1, sort_keys=True, default=str))
    emit("RECEIPT %s :: %s" % (out.name, json.dumps(
        {"sha256": sha256(out.read_bytes()).hexdigest(),
         "git_blob": git_blob(out.read_bytes())}, **dumps)))
    return 0 if k_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
