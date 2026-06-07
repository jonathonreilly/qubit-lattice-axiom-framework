# Boost-Covariance Is Blind to the Fermionic Datum — the Cross-Site-Kernel "Escape" Is True-but-Duplicative, and FS Sharpens to (A)+(B) — No-Go Sharpening

**Date:** 2026-06-06
**Claim type:** no_go (sharpening; bounds the boost-covariance route and re-locates the FS residual)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/fs_boost_covariance_blind_to_fermionic_datum_runner.py`](../scripts/fs_boost_covariance_blind_to_fermionic_datum_runner.py)
**Cached output:** [`logs/runner-cache/fs_boost_covariance_blind_to_fermionic_datum_runner.txt`](../logs/runner-cache/fs_boost_covariance_blind_to_fermionic_datum_runner.txt)

## Audit context

Fermionic statistics (FS) of the matter carrier is the deepest open admission of the
staggered-Dirac realization that the flavor sector rests on. FS = forced-modulo (emergent-Lorentz
+ R), reduced to the single open **Link C** (the boost-spinor). A natural escape — *the
statistics-blind cross-site staggered kernel `D(k)=M+iΣ_μγ_μ sin k_μ` selects the faithful boost
over the scalar, closing Link C* — was attacked by a 13-agent find-the-escape panel. This note banks
the panel's verdict: the escape is **true but duplicative**, and the panel's genuinely-new content is
a **negative** diagnostic — *boost-covariance is blind to the fermionic datum* — that bounds the
route and re-locates the residual.

## Safe statement

**Theorem (boost-covariance is blind to the fermionic datum).** Let `D(p)=M·1 + iΣ_μ γ_μ p_μ` be the
statistics-blind Dirac/staggered kernel (Hermitian Euclidean `γ_μ`, `{γ_μ,γ_ν}=2δ_{μν}`). The
boost/rotation covariance condition `S D(A^{-1}p) S^{-1} = D(p)` (with `A` derived from `S` via
`A_{νμ}=¼tr(γ_ν S γ_μ S^{-1})`) **forces the faithful spinor `S=exp(θΣ)`, `Σ_{μν}=¼[γ_μ,γ_ν]`, over
the scalar `S=λ1`** (which forces `A=1`, no rotation). **But this covariance is provably blind to the
two data that constitute Fermi statistics:**

1. **Blind to the double-valuedness `S(2π)=−1`.** The cover `S→SO(4)` is 2-to-1: `S(2π)=−1`
   (spinor) while `A(2π)=1` (`SO(4)`), and `S` and `−S` implement **identical** kernel conjugation
   (`S D S^{-1} = (−S) D (−S)^{-1}`). The fermionic sign lies in `ker(S→SO(4))` — **neither used nor
   produced** by covariance.
2. **Blind to the spin magnitude.** `Σ_{μν}` is traceless — but so is an integer-spin (vector/`SO(4)`)
   generator (`tr=0`, eigenvalues `±i` vs the spinor's `±i/2`). Tracelessness is **necessary, not
   sufficient**, for half-integer spin; covariance cannot pin the carrier to spin-½.

**Therefore the statistics-blind boost-covariance route — though true and retained — cannot supply
the fermionic datum.** FS sharpens to two statistics-**sensitive** residuals the blind kernel cannot
reach:

- **(A)** the **half-integer-carrier attachment** (which cross-site DOF is the spin index; the only
  retained forcing route runs through the *unaudited* Kawamoto-Smit reconstruction);
- **(B)** delivering the **emergent-time `Cl(3,0)→Cl(3,1)` `e₄`-doubling** (`e₄²=−1`) as a
  **positive-energy** (rung-C spectrum condition `Ĥ≥0`), **microcausal**, boost-covariant **massive**
  Dirac field — the non-compact Lorentzian boost-spinor the retained **Euclidean** (compact `Spin(4)`)
  kernel does not reach (= `KOIDE_ONSITE_BOOST_..._WEYL_FAITHFUL_VS_SCALAR_SELECTION` §6 open residual).

**(B) is the highest-leverage move and sits at the emergent-time + spectrum-positivity intersection.**

## Why the escape is true-but-duplicative (panel finding)

Every load-bearing piece is already retained on `origin/main`:
[`lorentz_boost_free_staggered_fermion_2point_so4`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
(`retained_bounded`, the Euclidean `SO(4)` covariance);
[`koide_onsite_boost_reconstruction_weyl_faithful_vs_scalar_selection`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md)
(`retained_bounded`, §5 resolves L1 / §7 removes G2 at the massless chiral boundary);
[`quantum_local_algebra_does_not_force_boost_action_faith_no_go`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
(`retained_no_go`, which **grants** the kinetic-kernel selector as its own carve-out). The γ_μ
statistics-blindness is the retained-`no_go` `staggered_dirac_substep1_statistics_agnostic`. The
escape's sole claimed novelty (cross-site rescues L1 where on-site failed) is **false** — the sister
note already resolved L1 via the on-shell numerator. The escape **relocates**, does not eliminate,
Link C.

## No-go gate (N1–N8)

- **N1 (alternative routes).** Five exercise slices (assumptions / Elon / literature / math-sector /
  record-ontology reframe) each independently returned `duplicates_existing = true`,
  `status = forced-modulo-retained`. No non-duplicate covariance route was found.
- **N2 (wall-independence).** The bound is independent of the kernel realization: it is the
  group-theoretic 2-to-1 cover `Spin→SO` and the traceless-≠-half-integer fact, not a feature of the
  staggered phases. Holds for any `γ`-kernel.
- **N3 (hidden-wall scan).** The genuine wall is *not* circularity w.r.t. the Grassmann frame (the
  γ_μ are statistics-blind c-numbers — confirmed). It is the **carrier-identification** step
  (half-integer vs integer) and the **double-valuedness**, located precisely here.
- **N4 (residual matching).** The residual `(A)+(B)` matches the standing FS reduction
  ([`flavor_spin_statistics_forces_modulo_reconstruction`](FLAVOR_SPIN_STATISTICS_FORCES_MODULO_RECONSTRUCTION_2026-05-31.md),
  `retained_bounded`): the missing ingredient is the non-circular reconstruction R turning the
  statistics-blind kernel into a positive-energy microcausal spinor field.
- **N5 (rhetoric audit).** No "closes/last/only-route" language. This **bounds** the covariance route
  and **opens** (A)+(B); the framework reproduces the phenomenology, so a derivation exists — (B) is
  the next path, at the emergent-time foundation.
- **N6 (partial-closure path).** (B) is partially supported: the `e₄`-doubling is retained
  ([`cl3_to_cl31_spinor_extension`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md),
  `retained`); the emergent-time axis/arrow/signature/microcausality are this session's foundation
  results; the open dependency is rung-C `Ĥ≥0` + RP.
- **N7 (steelman).** The escape's strongest form (the intertwiner space is *exactly* 1-dim = C·S_spin,
  verified) is granted in full — and is precisely what makes it duplicative of the retained covariance,
  not a new closure.
- **N8 (cross-cycle echo).** Consistent with the four standing CAR no-gos
  (`car_from_positivity_neutrality`, `ring_monodromy_does_not_force_car`,
  `staggered_dirac_substep1_statistics_agnostic`, `ks_eta_vs_jw_string_car_locality`): the exchange
  sign is statistics-sensitive data the statistics-blind kernel cannot carry.

## Boundary (honest)

- This is a **negative/sharpening** result: it bounds the boost-covariance route and re-locates the
  FS residual; it does **not** close FS and does **not** itself derive (A) or (B).
- The faithful-vs-scalar selection (A1) is reproduced as **retained context**, not claimed as new.
- (B)'s open dependency (rung-C spectrum condition, RP) is real; the note names it, does not discharge it.

## Forbidden imports check

No new axiom. A_min + the retained Dirac/staggered kernel facts (reproduced self-contained). The
Wigner/Streater-Wightman cover facts are reproduced numerically, not imported as authority. Exact
finite-dimensional.

## Runner check breakdown

Class A: (1) Hermitian Euclidean Clifford gammas; (2) faithful-over-scalar selection (A derived from
S; retained context); (3) blind to `S(2π)=−1` (`S` and `−S` identical conjugation); (4) blind to spin
magnitude (traceless ≠ half-integer); (5) the sharpened (A)+(B) frontier. Expected
`runner_check_breakdown = {A: 5, B: 0, C: 0, D: 0, total_pass: 5}`.

## Honest auditor read

The boost-covariance condition forces the faithful spinor over the scalar (A derived from S, in
`SO(4)`; reproducing the retained selection), but `S` and `−S` conjugate the kernel identically
(`S(2π)=−1` invisible) and the spinor generator is traceless exactly as an integer-spin generator is
— so covariance is blind to both the fermionic sign and the spin magnitude, the two data that are
Fermi statistics. This bounds the (statistics-blind, retained) boost-covariance route: it cannot
supply the fermionic datum, re-locating FS to (A) the half-integer-carrier attachment and (B) the
emergent-time `e₄`-doubling massive-Dirac delivery, with (B) highest-leverage at the emergent-time +
spectrum-positivity intersection. The note is honest that it is a negative sharpening of an
already-retained landscape, not a closure. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/fs_boost_covariance_blind_to_fermionic_datum_runner.py
```
