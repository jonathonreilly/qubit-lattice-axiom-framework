#!/usr/bin/env python3
"""J:provenance:PR8158 - every number in the theorem statements of the block 24 note (unrecorded sites: the free-window and integrated-
exterior readings differ iff an unrecorded component touches two recorded sites),
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
PR = 8158
BRANCH = "physics-loop/admissibility-induced-law-block24-unrecorded-sites-free-window-versus-integrated-exterior-20260915"
HEAD = "dd78e677ba6cda496d6de20cfc215ef8bd09374f"
NOTE = ("docs/ADMISSIBILITY_RULE_UNRECORDED_SITES_FREE_WINDOW_VERSUS_INTEGRATED_EXTERIOR_READINGS_DIFFER_IFF_AN_UNRECORDED_COMPONENT_TOUCHES_"
        "TWO_RECORDED_SITES_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.txt"
OTHER = []


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
def derive_phi2_entries():
    import sympy as sp
    p, q, r = sp.symbols("p q r", positive=True)
    S = p ** 2 + q ** 2 + 4 * r ** 2          # sum_u phi(v,u)^2
    A = 2 * p * q + 4 * r ** 2                 # sum_u phi(v,u) phi(u,-v)
    O = 2 * r * (p + q) + 2 * r ** 2           # sum_u phi(v,u) phi(u,w), w perp v
    ok = sp.expand(S - O - ((p - r) ** 2 + (q - r) ** 2)) == 0 and sp.expand(A - O - 2 * (p - r) * (q - r)) == 0
    # sector eigenvalues of phi^2 from its relation entries: lambda0 = S + A + 4O, lambda_odd = S - A, lambda_even = S + A - 2O
    Z1 = p + q + 4 * r
    ok = ok and sp.expand(S + A + 4 * O - Z1 ** 2) == 0 and sp.expand(S - A - (p - q) ** 2) == 0 and sp.expand(S + A - 2 * O - (p + q - 2 * r) ** 2) == 0
    return ok, "phi^2 entries S, A, O summed over the six middle values; S - O, A - O and the sector eigenvalues Z1^2, (p-q)^2, (p+q-2r)^2 (sympy)"


def derive_sphere():
    import sympy as sp
    b, w, t = sp.symbols("beta w t", positive=True)
    val = 2 * sp.pi * sp.integrate(sp.exp(b * w * t), (t, -1, 1))
    ok = sp.simplify((val - 4 * sp.pi * sp.sinh(b * w) / (b * w)).rewrite(sp.exp)) == 0
    return ok, "2 pi int_{-1}^{1} e^{beta w t} dt = 4 pi sinh(beta w)/(beta w) (sympy); |v_x + v_y|^2 = 2 + 2 v_x.v_y for unit vectors"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("menu", r"phi in \{p, q, r\}|six-axis", "DEFINITION", r"p, q, r > 0|six-axis menu", "the six-axis rule"),
    ("sphere-rule", r"exp\(beta s\.s'\)", "DEFINITION", r"e\^\{beta s\*s'\}", "the sphere rule"),
    ("R-names", r"R1|R2|R3|\(Q[1-5]\)|Q[1-5]", "EXCLUDED", "labels", "labels"),
    ("Q1", r"proportional to the W-bond product times a factor F_C\(v_\{partial C\}\) for each connected component C of E, and mu_W\^R2 is the average of mu_W\^R3\(\.\|omega\) over the exterior's law",
     "CACHE", r"Q1: on the plaquette with one unrecorded site, mu_W\^R2 equals the average", "Q1"),
    ("one-rec", r"touching exactly one recorded site|touches one recorded site|touches exactly one recorded site", "CACHE", r"pendant path", "Q2 condition"),
    ("Q2-exec", r"pendant paths and exactly on a plaquette with two pendant components|pendant path of two and of three unrecorded sites, symbolically in p, q, r, is the same polynomial for all six values of v_b",
     "CACHE", r"pendant path of two and of three unrecorded sites, symbolically for all six|same polynomial in \(p, q, r\) for all six values", "Q2 executed"),
    ("two-rec", r"touching two recorded sites|two-attachment|two attachments|two single-site components|two pendant components|two recorded", "CACHE",
     r"two unrecorded corners|touching all four recorded sites", "Q3 two attachments"),
    ("phi2", r"(?:phi\^2\(v_x, v_y\) = )?Z_1\^2 P_0 \+ \(p-q\)\^2 P_odd \+ \(p\+q-2r\)\^2 P_even|\(phi\^2\)\(v_x, v_y\) = Z_1\^2 P_0 \+ \(p-q\)\^2 P_odd \+ \(p\+q-2r\)\^2 P_even",
     "DERIVED", (derive_phi2_entries, r"squaring the decomposition"), "Q3(b) phi^2 sectors"),
    ("phi2-2", r"contributes phi\^2", "DERIVED", (derive_phi2_entries, r"since `?phi`? is symmetric"), "Q3(b)"),
    ("const-iff", r"constant iff p = q = r|constant matrix if and only if p = q = r", "CACHE", r"both vanish iff p = q = r", "Q3(b) criterion"),
    ("path", r"a path of k internal bonds contributes phi\^\{k\+2\}|F_C = phi\^\{k\+2\}", "CACHE", r"phi\^\{k\+2\}", "Q3(c) path"),
    ("iso", r"constant iff both of its nontrivial isotypic eigenvalues vanish|constant iff lambda_odd = lambda_even = 0", "CACHE", r"sector eigenvalues",
     "Q3(d) criterion (E1 prints the sector eigenvalues)"),
    ("sphere", r"4 ?pi sinh\(beta\|v_x ?\+ ?v_y\|\)/\(beta\|v_x ?\+ ?v_y\|\)", "CACHE", r"4 pi sinh\(beta w\)/\(beta w\) with w = \|v_x \+ v_y\|", "Q3(e) two-attachment"),
    ("sphere1", r"4pi sinh beta/beta", "CACHE", r"4 pi sinh\(beta\)/beta", "Q3(e) one-attachment"),
    ("sphere-norm", r"\|v_x \+ v_y\|\^2 = 2 \+ 2 v_x\*v_y", "DERIVED", (derive_sphere, r"polar coordinates"), "Q3(e)"),
    ("Q4a", r"(?:TV\(R1, R2\) = )?78621/4563820 at \(3, ?1, ?2\), 675203620/64463986907 at \(5, ?2, ?4\), 221667/30063356 at \(2, ?1, ?2\)", "CACHE",
     r"78621/4563820, 675203620/64463986907, 221667/30063356 at \(3,1,2\), \(5,2,4\), \(2,1,2\)", "Q4(a) values"),
    ("Q4a-geom", r"one unrecorded site adjacent to two adjacent corners|one site adjacent to two adjacent corners", "CACHE", r"one unrecorded site on two adjacent corners",
     "Q4(a) geometry (see the falsifier log: not a window of Z^3)"),
    ("Q4b", r"(?:TV = )?9778807/1312253264 at \(3, ?1, ?2\)", "CACHE", r"9778807/1312253264 at \(3,1,2\)", "Q4(b) value"),
    ("cube", r"cube with its top face unrecorded|bottom face of the unit cube, E its top face \(a four-cycle touching all four recorded sites\)", "CACHE",
     r"the cube with its top face unrecorded \(a four-cycle touching all four recorded sites\)", "Q4(b) geometry"),
    ("Q4c", r"(?:with two pendant components TV = 0)|(?:0 at \(2, 1, 2\))|TV\(R1, R2\) = 0 exactly at \(2, 1, 2\)", "CACHE", r"TV\(R1, R2\) = 0 exactly at \(2,1,2\)", "Q4(c)"),
    ("forest", r"a pendant path of two sites off one corner and a pendant site off the opposite corner", "CACHE", r"a pendant path of two sites off one corner and a pendant site off the opposite corner",
     "Q4(c) geometry"),
    ("clause", r"separating clause pair is recorded for the owner and not adopted", "EXCLUDED", "wording", "wording"),
    ("tori", r"on tori|reading-independent", "EXCLUDED", "wording (Q5)", "wording"),
    ("exterior-sites", r"finite set E of unrecorded sites|finite set W of recorded sites", "DEFINITION", r"finite set `?W`? of recorded sites", "W, E"),
    ("B4D3", r"B4, D3|D1-D3|B1-B2|B3|C1-C2|\(E1\)|D4", "EXCLUDED", "runner check labels", "labels"),
    ("six-vals", r"all six values of v_b", "CACHE", r"all six", "Q2 executed (six attachment values)"),
    ("dC", r"dC = \{b\}|dC = \{x, y\}", "EXCLUDED", "structural: attachment sets", "notation"),
    ("any-bonds", r"through any number of bonds", "EXCLUDED", "wording", "wording"),
    ("distinct-ab", r"distinct sites a != b of C through single bonds", "EXCLUDED", "structural", "wording"),
    ("lam-odd", r"lambda_odd = \(p-q\)\^2 tau_odd and lambda_even = \(p\+q-2r\)\^2 tau_even", "DERIVED", (derive_phi2_entries, r"with `?T`? in place"),
     "Q3(d) (the same sector algebra with T in the middle)"),
    ("Q3a", r"phi = Z_1 P_0 \+ \(p - q\) P_odd \+ \(p \+ q - 2r\) P_even", "CACHE", r"eigenvalue Z1 = p \+ q \+ 4r on constants, p - q on the three odd vectors", "Q3(a)"),
    ("diffs", r"phi\^2_\{same\} - phi\^2_\{orth\} = \(p-r\)\^2 \+ \(q-r\)\^2 and phi\^2_\{anti\} - phi\^2_\{orth\} = 2\(p-r\)\(q-r\)", "CACHE",
     r"phi\^2_same - phi\^2_orth = \(p - r\)\^2 \+ \(q - r\)\^2", "Q3(b) differences"),
    ("k3", r"k <= 3", "CACHE", r"k <= 3", "Q3(c) executed range"),
    ("two-corners", r"the two unrecorded corners of a plaquette", "CACHE", r"the two unrecorded corners of a plaquette", "E1 geometry"),
    ("labels2", r"\^\{\((?:1|2|3)\)\}|Z\^\{-1\}", "EXCLUDED", "reading labels mu^(1), mu^(2), mu^(3); the normalizer Z^{-1}", "notation"),
    ("wording", r"a single unrecorded site|single-site|[Oo]ne unrecorded site|one of them|pair relation|same pair|clause pair|The two readings are two models",
     "EXCLUDED", "wording (number words naming objects)", "wording"),
    ("three-eig", r"the three eigenvalues with explicit eigenvectors", "CACHE", r"on the three odd vectors", "B1"),
    ("blocks", r"blocks? (?:0[1-9]|1[0-9]|2[0-9])(?:[-–, and]+(?:0[1-9]|1[0-9]|2[0-9]))*|\(blocks[^)]*\)", "EXCLUDED", "references to other blocks", "citation"),
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
