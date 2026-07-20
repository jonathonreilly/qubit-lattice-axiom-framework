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

## Post-repair state

Runner 14/0 (G1-G9 + N1-N5 under the ordered manifest, CAR gates
included). Battery 16/16 from the final runner (incl. probe 15
JW-sign strip caught by CAR; probe 16 CAR-expectation attack;
probe 14 silent gate deletion vs manifest).
