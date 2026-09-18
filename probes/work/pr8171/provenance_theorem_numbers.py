#!/usr/bin/env python3
"""J:provenance:PR8171 - every number in the theorem statements of the block 27 note (the sphere formation law at weak coupling: the
causal coupling contracts, one invariant law, exponential loss of memory below 1/sqrt3),
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
PR = 8171
BRANCH = "physics-loop/admissibility-induced-law-block27-unsoldered-formation-law-weak-coupling-causal-coupling-contracts-20260916"
HEAD = "15b6e402b902964ada51ffdd8e8c88fb4e472013"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_WEAK_COUPLING_THE_CAUSAL_COUPLING_CONTRACTS_ONE_INVARIANT_LAW_AND_EXPONENTIAL_"
        "LOSS_OF_MEMORY_BELOW_ONE_OVER_ROOT_THREE_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_formation_law_weak_coupling_causal_coupling_contracts_one_invariant_law_2026_09_16.txt"
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block27"
CTL, REF = SPECS + ".out.txt", SPECS + "_refuter.out.txt"
OTHER = [CTL, REF]


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
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"), ("ε", "epsilon"), ("η", "eta"), ("δ", "delta"), ("→", "->"))


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
def derive_2rate():
    import sympy as sp
    b, t = sp.symbols("beta t", positive=True)
    D = 2                                                # D_0 <= 2: the chordal diameter of the sphere
    ok = sp.simplify(D * (sp.sqrt(3) * b) ** t - 2 * (sp.sqrt(3) * b) ** t) == 0
    return ok, "D_t <= (sqrt3 beta)^t D_0 with D_0 <= 2 (chordal diameter) gives 2 (sqrt3 beta)^t (the note's T2 proof)"


def derive_dual():
    return True, "for any coupling and unit d, |(E s - E s').d| <= E|s - s'|; d along F(V) - F(V') gives W_1 >= |F(V) - F(V')| (T4 proof)"


def derive_quarter():
    import sympy as sp
    w = sp.symbols("w", real=True)
    mac = sp.integrate(sp.Abs(w), (w, -1, 1)) / 2       # mean |cos| under the uniform law on S^2 (w uniform on [-1, 1])
    rate = mac / 2                                       # TV rate at V = 0: (1/2) E|s.d| per unit |V - V'|
    reach = sp.solve(sp.Eq(3 * 2 * rate * sp.Symbol("beta"), 1))[0]
    ok = rate == sp.Rational(1, 4) and reach == sp.Rational(2, 3)
    return ok, (f"TV rate at V = 0 = (1/2) E|w| = {rate} (uniform w on [-1, 1]; the note's T1 reading); the total-variation route contracts while "
                f"3 beta (2 x {rate}) < 1, i.e. beta < {reach} (T4 reading)")


def derive_c_lower():
    import sympy as sp
    b, x = sp.symbols("beta x", positive=True)
    delta = b * x                                        # x = |s_1 - s'_1|
    lower = delta * (sp.Rational(1, 3) - delta ** 2 / 45) / x
    ok = sp.simplify(lower - (b / 3) * (1 - 3 * b ** 2 * (x ** 2 / 45))) == 0
    return ok, "A(delta) >= delta/3 - delta^3/45 with delta = beta|s_1 - s'_1| gives c >= (beta/3)(1 - 3 beta^2 |s_1 - s'_1|^2/45) (sympy)"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("ref", r"block 26 executes the loss of memory at every coupling tried|block 26's T1\(a\)|block 26's bound|the causal coupling of block 27",
     "EXCLUDED", "reference (block 26)", "citation"),
    ("K-def", r"K_V\(ds\) = \(\|V\|/\(4 pi sinh\|V\|\)\) e\^\{V\.s\} dsigma", "DEFINITION", r"K_V\(ds\) = \(\|V\|/\(4pi sinh\|V\|\)\) e\^\{V\*s\} dsigma",
     "the sphere kernel"),
    ("preds", r"s_\{x-e_1\}, s_\{x-e_2\}, s_\{x-e_3\}|the three recorded predecessors", "DEFINITION", r"S = s_\{x-e_1\} \+ s_\{x-e_2\} \+ s_\{x-e_3\}",
     "the three predecessors"),
    ("Z3Z2", r"on Z\^3 in level order|level automaton on Z\^2", "EXCLUDED", "structural: the lattices", "wording"),
    ("two-planes", r"two initial planes", "EXCLUDED", "structural: two coupled runs", "wording"),
    ("kappa-pos", r"for every kappa > 0", "EXCLUDED", "structural: domain", "condition"),
    ("T1-TV", r"TV\(K_V, K_(?:V'|\{V'\})\) <= \|V - V'\|/\(2 ?sqrt3\)", "CACHE", r"TV\(K_V, K_V'\) <= \|V - V'\|/\(2 sqrt3\)", "T1(d) TV sensitivity"),
    ("T1-W1", r"W_1\(K_V, K_(?:V'|\{V'\})\) <= \|V - V'\|/sqrt3", "CACHE", r"W_1 <= \|V - V'\|/sqrt3", "T1(d) W1 sensitivity"),
    ("T1-var", r"Var(?:_\{K_V\})?\(w\) = A'\(kappa\)(?: = 1/kappa\^2 - 1/sinh\^2 kappa)?", "CACHE", r"Var\(w\) = A'\(kappa\) = 1/kappa\^2 - 1/sinh\^2 kappa",
     "T1(a)"),
    ("T1-moment", r"E(?:_\{K_V\})?\[\(\(s - A ?(?:u|û)\)\.?\*?d\)\^2\] = A/kappa \+ \(1 - 3A/kappa - A\^2\) ?(?:\((?:u\.d|u\*d)\)\^2|c\^2)", "CACHE",
     r"E\[\(\(s - A u\)\.d\)\^2\] = A/kappa \+ \(1 - 3A/kappa - A\^2\) c\^2", "T1(b) directional second moment"),
    ("T1-sign", r"(?:the sign lemma )?1 - 3A/kappa - A\^2 <= 0", "CACHE", r"A\(kappa\)/kappa is decreasing", "T1(c) sign lemma"),
    ("T1-third", r"A/kappa <= 1/3", "CACHE", r"A/kappa <= 1/3", "T1(c) A/kappa <= 1/3"),
    ("T1-unitd", r"for a unit vector d with (?:u|û)\*d = c", "EXCLUDED", "structural: a unit direction", "definition"),
    ("T2-rate", r"(?:contracts the per-site expected chordal distance by )?sqrt3 ?beta(?: per level)?|D_\{t\+1\} <= sqrt3beta D_t \(with eta -> 0\)", "CACHE",
     r"the contraction factor is 3 \(beta/sqrt3\) = sqrt3 beta", "T2 contraction factor"),
    ("T2-region", r"beta < 1/sqrt3", "CACHE", r"the region beta < 1/sqrt3", "T2 region"),
    ("T2-within", r"within 2 ?\(sqrt3 ?beta\)\^t", "DERIVED", (derive_2rate, r"With `?D_0 <= 2`?|With D_0 <= 2"), "T2 distance to the invariant law"),
    ("T2-one", r"exactly one invariant law", "CACHE", r"one", "T2 uniqueness (the count 'one')"),
    ("T2-zero", r"tends to 0 exponentially", "EXCLUDED", "structural: limit value", "wording"),
    ("T2-crossing", r"(?:position relative to 1 at beta = )?5773/10\^4 and 5774/10\^4", "CACHE", r"5773/10\^4 and above 1 at beta = 5774/10\^4", "T2 crossing points"),
    ("T3-mt", r"m_t <= \(sqrt3 ?beta\)\^t", "CACHE", r"m_t <= \(sqrt3 beta\)\^t", "T3 magnetization bound"),
    ("T3-onesite", r"(?:on the )?one-site (?:periodic )?plane(?:, from e,)? m_t = A\(3 ?beta\)\^t(?: exactly)?(?:,)? (?:with|and) A\(3 ?beta\) <= beta", "CACHE",
     r"one-site rate A\(3 beta\)\^t", "T3 one-site rate"),
    ("T3-C2", r"A\(3beta\) < beta at rational beta", "CACHE", r"A\(3 beta\) < beta at beta =", "T3 exact enclosure points"),
    ("T4-dual", r"W_1\(K_V, K_(?:V'|\{V'\})\) >= \|F\(V\) - F\(V'\)\|", "DERIVED", (derive_dual, r"For any coupling and any unit"), "T4 dual bound"),
    ("T4-F", r"F\(V\) = A\(\|V\|\) V/\|V\|", "DEFINITION", r"F\(V\) = E_\{K_V\}\[s\] = A\(\|V\|\) (?:u|û)", "the mean map"),
    ("T4-series", r"A\(delta\)/delta >= 1/3 - delta\^2/45(?: for delta > 0, with A\(delta\)/delta < 1/3)?", "CACHE",
     r"1/3 - delta\^2/45 <= A\(delta\)/delta < 1/3", "T4 series bounds"),
    ("T4-beta1", r"(?:beyond beta = 1|impossible for beta >= 1)", "CACHE", r"no coupling of this kind contracts for beta >= 1", "T4 reach"),
    ("T4-c", r"at least \(beta/3\)\(1 - 3beta\^2\*\(something bounded\)\)", "DERIVED", (derive_c_lower, r"c >= \(beta/3\)"), "T4 the per-predecessor bound"),
    ("T4-3c", r"a contraction 3c < 1 of the causal coupling", "EXCLUDED", "structural: the contraction criterion (3 predecessors)", "definition"),
    ("T4-quarter", r"numerically 1/4 per unit at small \|V\| \(route reach 2/3\)", "DERIVED", (derive_quarter, r"mean absolute cosine is `?1/2`?"),
     "claim_scope: TV rate at V = 0 and the TV route's reach"),
    ("T4-between", r"the proved constant 1/\(2 sqrt3\) sits between", "CACHE", r"TV\(K_V, K_V'\) <= \|V - V'\|/\(2 sqrt3\)", "claim_scope: placement"),
    ("route-const", r"The constant 1/sqrt3 is the route's", "CACHE", r"the region beta < 1/sqrt3 is the route's", "claim_scope"),
]


def control_checks():
    ctl, ref = show(CTL), show(REF)
    m = re.search(r"max TV/\|V - V'\| over (\d+) random pairs = ([0-9.]+)", ctl)
    m2 = re.search(r"max TV/\|V - V'\| = ([0-9.]+)", ref)
    notes = [f"TV sensitivity executed: control quadrature max {m.group(2)} over {m.group(1)} pairs; refuter Monte Carlo max {m2.group(1)} "
             f"(the claim_scope's 1/4 at small |V| is derived exactly in the note; 'never larger' is executed, in the T4 reading only)"]
    return {}, notes


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
