# Block07 plan — weighted-norm quasilocal-class walk expansion

Date: 2026-07-18. Seventh block, opened under the owner's directive to
continue with Opus 4.8 max workhorse workers (substitution disclosed in
the worker specs). Target: the last mathematical gap between the
family's strict finite-range classes and the log-transfer generators —
a Lieb-Robinson bound for SUPPLIED weighted-norm quasilocal
interactions.

## Class (avoids lattice-animal counting entirely)

Supplied family {h_S} over finite connected S, Hermitian, with the
supplied weighted bound
  kappa := sup_x sum_{S: x in S} ||h_S|| |S| e^{mu diam S} < infinity
(mu > 0 supplied). The |S| weight exists precisely to absorb the
contact-site choice in the stepwise factorization.

## Supervisor ground-truth derivation (independent, pre-worker)

- Chain lemma: chains S_1 (touch X) -> ... -> S_k (touch Y) have
  sum_j diam(S_j) >= d (induction on the accumulated reach).
- Weight split: Pi ||h_j|| <= e^{-mu d} Pi (||h_j|| e^{mu diam_j}).
- Factorization: F_n(S) := backward chain sums; G_n := sup F_n/|S|
  contracts: G_{n+1} <= kappa G_n, so F_n(S) <= |S| kappa^{n-1};
  top level over S_1 touching X gives T_k <= |X| kappa^{k-1} with
  every |S| weight consumed exactly.
- Assembly vs the sibling unrolled form (2||A||, per-step 2||h||,
  base 2||h|| ||B||):
    ||[tau_t(A),B]|| <= ||[A,B]||
      + 2||A|| ||B|| (|X|/kappa) e^{-mu d} (e^{2 kappa |t|} - 1).
- Velocity readout v <= 2 kappa / mu.
- Consistency: strict bond class gives kappa = 12 J e^mu exactly
  (6 bonds/site, |S| = 2, diam = 1) => 24 e J at mu = 1 vs the direct
  20 e J — general result weaker by exactly 6/5, as expected; the
  direct bond notes stay sharper on their class.
- Instance family: pair interactions h_{xy} = J lambda^{|x-y|} K_{xy}
  on Z^3; sites at distance r: 4r^2 + 2 exactly; kappa(q) =
  2J [4 q(1+q)/(1-q)^3 + 2 q/(1-q)] at q = lambda e^mu < 1 — exact
  rational in q. 1D-chain variant (2 per distance) for cheap gates.
- Scope: state for BOTH the tensor class (clean form) and the
  even-CAR class (explicit odd-odd zeroth term, via block04's graded
  lemma) — the log-transfer generators are fermionic bilinears, so the
  CAR version is the one the identification will need.

## Workers (Opus 4.8 max, workflow w0l2byq7b)

- Worker A scout: exact inventory of the four transfer-side bridge
  notes + block04 (what each controls, decay forms, whether the
  bilinear-from-decaying-kernel weighted bound is derivable, proposed
  block07/block08 split, needle candidates).
- Worker B math: the full inequality chain per the spec (graded
  against the ground truth above before any use).

## Cluster discipline

PR #7: evaluator must be re-run against B06's closing statement.
Honest basis for reopening: the owner directed continuation with a
strengthened worker seat, and the weighted-norm hypothesis form is the
genuinely new input that removes the lattice-animal obstruction B06's
"outside toolkit" judgment implicitly assumed.
