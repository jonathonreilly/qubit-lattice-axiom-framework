#!/usr/bin/env python3
"""J:provenance:PR8612 - every number in the theorem statements T1-T4 of block 77's note against its runner cache,
an exact derivation in the note itself, or (for numbers the note attributes to another block) that block's cache (INFO).
Unicode and ASCII forms are matched after one normalisation (minus, plus-minus, root, squares, subscripts, halves,
pi, sigma, sum, eps, phi, Theta, not-equal, times); whitespace is ignored."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PFX = "physics-loop/admissibility-induced-law-"
B77 = PFX + "block77-the-axioms-own-generator-and-a-staggered-rest-term-20260922"
NOTE = ("docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_"
        "OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md")
CACHE = ("logs/runner-cache/admissibility_rule_the_axioms_own_generator_scalar_hop_splits_species_staggered_term_"
         "gives_mass_2026_09_22.txt")
OTHER = {
    "block 62": (PFX + "block62-angles-are-the-tilt-of-the-coins-frame-two-disturbances-one-direction-free-speed-20260921",
                 "logs/runner-cache/admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_"
                 "travel_at_one_direction_free_speed_2026_09_21.txt"),
    "block 63": (PFX + "block63-what-the-walk-conserves-momentum-flows-on-bonds-20260921",
                 "logs/runner-cache/admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_"
                 "reach_second_neighbours_2026_09_21.txt"),
    "block 69": (PFX + "block69-reach-three-exact-books-and-one-geometry-for-all-eight-species-20260921",
                 "logs/runner-cache/admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_"
                 "2026_09_21.txt"),
    "block 70": (PFX + "block70-species-exchange-maps-what-each-varying-field-becomes-20260921",
                 "logs/runner-cache/admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_"
                 "of_the_coin_2026_09_21.txt"),
}

UNI = [("−", "-"), ("±", "+-"), ("√", "sqrt"), ("²", "^2"), ("³", "^3"), ("₀", "0"), ("₂", "_2"), ("½", "(1/2)"),
       ("π", "pi"), ("Σ", "sum"), ("σ", "sigma"), ("ε", "eps"), ("φ", "phi"), ("Θ", "theta"), ("≠", "!="),
       ("×", "x"), ("·", "."), ("`", "")]


def norm(s):
    s = s.lower()
    for u, a in UNI:
        s = s.replace(u.lower(), a)
    return re.sub(r"\s+", "", s)


def show(branch, path):
    ref = f"origin/{branch}:{path}"
    try:
        return subprocess.check_output(["git", "show", ref], cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run(["git", "fetch", "origin", branch, "--quiet"], cwd=ROOT, check=True)
        return subprocess.check_output(["git", "show", ref], cwd=ROOT, text=True)


def find(blob, alts):
    """first line of blob containing one of alts (normalised); returns (alt, excerpt) or None."""
    lines = [ln for ln in blob.splitlines() if "sha256" not in ln.lower()]
    for alt in alts:
        na = norm(alt)
        for ln in lines:
            nl = norm(ln)
            i = nl.find(na)
            if i >= 0:
                label = ln.strip().split(":")[0] + ":" + ln.strip().split(":")[1] if ln.startswith("PASS") else \
                    ln.strip()[:24]
                return alt, label
    return None


# (theorem, number as stated, role, where to look, [search forms])
#   where: "cache"  - block 77's runner cache;  "note" - an exact derivation in the note's premises or proofs;
#          ("block NN", ...) - the block the note attributes it to (INFO when that block's cache prints it)
NUMBERS = [
    ("T1", "eight zeros", "count of the walk's zeros", "cache", ["eight zeros"]),
    ("T1", "k = πn", "the zeros", "note", ["At `k = πn`: `Σcos k_j = 3 − 2|n|`"]),
    ("T1", "a₀ + 2a(3 − 2|n|)", "level energies", "cache", ["a0 + 2a(3 - 2|n|)"]),
    ("T1", "four levels", "number of levels", "cache", ["four energies", "four energy levels"]),
    ("T1", "|n| = 0, 1, 2, 3", "level labels", "note", ["`|n|` the number of components equal to 1"]),
    ("T1", "1, 3, 3, 1", "multiplicities", "cache", ["1:3:3:1"]),
    ("T1", "(−1)^{|n|}", "sense of a level", "block 70",
     ["det(D_n) is the sense of species n (the determinant of the slopes of sin k_a at its zero)"]),
    ("T1", "(−1)^{|n|}", "sense of a level (value)", "note", ["`cos(πn_j) = (−1)^{n_j}`"]),
    ("T1", "s(πn) = 0", "branches meet", "note", ["`sin(πn_j) = 0`"]),
    ("T2", "(1 − s_n)a₀ + 2aΣ_j(D_j − s_n)C_j", "exchange-map defect (s_n = det D_n)", "cache",
     ["(1 - det D_n) a0 psi + 2a sum_j (D_j - det D_n) C_j psi"]),
    ("T2", "n ≠ 0", "species broken", "cache", ["nonzero for the seven species n != 0"]),
    ("T2", "odd n when a₀ ≠ 0", "a0 part: 1 - s_n = 2 for odd |n|", "note", ["sense `s_n = (−1)^{|n|}`"]),
    ("T2", "Θ = σ₂K", "reversal of motion", "block 70", ["Theta = sigma_2 x (complex conjugation)"]),
    ("T2", "Θ commutes with H_a", "reversal kept", "cache", ["Theta still commutes with H_a"]),
    ("T3", "½Σ{E^j·σ, S_j}", "block 62's frame coupling", "block 62", ["(1/2) sum_j {E^j.sigma, S_j}"]),
    ("T3", "Σσ_a½{C_a[B_a^j], P_j}", "reach-three strain term", "block 69", ["sigma_a (1/2){C_a[d_a xi_j], P_j}"]),
    ("T3", "Σσ_a½{C_a[B_a^j], S_j}", "reach-two strain term", "block 63", ["sigma_a (1/2){(d_a xi_j) C_a, S_j}"]),
    ("T3", "(H + mε)² = H² + m²", "square of the massive walk", "cache", ["(H + m eps)^2 psi = (H^2 + m^2) psi"]),
    ("T3", "φ(H + mε)φ = φHφ + m w ε", "clocked form", "cache", ["phi (H + m eps) phi = phi H phi + m w eps"]),
    ("T4", "k + π(1,1,1)", "mixed wave vectors", "cache", ["k + pi(1,1,1)"]),
    ("T4", "2 × 2", "block size", "cache", ["2x2 blocks"]),
    ("T4", "a₀ ± √((2aΣcos k ± |s|)² + m²)", "block eigenvalues", "cache",
     ["a0 +- sqrt((2a sum cos k +- |sin k|)^2 + m^2)"]),
    ("T4", "(n, n + (111))", "pairing", "cache", ["(n, n + (111))"]),
    ("T4", "a₀ ± √(m² + 4a²(3 − 2|n|)²)", "energies at the zeros", "note", ["At a zero `|s| = 0`, `c = 3 − 2|n|`"]),
    ("T4", "√(m² + 36a²)", "heavy mass", "cache", ["ONE pair of mass sqrt(m^2 + 36a^2)"]),
    ("T4", "|n| = 0, 3 and 1, 2", "which pairs", "note", ["`|3 − 2|n||` is 3 or 1"]),
    ("T4", "√(m² + 4a²)", "light mass", "cache", ["THREE pairs of mass sqrt(m^2 + 4a^2)"]),
    ("T4", "four masses equal iff a = 0", "degeneracy", "cache", ["all four masses equal m iff a = 0"]),
]


def main():
    note = show(B77, NOTE)
    cache = show(B77, CACHE)
    stmts = {t: m.group(1) for t, m in ((t, re.search(r"## Theorem " + t + r" .*?\n\n\*Statement\.\*(.*?)\n", note, re.S))
                                        for t in ("T1", "T2", "T3", "T4")) if m}
    proofs = "\n".join(ln for ln in note.splitlines()
                       if ln.startswith("*Proof.*") or ln.startswith("- **"))
    others = {}
    counts = {"cache": 0, "note": 0, "info": 0, "none": 0}
    bad_listing = 0
    for thm, num, role, where, alts in NUMBERS:
        stated = norm(num.split(" when ")[-1].split(" and ")[0]) in norm(stmts.get(thm, "")) or \
            all(norm(p) in norm(stmts.get(thm, "")) for p in re.findall(r"[0-9]+", num))
        if not stated:
            bad_listing += 1
        if where == "cache":
            got = find(cache, alts)
            tag = "cache"
        elif where == "note":
            got = find(proofs, alts)
            tag = "note"
        else:
            if where not in others:
                others[where] = show(*OTHER[where])
            got = find(others[where], alts)
            tag = "info"
        if got:
            counts[tag] += 1
            label = {"cache": "OK cache", "note": "OK note (exact derivation)", "info": f"INFO {where} cache"}[tag]
            print(f"{thm} | {num} | {role} | {label}: '{got[0][:60]}' in {got[1][:40]}")
        else:
            counts["none"] += 1
            print(f"{thm} | {num} | {role} | UNSOURCED (looked in {where})")
    n = len(NUMBERS)
    print(f"statements read: {', '.join(sorted(stmts))}; every listed number occurs in its statement: {bad_listing == 0}")
    print(f"SUMMARY: {n} numbers in the statements of T1-T4 of PR #8612's note: {counts['cache']} printed by its runner "
          f"cache, {counts['note']} derived exactly in the note, {counts['info']} printed by the cache of the block the "
          f"note attributes them to (INFO); {counts['none']} unsourced")
    if counts["none"] or bad_listing:
        print("HIT: unsourced numbers in the theorem statements (see the UNSOURCED lines)")


if __name__ == "__main__":
    main()
