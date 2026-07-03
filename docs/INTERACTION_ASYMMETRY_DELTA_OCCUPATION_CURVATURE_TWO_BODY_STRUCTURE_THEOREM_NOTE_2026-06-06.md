# The Interaction Asymmetry `delta`: it is the Occupation-Number Curvature, Vanishes to All Orders for the Free Dynamics, and is Irreducibly Two-Body — Structure Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (the structure of `delta` / `|K|`; the precise value left open)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/interaction_asymmetry_delta_occupation_curvature_runner.py`](../scripts/interaction_asymmetry_delta_occupation_curvature_runner.py)
**Cached output:** [`logs/runner-cache/interaction_asymmetry_delta_occupation_curvature_runner.txt`](../logs/runner-cache/interaction_asymmetry_delta_occupation_curvature_runner.txt)

## Audit context

The emergent `C3` coupling `|K|` (the coefficient of the native double-shift `J − I` on the
generation triplet) vanishes at naive second order for a symmetric (linear) spectrum and is
sourced by an energy asymmetry `delta` between the `hw=0` and `hw=2` intermediate states
(`E_2 = 2*eps + delta`), with `|K| ~ t^2*delta / eps^2`. That `delta` is the open "actual
emergent coupling" named in
[`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
(`retained_bounded`). This note pins down **what `delta` is**: it is the occupation-number
**curvature** of the energy, it is **irreducibly two-body**, it cancels to **all orders** for
the free single-hop dynamics (not merely at second order), and it carries a **forced sign
law**. The diagonal companion — how the second-order *return* shapes the generation **masses**
— is the retained
[`HW1_SECOND_ORDER_RETURN_SHAPE_THEOREM_NOTE`](HW1_SECOND_ORDER_RETURN_SHAPE_THEOREM_NOTE.md);
the present note is its **off-diagonal** counterpart (the `C3` mixing `|K|`, not the species
diagonal).

## Safe statement

Setup (the minimal native model): the generation triplet is the Hamming-weight-1 sector of
the single-hop dynamics `H = eps*N + t*V` on `C^8`, with `V = sum_mu X_mu` (the native
single bit-flip) and `N` the excitation-number operator. Define the **occupation curvature**
`delta = E_2 − 2*E_1 + E_0`, the discrete second difference of the energy `E(hw)` in the
excitation count `hw`.

**Theorem.**

1. **The free dynamics cancels `|K|` to all orders — by factorization.** `H = eps*N + t*V`
   splits as a sum over the single-flip axes, `H = sum_mu (eps*n_mu + t*X_mu)`, so the full
   spectrum is the `L`-fold **sumset** of the per-axis spectrum (verified `L = 3, 4, 5`).
   Energy is therefore **additive** over excitations, `E(hw)` is **affine** in `hw`, and the
   curvature `delta = 0` **to all orders** — not merely at second order. No amount of the
   free single-hop dynamics sources `|K|`. (The naive second-order cancellation,
   `E^{(2)}(hw) = (2*hw − L)*t^2/eps` affine `⇒ delta_2nd = 0`, is the special case of this.)

2. **`delta` is the occupation curvature, and it is irreducibly two-body.** Decompose the
   energy into occupation functionals by degree. Every **one-body** functional `a*hw + b` is
   affine, so its second difference is `0` and it contributes **nothing** to `delta`. The
   **lowest-degree** functional with nonzero curvature is the **pair count**
   `C(hw,2) = hw(hw−1)/2`, whose second difference is identically `+1`. Hence
   `delta = w_pair` exactly: `delta` is carried by a genuine **connected two-body** coupling,
   and `delta = 0 ⟺ there is no two-body coupling`.

3. **Forced sign law in the no-resonance / weak-pair regime.** A native pair coupling
   `U * sum_{i<j} n_i n_j` sets `delta = U` exactly. Schur elimination of the `hw=0`
   and `hw=2` intermediates gives the off-diagonal generation-triplet coupling

   ```text
   K_off = t^2 * (1/eps - 1/(eps + U))
         = t^2 * U / (eps * (eps + U)).
   ```

   Therefore, for `eps > 0` and `eps + U > 0` (equivalently the perturbative
   no-resonance / weak-attraction window), `sign(K_off) = sign(delta) = sign(U)` and the
   coupling has the `C3` (`J − I`) form with all off-diagonals equal. The sign claim is
   **not** asserted across the denominator crossing `eps + U = 0`; beyond that boundary
   the second-order eliminated formula changes sign and the restricted theorem must be read
   as out of regime.

4. **The one-body lattice realization of `delta` is a forbidden diagonal.** In momentum space
   `n_mu = (1 − cos k_mu)/2`, so the pair term `n_mu n_nu` carries
   `cos k_mu cos k_nu = (1/2)[cos(k_mu+k_nu) + cos(k_mu−k_nu)]`, whose real-space image is a
   hop along `e_mu ± e_nu` — a **next-nearest (face-diagonal)** bond. The **LATTICE** axiom is
   6-nearest-neighbour cubic with **no diagonals**, so **no one-body 6-NN `H_0` can carry
   `delta`** (consistent with (1): every axis-separable one-body `H_0` is additive ⇒ affine ⇒
   `delta = 0`). `delta` is therefore a genuine **two-body / interaction** object, not a
   kinetic one.

So `delta` (hence the off-diagonal `K` channel) is not a hopping amplitude and not any one-body
lattice energy: it is the **two-body occupation curvature**, sign-locked to the underlying
pair coupling in the explicit `eps > 0`, `eps + U > 0` no-resonance regime, and zero for the
entire free single-hop sector.

## The genuine open piece (the route this opens)

The **value** of `delta` (its sign and scale) requires the native two-body interaction, which
the bare `{single-hop V, Hamming-graded H_0}` does not contain. The leading **non-import**
route is the framework's already-**retained** two-body mediator channel — the
`(L + mu^2) Phi = G|psi|^2` surface of
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md)
and
[`WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11`](WILSON_TWO_BODY_OPEN_REFINED_NOTE_2026-04-11.md)
(both `retained_bounded`), whose mutual energy is **attractive**. If that channel supplies the
generation-pair energy, then by the sign law (3) it fixes `sign(delta) < 0` and bounds
`|delta| = G·W(r_pair)` by the propagator value at the pair separation. That computation — the
mediator pair-energy at the generation separation — is the sharply-posed next artifact; it is
**not** performed here. Independent of the value, the flavor pattern is robust to the precise
`|K|` over a wide window, so the qualitative result (neutrino → `C3`, heavier sectors → corner)
survives the open `delta`.

## Boundary (honest)

- **A structure result, not a value.** It establishes that `delta` is the two-body occupation
  curvature with `sign(K_off) = sign(delta)` only in the stated `eps > 0`, `eps + U > 0`
  no-resonance regime, and that the free sector gives `delta = 0` to all orders; it does
  **not** compute the sign or scale of `delta`.
- **The all-orders statement is for the axis-separable single-hop model.** It is exact for
  `H = eps*N + t*sum_mu X_mu` and for any axis-additive one-body `H_0`. A genuine two-body
  term (the open object) is precisely what breaks the separability — that is the content of (2)
  and (4), not a loophole in (1).
- **Interpretation-independent.** The factorization, the curvature decomposition, and the
  forbidden-diagonal identity are statements about the operators `{N, V}`; they do not depend
  on whether the three single-flip axes are read as spatial directions or as taste/momentum
  axes (the latter reading rests on the currently-`unaudited` BZ-corner surface and is not
  used here).
- **Off-diagonal scope.** This note concerns the `C3` mixing coefficient `K` (off-diagonal,
  `J − I`); the species **diagonal** (mass weights) is the separate retained
  `HW1_SECOND_ORDER_RETURN_SHAPE_THEOREM_NOTE`.
- **Denominator boundary.** The exact Schur formula has denominators `eps` and `eps + U`.
  This row assumes `eps > 0` and `eps + U > 0`. It does not claim a global sign law through
  the resonance/level-crossing boundary where the eliminated second-order expression is no
  longer in the weak-pair regime.

## What this is not (no-go hygiene on the (4) clause)

Clause (4) is **route-opening, not closing**. It does not assert that `delta` is
underivable; it **locates** `delta` outside the one-body 6-NN kinetic sector and **points** at
the retained two-body mediator channel as the place to derive it. Alternative live routes (not
foreclosed): the retained mediator pair-energy (above); a real-space loop/ring-exchange effect
on the full `Z^3` lattice (the toy is loop-free, so its factorization does not bind the looped
lattice); and the records/sector-weight channel. No finite enumeration of sources is claimed.

## Forbidden imports check

No new axiom. `V = sum X_mu` and the Hamming-graded `H_0` are the minimal native lattice
dynamics; the factorization (sumset), the occupation-functional curvature decomposition, the
sign law, and the product-to-sum (`face-diagonal`) identity are arithmetic. The two-body
mediator route cited for the open value uses **retained** (`retained_bounded`) surfaces, not a
new import; its application to the generation-pair energy is named open, not asserted.

## Runner check breakdown

Class A (exact finite-dimensional linear algebra / arithmetic): (1) `H = eps*N + t*sum X_mu`
spectrum equals the `L`-fold per-axis sumset for `L = 3, 4, 5` (factorization ⇒ all-orders
`delta = 0`), and the affine second-order shift reproduces the naive cancellation; (2) one-body
occupation functionals have second difference `0` while the pair count `C(hw,2)` has second
difference `+1`, and a pure pair term gives `delta = w_pair` exactly; (3) a native pair coupling
`U` gives the exact formula `K_off = t^2 U/[eps(eps+U)]`, hence `sign(K_off)=sign(U)` only under
`eps>0`, `eps+U>0`, with the exact `C3` (`J − I`) form; (4) the product-to-sum identity
exhibiting the face-diagonal content. Expected `runner_check_breakdown = {A: N, B: 0, C: 0,
D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact: the free single-hop Hamiltonian factorizes across the flip axes,
so its energy is additive and the occupation curvature `delta = E_2 − 2E_1 + E_0` vanishes to
all orders — strengthening the second-order cancellation to an all-orders statement and
identifying `delta` as the discrete curvature of the energy in excitation number. The
occupation-functional decomposition shows `delta` is carried by the pair count (second
difference `+1`), so `delta` is irreducibly two-body. The sign law is the checked Schur formula
`K_off=t^2 U/[eps(eps+U)]`, restricted to `eps>0`, `eps+U>0`; the old unrestricted sign-lock
wording is not part of the theorem. The one-body realization of the pair term is a next-nearest
(face-diagonal) hop forbidden by the 6-NN lattice axiom, so `delta` is a genuine two-body object.
The result is a **structure + regime-scoped sign-law** localization of `delta`, not a value: the
precise sign/scale reduces to the retained two-body mediator channel, named open. Effective
status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/interaction_asymmetry_delta_occupation_curvature_runner.py
```
