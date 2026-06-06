# The Koide δ Rank-2 Eigenline Selector Is the Native Clifford Chirality (the Domain-Wall Edge), Not a Wilson Mark — No-Go Downgrade

**Date:** 2026-06-05
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a **no-go downgrade** (computable-side). The two retained no-gos
[`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`](./KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md)
and
[`KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md`](./KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md)
left an explicit falsifier open: *a retained theorem proving the physical Brannen line is a unique rank-1
summand of the rank-2 zero-mode sector.* This note supplies a **native candidate** for that selector — and
it is **not** a Wilson/APS mark (those are provably scalar), it is the **Clifford / Kähler-Dirac chirality
γ₅** (the on-site Cl(3,0) chirality / spin grade), realizing the **standard domain-wall edge** mechanism.
**Claim scope:** this is **not a full δ closure**. It downgrades the eigenline-selection residual from "no
non-scalar selector exists in the retained Wilson algebra" to "the selector is the native chirality γ₅,
conditional on three named gates." It does **not** discharge: (a) the single-physical-fermion reduction
(**rooting**) is non-local at finite spacing → principled only in the continuum (`retained_conditional`);
(b) the endpoint **c=0** (the based-section lift) is a separate residual; (c) the zero-mode/edge sector must
be the physical carrier. The separate **radian/unit admission** (δ = 2/9 *in radians* vs the index-theory
phase πη = 2π/9) is untouched.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_koide_delta_rank2_chirality_selector_exact.py`](./../scripts/audit_companion_koide_delta_rank2_chirality_selector_exact.py)

## The bottleneck and the resolution

The C₃[111] fixed-point density `L₃(1,2) = 2/9` is **forced** (retained-bounded). But the physical phase δ
reading it requires a **unique rank-1 line** out of a **rank-2 zero-mode sector**: two orthonormal zero-mode
lines `ψ₀, ψ₁` share the same Z₃ generation character, and every mixture `ψ(α)=cos α·ψ₀+sin α·ψ₁` is a valid
zero mode (`selected=cos²α`, `spectator=sin²α`). The cobordism no-go shows **every retained Wilson/APS mark
acts as `λI`** on this rank-2 space — so no *mark* selects.

**The resolution is that the selector is not a mark — it is the chirality.** Reproven in the runner (7/7):

1. **The obvious candidate fails for the right reason.** The site-parity `ε=(−1)^{x+y+z}` is **scalar**
   (`= −I₃`) on the three hw=1 corners (all Hamming weight 1, same parity), so it cannot split the doublet
   — consistent with the marks-are-scalar no-go. (Runner (1).)
2. **The Clifford/KD chirality γ₅ is non-scalar and splits it.** On the rank-2 zero-mode sector,
   `γ₅ = diag(+1,−1)` (distinct eigenvalues), and the chiral projector `P₊=(1+γ₅)/2` selects a **unique
   rank-1 line** (`Tr P₊ = 1`) — forcing `α=0`. (Runner (2),(3).) This is the on-site Cl(3,0) chirality /
   spin grade (the Quantum-axiom Pauli), confirmed by direct construction on the eigenline-no-go runner's
   actual `C²_spin⊗C²_taste⊗lattice` Hilbert space.
3. **The single-summand survives a vanishing global index.** `Tr(γ₅)=0`: the global index sums to zero over
   both chiralities (Nielsen-Ninomiya), yet the **selected (+) line reads the local density 2/9** while the
   global cancels. This is exactly the **domain-wall mechanism** — Fukaya-Onogi-Yamaguchi `index_DW = −η/2`:
   a single edge carries one local spectral asymmetry even when the bulk/global invariant cancels; and
   Donnelly's equivariant-η theorem localizes the boundary η to the C₃ **fixed point** as a sum of local
   fixed-point terms — the precise analog of `2/9 = L₃(1,2)`. (Runner (4),(6).)
4. **Why the no-gos missed it.** `γ₅` **anticommutes** with the massless operator (`γ₅²=I`, `Tr γ₅=0`), so it
   is **outside** the scalar Wilson/APS-mark algebra the cobordism no-go covers. The no-gos correctly ruled
   out *marks*; they did not (and explicitly could not) rule out the *chirality*. (Runner (5).)

## What this is, and the three gates it does NOT close

| | statement | status |
|---|---|---|
| the rank-1 selector | the native Clifford/KD chirality `γ₅` (domain-wall edge), not a Wilson mark | **identified** (runner 7/7) |
| single-local-η vs vanishing global | the selected chirality reads `2/9`; global cancels (Fukaya `index_DW=−η/2`) | **mechanism-backed** (lit) |
| (a) single physical fermion (**rooting**) | non-local at finite spacing → continuum-only | **open — conditional** |
| (b) endpoint **c=0** (based-section lift) | parity fixes orientation/sign, not the lift | **open — separate residual** |
| (c) edge sector = physical carrier | γ₅ is a good quantum number on the kernel; needs the edge to be physical | **open — domain-wall prescription** |
| the **radian** unit (δ=2/9 rad vs πη=2π/9) | a separate admission, untouched here | **open — separate bridge** |

**Net.** The eigenline-selection half of the δ bottleneck — the harder, structural half the two no-gos
isolated — now has a **framework-native answer**: the on-site Clifford chirality `γ₅`, realizing the standard
domain-wall edge (one local η from a vanishing global index). This **downgrades** the rank-2 no-go to a
conditional. It is **not** a derivation of δ: the rooting/continuum justification, the `c=0` endpoint, and the
separate radian admission remain. But it converts "no selector exists" into "the selector is the chirality,"
which is a real structural advance on the one genuinely-derivable flavor value.

## No-go discipline / steelman

**Strongest objection (the rooting gate).** The single-physical-fermion reduction from the taste-doubled
spectrum is **provably non-local at finite lattice spacing** (Bernard-Golterman-Shamir, Creutz); it is
principled only in the continuum limit where taste symmetry restores. So "the physical lepton reads one local
`2/9`" is a continuum statement, gated at finite spacing — which is why this note keeps it **conditional**
(`retained_conditional`), not a theorem. **Second objection (kernel-only).** `γ₅` does not commute with the
*massive* Wilson operator; its selection is exact on the *massless* zero-mode/edge sector, so a clean
statement needs the edge to be the physical carrier (the domain-wall prescription) — gate (c). Both objections
are accommodated by the explicit conditional scope; the selector existence (Parts 1–4) stands regardless.

## Forbidden-import / reprove-and-cite

All algebra (ε scalar; γ₅ non-scalar; P₊ rank-1; global trace zero; `L₃(1,2)=2/9`) is **reproven** from the
C₃ / Clifford primitives in the runner (sympy, 7/7). Fukaya-Onogi-Yamaguchi (`index_DW=−η/2`, arXiv:1710.03379),
Donnelly (equivariant-η fixed-point localization), the staggered-taste / Kähler-Dirac chirality `Γ=(−1)^p`
literature, and the rooting-locality results are **comparators** only. No PDG values; `δ≈2/9` named only as
the target this note advances (not derives).

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md`](./KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24.md)
- [`KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md`](./KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24.md)
- [`KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md`](./KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23.md)
- [`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](./KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`](./STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)

**Independent audit required.** This note asserts no effective-status change.
