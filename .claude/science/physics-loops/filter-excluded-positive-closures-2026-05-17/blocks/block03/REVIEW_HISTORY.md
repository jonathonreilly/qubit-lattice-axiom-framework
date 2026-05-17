# Block 03 Review History

**Date:** 2026-05-17
**Target:** `g_bare_derivation_note`

## V1: Verdict-identified obstruction → PASS

The 2026-05-07 L3a 10-vector obstruction explicitly records the uniform
inflation factor `dim(V_fiber) = 2` between the V_3 and V trace surfaces
(S1 sharpening) but classifies the L3a binary admission as a structural
overall scale, NOT as an inert convention. The gap: no prior note routes
this inflation through the Wilson matching equation to demonstrate g_bare
invariance.

## V2: New content → PASS

The theorem establishes:

| Claim | Content |
|-------|---------|
| (T1) | `Tr_V(F²) = 2 · Tr_{V_3}(F²)` from V-embedding `T_a^V = T_a^{(3)} ⊗ I_2` |
| (T2) | Lattice-side ratio `F^{(V)}/F^{(V_3)} = 3/4` (exact structural) |
| (T3) | Continuum-side invariance via `(1/N_F^{(W)})` cancellation |
| (T4) | Wilson matching `β^{(W)} = dim(W)/(N_F^{(W)} g_bare²)` |
| (T5) | L3a binary inert for `g_bare`: both surfaces yield `g_bare = 1` |

The routing structurally parallels the 2026-05-03 generator-rescaling
routing (T_a → cT_a routes c² into β). This is the FIRST explicit
demonstration of the L3a binary's physical inertia.

## V3: Audit lane could complete → FAIL (i.e., the audit lane CANNOT do this)

The audit lane is restricted to syntactic/dependency checks and cross-row
consistency. The required content here is:

- Numerical small-`a` plaquette coefficient extraction on both V_3 and V
  via numpy least-squares.
- Symbolic continuum-side invariance proof via sympy simplify across the
  binary admission.
- Identification of the L3a routing as algebraically parallel to the
  rescaling routing, completing the routing-table of L3 admissions.

None of these can be authored by the audit pipeline. The audit lane will
review the bridge after written.

## V4: Non-trivial marginal content → PASS

Three contributions not in any existing note:

1. Explicit demonstration that L3a S1 uniform inflation produces `g_bare`
   invariance via Wilson matching.
2. Exact structural ratios: lattice-side `3/4` and β `4/3`, neither
   computed by any existing note.
3. Recognition that L3a binary swap is algebraically parallel to the
   2026-05-03 rescaling swap, with both routing into β.

Downstream unlock: even if L3a is never closed structurally, the parent
`g_bare_derivation_note`'s L4 conclusion is robust against the residual.

## V5: Not a one-step variant → PASS

Distinguishing content from each potentially-overlapping prior note:

| Prior note | Their content | This block's content |
|------------|---------------|---------------------|
| `N_F_BOUNDED_Z2_REDUCTION` (2026-05-07) | Narrows to `{1/2, 1}` binary | Routes binary through Wilson matching |
| `L3A_V3_TRACE_SURFACE_BOUNDED_OBSTRUCTION` (2026-05-07) | S1 uniform inflation recognition | Cancellation in Wilson matching equation |
| `G_BARE_RESCALING_FREEDOM_REMOVAL` (2026-05-03) | Generator-rescaling routing into β | Trace-surface routing into β (orthogonal) |
| `G_BARE_HILBERT_SCHMIDT_RIGIDITY` (2026-05-07) | Form rigidity (scalar within surface) | Trace surface choice (different DoF) |
| `G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE` (2026-05-09) | Ward two-form route | L3a routing route (orthogonal) |
| `G_BARE_FORCED_VIA_WARD_SUBSTITUTION_NARROW` (2026-05-17) | Ward-substitution exact-sympy | L3a routing exact-sympy (different identity) |
| `N_F_V3_NORMALIZATION_BOUNDED` (2026-05-07) | N_F=1/2 conditional on L3a | L3a-inertness regardless of admission |

## Overall outcome

**V1-V5: PASS.**

Route: write source narrow theorem +
audit-companion runner + cache.

## Block status

**COMPLETE.** Source note (`G_BARE_L3A_TRACE_SURFACE_INVARIANCE_NARROW_THEOREM_NOTE_2026-05-17.md`),
runner (`audit_companion_g_bare_l3a_trace_surface_invariance_2026_05_17.py`),
and cache (`logs/runner-cache/audit_companion_g_bare_l3a_trace_surface_invariance_2026_05_17.txt`)
all landed. Block artifacts populated. PASS = 33, FAIL = 0.
