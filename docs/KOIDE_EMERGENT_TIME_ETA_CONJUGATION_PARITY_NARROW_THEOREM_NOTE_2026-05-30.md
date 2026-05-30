# Koide Emergent-Time eta-Invariant Conjugation-Parity (sharp-isolation no-go)

**Date:** 2026-05-30
**Claim type:** bounded_theorem / no-go
**Status:** bounded route diagnostic and sharp isolation. This note approves
no new axiom, no import, and no audit verdict. It sets no tier; the audit lane
sets status.
**Primary runner:**
`scripts/frontier_koide_emergent_time_eta_conjugation_parity_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_emergent_time_eta_conjugation_parity_2026_05_30.txt`.

## Question

Charged-lepton Koide `Q=2/3` is equivalent to `r=|b|^2/a^2=1/2` on the `C_3`
generation circulant `M = a I + b C + conj(b) C^2` (`a` real, `b` complex). In
the block free energy the doublet block carries an exponent `nu`: `nu=1` (one
holomorphic/Weyl mode, `conj(b)` the conjugate momentum of `b`) gives `r=1/2`
and a chiral generation field; `nu=2` (two independent real quadratures
`Re b, Im b`) gives `r=1` (`Q=1`). The selector that fixes `nu` is the
conjugation parity of the first-order-in-`d_tau` part of the effective action
`S_eff = Tr log(d_tau + D(b(tau)))` obtained by integrating out the staggered
site fermions over a slowly varying background `b(tau)`: a conjugation-odd
imaginary term `INT (conj(b) d_tau b - b d_tau conj(b))` is a Berry / eta /
spectral-asymmetry term (a symplectic form making `conj(b)` the conjugate
momentum) and forces `nu=1`; a conjugation-even real term is a metric and
forces `nu=2`.

Does the framework's retained structure produce the conjugation-odd term?

## Result

No. The conjugation-odd imaginary coefficient vanishes identically; the
surviving first-order term is conjugation-even real (`nu=2`, the no-import
`Q=1` default). The reason is kernel-independent:

- The map `b -> conj(b)` (equivalently `arg b -> -arg b`) is realized on the
  generation triplet by the **transposition** `P` (the `1<->2` swap of the
  `C_3` orbit). With `I (x) P` commuting with `D (x) I`, conjugation acts as a
  **real-orthogonal similarity** of the full coupled operator:
  `(I (x) P) H(b) (I (x) P) = H(conj(b))` exactly. A real-orthogonal
  similarity fixes the entire spectrum, so **every** spectral functional
  `Tr h(O)` — eta, determinant, free energy, for any kernel `h` — is
  conjugation-invariant. The conjugation-odd part is therefore `0`.
- Equivalently, the candidate Berry one-form `A = sum_k g(lam_k) d lam_k` is an
  exact differential `d(sum_k G(lam_k))` because all `C_3` circulants share the
  `b`-independent Fourier eigenbasis (`[M(b_1), M(b_2)] = 0`, connection
  `<v_k| d v_k> = 0`), so its curl is `0` for every kernel and its loop
  integral vanishes.
- The generation mass `b` scales eigenvalues and permutes the multiset
  (`k = 1 <-> 2`); it does not split a `+/-` pairing. So `conj(b)` is the
  transposition partner of `b` (field-count `2`), not its conjugate momentum
  (field-count `1`).

**The null is real signal, not a blind probe.** Positive control: the chiral
deformation `M_chi = a I + b C + c C^2` with `c` an independent complex coupling
(not `conj(b)`, breaking anti-Hermiticity) produces a nonzero conjugation-odd
part (`odd = 4.0`) where the retained anti-Hermitian coupling gives `0.0`. The
machinery detects an odd term when one genuinely exists.

**Over-determined.** The static retained generation circulant alone forces the
result (pure linear algebra): its determinant stays exactly real as `arg b`
winds around the full circle (the runner checks `|Im det| / |det| < 1e-9` over
`theta in [0, 2 pi)` at the Koide radius `|b|/a = 1/sqrt(2)`), so `arg det` has
no continuous Berry winding. The conclusion therefore does not rest on the
unaudited time-emergence content; the emergent-time Matsubara time operator
`d_tau + D(b(tau))` only confirms it survives the full construction.

**Reality, not just `P` (the sharper root).** The transposition `P` is a
*sufficient but not necessary* witness. The deeper reason is that `b -> conj(b)`
is the **transpose** on the circulant (`M(conj b) = M(b)^T`), and transpose
preserves spectrum unconditionally. So for **any** real-symmetric structure added
to the operator — even one that explicitly breaks the transposition lift
(`[W_mix, I (x) P] != 0`) — one still has `D(a, conj b) = D(a, b)^T`, hence
`spec D(b) = spec D(conj b)` and a conjugation-even `eta`. The runner confirms
this: a generic real-symmetric `W_mix` fully coupling space and generations, with
`[W_mix, I (x) P]` of order `1` (P broken), still gives matched spectra to
`~1e-14`. **The conjugation-odd term is therefore unreachable by any real
operator**; it requires a genuinely complex (imaginary-antisymmetric) generation
coupling. This upgrades the no-go from a `C_3`/`P`-equivariance statement (which a
clever import might dodge) to a **reality** statement enforced by the entire
retained real anti-Hermitian Dirac substrate.

**What the odd generator actually is.** The unique `C_3`-equivariant, `P`-odd,
Hermitian generation generator is `i(C - C^2)` — but it is purely the **`arg b`
tangent**: adding `eps * i(C - C^2)` sends `b -> b + i eps` within the same
conjugate-symmetric family (`coeff(C^2)` stays `conj(coeff(C))`), an integer-
winding reparametrization that does not pin `r`. A genuine conjugation-odd Berry
term instead needs `coeff(C^2) != conj(coeff(C))` — the **two-complex-parameter
chiral circulant** `M_chi = a I + b C + c C^2` with `c` independent of `conj(b)`
(non-Hermitian, the holomorphic/Weyl polarization). The correct ban criterion is
this `coeff(C^2) != conj(coeff(C))` chirality, not "non-Hermiticity" or
"`C_3`-non-equivariance" per se.

## Mechanism attribution (corrected)

Two attributions used in working drafts are imprecise and are corrected here:

- The `+/- i mu` spectral pairing of a real anti-Hermitian operator follows from
  **real-characteristic-polynomial conjugate-pair closure** (a real matrix has
  conjugate-closed spectrum), not from the CPT relation alone (which gives only
  `lam -> -conj(lam)` with a trivial `mu -> mu` fixed point on imaginary
  spectrum).
- The conjugation-even cancellation here is the **generation-index transposition
  similarity** verified directly (`(I (x) P) H(b) (I (x) P) = H(conj(b))`), not
  an APS spatial/temporal Hamming-weight chirality `Gamma_5 = (-1)^{|x|}`, which
  acts on the `Z^3 x S^1` lattice index, not on the generation triplet.

## Boundary

This is not a global no-go. It is a sharp isolation: on the retained generation
circulant with the retained time/Dirac structure, the conjugation-odd Berry
term is identically zero, so `Q=2/3` requires breaking the transposition
similarity `P`. The only deformation found to do so is the chiral
`c`-independent-of-`conj(b)` step (the holomorphic/Weyl polarization), which is
the chirality import shared with the generation-identification chirality gate
and is not approved here.

Scope: the result is forced by the retained generation **circulant**; the
retained real anti-Hermitian Dirac class is one-parameter (`alpha (C - C^2)`)
and cannot host the two-parameter complex `b`, so the precise statement is
"forced by the retained circulant, unchanged by the retained time/Dirac
structure," not "derived from the retained Dirac operator." The `anomaly_forces_time`
content is cited as non-load-bearing context only (it is unaudited and the
static circulant already forces the result).

The three external `P`-breaking routes one would reach for are all **real**
operators and so cannot touch the reality root, and none is retained as a
`P`-breaker on the generation sector (each checked, not asserted):

- **Gauge background.** The retained Wilson/plaquette weight is a Hamming-weight
  class function (`W = 2r` on the whole `hw=1` orbit), so its background is
  `2r * I_3` — it commutes with `C` and `P` and only renormalizes `a`. Native
  gauge fields act as `G (x) I_gen` (tensor-trivial on generations). A
  `C_3`-equivariant `U(1)_F` charge is forced equal on the three states
  (commutant of `C_3` is scalar), hence `P`-symmetric; a `P`-breaking charge
  breaks `C_3` and is an import.
- **Boundary geometry.** Every retained boundary (emergent-time `S^1`/open chain,
  spatial BC, growth frontier, BZ corner) tensors as `B (x) I_3`; the APS
  open-vs-periodic `eta` mechanism is live but generation-blind, and the bulk
  staggered `eta` vanishes by the spacetime `Gamma_5 = (-1)^{x+y+z+t}` pairing.
- **Wilson / domain-wall.** The retained Wilson/`O_h` content is parity-even (its
  `det`-odd slot is forced to zero — strong-CP `theta = 0`), and the staggered
  `eps = (-1)^{sum x}` maps `hw=1 -> hw=2` (`3 <-> 3bar`), not within the triplet.
  The framework has no Ginsparg-Wilson relation, so a generation-chiral
  Wilson/DW/overlap term is import-only.

This independently reproduces the framework's own retained scoping
(`HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING`, gap table), which already marks
the Wilson/DW-mass, non-trivial-gauge-background, and manifold-with-boundary
routes as absent (closed flat torus / mean-field factorization / no Wilson mass)
— each "a non-trivial extension of the substrate," i.e. an import. And by the
reality argument above, even breaking `P` would not suffice.

The one genuinely distinct open door (a future program, recorded as a review
trigger, not claimed here): **is there a retained source for a complex /
imaginary-antisymmetric generation coupling** (a complex `C`, or a complex
anti-Hermitian generator on the generation `R^3` along `i(C - C^2)` whose
coefficient deviates from `conj(coeff(C))`)? The gauge/boundary/Wilson routes,
being real, leave this untouched; candidate retained substrates to probe are the
qubit-factor symplectic/Berry phase and the signed-vs-singular-value (`sqrt m`
sign) readout dimension.

## Relation to Koide

The retained Koide algebraic surfaces continue to locate the observed value at
the `C_3` character-norm / block split (`koide_circulant_q_two_thirds`,
`koide_anticommuting_operator_derivation`). This note adds that the dynamical
(emergent-time eta) selector does not choose `r=1/2`: it is conjugation-even on
the retained operator, so it confirms the `Q=1` no-import default from the
action side and isolates the single chirality import as the unique
transposition-breaking step. This converts a diffuse "why `Q=2/3`" into one
precise obstruction and strengthens the shared chirality-gate inventory.
