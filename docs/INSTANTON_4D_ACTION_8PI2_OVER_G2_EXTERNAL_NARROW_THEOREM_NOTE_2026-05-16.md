# 4D Instanton Minimal Action `8π²/g²` — External Narrow Theorem

**Date:** 2026-05-16
**Claim type:** positive_theorem
**Scope:** external 4D Euclidean SU(N) Yang-Mills instanton minimal action
formula (BPST 1975; 't Hooft 1976) and lattice preservation under Lüscher
admissibility (Lüscher 1982; Lüscher 2010). Cited only as published
gauge-theory context. No framework substrate identification, hierarchy
closure, scale ratio derivation, or `α_LM^16` substitution is claimed.
**Status authority:** independent audit lane only; pipeline-derived
status set by `compute_effective_status.py`.
**Runner:** [`scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py`](../scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.txt`](../logs/runner-cache/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.txt)

## Claim

Let `A_μ(x)` be a smooth Euclidean SU(N) gauge connection on `R^4` (or
on a 4-torus / 4-sphere compactification at infinity), with field
strength

```text
F_μν = ∂_μ A_ν - ∂_ν A_μ + i [A_μ, A_ν]
```

and Hodge dual

```text
(*F)_μν = (1/2) ε_μνρσ F^ρσ.
```

The Euclidean Yang-Mills action is

```text
S[A] = (1 / (4 g²)) ∫ d^4x  Tr( F_μν F^μν ).
```

Define the topological charge

```text
Q = (1 / (32 π²)) ∫ d^4x  Tr( F_μν *F^μν ).
```

Here `Tr` denotes the standard component/trace normalization in which
the self-duality bound below has coefficient `8π²/g²`; changing the
generator normalization changes the displayed action and charge
normalizations together, not the invariant instanton weight.

**Statement (external theorem):**

1. *Atiyah-Singer integrality.* For any smooth finite-action SU(N) gauge
   configuration on a compactified 4-manifold, `Q ∈ Z`. This is the
   Atiyah-Singer index theorem applied to the chiral Dirac operator in
   the gauge background (Atiyah-Singer 1968-1971).

2. *Self-duality bound.* For any gauge configuration with topological
   charge `Q`, the action satisfies

   ```text
   S[A] ≥ (8 π² / g²) |Q|,
   ```

   with equality iff `F = *F` (self-dual) when `Q > 0`, or `F = -*F`
   (anti-self-dual) when `Q < 0`.

3. *BPST minimal-action solution.* At `|Q| = 1`, there exists an
   explicit self-dual classical solution (the BPST instanton; Belavin,
   Polyakov, Schwartz, Tyupkin 1975) whose action is exactly

   ```text
   S_inst = 8 π² / g².
   ```

4. *Lattice preservation under admissibility.* On a 4D Wilson lattice
   with link variables `U_x,μ ∈ SU(N)` and bare coupling `β = 2N/g²`,
   Lüscher's admissibility condition (`||1 - U_p|| < ε` for a fixed
   `ε > 0` on every plaquette `p`; Lüscher 1982) restricts the
   configuration space to a disjoint union of topological sectors
   labelled by integer `Q_lat`, with `Q_lat` agreeing with the continuum
   `Q` up to standard `O(a²)` lattice artifacts. The Wilson gradient
   flow (Lüscher arXiv:1006.4518, 2010) provides a modern smoothing
   procedure that extracts the same integer `Q` from a thermalized
   lattice configuration; in the continuum limit `a → 0`, the lattice
   minimal-`|Q|=1` action approaches `8 π² / g²` with `O(a²)`
   corrections.

The action `S_inst = 8 π² / g²` is the canonical 4D SU(N) instanton
minimal action and is independent of `N` (BPST is realized inside an
SU(2) subgroup of SU(N) for `N ≥ 2`); the determinant prefactor
multiplying `exp(-S_inst)` does depend on `N` and was computed by
't Hooft (Phys. Rev. D **14** (1976) 3432).

## Boundary

This note records an external 4D Yang-Mills theorem and its standard
published lattice-gauge context. It does **not** claim:

- that the BPST instanton substrate is identified with the framework's
  substrate (lattice cell, taste, blocking, plaquette family, or any
  project-specific structure);
- that the 4D SU(N) Wilson lattice is identified with any
  framework-specific lattice;
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- closure of the `α_LM^16` substitution or any framework `α^N`
  hierarchy at integer `N`;
- closure of `v/M_Pl` or any other dimensional scale ratio (the
  hierarchy formula `v/M_Pl = exp(-8π²/g²)` is **not** claimed; the
  note records only the instanton action as a standalone external
  theorem);
- any numerical prediction or comparison with observation beyond the
  published gauge-theory context;
- any new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework
substrate with the 4D SU(N) gauge background, identify a framework
observable with the instanton sector, and verify the substrate-specific
bridge.

## External References

- A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Y. S. Tyupkin,
  "Pseudoparticle Solutions of the Yang-Mills Equations",
  Phys. Lett. B **59** (1975) 85.
- G. 't Hooft, "Computation of the Quantum Effects Due to a
  Four-Dimensional Pseudoparticle", Phys. Rev. D **14** (1976) 3432;
  erratum Phys. Rev. D **18** (1978) 2199.
- M. F. Atiyah, I. M. Singer, "The Index of Elliptic Operators I-V",
  Ann. Math. **87** (1968) 484-604; **93** (1971) 119-149; **93**
  (1971) 546-604.
- M. Lüscher, "Topology of lattice gauge fields",
  Commun. Math. Phys. **85** (1982) 39.
- M. Lüscher, "Properties and uses of the Wilson flow in lattice QCD",
  JHEP **08** (2010) 071; arXiv:1006.4518.
- E. Witten, "Some Exact Multipseudoparticle Solutions of Classical
  Yang-Mills Theory", Phys. Rev. Lett. **38** (1977) 121
  (multi-instanton classical solutions).

## Verification

The paired runner checks (in exact Fraction arithmetic with SymPy `pi`
symbolic and `mpmath`-equivalent numerical surrogates where needed):

1. **T1**: symbolic minimal action formula `S_inst = 8 π² / g²` at `Q = 1`
   reproduced from the Bogomolny bound `S ≥ (8π²/g²) |Q|` saturated by
   `F = *F`.
2. **T2**: Atiyah-Singer integrality — `Q ∈ Z` is stated as an external
   theorem; runner verifies that the integrality check is part of the
   note text and that the symbolic Q-formula `Q = (1/32π²) ∫ Tr(F *F)`
   matches the documented normalization.
3. **T3**: numerical `S_inst` at `g² ∈ {1/2, 1, 2}` evaluated as
   `8 π² / g²` ≈ `157.91`, `78.96`, `39.48` respectively.
4. **T4**: numerical `exp(-S_inst)` at the same `g²` values, exhibiting
   the canonical instanton suppression at intermediate coupling.
5. **T5**: at `g² = 1`, `S_inst = 8 π² ≈ 78.9568...` and
   `exp(-S_inst) ≈ 5.05 × 10^{-35}`.
6. **T6**: self-duality identity `F = *F ⟹ S = (1/(2 g²)) ∫ Tr(F²)
   = (8π²/g²) |Q|`, verified algebraically.
7. **T7**: lattice `O(a²)` correction structure — runner asserts that
   the note states lattice preservation with `O(a²)` corrections under
   admissibility (no numerical artifact claim is made; the structural
   form is recorded).
8. **T8**: source-note boundary — note declares `claim_type:
   positive_theorem`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure or any hierarchy substitution.

Expected runner result: `PASS=N`, `FAIL=0`.

## Upstream authority

- [TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md](TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md) — bounded named-import umbrella wrapper covering Bogomolny bound, BPST `|Q|=1` solution, Atiyah-Singer integrality, and Luescher admissibility / gradient-flow lattice charge. Provides the one-hop authority for the four external textbook ingredients used by this narrow theorem.
