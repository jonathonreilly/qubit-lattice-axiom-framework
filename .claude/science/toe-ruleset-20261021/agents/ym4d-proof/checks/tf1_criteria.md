# tf1 — pre-registered criteria for the τ_♭ binding-entry adjudication

Written **after** TAUFLAT.md §0 (PRE-STATED) was on disk and **before** `checks/tf1_tau.py` existed.
Timestamp of this file: see its mtime. I state the order rather than a hand-typed clock reading, because
two workers in this session forward-dated a header and had to disclose it.

## 0. The rule this file obeys, and how

The binding process rule is: *a criteria file may contain NO constant derived in the same session.*

**This file therefore contains no numeric constant at all.** Not one. Every quantity below is a symbol,
and the script's first action is to **transcribe** each symbol's value from the owning file with a
file+line citation, printing the transcription table before any verdict. The only numbers I register here
are the **decision thresholds of the verdicts themselves** (ten; one-point-two; two), which are mine,
invented at the moment of writing, and derived from nothing.

This also fixes what the check can and cannot establish: it is an **arithmetic-consistency** check between
two transcriptions. It does not validate any transcribed constant, and a PASS is not an endorsement of
any source file.

## 1. The symbols, and where each is transcribed from

| symbol | meaning | owning file to transcribe from |
|---|---|---|
| C′ | FORCE's amplification constant | SQ.md, Lemma FORCE |
| c_♭ | DESC's energy coefficient | SQ.md, Lemma DESC (a) |
| τ_R | the (REG-min) corollary's threshold | REVIEW_SQ_S4 S4-14 |
| C_err(C_D) | SUP-price's error constant as a function of C_D | REVIEW_SQ_S4 S4-16 |
| θ_0^SUP | 1/(2·C_err), SUP-price's own θ_0 | SQ.md Theorem SUP-price + REVIEW_SQ_S4 S4-16 |
| C_D(C_T) | C_D as an output of EPS-T | REVIEW_SQ_S4 S4-16 |
| C_T | the Moser constant this chain now carries | EPSSTAR.md §7.1 |
| ε_1 | RLARGE's small-field cut, at its current ceiling | RLARGE.md §0 |
| η_AE | AE-red's own energy threshold | REVIEW_HIST_S4 |
| C_3 | A5's energy coefficient (unknown; reference value only) | HIST.md Theorem A5 |

τ_♭ and η_♭ are **not** transcribed: they are the quantities in dispute and the script computes them from
their definitions in SQ.md Corollary DESC-ε, under each candidate binding entry separately.

## 2. The pre-registered verdicts

**TF1-A (the symbol-identity gate — must be settled by READING, before any arithmetic is believed).**
I will record, from the owning files, whether the two occurrences of θ_0 inside τ_♭'s and τ_R's defining
minima are the SAME symbol or two different symbols, and likewise whether the ε_1 in HIST's A5 clause is
the same ε_1 as RLARGE's small-field cut.
- **DISSOLVED** if τ_♭'s θ_0 entry and τ_R's θ_0 entry are the same symbol and the apparent conflict is a
  double-count of one constraint, or if the two ε_1 are different symbols. The whole finding is then WRONG
  and nothing below matters.
- **DISTINCT-AND-BOTH-BIND** if they are different symbols and both appear in the min that defines τ_♭.
  Only then do TF1-B..E mean anything.

**TF1-B (is the conflict real).** Compute η_♭ twice from SQ.md's definition η_♭ = c_♭·τ_♭²/C′², once with
τ_♭ taken at the entry τ_R and once with τ_♭ taken at the entry θ_0^SUP/C′ evaluated at the chain's
current C_D.
- **CONFLICT-REAL** if the two values differ by **at least ten decades**.
- **CONFLICT-ABSENT** if they differ by less than ten decades.

**TF1-C (the consistency window).** Compute the exact largest C_D for which τ_R ≤ θ_0^SUP/C′, i.e. the
window in which the two items of the review are jointly consistent. Report it exactly. Verdict: whether
the chain's current C_D lies inside or outside that window.

**TF1-D (the DESC-ε clause).** Evaluate the clause η_♭ ≥ 4·C_3·ε_1² at the chain's current C_D, at the
reference C_3, with ε_1 at RLARGE's current ceiling.
- **CLAUSE-HOLDS** or **CLAUSE-FAILS**, with the shortfall reported in decades of energy and in decades
  of ε_1. A FAIL is reported as a FAIL.

**TF1-E (the repair bar, and a check on the source's own arithmetic).** Compute, exactly, (a) the t_pr the
clause requires, (b) the implied ceiling on C_D, (c) the implied ceiling on C_T. Then compare each with
the corresponding figure stated in EPSSTAR §6.6, which the script transcribes.
- **SOURCE-REPRODUCED** if each of my three agrees with EPSSTAR's to within a factor of **one-point-two**.
- **SOURCE-DISAGREES** otherwise, in which case I report my value, EPSSTAR's value, the exact ratio, and
  the direction — whether the correction makes the reported failure better or worse. A disagreement is
  **not** grounds for discarding either; it is reported.

**TF1-F (the AE-red comparison).** Evaluate AE-red's own clause 4·C_3·ε_1² ≤ η_AE at the same ε_1 and C_3.
- **AE-CLAUSE-HOLDS** or **AE-CLAUSE-FAILS**, with the margin in decades. This is the quantity that
  decides whether the alternative route's *number* is alive, as distinct from its *status*.

## 3. The power check (this is mandatory, and it decides whether any PASS above counts)

Three findings in this session were that a verification gate lacked the power to fail: a literal
tautology, a gate built from its object's own primitives, and an abelian model vacuous for a nonabelian
claim. So, pre-registered **before** the script exists:

**TF1-G (designed counterfactual).** The script must re-run TF1-B and TF1-D with one single input
substituted — C_D set to a value **inside** the TF1-C window instead of the chain's current value — and
must then return **CONFLICT-ABSENT** and **CLAUSE-HOLDS**. Nothing else may be changed.
- If the counterfactual returns the same verdicts as the main run, **the check has no power to fail and I
  will report it as having no power, not as a PASS**, and the adjudication will rest on the reading alone.
- The counterfactual value is chosen by the script as the TF1-C window boundary divided by two, so it is
  not a number I pick here.

**TF1-H (precision).** Every decade comparison is computed in exact `fractions.Fraction`; `Decimal` is
used only to display. The script asserts that the exact and the displayed verdicts agree at two different
`Decimal` precisions. Any disagreement is a FAIL of TF1-H.

**What this check still cannot do, stated in advance:** it cannot detect an error in SQ.md's derivation of
η_♭, in REVIEW_SQ_S4's C_err model, in EPSSTAR's C_T, or in RLARGE's ε_1 ceiling. It compares
transcriptions. The load-bearing question (TAUFLAT §0.2) is **not** a numeric question and no script here
bears on it; it is decided by the statuses quoted from the owning files.

## 4. Provenance

Order asserted: TAUFLAT.md §0 → this file → `checks/tf1_tau.py` → `checks/tf1_out.txt`. Verifiable by
mtime. No constant in §1-§3 above was computed by me or by any session-24 file; §1 names only where each
will be read from. Plain `python3 -I`, single thread, no numpy, no BLAS, no numeric lock (exact rational
arithmetic only).
