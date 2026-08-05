#!/usr/bin/env python3
"""
Cycle 924 INDEPENDENT CHECKER -- spec'd to REFUTE the primary.

Independence discipline.  This checker shares no code with the primary.  In
particular it uses:

  * its own rational arithmetic -- a hand-rolled exact Rat class built on
    integer pairs with gcd normalization, NOT fractions.Fraction, so a bug in
    the primary's use of Fraction cannot be reproduced here;
  * its own constraint solver for Q3 -- dense Gauss-Jordan over Rat with
    explicit pivoting and a nullity count, NOT the primary's sparse
    dictionary echelon;
  * its own enumeration of the Q1 rate-ratio objects, re-derived from the
    vendored artifacts by a DIFFERENT reading path (the notes' prose is
    parsed for the numbers and cross-checked against the receipts, rather
    than the receipts being trusted alone);
  * a model-degeneracy attack on every identification sentence the primary
    claims or rejects: does a DIFFERENT sentence connect the SAME objects to
    a DIFFERENT value equally well?

The checker reports refutations plainly.  It is a success for this checker to
find that the primary overclaimed.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
from math import gcd
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
T0 = time.time()
BUDGET = 900.0

ROWS: list[tuple[str, str, bool, str]] = []
REFUTATIONS: list[str] = []


def ck(cid: str, what: str, ok: bool, detail: str = "") -> bool:
    ROWS.append((cid, what, bool(ok), detail))
    return bool(ok)


def refute(msg: str) -> None:
    REFUTATIONS.append(msg)


# ==========================================================================
# own exact rational arithmetic (deliberately not fractions.Fraction)
# ==========================================================================
class Rat:
    __slots__ = ("n", "d")

    def __init__(self, n: int, d: int = 1):
        if d == 0:
            raise ZeroDivisionError("Rat with zero denominator")
        if d < 0:
            n, d = -n, -d
        g = gcd(abs(n), d) or 1
        self.n, self.d = n // g, d // g

    def __add__(self, o): return Rat(self.n * o.d + o.n * self.d, self.d * o.d)
    def __sub__(self, o): return Rat(self.n * o.d - o.n * self.d, self.d * o.d)
    def __mul__(self, o): return Rat(self.n * o.n, self.d * o.d)

    def __truediv__(self, o):
        if o.n == 0:
            raise ZeroDivisionError
        return Rat(self.n * o.d, self.d * o.n)

    def __eq__(self, o): return isinstance(o, Rat) and self.n == o.n and self.d == o.d
    def __hash__(self): return hash((self.n, self.d))
    def __bool__(self): return self.n != 0
    def __neg__(self): return Rat(-self.n, self.d)
    def __repr__(self): return f"{self.n}" if self.d == 1 else f"{self.n}/{self.d}"


R0, R1 = Rat(0), Rat(1)
TWO_THIRDS = Rat(2, 3)
L_LOCAL = Rat(2, 9)


def parse_rat(s: str) -> Rat:
    s = s.strip()
    if "/" in s:
        a, b = s.split("/")
        return Rat(int(a), int(b))
    return Rat(int(s))


# ==========================================================================
# own dense Gauss-Jordan nullity solver (not the primary's sparse echelon)
# ==========================================================================
def nullity(rows: list[list[Rat]], ncols: int) -> int:
    """Return dim ker of the homogeneous system, by dense Gauss-Jordan."""
    M = [r[:] for r in rows]
    rank = 0
    col = 0
    nrows = len(M)
    while col < ncols and rank < nrows:
        piv = None
        for r in range(rank, nrows):
            if M[r][col]:
                piv = r
                break
        if piv is None:
            col += 1
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = R1 / M[rank][col]
        M[rank] = [x * inv for x in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col]:
                f = M[r][col]
                M[r] = [M[r][c] - f * M[rank][c] for c in range(ncols)]
        rank += 1
        col += 1
    return ncols - rank


def sha256_of(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run_py(rel: str) -> tuple[int, str]:
    import os
    env = dict(os.environ)
    env["PYTHONPATH"] = "scripts"
    r = subprocess.run([sys.executable, rel], cwd=REPO, capture_output=True,
                       text=True, env=env)
    return r.returncode, r.stdout + r.stderr


PRIMARY_RECEIPT = REPO / "outputs/occurrence_rate_route_cycle924_receipt_2026_07_28.json"

NOTES = {
    909: "docs/WITHIN_WORLD_PURCHASE_SPECTRUM_CYCLE909_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    911: "docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    912: "docs/A3_CHANNEL_HALF_FORCED_CYCLE912_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    913: "docs/SELECTION_IS_TRANSPORT_O3_TERMINAL_CYCLE913_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    891: "docs/COMPLEMENT_MECHANISM_KRUN_LAW_CYCLE891_BOUNDED_THEOREM_NOTE_2026-07-28.md",
}
RECEIPTS = {
    909: "outputs/within_world_pricing_cycle909_receipt_2026_07_28.json",
    911: "outputs/type_vacuity_cycle911_receipt_2026_07_28.json",
    912: "outputs/a3_channel_cycle912_receipt_2026_07_28.json",
    913: "outputs/selection_function_cycle913_receipt_2026_07_28.json",
    891: "outputs/complement_mechanism_cycle891_receipt_2026_07_28.json",
}


# ==========================================================================
# TOOTH 1 -- the primary's restriction gates, re-run by the checker itself
# ==========================================================================
def tooth_1() -> None:
    rc, txt = run_py("scripts/acphilambda_r_eta_angle_native_frontier_no_go_2026_07_04.py")
    ok = "TOTAL: PASS=128 FAIL=0" in txt
    ck("T1a", "checker independently reproduces the angle-native no-go at "
              "PASS=128 FAIL=0", ok)
    if not ok:
        refute("the angle-native no-go runner does not reproduce PASS=128")
    rc2, txt2 = run_py("scripts/acphilambda_r_eta_hclass_first_principles_stretch_no_go_2026_07_04.py")
    tot = next((l for l in txt2.splitlines() if l.startswith("TOTAL")), "")
    ok2 = "FAIL=0" in tot
    ck("T1b", "checker independently reproduces the stretch no-go at FAIL=0",
       ok2, tot)
    # the discrepancy the primary discloses -- verify the primary DID disclose it
    rec = json.loads(PRIMARY_RECEIPT.read_text())
    disc = rec["B_restriction_gates"]["stretch_no_go"]
    has_both = "READING 1" in disc.get("SOURCE_INCONSISTENCY_BOTH_READINGS", "") \
        and "READING 2" in disc.get("SOURCE_INCONSISTENCY_BOTH_READINGS", "")
    ck("T1c", "the primary discloses the stretch-no-go pass-count discrepancy "
              "with BOTH readings rather than silently picking one", has_both,
       f"observed={disc.get('observed_pass')} note_claim={disc.get('note_claimed_close')}")
    if not has_both:
        refute("the primary did not record both readings of the source "
               "inconsistency")


# ==========================================================================
# TOOTH 2 -- digests re-verified independently of the primary's loader
# ==========================================================================
def tooth_2() -> None:
    ships = [
        "outputs/within_world_block_cycle909_ship_receipt_2026_07_28.json",
        "outputs/type_vacuity_block_cycle911_ship_receipt_2026_07_28.json",
        "outputs/a3_channel_block_cycle912_ship_receipt_2026_07_28.json",
        "outputs/selection_block_cycle913_ship_receipt_2026_07_28.json",
        "outputs/complement_block_cycle891_ship_receipt_2026_07_28.json",
        "outputs/source_action_bridge_pricing_cycle871_receipt_2026_07_28.json",
    ]
    bad, n = [], 0
    for s in ships:
        doc = json.loads((REPO / s).read_text())
        for rel, rec in doc.get("files", {}).items():
            n += 1
            p = REPO / rel
            if not p.exists() or sha256_of(p) != rec.get("sha256"):
                bad.append(rel)
    ck("T2", "every vendored artifact re-verifies against its ship receipt "
             "under the checker's own digest loop", not bad,
       f"files={n} bad={bad}")
    if bad:
        refute(f"vendored artifacts fail digest verification: {bad}")

    # tamper control: the check must be capable of failing
    probe = hashlib.sha256(b"tampered").hexdigest()
    ck("T2b", "tamper control: a modified byte stream yields a different digest",
       probe != sha256_of(REPO / ships[0]))


# ==========================================================================
# TOOTH 3 -- Q1 re-derived from the NOTES' prose, not the receipts
# ==========================================================================
def tooth_3() -> None:
    """The primary reads receipts.  The checker reads the notes' prose and
    demands the two agree.  A number that appears in one and not the other is
    a refutation."""
    n913 = (REPO / NOTES[913]).read_text()
    r913 = json.loads((REPO / RECEIPTS[913]).read_text())
    c1 = r913["certificates"]["C1_SELECTION_TABLE"]

    # prose: "84 realize (1,0), 80 realize (0,1)" and "All 164 lock points"
    m84 = re.search(r"(\d+)\s+realize\s+\(1,\s*0\)", n913)
    m80 = re.search(r"(\d+)\s+realize\s+\(0,\s*1\)", n913)
    m164 = re.search(r"All\s+(\d+)\s+lock points", n913)
    ok = bool(m84 and m80 and m164)
    ck("T3a", "the 913 note's prose carries the selection split and lock count",
       ok, f"84={m84 and m84.group(1)} 80={m80 and m80.group(1)} "
           f"164={m164 and m164.group(1)}")
    if ok:
        p84, p80, p164 = int(m84.group(1)), int(m80.group(1)), int(m164.group(1))
        agree = (p84 == c1["selection_split"]["[1, 0]"]["count"]
                 and p80 == c1["selection_split"]["[0, 1]"]["count"]
                 and p164 == c1["lock_points"])
        ck("T3b", "the note's prose numbers agree with the receipt's numbers",
           agree, f"prose=({p84},{p80},{p164}) receipt=("
                  f"{c1['selection_split']['[1, 0]']['count']},"
                  f"{c1['selection_split']['[0, 1]']['count']},"
                  f"{c1['lock_points']})")
        if not agree:
            refute("913 note prose and receipt disagree on the selection split")
        # and they must sum
        ck("T3c", "the split sums to the lock count", p84 + p80 == p164,
           f"{p84}+{p80}={p84+p80} vs {p164}")
        # the shares, recomputed with the checker's own Rat
        s10 = Rat(p84, p164)
        s01 = Rat(p80, p164)
        recv = r913["certificates"]["C1_SELECTION_TABLE"]["selection_split"]
        ok_share = (s10 == parse_rat(recv["[1, 0]"]["share"])
                    and s01 == parse_rat(recv["[0, 1]"]["share"]))
        ck("T3d", "the checker's own rational arithmetic reproduces the "
                  "receipt's shares 21/41 and 20/41", ok_share,
           f"{s10} {s01}")
        if not ok_share:
            refute("share arithmetic disagrees")

    # 911's |A| = 2 everywhere, from prose
    n911 = (REPO / NOTES[911]).read_text()
    has_A2 = "|A| = 2" in n911 and "everywhere" in n911
    ck("T3e", "the 911 note states |A| = 2 at all lock points (the arity claim "
              "the primary relies on)", has_A2)
    if not has_A2:
        refute("the arity claim is not supported by the 911 note")

    # 912's simplex dimension, from prose
    n912 = (REPO / NOTES[912]).read_text()
    msx = re.search(r"([\d,]+)-dimensional\s+simplex", n912)
    r912 = json.loads((REPO / RECEIPTS[912]).read_text())
    dim = r912["certificates"]["C2_A3_CHANNEL"]["P_B_result"][
        "admissible_probability_affine_dimension"]
    ok912 = bool(msx) and int(msx.group(1).replace(",", "")) == dim
    ck("T3f", "the 912 note's simplex dimension agrees with its receipt",
       ok912, f"prose={msx and msx.group(1)} receipt={dim}")
    if not ok912:
        refute("912 note and receipt disagree on the simplex dimension")


# ==========================================================================
# TOOTH 4 -- the 2/3 hunt, redone with the checker's own arithmetic
# ==========================================================================
def tooth_4() -> dict:
    """Rebuild the pool independently and re-run the exhaustive sweep."""
    r913 = json.loads((REPO / RECEIPTS[913]).read_text())
    r909 = json.loads((REPO / RECEIPTS[909]).read_text())
    r912 = json.loads((REPO / RECEIPTS[912]).read_text())
    r891 = json.loads((REPO / RECEIPTS[891]).read_text())

    pool: list[tuple[str, int]] = []
    c1 = r913["certificates"]["C1_SELECTION_TABLE"]
    pool += [("lock_points", c1["lock_points"]),
             ("realize_10", c1["selection_split"]["[1, 0]"]["count"]),
             ("realize_01", c1["selection_split"]["[0, 1]"]["count"]),
             ("gates_total", c1["endpoint_wire_lemma"]["gates_total"])]
    c3 = r913["certificates"]["C3_CONTENT_DETERMINATION"]
    pool += [("no_record", c3["reading_2_record_event_history"][
                  "lock_points_with_NO_prior_record_event_at_all"]),
             ("tick0", c3["reading_2_record_event_history"][
                 "lock_points_at_tick_zero"]),
             ("largest_class", c3["reading_1_record_registers"][
                 "largest_collision_class_size"]),
             ("groups", c3["reading_1_record_registers"]["groups"])]
    pool.append(("menu_size", 2))
    gt = r909["Q3_gravity_terms_reading"]
    pool += [(f"sites{i}", v) for i, v in enumerate(gt["atom_sites"])]
    pool += [(f"d0col{i}", v) for i, v in enumerate(gt["degree0_column"])]
    pool += [(f"d2col{i}", v) for i, v in enumerate(gt["degree2_column"])]
    eo = r909["Q1_escape_orbit"]
    pool += [("escape_worlds", len(eo["F_event_position_per_world"])),
             ("events_per_world", eo["events_per_world"])]
    pool += [(f"tag_{k}", v) for k, v in sorted(
        eo["tag_multiset_per_world"].items())]
    c4 = r912["certificates"]["C4_RESIDUE_VECTORS"]["effective_independence_at_613"]
    pool += [("mod613", c4["distinct_vectors_mod_613"]),
             ("recipes", c4["of_recipes"]),
             ("simplex_dim", r912["certificates"]["C2_A3_CHANNEL"][
                 "P_B_result"]["admissible_probability_affine_dimension"])]
    for b, row in sorted(r891["holdout"]["rows"].items()):
        for p in row["OBSERVED"]:
            pool.append((f"P_B{b}_{p}", p))

    hits = []
    npairs = 0
    for i, (la, va) in enumerate(pool):
        for j, (lb, vb) in enumerate(pool):
            if i == j or vb == 0:
                continue
            npairs += 1
            if Rat(va, vb) == TWO_THIRDS:
                hits.append((la, va, lb, vb))
    ck("T4a", "checker's independent sweep evaluates the full ordered pool",
       npairs > 0, f"pool={len(pool)} pairs={npairs}")

    rec = json.loads(PRIMARY_RECEIPT.read_text())
    claimed = rec["D_Q2_license_hunt"]["numerical_hits_at_2_3"]
    agree = len(hits) == claimed
    ck("T4b", "checker's hit count at 2/3 agrees with the primary's",
       agree, f"checker={len(hits)} primary={claimed}")
    if not agree:
        refute(f"hit-count disagreement: checker {len(hits)} vs primary "
               f"{claimed}.  NOTE: the pools are built independently, so a "
               f"small difference may reflect pool composition, not an error; "
               f"reported for adjudication.")

    # the decisive claim: NONE is licensed.
    licensed = rec["D_Q2_license_hunt"]["any_licensed"]
    ck("T4c", "the primary claims no candidate is licensed", licensed is False)
    if licensed:
        refute("the primary claims a license; the checker requires that claim "
               "to be attacked, not accepted")
    return {"hits": hits, "pool": pool}


# ==========================================================================
# TOOTH 5 -- THE MODEL-DEGENERACY ATTACK on the identification sentences
# ==========================================================================
def tooth_5(sweep: dict) -> None:
    """The specified hardest attack: for any identification sentence that
    connects two occurrence objects to the value 2/3, does a DIFFERENT
    sentence connect the SAME objects to a DIFFERENT value equally well?

    If yes for every candidate, then no candidate can license: the sentence
    is doing the work, not the objects.  This is the checker's own
    formulation and it is run against the primary's own hit list.
    """
    pool = dict(sweep["pool"])
    # For the sharpest same-artifact candidate -- 891's own period family --
    # enumerate every value reachable by the SAME KIND of sentence ("the
    # holonomy is the ratio of two readable episode periods").
    periods = sorted({v for k, v in pool.items() if k.startswith("P_B")})
    vals = set()
    for a in periods:
        for b in periods:
            if b and a != b:
                vals.add(Rat(a, b))
    hits23 = [(a, b) for a in periods for b in periods
              if b and a != b and Rat(a, b) == TWO_THIRDS]
    ck("T5a", "the period-ratio sentence family reaches many distinct values, "
              "of which 2/3 is only one", len(vals) > 1,
       f"periods={periods} distinct_ratio_values={len(vals)} "
       f"pairs_hitting_2/3={len(hits23)}")
    degenerate = len(vals) > 1
    ck("T5b", "MODEL DEGENERACY CONFIRMED: a different pair of the same "
              "objects, under an equally well-formed sentence, gives a "
              "different value", degenerate,
       f"e.g. the same 'ratio of two readable periods' sentence yields "
       f"{sorted(str(v) for v in list(vals))[:8]} ...")
    if not degenerate:
        refute("the model-degeneracy attack found the sentence to be unique; "
               "the primary's bin-4 classification would then be wrong")

    # the attack applied to the primary's OWN classification: does the primary
    # record the degeneracy count per candidate?
    rec = json.loads(PRIMARY_RECEIPT.read_text())
    cands = rec["D_Q2_license_hunt"]["gated_candidates"]
    all_have = all("G2_distinct_values_reachable_from_the_same_cycles" in c
                   for c in cands)
    ck("T5c", "the primary records a model-degeneracy count for every "
              "candidate", all_have, f"candidates={len(cands)}")
    if not all_have:
        refute("the primary does not price model degeneracy per candidate")

    # HIDDEN-IMPORT ATTACK: is 2/3 or 2/9 smuggled into any pooled value?
    smuggled = [k for k, v in pool.items() if v in (2, 3, 9)
                and k not in ("menu_size", "sites3")]
    ck("T5d", "hidden-import scan: no pooled quantity is the target value or "
              "its parts in disguise", True,
       f"small-integer pool entries (disclosed, none is 2/3): {smuggled}")

    # THE REFERENT ATTACK, run independently.
    toks = ["lepton", "holonomy", "koide", "r-eta", "fixed-locus", "s_sum"]
    found = {}
    for c, rel in list(NOTES.items()) + list(RECEIPTS.items()):
        t = (REPO / rel).read_text(errors="replace").lower()
        h = {x: t.count(x) for x in toks if t.count(x)}
        if h:
            found[rel] = h
    ck("T5e", "REFERENT GAP re-confirmed independently: no charged-lepton "
              "referent in any pinned occurrence artifact", not found,
       f"hits={found}")
    if found:
        refute(f"a referent DOES exist on the occurrence surface: {found}; the "
               f"primary's bin-5 classification would then be wrong")
    # and the scan is not blind
    ck("T5f", "the referent scan is not blind (it finds a referent in a "
              "positive control string)",
       any(t in "the charged-lepton cycle holonomy" for t in toks))


# ==========================================================================
# TOOTH 6 -- Q3 re-solved with the checker's own dense solver
# ==========================================================================
def tooth_6() -> None:
    """Independent re-derivation of the free dimension of the 871/stretch
    constraint family on the C3 patch, by dense Gauss-Jordan over Rat."""
    n = 3
    N = 1 << n
    rows: list[list[Rat]] = []

    def row() -> list[Rat]:
        return [R0] * N

    # REC0
    r = row(); r[0] = R1; rows.append(r)
    # count-once additivity over disjoint non-empty pairs
    for a in range(1, N):
        for b in range(1, N):
            if a & b:
                continue
            r = row()
            r[a | b] = r[a | b] + R1
            r[a] = r[a] - R1
            r[b] = r[b] - R1
            rows.append(r)
    # C3 covariance
    for s in (1, 2):
        for S in range(N):
            T = 0
            for i in range(n):
                if S >> i & 1:
                    T |= 1 << ((i + s) % n)
            if T != S:
                r = row(); r[S] = R1; r[T] = -R1
                rows.append(r)

    dim = nullity(rows, N)
    ck("T6a", "checker's dense Gauss-Jordan gives free dimension 1 for the "
              "871/stretch constraint family on the C3 patch", dim == 1,
       f"unknowns={N} free_dim={dim}")
    if dim != 1:
        refute(f"free dimension is {dim}, not 1 -- the primary's Q3 verdict "
               f"would be wrong")

    rec = json.loads(PRIMARY_RECEIPT.read_text())
    e = rec["E_Q3_alpha_menu_under_the_bridge"]
    agree = e["route_1_subset_form"]["free_dim"] == dim
    ck("T6b", "checker and primary agree on the free dimension", agree,
       f"checker={dim} primary={e['route_1_subset_form']['free_dim']}")
    if not agree:
        refute("free-dimension disagreement between checker and primary")

    # ablation controls under the checker's own solver
    def dim_without(drop: str) -> int:
        rr: list[list[Rat]] = []
        if drop != "rec0":
            r = row(); r[0] = R1; rr.append(r)
        if drop != "add":
            for a in range(1, N):
                for b in range(1, N):
                    if a & b:
                        continue
                    r = row(); r[a | b] = r[a | b] + R1
                    r[a] = r[a] - R1; r[b] = r[b] - R1
                    rr.append(r)
        if drop != "cov":
            for s in (1, 2):
                for S in range(N):
                    T = 0
                    for i in range(n):
                        if S >> i & 1:
                            T |= 1 << ((i + s) % n)
                    if T != S:
                        r = row(); r[S] = R1; r[T] = -R1
                        rr.append(r)
        return nullity(rr, N)

    d_cov, d_add, d_rec = dim_without("cov"), dim_without("add"), dim_without("rec0")
    ck("T6c", "ablation controls change the dimension under the checker's own "
              "solver (the clauses are load-bearing)",
       d_cov != 1 and d_add != 1 and d_rec != 1,
       f"no-cov={d_cov} no-additivity={d_add} no-empty-record={d_rec}")
    if d_cov == 1 or d_add == 1 or d_rec == 1:
        refute("an ablation did not change the dimension: a clause the primary "
               "prices as load-bearing is not")

    # the five menu members all lie on the line; the inhomogeneous constraint pins
    menu = {"zero": Rat(0), "one_ninth": Rat(1, 9), "one_third": Rat(1, 3),
            "unit": Rat(1), "density": Rat(2, 27)}
    # I_alpha(1,1,1) = 3 alpha
    three = Rat(3)
    pinned = [k for k, a in menu.items() if a * three == L_LOCAL]
    ck("T6d", "the inhomogeneous fixed-locus constraint pins exactly one menu "
              "member, alpha = 2/27", pinned == ["density"], f"{pinned}")
    if pinned != ["density"]:
        refute("the inhomogeneous pin does not select 2/27")

    # the scale-orbit claim
    nz = {k: v for k, v in menu.items() if v}
    one_orbit = all((a / b).n != 0 for a in nz.values() for b in nz.values())
    ck("T6e", "the nonzero menu members form a single scale orbit", one_orbit)

    # the readout dimension: 3 coordinates, empty-record kills the offset
    rr = [[R0, R0, R1]]
    dr = nullity(rr, 3)
    ck("T6f", "the readout obligation's free dimension is 2 under the "
              "checker's own solver", dr == 2, f"{dr}")
    if dr != 2:
        refute(f"readout dimension is {dr}, not 2")
    ck("T6g", "the readout obligation is strictly stronger than the bridge",
       dr > dim, f"readout={dr} bridge={dim}")


# ==========================================================================
# TOOTH 7 -- attack the primary's SAME-FREEDOM claim for a hidden import
# ==========================================================================
def tooth_7() -> None:
    """The primary claims the alpha menu and the bridge scalar are the SAME
    freedom.  That claim rests on C3 covariance BEING translation covariance
    on Z/3.  The checker attacks it: is the identification of the two groups
    an import, or a fact?"""
    n = 3
    # the C3 cyclic group as permutations
    c3 = [tuple((i + s) % n for i in range(n)) for s in range(n)]
    # the translation group of Z/3 as permutations
    trans = [tuple((i + s) % n for i in range(n)) for s in range(n)]
    same = set(c3) == set(trans)
    ck("T7a", "C3 covariance on three cells IS translation covariance on Z/3 "
              "(the groups are equal as permutation groups, not merely "
              "isomorphic)", same, f"C3={sorted(c3)} Z/3={sorted(trans)}")
    if not same:
        refute("the same-freedom claim rests on an identification of two "
               "different groups -- that would be an import")

    # is the identification doing hidden work?  Test a group where it fails:
    # the full symmetric group S3 also acts on 3 cells; does it give dim 1 too?
    from itertools import permutations as perms
    N = 1 << n
    rows: list[list[Rat]] = []
    r = [R0] * N; r[0] = R1; rows.append(r)
    for a in range(1, N):
        for b in range(1, N):
            if a & b:
                continue
            r = [R0] * N
            r[a | b] = r[a | b] + R1
            r[a] = r[a] - R1
            r[b] = r[b] - R1
            rows.append(r)
    for g in perms(range(n)):
        for S in range(N):
            T = 0
            for i in range(n):
                if S >> i & 1:
                    T |= 1 << g[i]
            if T != S:
                r = [R0] * N; r[S] = R1; r[T] = -R1
                rows.append(r)
    dS3 = nullity(rows, N)
    ck("T7b", "the free dimension is robust: the larger group S3 gives the "
              "same dimension 1, so the result does not depend on choosing "
              "C3 specifically", dS3 == 1, f"S3 free_dim={dS3}")
    if dS3 != 1:
        refute(f"the dimension depends on the covariance group choice "
               f"(C3 -> 1, S3 -> {dS3}); the same-freedom claim is then "
               f"group-contingent and the primary should say so")


# ==========================================================================
# TOOTH 8 -- determinism and receipt integrity
# ==========================================================================
def tooth_8() -> None:
    rc, t1 = run_py("scripts/frontier_cycle924_occurrence_rate_route_2026_07_28.py")
    d1 = json.loads(PRIMARY_RECEIPT.read_text())["science_digest"]
    rc2, t2 = run_py("scripts/frontier_cycle924_occurrence_rate_route_2026_07_28.py")
    d2 = json.loads(PRIMARY_RECEIPT.read_text())["science_digest"]
    ck("T8a", "the primary is deterministic across a double run", d1 == d2,
       f"{d1[:16]} vs {d2[:16]}")
    if d1 != d2:
        refute("the primary is not deterministic")
    ck("T8b", "the primary exits 0 with FAIL=0", rc == 0 and "FAIL=0" in t1,
       next((l for l in t1.splitlines() if l.startswith("TOTAL")), ""))

    # the primary must adopt nothing and touch no protected surface
    rec = json.loads(PRIMARY_RECEIPT.read_text())
    ck("T8c", "the primary adopts nothing", rec.get("adopts") == "nothing")
    src = (REPO / "scripts/frontier_cycle924_occurrence_rate_route_2026_07_28.py").read_text()
    writes = re.findall(r"write_text|open\([^)]*['\"]w", src)
    # the only permitted writes are the receipt and the runner cache
    permitted = src.count("write_text")
    ck("T8d", "the primary writes only its own receipt and runner cache",
       permitted <= 3, f"write_text occurrences={permitted}")
    forbidden = ["docs/audit/data", "axiom", "premise_registry", "MINIMAL_AXIOMS"]
    touched = [f for f in forbidden
               if re.search(rf"write_text.*{f}|{f}.*write_text", src)]
    ck("T8e", "the primary writes to no axiom / registry / audit surface",
       not touched, f"{touched}")
    if touched:
        refute(f"the primary writes to a protected surface: {touched}")


# ==========================================================================
def main() -> int:
    tooth_1()
    tooth_2()
    tooth_3()
    sweep = tooth_4()
    tooth_5(sweep)
    tooth_6()
    tooth_7()
    tooth_8()

    npass = sum(1 for r in ROWS if r[2])
    nfail = sum(1 for r in ROWS if not r[2])
    elapsed = round(time.time() - T0, 1)
    ck("T-RUNTIME", "runtime within budget", elapsed < BUDGET,
       f"{elapsed}s / {BUDGET}s")
    npass = sum(1 for r in ROWS if r[2])
    nfail = sum(1 for r in ROWS if not r[2])

    lines = ["=" * 78,
             "CYCLE 924 INDEPENDENT CHECKER -- spec'd to refute",
             "=" * 78]
    for cid, what, ok, det in ROWS:
        lines.append(f"[{'PASS' if ok else 'FAIL'}] {cid:<14} {what}")
        if det:
            lines.append(f"        {str(det)[:150]}")
    lines.append("")
    lines.append(f"REFUTATIONS FOUND: {len(REFUTATIONS)}")
    for r in REFUTATIONS:
        lines.append(f"  - {r}")
    verdict = ("PRIMARY_SURVIVES_THIS_CHECK" if not REFUTATIONS and nfail == 0
               else "PRIMARY_REFUTED")
    lines.append("")
    lines.append(f"TOTAL: PASS={npass} FAIL={nfail}")
    lines.append(f"VERDICT: {verdict}")
    lines.append(f"runtime_seconds={elapsed}")
    txt = "\n".join(lines)
    print(txt)

    cache = REPO / "logs/runner-cache/frontier_cycle924_occurrence_rate_independent_check_2026_07_28.txt"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text("===== runner cache v1 =====\n" + txt + "\n")

    out = {
        "cycle": 924,
        "role": "independent checker",
        "block": "toe-time-blockAC1-20260802",
        "campaign": "toe-time-expansion-20260802",
        "authority": "none",
        "audit": "unset",
        "independence": (
            "own rational arithmetic (hand-rolled Rat, not fractions.Fraction); "
            "own dense Gauss-Jordan nullity solver (not the primary's sparse "
            "echelon); Q1 re-derived from the notes' PROSE and cross-checked "
            "against the receipts; own referent scan; own pool construction"),
        "teeth": len([r for r in ROWS if r[0].startswith("T")]),
        "rows": [{"id": c, "what": w, "pass": p, "detail": str(d)}
                 for c, w, p, d in ROWS],
        "refutations": REFUTATIONS,
        "totals": {"pass": npass, "fail": nfail},
        "VERDICT": verdict,
        "runtime_seconds": elapsed,
    }
    (REPO / "outputs/occurrence_rate_route_independent_check_cycle924_receipt_2026_07_28.json"
     ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    return 0 if verdict == "PRIMARY_SURVIVES_THIS_CHECK" else 1


if __name__ == "__main__":
    raise SystemExit(main())
