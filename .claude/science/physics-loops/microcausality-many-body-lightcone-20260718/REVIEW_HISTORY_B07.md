# Review history — block07 (weighted quasilocal-class walk-expansion LR bound)

## Round 0 — workhorse worker grading (supervisor, 2026-07-18)

Worker seat: Opus 4.8 max effort (owner-directed substitution under the
workhorse skill, disclosed in both specs). Ground truth derived and
recorded in BLOCK07_PLAN.md BEFORE reading worker output.

**Worker B (math build, `worker_b07_math_analysis.md`): graded CORRECT
on every load-bearing item.** Chain lemma and weight split match the
ground truth verbatim; the back-to-front peeling (its U_j tails) is the
ground-truth contraction in equivalent form, with the |S|-fuel
bookkeeping made explicit ("the |S_j| handed up reconstituted w*");
final display identical (c = 2, sharp prefactor n_X^w/kappa, coarse
|X|, v = 2 kappa/mu); consistency reduction kappa_bond = 12 J e^mu and
the 6/5 ratio match, PLUS worker-added value adopted: the exact slack
ladder 12 -> 11 -> 10 (union double-count of self; sibling self-drop);
instance closed forms match (kappa_3D simplified numerator 2 rho(3 +
rho^2) — verified against the independently computed kappa(1/3) =
14 J0; worked sample 684 J0 verified). Its LIMITS L1-L12 are the right
caveats; the two supervisor verifications it requested check out: (L2)
the siblings deliver CONSECUTIVE overlap (their per-term re-derivation
— the family's own walk-vs-accumulated-support distinction), and (L7)
the sibling rate is 2 x 10 J e^mu exactly as reconstructed.

**Worker A (scout, `worker_b07_scout_analysis.md`): graded CORRECT
with all load-bearing quotes verified against the sources** (one
apparent miss was a line-wrap; the whitespace-normalized needle
matches). Its three decisive contributions, all adopted: (i) the
overlap honesty flags — the free-bilinear note ALREADY proves the
U = 1 pair-support instance (B1 + B2), so block07's delta must be and
is scoped to arbitrary |S|, the family form, the fermionic lift, and
the disposition layer; (ii) the metric convention key (the landed
notes disagree; this note declares ambient l1 once); (iii) the
disposition that the exp-decay note's reproducing no-go binds the
reproducing METHOD only — the single most important disambiguation in
the packet, now a gated, needled section of the note. Its LIMITS were
honest (the general-|S| claim was a conjecture pending the math
worker; worker B's Section 3 closed it, graded against ground truth).

Supervisor self-audit of the central disposition (recorded before the
lens round): the reproducing ratio requires a two-point convolution;
this route extracts e^{-mu d} once per chain via the chain lemma and
then sums only the single-center activity kappa per step — no
convolution of two-point decay functions is ever formed. Structural,
not cosmetic.

## Round 1 — combined adversarial lens (codex, read-only; cross-family
independence from the Opus workers), 2026-07-18

Spec: `lens_b07_spec.md`. Output: `lens_b07_out.txt`. Verdict as
issued: mathematical core survives ("salvageable BOUNDED"); claim
scope and several gates FAIL as written. The lens ran its OWN
exhaustive enumeration (all 31 subsets of a five-site segment,
disconnected included, 6,100 chains at k = 3) and the peeling passed —
and it confirmed the central reproducing-no-go disposition as
"genuinely non-binding" after explicit attack. Dispositions:

### Majors (4), all ACCEPTED and repaired

1. **Bond-class equality false** (`κ = 12Je^μ` asserted where only
   `≤` holds; a single-bond family gives `2Je^μ`). Repaired to the
   worst-case-envelope statement with the saturated bulk model
   attaining equality (gated: enumerated 6 incident bonds), the
   single-bond counter-instance gated, and "exactly 6/5" requalified
   as the envelope ratio.
2. **Delta overstated; pair map missed a factor two.** The exp-decay
   note's many-body theorem already covers arbitrary finite supports
   (in its polynomial-corrected weight) — the uniqueness claims
   ("arbitrary size is new", "family form is new") were removed; the
   honest delta is the hypothesis form (site-summed |S|-weighted
   PURE-exponential activity) and its output, plus the even-CAR
   formulation and the disposition layer. The free-bilinear map is
   `κ = 2W_mu` (not `W_mu`); corrected — and the corrected map makes
   the rates agree exactly (`2κ = 4W_mu`), a stronger consistency
   check than the wrong version.
3. **`κ = 0` division.** `κ > 0` added to the hypotheses (trivial case
   excluded by convention, as in the siblings).
4. **Runner gates weaker than advertised.** All repaired: the trivial
   reconstitution check replaced by the honest inductive-step gate
   plus the new ALL-SUBSETS exhaustive peeling gate (Q4b — the lens's
   own strongest check, implemented natively: 31 supports including
   disconnected, chains k = 1..3, exact sums vs the bound); the
   envelope gates replace the false-equality gate; the `Σ r² ρ^r`
   telescoping identity added; N4/N4b now read both sibling files
   with their own needles; the order-one gate relabeled as the
   majorant coefficient; Q11 added (mixed-size tensor reduction with
   a three-site term).

### Additional review outcomes

- **Connectedness retired** (lens: "irrelevant — the proof never uses
  it"; my own CAR example was itself a disconnected support — real
  inconsistency caught). The class is now all finite nonempty
  supports; Non-Claims updated (disconnected supports ARE covered).
- **Volume-uniformity clarified**: constants depend on `Λ` only
  through the supplied `κ`.
- **N1-N8 rebuilt** around the lens's own attack list (each ATTEMPTED
  with outcome); the wall list corrected (gauged-kernel is a subcase
  of transfer instantiation; `μ`-optimization under sharp constants).
- Minors: strictness needs `w* > 0` (added); odd-odd velocity caveat
  repeated in the theorem; sphere-count wording fixed.

### Lens-confirmed survivals (for the record)

Chain lemma (stronger than stated — connectedness-free); weight
split; peeling with contact-multiplicity covered; start factor;
assembly constants and resummation; the central disposition; all
instance arithmetic (`4r²+2`, both closed forms, values 14/684/4);
the fermionic lift's algebra; scope hygiene including worker
disclosure.

### Post-repair state

Runner 20/0 under the ordered label manifest (Q1-Q11 + needles).
Battery: 13 probes flipping exactly their targets (two probe designs
were themselves repaired mid-battery: one had tried to refute the
theorem by changing weights — impossible for a true theorem — and one
mutated an insensitive direction; both replaced with assertion-level
probes).
