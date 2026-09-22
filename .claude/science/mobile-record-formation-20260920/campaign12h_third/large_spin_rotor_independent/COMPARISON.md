# Large-spin record motion: bounded post-seal source comparison

Completed 2026-09-22. This is scientific source scrutiny, not publication,
retention, or formal audit status. No author source was edited.

**Disposition:** no substantive correction identified in the frozen packet.
The generated electric and magnetic coefficients, the finite-spin corrections,
and the stated conditional, uniform local rotor limit agree with the sealed
independent reconstruction. The author's more general allowance for a
fourth-order effective-block basis change is valid; it does not conflict with
the equality proved for my particular edgewise circuit. The qualifications on
state moments, preparation, time, growing resources, and vanishing birth rates
are indispensable.

## Read boundary and exact sources

The blind reconstruction is `REPORT.md`, SHA-256
`072e1b6c833d023bec988126ca79379848718455122f7462db20db069a790732`.
Its `PRE_COMPARISON_SEAL.json`, SHA-256
`f8f457305153006eccda68740a518cfed0c11d3c28d1c77ad3ce6df71970e3c5`,
was fixed before opening any new author large-spin argument, checker, result,
or seal contents. All 27 PRE bindings remain unchanged and authenticate.

After explicit comparison authorization I authenticated and read the complete
12-artifact packet named by `LARGE_SPIN_RECORD_AUTHOR_SEAL.json`, SHA-256
`40797e4620ebb864744753ae5429a1727c7b407fc712bda4360e75ea295a1f3b`.
The substantive sources are:

| Source | SHA-256 |
|---|---|
| `ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION.md` | `52f5ce8bd8f1b39049ebbb0407e6881ed8e11de80bc2c29db9e0e56c5cdd3fc2` |
| `large_spin_record_electric_ring_check.py` | `ed23eb7e64c1847d78501dcb30263ea8d447eafc3a3835abb32e4a7f04fdf090` |
| `large_spin_live_birth_and_weight_check.py` | `a55e302832c91ae8410e79ef0fa621fbfd24d43ad376f89d078d0adc57585fec` |
| `LARGE_SPIN_RECORD_ELECTRIC_RING_RESULTS.json` | `71b0679661d84156f8f637155ca15452b6ba371f7127472b9130256359e7efe6` |
| `LARGE_SPIN_LIVE_BIRTH_AND_WEIGHT_RESULTS.json` | `12e30c1a18238e999c1a124da5a756085f0ec37c03c30a8dbef283a6211425a8` |

Both complete scripts, both complete result files, both stdout streams, the
empty stderr streams, both run receipts, and the complete context manifest
were inspected. Four context dependency bindings were also authenticated.
The same previously checked finite-circuit/locality argument is reused at
source identity `e03793ab0cc06bcc0d536db5b846addf3a999733c6dc25cc4d08ae457263e16e`;
its independent final seal remains
`cc213db7ba3b00cce3ae52d8206878219257bda27b831bfdad93129a9dbcafcf`.
The author's historically pending-review wording accurately describes its
freeze boundary; this comparison does not confer retained status.

No other new author packet, campaign checkpoint, registry, weak-field, ramp,
energy, or transport work was opened. New executable evidence here is
`comparison_check.py`, its result, complete stdout/stderr, and receipt. It
imports only my frozen `finite_spin_check.py`, never an author runner.

## Coefficients, geometry, and rate conventions

With $C=S(S+1)$, integer $S\ge1$, and stored-edge sublattice sign
$\sigma_e$, the squared initial hop amplitude is
$F_e=1-(E_e^2-\sigma_e E_e)/C$. Summing the linear term gives
$\sum_e\sigma_e E_e=\sum_{x\in A}\operatorname{div}E_x=0$ on ice.
Thus the dimensionless second-order block is
$-dV+\sum_eE_e^2/C$, rather than the scalar spin-half block.

At fourth order the two nonreturning excursions must use disjoint endpoints.
Their four orderings contribute $-2F_eF_f$ for each unordered disjoint pair;
the normalization term is $(\sum_eF_e)^2$. The residual diagonal is exactly
$\sum_eF_e^2+2\sum_{e\sim f}F_eF_f$. Four bosonic exchange paths around
each square have denominators $1,2,1$, producing
$-2(W_{p,S}+W_{p,S}^\dagger)$. These are the independently derived terms
in the author's Eq. (9), including its folded normalization. The required
even periods at least six exclude the short parallel-edge and winding
ambiguities. At unit weights the diagonal constant is $dV(4d-1)$.
Its exact finite-spin expansion is the author's Eq. (11), including the
quadratic correction $-J(4d-1)\sum E^2/C$ in physical units.

The two penalties coincide on the closed initial-number sector. In the full
physical live sector the field-star term equals
$N_{A,-}+N_{B,+}$; this is an integer-valued onsite matter penalty, not an
electric link energy added by hand. This distinction survives arbitrary $S$
and is used correctly in the normal form.

The exact per-edge formation loss for the two resolved channels is
$2\beta P_{\rm vac}(1-E^2/C)$. Orthogonality of the two charged matter
targets kills $V_+^\dagger V_-$, so one coherent sum has the same loss but
a different birth CP map. Norm bounds are uniform for integer spins. The
smallest available loss at an electric endpoint is $2\beta/(S+1)$:
there is no uniform positive clock bound in this limit. Neither the note nor
the local theorem uses one. Taking both coherent signs as separately
normalized channels without changing their coefficients would double the
loss; that is not the instrument stated here.

The scaling agrees exactly after identifying the author's $K$ with my $g$:
$\epsilon^2C=J/(2K)$, $\Delta=2K^2C^2/J$,
$t^2/\Delta=KC$, and $\beta=\beta_0\epsilon^{2d}$.
Both $K,J$ are fixed positive numbers. Formation is enabled at every finite
spin when $\beta_0>0$; the allowed $\beta_0=0$ is the closed control.

## The fourth-order circuit-basis issue

Here “block gauge” means the analytic choice of orthonormal coordinates in
the effective matter-code block, not a change of the physical Gauss law.
For a code rotation $V(\epsilon)=\exp(\epsilon^2G_2+\cdots)$, the
fourth-order coefficient changes by $[G_2,H_2]$. Since $H_2$ is
nonconstant at finite spin, this term cannot generally be discarded.

My PRE proof selected individual edge generators. Two distinct first-order
edge generators cannot return a checkerboard code state in two hops:
$PS_{1,e}S_{1,f}P=0$ for $e\ne f$. The order-two generators have
zero diagonal block. Hence that particular circuit agrees with the canonical
orthonormal identification through the order relevant for $H_4$. Its exact
square implementations at spins one and two corroborate that argument.
This is a property of the specified circuit, not a universal prohibition of
other low-block coordinates.

The author instead retains the actual finite-circuit coefficient
$D_{4,S}$, with a fixed structural decomposition and coloring across $S$.
The coefficient is a finite sum of fixed-length words in bounded $U_S$,
$U_S^\dagger$ and matter matrices, with spin-independent scalar
coefficients. Replacement by unit rotor shifts is therefore well-defined.
Only *after* this replacement is $H_{2,\infty}=-dV I$ on the ice code.
Every analytic block change then commutes with $H_{2,\infty}$, so
$D_{4,\infty}=dV(4d-1)I-2\sum_p(W_p+W_p^\dagger)$.
The weighted word estimate controls the remaining finite-spin difference.
This is a valid route to the limit even without asserting exact equality
between $D_{4,S}$ and the canonical formula at each finite $S$.

As a separate post-seal control, set $G_2=W_S-W_S^\dagger$ on the square
code. Then
\[
 [G_2,H_2]_{m+1,m}
 =-\frac{4(2m+1)}{C}\left(1-\frac{m(m+1)}C\right)^2.
\]
The $0\to1$ entry is $-4/C$, so the finite-spin correction is real and
nonzero. Multiplication on the right by $(1+E^2)^{-1}$ gives norm at most
$12/C$, while the commutator is exactly zero for the unit-link scalar
second-order block. Exact controls at $S=1,2,3,5$ verify these statements.
They illustrate the author's allowance; they do not assert that its actual
circuit has a nonzero change. An $S$-dependent decomposition into an
unbounded number of electric-level projectors would require new estimates;
the fixed finite-word construction avoids that issue.

## Uniform local comparison and unbounded-field details

The normal-form inverse uses integer matter grades and has a norm bound
independent of the link dimension. Fixed-order circuit depth, range, and
Taylor bounds therefore remain uniform in $S,V$. The large $\Delta N$
is removed in an onsite interaction picture. Using order $n=2d+6$, the
Hamiltonian remainder has strength $O(\Delta\epsilon^{n+1})$.
The transformed birth satisfies $\|YjY^\dagger P\|=O(\epsilon)$.
For a code-supported density the *full* dissipator, including its loss
anticommutator, is $O(\epsilon)$ in trace norm. No small jump probability
is substituted for the no-event backaction. The polynomial light-cone volume
has scale $h^d=O(\epsilon^{-2d})$, so the supplied birth schedule and this
source bound give a vanishing $O(\epsilon)$ local error. A global no-birth
conditioning is neither needed nor used.

Inside the code the second order is the exact onsite $K\sum E^2$; the
fourth order has bounded local strength $O(J)$ and the higher terms have
strength $O(J\epsilon^2)$. Thus this *second* comparison has velocity
of order $J$, not the microscopic $h=KC$. Confusing these two velocities
would lose the claimed error; the source keeps them separate.

The author's zero extension of $U_S$ agrees with the spin representation
on its invariant interval. The pointwise bound
$\|(U_S-U)(1+E^2)^{-1}\|\le2/C$ includes both cutoff endpoints and
the exterior. Products can be telescoped: every preceding or following
bounded shift changes the local weight by only a fixed factor. Consequently
local fourth-moment control suffices for a trace-norm source of order $C^{-1}$
even for entangled densities. Uniform operator-norm convergence is false
and is not assumed.

For $w_e=(1+E_e^2)^2$, the neighboring ratio is at most nine. The weighted
commutator constant six in Eq. (19) is conservative; the smaller constant
used in my PRE is not a discrepancy. The stated bound
$\langle w_e\rangle_t\le B\exp[24J(d-1)t]$ follows by counting the
two circulations of the $2(d-1)$ incident plaquettes. The truncated weight
$\min(w_e,L)$ has the same ratio property. Its bounded commutator gives
the estimate first on bounded weights and then by monotone convergence,
so finite initial fourth moments suffice.

In each finite spatial volume the electric Hamiltonian is self-adjoint on
its natural domain and the magnetic part is a bounded perturbation. Removing
the onsite evolution gives bounded, strongly continuous local interactions.
Vector Dyson integrals and commutator iterations establish the spatial
bound without assuming operator-norm continuity of those conjugated
interactions. My PRE supplied the equivalent route of truncating the rotor
at a second cutoff, proving dimension-independent finite-matrix bounds, and
passing to the strong limit. The author's direct strong-integral formulation
is compatible with that proof and introduces no finite-dimension factor.

Duhamel with the target rotor state on the source side uses the small
weighted source near the cone and the bounded operator norm with exponential
locality outside it. A radius of order $JT+\log C$ yields
$O(\epsilon^2+C^{-1}(1+\log C)^d)$. Adding the microscopic and
observable-dressing errors gives Eq. (15), uniformly over the specified
finite tori at fixed support and fixed time. It compares against the same
embedded, possibly $S$-dependent initial density. An initial limiting
thermodynamic state or convergence for unbounded observables does not follow
automatically.

## Executable coverage, attribution, and limits

All integer-spin second- and fourth-order square matrices in the author
result agree entry by entry with the independently sealed matrices for
*both* penalties. The full live dimensions $19,39,59$ and the closed
initial-number dimensions $13,25,37$ refer to different spaces, correctly
distinguished in the source. The extra spin-half check uses a link amplitude
$2/\sqrt3$, so its second and fourth coefficients scale by $4/3$ and
$16/9$. That normalization also checks exactly.

The post-seal checker independently assembles the spin-16 live square,
restricts its Hamiltonian to the 193-dimensional initial-number sector,
and recomputes the six shifted energies. The maximum difference from the
author values is $1.141753358524511\times10^{-11}$, the eigenpair residual
is $2.192292282386644\times10^{-11}$, and the ground code weight agrees
at the displayed precision. The other three large-spin diagonalizations
were not repeated. Their source bindings, full reported data, stdout,
receipts, dimensions, scaling, removed scalar, energy-error arithmetic,
and error normalization were checked. These checks are not exact spectral
enclosures or many-volume convergence evidence. The 7,440 scalar screen is
properly described as a control of the separate analytic inequalities.

The existing nonunitary-link electric mechanism is correctly credited to
Zohar, Cirac and Reznik, [arXiv:1303.5040v3, Section VII.A](https://arxiv.org/html/1303.5040v3#S7.SS1).
I read Eqs. (96)–(101) and the associated discussion, checking attribution
and the different auxiliary-matter setup. No coefficient or local-limit
theorem is imported from that paper. The primary HTML and read receipt are
preserved in `comparison_literature/`.

One optional extraction helper failed because `bs4` was unavailable. Its
exact code and complete returned tool output are preserved under
`failed_attempts/comparison_literature_bs4/`; a standard-library parser then
extracted the already-read section. No scientific assertion failed, no
threshold was changed, and no author source was modified. The independent
comparison checker passed on its first execution, with empty stderr.

The confirmed conclusion remains conditional on the supplied qutrit/link
model, finite local preparation, fixed positive $K,J$, bounded initial
fourth moments, fixed time/support, and the specified joint resource scaling.
It does not establish unrestricted initial-spin-band convergence, fixed
positive birth rate in the limit, positive limiting production density,
bare-quench dynamics, long-time uniformity, a Coulomb phase, continuum
photons, native one-qubit realization, or inexpensive compilation of the
growing link memory. The saturated-flux countercontrol remains in the
unchanged PRE packet. There is no unresolved mathematical finding within
the reviewed claim and no request for a source correction.
