# Source comparison: microscopic energy across the electric family

**Finding:** no mathematical discrepancy was found between the released author
bridge and the sealed independent reconstruction within the supplied physical
three-leaf star. Both original instruments have the stated marked moments,
initial loss term, exact finite-time energy relation, and leading singular
energy cost. This is a conditional scientific source comparison, with no audit,
landing, native-law, or autonomous-realization status.

The independent PRE was frozen before the author sources were released. Its
seal is `92f534204e822fbbc38f4cfbd8a5f6d1d33f09b727d7bead68fd22dfb4734faa`.
All 22 bound files and the seal itself remain unchanged. The PRE argument is
[PRE_RECONSTRUCTION.md](PRE_RECONSTRUCTION.md); its decisive implementation is
[star_local_matrix_control.py](star_local_matrix_control.py), with a separate
full-GKLS and no-event time control in
[star_finite_time_control.py](star_finite_time_control.py).

## Frozen sources and comparison method

The principal released source is
[STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY.md](comparison_sources/campaign12h_fourth/microscopic_electric_robustness_author/STAR_ENERGY_COST_ACROSS_THE_ELECTRIC_FAMILY.md),
SHA256 `a7dfe854f72be6e30b7aa4bbb61e10c5e7876b6cd62698735968af33ae0477c2`.
Its complete author seal has SHA256
`fe08f9e62cfc1278cf659127e23989435cb6f0dcc39942a1e6cbef7eec0b1b21`.
The full current runner, its complete pinned exact-star builder, the prior
exact microscopic note and prior finite-time/supply note were read. The
retained failed source and its one-line correction were compared directly.

[COMPARISON_SOURCE_BINDINGS.json](COMPARISON_SOURCE_BINDINGS.json) binds all
16 released artifacts/dependencies by exact hash and maps them to local
snapshots. These include every artifact listed in the author seal and every
listed dependency. The governing and common operator/electric-family sources
remain bound by the PRE seal. Source aliases and all operational comparison
paths are relative: a published archive can relocate these snapshots by hash
without depending on an absolute private working path. Historical logs retain
their original bytes, including any path printed in a traceback.

The independent computation has no author-builder import. It uses the
independently written and frozen complete local matrices, compares both charge
word orderings explicitly, and then compares author result data. The author
runner and its transitive builder were also replayed in separate child
processes using exact source copies in new owned runtime directories. Their
reproduction establishes consistency; independence comes from the prior
source-blind derivation and local construction, not that replay.

## Claim-by-claim agreement

Write `a=1+3 epsilon^2`, `ell=K lambda`, `Omega=delta epsilon^-4`, with
`K,delta,kappa>0`, `0<=lambda<=1`, integer `S>=1`, and
`epsilon^2 S(S+1)=delta/K`. Here `ell` denotes the scalar `K lambda`; the
previous author finite-time note instead uses the letter ell for a vector.

| Load-bearing claim | Comparison finding |
| --- | --- |
| Complete physical space | Gauss gives `E_0b=-q_b`, `sum q=1`. There are four N=1 and twelve N=3 states. All fields are 0 or ±1, with all actual normalized spin shifts exactly one for every S>=1. The independent PRE constructs these transitions, including their field increments. |
| Compensation and electric correction | `D_ext=0` throughout the physical space, `C_S=F†F`, and `E2=N-1+W`. Thus `H_lambda=Omega(W-epsilon F)†(W-epsilon F)+ell E2`. Its addition has norm at most 3K; the full Hamiltonian is nonnegative. |
| Common initial state | `psi=(g+epsilon Fg)/sqrt(a)`, `||Fg||²=3`. It obeys `H_lambda psi=ell epsilon Fg/sqrt(a)`, so it is not an eigenstate when lambda>0. Its mean is `3ell epsilon²/a`. The PRE also supplies variance `3ell² epsilon²/a²`; this extra fact is not attributed to the author bridge. |
| Actual marks and weights | All six resolved intensities are `2kappa/a`; each of three coherent intensities is `4kappa/a`. The full physical output word amplitudes agree after basis mapping. Total intensity is `12kappa/a`. |
| Complete marked energy moments | For `c=2,1,3/2` for resolved plus, resolved minus and coherent respectively, the mean is `c delta/epsilon²+2ell`; the variance is `c delta² epsilon^-6[1+(3-c)epsilon²]`. All nine outputs agree exactly. |
| Full initial energy derivative | Gain is `(18kappa delta/epsilon²+24kappa ell)/a`. The signed anticommutator contribution is `-12kappa ell/a`. The full derivative is `(18kappa delta/epsilon²+12kappa ell)/a` for either instrument. The PRE stores the positive loss quantity to subtract, so the differing loss signs in the JSON files are a convention, not a discrepancy. |
| Exact finite-time relation | If `p3(t)` is the formed-sector probability, `E_total(t)=E_no(t)+[3delta/(2epsilon²)+2ell]p3(t)`, with `E_no>=0`, for the common preparation and either instrument. The independent complete-matrix source identity holds on the actual invariant two-dimensional no-event subspace. |
| Fixed-time limit | For each fixed positive time, `epsilon² E_total(t)` tends to `(3delta/2)(1-exp(-12kappa t))`. Equivalently the limit after division by `S(S+1)` is `(3K/2)(1-exp(-12kappa t))`. The author's fixed-lambda proof is checked below. The PRE supplies a separate stronger uniform-in-lambda proof. |
| Proposed reservoir account | With nonnegative environment energy and conserved additive total energy, and reproduction of the microscopic energy moment, the necessary supply inequality is `E_R(0)>=E_total(t)-E_initial`. The positive initial energy must be subtracted. A conserved bounded interaction allows `E_R(0)+2||V||` on the left. These are extra hypotheses, not a derived realization. |

For the variance calculation, the extra electric term acts as the scalar
`2ell` only on each immediate output. It does not commute with the original
Hamiltonian throughout the physical sector. The author's calculation correctly
uses the full twelve-dimensional Hamiltonian square. In the independent
calculation the component of `H v` in W=1 contributes the leading
`c delta² epsilon^-6` term. Compressing H to P before computing its square
would omit it; the PRE explicitly checks this failure. The old two-eigenvalue
spectral formula is valid at lambda=0 and is not silently reused as the new
lambda>0 spectrum.

The finite-time relation needs the common coherent leaf preparation. The
no-event evolution stays in `span(g,Fg/sqrt(3))`, each nonzero first mark has
a time-independent normalized output, and all N=3 marks vanish. The N=3 sector
then evolves unitarily, preserving its H energy. These facts justify the exact
one-jump integral. A general one-record density does not obey the same injected
energy coefficient: the PRE's leaf-dephased mutation gives
`delta/epsilon²+2ell`, so this restriction matters. Neither note claims an
input-independent identity.

## Checking the author's asymptotic proof on its own terms

In the orthonormal basis `g,u=Fg/sqrt(3)`, both constructions give

```
G = -i [[3delta/epsilon², -sqrt(3)delta/epsilon³],
        [-sqrt(3)delta/epsilon³, delta/epsilon⁴+ell]]
    -diag(0,2kappa/epsilon²).
```

The independent matrices give the scaled characteristic polynomial

```
epsilon⁴ z² + [i delta a + 2kappa epsilon² + i ell epsilon⁴] z
              + i6kappa delta - 3delta ell epsilon².
```

At epsilon=0 the slow root is `-6kappa` and the z derivative is `i delta`,
which is nonzero. Coefficient comparison, independently performed from this
matrix, gives

```
z_s = -6kappa + [18kappa-i(12kappa²/delta+3ell)]epsilon²
                 +O(epsilon⁴).
```

The released previous note defines its orthonormal columns as
`l=(1,sqrt(3)epsilon)/sqrt(a)` and
`r=(sqrt(3)epsilon,-1)/sqrt(a)`. With that precise sign convention, the
rotated generator has

```
A = -6kappa/a-i3ell epsilon²/a,
B = 2sqrt(3)kappa/(epsilon a)+i sqrt(3)ell epsilon/a,
D = -2kappa/(epsilon²a)-i delta a/epsilon⁴-i ell/a.
```

These match the author bridge. In particular
`z_s-A=-i12kappa² epsilon²/delta+O(epsilon⁴)` and B is of order
`epsilon^-1` with nonzero leading coefficient. The slow eigenvector's high
component `(z_s-A)/B` is therefore of order `epsilon³`. The other eigenvalue
is `tr(G)-z_s` and its separation from A is of order `epsilon^-4` with
nonzero leading coefficient `-i delta`; the fast eigenvector's low component
is also of order `epsilon³`. The inverse eigenvector matrix remains bounded
for small epsilon. Decomposing the common initial column `(1,0)` in this basis
therefore gives a fast coefficient of order `epsilon³`.

Since `G+G†=-diag(0,4kappa/epsilon²)`, every eigenvalue has nonpositive real
part. The scalar exponential factors cannot magnify those coefficients. On
each fixed `[0,T]`, the high component is `O_T(epsilon³)` and the low
component is `exp(-6kappa t)+O_T(epsilon²)`. The leaf component is
`O_T(epsilon)`. Consequently the original positive square contributes
`Omega a O_T(epsilon⁶)=O_T(epsilon²)` to the no-event energy; the electric
term contributes `ell O_T(epsilon²)` as well. This supplies both
`p3=1-exp(-12kappa t)+O_T(epsilon²)` and `E_no=O_T(epsilon²)` for fixed
lambda, exactly as used in the author note.

This reasoning checks the author's eigenvector proof; it does not replace it
with the PRE proof. The latter directly controls
`beta-sqrt(3)epsilon alpha` by Duhamel integration and gives the error bounds
uniformly for `ell in [0,K]`. Its conclusion includes choices `lambda=lambda_S`.
That stronger uniform statement is expressly an independent PRE derivation,
not a proof claimed in the frozen author bridge. Both arguments hold at fixed
positive K, delta and kappa and fixed finite time intervals; they supply no
uniformity in graph size, varying delta/kappa, or times growing with S.

## Scope and physical interpretation

The electric family changes the finite target postbirth phase: the target
Hamiltonian on this star is zero in N=1 and `2K lambda` in N=3. It leaves the
leading microscopic energy requirement intact for the common preparation and
unchanged original marks. The initial microscopic mean tends to zero, whereas
at any fixed positive time the formed probability has a positive limit and the
mean grows as `S(S+1)`. This is not caused by input flux growing with S: all
physical fields remain at most one and the physical dimension stays sixteen.
The singular observable and couplings account for the moment issue.

A density limit or a vanishing high-energy spectral probability does not imply
convergence of these microscopic energy moments. The initial state has a
W=1 component, so invoking a theorem restricted to P-supported microscopic
initial data would not suffice. Here both the independent proof and author
bridge use the complete microscopic dynamics directly. The prior exact note's
zero-energy low-cluster statement applies to lambda=0; neither comparison
extends it to the changed lambda>0 Hamiltonian.

The necessary environmental inequality, under its explicit finite-energy,
positivity and conservation assumptions, is

```
E_R(0) >= [3delta/(2epsilon²)+2ell]p3(t)-3ell epsilon²/a.
```

With a conserved total `H_system+H_R+V`, the exact statement retains
`<V>_0-<V>_t`; a bounded self-adjoint V gives the stated `2||V||` allowance.
An environment supply or interaction norm growing with S is not excluded.
Reproduction of the microscopic energy expectation is essential; trace-distance
reproduction alone does not entail this inequality for an approximating state.
Nothing here identifies the increase as heat, constructs an autonomous
reservoir, supplies a reservoir spectrum, selects lambda, or establishes a
universal no-go. There is only one possible formation on this tree. General
cube, repeated formation, other initial preparations, infinite volume and
empirical interpretation remain outside this comparison.

## Executed evidence, failures and final disposition

[COMPARISON_RESULTS.json](COMPARISON_RESULTS.json) records 144 exact symbolic
comparisons, including full local-sector basis mapping, all physical output
amplitudes, all nine marked means and variances, gain and loss separately, the
finite-time source identity, and the no-event polynomial, rotation and
eigenvector order coefficients. The count is a record of coverage, not a
substitute for the analytic arguments. The independent PRE exact result
reproduced byte for byte. The successful author result JSON and stdout also
reproduced byte for byte. Full outputs, exit codes and source hashes are in
[COMPARISON_EXECUTION_RECEIPT.json](COMPARISON_EXECUTION_RECEIPT.json).

The author reports two pre-seal assertion failures and preserves a complete
snapshot of the second. That retained failed script again exits with code 1
at the documented assertion. The unsimplified coefficient is

```
epsilon²[-3K delta lambda + delta(3K lambda+12kappa²/delta)-12kappa²].
```

It is algebraically zero but is not structurally the literal zero in the
retained expression. The final author source differs only by applying
`simplify` to this exact-zero check; no physical coefficient or tolerance is
changed. The complete one-line source diff is retained as
[author_structural_assertion_fix.diff](author_structural_assertion_fix.diff).
The first historical failure is reported, not claimed independently recovered
from an unavailable full snapshot. There are no unresolved execution failures
or scientific discrepancies in this comparison.

The current author runner and its imported exact-star builder were reproduced;
the old finite-time dependency's complete analytic proof was checked directly.
Its historical numerical runner was not rerun in this phase. Independent
finite-time full-GKLS calculations and the uniform limit proof already reside
in the immutable PRE. These distinctions preserve the actual evidence scope.

Only new comparison files in this owned directory were written. No PRE file,
external author file, git state or publication surface was changed. The final
seal binds this comparison, the source snapshots, all comparison controls and
receipts, and the unchanged PRE packet. Work stops at this source comparison.
