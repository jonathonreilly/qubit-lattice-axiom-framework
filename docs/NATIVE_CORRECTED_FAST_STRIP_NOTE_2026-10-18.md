# Native corrected fast channel and slow composite pole

Claim type: bounded_theorem.

Primary runner: `scripts/native_corrected_fast_strip.py`

**Status:** bounded-support.

The [native correction calculation](NATIVE_SLOW_COMPOSITE_CONTROL_NOTE_2026-10-18.md)
left a next-neighbor term in the decay channel. Its size exceeds the imaginary
part of the candidate resonance, so a naive global resolvent perturbation is
invalid. This block closes that estimate for the specified projected model,
then includes the derived long-arm fourth-order coefficients. It does not
prove a resonance of the entire microscopic Hamiltonian. All calculations
are exposed model development, with no independent observation test.

## Precisely specified channels

Use the same supplied one-qubit compass Hamiltonian and small positive
lambda=Jx/Jz=Jy/Jz. In fast units lambda Jz, the host dispersion is

    epsilon(k)=-4(cos kx+cos ky)-lambda(cos kx-cos ky)^2.

The host form factors are d=cos kx-cos ky and d2=cos2kx-cos2ky.
There is a native contact +lambda|d><d|. The confined arm n>=1 has

    diagonal f(n+1)-5lambda/2, f=lambda^3/16,
    nearest hopping -2, next-nearest hopping -lambda/4.

The host-arm matrix, with rows(d,d2), columns(e1,e2), is

    W=[[-2,-lambda/4],[-lambda,0]].

Slow A2 and D2 couple respectively through -d2-e1 and -2e1. These are
previously computed native coefficients, not new interactions. Retaining
these coefficients and a linear confining arm defines the model analyzed
here; this truncation is not an exact identity for the full Hamiltonian.

## Host and corrected-arm estimates

The outgoing host at z=-6lambda+O(lambda^(7/3))-i O(lambda^3) has, after
contact resummation,

    Gh=[[G,c],[c,b]],
    G=-i log(1/lambda)/pi+O(1),
    c=1/2+O(lambda log(1/lambda)),
    b=19lambda/16+O(lambda^2 log(1/lambda)).

An analytic one-dimensional quadrature, obtained by integrating the
quadratic cosine denominator, agrees with direct upper-half-plane periodic
quadrature. Its lower-half-plane values are the outgoing continuation;
the confined arm instead uses its ordinary self-adjoint resolvent there.
These sheets must not be conflated.

The arm estimate is uniform for eta/f in any fixed compact positive interval.
Put epsilon=lambda/4, T=S+S*, v=f(n+1)-2lambda, and

    A=(sqrt(1+epsilon(v-x))-1)/epsilon,
    D=2+epsilon A, L=T-A, C=D+epsilon T.

Then H0-x=-(CL+LC)/2, while the physical half-line arm is H0-epsilon P1.
The double commutator [C,[C,L]] is bounded O(epsilon^2 f), including the
endpoint. Square-root functional calculus yields

    H0-x=-sqrt(C) L sqrt(C)+R, ||R||=O(epsilon^2 f).

With J=sqrt(D)Lsqrt(D), U=sqrt(C)D^(-1/2), the transformed resolvent is
that of J-i eta M-E, where M=I+O(epsilon), E=O(epsilon^2 f).
This gives a perturbation O(epsilon eta), small relative to eta.
A variable-Jacobi transfer argument over O(1/f) sites bounds local Green
entries and gives a positive dissipative bound at the first site. The
transformed endpoint vector has a spatial tail O(epsilon^K) beyond any
fixed K; taking K>=8 makes the crude tail error O(epsilon^K/eta) vanish.
The localized resolvent identity therefore costs O(epsilon), not
epsilon/eta. The final endpoint perturbation is finite rank.

The full argument, including domains, the weighted tail estimate, and the
explicit variable-Jacobi step, is in
CORRECTED_FAST_STRIP_PROOF (`outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_STRIP_PROOF.md`).
It proves bounded two-site arm Green matrix g and
Im(w*gw)>=c>0 for w=(-2,-epsilon). It does not assert positive definiteness
of the whole two-site imaginary part, or any uniform real-axis limit.
The original failed 4x4 transfer route is preserved in the independent report.

## Consequence for the specified composite

Writing W^T Gh W=Gww^T+O(lambda), finite-rank elimination gives a bounded
arm response and suppression along w by 1/log(1/lambda). Cancellation in
the A2 vertex is essential. The slow self-energy matrix obeys

    M_AA=O(lambda), M_AD=O(lambda), M_DD=O(1/log(1/lambda)).

Its correction in slow units is lambda M. The earlier partial-model
Rouche comparison therefore retains a pole displacement
O(Jz lambda^5/log(1/lambda)), smaller than its lambda^4 width, now including
complete native fast K2. The same vertices give the original induced source
limit (1,2)/sqrt2 after division by lambda^2; convergence is logarithmic.
See CORRECTED_FAST_SCHUR_PROOF (`outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_SCHUR_PROOF.md`).
This is a derived overlap within the model, not an empirical detector map.

The complete long slow-arm K4 row adds, in slow units Jz lambda^2,

    diagonal lambda^2(ell/8+29/192),
    nearest correction 19lambda^2/32,
    next-nearest correction -13lambda^2/128.

Its symbol at the leading band bottom is 109/96. Applying this long-row
formula down to ell3 is an explicit model boundary completion, not a
derivation of the complete native short rows. Let alpha be the first
positive Airy zero magnitude and a=-0.2796521330954-0.4544316488004i.
The specified model, with these long-arm terms and the corrected fast channel,
has the asymptotic prediction

    E/Jz=8-6lambda^2+alpha(lambda^2/8)^(2/3)lambda^2
          +lambda^4[109/96+(2+a)/8]+o(lambda^4).

The real lambda^4 coefficient is 1.35046015003; the width coefficient is
0.11360791220. Numerical poles at lambda=.2,.1,.05,.025,.02 approach these
values, with scalar Schur-equation residuals below3.6e-10. These are neither
eigenvector residuals nor certified pole-location error bounds. The corresponding real coefficients
are1.34226,1.34525,1.34812,1.34935,1.34959. These finite calculations check
the specified model and do not certify its asymptotic remainder by themselves.
The range-two slow-arm asymptotic still requires a uniform complex Airy proof.
The numerical cutoff is20 Airy lengths; its tiny fixed scaled truncation error
is not literally an asymptotic little-o bound. An asymptotic proof must use
the infinite arm or increase that scaled cutoff.
The short runner recomputes representative host, arm, algebra and pole controls;
the longer parameter grids are preserved alongside their generating scripts.

## Surviving obstacles

Finite-boundary higher-order terms, other channels, the actual uniform
Schrieffer-Wolff remainder, and the full dressed source still require control.
No full-H pole is claimed. The mass remains near8Jz despite increasing internal
size; this calculation supplies neither a light mediator nor the relation of
Jz to an observed scale. Preparation, cosmological state, detector identification,
and universal coupling remain unproved. The microscopic action, geometry and
anisotropy were supplied. None is counted as a retired assumption here.

## Portable proof and execution closure

The complete mathematical sources below retain their actual assumptions and derivations. Historical execution/review labels are not fresh evidence. The primary uses an isolated temporary copy of the bound source package, streams child diagnostics, enforces one aggregate wall-clock cap and records required fresh JSON identities. Large frozen grids remain historical source-bound results, not replays. No stronger physical or asymptotic scope is inferred.

- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_SCHUR_PROOF.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/CORRECTED_FAST_STRIP_PROOF.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_HOST.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_SCHUR.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_CORRECTED_FAST_STRIP.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/INDEPENDENT_NATIVE_K4_POLE.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9744/native/REVIEW_CORRECTED_FAST.md`
