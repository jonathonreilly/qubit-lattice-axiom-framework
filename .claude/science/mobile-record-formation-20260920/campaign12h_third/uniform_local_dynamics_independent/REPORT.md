# Independent local-dynamics reconstruction with decreasing live formation

This answers the neutral question in INPUT_SPEC.md. No newer author transport,
ramp or uniform-local normal-form note, runner, result, checkpoint or registry
was opened. The premises and fourth-order coefficient are reused from the
previously sealed hard-core packet. This is a conditional mathematical result
for the supplied quantum models, not a native implementation or phase claim.

## Result

A sufficient construction exists for both supplied penalties. In dimension
three, fix \(J>0\), use the tenth-order number/gauge-preserving local preparation
defined below, and set
\[
 \Delta=\frac{J}{2\epsilon^4},\qquad t=\frac{J}{2\epsilon^3},
 \qquad 0<\beta(\epsilon)\le\beta_0\epsilon^7.                 \tag{1}
\]
For any bounded gauge-invariant field observable \(A\) with fixed bounded
support and any fixed \(T<\infty\),
\[
 \sup_{\Lambda,\rho}\sup_{0\le s\le T}
 \left|\operatorname{Tr}\!\left[
 A\Phi^\epsilon_{\Lambda,s}(U_{\Lambda,\epsilon}^\dagger
 \rho U_{\Lambda,\epsilon})\right]
 -\operatorname{Tr}\!\left[Ae^{-isH_{\rm ring}}\rho
 e^{isH_{\rm ring}}\right]\right|\le C_{A,T,J,\beta_0}\epsilon. \tag{2}
\]
Here \(H_{\rm ring}=-J\sum_pX_p\), the volumes are cubic tori with even sides
at least six, and \(\rho\) is any density in their supplied ice code. Arbitrary
ice-field entanglement and winding-sector mixtures/coherences are permitted;
no product-state or spatial-mixing assumption is imposed. Constants and the
small-\(\epsilon\) threshold are independent of volume.

More generally, in fixed dimension \(d\), order \(r=2d+4\) and
\(\beta=o(\epsilon^{2d})\) suffice for convergence. The choice
\(\beta\le\beta_0\epsilon^{2d+1}\) gives \(O(\epsilon)\). These powers are
sufficient, not optimal. The result concerns the specified dressed preparation.
It does not establish the same uniform statement for the undressed bare state,
fixed positive \(\beta\), or growing observation times. Formation is strictly
enabled at every finite parameter value; its local effect vanishes in this
chosen limit. No histories are conditioned to have no birth.

## 1. Onsite representatives and the relevant grading

Use the checked qutrit matter \(0,+,-\), spin-half links, identical bosonic
hard-core hopping, and
\[
 G_x=\operatorname{div}E_x+1_A(x)-q_x=0.
\]
Assign the outgoing links to each cell. The unconstrained cell Hilbert
dimension is \(D_*=3\,2^d\), independent of volume and \(\epsilon\).
Hops act on neighboring cells. Locality is applied on this tensor product;
the constrained physical Hilbert space is not assumed to factorize.

For the original penalty take \(Q=N_B\). For the homogeneous field-star
model use the onsite matter representative
\[
 Q_*=\frac12\sum_x(q_x-1_A(x))^2.                           \tag{3}
\]
It equals \(\frac12\sum_x(\operatorname{div}E_x)^2\) on the physical sector.
All states and operations used below preserve that sector, so this extension
changes no physical prediction. It is not an equality off that sector, nor an
identification of the two models after births.

For either representative write
\[
 H_\epsilon=\Delta(Q+\epsilon V),                         \tag{4}
\]
where \(V\) is the dimensionless negative hopping sum. \(Q\) is an onsite
sum with integral or half-integral local spectrum. Every hop changes its
penalty by \(+1\) or \(-1\). For \(Q_*\), an A-to-B positive hop raises the
penalty, and an A-to-B negative hop lowers it. The reversed hops have the
opposite changes. Therefore
\[
 \mathcal P_QV=0,\qquad e^{i\pi Q}Ve^{-i\pi Q}=-V.         \tag{5}
\]
The exact local transition check includes both charges and orientations.
The large \(\Delta\) term cannot simply be counted as an interaction speed.

## 2. Explicit finite-order local preparation

Define
\[
 \mathcal P_Q B=\frac1P\int_0^P e^{iuQ}Be^{-iuQ}\,du,\qquad
 \mathcal I_Q B=\frac1P\int_0^P i(u-P/2)e^{iuQ}Be^{-iuQ}\,du, \tag{6}
\]
with \(P=2\pi\) for \(N_B\), \(P=4\pi\) for \(Q_*\). On a nonzero penalty
difference \(\omega\), \(\mathcal I_Q\) divides by \(\omega\). Thus
\[
 [Q,\mathcal I_QB]=B-\mathcal P_QB,\qquad
 \|\mathcal I_QB\|\le P\|B\|/4.                            \tag{7}
\]
For Hermitian \(B\), \(\mathcal I_QB\) is anti-Hermitian. The maps leave
local support unchanged, because \(Q\) is onsite. They preserve commutation
with number, each species count and all \(G_x\).

Starting from the polynomial \(Q+\epsilon V\), perform the following finite
recursion through order \(r\). If \(B_n\) is its order-\(n\) coefficient after
the preceding conjugations, set
\[
 S_n=\mathcal I_QB_n,\quad D_n=\mathcal P_QB_n,\quad
 U_r=e^{\epsilon^rS_r}\cdots e^{\epsilon S_1}.             \tag{8}
\]
At each step compute BCH through order \(r\). Since
\([S_n,Q]=-(B_n-D_n)\), the new order-\(n\) coefficient is \(D_n\);
lower orders are unchanged. This is a finite algorithm defining the actual
unitaries, not a formal claim of uniform convergence as \(r\to\infty\).

Only overlapping supports survive a nested commutator. At fixed order all
\(S_n,D_n\) are finite-range sums of connected terms with uniformly bounded
per-cell interaction norms. Constants depend on \(r,d\), not volume.
For decompositions with support sizes at most \(a,b\), the elementary estimate
\(\|[A,B]\|_1\le2(a+b)\|A\|_1\|B\|_1\) follows by assigning an overlap
to the term containing the chosen cell. Here \(\|F\|_1=\sup_x\sum_{Z\ni x}
\|F_Z\|\). Equation (7), this estimate and the finite BCH sums give recursive
finite bounds on every coefficient, starting from \(\|Q\|_1\le2\) and
\(\|V\|_1\le2d\). Thus no volume-dependent norm enters that induction.
Averaging is applied termwise, so each term of \(D_n\) commutes with \(Q\).
Each \(S_n\) commutes with record number, both species counts and Gauss.

The actual preparation is \(U_r^\dagger\). It is a finite sequence of
finite-range Hamiltonian evolutions generated by the Hermitian \(-iS_n\)
for positive durations \(\epsilon^n\), applied in order \(n=r,r-1,\ldots,1\).
This is an additional
supplied preparation resource; no claim is made that the bare hopping
dynamics implements these controls.

The grading (5) gives parity \((-1)^n\) at order \(n\). Since \(D_n\)
commutes with \(Q\), every odd \(D_n\) is zero, including \(D_1\).
Block diagonalization with respect to the entire onsite penalty is useful:
preserving just a global low-space projector would not alone remove the
large onsite term from a propagation bound.

## 3. Uniform local remainder

The exact transformed Hamiltonian is
\[
 U_rH_\epsilon U_r^\dagger=H_{\rm bd}+R_r,\quad
 H_{\rm bd}=\Delta Q+F_r,\quad
 F_r=\Delta\sum_{n=2}^r\epsilon^nD_n.                    \tag{9}
\]
\(F_r\) has fixed finite range and interaction strength at most
\(C_r\Delta\epsilon^2\). The exact remainder admits an anchored decomposition
\[
 R_r=\sum_x\sum_{\ell\ge0}R_{x,\ell},\quad
 \operatorname{supp}R_{x,\ell}\subset B(x,c_r+\ell),\quad
 \|R_{x,\ell}\|\le C_r\Delta\epsilon^{r+1}e^{-\mu\ell},    \tag{10}
\]
uniformly over tori and sufficiently small \(\epsilon\). This local statement,
rather than a bound \(O(V\epsilon^n)\) on the total norm, is needed.

Here is a finite-order proof. At a step \(n\), Taylor-expand
\(e^{\epsilon^n\operatorname{ad}S_n}\) on each retained coefficient only as
far as needed through degree \(r\). Each discarded Taylor remainder is an
integral of a fixed finite nested commutator conjugated by
\(e^{u\epsilon^nS_n}\), \(0\le u\le1\). Before conjugation it is a sum of
bounded-range terms with per-cell norm \(C_r\epsilon^{r+1}\) or smaller.
The normalized onsite \(Q\) has bounded local norm; multiplication by
\(\Delta\) occurs afterward. Earlier remainders undergo only the remaining
finite sequence of these small-time conjugations.

For a term initially supported near \(x\), the finite-range locality bound
for that sequence, whose total interaction-time strength is \(O_r(\epsilon)\),
approximates its conjugate by its conditional expectation onto
\(B(x,c_r+\ell)\), with error at most
\[
 C_r\|B\|(1+\ell)^d e^{-\mu_0\ell}.
\]
Average the exterior cell unitaries and sum their commutator bounds to obtain
this estimate. Differences of successive conditional expectations supply
the shell terms. Absorb the polynomial factor by reducing the decay rate.
There are only finitely many steps, so constants remain uniform and (10)
follows. No infinite-order series or uniform global spectral gap is assumed.

The same argument on a local normalized birth operator \(j_e\) gives
\[
 \widetilde j_e=U_rj_eU_r^\dagger=\sum_{\ell\ge0}j_{e,\ell},
 \quad \|j_{e,\ell}\|\le C_re^{-\mu\ell},\quad
 \|\widetilde j_e\|=\|j_e\|\le1.                         \tag{11}
\]
It also gives \(\|U_rAU_r^\dagger-A\|\le C_{r,A}\epsilon\) for each fixed
local \(A\), by integrating commutators with the small-time generators.
This is local closeness, not global closeness of large-volume states.
The sequence has finitely many pulses. Applying the time-independent locality
bound successively and, if needed, reducing its decay rate at each step suffices;
no unverified time-dependent locality theorem is being imported. The recursive
coefficient bounds give a positive, volume-independent threshold making the
total preparation interaction-time strength bounded.

## 4. Checked locality input and polynomial cone volume

The external locality input is Nachtergaele--Sims,
[math-ph/0506030v3](https://arxiv.org/pdf/math-ph/0506030v3), Theorem 1,
its interaction norm (1), and the complete Section 3.1 proof. It applies to
finite-dimensional tensor-product cells on a metric space with finite
weighted interaction norm. Here the cell dimension, finite ranges and
support sizes are fixed. Its norm is bounded by a constant times the
per-cell interaction strength. The torus metric is allowed. No state,
translation-invariance or spectral-gap assumption is required. Its separate
exponential-clustering theorem is not used.

For \(F_r\), that theorem plus the trivial norm bound gives
\[
 \|[B_Y,\tau_{F_r,s}(A)]\|
 \le C_A\|A\|\|B_Y\|
 \min\{1,|Y|e^{-\mu[\operatorname{dist}(X,Y)-v_rs]}\},
 \qquad v_r\le C_r\Delta\epsilon^2.                      \tag{12}
\]
A field \(A\) commutes with the onsite matter \(Q\), and each \(D_n\)
commutes with \(Q\); hence \(\tau_{{\rm bd},s}(A)=\tau_{F_r,s}(A)\).
The large onsite energy therefore contributes no propagation speed in this
comparison. For the star model this uses the justified extension (3).

Uniform torus growth gives \(|B(x,L)|\le C_d(1+L)^d\), also when a cone is
wider than a period. For terms on \(B(x,c_r+\ell)\), sum the clipped bound
(12) over their anchors. Split at radius
\[
 c_r+\ell+v_rs+\mu^{-1}\log[C(1+\ell)^d]+O(1).
\]
Inside use the ball volume; outside sum exponential tails against polynomial
shell counts. A valid bound is
\[
 \sum_x\min\{1,C(1+\ell)^d
 e^{-\mu[\operatorname{dist}(x,X)-c_r-\ell-v_rs]}\}
 \le C_{r,A}(1+\ell+v_rs)^d(1+\ell)^d.                  \tag{13}
\]
The proof remains valid on a torus smaller than the splitting radius.
Using (10)-(11), their exponential shell tails absorb all \(\ell\) factors:
\[
 \sum_{x,\ell}\|[R_{x,\ell},\tau_{{\rm bd},s}(A)]\|
 \le C_{r,A}\|A\|\Delta\epsilon^{r+1}(1+v_rs)^d.          \tag{14}
\]
The corresponding sum for \(\widetilde j_e\) is bounded by
\(C_{r,A}\|A\|(1+v_rs)^d\). Merely keeping the unclipped exponential in
(12) would miss this sufficient polynomial schedule.

## 5. Full birth backaction and local Duhamel bound

The transformed generator has Hamiltonian (9) and jumps
\(\sqrt\beta\,\widetilde j_e\), with at most two refinements per edge.
For one jump,
\[
 \mathcal D_j^*(B)
 =\tfrac12\{j^\dagger[B,j]+[j^\dagger,B]j\}.              \tag{15}
\]
Both the CP birth term and the no-event anticommutator are included.
The norm is controlled by the two commutators since \(\|j\|\le1\).
One coherent sign, or the two charge-resolved channels together, has the
supplied loss \(\beta P_{\rm vac,e}\). The two coherent signs at that
strength are not silently added.

The finite-volume open Heisenberg semigroup is unital CP and norm contractive.
Apply Duhamel with the block-diagonal unitary dynamics as reference; bound
the remaining open-semigroup factor by contraction. Equations (14)-(15)
give, without any state assumption,
\[
 \sup_{s\le T}\|
 \widetilde\Phi_s^{\epsilon,*}(A)-\tau_{{\rm bd},s}(A)\|
 \le C_{r,A}\|A\|T(\Delta\epsilon^{r+1}+\beta)
 (1+C_r\Delta\epsilon^2T)^d.                            \tag{16}
\]
No locality theorem for the full perturbed generator is needed. Neither a
small global number of births nor a no-birth conditioning is assumed.
In large volumes the total event number need not be small.

## 6. Restriction of the reference to ring dynamics

For \(Q=N_B\), also fix the preserved no-minus and \(N=N_0\) sector.
Its \(Q=0\) states have exactly the initial A-plus/B-vacant matter pattern.
For \(Q_*\), the zero-penalty matter pattern is already that pattern.
Gauss supplies the ice field. All \(D_n\) preserve these conditions.

The previously checked fourth-order calculation gives on this code
\[
 PD_2P=-MP,\quad
 PD_4P=M(2d-1)P-2\sum_pPX_pP,\qquad M=dV/2.             \tag{17}
\]
It also holds for the all-penalty normalization (8). At each fixed finite
volume, two formal block diagonalizations differ in the low sector by a
near-identity formal unitary. Since all lower coefficients there are zero
or scalar, this cannot change the first nonscalar fourth-order coefficient.
The independently written checker also verifies the full matrix coefficient,
not merely the eigenvalue splitting. All higher odd \(D_n\) vanish.

Taking the matrix element in the fixed matter pattern yields local field
interactions. Remove the \(D_2\) scalar on the ice sector. On other field
sectors this subtraction defines a convenient local extension; no equality
of the removed interaction to a scalar off ice is needed. The order-four
extension has strength \(O(J)\) and restricts to \(H_{\rm ring}\) plus a
scalar. The remaining orders \(6,8,\ldots,r\) have strength
\[
 O_r(\Delta\epsilon^6)=O_r(J\epsilon^2).                 \tag{18}
\]
They all preserve ice. Apply the same local comparison, now at bounded
reference speed, to these field extensions, and then evaluate on the invariant
ice sector. This gives \(C_{A,T}\epsilon^2\). A nonlocal projected observable
is never substituted into a locality theorem.

For the prepared initial state, move \(U_r\) through the expectation; its
observable becomes \(U_rAU_r^\dagger\). Replacing that by \(A\) costs
\(C_A\epsilon\), using contraction. Combining this, (16) and (18) gives
\[
 {\rm error}\le C_{r,A,T,J}
 \left[\epsilon+\epsilon^2+
 \epsilon^{r-3}(1+\epsilon^{-2})^d+
 \beta(1+\epsilon^{-2})^d\right].                       \tag{19}
\]
This proves (2). With \(r=2d+4\), the remainder times cone volume is
\(O(\epsilon)\), while \(\beta=o(\epsilon^{2d})\) makes the birth term vanish.
Constants may be large at fixed high order. No optimality or useful small
experimental prefactor is asserted.

## 7. Independent controls and unsuccessful routes

normal_form_check.py imports only the sealed independent Gauss-sector builder.
On the complete nine-state physical square it computes (8) through order ten
with exact rational matrices for both penalties. Every coefficient commutes
with its penalty, every generator preserves record number, and odd coefficients
vanish. The low even coefficients are
\[
 D_2=-2I,\quad D_4=\begin{pmatrix}2&-2\\-2&2\end{pmatrix},
 \quad D_6=\begin{pmatrix}-6&10\\10&-6\end{pmatrix},
\]
\[
 D_8=\begin{pmatrix}34&-46\\-46&34\end{pmatrix},\qquad
 D_{10}=\begin{pmatrix}-218&230\\230&-218\end{pmatrix}.
\]
The two constructions agree exactly on the original-number sector, but their
full penalty diagonals differ. Other exact controls check the homological
inverse for integral/half-integral modes, all local hop/birth penalty gaps,
and the scaling exponents. Finite torus shell sums also test wraparound.

The full nine-state Lindblad control uses \(J=1,\beta=\epsilon^7\) and the
actual prepared state. For one link \(Z\) at time one, errors against the
square's ring value are \(0.246085,0.144087,0.0828431\) at
\(\epsilon=0.16,0.12,0.09\). Remainder norms divided by
\(\Delta\epsilon^{11}\) are approximately
\(5.61,5.87,6.03\times10^4\). These expose sizable high-order constants;
they do not replace the locality proof. The square is a local coefficient
control, not a torus satisfying the period-at-least-six hypothesis.

The scientific checker passed its first run. Complete results, stdout,
empty stderr and receipt are preserved. A failed external lookup of a nonexistent
arXiv version, and a rejected report-file patch with a missing patch prefix,
are recorded separately; neither changed a scientific calculation. The following
routes were rejected analytically rather than used without justification:

- An extensive norm remainder alone does not yield a volume-uniform theorem.
- Counting the onsite penalty in a naive propagation speed loses the useful
  scale. Its removal here is justified by (3), (5) and all-penalty averaging.
- Fourth order alone is inadequate for the chosen growing-cone comparison.
- Event probabilities alone omit no-event backaction; (15) includes it.
- Local closeness of the bare and dressed preparations does not control their
  later difference under fast propagation through a growing region. The bare
  uniform-volume claim remains unproved here.

## Sources and remaining boundaries

The imported locality theorem was read with its hypotheses and proof:
Nachtergaele--Sims, math-ph/0506030v3, Theorem 1 and Section 3.1.
The downloaded PDF hash is
c6af8d70ba5081a5d5bf000881d47fca6bfd19eb9a9bc74ff40939e48079c498.

For established perturbative context, Section 4.4 of Bravyi--DiVincenzo--Loss,
[1105.0675v1](https://arxiv.org/html/1105.0675v1), was read through its
local recursion and interaction-strength proof. Its ground-energy theorem
is not used as a dynamical theorem. The all-penalty recurrence, finite local
integral remainder and open comparison needed here are written explicitly
above. Exact downloaded source/read identities are in the evidence.

This result requires the supplied enlarged spaces, gauge sector, quantum
amplitudes, bosonic statistics, scalable energies, decreasing positive
formation and the extra local preparation. It does not preserve each site's
occupation during preparation; it preserves whole-record species/counts and
Gauss exactly. No native compiler, bounded apparatus-energy construction,
fixed-rate or indefinite-time theorem, thermodynamic phase, photon or Lorentz
claim follows. The proof does not inspect or prejudge the unread author work.
