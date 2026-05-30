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

Open, non-banned routes that could still source a conjugation-odd `eta(b)` by
breaking `P` externally (each a distinct downstream program, recorded as future
review triggers): (1) an alternative emergent-time realization; (2) a Wilson /
domain-wall term; (3) a gauge background that is not `P`-symmetric on the
generation sector; (4) boundary geometry (an APS boundary `eta`). Whether any
such structure is retained (rather than an import) is open.

## Relation to Koide

The retained Koide algebraic surfaces continue to locate the observed value at
the `C_3` character-norm / block split (`koide_circulant_q_two_thirds`,
`koide_anticommuting_operator_derivation`). This note adds that the dynamical
(emergent-time eta) selector does not choose `r=1/2`: it is conjugation-even on
the retained operator, so it confirms the `Q=1` no-import default from the
action side and isolates the single chirality import as the unique
transposition-breaking step. This converts a diffuse "why `Q=2/3`" into one
precise obstruction and strengthens the shared chirality-gate inventory.
