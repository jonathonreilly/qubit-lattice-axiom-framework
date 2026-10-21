# A derived zone-boundary composite and its large-feature threshold

Claim type: bounded_theorem.
Primary runner: [native_zone_boundary_composite.py](../scripts/native_zone_boundary_composite.py).


Status: conditional-support. Local native coefficients and exact symmetries lead
to a bound mode of the limiting effective operator, with a derived coupling to the
original composite readout. Finite full-H tests support it. A native infinite-volume
pole and a physical scalar remain open. No interaction or qubit is added.

Premises remain the supplied directional Hamiltonian, positive rung parity,
periodic2×2×L geometry, invariant state/source and small λ=Jperp/Jz. The calculations
extend [the complete scalar-band proof](NATIVE_SCALAR_BAND_LOCAL_PROOF_NOTE_2026-10-18.md).
All sizes, momenta and ratios are exposed development data. No empirical dataset,
physical scale, cosmological state or matter/detector identification is supplied
by this result. In particular qπ is a lattice-zone-boundary feature, not a
long-wavelength relativistic scalar.

## Derive the local operator before taking a limit

At second order, nonadjacent active rungs commute and have additive virtual energy
changes a,b. A return to the same unperturbed energy requires a+b=0. The two path
orders cancel through −1/a−1/b=0. When both vanish, both intermediates belong to P
and are excluded by Q; they are not divergent virtual contributions. Only same-rung
returns and adjacent pairs survive, depending on at most a four-rung motif.
Vacuum subtraction removes remote loops.

Exact Fraction enumeration of signed interval states at L18,20, with complete
output reconstruction, gives the following normalized kernels away from folded
endpoints. Independent full-band application at L12,14 checks the entire vectors.
Local support extends the coefficients when the corresponding neighborhoods are
unchanged; lengths1,2 are explicitly retained, while lengths and remote arcs at
least3 have separated-wall motifs.

- E1 has diagonal1/4 and translations±1 with coefficient−1/8.
- Edge lengths at least2 have diagonal−1/2.
- E_ell→E_(ell+2) has two entries−1/8 at starts0,−2; reverse starts0,+2.
- E2↔D2 has coefficient−sqrt2. Raw interval norms are32 and16, so unnormalized
  coefficients−2 and−1 are consistent with the same Hermitian normalized vertex.
- Every even D has diagonal−2; only D2 couples to E2 at this order.

This is a local formal coefficient derivation, not a volume-uniform remainder
bound. An initial test omitted target length8 for a length6 input; its complete
reconstruction assertion failed. The failed script is preserved. The corrected
range uses lengths strictly before the periodic folded endpoint.

In momentum space the edge diagonal is (1−cosq)/4 at length1 and−1/2 elsewhere;
length-step2 hopping is−cosq/4. The first-order length-step1 hopping is2cos(q/2).
The original centered Oq/sqrt(L) has leading source2λcosq E1. This normalization
also follows locally: a native edge flip changes the two affected NNN bonds per
flipped physical column by a total−8cosq, multiplying the ground-state virtual
coefficient−1/8. It is not an adjustable coupling.

## Exact zone-boundary selection

At qπ, reflection j→−j gives E_ell parity(−1)^(ell−1); all even D have parity−1.
The centered Oπ is reflection even. The corresponding terminal transition
exclusion for a reflection-positive state is preserved with its complete character
proof as deferred scientific source, pending promotion; it is not an active
exclusion claim of this constructive coefficient note.

There is also an all-order finite-band statement. The physical checkerboard
operator Q=product_j Z_(0,1,j)Z_(1,0,j) changes V→−V and leaves H0 unchanged.
Within the complete scalar E8 qπ space, Q has sign(−1)^ell on E and+1 on D, so
reflection R=−Q. An equivariant canonical effective H commutes with R and transforms
under Q as λ→−λ. Consequently every odd coefficient vanishes in this sector.
This does not establish a uniform analytic continuation as L grows.

The reflection-positive odd-edge chain has bulk diagonal b=−1/2, hopping t=1/4,
and endpoint diagonal+1/2. Its boundary defect v=1 produces

    r=t/v=1/4,  E2=b+v+t²/v=9/16,  Z=1−r²=15/16.

The leading gap is8Jz+(9/16)Jperp²/Jz. The original-source weight is
4Zλ²=15λ²/4. These are derived effective-mode and readout coefficients. They are
not a physical mass or universal matter coupling.

The reflection-negative even-edge chain and D2 have two bound roots

    E2=(−38±16sqrt10)/31,

both satisfying |(E2+2)/8|<1. They lie on opposite sides of the host continuum
[−1,0]; further even D levels remain flat at−2 at this order. This source does not
see those two branches at qπ. Higher orders can lift the flat degeneracy.

## Finite full-H validation

A direct periodic32-site calculation uses the original H and centered Oπ/sqrt(L),
not an effective mode inserted into H. At finite L8, the positive-reflection K2
block is [[1/2,1/4],[1/4,−1/4]]. Its upper shift is(1+sqrt13)/8 and original-source
coefficient2+6/sqrt13, distinct from the infinite-halfline coefficients above.
These predictions were fixed before the full-H response run.

| λ | Native upper gap/Jz | Full-H residual | Weight/λ² | Gap error/λ⁴ |
|---|---:|---:|---:|---:|
| .1 | 8.005737479158025 | 6.26e−13 | 3.66852357391 | −.19459936 |
| .2 | 8.022719764135115 | 1.17e−13 | 3.68057316676 | −.19249515 |

The finite prediction for weight/λ² is3.66410058868. Errors are consistent with
higher even-order corrections at these two points, not an asymptotic proof.
Candidates0 and2 are residual-qualified at both ratios. Every other reconstructed
node is rejected, including a near duplicate at λ=.2 with residual.00797; its
weight must not be counted twice. Small residuals establish nearby spectrum,
not exact individual weights, completeness, global ground selection or bulk
stability. The full-H output is declared frozen auxiliary data with replay code.

## Derive the crossover rather than extrapolate through a singular limit

For q=π−λκ, the formal leading operator is

    gap/Jz = 8 + λ² M(κ) + higher terms.

M has edge nearest hoppingκ, next-nearest hopping1/4, bulk diagonal−1/2,
endpoint diagonal+1/2, and D2 of energy−2 attached to edge site1 by−sqrt2. Other
even D states are decoupled at−2 at this order. The coefficient functions give a
formal next orderλ⁴, but no uniform bound in the simultaneous large-L/small-λ
limit is claimed. Allowed finite-ring momenta require compatible sequences.

The essential dispersion is x²+2κx−1, x∈[−1,1], with upper edge2|κ|. At a positive
upper threshold, a bounded host solution is A+B r^n, where r∈(−1,0) and
κ=−(r+1)²/(4r). Elimination of D2 gives η=1/(κ+1), and the boundary matrix is

    [[κ−3/4, κ/r+1/(4r²)−1], [1/4−η, 1/(4r)−ηr]].

Its determinant is −(16r⁴+92r³+39r²−2r−1)/(16r²(r−1)). The full root-count, monotone-form and threshold proof is preserved as deferred
scientific source pending negative promotion. The displayed boundary matrix and
determinant remain constructive identities; this note does not promote a terminal
mode-exclusion count.
The upper source mode has curvature E2(κ)=9/16+(208/27)κ²+O(κ⁴), obtained from the
even-chain resolvent including D2, rather than fitted finite differences.

## A large feature and its coupling emerge together, conditionally

Near κ2 from below, write δ=κ2−κ and r1=exp(−β). The decaying host wave is
ψ_n=A(r1^n+B/A r2^n); D2 has amplitude−sqrt2 ψ1/(E+2). Exact geometric normalization
and the boundary determinant give

    β/δ → .481280830410806,
    (E−2κ)/δ² → .473735533207417,
    B/A → −.167993376787152.

The mean host index diverges as1/(2β), while the original local-source boundary
probability Z tends to2β(1+B/A)². Therefore

    Z × mean_host_index → .692235021070046.

Host index n is interval length ell−1; adding the finite D2 contribution to a
length expectation leaves this divergent asymptotic unchanged. Thus this limiting
operator produces arbitrarily large relative-coordinate features and a weakening
local readout together, without an added binding interaction. The readout spectral
weight is4λ²Z at this leading order. Size is selected by approaching a momentum
threshold; no natural preparation mechanism or parameter-free large size has been
derived. Finite-size and higher-order control become harder, not easier, there.
The energy still begins at8Jz: an extended feature is not thereby a light scalar.

## Prior art and artifacts

Compass ladders, defect-sector mappings and bound excitations are established
research directions: [Brzezicki and Oleś, 2009](https://arxiv.org/abs/0906.4462),
and [Sur, Laad and Hassan, 2021](https://doi.org/10.1103/PhysRevB.103.144419) discuss
related models and mechanisms. These are context, not proof inputs; their supplied
models do not certify this tube's coefficients. No general novelty claim for
bound states or spin-ladder mappings is made.

[Runner](../scripts/native_zone_boundary_composite.py) reproduces the local,
symmetry, recurrence and size/readout controls. Provenance (`outputs/neutral_composite_continuation_review_2026_10_18/provenance/pr9727/ZONE_BOUNDARY_PROVENANCE.md`)
separates reproduced checks, frozen native data, failures and independent checks.
Remaining targets are uniform native control near the threshold, larger transverse
features, state selection, interactions among features, and observational source
and detector identification.

## Source and promotion boundary

Reflection and checkerboard coefficient identities and the constructive conditional half-line roots/residues remain live. Negative crossover mode-count promotion is packet-pending; the complete recurrence, boundary and monotonicity proofs remain inspectable for the displayed half-line operator. No native infinite-chain pole exclusion is inferred.

Full supporting mathematics and provenance are indexed in `outputs/neutral_composite_continuation_review_2026_10_18/INPUT_CLOSURE.json`. The scope register is `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. The primary binds literal source/input identities, stages owning-head helpers and frozen inputs in a temporary directory, and captures their diagnostics. Frozen expensive producers are provenance only and are not rerun. Historical reports and executions do not supply a fresh verdict.
