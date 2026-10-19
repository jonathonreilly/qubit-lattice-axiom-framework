<!-- Original PR9777 source SHA256 18aab6bb012badf82235dad1f71bca40df2edc174695d5ce7d4df1b5b942f6c6. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Conditional actual spectral-window check near the K1 binding threshold

Read `/tmp/neutral_native_threshold_window_root.md` and the existing `native/MICROSCOPIC_GROUND_WINDOW_PROOF.md`. The residual-to-positive-window argument is correct. The draft is not yet an unconditional microscopic theorem: the uniform coefficient/action bound and uniform source/orbit construction identified below are genuine prerequisites, not consequences of a small finite-volume Ritz residual.

## Exact spectral inequality

Let H be the actual self-adjoint finite-box Hamiltonian, |g> an exact normalized ground state, and Xi a normalized trial with

||(H-Eg-Jz[8+lambda E_b])Xi||<=C Jz lambda^2.

Let P_w be the spectral projection onto the interval centered at Eg+Jz[8+lambda E_b], of halfwidth w=Jz lambda delta/4. The spectral theorem gives

||(1-P_w)Xi||<=4C lambda/delta.

For the connected source q=(C_Q-<C_Q>)|g>, write a=|<Xi,q>|. Then

||P_w q||>=a-||(1-P_w)Xi||||q||.

No isolated actual band is needed. This inequality follows by splitting <Xi,q> into the projected and complementary pieces and applying Cauchy-Schwarz. Squaring its positive lower bound gives an actual nonnegative spectral-window weight.

If ||q||<=Cq lambda and a=lambda sqrt(W0 delta) log(1/delta)[1+o(1)], the subtraction is O(lambda^2/delta). Its relative size is

O(lambda/[delta^(3/2)log(1/delta)]).

Thus delta=lambda^alpha with 0<alpha<2/3 is sufficient. Under exactly these uniform estimates, alpha=2/3 also gives a vanishing 1/log error, although the strict inequality is a safer stated regime and no endpoint claim is necessary. The conclusion is a lower bound

||P_w q||^2 >= W0 lambda^2 delta log^2(1/delta)[1-o(1)],

not equality: additional spectral weight may lie in the same window. Jz cancels from the residual/window ratio. The energy center must use the actual Eg; an error O(Jz lambda^29) in Eg is negligible here.

An O(lambda^2) higher-source error is smaller than the proposed overlap for this regime, since lambda/[sqrt(delta)log(1/delta)]->0. But that error must be volume-uniform in source-vector norm, not merely an extensive operator-norm estimate.

## Finite momentum and box scale

For Q=(0,Qy,0), choose Qy=2pi k/L on the even periodic cube. The original midpoint readout has C_Q dagger=C_-Q. The previous phase-weight argument is not intrinsically restricted to longitudinal or small momenta: all local norm, plane-invariance, charge-filter, and absolute Lieb-Robinson estimates depend only on modulus-one weights. It therefore extends to these allowed transverse momenta.

Choosing the nearest allowed Qy changes b=cos(Qy/2) by O(1/L). In the stated threshold law d log(delta)/db is of order log^2(1/delta), so L~lambda^-4 produces only a relative O(lambda^4 log^2(1/lambda)) change in delta. A uniform version of that derivative estimate, or direct bracketing of the mesh-selected binding energy, should be included rather than asserting an exactly prescribed delta on every finite torus.

The transverse extent delta^-1/2 fits well within L in this regime. Exponential finite-volume wrap estimates additionally need their usual normalization/prefactor control; polynomial or logarithmic threshold factors are harmless against exp[-c L sqrt(delta)]. The vertical ray remains uniformly evanescent because its energy is below its own continuum by a fixed amount near b_c.

## Ground-orbit transfer is possible, but needs an excitation map

The existing ground theorem supplies a near-identity map from every actual ground vector into the large P0 column-pattern manifold. It does not by itself prove the stated overlap with a particular trial built above all-up. For a general superposition of ground patterns, construct an excitation map T_Q on P0: take the bound-state trial above one reference, transport it by the exact plane symmetries to each column pattern, and retain the physical Fourier phases. One needs

T_Q dagger T_Q=I_P0+small error,
T_Q dagger q_operator P0=a0 I_P0+small error,
||residual_operator T_Q|| on P0 <=C Jz lambda^2.

Then T_Q applied to the mapped actual ground vector gives the desired Xi uniformly, without choosing a polarized reference.

These identities can be justified by the same disjoint-support mechanism as the prior ground proof, but with the extended bound-state profile accounted for. Truncate the exponentially decaying vertical interval lengths and the transverse bound-state tail on scales well below L. Different column backgrounds cannot be connected by two such finite-excitation configurations unless a complete column pattern is changed; plane transitivity equates diagonal Gram and overlap entries. After summing the COM translations, use operator identities or orthogonality, not an estimate multiplied by the exponentially large number of ground patterns. Residual vectors generated by a fixed-order local coefficient require the same support/Gram check. The discarded tails must be bounded below the desired overlap and residual scales.

A Fourier source mean is not automatically zero in an arbitrary exact ground superposition. Center it explicitly. Under the above charge/excitation construction Xi is orthogonal to the ground manifold up to controlled errors, so centering does not remove the desired excited overlap. Mixed ground densities follow by a uniform vector-state bound and convexity, provided all vectors lie in the exact ground eigenspace with the same Eg.

## What remains to establish

1. The delta-uniform bound on vacuum-subtracted D_j acting on the normalized extended trial. Uniform vertical-length moments and local connected support are promising, but spatial delocalization and the fixed-COM sum must be handled by the actual quadratic-form/operator argument. I have not assumed this missing estimate.
2. The volume-uniform connected-source norm O(lambda), and the O(lambda^2) remainder acting on the ground-orbit space. Local Gram summability and normal-form charge selection can provide them; the earlier global bound ||C_Q||<=sqrt(V) alone cannot.
3. The excitation-map Gram/residual control just described, including finite wrapping and the exact-ground intertwiner. The existing ground projector theorem provides the starting point, not all these excited-state estimates automatically.

If these inputs are supplied, the positive-window lower bound follows by the elementary inequality above and avoids outgoing-pole transfer entirely. It still proves neither an isolated microscopic line nor a unique particle, group velocity, Lorentz scalar, gravitational coupling, or cosmological state selection. It establishes finite-box positive spectral weight of the specified original observable in a shrinking but controlled energy window.

## Follow-up: truncated ground-orbit excitation map

The proposed orbit construction resolves the ground-superposition issue, subject to the explicit truncation and the still-separate single-reference D_j bound.

On the even periodic cube, X/Y transverse-plane flips act transitively on P0 patterns s_xy=a_x b_y. A product with trivial action on these column signs is diagonal (up to its fixed Pauli phase). In the X/Y subgroup the only nontrivial pattern redundancy is simultaneous reversal of every row and every column; its physical operator is proportional to global Z. If longitudinal Z-plane generators are included, they are also diagonal stabilizers. The layer-even N=4 state has the same + Z-plane parities as all-up and therefore the same global-Z character. Fixed Pauli phases in a stabilizer are identical on both states. Thus every stabilizer of the reference pattern acts on chi by the same scalar as on the reference vector, and T(U_g Omega)=U_g chi is well-defined independently of the chosen representative. It is important to use this equality of characters, rather than say all stabilizers literally act as identity without accounting for phases.

Truncate each interval length below Lz/4 and normalize chi. The truncation is invariant under the diagonal stabilizers. A configuration in chi above one background differs from it on at most two short intervals. Two such configurations above different column backgrounds cannot coincide: their symmetric difference on any particular column covers less than Lz/2, whereas a nontrivial background change reverses at least one entire column of length Lz. The same argument holds after fixed-order local coefficient actions on both states: those actions add only a fixed number of spin changes, so Lz/2+O(j)<Lz for large enough boxes. Sums over COM translations do not change this support argument. Transverse separation truncation helps the periodic approximation but is not needed for this particular column-length disjointness.

Consequently distinct background images have disjoint computational-basis support, both for chi and for each fixed-order residual vector. With normalized chi,

T dagger T=I on P0.

The leading local source images obey the same disjointness. Since C_Q and the normal-form coefficients commute with the plane actions, all diagonal source overlaps equal the all-up overlap a. Hence

T dagger q_leading P0=a I on P0

exactly for the truncated construction (with its truncated a). The residual vectors have equal norms by symmetry and are orthogonal between backgrounds. Therefore a single-reference residual bound implies the identical operator norm bound on the entire P0 space; no factor proportional to the exponentially large number of backgrounds appears.

This does not supply the remaining delta-uniform bound on D_j chi: it only shows how that separately proved bound transfers to every ground superposition. The lost tail and truncation-induced residual must also be estimated using the stated vertical evanescence and transverse binding decay.

The reference effective ground energy is scalar on P0 because fixed-support N-preserving terms cannot flip whole columns and plane transitivity equates their diagonal values. The exact-ground intertwiner can then be combined with T without assuming translation invariance of the actual ground vector. If one uses the conservative gap lower bound of order lambda^4, global remainder O(lambda^29) gives ground-subspace proximity O(lambda^25). Multiplying by ||C_Q||<=sqrt(V)=O(lambda^-6) yields source-vector error O(lambda^19), negligible on the present overlap scale. The stronger constant-gap estimate in the original growing-box proof only improves this. Both must use the actual ground eigenvalue for centering.

Thus the stabilizer and disjointness parts of the proposed map are sound and close that particular prerequisite. Uniform coefficient action, uniform higher-source norm, and quantitative tail bounds remain distinct inputs.

## Follow-up: uniform coefficient, source, and truncation estimates

The latest appended construction in `/tmp/neutral_native_threshold_window_root.md` supplies a valid route to the remaining estimates, with the precise local-term conventions below. No norm bound uniform over *all* arbitrarily long intervals is asserted.

### Fixed-order coefficient action

Use the individually N-preserving local decomposition obtained by the commuting-N filter, and include incident vertical neighbors in each term's support. This enlargement matters: a flip on an up spin immediately beside a down interval can move a wall even though the bare transverse-flip support contains no down spin. After the enlargement, a support genuinely missing the down set sees a wall-free vacuum neighborhood. It cannot make a nonempty finite zero-wall excitation, and it cannot exchange wall energy with a disjoint region; after subtracting its vacuum scalar it annihilates that configuration.

At fixed order j, the enlarged supports have uniformly bounded size/range and coefficient sums. A compact N=4 basis state has two columns occupied on one common interval of length ell. At most C_j(ell+1) translated supports meet that down set, regardless of the distance between the two columns. Each local term has only a fixed number of possible output spin patterns. Thus the absolute matrix row and column sums of the vacuum-subtracted coefficient are bounded by C_j(ell+1).

Every output still lies in compact layer-even N=4 when the input interval and all local supports are shorter than the torus periods. A nonzero matrix element changes the number of down spins by at most a fixed number, hence |ell_out-ell_in|<=R_j. This also covers a short interval whose column labels change. Define W=ell+1. For T=(D_j-E_j,vac)W^-1, neighboring weights are comparable by a constant depending only on j. Its row sums and column sums are therefore bounded uniformly. The ordinary Schur test yields

||(D_j-E_j,vac)psi||<=C_j||W psi||.

This is a graph-matrix estimate before taking a COM fiber, so the normalized translation sum cannot invalidate it. Equivalently one can retain the same absolute row sums after Fourier phases. There is no factor depending on transverse separation or box volume.

Near the critical point, the host portion of chi has ell=1, whereas each interval-ray tail decays with ratio rho=|sigma(E)|/2<0.6 uniformly. Root amplitudes are at most one for the normalized full state. Consequently ||(ell+1)^r chi|| is bounded uniformly for every fixed r, even as the host's transverse extent diverges. The finite sum j=2,...,40 is therefore O(lambda^2) on chi with a delta-independent constant. This closes the coefficient-action estimate within the specified finite-order local decomposition.

### Normalized original-source remainder

For each fixed local Taylor coefficient of the dressed readout, subtract its reference scalar and write its translated action on all-up as a finite set of nonempty spin-excitation patterns. Two translates with disjoint supports have zero Gram overlap in the product reference. Only a fixed number of relative translations contribute. The 1/sqrt(V)-normalized Fourier sum consequently has vector norm at most C_j, uniformly in V and real allowed Q. At nonzero Q the translation-independent scalar contribution sums to zero; explicit centering covers the general formulation.

Summing source orders j>=2 gives an O(lambda^2) remainder, while the first nonzero term has norm O(lambda). The previously checked ground-orbit disjointness transfers these vector estimates uniformly to P0, including coherent superpositions, without a ground-dimension factor. Fixed-order source terms need not preserve N for this Gram argument; their finite support and bounded spin changes suffice.

The exact order-40 source remainder has the conservative global norm sqrt(V)lambda^41=O(lambda^35). The exact-ground-subspace correction contributes O(lambda^19) under the conservative lambda^25 ground-vector estimate. Both are smaller than lambda^2. Thus the claimed actual connected-source norm O(lambda) and remainder O(lambda^2) follow, assuming the previously established exact local Taylor-remainder estimate.

### Tail and finite-box control

Vertical ray tails are uniformly exponential, so their weighted length moments beyond Lz/4 are exponentially small. For the transverse host below its quadratic band edge by delta, the fixed-source lattice Green function admits decay exp[-c sqrt(delta)|r|] with at worst polynomial delta-dependent prefactors. One way to justify the rate, rather than invoke a generic gap-only Combes-Thomas estimate, is to shift the Fourier contour by an imaginary vector of size c sqrt(delta): the change in the real band minimum is O(|shift|^2), leaving a fixed fraction of the gap. The inverse denominator is then bounded polynomially in delta. Cavity subtraction involves only finitely many source sites and logarithmic/polynomial coefficients near this threshold, so preserves such a bound.

Accordingly truncation at relative distance L/4 gives a norm/weighted-residual error bounded by polynomial factors in L and delta^-1 times exp[-c L sqrt(delta)], in addition to the vertical exp[-c L] tail. For L~lambda^-4 and delta~lambda^alpha, alpha<2/3, these are smaller than every power of lambda. The same estimates control normalization, periodic image sums, and local finite/infinite matrix mismatch. Applying a fixed-order D_j only adds fixed polynomial or interval-length factors, which cannot overcome the exponential. Truncation of an exact K1 eigenvector also gives a negligible K1 residual by bounded finite-range hopping.

These arguments complete the stated uniform estimates at fixed order; they do not supply constants uniform in j->infinity, or a fixed-lambda thermodynamic ground theorem. Combined with the orbit-map and spectral-window inequality above, they support the proposed positive microscopic finite-box spectral-window lower bound, using the earlier local normal-form and ground-gap theorems as inputs. The conclusion remains a lower bound on complete spectral weight, not a microscopic isolated pole or a lifetime claim.
