# Review history — d-dim action-level many-body transfer identity

## Round 0 — workhorse worker grading (two Opus 4.8 max workers)

Ground truth recorded in PLAN.md before reading either deliverable.

- **Scout (10 sections): CORRECT on every extraction**, three catches
  adopted: (1) block11's note is ABSENT on this branch (cut from
  origin/main; PR #5547 unmerged) — the new note cites landed
  authorities only and block11 appears only in the PR body as the
  consumer; (2) "corner" is overloaded (DISP taste corners vs the
  corner-note's three generation channels) — the note says "taste
  corner" exclusively for DISP's r and cites the corner note only for
  the abstract finite-mode functor; (3) a_tau is three-valued across
  sources (RP symbolic, DISP absent, CORNER = 1) — carried explicitly
  with a_tau = 1 as the reconciling default. Also: the dispersion
  note has NO (0,1] statement, NO projectors, NO coherent kernel, NO
  Gamma at general d (its runner builds none of them) — the gap list
  confirms the item is a genuinely un-built bridge.
- **Math (6 items): CORRECT on every derivation**, sharpenings
  adopted: (1) S(k)^2 = (sum sin^2) * I is SCALAR x I (stronger than
  the plan's "diagonal"; the worker refused to force the weaker
  wording — this is the collapse mechanism and the taste-degeneracy
  source); (2) per-k block dimension 2^{d+1}, eigenvalues e^{+-2E_d}
  each multiplicity 2^d (worker's honest assembly, gate-verified not
  DISP-quoted — LIMITS L10); (3) the d-blind/d-dependent split: the
  forward-selection sentence is dimension-blind; the FURNISHING of
  the 2x2 blocks (Clifford step) is where d enters; (4) C = 1 pinned
  by the coherent kernel's constant term AND tied to CORNER (ii)
  vacuum-fixing — with the counterexample-based Gate F because
  DEGENERATE Fock gates cannot discriminate the pin (W commutes at
  full degeneracy); (5) bridge status (LIMITS L2): the d-dim
  identity has the SAME three supplied bridge parts as the landed
  d = 1 note (selection, coherent-exterior, functor) — parity, not
  weakening; only the Clifford step is d-dependent; (6) sign
  convention fork (L3) routed through n / 1-n kernels, inert.

Supervisor verification beyond the workers: the L = 2 degeneracy
(H_hop = 0 identically since tau_+ = tau_- at L = 2) checked by
hand; the position-space H_hop^2 spectrum at d = 2, L = 4
({0 x4, -1 x8, -2 x4}) computed independently as the
position<->momentum faithfulness gate; minimal-polynomial +
trace route chosen over symbolic 8x8 eigendecomposition for A2.

## Round 1 — combined adversarial lens (codex, cross-family)

Spec: `lens_spec.md`. Output: `lens_out.txt`. One BLOCKER, two
MAJORs, five MINORs — all repaired:

1. **BLOCKER: "C = 1 derived from the action" over-claim.** The RP
   note's coherent-kernel sentence is CONDITIONAL ("For a one-mode
   coherent-state kernel..."); the exponential form is supplied, not
   action-derived, at every d including the landed d = 1. ACCEPTED:
   rescoped everywhere to "C = 1 pinned RELATIVE TO the supplied
   kernel form" (given the form, the constant term excludes the
   Gaussian scalar); "action-level" now DEFINED in the claim scope
   as the landed 1+1d bridge status (three supplied parts: selection
   prescription, kernel form, functor); Purpose/Results/N3/N5/N7/
   Non-Claims all updated; G6 relabeled "GIVEN the supplied form".
2. **MAJOR: finite-norm selection is a prescription.** On finite
   time extent both reciprocal solutions are finite; the
   stable-half-line prescription is supplied (same as d = 1).
   ACCEPTED: stated as such in claim scope, Results, N3, steelman.
3. **MAJOR: JW-sign discrimination absent.** For diagonal Gamma the
   intertwiner is sign-convention-blind (both sides carry the same
   sign; all-signs-+1 passes). ACCEPTED: G7 gains genuine CAR
   anticommutator gates ({a_i, a_j^dag} = delta_ij,
   {a_i^dag, a_j^dag} = 0, all pairs) which DO discriminate signs
   (battery probe 15: signs stripped -> CAR fails); G7/G8 labels
   rewritten honestly; note Verification updated.
4. **MINOR: G9 multiplicativity conjunct near-tautological.**
   ACCEPTED: relabeled "inherits multiplicativity by conjugation
   (instance-checked; abstract argument is the corner note's)".
5. **MINOR: sign-eigenspace merge at lambda = 0.** ACCEPTED:
   parenthetical added (conclusions unaffected, lens agrees).
6. **MINOR: mixed a_tau displays.** ACCEPTED: all displays at
   a_tau = 1; no general-a_tau display claimed; the RP note's own
   glyph tension noted as reconciled at a_tau = 1.
7. **MINOR: common-L undefined.** ACCEPTED: general-period count
   prod(L_mu/2) 2^d = prod L_mu stated (hypercubic instance kept);
   gated symbolically in G1.
8. **MINOR: "battery flips each gate" wording.** ACCEPTED: N2 now
   says the battery is the loop-pack's supervisor-run probe set,
   not an in-runner hypothesis sweep.

Lens-confirmed survivals: per-k algebra, Hermiticity, det/trace,
e^{+-2E_d} spectrum, multiplicity arithmetic, strict split at
p = 0, G2/G3 momentum counts.

## Post-repair state (round 1)

Runner 14/0 (G1-G9 + N1-N5 under the ordered manifest, CAR gates
included). Battery 16/16 from the final runner (incl. probe 15
JW-sign strip caught by CAR; probe 16 CAR-expectation attack;
probe 14 silent gate deletion vs manifest).

## Round 2 — review-loop (2026-07-24, PR #5549, codex GPT-5.6-Sol xhigh reviewer seat + independent operator recomputation)

The round-1 repair was NOT sufficient. Round 2 returned
CODE_RUNNER FAIL, PROOF_OBLIGATIONS EQUIVALENT-GAP,
NO_GO_DISCIPLINE FAIL, IMPORTS_SUPPORT DEMOTE. Findings accepted
and repaired before landing:

1. **BLOCKER (central).** "Supplies the operator identification the
   corner-note names as an unsupplied prerequisite" is CIRCULAR.
   Specifying the one-mode coherent kernel as exp(zbar' lambda z)
   IS the coherent-state form of the identification
   T = diag(1, lambda); supplying it mode-by-mode plus factorization
   SUPPLIES the identification rather than deriving it. The note
   relocates the conditional from d = 1 to general d. Independently
   corroborated by the live ledger: the d = 1 anchor
   `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`
   is `audited_failed` (2026-07-21) on exactly this leg, with the
   audit naming the identification "target-equivalent" and setting
   the repair target as an explicit two-slice Berezin derivation of
   the kernel, residue, normalization, CAR metric, and reflected
   inner product. REPAIRED: claim split into grade (A) derived
   classical algebra and grade (B) conditional Fock assembly; the
   discharge claim RETRACTED in claim_scope, Purpose, Results,
   N4/N5/N6/N7/N8, Non-Claims, and the runner's N3 gate label.
2. **BLOCKER.** Three residual round-1 leftovers: "derives the full
   many-body two-step identity from the staggered action" (Purpose),
   "with C = 1 derived" (Theorem), "it does not infer -- it derives"
   (N8). All three RETRACTED in place.
3. **BLOCKER.** Gate labels G2/G7/G8 advertised d = 2 / d = 3
   coverage they do not have (H_hop vanishes identically at L = 2;
   G7/G8 are generic exterior-algebra bookkeeping in a free symbolic
   t). RELABELLED "SUPPORT-ONLY ... carries NO d-dimensional
   content", and the note's Verification now states per-gate
   coverage explicitly, including that NO gate composes the
   grade-(A) algebra with the Fock construction.
4. **NARROW.** "The fermionic structure is pinned by the separate
   CAR gate" over-claimed. The CAR gates verify only that the
   runner's own Jordan-Wigner matrices satisfy the CAR. Reworded in
   the note and in the G7 label.
5. **NARROW.** G6's "C != 1 rejector" and G9's multiplicativity
   conjunct are true-by-construction bookkeeping, not independent
   oracles. Both labels corrected.
6. **NARROW.** The +-lambda multiplicity-2^{d-1} step needs
   tr S = 0, which was asserted without reason. Reason supplied
   (Gamma_mu = -Gamma_nu Gamma_mu Gamma_nu, trace cyclic), and the
   multiplicity conclusion restructured to rest only on the
   separable minimal polynomial plus the full-block trace, which
   need neither tr S = 0 nor an eigendecomposition.
7. **BLOCKER.** The self-asserted No-Go "Status: PASS" was a
   closure certificate the battery does not earn (N7 concedes an
   unclosed target-equivalent objection). Replaced with an explicit
   no-closure statement; steelman item (b') added as CONCEDED.
8. **BLOCKER (governance).** `lens_out.txt` (1.2 MB raw reviewer
   transcript, machine-local paths, trailing whitespace failing
   `git diff --check`; no precedent on main, where the largest
   loop-pack file is 29 KB) STRIPPED from the landing. The
   retracted wording in `CLUSTER_CAP_EVALUATION.md` carries a dated
   retraction block rather than being silently deleted.
9. **REJECTED finding.** The reviewer called the `G1`..`G9` /
   `N1`..`N5` gate labels a controlled-vocabulary violation. Not
   upheld: 58 landed runners and 6 landed caches use exactly this
   `G<n> <explicit scientific description>` shape, which is the
   permitted "shorthand as alias" pattern, not a bare science name.

Operator-side independent recomputation (not shared with the
runner's implementation path): a separate Kronecker-product
construction of the corner algebra confirms Gamma_mu^2 = I,
Hermiticity, tracelessness and anticommutation at d = 1..5 and
S(k)^2 = (sum sin^2)I for random integer coefficients; the block
display, det = 1, tr = 2^d(2+4R), spectrum e^{+-2E_d} with
multiplicity 2^d and the minimal polynomial all reproduce at
GENERIC k for d = 1..4 (the runner gates only d = 2 at two special
k); the G3 charpoly lam^4 (lam+1)^8 (lam+2)^4 reproduces from a
pure momentum count, and an unstaggered control gives a DIFFERENT
spectrum, so G3 does exercise the phases; H_hop = 0 at L = 2 is
confirmed for d = 2, 3; and the intertwiner is confirmed to pass
for sign-free raising operators while the CAR gate fails for them.

## Round 2 confirmation pass

The reviewer's confirmation round returned LAND-WITH-NAMED-FIXES
(CODE_RUNNER RISK, PHYSICS_CLAIM_BOUNDARY BOUNDED, PROOF_OBLIGATIONS
CONDITIONAL, IMPORTS_SUPPORT DISCLOSED, NATURE_RETENTION BOUNDED,
NO_GO_DISCIPLINE PASS, LABELING_CONVENTION PASS, REPO_GOVERNANCE FIX,
AUDIT_COMPATIBILITY PASS), confirming that the grade split is honest
(nothing in grade (A) uses either supplied input) and that
`bounded_theorem` is defensible under the narrowed scope. Four named
fixes, all applied:

- **Loop-pack retraction hygiene.** `CLUSTER_CAP_EVALUATION.md`'s
  "the free case is complete and gate-able now" reworded to name the
  CLASSICAL algebra only; dated SUPERSEDED banners added to
  `PLAN.md`, `worker_b_math_spec.md`, and `worker_b_math_report.md`
  (the last two carried "the kernel DERIVES the overall
  normalization" and "supplied by the action"). Files preserved
  unedited below the banners as provenance; the directory is NOT
  stripped (loop packs are precedented: 127 directories / 1289 files
  on main).
- **The anti-drift claim was not true as written.** The N5 needles
  are presence-only, so restoring a retracted sentence elsewhere
  would still have passed. A real ABSENCE gate `N6` was added over
  the note's live claim surface (YAML `claim_scope` + all body
  sections except the N5 rhetoric-audit bullet, whose exclusion ends
  at the next list item or heading). Mutation-probed: all eight
  retracted phrases injected into the live Results section trip the
  gate; the same phrases inside the excluded historical bullet do
  not; and a new live list item placed immediately after that bullet
  IS caught, so the exclusion is not an escape hatch.
- **G7 "all pairs" was literally false** — `{a_i^dag, a_j^dag} = 0`
  was checked only for `i < j`. The `i = j` (nilpotency) case is now
  checked and the label says "all ordered pairs INCLUDING i = j".
- **Malformed Round-2 heading** in this file repaired.

## Post-repair state (round 2)

Runner 15/0 (G1-G9 + N1-N6 under the ordered manifest) with the
corrected labels, the N5 self-pin needles rewritten to pin the
RETRACTED-claim boundary, and the N6 absence gate making a silent
restoration of "supplies the prerequisite" or "C = 1 derived" fail
the runner.
