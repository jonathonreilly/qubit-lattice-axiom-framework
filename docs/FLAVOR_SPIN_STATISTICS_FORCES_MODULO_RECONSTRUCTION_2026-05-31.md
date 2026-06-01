# Flavor — spin-statistics does NOT yet force the fermionic frame P1 from A1+A2+emergent-spacetime: the engine is genuine and Dirac–Kähler is evaded, but P1 = forced-modulo the free-field reconstruction R (+ the L1 boost-spinor embedding is a compatible choice)

**Date:** 2026-05-31
**Claim type:** bounded — a genuine partial forcing + two precisely-located gaps. Not a closure.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_spin_statistics_forces_modulo_reconstruction_2026_05_31.py` (SCORECARD 6/6).
**Source:** workflow `wf_83c9f756` — 6 routes + 3-lens adversarial verification + synthesis (13 agents). Directive: derive from the axioms up, ledger non-constraining.

## Question
Does spin-statistics from the emergent Lorentz (3,1) **force** the fermionic matter frame P1 — the one
import the whole charged-lepton flavor sector reduces to — from A1+A2+emergent-spacetime?

## Verdict: P1 forced *modulo one ingredient* (the engine is real; two gaps remain)

The chain `emergent-Lorentz → qubit-is-spinor (L1) → spin-statistics (L3) → fermionic frame (P1)` is
genuine and partly executes, but it does **not** close on the current surface. Routes split 4–2 against
forcing, and both forcing-claimants were refuted 3/3 on exactly the flagged obstacles.

### What is genuinely established (real progress)
- **The spin-statistics ENGINE (T1) is a true forcing for a *given* relativistic spin-½ field** —
  not mere compatibility. Verified (runner T1a/b): Bose quantization of a Dirac field (modes
  `{+E,+E,−E,−E}`, `sign(ūu)=−sign(v̄v)`) gives `H=E(n_p−n_a)` **unbounded below** (no stable vacuum)
  and breaks microcausality, while CAR is healthy and bounded below at 0. The bosonic frame **for that
  field** is genuinely excluded.
- **The Dirac–Kähler / Becher–Joos obstacle is EVADED.** Verified (runner DKa): taste enters as a
  **4-fold spectator spectral multiplicity** of a clean j=½ block — it multiplies the spectrum, it does
  *not* mix spin into an inhomogeneous-form object. So the classic "tensor-as-fermion" spin-statistics
  puzzle does **not** block this route at the IR/block level. (Caveat: clean factorization is the a→0
  statement; finite-a has O(a) non-spectator taste mixing.)
- **L1 spatial half is derived:** `per_site_su2_spin_half` — the qubit ℂ² is the unique j=½ su(2)
  module under `S_i=σ_i/2` (runner L1a, Casimir = ¾). Matter is **not** a Lorentz-scalar; the
  spin-statistics theorem is not vacuously inapplicable.

### Why P1 is not yet forced — two precisely-located gaps
- **(L1) The full-Lorentz boost-spinor embedding on the bare qubit is *posited*, not forced.** The
  spatial rotation spin-½ is derived, but identifying the emergent so(3,1) **boosts** as acting on the
  internal ℂ² (qubit = Weyl (½,0) of SL(2,ℂ)) is a *choice of how to embed Lorentz in the qubit
  operators*. The only on-main construction that actually carries a Lorentz spinor index builds it from a
  **2⁴-hypercube-blocked Grassmann staggered field** — i.e. it **presupposes the fermionic frame** to
  forge the very spinor whose Bose-quantization T1 then declares inconsistent (an **L1→L3 circularity**,
  caught by both the circularity and genuinely-from-axioms lenses). On main, emergent SO(3,1) is exhibited
  on the spacetime/momentum arguments of a *scalar* dispersion, with no internal index forced onto the qubit.
- **(IR→UV) T1 does not back-propagate to the UV lattice.** T1 is a *continuum* statement about a *given*
  field; it does **not** show the bosonic *lattice* frame has no consistent Lorentz-invariant continuum
  limit. The free propagator kernel `S(p)=(m − iγ·p)/(p²+m²)` is **statistics-blind** (runner UVa): a
  bosonic Gaussian on the same `S(p)` is well-defined, and the bosonic staggered *scalar* 2-point is
  itself SO(4)-covariant in the continuum — so a bosonic lattice frame demonstrably **does** flow to a
  Lorentz-covariant limit. Two retained no-gos anchor this: `staggered_dirac_substep1_statistics_agnostic`
  (qubit ≅ hard-core boson ≅ JW-fermion span the identical ungraded algebra — runner AGa) and
  `fs_rotation_exchange_discrete_insufficiency` (the rotation→exchange bridge is continuous, dies on Z³).

### The single load-bearing missing ingredient
**R** = the free-field Osterwalder–Schrader → Wightman reconstruction of the statistics-blind kernel
`S(p)` into a **positive-energy, microcausal, Poincaré-covariant spin-½ field** that meets T1's
hypothesis (the Dirac antiparticle / relative-sign Fock structure) **without presupposing** the
fermionic frame. `R` (`FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION`, unaudited/partial) currently builds OS
positivity only on the **pre-chosen fermionic branch**, with the boost-sector Poincaré rep a textbook
black box and the lattice→continuum bridge unbuilt — so it **presupposes** the sign structure it must
produce. That circularity is precisely the gap between "forced-modulo" and "forced."

## Net standing of the charged-lepton flavor sector
The whole sector **closes from A1+A2+emergent-spacetime modulo two items**:
1. **R** — the free-field reconstruction that lifts P1 from *forced-modulo* to *forced* (delivers the
   antiparticle/relative-sign Fock structure from the statistics-blind kernel, and an emergent-boost
   spinor that does not ride on the multi-site Grassmann construction);
2. **r=1/2** — the separate continuous Yukawa modulus (+ the readout class).

Given P1, everything downstream (P2 first-order chiral Dirac, the hw=1 locus, the count 3, the carrier,
the Koide Q=2/3 chiral structure) follows. So the spin-statistics route is **viable and partly executed**
— the engine works and the Dirac–Kähler puzzle is cleared — and the residual is one named, buildable
object R plus the continuous r=1/2.

## Not terminal — the two next levers
This is a current-state reduction, not an impossibility. The two precise moves that would close it:
- **(a)** build the emergent so(3,1) **boost** generators out of the on-site Pauli on ℂ² (so L1's
  spinor does not ride on the multi-site Grassmann staggered field);
- **(b)** build/audit **R** so the Dirac antiparticle/relative-sign Fock structure is **forced from
  `S(p)`** rather than presupposed — at which point T1 back-propagates and P1 is forced.

## Provenance (verified 2026-05-31; T1 + kernel + anchor checked directly)
- T1 energy-positivity exclusion verified directly (runner T1a/b), matching `FREE_SECTOR_SPIN_STATISTICS_LEVEL1` (PASS=8).
- Statistics-blind kernel and statistics-agnostic anchor verified (runner UVa/AGa); anchored by retained `staggered_dirac_substep1_statistics_agnostic_no_forcing` and `fs_rotation_exchange_discrete_insufficiency`.
- L1 spatial spin-½ from `per_site_su2_spin_half` (retained); emergent SO(3,1) from `LORENTZ_BOOST_COVARIANCE_3PLUS1D` / `EMERGENT_LORENTZ`; L2 microcausality from `lieb_robinson_equal_time_tensor_locality` (retained_bounded, ungraded).
- `R` = `FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION` (unaudited/partial) — the named remaining ingredient.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
