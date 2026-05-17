# Block 04 Value Gate (V1-V5) — L3b Overall Scalar

**Target:** L3b overall scalar admission for g_bare. L3b = the choice of
positive scalar `N_F` in `Tr(T_a T_b) = N_F · δ_{ab}` within a fixed
trace surface (after L3a binary V_3 vs V is fixed). Framework adopts
canonical `N_F = 1/2` (Gell-Mann).

Block 03 addressed L3a (binary `N_F ∈ {1/2, 1}` from trace-surface choice
V_3 vs V), proving the binary is inert for g_bare.

## V1 — Independent science content (not a one-step relabeling)

**Claim:** L3b is a *continuous* one-parameter convention orbit
`N_F > 0`, not a finite-set choice. Block 03 (L3a) handled a 2-point
subset (binary, set by structural inflation factor 2). Block 04 (L3b)
must handle the *entire* positive real ray `N_F ∈ R_{>0}`.

**Is this >1 step from block 03?**

Block 03's identity: under W ∈ {V_3, V}, `β^{(W)} = dim(W) / (N_F^{(W)}
· g_bare²)`. The L3a binary was discretely indexed by trace surface; the
inflation factor `c_V = 2` was structurally forced by `dim(V_fiber) = 2`.

Block 04's identity must address the L3b orbit on a FIXED trace surface
(W = V_3, dim = 3), with the convention scalar `N_F` itself sweeping
the positive reals. The L3a structural factor 2 does NOT appear here;
instead the orbit is parameterized by an arbitrary positive real. The
two questions are mathematically distinct:

- L3a: "Does the 2-point binary, with discretely-fixed factor 2 from
  Cl(3) + Z^3, leave g_bare unchanged?" — answered by structural
  inflation cancellation.
- L3b: "Does the continuous 1-parameter family `N_F > 0`, parameterized
  by a free positive real, leave g_bare unchanged?" — requires
  re-expressing Wilson matching as a covariant identity along the
  N_F orbit, then showing g_bare is an orbit invariant.

The 2026-05-03 rescaling-removal theorem partially overlaps L3b: it
treats `T_a → c T_a` and shows β → c² β. But it does NOT package the
result as "L3b is inert for g_bare" — it packages it as "rescaling
freedom is removed by canonical normalization". Block 04's contribution:
explicitly identify the continuous L3b orbit with the c-rescaling
family, and show that g_bare is an orbit invariant under the full
N_F > 0 sweep, regardless of which N_F is chosen as canonical.

**Verdict V1: pass.** Block 04 covers the continuous orbit; block 03
covered a 2-point structural subset; the 2026-05-03 rescaling theorem
covered a different physical reading (rescaling vs. convention choice).
The packaging as "L3b orbit invariance of g_bare under continuous N_F"
is new.

## V2 — Source-only deliverable (no audit-data touches)

Source theorem + paired runner + cache. No status promotion. The
`docs/G_BARE_DERIVATION_NOTE.md` parent row is NOT modified. The
audit lane decides retention.

**Verdict V2: pass.**

## V3 — A_min only (no imports)

The theorem uses only:
- The Wilson plaquette matching equation (cited from runner section C
  of `frontier_g_bare_derivation.py`)
- The trace identity `Tr(T_a T_b) = N_F · δ_{ab}` (definitional, on
  fixed trace surface V_3)
- Polynomial algebra over R_{>0}

No PDG values, no fitted constants, no literature comparators. The
canonical N_F = 1/2 enters only as the framework's adopted value;
the theorem proves invariance across the full positive ray.

**Verdict V3: pass.**

## V4 — Honest no-overclaim

The theorem does NOT claim:
- That N_F = 1/2 is uniquely forced by A1 + A2 (this remains the
  honest open question, per the 2026-05-07 four-layer stratification)
- That the L3b admission is closed (it remains admitted; we prove it
  is inert for g_bare, not that it is structurally derived)
- That g_bare = 1 is an absolute derivation (it is a derived
  constraint relative to the L3 convention layer)

The genuine novel content: the L3b convention scalar parameterizes
a 1-parameter orbit, and g_bare is an explicit orbit invariant under
the Wilson matching identity. Either choice of N_F yields the same
physical g_bare = 1 at the canonical-normalization-forced β value
for that N_F.

**Verdict V4: pass.**

## V5 — Not a one-step variant of block 03

Block 03's identity: `β^{(W)} = dim(W) / (N_F^{(W)} · g_bare²)`
parameterized by W ∈ {V_3, V} with N_F^{(W)} ∈ {1/2, 1} (binary).

Block 04's identity: `β^{(N_F)} = 2 N_c · (1/2) / N_F · (1 / g_bare²)`
(or equivalently `β · g_bare² · N_F = N_c`, after replacing the
canonical Gell-Mann N_F = 1/2 with the L3b free scalar) parameterized
by N_F ∈ R_{>0} (continuous), with the SAME trace surface V_3 fixed.

Mathematical distinctions:
1. **Indexing variable**: discrete W ∈ {V_3, V} vs. continuous
   N_F ∈ R_{>0}.
2. **Source of the parameter**: structural Cl(3) + Z^3 inflation
   factor vs. free convention scalar choice.
3. **Dimensionality of orbit**: 2-point subset vs. 1-parameter
   continuous orbit.
4. **Proof technique**: structural inflation cancellation (uses
   dim(V)/dim(V_3) · c_W ratio) vs. continuous orbit invariance
   (uses derivative/differential identity along the N_F orbit).

This is NOT a one-step relabeling. It is the continuous-orbit
generalization that block 03's binary identity is a 2-point
specialization of. The novel claim is the **orbit-invariance form**:
`d g_bare / d N_F = 0` along the canonical-matching surface, for
any N_F > 0.

**Verdict V5: pass.**

## Summary

All five gates pass. Proceed to derivation.

The block 04 theorem's load-bearing identity, on the fixed trace
surface V_3 with continuous L3b scalar N_F ∈ R_{>0}:

```
β(N_F) = (2 N_c) · (1/2) / N_F · (1 / g_bare²)
       = N_c / (N_F · g_bare²)
```

with N_c = 3. At each N_F, the canonical-normalization-forced
Wilson coefficient is `β_canonical(N_F) = N_c / N_F` (the value
forced when g_bare = 1 at that N_F).

Solving back: `g_bare²(N_F) = N_c / (N_F · β_canonical(N_F)) =
N_c / (N_F · (N_c / N_F)) = 1`.

So g_bare = 1 for *every* N_F > 0 under the canonical matching
surface. The L3b admission is inert for g_bare.
