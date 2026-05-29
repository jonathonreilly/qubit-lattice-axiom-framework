# Finite Z4 Staggered-Grading Trace Theorem (Bounded)

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py`](../scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.txt`](../logs/runner-cache/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.txt)
(PASS=50 FAIL=0)

## Review-Loop Boundary

This note is the salvageable finite-lattice core from PR #1959. The
submitted branch framed the result as an internal ABJ / Wess-Zumino /
Fujikawa replacement. Review-loop narrows that claim: the runner and
proof support a finite-dimensional staggered-grading trace identity on
even periodic Z4 lattices. They do **not** prove a non-zero anomaly, a
continuum ABJ coefficient, a non-abelian Wess-Zumino cocycle, or a
local-counterterm cohomology obstruction.

Consequently this note does not retire any external ABJ import and does
not promote any downstream anomaly-forces-time consumer. Those stronger
uses require separate source notes plus independent audit.

## Framework Boundary

The framework baseline remains
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
reality is a qubit at every site of the Z3 spatial substrate, with the
one-qubit operator algebra at each site. This note does not introduce a
new framework substrate or axiom. It studies an auxiliary finite
periodic Euclidean Z4 staggered-Dirac construction used as a bounded
algebraic support calculation.

The lattice grading here is
`epsilon(x) = (-1)^(x_0+x_1+x_2+x_3)`. It acts on the site-index factor
of the finite Z4 torus, not on the one-qubit local algebra. This is
compatible with
[`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md),
which forbids a per-site gamma5 inside M_2(C). The related retained Z3
staggered identity is
[`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md); the Z4 anticommutation used
below is checked directly by the paired runner.

## Statement

Let `Lambda = (Z/L)^4` with even `L`, let `D[U]` be the massless
nearest-neighbor staggered Dirac matrix on `Lambda` coupled to U(1)
link phases, and let `epsilon = diag(epsilon(x))`.

For the finite boxes and backgrounds exercised by the runner
(`L in {4,6}`, free links, random U(1) links, and the explicit
flux-winding U(1) background), the following bounded facts hold to the
printed tolerances:

1. The heat-kernel regularized Jacobian functional
   `alpha -> sum_x alpha(x) epsilon(x) <x|exp(-t D^\dagger D)|x>`
   is real-linear in `alpha` for the tested `t` values.
2. The staggered grading anticommutes with the Dirac matrix:
   `epsilon D[U] epsilon = -D[U]`.
3. The trace
   `A_t[U] = Tr(epsilon exp(-t D^\dagger D[U]))`
   is independent of the tested `t` values, equals the zero-mode
   chirality count `n_+ - n_-`, and is integer-valued within numerical
   tolerance.
4. `A_t[U]` is invariant under tested U(1) gauge rotations.
5. The explicit flux-winding U(1) background is non-trivial as a link
   background, but the observed staggered index on the tested small
   even boxes is zero. Non-zero-index existence is not claimed.

The theorem-grade content is the finite matrix identity and its
bounded numerical verification on the listed boxes. The note is not an
ABJ anomaly theorem.

## Proof Sketch

For each nearest-neighbor hop on an even periodic Z4 torus, changing a
single coordinate flips `epsilon(x)`. Therefore the massless staggered
Dirac matrix satisfies `epsilon D epsilon = -D`; the runner checks this
directly for the tested free, random U(1), and flux-winding U(1)
backgrounds.

Because `D` is finite-dimensional and anti-Hermitian in this staggered
construction, `D^\dagger D` is Hermitian positive semidefinite and
commutes with `epsilon`. On each positive eigenvalue subspace, `D`
maps the `epsilon=+1` part bijectively to the `epsilon=-1` part, so
the non-zero modes cancel in
`Tr(epsilon exp(-t D^\dagger D))`. Only zero modes remain, giving
`A_t[U] = n_+ - n_-`, independent of `t` and integer-valued.

For a U(1) gauge rotation, `D[U]` is unitarily conjugated by a
site-diagonal unitary `Omega`. Since `Omega` commutes with the
site-diagonal `epsilon`, cyclicity of trace gives invariance of
`Tr(epsilon exp(-t D^\dagger D))`. The paired runner also checks
spectral invariance under the same transformations.

The linearity of the regularized Jacobian functional in `alpha` is the
finite-dimensional linearity of the displayed sum after the heat-kernel
regularizer has been fixed.

## Honest Residuals

- No non-zero index is exhibited. The finite boxes tested by the
  runner all produce observed integer index zero.
  - **Correction pointer (2026-05-28; editorial, reviewer to decide):**
    [`ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md`](ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md)
    explains this `index = 0` on the free/flat background as the
    `eps`-gap (`{eps, D} = 0` => `H(m)^2 = K^2 + m^2 I` => spectral flow 0)
    plus `chi = 0` (`+/-` pairing) -- NOT a Ginsparg-Wilson / overlap
    necessity. The downstream U(1)_Y note's "(P1') requires overlap-Dirac
    (Adams 2002)" attribution is corrected there; the open residual is
    "exhibit a `chi != 0` / `Q != 0` background".
- No local-counterterm, Wess-Zumino cohomology, or anomaly-noncanceling
  conclusion is proved here.
- No continuum limit, Seeley-DeWitt coefficient, or
  `1/(16 pi^2) tr(F wedge F)` formula is proved here.
- No non-abelian gauge-group generalization is proved here.
- No physical (3,1) Lorentzian decomposition is proved here.

## External Context

Fujikawa's path-integral formulation, Wess-Zumino consistency, the
Atiyah-Singer / APS index framework, and staggered-lattice anomaly
literature motivate the construction. They are context for why this
finite trace identity is worth carrying; they are not imported as a
load-bearing audit shortcut. Any successor that wants to retire an ABJ
import must prove the missing anomaly/cohomology bridge explicitly.

## Audit Handoff

This source note requests independent audit of the bounded finite Z4
trace theorem above. It does not apply audit results, edit existing
audit rows, set `audit_status`, set `effective_status`, or request
promotion of any downstream source note.
