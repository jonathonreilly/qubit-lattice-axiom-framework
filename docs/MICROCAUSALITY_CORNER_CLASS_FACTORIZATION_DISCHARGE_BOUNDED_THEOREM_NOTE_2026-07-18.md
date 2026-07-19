---
claim_id: microcausality_corner_class_factorization_discharge_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional discharge of the sibling feed's Gaussian-factorization hypothesis on the landed corner-transfer surface, plus the native rebuild of the second-quantization functorial relation that surface imports (axioms supply no dynamics; every transfer object is supplied by the cited notes on their own surfaces): (D1) the REBUILT functorial relation — for positive one-particle t on finitely many modes, the number-conserving second quantization is Gamma(t) = e^{dGamma(ln t)}, with the occupation-basis action (1, lambda_2, lambda_1, lambda_1 lambda_2, ...), the trace identity Tr Gamma(t) = det(1 + t) (gated symbolically on diagonal spectra AND on a non-diagonally-realized instance), multiplicativity Gamma(t_1)Gamma(t_2) = Gamma(t_1 t_2) (gated symbolically), and the LOG IDENTITY -log Gamma(t) = dGamma(-log t) (gated symbolically) — this retires, on the gated surface, the 'standard free-fermion functorial relation' import row carried by the cited gauge-extension engine note (needled); (D2) the composition: with the corner notes' supplied two-step kernel t = e^{-2E}, E = arcsinh(sqrt(m^2 + sin^2 p)) per channel, and the supplied many-body identity T_hat^2 = Gamma(t) (free surface, displayed there; fixed backgrounds via the engine note's definition sentence, inherited with its own provenance including its sampled-positivity table and its 'expected to survive at arbitrary spatial U' hedge, all needled), the many-body two-step log-transfer generator is EXACTLY the bilinear: -log T_hat_MB^2 = dGamma(-log t) = 2 a_tau dGamma(h[U]) at the shared convention a_tau = 1, with the generation-channel-versus-spatial decomposition bridged per channel (m <-> lambda_k on the supplied positivity domain) (silently adopted by the corner notes, symbolic in the CT note — the reconciliation is stated, and the T_hat^2 glyph clash between the notes — many-body in the corner note, one-particle in the CT note's h-definition — is disambiguated explicitly); (D3) hence the sibling feed's hypothesis T_MB[U] = C(U) Gamma(T_1[U]) holds on this surface with C = 1 (the corner note's own lambda = 1 normalization-forcing sentence is the uniqueness authority, needled; robustness to a scalar C(U) != 1 is the sibling's own gated scalar-drop), so the conditional transfer-operator reading of the sibling feed becomes UNCONDITIONAL on the corner surface: the reconstructed many-body Hamiltonian H_MB = dGamma(h[U]) generates real-time dynamics e^{i H_MB t} governed by the block07 display with a NATIVELY COMPUTED 1D activity envelope kappa <= K + 8K x/(1-x), x = e^{-(eta-mu)}, mu < eta (the corner surface is 1+1d — worker-flagged; the sibling's Z^3 shell envelopes do NOT apply and are not used; a 1D chain embeds in Z^3 so the block07 class applies verbatim; the d = 3 discharge is NOT claimed and is named open — no 3+1d free-fermion second-quantization surface currently exists in the repo); strict positivity 0 < t < 1 is sourced from the m > 0 gap (free exp-form; CT G1 m^2 I <= D[U] at fixed background), not from semidefiniteness alone; the Euclidean steps T_hat^{2k} are NOT conflated with real time (stated); (D4) the mode-set fork of the corner note is quoted as fork-INDEPENDENT for this identification (its own 'does not select between branches' sentence needled) — the discharge holds identically on both branches. NOT claimed: the U-integrated measure side; interacting/non-quadratic transfers (the sibling's quartic counterexample stands untouched, needled); anything beyond the corner notes' own scope and provenance; sharp constants; audit verdicts; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
  - microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - corner_axis_free_transfer_extension_per_channel_trace_correspondence_and_mode_set_fork_bounded_note_2026-06-12
  - corner_transfer_extends_to_fixed_gauge_backgrounds_bounded_note_2026-06-12
  - rp_p2_gauge_extension_and_realization_residual_note_2026-05-28
  - axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
runner: scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py
---

# Microcausality: Corner-Class Factorization Discharge

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every transfer object supplied by the
cited corner/engine/CT notes on their own surfaces; the axioms supply
no dynamics; the discharge inherits exactly those surfaces.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py`](../scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_corner_class_factorization_discharge_2026_07_18.txt`](../logs/runner-cache/microcausality_corner_class_factorization_discharge_2026_07_18.txt)

## Purpose

The sibling feed
[`MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md)
made its transfer-operator reading conditional on an explicit
Gaussian-factorization hypothesis `T_MB[U] = C(U)·Γ(T_1[U])`, with a
counterexample showing a one-particle kernel alone cannot force it.
This note discharges that hypothesis where the repo has already landed
it: the corner-transfer surface. The corner note
[`CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md`](CORNER_AXIS_FREE_TRANSFER_EXTENSION_PER_CHANNEL_TRACE_CORRESPONDENCE_AND_MODE_SET_FORK_BOUNDED_NOTE_2026-06-12.md)
displays `T_hat^2 = Gamma(t) = B^dag B` with `t(p) = exp(−2E(m,p))`,
`E = arcsinh(sqrt(m^2 + sin^2 p))`; its fixed-background companion
[`CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md`](CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md)
carries `Tr Gamma(t[U]) = det(1 + t[U])` with the `lambda = 1`
normalization forced; and the gauge-extension engine
[`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
defines the many-body two-step transfer at fixed background as
`T_hat^2[U] = Gamma(t1^(2)[U])` — while carrying the functorial
relation itself as an **import** ("standard free-fermion functorial
relation" in its supplied table). This note does two things: it
**rebuilds that imported relation natively** (the second quantization
as `e^{dGamma(ln t)}`, with the trace, multiplicativity, and log
identities gated exactly), and it **composes the discharge**: on the
corner surface the many-body log-transfer generator is exactly the
bilinear `dGamma(h[U])`, with `C = 1`, so the sibling chain's
Lieb-Robinson bounds govern the reconstructed many-body Hamiltonian's
real-time dynamics unconditionally there. Everything else — the
`U`-integrated measure side, interacting transfers, the engine note's
own residuals — remains exactly as those notes state it.

## Hypotheses (all supplied, none derived)

The supplied objects, each on its own note's surface and provenance:
(i) the corner free surface — per-channel two-step kernels
`t_k(p) = exp(−2E(lambda_k, p))` with the displayed many-body identity
`T_k^2 = Gamma(t_k) = B_k^dag B_k` (positive Hermitian) and the full
corner object the tensor product over channels; (ii) the
fixed-background extension — the engine note's definition sentence
("the many-body two-step transfer is the second quantization
`T_hat^2[U] = Gamma(t1^(2)[U])`"), its sampled-`SU(3)` positivity
table, AND its own hedge ("expected to survive at arbitrary spatial
`U`") — the discharge at fixed background inherits exactly this
status, no more; (iii) the CT note's reconstructed one-particle
Hamiltonian `h = −log(T_hat^2)/(2 a_tau)`, `h[U] =
arcsinh(sqrt(D[U]))`, with its kernel bound feeding the sibling
chain. **Convention reconciliation (worker-verified, stated):** the
corner notes silently adopt `a_tau = 1` (their `exp(−2E)` versus the
CT note's symbolic `2 a_tau`); and the glyph `T_hat^2` denotes the
MANY-BODY transfer in the corner/engine notes but the ONE-PARTICLE
two-step kernel in the CT note's `h`-definition formula (forced by
`h` being single-particle) — throughout this note, `t` is the
one-particle kernel and `T_hat_MB^2 = Gamma(t)` the many-body
operator, and the chain reads `t = e^{−2 a_tau h}`,
`−log T_hat_MB^2 = 2 a_tau · dGamma(h)`. The corner notes decompose
by GENERATION channel (circulant masses `λ_k`) while the CT note
works in spatial position space (mass `m`); the bridge is `m ↔ λ_k`
per channel on the supplied positivity domain (all channel masses
positive), with the full corner object the tensor product over
channels. The axioms supply no
dynamics (needled). Workhorse disclosure: one Opus 4.8 max worker
verified the object matching across the four source notes against
supervisor ground truth recorded first (its two convention flags are
the reconciliation above); the runner gates everything natively.

## Results

**Rebuilt functorial relation, pinned by the intertwiner (review-
sharpened).** The cited RP-positivity note
[`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
states the DEFINING property of the second quantization — vacuum
fixing plus the creation intertwiner
`Gamma(K)|vac⟩ = |vac⟩`, `Gamma(K) a_p^† = λ_p a_p^† Gamma(K)` — and
already derives the diagonal-kernel relation
`Gamma(e^{−h}) = e^{−dGamma(h)}` in-repo ("derived/checked in-repo,
not asserted", needled). This note supplies the exact-symbolic
version and the uniqueness discipline around it:

- **Realization:** `Gamma(t) := e^{dGamma(ln t)}` for positive `t`
  SATISFIES the defining property — the conjugation identity
  `e^{dGamma(X)} c_a^† e^{−dGamma(X)} = Σ_b (e^X)_{ba} c_b^†` and
  vacuum fixing are gated symbolically.
- **Uniqueness:** the defining property determines `Gamma(K)` on all
  of Fock space (induction: any vector is `Π c^†(f_i)|vac⟩`, and the
  intertwiner walks `Gamma` through each factor) — so the realization
  IS the corner notes' functor on the shared modes.
- **A load-bearing negative (review counterexample, adopted as a
  native gate):** trace correspondence plus multiplicativity plus
  positivity do NOT pin `Gamma` — conjugating by a number-conserving
  permutation `W` of the two-particle sector yields a distinct
  functor `Γ̃ = WΓW^†` with the same trace, the same commuting-family
  multiplicativity, and positivity, but violating the intertwiner and
  the log identity (`−log Γ̃(diag(2,3,5))` has two-particle block
  `diag(10,6,15) ≠ diag(6,10,15)` — gated). The `lambda = 1` forcing
  fixes only the scalar pair-measure normalization; the INTERTWINER
  is the pin. An earlier draft claimed the trace correspondence
  pinned the functor; corrected.
- **Consequences (gated):** the occupation action
  (`1, λ_2, λ_1, λ_1λ_2` at two modes), the trace identity
  `Tr Gamma(t) = det(1+t)` (diagonal symbolic AND a non-diagonally
  realized instance), multiplicativity **on commuting positive
  pairs** — the product of non-commuting positives need not be
  Hermitian (the instance `diag(2,1)·[[2,1],[1,2]]` is non-Hermitian,
  gated as a domain rejector), and commuting pairs are all the corner
  surface uses (powers of one kernel) — and the log identity
  `−log Gamma(t) = dGamma(−log t)`.

With the intertwiner characterization cited to the RP note and gated
natively, the engine note's import row ("standard free-fermion
functorial relation") is covered on the gated finite-mode surface by
repo-native content: the defining property, its unique realization,
and the consequences the corner chain uses.

**Composition (the discharge).** With the corner kernels
`t = e^{−2E}` — where STRICT positivity `0 < t < 1` is sourced from
the `m > 0` mass gap (`E ≥ arcsinh(m) > 0`, the free note's exp-form;
at fixed background the CT note's gap display `m^2 I ≤ D[U]` carries
it), NOT from the fixed-background note's `B^†B ≥ 0` alone
(semidefiniteness would not license the logarithm) — gated, and
matching the engine's `0 < mu ≤ 1` spectrum sentence (needled) and the supplied many-body identity
`T_hat_MB^2 = Gamma(t)`:

> `−log T_hat_MB^2 = dGamma(−log t) = dGamma(2E) = 2 a_tau ·
> dGamma(h[U])`  (at the shared `a_tau = 1`),

so the reconstructed many-body Hamiltonian is **exactly the
bilinear**:

> `H_MB := −log(T_hat_MB^2)/(2 a_tau) = dGamma(h[U])`,  `C = 1`.

The sibling feed's factorization hypothesis `T_MB = C(U)Γ(T_1)` holds
on this surface with `T_MB = T_hat_MB^2`, `T_1 = t[U]`, `C = 1` — the
corner note's own `lambda = 1` normalization-forcing sentence is the
uniqueness authority (needled) — `C = 1` is the corner surface's
asserted normalization, not an independent computation here — and
the sibling's gated scalar-drop makes the LR conclusion robust even
if a nontrivial scalar were present. Hence on the supplied definitional corner surface the sibling
chain's transfer-operator reading needs **no additional
Gaussian-factorization premise** (an earlier draft said
"unconditional", which overstated: the surface itself carries the
engine's definitional/sampled/hedged provenance, inherited). The Heisenberg object is written explicitly:
`τ_t(A) = e^{iH_MB t} A e^{−iH_MB t}` (`H_MB` self-adjoint since `h`
is). **Dimension scoping (worker-flagged, load-bearing):** the corner surface is `1+1d` (one
spatial dimension), so the sibling feed's `Z^3` shell envelopes do
NOT apply to it and are not used; instead this note computes the
corner surface's activity envelope natively — in one dimension there
is no metric conversion (`l_1 = l_∞`), the shell count is `2` per
distance, and with the CT kernel bound the block07 activity obeys

> per channel: `κ_k ≤ K_k + 8K_k·x_k/(1 − x_k)`, `x_k = e^{−(η_k−μ)}`;
> aggregate over the three generation channels (mode-disjoint on
> shared sites, so per-site activities ADD — gated):
> `κ_tot ≤ Σ_k [K_k + 8K_k·x_k/(1 − x_k)]`, for every
> `0 < μ < min_k η_k`

(gated; single-channel instance `9K` at `x = 1/2`; identical-channel
aggregate `3·9K` with the on-site norm `3K` exhibited via commuting
number operators) — a 1D **open** chain embeds in `Z^3` as an axis,
so the block07 class and display apply verbatim to the embedded
family. **Boundary scoping (review-found):** the transfer engine's
spatial carrier is periodic; a periodic wrap term has cycle-metric
kernel size `O(Ke^{−η})` but AMBIENT diameter `L − 1`, so its
site-weighted activity `≥ 2Ke^{−η}·e^{μ(L−1)}` grows without bound in
`L` (gated) — the volume-uniform envelope is therefore claimed for
the OPEN-BOUNDARY restriction of the corner family only; the
cycle-metric reformulation of the block07 class is named open. The real-time dynamics `e^{i H_MB t}` generated by
the reconstructed many-body Hamiltonian then obeys the block07
Lieb-Robinson display with this native envelope. **The `d = 3`
discharge is NOT claimed** — the corner notes land the factorization
at `d = 1` only, and a `3+1d` free-fermion second-quantization
surface does not currently exist in the repo (named open). The
Euclidean transfer steps `T_hat_MB^{2k}` are a different object and
are **not** conflated with real time.

**Fork independence (quoted).** The corner note's mode-set fork
(per-channel versus per-K-orbit registered occupancy) "does not
select between branches" at the level of the trace-fixed kernel
normalization — the identification `T_k^2 = Gamma(t_k)` holds
identically on both branches (needled), so the discharge is
fork-independent; nothing here bears on the downstream occupancy
premise.

**Scope inheritance, stated plainly.** The free per-channel discharge
rests on the corner note's displayed identity. The fixed-background
discharge rests on the engine note's DEFINITION of the many-body
transfer plus its sampled positivity and hedged arbitrary-`U`
language — this note inherits exactly that provenance (all three
sentences needled) and adds nothing to it. The `U`-integrated measure
side and interacting (non-quadratic) transfers remain open — the
sibling's quartic counterexample is untouched (needled) and marks
precisely where the discharge cannot go.

## No-Go Discipline Gate

- **N1 route inventory — ATTEMPTED.** (1) "The functorial relation
  might need Berezin machinery this note lacks" — ATTEMPTED and
  RESOLVED: the DEFINING intertwiner (cited to the RP-positivity
  note, which derives the diagonal case in-repo) is realized by
  `e^{dGamma(ln t)}` and gated symbolically, with uniqueness by the
  intertwiner induction; the engine note's import row is covered on
  this surface by repo-native content (the Berezin construction
  itself stays the corner notes' content); the review counterexample
  showing trace-plus-multiplicativity does NOT pin the functor is
  adopted as a native discrimination gate; (2) "the one-particle kernel might not
  determine the many-body object" — ATTEMPTED and AGREED: that is
  the sibling's counterexample, which is why the discharge uses the
  corner notes' SUPPLIED many-body identity, not the kernel; (3)
  "the glyph clash might hide a factor" — ATTEMPTED and RESOLVED by
  the worker-verified reconciliation (`a_tau = 1`; one-particle vs
  many-body `T_hat^2` disambiguated; every factor tracked); (4) "the
  mode-set fork might change the object" — ATTEMPTED and REFUTED by
  the corner note's own sentence (fork-independent, needled); (5)
  "Euclidean steps might be passed off as real-time causality" —
  ATTEMPTED and BLOCKED in text: the LR statement concerns
  `e^{iH_MB t}` only, stated where the theorem is stated. Not
  attempted, not smuggled: the `U`-integrated measure side,
  interacting transfers, sharp constants, the engine note's own
  residuals.
- **N2 hypothesis independence (pairwise) — ATTEMPTED.** The
  functorial relation (algebra only), the corner identity (supplied
  surface only), the positivity `0 < t < 1` (log-well-definedness
  only), and the convention `a_tau = 1` (bookkeeping only) enter at
  disjoint steps; the loop-pack battery flips each runner gate
  separately.
- **N3 hidden-wall scan — ATTEMPTED.** Conditions surfaced and
  stated: the fixed-background identity is the engine's DEFINITION
  with sampled (not proven-for-all-`U`) positivity and a hedge — all
  three needled, provenance inherited, nothing upgraded; the
  discharge is finite-mode (the corner notes' own finite surface);
  `a_tau = 1` is the corner notes' silent convention, made explicit;
  multiplicativity is scoped to COMMUTING positive pairs (the
  non-Hermitian product of non-commuting positives is a gated domain
  rejector); the aggregate envelope sums the three generation
  channels' activities (mode-disjoint additivity gated); the
  volume-uniform claim is scoped to OPEN boundaries (the periodic
  wrap term's ambient-diameter blow-up is gated; the cycle-metric
  class is named open).
- **N4 dependency roles, per citation — ATTEMPTED.**
  - Corner free note: supplies the displayed per-channel many-body
    identity and kernels (residual: its mode-set fork — untouched,
    fork-independence quoted).
  - Corner fixed-background note: supplies the trace correspondence
    and the `lambda = 1` forcing (residual: its own inherited engine
    dependency, which this note needles directly).
  - Engine note: supplies the fixed-background definition, sampled
    positivity, and the import row this note retires on the gated
    surface (residuals: its hedge and realization residuals —
    inherited, not upgraded).
  - CT note: supplies `h` and the kernel bound feeding the sibling
    chain (residual: its items remain as the siblings state).
  - Sibling block08: supplies the hypothesis being discharged, the
    scalar-drop gate, and the counterexample marking the boundary
    (all needled).
  - Block07: the LR display that now governs `e^{iH_MB t}`.
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Loop-pack worker analysis (`worker_b10_*`): disclosed
    scaffolding, graded against prior ground truth; not executed by
    the runner.
- **N5 rhetoric audit — ATTEMPTED.** "Discharge" is scoped to the
  corner surface with its provenance inherited sentence-by-sentence;
  "unconditional" modifies only the previously-conditional READING
  on that surface; "retires the import" is scoped to the gated
  finite-mode surface; real-time vs Euclidean is explicit.
- **N6 partial-closure scan — ATTEMPTED.** Closed here: the
  factorization hypothesis on the landed corner class, and the
  native rebuild of the imported functorial relation. Still open,
  named: the `U`-integrated measure side, interacting transfers (the
  counterexample boundary), sharp constants, and the engine note's
  own realization residuals.
- **N7 steelman (strongest counterarguments, answered) — ATTEMPTED.**
  (a) "The fixed-background identity is a definition plus samples,
  not a theorem — the discharge launders it." No: the inheritance is
  stated three-sentence-explicitly (definition, samples, hedge, all
  needled); the discharge's status at fixed background is exactly
  the engine's status, claimed as such. (b) "This is a two-line
  composition dressed as a block." The composition is deliberately
  small; the block's second half — the native rebuild retiring a
  named import row — is the standing-directive work, and the
  convention reconciliation (worker-verified) is where a wrong
  factor would silently corrupt every downstream constant. (c) "The
  log of a definition-level `Gamma` might differ from the Berezin
  object's log — indeed trace correspondence plus multiplicativity
  do NOT pin the functor (the review's permutation-conjugated
  counterexample, now gated natively)." Correct as an attack on the
  earlier draft; the pin is the DEFINING INTERTWINER (the
  RP-positivity note's own characterization, needled), which the
  realization satisfies (gated) and the counterexample violates
  (gated); beyond the gated surface nothing is claimed.
- **N8 prior-wall echo — ATTEMPTED.** The sibling's counterexample
  wall is respected (the discharge never argues from the kernel);
  the engine note's hedge is inherited, not crossed; the corner
  fork is untouched; no landed no-go concerns second-quantization
  functorial identities. The family's exhibit-pair discipline is
  repeated (identities gated symbolically plus a non-diagonal
  instance; the positivity window gated).

**Status: PASS** (all eight items answered; the block's two honest
weak points — the definitional/sampled status at fixed background and
the smallness of the composition — are the subjects of N7(a)/(b), not
footnotes).

## Non-Claims

- Does **not** upgrade the engine note's fixed-background status
  (definition + sampled positivity + hedge, inherited verbatim).
- Does **not** touch interacting/non-quadratic transfers (the
  sibling's quartic counterexample stands, needled) or the
  `U`-integrated measure side.
- Does **not** claim the Berezin construction itself (the corner
  notes' content); the import retirement is scoped to the gated
  finite-mode functorial relation.
- Does **not** conflate Euclidean transfer steps with real-time
  dynamics (the LR statement concerns `e^{iH_MB t}` only).
- Does **not** bear on the corner note's mode-set fork (quoted as
  fork-independent for this identification).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py`](../scripts/microcausality_corner_class_factorization_discharge_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **symbolic
identity gates** (the occupation action; the trace identity on
diagonal spectra; multiplicativity; the log identity; the composition
`−log Gamma(e^{−2a_tau h}) = 2a_tau·dGamma(h)`; the `a_tau`
reconciliation arithmetic), **exact instance gates** (the
non-diagonally-realized trace identity with spectrum `{1/4, 4}`; the
positivity window `0 < t < 1` at `E > 0` instances), and **presence
needles** (the corner displays and fork sentence; the engine's
definition, import row, hedge, and sampled-positivity fragment; the
CT definitions; the sibling's hypothesis, scalar-drop, and
counterexample sentences; the axiom memo — presence checks, not
correctness oracles). The gate sequence is enforced against an
ordered label manifest. The runner prints one `PASS`/`FAIL` line per
gate and a final total; the cached transcript is committed at the
path in the header at landing time.
