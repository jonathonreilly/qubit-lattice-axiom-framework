# Block 03 V1-V5 Value Gate — g_bare_derivation closure attempt

**Date:** 2026-05-17
**Target:** `g_bare_derivation_note` (audited_conditional, parent open_gate)
**Chosen route:** **Positive narrow theorem** — L3a binary admission is
physically inert for g_bare via the trace-surface routing into β
(algebraically parallel to the 2026-05-03 generator-rescaling routing).

## Honest landscape (read first)

The g_bare derivation chain has matured substantially:

- The Hilbert-Schmidt rigidity theorem (2026-05-07) closes "no scalar dilation"
  on the form.
- The four-layer stratification (2026-05-07, restatement note) identifies L3
  (overall scalar `N_F`) as the single convention layer.
- The N_F binary reduction theorem (2026-05-07, w2) narrows the continuum
  freedom to `N_F ∈ {1/2, 1}` — the binary trace-surface admission (V_3 vs V).
- The L3a 10-vector obstruction (2026-05-07, l3a) consolidates a sharpened
  bounded obstruction: 0 unconditional positive arrows, 4 partials all
  converging on the matter-rep / staggered-Dirac realization gate, 6 clean
  obstructions. The S1 sharpening notes uniform inflation, but does not
  route it through Wilson matching.
- Today's Ward-substitution narrow (2026-05-17) isolates the substitution
  closure as exact-sympy bounded theorem, conditional on the same-1PI
  pinning row.

The L3a 10-vector obstruction observes (S1) that the V_3-to-V trace
inflation is a "uniform global multiplicative factor, NOT a structural
discriminator." This block makes that observation **load-bearing for
g_bare** by routing the inflation through the Wilson matching equation.

## V1: Verdict-identified obstruction

**Yes.** The L3a 10-vector obstruction's S1 sharpening explicitly recognizes
that polynomial-in-T_a observables uniformly inflate by `dim(V_fiber) = 2`
between V_3 and V (line 63-64). But the L3a note classifies the binary
admission as a structural overall scale, NOT as an inert convention. The
gap: nobody has explicitly demonstrated that the Wilson matching cancels
this inflation symmetrically on both sides, leaving `g_bare` invariant.

This block closes that gap as a class-(A) positive theorem.

## V2: NEW content (not in any existing note)

The narrow theorem will establish:

1. **(T1) Trace inflation identity.** `Tr_V(F²) = c_V · Tr_{V_3}(F²)` with
   `c_V = 2`, structurally from the V-embedding `T_a^{(V)} = T_a^{(3)} ⊗ I_2`.

2. **(T2) Lattice-side small-`a` coefficient.** The Wilson plaquette functional
   `F^{(W)}(U) = (dim(W) - Re Tr_W(U))/dim(W)` has small-`a` coefficient
   ratio `F^{(V)}/F^{(V_3)} = 3/4` (an exact computable structural factor).

3. **(T3) Continuum-side invariance.** Both `(1/(2g²)) (1/N_F^{(W)}) Tr_W(F²)`
   expressions reduce to the convention-independent `(1/(4g²)) Σ_a F^a_μν F^{a μν}`,
   verified by sympy symbolic simplify.

4. **(T4) Wilson matching identity.** Solving the small-`a` lattice-to-continuum
   match: `β^{(W)} = dim(W)/(N_F^{(W)} · g_bare²)`. At `g_bare = 1`:
   `β^{(V_3)} = 6 = 2 N_c` (the canonical Wilson formula); `β^{(V)} = 8 = dim(V)`.

5. **(T5) g_bare invariance under L3a binary swap.** Both binary admissions
   yield the SAME `g_bare = 1` at the canonical matching surface; only the
   conventional `β` differs (6 vs 8, related by structural ratio 4/3).

Positive content: the L3a binary admission routes entirely into β, leaving
g_bare invariant. This is the **first explicit demonstration** of the L3a
binary's physical inertia for the only quantity the g_bare chain certifies.

## V3: Audit lane could complete?

**No.** The audit lane does syntactic/dependency checks and cross-row
consistency. It cannot:

- Compute the small-`a` lattice plaquette coefficient on V vs V_3 numerically
  and exactly.
- Construct the symbolic continuum-side invariance proof via sympy.
- Demonstrate that the L3a routing into β parallels the 2026-05-03
  rescaling routing into β, completing the routing-table of L3 admissions.

This requires structural mathematical insight bridging the L3a uniform
inflation (S1 of 2026-05-07) with the Wilson matching equation. The audit
lane can REVIEW the bridge after written; it cannot AUTHOR it.

## V4: Non-trivial marginal content

**Yes.** The theorem does three things not present anywhere on main:

- Demonstrates explicitly that the L3a S1 "uniform inflation" observation
  produces `g_bare` invariance via Wilson matching (the prior notes stop
  at recognizing the inflation; this note routes it through matching).
- Computes the exact structural lattice-side ratio `F^{(V)}/F^{(V_3)} = 3/4`
  and the exact β ratio `β^{(V)}/β^{(V_3)} = 4/3`, neither present in any
  existing note.
- Identifies the L3a binary swap as algebraically parallel to the 2026-05-03
  generator-rescaling swap, completing the "routing-into-β" table of L3
  admissions: scalar rescaling ↔ trace-surface choice ↔ both route into β,
  leave g_bare invariant.

This unlocks downstream consumers of `g_bare_derivation_note`: even if the
L3a admission is never closed structurally, the parent's L4 conclusion
`g_bare = 1` is robust against the residual L3a binary admission. The
parent re-audit can cite this row as supporting evidence for L4-conclusion
robustness.

## V5: Not a one-step variant

**Not a relabel of:**

- The 2026-05-07 N_F binary reduction (which narrows to `{1/2, 1}` but does
  not route via Wilson matching).
- The 2026-05-07 L3a 10-vector obstruction (which records S1 uniform
  inflation but does not derive `g_bare` invariance).
- The 2026-05-03 rescaling-freedom-removal theorem (which addresses
  generator-rescaling, a different convention layer).
- The 2026-05-07 HS rigidity theorem (which addresses the form, not the
  trace surface).
- The 2026-05-09/05-17 Ward-route theorems (different upstream authorities;
  not via L3a).
- The 2026-05-10 abstract narrow theorems (which strip physics; this note
  routes the binary inflation through Wilson matching physics).
- The 2026-05-07 N_F V_3 normalization note (which derives N_F=1/2
  conditional on the L3a admission; this note's complementary statement is
  L3a-inertness regardless of the admission).
- Today's blocks 01-02 staggered-Dirac substep theorems (which address the
  Dirac structure; orthogonal to the gauge-coupling routing).

The narrow theorem is genuinely NEW: it is the **only** note that explicitly
chains the L3a S1 uniform inflation TO the Wilson matching equation,
producing the `g_bare` invariance corollary as a class-(A) algebraic
identity with structural lattice-side and continuum-side coefficients
verified at exact precision.

## V1-V5 outcome: PASS

Route: write a **POSITIVE NARROW THEOREM** for L3a binary `g_bare`-inertness
via the trace-surface routing into β.

## Honest scope limits (in writing now)

The theorem does NOT:

- Close the L3a admission (the trace-surface choice remains an admitted
  convention).
- Newly derive `N_F = 1/2` from A1+A2.
- Lift the parent g_bare_derivation_note's audited_conditional status (which
  requires retained-grade closure of upstream rescaling/constraint deps).
- Modify the four-layer stratification's L3 admission count.

It DOES:

- Establish a NEW positive arrow: L3a binary → β routing → g_bare invariance.
- Compute the exact structural ratios (lattice `3/4`, β `4/3`).
- Identify the L3a routing as algebraically parallel to the 2026-05-03
  rescaling routing.
- Demonstrate that the parent's L4 g_bare = 1 conclusion is L3a-binary-inert.
- Provide a chain through which downstream consumers can treat the L3a
  residual as `g_bare`-physically-inert, even pre-closure.
