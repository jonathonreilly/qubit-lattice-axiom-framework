# Focused native column-plaquette review

Disposition: PASS for fixed-order coefficient and fixed-finite-size common-scale parity selection, subject to explicitly stating the nonzero fixed transverse-ratio premise below. Parent live replay and publication mechanics remain separate. No repository edits, formal audit, or new full-H computation by this reviewer.

Read complete canonical note, aggregate runner, native plaquette/parity scripts and independent /private/tmp/neutral-column-plaquette-check.md. Reused the independent exact24-order path calculation and inspected the root's stronger full canonical fourth-order sum. Native JSON was being rewritten by the parent's live replay; inspected completed L5 entries and do not classify transient absence of L6 entries as a failure.

## Mathematical findings

The -YY amplitude depends on current spin signs, and the root path implementation retains those signs and signed denominators. All16 aligned colors are included. For L>=5 a four-operation process cannot reverse a whole column; each site must therefore return with even flip count. A distinct-edge square forces the four operations onto one slice. Repeated-edge loops affect only the scalar contribution. The scalar K2 and metric ensure the canonical folded term cannot change the plaquette coefficient. The root's full two-step dictionary includes every intermediate destination and interference before squaring; its direct-minus-E2*metric formula is appropriate here. Open bulk/end counting gives(L+14)/128, periodic counting givesL/128, multiplying Jx²Jy²/Jz³. No added microscopic plaquette interaction is being smuggled in.

At fixed finite L>4, a nonzero order-four splitting dominates order-L tunneling under a fixed common transverse scale. Perturbative continuation of the isolated aligned manifold then supports the conditional energetic preference. It does not establish exact parity as a kinematic constraint, select a vacuum superposition, prove uniform convergence with length, or prove the isotropic phase. The note keeps these limits explicit. The native test compares the two uniform-rung-parity sectors containing the aligned states; it is not an exhaustive comparison of all nonuniform rung-parity sectors, and is correctly not called a global ground certificate.

The rectangular constraints imply z_xy=a_x b_y by fixing one row and column and propagating each elementary relation. The shared sign redundancy gives2^(Nx+Ny−1), also on compatible nonduplicated periodic rectangles. This is a subsystem degeneracy and commuting energy constraint; gauge/topological identification is correctly excluded. Prior art is explicitly acknowledged as context, not as derivation of this model's coefficient.

## Required narrow clarification

State Jx=λ jx and Jy=λ jy with fixed nonzero jx,jy as λ→0 (or explicitly restrict the selection assertion to equal Jperp). K_L vanishes if either coupling is zero; a λ-dependent transverse ratio can also alter order counting relative to tunneling. The independent report already supplies this common-scale premise. Add a Markdown link to scripts/native_column_plaquette_selection.py for a concrete canonical replay entry point. These are scope/provenance clarifications, not new physical premises.

## Runner/evidence

Exact assertions cover all colors at L5..8 and all bulk/end loop cases. The numerical runner tests ground ordering and mean-band splitting with residual-qualified eight-state bands, not an all-sector ground theorem. Its GF(2) checks support the array count while the row/column argument supplies the all-size proof. For inspected L5 λ=.1,.2 outputs even the entire positive eight-state band lies below the negative band (gaps2.66668e−5 and3.79752e−4), with residuals below2.6e−13. Parent replay must confirm the complete final output. No source/readout, empirical calibration or scale bridge is inferred from this splitting.

## Reviewed source hashes
- `docs/NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md`: `ed470f3913212a85f1c61fce79e83e9b3e75daa14c111933b34d92305973b657`
- `scripts/native_column_plaquette_selection.py`: `99a44b04e829f4c1e52dc85729f5fda32d09a1eb869d728b92c024870f8de1c5`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_plaquette.py`: `94aaba329f92a322e6cc52c98138670e5edf4a35e571989a461ae63803361a93`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_parity_native.py`: `17ee3270a0c6c37722e2a3fc2d7202a7c07724ba02f0eefb63e2f1cfa79e258e`

## Same-session affected-fix confirmation

Confirmed the fixed nonzero common-scale Jx/Jy premise, the zero/vanishing-ratio caveat and primary runner link in the current note. Final scoped disposition: PASS. Parent full replay and mechanical gates remain separate. Final note SHA256: `ed470f3913212a85f1c61fce79e83e9b3e75daa14c111933b34d92305973b657`.

## Affected extension: original composite readout

Disposition: PASS for the order-four readout coefficient and elastic interpretation, pending the parent's live source-bound numerical replay. Read the new canonical section, modified native readout calculation, aggregate assertions and /private/tmp/neutral-column-readout-check.md. No source edits or duplicate heavy run.

For H+sC the cost2n1Jz−2sn2 is correct. Differentiating−Jx²Jy²/(2d³) gives−6n2K/d. Two endpoints, two next-to-end heights and L−4 interior heights sum to−3(L+13)Jx²Jy²/(128Jz4). Twice that coefficient gives the displayed single-square positive-minus-negative difference. This is consistent with the independent rational count and with the original open NNN readout, not an appended physical interaction.

The canonical connection is explicitly retained conceptually rather than discarded as a general identity. Its first projected order vanishes and lower effective terms are scalar, so it cannot change the claimed fourth-order parity coefficient; the trace commutator vanishes exactly for the continued isolated band. The numerical script computes C directly as the open j,j+2 diagonal and averages its expectation across eight normalized real eigensolver vectors. The compared uniform-rung-parity blocks are exact invariant sectors in this tube, making that trace comparison legitimate. The doubled coefficient is explicitly restricted to the single-square case, not asserted for arbitrary array labels.

The note correctly describes this order as commuting/elastic and makes no inference of an inelastic pole, detector identity or cosmological coupling. No required correction found for this extension. Updated source hashes:
- `docs/NATIVE_COLUMN_PLAQUETTE_SELECTION_NOTE_2026-10-18.md`: `9e2d8594a8882f3ac291d35b8e828fa6f0c809140907f96f482d89ac37658f6b`
- `scripts/native_column_plaquette_selection.py`: `04857b08d5e4c188849af5a6ab7c30ea31dddb965e3cf82e68cd5a963de0d7a4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_column_parity_native.py`: `2b6e8560fd6c2cf15d83448b3746358bef937aa88c366e5293d7c47ce0ee5049`
