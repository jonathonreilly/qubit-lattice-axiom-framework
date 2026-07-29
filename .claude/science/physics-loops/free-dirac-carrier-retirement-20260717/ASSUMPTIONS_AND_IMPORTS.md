# Assumptions And Imports

## First-principles reset

The supplied axiom surface is exactly the stable `minimal_axioms` node:

1. **Lattice:** physical sites are `Z^3` with nearest-neighbor adjacency,
   translations, and proper cubic rotations; no site is privileged.
2. **Qubit:** the full one-site possibility domain has presentation `M_2(C)`;
   the compatible `Cl(3,0)` presentation adds no primitive structure; no
   possibility is privileged.
3. **Admissibility:** one fixed translation/proper-cubic-covariant
   nearest-neighbor rule determines locally available possibilities.
4. **Record:** records form, lock one admissible possibility, are unique per
   site and permanent, and have content-only finite additive scalar readout.

Approved primitives were checked directly in
`docs/audit/data/axiom_premise_nodes.json`. The only load-bearing primitive
proposed here is `kinetic_isotropy_primitive`, supplying `c_t=c_s` and nothing
else. `scale_reference_primitive` and `realized_state_primitive` are not needed.

## Import ledger

| Item | Exact role | Current class | Load-bearing? | Open for stronger claim? | Disposition |
|---|---|---|---:|---:|---|
| `minimal_axioms` | actual Lattice/Qubit/Admissibility/Record boundary | accepted axiom premise | no for the bounded theorem | yes for any physical realization claim | checked directly; deliberately not a graph dependency because it supplies no dynamics or composition theorem |
| `kinetic_isotropy_primitive` | equality of temporal/spatial kinetic form | approved structural primitive | yes | no | allowed only as `c_t=c_s` |
| `ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md` | finite `16x16` Clifford symbol `D_red` and taste commutant | `retained_bounded` | yes | no | candidate one-hop parent of the new derivation |
| `FERMION_PARITY_PAULI_TENSOR_INVOLUTION_NARROW_THEOREM_NOTE_2026-05-10.md` | comparison for parity/occupation identities on a given finite qubit tensor product | `retained` | no | yes | plain-code context only; it supplies neither physical composition nor CAR, and the needed identities are re-derived |
| finite complex/spectral/Fourier analysis | pole, residue, projectors, compact-momentum convergence | mathematical infrastructure | yes | no | must be re-derived in the artifact, not cited as physics authority |
| finite ordered tensor product plus Jordan-Wigner strings | exact CAR realization | mathematical construction | possible | yes for physical reading | hard-premise test; do not hide as an axiom consequence |
| canonical free-staggered action as physical law | selects the analyzed lattice dynamics | missing physical bridge | no for a theorem conditional on the retained symbol; yes for actual framework realization | yes | explicit boundary |
| OS reconstruction/continuum existence | promotes Euclidean poles to a physical Wightman theory | missing | no for algebraic pole-carrier limit; yes for reconstruction | yes | excluded from proposed bounded scope |
| CAR/statistics selection | says the framework physically chooses CAR | missing | no for a given-CAR relabelling theorem; yes for spin-statistics | yes | excluded; relabelling must not masquerade as selection |
| observed/fitted/literature value | empirical or external proof input | forbidden | no | no | absent |

The retained ABJ parent already writes a symmetric four-label Euclidean
formula, but only as a finite algebraic free surface. It does not normalize its
`mu=0` label against the emergent temporal tick. The primitive's nonduplicative
role is precisely that kinetic-form normalization before the mathematical pole
continuation; it does not by itself turn the pole parameter into physically
reconstructed transfer energy. The parent alone carries all finite matrix
identities.

## Counterfactual pass

| Assumption under test | If false | Alternative direction opened | Current classification |
|---|---|---|---|
| `c_t=c_s` | temporal coefficient differs | the displayed deformed pole shell and residue differ in the continuum limit | discriminating control for this coefficient family only |
| finite staggered Clifford symbol is the analyzed free sector | another admissible kinetic law is selected | pole geometry and species content change | physical-action bridge remains open |
| ordered tensor product is available | only local one-site algebras are supplied | JW strings cannot be defined as physical cross-site operators | live CAR-composition wall |
| JW string is omitted | raw disjoint ladders commute | off-site CAR anticommutators are nonzero | exact control in the chosen ordered tensor realization |
| positive-pole projector is used | negative branch is not separated | one-particle positive carrier and antiparticle relabelling are undefined | explicit sector choice within the given free symbol |
| compact momentum is held fixed as `a -> 0` | momenta scale to a BZ edge | doublers/taste corners remain rather than one continuum patch | bounded convergence domain must be stated |

## Forbidden imports

- no target Poincare generators, boosts, invariant measure, or CAR Hamiltonian
  may be inserted as starting definitions and then called derived;
- no new axiom/primitive or governance edit;
- no audit ledger/status/queue edit and no audit verdict;
- no observed/fitted values or literature input as proof;
- no use of the active `cl3_to_cl31` runner-artifact or Koide dial work;
- no claim of physical action selection, OS reconstruction, interacting
  Lorentz invariance, taste removal, or spin-statistics unless independently
  supplied.

## Cycle 2 transport audit

No physics premise or dependency changes in the packet repair. The registered
primitive check still identifies only `kinetic_isotropy_primitive` as relevant
to the upstream derivation, with exactly its declared `c_t=c_s` role. The
current repair consumes only repository facts: the target has one cited
authority, that authority is 20,118 characters, and the ordinary per-authority
transport cap is 10,000 characters. The scoped 22,000-character allowance is
tooling capacity, not a scientific premise or normalization.
