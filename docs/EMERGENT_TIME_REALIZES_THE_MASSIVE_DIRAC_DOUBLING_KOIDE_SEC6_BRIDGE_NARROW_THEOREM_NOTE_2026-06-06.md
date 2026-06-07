# The Derived Emergent-Time Axis Realizes the Cl(3,0)→Cl(3,1) Massive-Dirac Doubling — the KOIDE §6 Bridge (Narrow Theorem)

**Date:** 2026-06-06
**Claim type:** bounded_theorem (a bridge connecting two retained endpoints; the positive-energy part remains modulo R + rung C)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/emergent_time_realizes_massive_dirac_doubling_runner.py`](../scripts/emergent_time_realizes_massive_dirac_doubling_runner.py)
**Cached output:** [`logs/runner-cache/emergent_time_realizes_massive_dirac_doubling_runner.txt`](../logs/runner-cache/emergent_time_realizes_massive_dirac_doubling_runner.txt)

## Audit context

The FS carrier admission reduces (this session's panel) to two statistics-sensitive residuals; the
highest-leverage is **(B)**: deliver the emergent-time `Cl(3,0)→Cl(3,1)` `e₄`-doubling as a
positive-energy, microcausal, boost-covariant **massive** Dirac field. The on-site boost note
[`KOIDE_ONSITE_BOOST_..._WEYL_FAITHFUL_VS_SCALAR_SELECTION`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md)
(`retained_bounded`) **§6** names this residual exactly: a single qubit `C²` carries **one**
chirality (massless Weyl); a massive Dirac field needs **both**, furnished by the `e₄`-doubling
(`e₄²=−1`, `e₄=iγ⁰`; algebra `retained`,
[`CL3_TO_CL31_SPINOR_EXTENSION`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)),
and §6 states *"this is exactly the emergent-time / Wick-rotation step … what is **not** established
is that the framework's emergent-time field on `Z³` realizes that doubling as a positive-energy,
microcausal, boost-covariant massive field."* This note **builds that bridge** using the session's
**derived** emergent time.

## Safe statement

Two endpoints are retained but **disconnected from the framework's emergent time**: the **Euclidean**
free staggered kernel is compact-`Spin(4)`-covariant
([`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md),
`retained_bounded`), and the **Lorentzian** free massive Dirac field carries the non-compact
`so(3,1)` Poincaré rep
([`FREE_DIRAC_POINCARE_REPRESENTATION`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md),
`retained_bounded`, *"textbook free-field checks"*). The bridge:

**Theorem (the derived emergent-time axis realizes the doubling).**

1. **Euclidean endpoint.** The retained staggered kernel's symmetry is **compact** `Spin(4)`: all
   six `Σ^E_{μν}=¼[γ^E_μ,γ^E_ν]` are anti-Hermitian, so its boosts `exp(θΣ^E_{4j})` are **unitary**
   — the Euclidean kernel **does not reach** the non-compact boost-spinor.
2. **The emergent-time axis IS `e₄`.** The session's derived emergent time (the record-count
   `I`-axis, with the `e₄²=−1` Lorentzian signature) is the **timelike** `e₄=iγ⁰` (`(γ⁰)²=+1`,
   `e₄²=−1`), exactly the `Cl(3,0)→Cl(3,1)` doubling direction. The Lorentzian Clifford
   `{γ^μ,γ^ν}=2η^{μν}` (`η=diag(+,−,−,−)`) holds.
3. **The Wick rotation flips compact → non-compact.** Along the emergent-time `e₄=iγ⁰`, the boost
   `K_j=Σ^{0j}_L = i·Σ^E_{4j}`: the emergent-time factor `i` turns the **anti-Hermitian** (compact,
   unitary) Euclidean `Σ^E_{4j}` into the **Hermitian** (non-compact, `exp(θK_j)` non-unitary)
   Lorentzian boost — while rotations `J_k` stay anti-Hermitian (compact). This **reaches the
   non-compact boost-spinor** the compact Euclidean kernel cannot.
4. **The retained non-compact algebra + the massive doubling.** `[K^i,K^j]=−ε^{ijk}J^k` (boosts
   give the **opposite** sign to `[J^i,J^j]=+ε^{ijk}J^k` — the non-compact `so(3,1)` signature, =
   the retained `FREE_DIRAC_POINCARE` sign). The single qubit `C²` is **one** chirality
   (`ω=γ₁γ₂γ₃=+i·1`); the `e₄`-doubling `C²→C⁴` carries **both** (`tr P_± = 2`), and the on-shell
   projector `(p̸+m)/2m` is idempotent **only on `C⁴`**, with the mass `m` **coupling** the two
   chiralities (massive Dirac, not Weyl).

So **the framework's derived emergent-time axis realizes the `e₄`-doubling** that bridges the retained
compact-`Spin(4)` Euclidean kernel to the retained non-compact `so(3,1)` **massive** Dirac
bispinor — the structural core of §6's residual — boost-covariant and **microcausal** (the merged
reconstructed-`H` quasi-locality bridge, #3127).

## What this delivers (and what remains)

- **Delivered:** the §6 residual's **structural + causal** core — *the framework's emergent time
  realizes the boost-covariant massive `Cl(3,0)→Cl(3,1)` doubling*, with the non-compact boost-spinor
  reached and microcausality from #3127. The `e₄` is no longer an *adjoined* Euclidean coordinate; it
  is the **derived** record-`I`-axis.
- **Remaining dependency (named):** **positive energy** on the reconstructed Hilbert space via **R**
  (the spin-statistics engine selecting CAR — built but gated on the **(A)** half-integer-carrier
  attachment) **+ rung C** (the spectrum condition; the general
  [`axiom_first_spectrum_condition_theorem`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
  is `retained_bounded`, the reconstruction-specific rung C is conditional). This note does **not**
  force CAR.

So (B)'s **massive boost-covariant doubling** is delivered by the derived emergent time; the
**positive-energy / CAR** half rides on R + (A) — the session's two named, separated FS residuals.

## Boundary (honest)

- **A bridge between retained endpoints, not a new free-field theorem.** The Euclidean kernel, the
  Lorentzian Dirac Poincaré rep, and the `e₄`-doubling algebra are all retained; the new content is
  that the **derived** emergent time *realizes* the `e₄` connecting them (the §6 residual).
- **Positive energy is not delivered here** — it is the R + rung-C dependency, named not discharged.
- The half-integer carrier (`(A)`) is the panel's other residual and is untouched here.

## Forbidden imports check

No new axiom. A_min + retained Clifford/Dirac facts (reproduced self-contained). The emergent-time
identification (`e₄=iγ⁰` = the derived record-`I`-axis with `e₄²=−1`) is the session's foundation
(time axis #3149, signature #3154), not a new import. Exact finite-dimensional.

## Runner check breakdown

Class A: (1) Euclidean compact `Spin(4)` (all `Σ^E` anti-Hermitian, unitary boosts); (2) the
emergent-time axis = `e₄=iγ⁰`, `e₄²=−1`; (3) the Wick rotation flips compact→non-compact (`K_j`
Hermitian, `exp(K_j)` non-unitary); (4) non-compact `so(3,1)` sign + massive bispinor (both
chiralities, `m`-coupled, idempotent only on `C⁴`); (5) the bridge assembled. Expected
`runner_check_breakdown = {A: 5, B: 0, C: 0, D: 0, total_pass: 5}`.

## Honest auditor read

The retained Euclidean staggered kernel has compact-`Spin(4)` symmetry (anti-Hermitian generators,
unitary boosts); the derived emergent-time axis is the timelike `e₄=iγ⁰` (`e₄²=−1`); and the boost
`K_j=i·Σ^E_{4j}` is Hermitian (non-compact), so the emergent-time factor `i` Wick-rotates the compact
Euclidean boost into the non-compact Lorentzian one, landing on the retained `so(3,1)` massive Dirac
rep (`[K,K]=−εJ`, both chiralities coupled by `m`, projector idempotent only on `C⁴`). This realizes
KOIDE §6's named residual — that the framework's emergent time realizes the boost-covariant massive
doubling — with microcausality from the merged #3127 bridge. The note is explicit that it bridges
retained endpoints (not a new free-field result) and that the positive-energy/CAR half remains the
R + rung-C + (A)-carrier dependency. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_time_realizes_massive_dirac_doubling_runner.py
```
