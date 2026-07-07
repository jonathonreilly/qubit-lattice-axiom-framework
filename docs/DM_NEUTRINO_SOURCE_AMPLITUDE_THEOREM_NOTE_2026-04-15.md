# DM Neutrino Source-Amplitude Theorem

**Claim type:** bounded_theorem

**Date:** 2026-04-15  
**Status:** bounded conditional sharp-branch source-amplitude result on the
named-input `K_R` carrier definition
**Script:** `scripts/frontier_dm_neutrino_source_amplitude_theorem.py`

## Framework sentence

In this note, “axiom” means only the single framework axiom `Cl(3)` on `Z^3`.
Everything else is a derived atlas row.

## Question

After the DM weak-to-triplet transfer coefficients are fixed, what is still
left on the source side?

Can the selector amplitude `a_sel` and the symmetric weak source amplitude
`tau_+ = tau_E + tau_T` be fixed canonically on the sharp source-oriented
branch, inside the named-input `K_R` carrier definition?

## Bottom line

Yes, inside that bounded carrier context.

On the sharp source-oriented branch:

- `a_sel = 1/2`
- `tau_E = tau_T = 1/2`
- `tau_+ = 1`

Therefore, using the already-derived transfer coefficients inside the same
bounded source package,

- `gamma = c_odd a_sel = 1/2`
- `E1 = sqrt(8/3) tau_+ = sqrt(8/3)`
- `E2 = (sqrt(8)/3) tau_+ = sqrt(8)/3`

So on the refreshed `main`-derived branch, the source side is no longer a
floating pair of amplitudes on the sharp branch once the named-input `K_R`
carrier definition is supplied. This does not derive that carrier as a
physical primitive.

## 2026-07-04 scope repair

The upstream `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` now records `K_R` as a
class-A definition under named admitted inputs `(delta_A1, u_E, u_T)`. It
explicitly does not derive those inputs, the decoupling fact, the
aligned-bright coordinates, or a physical tensor-primitive interpretation.

This note is therefore not an exact physical weak-carrier theorem. Its
load-bearing result is conditional: given the named-input `K_R` row factor and
the sharp source-oriented projection, the source amplitudes are fixed as
`a_sel = 1/2`, `tau_E = tau_T = 1/2`, and `tau_+ = 1`.

## Selector amplitude

The reduced selector lane already gives one exact class with one real
amplitude,

`B_red = a_sel S_cls`

with

`S_cls = chi_N_nu - chi_N_e`.

The sign theorem already says `a_sel > 0` picks the neutrino-side branch.

The new step is the sharpness normalization. Reusing the bosonic-bilinear
selector principle, the selected branch is not treated as a soft weighted
mixture. It is treated as a sharp resolved branch projector.

On the reduced `N_nu/N_e` block, the source-oriented sharp selector is

`P_nu = diag(1,0)`

and its centered selector part is

`P_nu - (1/2)(P_nu + P_e) = (1/2) S_cls`.

So the canonical sharp selector amplitude is

`a_sel = 1/2`.

## Symmetric weak source amplitude

The named-input weak source carrier definition is the two-column bright bundle

`K_R(q) = [[u_E(q), u_T(q)], [delta_A1(q)u_E(q), delta_A1(q)u_T(q)]]`.

The swap-reduction theorem already showed that only the symmetric source mode
survives into the exact even-response law:

`tau_+ = tau_E + tau_T`.

The sharp bosonic-even source on that exact two-channel factor is the swap-even
projector

`P_+ = (1/2)(I + P_swap) = (1/2) [[1,1],[1,1]]`.

Its source coordinates are exactly

`(tau_E, tau_T) = (1/2, 1/2)`,

so

`tau_+ = 1`.

## Immediate DM consequence

The coefficient theorems already gave:

- `c_odd = +1`
- `v_even = (sqrt(8/3), sqrt(8)/3)`.

Substituting the sharp source amplitudes gives the bounded triplet-side source
data

- `gamma = 1/2`
- `E1 = sqrt(8/3)`
- `E2 = sqrt(8)/3`.

That is the current bounded source-amplitude point on the refreshed
`main`-derived DM branch, conditional on the named-input `K_R` carrier
definition.

## What remains open

This note does **not** derive the `K_R` carrier as a physical weak tensor
primitive. It also does **not** yet rewrite the full leptogenesis benchmark in
terms of these sharp source amplitudes. The existing benchmark runner still
uses the older reduced kernel.

So this is a bounded source-amplitude result inside a supplied carrier
definition, not yet the final `eta` note.

## Command

```bash
python3 scripts/frontier_dm_neutrino_source_amplitude_theorem.py
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [hierarchy_bosonic_bilinear_selector_note](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
- [s3_time_bilinear_tensor_primitive_note](S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md)
- [dm_neutrino_weak_even_swap_reduction_theorem_note_2026-04-15](DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md)
- [dm_neutrino_codd_bosonic_normalization_theorem_note_2026-04-15](DM_NEUTRINO_CODD_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
- [dm_neutrino_veven_bosonic_normalization_theorem_note_2026-04-15](DM_NEUTRINO_VEVEN_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md)
