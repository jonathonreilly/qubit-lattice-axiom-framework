#!/usr/bin/env python3
"""J:provenance:PR8152 - every number in the theorem statements of the block 18 note (menus: neighbour-generated supports under the
unsoldered reading, cube-orbit menus under the soldered one),
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
PR = 8152
BRANCH = "physics-loop/admissibility-induced-law-block18-menus-neighbour-generated-supports-cube-orbits-20260915"
HEAD = "70f28178c47a6f5bc3666c3e2878950dc212d3f6"
NOTE = ("docs/ADMISSIBILITY_RULE_MENUS_NEIGHBOUR_GENERATED_SUPPORTS_UNSOLDERED_AND_CUBE_ORBIT_MENUS_SOLDERED_BOUNDED_THEOREM_NOTE_"
        "2026-09-15.md")
RUNNER = "scripts/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_menus_neighbour_generated_supports_and_cube_orbit_menus_2026_09_15.txt"
OTHER = [".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block18_menus.out.txt",
         ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block18_refuter.out.txt"]


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
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"), ("ε", "epsilon"), ("η", "eta"), ("δ", "delta"), ("→", "->"), ("α", "alpha"), ("γ", "gamma"),
        ("λ", "lambda"), ("↦", "->"), ("±", "+-"), ("D̄", "Dbar"), ("Ū", "Ubar"),
        ("F̄", "Fbar"), ("R̄", "Rbar"), ("μ", "mu"), ("⊥", " perp "), ("𝓔", "Ecal"), ("𝕋", "TT"), ("𝒯", "Tcal"), ("𝓒", "Ccal"), ("𝓕", "Fcal"))


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in REPL:
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


def statement_sections(note):
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", re.sub(r"\s+", " ", norm(m.group(1))))]
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        if re.match(r"(theorem|corollary|lemma|proposition)\b", title.lower()):
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            body = re.sub(r"\*{1,2}Proof\.?\*{1,2}.*?(?:∎|$)", " ", body, flags=re.S)
            body = re.split(r"\*Reading\.\*", body)[0]          # interpretation paragraphs are not statements
            out.append((title.split(" — ")[0], re.sub(r"\s+", " ", norm(body))))
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
import itertools
import sympy as sp


def cube_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = sp.zeros(3, 3)
            for i, j in enumerate(perm):
                R[i, j] = signs[i]
            if R.det() == 1:
                out.append(R)
    return out


def derive_orbits():
    O = cube_rotations()
    axis_pts = set()
    for R in O:
        if R == sp.eye(3):
            continue
        for v in (R - sp.eye(3)).nullspace():
            v = v * sp.ilcm(*[sp.fraction(x)[1] for x in v])
            g = sp.igcd(*[int(x) for x in v])
            v = tuple(int(x) // g for x in v)
            axis_pts.add(v)
            axis_pts.add(tuple(-x for x in v))
    orbits, left = [], set(axis_pts)
    while left:
        v = left.pop()
        orb = {tuple(int(x) for x in R * sp.Matrix(v)) for R in O}
        left -= orb
        stab = sum(1 for R in O if tuple(int(x) for x in R * sp.Matrix(v)) == v)
        orbits.append((len(orb), stab))
    generic = {tuple(int(x) for x in R * sp.Matrix([1, 2, 3])) for R in O}
    sizes = sorted(orbits)
    ok = (len(O) == 24 and len(axis_pts) == 26 and sizes == [(6, 4), (8, 3), (12, 2)] and len(generic) == 24
          and all(a * b == 24 for a, b in sizes) and [a for a, _ in sizes].count(6) == 1)
    return ok, ("the 24 signed permutations of det 1: axis points of the 23 non-identity rotations number 26 = 6 + 8 + 12 in three orbits with "
                "(size, stabilizer) (6,4), (8,3), (12,2); a point off the axes has orbit 24; the only orbit of size 6 is the axes, so the "
                "six-axis menu is the unique smallest nontrivial union of orbits (sympy, exact)")


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("M3sizes", "~whose sizes are 6, 8, 12 and 24", "CACHE",
     r"C1 M3: the 24 proper rotations of the cube; orbit sizes and stabilizer orders \(6,4\), \(8,3\), \(12,2\), \(24,1\)", "M3 orbit sizes"),
    ("M3orbits", "~the six axis points (stabilizer order 4), the eight cube diagonals (order 3), the twelve edge directions (order 2), and orbits "
     "of 24 points (trivial stabilizer)", "CACHE",
     r"C1 M3: the 24 proper rotations of the cube; orbit sizes and stabilizer orders \(6,4\), \(8,3\), \(12,2\), \(24,1\)", "M3 orbits and stabilizers"),
    ("M3smallest", "~the six-axis menu is the smallest nontrivial covariant menu¦The six-axis menu is the unique smallest nontrivial covariant menu",
     "DERIVED", (derive_orbits, r"with equality only for the axes"), "M3 smallest menu"),
    ("M3exec24", "~(proved; executed on the 24 rotations)¦the 24 proper signed permutations", "CACHE", r"C1 M3: the 24 proper rotations",
     "M3 executed (C1)"),
    ("M3exec5", "~the orbits and stabilizers of the five sample directions (C1)", "CACHE", r"per_site: executed .* the five sample directions",
     "M3 executed (C1, the five sample directions)"),
    ("M3exec2", "~invariance of the six-axis, eight-diagonal and twelve-edge sets and non-invariance of a mixed set (C2)", "CACHE",
     r"C2 M3: the six axes, the eight diagonals, the twelve edge directions and their unions are invariant", "M3 executed (C2)"),
    ("M1exec", "~the rational rotation about z with cosine 3/5¦moves the point (3/5, 0, 4/5) through twelve distinct positions while fixing "
     "the pole (B1)", "CACHE", r"B1 M1: a rational rotation about the pole \(cosine 3/5\) fixes the pole and moves the unit point "
     r"\(3/5, 0, 4/5\) through 12 distinct positions", "M1 executed (B1)"),
    ("M1sine", "~and sine 4/5", "RUNNER", r"c, s_ = sp\.Rational\(3, 5\), sp\.Rational\(4, 5\)", "M1's rotation sine (runner source)"),
    ("M2range", "~S_0(t) ⊂ S^2 an arbitrary subset for each angle t in (-1, 1)", "EXCLUDED",
     "structural: the inner product of two non-collinear unit vectors ranges over (-1, 1)", "domain"),
    ("M5", "~(1 + s*q)/2 equals 1 at s = q and 0 at s = -q¦the Born overlap (1 + s . q)/2 is deterministic on the antipodal menu", "CACHE",
     r"D2 M5: the Born overlap \(1 \+ s\.q\)/2 equals 1 at s = q and 0 at s = -q", "M5 (D2)"),
    ("M4exec", "~Executed: a path of five sites with the antipodal support and a symbolic seed (D1)", "CACHE",
     r"D1 M4: on a path of five with the antipodal support", "M4 executed (D1)"),
    ("words", r"one recorded neighbour|exactly one|one-neighbour case|two non-collinear recorded values|two recorded values|any two of them"
     r"|a two-valued field|two readings|the antipodal pair|SO\(3\)", "EXCLUDED", "wording, conditions and notation (number words; the group SO(3))", "wording"),
]


def control_checks():
    return {}, []


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
    def loose(p):
        if isinstance(p, str) and p.startswith("~"):
            alts = [a for a in p[1:].split("¦")]          # "¦" separates alternatives ("|" is an absolute value)
            return "|".join(r"\s*".join(re.escape(c) for c in a.replace(" ", "")) for a in alts)
        return p
    for item in ITEMS:
        iid, pat, kind, src, role = item[:5]
        pat = loose(pat)
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
        elif kind == "RUNNER":
            ok = re.search(src, show(RUNNER)) is not None
            counts["RUNNER"] += 1 if ok else 0
            counts["HIT"] += 0 if ok else 1
            if ok:
                print(f"[RUNNER] {iid} | {loc} | {role} | present and checked in the runner source (not printed)")
            else:
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | not in the runner source or its printed output"))
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
          f"cache-sourced {counts['CACHE']}, runner-checked (not printed) {counts['RUNNER']}, derived here from the note's formulas {counts['DERIVED']}, definitions {counts['DEFINITION']}, "
          f"excluded {counts['EXCLUDED']}; unsourced {counts['HIT']} = {len(claimed)} in the proved statements ({', '.join(claimed) or 'none'}) + "
          f"{len(execd)} executed-not-claimed numbers printed only by controls; stated values disagreeing with the control output: "
          f"{', '.join(mism) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
