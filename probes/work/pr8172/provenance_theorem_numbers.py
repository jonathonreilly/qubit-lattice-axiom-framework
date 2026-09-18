#!/usr/bin/env python3
"""J:provenance:PR8172 - every number in the theorem statements of the block 28 note (the map of memory: the four laws' strengths located
against the proved regions, with the healing and influence bounds),
located in the runner's cached stdout, in the runner's own checks, or in an exact derivation in the note.

Statement text = the front-matter claim_scope + each '## Theorem ...' section with its proof spans ('*Proof.* ... ∎') and its '*Reading.*'
paragraphs removed.  Every
numeric token of that text (integers, decimals, fractions a/b, number words) must fall inside one listed item:
  CACHE       printed by the runner (logs/runner-cache/<runner>.txt at the PR head)                              -> sourced
  RUNNER      computed and checked by the runner source at the stated precision, not printed                     -> sourced (flagged)
  DERIVED     an exact derivation or formula stated in the note, re-executed here (fractions / sympy)             -> sourced
  DEFINITION  a constant of a declared object                                                                    -> not a claim
  EXCLUDED    a reference (block / PR number) or a structural constant of a condition, domain or notation        -> not a claim
  (else)      HIT: no runner line, no runner check, no derivation in the note; the PR files that carry it are named, and where a
              control output prints the quantity the stated value is compared with it (MISMATCH notes).
Tokens covered by no item are printed as UNCOVERED; the run is logged only with zero UNCOVERED.  Self-contained; reads the PR head via
git (fetches the branch if the commit is missing).
"""
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PR = 8172
BRANCH = "physics-loop/admissibility-induced-law-block28-map-of-memory-four-laws-located-healing-influence-20260916"
HEAD = "c8ae4a4622c1aa924ff6c9b3452021022f20746d"
NOTE = ("docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_"
        "HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py"
CACHE = ("logs/runner-cache/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_"
         "bounds_2026_09_16.txt")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block28_"
EXA, REF, FORM, STS, SPH = (SPECS + "exact.out.txt", SPECS + "refuter.out.txt", SPECS + "scan_formation_sixaxis.out.txt",
                            SPECS + "scan_static_sixaxis.out.txt", SPECS + "scan_static_sphere.out.txt")
OTHER = [EXA, REF, FORM, STS, SPH]


# ------------------------------------------------------------------------------------------------------------------ text access
def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {HEAD}: {r.stderr.strip()}")
    return r.stdout


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
REPL = (("θ̂", "theta^"), ("θ̄", "theta_bar"), ("ξ̂", "xi^"), ("m̂", "m^"), ("ŝ", "s^"), ("−", "-"), ("–", "-"), ("—", " - "), ("×", "x"),
        ("≤", "<="), ("≥", ">="), ("π", "pi"), ("β", "beta"), ("σ", "sigma"), ("φ", "phi"), ("θ", "theta"), ("`", ""), ("∗", "*"),
        ("Σ", "Sigma"), ("ᵀ", "^T"), ("≳", ">~"), ("√", "sqrt"), ("∂", "d"), ("≠", "!="), ("ξ", "xi"), ("γ", "gamma"), ("τ", "tau"),
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"), ("ε", "epsilon"), ("η", "eta"))


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in REPL:
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


def statement_sections(note):
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", norm(m.group(1)))]
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        if title.lower().startswith("theorem"):
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            body = re.sub(r"\*{1,2}Proof\.?\*{1,2}.*?(?:∎|$)", " ", body, flags=re.S)
            body = re.split(r"\*Reading\.\*", body)[0]          # interpretation paragraphs are not statements
            out.append((title.split(" — ")[0], norm(body)))
    return out


def section(note, prefix):
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        if sec.startswith(prefix):
            return norm(sec)
    return ""


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+/\d+|\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|sixteen|sixty-four|third|thirds|half|quarter|"
                   r"tenth|tenths|hundred|hundredth|double|twice|single|pair)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


# ------------------------------------------------------------------------------------------------------------------ exact re-derivations
AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi(v, w, p, q, r):
    if v == w:
        return p
    if all(a == -b for a, b in zip(v, w)):
        return q
    return r


def c_sens(p, q=Fr(1), r=Fr(2)):
    """block 08's c(p): max over predecessor triples (a, b, c) and alternatives a' != a of TV(K(.|a,b,c), K(.|a',b,c)),
    K(v | a, b, c) proportional to phi(v,a) phi(v,b) phi(v,c) - computed here from the definition (6^3 triples x 5 alternatives)."""
    def K(a, b, c):
        w = [phi(v, a, p, q, r) * phi(v, b, p, q, r) * phi(v, c, p, q, r) for v in AX]
        z = sum(w)
        return [x / z for x in w]
    best = Fr(0)
    for a in AX:
        for b in AX:
            for c in AX:
                k0 = K(a, b, c)
                for a2 in AX:
                    if a2 == a:
                        continue
                    k1 = K(a2, b, c)
                    tv = sum(abs(x - y) for x, y in zip(k0, k1)) / 2
                    best = max(best, tv)
    return best


def eps(p, q=Fr(1), r=Fr(2)):
    d1 = (q ** 3 + 4 * r ** 3) / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p * p * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p * p * r / (r * (p * p + q * q) + r * r * (p + q) + 2 * r ** 3)
    return max(d1, d2, d3)


def derive_T1_c():
    c1, c2 = c_sens(Fr(37, 10)), c_sens(Fr(19, 5))
    ok = 3 * c1 == Fr(406962630, 413162167) and 3 * c2 == Fr(871815, 862244) and 3 * c1 < 1 < 3 * c2
    return ok, f"recomputed from the definition over 216 x 5 (triple, alternative) pairs: 3c(37/10) = {3 * c1}, 3c(19/5) = {3 * c2}"


def derive_T1_eps():
    e1, e0 = eps(Fr(285718)), eps(Fr(285717))
    ok = e1 <= Fr(7, 10 ** 6) < e0
    return ok, f"block 25's closed forms (quoted in the proof): eps(285718) = {float(e1):.9e} <= 7e-6 < eps(285717) = {float(e0):.9e}"


def derive_between():
    ok = Fr(37, 10) == Fr(37, 10) and Fr(19, 5) == Fr(38, 10)
    return ok, "37/10 = 3.7 and 19/5 = 3.8: the criterion's threshold lies between them (from the two printed values)"


def derive_third():
    lo, hi = Fr(36, 10) / 11, Fr(37, 10) / Fr(105, 10)
    return True, f"located brackets (3.6, 3.7) static and (10.5, 11) formation give a ratio in ({float(lo):.3f}, {float(hi):.3f}) (control brackets; see exec lines)"


def island_region(I):
    """exact U(I) and F_{D+1}(I) for a level-0 island I (list of integer triples with zero coordinate sum)."""
    M = [max(i[j] for i in I) for j in range(3)]
    D = sum(M)
    F = set()
    for i in I:
        for d1 in range(D + 2):
            for d2 in range(D + 2 - d1):
                d3 = D + 1 - d1 - d2
                F.add((i[0] + d1, i[1] + d2, i[2] + d3))
    U = set()
    for x in F:
        for e1 in range(D + 1):
            for e2 in range(D + 1 - e1):
                for e3 in range(D + 1 - e1 - e2):
                    y = (x[0] - e1, x[1] - e2, x[2] - e3)
                    if 1 <= sum(y) <= D + 1:
                        U.add(y)
    return D, M, F, U


def t2_proof_step_info():
    import random
    rnd = random.Random(8172)
    worst = Fr(0)
    viol = 0
    n = 0
    examples = [[(1, 1, -2)], [(2, -1, -1)], [(3, 0, -3), (0, 1, -1)]]
    for _ in range(400):
        k = rnd.randint(1, 4)
        I = set()
        while len(I) < k:
            a, b = rnd.randint(-3, 3), rnd.randint(-3, 3)
            I.add((a, b, -a - b))
        examples.append(sorted(I))
    for I in examples:
        D, M, F, U = island_region(I)
        if D > 6:
            continue
        n += 1
        worst = max(worst, Fr(len(U), (D + 1) ** 3))
        if any(y[j] > 2 * D + 1 for y in U for j in range(3)):
            viol += 1
    D, M, F, U = island_region([(1, 1, -2)])
    ymax = max(y[0] for y in U)
    return (f"T2's derivation step 'x_j <= D + 1 + i_j <= 2D + 1' (so every y in U(I) has y_j <= 2D + 1) fails on {viol} of {n} "
            f"enumerated level-0 islands with D <= 6 (coordinates in [-3, 3]); e.g. I = {{(1, 1, -2)}}: D = {D}, U(I) = {sorted(U)}, "
            f"y_1 up to {ymax} > 2D + 1 = {2 * D + 1}; the stated bound itself holds on all of them: max |U(I)|/(D + 1)^3 = {worst} "
            f"= {float(worst):.3f} <= 18 (the per-coordinate box y_j <= D + 1 + M_j gives |U(I)| <= 2(D + 1)^2 (4D + 3) <= 8(D + 1)^3)")


def derive_T2_poly():
    import sympy as sp
    D = sp.symbols("D", nonnegative=True)
    ok = sp.expand(18 * (D + 1) ** 3 - (D + 1) * (6 * D + 5) * (6 * D + 4) / 2 - (D + 1) * (9 * D + 8)) == 0
    return ok, "18(D+1)^3 - (D+1)(6D+5)(6D+4)/2 = (D+1)(9D+8) (sympy)"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("ref-blocks", r"block (?:08|25|26|27)'?s?(?: uniqueness criterion| ordering condition| criterion)?|\(block (?:26|27)\)|causal coupling of block 27",
     "EXCLUDED", "reference (blocks 08, 25, 26, 27)", "citation"),
    ("weights", r"weights \(p, q, r\)|at \(p, 1, 2\)|epsilon\(p, 1, 2\)|\(p, 1, 2\)", "DEFINITION", r"the weights \(p, 1, 2\) throughout the map",
     "the weight line (p, 1, 2)"),
    ("Z3Z2", r"Gibbs law on Z\^3\)|level automaton on Z\^2\)", "EXCLUDED", "structural: the lattices of the two readings", "wording"),
    ("six-axis", r"six-axis", "EXCLUDED", "name of the menu", "wording"),
    ("two-planes", r"two initial planes", "EXCLUDED", "structural: two coupled runs", "wording"),
    ("T1-c", r"3c < 1 for the formation law holds at p = 37/10 and fails at p = 19/5|3c\(37/10\) = 406962630/413162167 < 1 and 3c\(19/5\) = 871815/862244 > 1",
     "CACHE", r"3c = 406962630/413162167 < 1 at p = 37/10 and 3c = 871815/862244 > 1 at p = 19/5", "T1 block 08's criterion at two points"),
    ("T1-c-exact", r"406962630/413162167", "DERIVED", (derive_T1_c, r"evaluated exactly at the two points over the 216 triples"),
     "T1 exact values recomputed"),
    ("T1-one-pred", r"to one predecessor", "EXCLUDED", "structural: the definition of c (one predecessor changed)", "definition"),
    ("T1-eps", r"epsilon(?:\(p, 1, 2\))? <= 7/10\^6 holds (?:from|at) p = 285718(?: and fails at 285717)?", "CACHE",
     r"epsilon\(p, 1, 2\) <= 7/10\^6 holds at p = 285718 and fails at 285717", "T1 block 25's condition"),
    ("T1-eps-exact", r"fails at 285717", "DERIVED", (derive_T1_eps, r"closed forms"), "T1 eps recomputed from the closed forms"),
    ("T1-between", r"holds up to a p between 3\.7 and 3\.8", "DERIVED", (derive_between, r"between `?3\.7`? and `?3\.8`?"), "T1 threshold bracket"),
    ("T2-level0", r"island of ones at level 0", "DEFINITION", r"a finite set `?I`? of ones on level `?0`?|finite set I of ones on level 0", "island"),
    ("T2-D", r"D = M_1 \+ M_2 \+ M_3", "CACHE", r"D = M_1 \+ M_2 \+ M_3", "T2 D"),
    ("T2-empty", r"(?:is )?empty at level D \+ 1", "CACHE", r"every island is empty at level D \+ 1", "T2 eroder bound"),
    ("T2-cone", r"one in (?:its forward cone at level D \+ 1|F_\{D\+1\}\(I\))", "CACHE", r"forward cone", "T2 the event (a one in F_{D+1})"),
    ("T2-18", r"(?:at most )?18 ?\(D \+ 1\)\^3(?: sites| ?epsilon)?", "CACHE", r"at most 18 \(D\+1\)\^3 sites", "T2 region bound"),
    ("T2-prob", r"survives with probability at most 18 \(D \+ 1\)\^3 epsilon|<= \|U\(I\)\| epsilon <= 18\(D \+ 1\)\^3 epsilon", "CACHE",
     r"18 \(D\+1\)\^3", "T2 survival bound (the region bound times epsilon)"),
    ("T2-poly", r"the eroder bound re-proved", "DERIVED", (derive_T2_poly, r"the difference being"), "T2 the polynomial comparison"),
    ("T2-120", r"on 120 random islands", "CACHE", r"on 120 random islands", "T2 executed island count"),
    ("exec-T2-405", r"at most 4\.05\(D \+ 1\)\^3", "CACHE", r"4\.05", "executed (T2 parenthetical): max |U|/(D+1)^3", r"worst \|U\|/\(D\+1\)\^3"),
    ("exec-T2-eps3", r"epsilon = 10\^\{-3\}", "CACHE", r"10\^-3", "executed (T2 parenthetical): refuter noise level", r"eps = 10\^-3"),
    ("T3-bound", r"2 ?\(sqrt3 ?beta\)\^t p_t\(x - x_0\)", "CACHE", r"2 \(sqrt3 beta\)\^t p_t\(x - x_0\)", "T3 influence bound"),
    ("T3-sum", r"Sigma_x D_t\(x\) <= 2\(sqrt3beta\)\^t", "CACHE", r"whose sum over the level is 2 \(sqrt3 beta\)\^t", "T3 level sum"),
    ("T3-onesite", r"differing at one site x_0|differ at x_0 only", "EXCLUDED", "structural: one differing site", "condition"),
    ("T3-beta", r"at any beta > 0", "EXCLUDED", "structural: coupling domain", "condition"),
    # executed and not claimed (the map)
    ("exec-form", r"keeps its aligned plane from a strength between 10\.5 and 11", "CACHE", r"10\.5", "executed-not-claimed: formation six-axis bracket",
     r"p=  1[01]\.[05]: memory mean"),
    ("exec-form-runs", r"\(128\^2 and 256\^2 planes, 4000-8000 levels\)", "CACHE", r"on 128\^2 and 256\^2 planes", "executed: formation runs (descriptive)"),
    ("exec-regions", r"proved region p >= 285718 and uniqueness for p <= 37/10", "CACHE", r"285718", "placement: the T1 values"),
    ("exec-static", r"keeps a majority value from a strength between 3\.6 and 3\.7", "CACHE", r"3\.6 and 3\.7",
     "executed-not-claimed: static six-axis bracket", r"p= 3\.[67]0: order"),
    ("exec-static-runs", r"\(16\^3, 24\^3, 32\^3 lattices, aligned and random starts, heat bath and single-site proposals\)", "CACHE",
     r"the six-axis static law on 16\^3, 24\^3, 32\^3", "executed: static six-axis runs (descriptive)"),
    ("exec-b17", r"proved region p >= 432 at \(p, 1, 2\) and uniqueness at \(3, 1, 2\)", "EXCLUDED", "reference: blocks 17 (p >= 432) and 03 ((3, 1, 2))",
     "citation"),
    ("exec-sphere", r"keeps a magnetization from beta between 0\.66 and 0\.72 \(16\^3, 24\^3\)", "CACHE", r"0\.66 and 0\.72",
     "executed-not-claimed: static sphere bracket", r"beta=0\.(?:66|68|70|72)0: \|m\|"),
    ("exec-b22", r"proved region beta > 76/100 and uniqueness for beta < sqrt3/6", "EXCLUDED", "reference: blocks 22 (76/100) and 21 (sqrt3/6)",
     "citation"),
    ("exec-b27", r"uniqueness for beta < 1/sqrt3", "EXCLUDED", "reference: block 27 (1/sqrt3)", "citation"),
    ("exec-third", r"about a third of the preference strength", "CACHE", r"a third", "executed-not-claimed: static/formation ratio"),
]


def control_checks():
    extra, notes = {}, []
    sts, form, sph, ref = show(STS), show(FORM), show(SPH), show(REF)

    def rows(txt, tag, pat):
        out = {}
        for blk in re.split(r"(?m)^===== ", txt)[1:]:
            name = blk.split(" =====", 1)[0]
            if tag in name:
                for m in re.finditer(pat, blk):
                    out[(name, float(m.group(1)))] = tuple(float(g) for g in m.groups()[1:])
        return out
    st = rows(sts, "stat_sixaxis", r"p= ([0-9.]+): order ([0-9.]+) \| ([0-9.]+)")
    runs = {}
    for (name, p), v in st.items():
        runs.setdefault(name, []).append((p, v))
    br = []
    for name, lst in sorted(runs.items()):
        lst.sort()
        lo = max((p for p, v in lst if max(v) < 0.5), default=None)
        hi = min((p for p, v in lst if min(v) > 0.5 and (lo is None or p > lo)), default=None)
        br.append(f"{name}: ({lo}, {hi})")
    met = {float(m.group(1)): float(m.group(2)) for m in re.finditer(r"p= ([0-9.]+): order ([0-9.]+)", ref.split("(b)")[1].split("(c)")[0])}
    mlo = max(p for p, v in met.items() if v < 0.5)
    mhi = min(p for p, v in met.items() if v > 0.5)
    at37 = [name for (name, p) in st if abs(p - 3.7) < 1e-9]
    extra["exec-static"] = (f"; control brackets of the order: {'; '.join(br)}; single-site proposals (refuter, L=16): ({mlo}, {mhi}); runs at p = 3.7: "
                            f"{', '.join(sorted(set(at37)))} only (none on 16^3, none with single-site proposals): MISMATCH with the stated run list "
                            f"'16^3, 24^3, 32^3 ... heat bath and single-site proposals' for the bracket (3.6, 3.7)")
    fm = rows(form, "form_sixaxis", r"p= +([0-9.]+): memory mean ([0-9.]+)")
    fr = {}
    for (name, p), v in fm.items():
        fr.setdefault(name, []).append((p, v[0]))
    fb = []
    for name, lst in sorted(fr.items()):
        lst.sort()
        lo = max((p for p, v in lst if v < 0.5), default=None)
        hi = min((p for p, v in lst if v > 0.5 and (lo is None or p > lo)), default=None)
        fb.append(f"{name}: ({lo}, {hi})")
    extra["exec-form"] = "; control brackets of the memory: " + "; ".join(fb)
    sp_ = rows(sph, "stat_sphere", r"beta=([0-9.]+): \|m\| = ([0-9.]+)")
    extra["exec-sphere"] = "; control |m| on 24^3 fine: " + ", ".join(f"{b:.2f}: {v[0]:.4f}" for (n, b), v in sorted(sp_.items()) if "L24_fine" in n)
    exa = show(EXA)
    m = re.search(r"on (\d+) random islands: True; worst \|U\|/\(D\+1\)\^3 = ([0-9.]+)", exa)
    extra["exec-T2-405"] = (f"; MISMATCH: the runner prints 'on 120 random islands (largest ratio 6671/1728)' = {6671 / 1728:.3f}; the exact spec prints worst "
                            f"{m.group(2)} on {m.group(1)} islands: the stated '120 random islands ... at most 4.05' pairs the runner's island count with "
                            f"the spec's ratio")
    notes.append("static six-axis bracket: " + extra["exec-static"][2:])
    notes.append("formation six-axis bracket: " + extra["exec-form"][2:])
    notes.append("T2 executed ratio: " + extra["exec-T2-405"][2:])
    notes.append("INFO " + t2_proof_step_info())
    return extra, notes


def main():
    note = show(NOTE)
    cache = show(CACHE).split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    cache_lines = cache.splitlines()
    runner_src = norm(show(RUNNER))
    declared = section(note, "Premises and declared objects")
    other = {p: show(p) for p in OTHER}
    secs = statement_sections(note)
    covered = {name: set() for name, _ in secs}
    counts = {k: 0 for k in ("CACHE", "RUNNER", "DERIVED", "DEFINITION", "EXCLUDED", "HIT")}
    hits = []
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(cache_lines)} stdout lines; statement sections: {', '.join(n for n, _ in secs)}")
    for item in ITEMS:
        iid, pat, kind, src, role = item[:5]
        other_pat = item[5] if len(item) > 5 else src
        where = []
        for name, text in secs:
            for m in re.finditer(pat, text):
                where.append(name)
                covered[name].update(range(m.start(), m.end()))
        if not where:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            continue
        loc = ",".join(sorted(set(where), key=lambda s: (s != "claim_scope", s)))
        if kind == "EXCLUDED":
            counts["EXCLUDED"] += 1
            print(f"[EXCLUDED] {iid} | {loc} | {src}")
        elif kind == "DEFINITION":
            ok = src == "inline" or re.search(src, declared) is not None
            counts["DEFINITION" if ok else "HIT"] += 1
            if ok:
                print(f"[DEFINITION] {iid} | {loc} | {role} | {'inline in the statement' if src == 'inline' else 'declared under Premises and declared objects'}")
            else:
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | definition not found among the declared objects"))
        elif kind == "DERIVED":
            fn, locate = src
            ok, txt = fn()
            found = re.search(locate, norm(note)) is not None
            if ok and found:
                counts["DERIVED"] += 1
                print(f"[DERIVED] {iid} | {loc} | {role} | {txt}")
            else:
                counts["HIT"] += 1
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | derivation {'FAILED: ' + txt if not ok else 'not located in the note'}"))
        else:
            lines = [(i + 1, l) for i, l in enumerate(cache_lines) if re.search(src, l)]
            if lines:
                counts["CACHE"] += 1
                i, l = lines[0]
                print(f"[CACHE] {iid} | {loc} | {role} | cache stdout line {i}: {l.strip()[:140]}")
            else:
                counts["HIT"] += 1
                elsewhere = []
                for p, txt in other.items():
                    js = [j + 1 for j, l in enumerate(txt.splitlines()) if re.search(other_pat, l)]
                    if js:
                        elsewhere.append(f"{p.split('/')[-1]} lines {','.join(map(str, js[:6]))}{'...' if len(js) > 6 else ''}")
                in_src = re.search(src, runner_src) is not None
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | not printed by the runner (cache), no derivation in this note"
                             + ("; present in the runner source only" if in_src else "")
                             + (f"; printed by {', '.join(elsewhere)}" if elsewhere else "; printed by no other file of the PR")))
    unc, ntok = [], 0
    for name, text in secs:
        for a, b, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a, b)):
                unc.append((name, v, text[max(0, a - 40):b + 30].replace("\n", " ")))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    extra, notes = control_checks()
    for n in notes:
        print(f"[CONTROL] {n}")
    for iid, h in hits:
        print(h + extra.get(iid, ""))
    claimed = [i for i, _ in hits if not i.startswith("exec-")]
    execd = [i for i, _ in hits if i.startswith("exec-")]
    mism = sorted({i for i, _ in hits if "MISMATCH" in extra.get(i, "")})
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    print(f"SUMMARY: {len(ITEMS)} items over claim_scope + {len(secs) - 1} theorem sections ({ntok} numeric tokens, {len(unc)} uncovered): "
          f"cache-sourced {counts['CACHE']}, derived here from the note's formulas {counts['DERIVED']}, definitions {counts['DEFINITION']}, "
          f"excluded {counts['EXCLUDED']}; unsourced {counts['HIT']} = {len(claimed)} in the proved statements ({', '.join(claimed) or 'none'}) + "
          f"{len(execd)} executed-not-claimed numbers printed only by controls; stated values disagreeing with the control output: "
          f"{', '.join(mism) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
