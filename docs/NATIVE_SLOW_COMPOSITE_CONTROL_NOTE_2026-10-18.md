# Native correction structure of the slow large feature

Claim type: bounded_theorem.

Primary runner: `scripts/native_slow_composite_control.py`


Status: bounded-support. Exact finite-order local coefficients and selection
rules for the supplied one-qubit directional Hamiltonian; no full native
resonance theorem or physical scalar identification.

The [slow-composite block](NATIVE_SLOW_BULK_COMPOSITE_NOTE_2026-10-18.md)
obtained a mode and original-readout coupling in an explicit coefficient
model. This block attacks its omitted native terms. It does not replace
those terms with an adjustable interaction. The Hamiltonian, anisotropy
Jx=Jy=lambda Jz, uniform longitudinal reference and readout remain supplied
premises. All computations are exposed development controls, not observations.

## 1. Exact grading and support

Let U multiply a finite spin configuration by (-1) to the number of down
spins on odd x+y sites. Equivalently on a finite compatible grid it is the
product of Z on that transverse checkerboard. UH(lambda)U=H(-lambda).
Canonical perturbation built from H0 spectral projectors/resolvents inherits
U K_n U=(-1)^n K_n.

In the compact four-wall even-plane-parity sector, a configuration has two
columns sharing one interval I of length ell. Its U sign is
(-1)^[ell(chi(r1)+chi(r2))]. The axial-distance-two family and the entire
ell=2 relative host have U=+. Direct odd-order terms within that active
graph therefore vanish. This statement alone would not exclude transitions
to U=- states elsewhere.

A stronger support statement does. Every order-n canonical monomial,
including folded terms, contains exactly n native transverse edge flips.
If a final configuration has a different unordered column pair and interval
I' of length ell', the configurations overlap in at most one column, so

    Hamming distance >=2ell+2ell'-2|I intersect I'| >=2ell.

Each V flips only two physical bits. Thus n>=ell is necessary to change the
column pair. For an axial-distance-two initial interval with ell>n, all
outputs retain its U=+ column pair, and hence **every odd-order E8 row
vanishes**. In particular the entire K3 row from ell>=4 is zero, including
transitions to fast and frozen channels. This is an exact selection rule,
not an assumption that the chosen graph is closed to all orders.

The full slow complement contains U=- odd-length opposite-color pairs.
Their K2 block is flat at -4, separated from the active arm bottom -6, but
fast U=- channels are not gapped. Neither can be erased from higher-order
analysis by the grading alone.

## 2. The surviving third-order boundary

At ell=3, a different-column output saturates the six-bit count. Layerwise
edge parity shows that the only possibilities translate one entire occupied
column by one transverse nearest-neighbor step, leaving the interval fixed.
A shorter target would require a removed layer's two distance-two endpoints
to be connected by one edge, which is impossible. A longer target exceeds
the bit budget. Same-column targets vanish by grading.

For each allowed physical column move there are six ordered paths. Two
have excess energy costs (4,4), four have (4,8) or (8,4), all with product
of V matrix elements -1. No intermediate lies in E8, so no folded term
survives. Their exact sum is

    -2/16-4/32=-1/4.

At zero center momentum the two physical column moves give relative hopping
-1/2. In the normalized scalar channels the native A3-to-adjacent E3 vertex
is -1/2, in units Jz lambda^3. Other outputs enter frozen odd-color ell=3
states. The third-order interaction is therefore a derived short-interval
boundary coupling, not an absent interaction and not a bulk decay term.

## 3. Exact fourth-order kernel

For initial and final slow states annihilated by K1, all canonical fourth-
order terms carrying K1 at an external end vanish. Put R=Q/(8-H0),
B_a(s)=<s|V R V|a>, A_a(s)=<s|V R^2 V|a>. The remaining exact kernel is

\[
(K_4)_{ba}=\sum_{s\in Q}\frac{B_b(s)B_a(s)}{8-E_s}
-\frac12\sum_{s\in P}\{A_b(s)B_a(s)+B_b(s)A_a(s)\}.
\]

All coefficients in the runner are rational; large disconnected contributions
are canceled exactly, not by floating-point subtraction. This formula is
restricted to the stated external states, not a general replacement for K4.

The vacuum-subtracted diagonal for every ell>=3 is

\[
(K_4)_{aa}-K_{4,vac}=\ell/8+29/192.
\]

This is not a line fitted through finite data. A diagonal four-edge word is
a repeated edge, two repeated edges, or a transverse square. Disconnected
pieces on nonadjacent z layers cancel the folded term exactly. The surviving
clusters occupy one layer or two adjacent layers; for ell>=3 they cannot
inspect both interval boundaries. The excess must therefore be affine in
ell. Independently summing the 24 square-loop orders gives -P_square/128;
the two columns change eight plaquette signs per interior layer, fixing
slope1/8. The exact ell=3 endpoint computation101/192 fixes the intercept.
Controls ell4,5,6,8 give125/192,149/192,173/192,221/192.

For ell>=5 the full long-row support at fourth order is exhausted as follows.
Changing columns needs at least ell operations. With the same columns, every
changed layer needs two transverse edges; thus there can be at most two
changed layers. A final common interval permits only one-end steps of one or
two layers, or a one-layer step at each end. The separated two-end processes
cancel between direct and folded terms. Root's exact kernels and an
independent single-wall geometry give

| Native x-oriented endpoint move | Direct + folded coefficient |
|---|---:|
| one layer | 19/64 |
| two layers | -13/256 |
| two separated ends | -1/8+1/8=0 |

One-layer moves use two operations on that layer; the other two form a detour
or return loop. Only neighboring-layer loops can remain connected through
H0. Two-layer moves use all four operations on those layers. Consequently
these coefficients belong to a bounded wall neighborhood and extend to all
long intervals, not just the tested ell5,6. Short intervals and nearby
periodic images require separate kernels. The y-oriented one-layer sign is
reversed and is removed by the scalar basis factor (-1)^ell; two-layer signs
are unchanged.

## 4. What this changes about the candidate

At zero longitudinal center momentum the two endpoints give K4 length hops
19/32 and -13/128. Excluding the linear tension, the symbol is

\[
29/192+(19/16)\cos k-(13/64)\cos2k.
\]

Its value at the leading K2 slow-arm band bottom k=0 is109/96; its
quadratic correction is-3/16.
The native long-arm expression is therefore

\[
E/J_z=8-6\lambda^2+\lambda^4(\ell/8+109/96)
 +(\lambda^2-3\lambda^4/16)k^2+\cdots.
\]

The real shift109 lambda^4/96 is of the same order as the previously
calculated conditional width; treating *all* omitted K4 effects as smaller
would be wrong. It is now derived rather than fitted. For an Airy-sized
feature, k^2 is of order lambda^(4/3), so the displayed kinetic correction
has energy order lambda^(16/3). The tension remains the derived lambda^4/8.

These facts do not yet promote the projected-model width to a native
lifetime. A bounded finite boundary correction of physical order lambda^4
would change the slow boundary scattering coefficient by order lambda^2,
and hence the Airy pole by order lambda^6, **if** the required outgoing
finite-source resolvents remain uniformly bounded. Third-order virtual
boundary transitions need that same check. The supplied fast block also
has native second-order corrections; its complete resolvent control remains
open. A finite-order symmetry or a real bulk energy shift is not proof of
an infinite-volume resonance.

## 5. A restricted norm bound, with its boundary

A volume-independent bound can also be proved for each fixed-order normal-
form coefficient. Decompose D_n=sum_X d_X into Hermitian local terms filtered
separately to commute with H0. The integer-wall filter only enlarges each
support by its longitudinal neighbors. On a proper local support the all-up
pattern is the unique finite zero-wall configuration. Thus subtracting the
local vacuum scalar gives b_X=Q_X b_X Q_X, where Q_X projects off the all-up
pattern and ||b_X||<=2||d_X||. Whole-column wrapping terms on a finite periodic
z ring are excluded from this local statement.

Since Q_X<=sum_(i in X) n_i and a0(D_n)=sup_i sum_(X containing i)||d_X||,

    |<psi|(D_n-Evac)|psi>| <=2 a0(D_n)<psi|Ndown|psi>.

For P_L projecting onto all compact E8 column pairs with ell<=L (not just
the active arm), this yields

    ||P_L(D_n-Evac)P_L|| <=4 L a0(D_n).

There is no matrix-entry norm or exponential support-size factor. Moreover
an order-n word flips at most2n spins and preserves E8 and plane parity, so
its output from P_L lies in P_(L+n). The same bound with L+n therefore bounds
||(D_n-Evac)P_L|| as well. It controls escape from the length cutoff within
the fixed-order E8 sector. It does not control the untransformed Hamiltonian's
leakage into other wall sectors.

For any fixed upper order m, the omitted finite sum of orders5 throughm has
norm at most4(L+m) sum_(n=5)^m lambda^n a0(D_n). At an Airy-size cutoff
L=O(lambda^(-2/3)) this is O_m(lambda^(13/3)), smaller than lambda^4.
No convergence of an infinite perturbation series is asserted. The actual
normal-form remainder, cutoff tails and corrected fast boundary resolvent
remain to be controlled. Even an error smaller than the linewidth does not
automatically resolve the original-readout spectral signal of order lambda^6.
Prepared-state selection, cosmological scale and source/detector identification
remain separate unresolved assumptions.

## Reproduction and status

Run the [source-bound runner](../scripts/native_slow_composite_control.py) with
`python scripts/native_slow_composite_control.py`. It replays exact
third/fourth-order path contractions and a separate single-wall calculation;
source identities and rational results are recorded. Focused independent
proof checks are stored in the campaign pack. No empirical data, new
interaction, formal audit verdict or retained-status promotion is introduced.

## Portable proof and execution closure

The complete mathematical sources below retain their actual assumptions and derivations. Historical execution/review labels are not fresh evidence. The primary uses an isolated temporary copy of the bound source package, streams child diagnostics, enforces one aggregate wall-clock cap and records required fresh JSON identities. Large frozen grids remain historical source-bound results, not replays. No stronger physical or asymptotic scope is inferred.

- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_FOURTH_DIAGONAL.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_FOURTH_KERNEL.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_PARITY.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_RESTRICTED_BOUND.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_SUPPORT.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/INDEPENDENT_SLOW_THIRD.md`
- `outputs/neutral_continuation_review_2026_10_18/pr9740/native/REVIEW_SLOW_NATIVE_CONTROL.md`
