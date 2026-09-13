# Next campaign: the native charged gauge phase

Start after the Hall-free quartet construction. Target the remaining charged
quantum gauge realization rather than derive another formal beta coefficient
while its photon phase remains supplied. The initial analytic ideas below
were formulated before reading the detailed Tong et al. truncation proof;
its introduction/abstract was subsequently found as close established work.
None of these draft estimates is a completed phase theorem.

## Candidate exact Hamiltonian and state domain

Use the four-orbital hopping coefficients from block11, or any finite-range
number-preserving CAR coefficients with common unit charge. Put integer flux
E_l on each oriented link, U_l|n>=|n+1>. Use
H=H_onsite+sum_l(c_x^dag T_l U_l c_y+h.c.)
  +(g^2/2)sum_l E_l^2-(1/(2g^2))sum_p(W_p+W_p^dag),
with conventional overall spacing and time units still supplied.
Gauss G_x=div E_x-(N_x-2). The same onsite T=tau_x K acts on matter and
complex conjugation acts on the real link-flux basis. E and U are unchanged
as operators by that conjugation, while the physical angle is time-reversed.
Check the hopping coefficient condition tau_x T_l^* tau_x=T_l explicitly.
The whole quantum Hamiltonian can therefore preserve T without adding an axiom.

For integer cutoff S>=1, take U_S=P_S U P_S, E_S=P_S E P_S.
[E_S,U_S]=U_S exactly, but U_S is not unitary at the endpoints. Gauss,
number, T and magnetic plaquette covariance survive. The physical sector is
nonempty on every periodic finite cubic graph: occupy two orbitals per cell
and put E=0 on every link. This supplies a finite physical Hilbert space and
a Gibbs state, not a Weyl-plus-photon ground-state theorem. In a gauge-invariant
state, an undressed open-link expectation vanishes; replacing U by its
expectation is therefore not a legitimate test of the charged phase.

No finite-dimensional unitary U can obey [E,U]=U: U^dag E U=E+I would violate
trace invariance. This exact algebraic limitation is avoided by the nonunitary
hard truncation; it does not forbid finite-dimensional emergent photons.

## Proposed local flux-growth bound

For one link l decompose the full Hamiltonian into a part commuting with E_l
and bounded shifts B_l+B_l^dag, [E_l,B_l]=B_l. Let J_l bound ||B_l||,
or safely the sum of norms of the raising terms. The remaining couplings,
including all matter and other gauge links, need not be product states.
Conjugation by exp(lambda E_l) changes only those shifts. Its anti-Hermitian
part has norm at most 2 J_l sinh(lambda), suggesting

||P_(E_l>=S) exp(-itH) P_(E_l<=M)||
 <= exp[-lambda(S-M)+2 J_l |t| sinh(lambda)].

The lower tail follows with -E_l; combine with a stated factor rather than
silently assuming the two tails are one. Prove the unbounded-operator step
by finite flux cutoff followed by a strong limit, or through an exponential
weight energy estimate on an appropriate core. The bound is independent of
the total spatial volume and of the electric E_l^2 norm.

The commutator and the same estimate hold for the truncated H_S. A Duhamel
comparison between full evolution and embedded compressed evolution only
sees matrix elements crossing flux boundaries. A safe bound is expected of
form C |t| sum_l J_l exp[-lambda(S-M)+2 J_l |t|sinh(lambda)] on initial
states with every link flux bounded by M. Fix all factors by proof.
This gives cutoff growth linear in time and logarithmic in inverse precision
and volume, rather than the crude total-Hamiltonian Dyson scale volume*time.

For a bounded local even observable, the unbounded E^2 part is onsite. In
its interaction picture all propagation terms retain bounded norms and finite
spatial supports, hence a cutoff-independent Lieb-Robinson speed should apply.
Localize to a ball of radius R, use the finite-ball flux bound there, and add
the exponentially small spatial boundary error. The required cutoff can then
be independent of the total volume for fixed observation region, time and
precision. This is a local dynamical approximation theorem, not yet a
fixed-cutoff infrared photon theorem.

## Phase question that must remain separate

A finite-time approximation does not establish the ground state, the
thermodynamic gapless spectrum, a stable phase at one fixed S, or a common
renormalized matter/gauge cone. Existing current-main spin-half cubic-ice
sources provide exact RK component facts and finite static diagnostics, with
an imported adjacent-phase argument. Their charged defects are not already
the massless quartet. Pure compact-U(1) deconfinement theorems must be read for
whether their hypotheses allow this gapless fermion determinant; they cannot
be applied by the word gauge alone.

Live routes: fixed spin-half ice with gapless charged matter; large finite
integer links with controlled truncation and weak compact gauge phase;
noncompact Gaussian photon supplied as an effective comparison; rigorous
Villain dual monopole loop bounds with an explicit charged-determinant step;
and a microscopic symmetry/RG route protecting the aligned carrier. None is
closed by this seed or by absence of a ready proof.
