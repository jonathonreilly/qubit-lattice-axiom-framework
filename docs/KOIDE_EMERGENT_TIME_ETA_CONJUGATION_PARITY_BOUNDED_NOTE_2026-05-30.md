# Koide Emergent-Time Eta Conjugation-Parity Bounded Note

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no import,
and no audit verdict. The independent audit lane sets audit and effective
status.
**Primary runner:** [`frontier_koide_emergent_time_eta_conjugation_parity_2026_05_30.py`](../scripts/frontier_koide_emergent_time_eta_conjugation_parity_2026_05_30.py)

## Scope

This note records a finite algebra fact about the conjugate-symmetric
`C_3` generation circulant

```text
M(a,b) = a I + b C + conj(b) C^2,
```

with `a` real and `C^3 = I`. It is useful for the Koide lane because this
family is the standard three-generation circulant surface on which the ratio
`|b|^2/a^2` is discussed.

The claim is deliberately bounded. It does not prove Koide `Q = 2/3`, does not
close the charged-lepton lane, and does not assert a global no-go against every
future source of a conjugation-odd Berry term. It only says that this
conjugate-symmetric circulant family, and real transpose-preserving extensions
of it, cannot themselves supply that odd term.

## Bounded Theorem

Let `P` be the generation transposition with `P C P = C^2`. Then

```text
P M(a,b) P = M(a,conj(b)).
```

Consequently, for any operator family whose `b -> conj(b)` action is this
transpose/similarity, the spectrum is invariant under conjugation of `b`.
Every spectral functional that depends only on the spectrum is therefore
conjugation-even on this surface. In particular, the conjugation-odd
first-order Berry/eta coefficient of the form

```text
conj(b) d_tau b - b d_tau conj(b)
```

vanishes for the displayed family.

Equivalently, the `C_3` circulants share a `b`-independent Fourier eigenbasis.
For eigenvalues `lambda_k(a,b)`, a candidate one-form

```text
A = sum_k g(lambda_k) d lambda_k
```

is exact for any scalar kernel `g`, so its curl and loop integral vanish.

The same conclusion holds after adding a real-symmetric mixing term `W` that
preserves the transpose relation

```text
O(a,conj(b)) = O(a,b)^T.
```

That extension may break the explicit transposition witness `P`, but transpose
still preserves the spectrum, so it still cannot generate a conjugation-odd
spectral term.

## Runner Checks

The paired runner verifies:

- the determinant and eigenvalue multiset are even under `b -> conj(b)`;
- `P C P = C^2` and `P M(b) P = M(conj(b))`;
- the tensor-lifted operator has matched spectra under `b -> conj(b)`;
- the symbolic Berry curl is zero for arbitrary kernel `g`;
- `det M(|b| exp(i theta))` stays real around the full phase circle;
- a non-conjugate-symmetric two-parameter control `a I + b C + c C^2` has a
  nonzero spectral-asymmetry signal, so the null result is not just a blind
  detector;
- the generator `i(C - C^2)` is the tangent to changing `arg b` inside the same
  conjugate-symmetric family, not an independent holomorphic polarization.

## Boundary For Downstream Use

This result should be cited only as a bounded obstruction to one proposed
mechanism: the conjugate-symmetric `C_3` circulant plus transpose-preserving
real extensions do not generate a conjugation-odd eta/Berry selector for the
Koide radius. It does not rule out future retained work that supplies a
genuinely complex generation coupling, a holomorphic polarization, or another
source whose `b -> conj(b)` action is not the transpose/similarity above.

The working interpretation is therefore:

- the real two-quadrature `b` surface remains conjugation-even;
- a one-complex-variable holomorphic/Weyl interpretation would require an
  additional source that breaks `coeff(C^2) = conj(coeff(C))`;
- this note does not approve that additional source.

## No-Go Discipline Boundary

This is not landed as a `no_go` row. The review-loop narrowing removes the
original exhaustive phrasing. The untested routes are explicit: complex
generation coupling, holomorphic polarization, qubit-factor Berry phase,
signed-versus-singular-value readout, and any non-transpose-preserving
generation-sector source. Those remain open future work rather than claims
closed by this note.
