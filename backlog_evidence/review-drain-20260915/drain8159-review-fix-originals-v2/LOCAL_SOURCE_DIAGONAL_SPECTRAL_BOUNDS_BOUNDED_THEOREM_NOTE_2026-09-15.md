---
claim_id: local_source_diagonal_spectral_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/local_spectrum_check_2026_09_15.py
upstream_dependencies: ["docs/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md"]
claim_scope: "Bounded conditional local-source diagonal spectroscopy; supplied hypotheses and limit order retained in full proofs."
---

# Local-source diagonal spectroscopy

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15](POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK10_LOCAL_SOURCE_SPECTRA_AND_DARK_THRESHOLD

Original source identity: `BLOCK10_LOCAL_SOURCE_SPECTRA_AND_DARK_THRESHOLD.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Local pair spectroscopy and a threshold invisible to finite strings

Personal derivation, 2026-09-15. PROVISIONAL; personal analytic review and bounded checks completed.
No independent scientific audit or retained-status decision.
This extends the exact polarized word sector (`BLOCK9_POLARIZED_CHARGED_SECTOR_AND_FLAT_THRESHOLD.md`)
for the same supplied native Hamiltonian and boundary representation.
No physical vacuum or new primitive is selected. Put lambda=|t|>0,
a=sqrt(3)lambda and E_pol=2U-4a. The result concerns actual local sources,
not only the infimum of the entire charged Hilbert space.

#### 1. An explicit phase frame and a local translation-covariant source

With lexicographic vertex ordering, the native phase frame in Block9 has
the particularly simple closed form

    d(m,w)=epsilon_m  if n=|w| is odd,
           i          if n is even.                         (1)

For a positive append at the endpoint p, the native T amplitude is
-i epsilon_p. For a negative prepend at m, it is i epsilon_m.
To check the first sign, on a positive edge (p,p+e_j) the reference
ordered-star Z product is epsilon_p. The existing incoming path edge
precedes every outgoing edge in that star, so it supplies one extra
minus sign; the neutral new endpoint is untouched. The B difference
is2 because the charged endpoint has even occupied degree and the neutral
endpoint has odd degree. For prepend, the initial vertex is neutral and
the charged upper vertex has its changed outgoing edge after the incoming
edge in the ordered star. The reference star product is-epsilon_m and
the B difference is-2. The two displayed amplitudes follow.

Since epsilon_p=(-1)^n epsilon_m, (1) sends both forward moves to-1.
Reverse moves follow by adjoints; the word graph is connected, so this
agrees with Block9's frame fixed at the origin length-one x-word.
For negative t multiply this frame by(-1)^n; that changes only an overall
sign on each length-one source and has no effect on the spectral formulas.

Let Omega denote the polarized neutral product state and define the local
Hermitian Pauli source

    C_m=epsilon_m/sqrt(3) sum_(i=1)^3 X_(m,i).       (2)

It is supported on three outgoing physical edges. Each term creates one
negative charge at m and one positive charge at m+e_i. Under (1),
C_m Omega maps exactly to |m> tensor u, u=(1,1,1)/sqrt(3).
No state-dependent nonlocal source dressing has been inserted.

There is also a local symmetry implementation of the word translation.
Translate the bits by b and complement them if epsilon_b=-1; this preserves
the reference and simply translates its flipped edges. Multiply a finite
flip basis state by(-1)^(|b|_1 n). On local Pauli operators this extra
factor is the uniform Z-conjugation automorphism when b is odd. The
combined transformation fixes Omega and is a genuine representation of
Z^3: flip count is preserved and the parity factors compose. Call it U_b.
Equation(1) conjugates U_b to plain anchor translation. It therefore
commutes with the supplied sector Hamiltonian, and

    U_b C_m U_b^*=C_(m+b).                         (3)

Thus the Fourier fibers used below are those of this explicit symmetry.
The bit complement and Z action are essential; a naive bare permutation
of the native Pauli variables is not substituted for (3).

#### 2. A conserved internal count on a diagonal momentum line

At k=(theta,theta,theta), the left creation vector is e^(i theta)u.
Choose any orthonormal w1,w2 spanning u-perp and rotate each word factor
to the alphabet {u,w1,w2}. The ring operator is invariant under this
common unitary rotation, since every swap is. Define

    M_n=sum_(j=1)^n (I-|u><u|)_j.                 (4)

It counts the non-u letters in this rotated alphabet. Rings preserve M,
and both endpoint creations add u, so the complete H(k) reduces each
integer-M subspace. This is not the number of native charged particles;
it is a conserved word-color count on this symmetry line only.
An arbitrary vector supported on word lengths <=N lies in M<=N.

For M>=1, specify a basis by the ordered non-u colors c1,...,cM and
nonnegative u-run lengths r0,...,rM:

    u^r0 c1 u^r1 ... cM u^rM.                    (5)

Left creation increases r0, with phase e^(i theta); right creation
increases rM, with phase1. Swapping a u across marker j transfers one
unit between r_(j-1) and r_j. A swap of adjacent non-u colors contributes
an additional positive graph-Laplacian form and may be dropped in a lower
bound. There is no added physical marker degree of freedom: this is a
unitary change of basis within the existing word space.

#### 3. A uniform lower bound within every finite-M sector

Write f(x) for the coefficients of a finite-support vector in (5), and
let I_j x mean inserting one extra u in run j. The positive isometry
identity in Block9 writes H-E_pol as two endpoint edge forms, positive
endpoint boundary terms, and the ring form. For each x, telescope

    (1-e^(i theta)) f(x)
      =[f(I_0 x)-e^(i theta)f(x)]
       +sum_(j=0)^(M-1)[f(I_(j+1)x)-f(I_j x)]
       -[f(I_M x)-f(x)].                         (6)

Weighted Cauchy-Schwarz gives

    4 sin^2(theta/2)|f(x)|^2
       <=(2/a+M/J){a|f(I_0x)-e^(i theta)f(x)|^2
                  +a|f(I_Mx)-f(x)|^2
                  +J sum_j |f(I_(j+1)x)-f(I_jx)|^2}.           (7)

Each endpoint edge occurs once when x is summed. Each ring edge that swaps
u and a non-u letter also occurs exactly once: remove the transferred u
from its source run to recover the unique x, its marker index, and its
ordered color sequence. This injective recovery is the important counting
step. Other ring edges and endpoint boundary terms are positive.
For every fixed M>=1 and J>0, density then extends (7) to

    H(k)|_M >= E_pol+delta_M,
    delta_M=4 sin^2(theta/2)/(2/a+M/J).            (8)

For M=0 the same telescope has no ring steps and gives
 delta_0_bound=2a sin^2(theta/2). The exact M=0 edge is given next.
No finite-volume gap, mixing estimate or large matrix diagonalization is
used in (8). The bound is uniform in word length at each fixed M, but
tends to zero as M tends to infinity, in agreement with Block9.

#### 4. Exact local symmetric-source spectrum

The M=0 subspace is spanned by |n>=u^(tensor n), n>=1. Every ring term
annihilates it. Its Hamiltonian, for every uniform J>=0, is

    H_rad=2U-a[(1+e^(i theta))S+(1+e^(-i theta))S^*],             (9)

where S|n>=|n+1> and S^*|1>=0. A scalar length-dependent phase changes
(9) to 2U-h(S+S^*), with h=2a|cos(theta/2)|. The source(2) is |1>.
The sine transform of a half-line adjacency gives, for h>0,

    d mu_theta(E)=sqrt(4h^2-(E-2U)^2)/(2pi h^2) dE,
    |E-2U|<=2h.                                  (10)

It is a normalized absolutely continuous semicircle. Its lower edge is
2U-2h, strictly above E_pol unless theta=0 modulo2pi. It has no atom.
At theta=pi modulo2pi, h=0, and the source measure is exactly delta_(2U).
This is a spectral atom at a special momentum; it is not an isolated
massive lowest band. Indeed the entire M=0 space has eigenvalue2U there.

For real time s and imaginary time tau>=0, the exact source responses are

    <1|exp(-isH_rad)|1>=exp(-2iUs) J_1(2hs)/(hs),
    <1|exp(-tau H_rad)|1>=exp(-2U tau) I_1(2h tau)/(h tau),       (11)

with the continuous value1 for the Bessel quotient at zero. For h>0,
the imaginary-time response has prefactor
 (2sqrt(pi) h^(3/2) tau^(3/2))^(-1)
times exp[-(2U-2h)tau] asymptotically. A continuum edge rather than a
single exponential is observable in this supplied source channel.

This half-line source mechanism has a close predecessor in the all-even
sector of the2012 quantum-string paper cited in Block9. Here it follows
exactly from the native cubic RK operator, without their perturbative
Hamiltonian or a string-tension term.

#### 5. Every bounded-length source misses an interval above the full floor

Let psi_theta be any fiber vector supported on word lengths1,...,N.
Its M components lie in0,...,N. Since delta_M decreases with M, equations
(8) and the M=0 bound give, for J>0,

    1_[E_pol,E_pol+delta_N)(H(k)) psi_theta=0.      (12)

For a finite-support physical edge operator applied to Omega and projected
to this D=2 sector, only finitely many changed edges and hence a bounded
word length can occur. Fourier transforming its translates under(3)
gives precisely such a vector, up to source-dependent anchor phases.
Thus(12) is a statement about actual finite local preparation, under the
specified momentum convention and polarized boundary state. It is not
an assertion about all momenta or all states of this Hamiltonian.

Block9 still gives inf spec H(k)=E_pol. For theta not0 modulo2pi, that
infimum is approached only with unbounded M; all finite-word sources have
a positive separation that depends on their support size. There is no
single support-independent dark interval: delta_N tends to zero. The
union of finite-word source vectors is dense, which is fully compatible
with these source-dependent gaps.

#### 6. Zero-ring control and near-line leakage

At J=0, a one-letter w in u-perp generates the reducing two-half-line
space u^r w u^s. The left phase can be gauged away. Its source spectral
measure is the convolution of two semicircles with hopping a, independent
of theta; it reaches E_pol. Its return amplitude is

    exp(-2iUs)[J_1(2as)/(as)]^2.                  (13)

The density near E_pol+epsilon is asymptotic to
epsilon^2/(8pi a^3), and the integrated weight to
epsilon^3/(24pi a^3). Thus the positive-J restriction in(12) matters.
A single native oriented-edge source has weight1/3 in M=0 and2/3 in
M=1; at J=0 these orthogonal source measures combine with those weights.

For k near k0=(theta,theta,theta), let

    eta=2lambda sqrt(sum_i |e^(ik_i)-e^(i theta)|^2).

Only left creation changes, so ||H(k)-H(k0)||<=eta. Put delta=delta_N
and Q=1_E_pol,E_pol+delta/2 (`H(k`)). For P=1_(M<=N), the spectra of
H(k0)|_P and H(k)|_Q are separated by at least delta/2. The Sylvester
identity for X=PQ has right side -P[H(k)-H(k0)]Q. Its convergent Laplace
integral gives ||PQ||<=2eta/delta. Consequently for psi=Ppsi,

    ||Q psi||^2 <=min(1,4eta^2/delta^2)||psi||^2.   (14)

This is a bound on source leakage near a symmetry line, not a spectral
gap for the whole fiber. It requires theta not0 and J>0 so delta>0.
No analytic continuation of an isolated particle pole is asserted.

#### 7. Scope and remaining work

The native background, J,lambda and translation symmetry are supplied.
Spectral measure, spectral infimum, a momentum-special atom and an isolated
particle band are different objects here and have been kept distinct.
The word-color symmetry is exact on the diagonal line; generic momenta
mix its sectors. The periodic ground-state representation and any selected
physical vacuum remain separate.

The runner checks5760 literal native forward moves, the closed phase and
local translation/source identities, a full363-dimensional word-color
rotation, and complete fixed-M matrices through M=3 and length7. It
checks the injective recovery of every u-marker swap edge and the full
energy form including its endpoint boundary terms. Full native-word
closed-walk moments through order8 match the two exact source measures;
these moments do not reach the cutoff. Bessel integrals have separate
sine-quadrature controls. Native local operator definitions are explicitly
reused from Block9, so this is not an independent implementation or review.
No numerical extrapolation establishes the infinite statements.
See the N1-N8 review (`BLOCK10_ROUTE_AND_NO_GO_REVIEW.md`).

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK10_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK10_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Local-source spectroscopy: N1-N8 personal review

Companion to the exact source derivation (`BLOCK10_LOCAL_SOURCE_SPECTRA_AND_DARK_THRESHOLD.md`).
The negative statement is a source-specific spectral interval in one
boundary representation on a specified momentum line. A general claim
that there are no measurable excitations or no particles is **FAIL**.

#### N1 — Real mechanisms examined

| Family | Work performed | Status |
|---|---|---|
| Native local operator and symmetry | Derive closed parity phase, explicit three-edge Pauli source and local symmetry | ATTEMPTED; the source has no hidden nonlocal dressing |
| Conserved word-color charge | Rotate all word factors and prove count preservation on the diagonal line | ATTEMPTED; generic momentum control explicitly breaks it |
| Configuration edge-form lower bound | Unique insertion-base reconstruction and weighted telescoping | ATTEMPTED; positive finite-M gap uniform in length |
| Source cyclic spectral transform | Exact radial sine transform, Bessel response and special-momentum atom | ATTEMPTED; this is a positive spectral result, not no excitations |
| Zero-ring alternative | Orthogonal local source reduces to two half-lines | ATTEMPTED; it reaches the full threshold, defeating extension to J=0 |
| Off-line source response | Bounded Hamiltonian difference and a separated-spectrum Sylvester estimate | ATTEMPTED; controlled leakage bound, no whole-spectrum gap |

These are different mathematical objects/mechanisms. Their number does
not establish a universal no-go. None is declared ruled out by retained
authority; the broad claim fails because positive alternatives survive.

#### N2 — Dependence and scope

Finite-M gap, finite-source dark interval and growing color count are
consequences of the same telescoping bound. They are one mechanism, not
three independent walls. The radial source formula is an exact reducing
subspace result. The broad vacuum-selection and full-field obligations
have unresolved implications; no independent physical-wall count is made.

#### N3 — Hidden hypotheses

Polarized finite excitation is supplied. J>0, lambda>0 and nonzero diagonal
momentum are explicit for the dark interval. The bound depends on source
word length; there is no uniform gap for all local sources. The source is
an actual finite Pauli operator with explicit staggered coefficients.
Translation is the displayed geometric/complement/Z symmetry, not a bare
permutation. The non-u count is a word-basis quantum number and not a
new physical particle species. No approved primitive or physical clock is
replaced by this conditional Hamiltonian analysis.

#### N4 — Witness matching

Block9 supplies the exact word Hamiltonian and its whole-fiber infimum.
The present native parity calculation makes its phase frame local-source
compatible. Neither Block8 twist flatness nor any clock no-go is a witness
against local spectral response. The2012 string paper supplies context,
not a theorem imported onto this carrier. No mismatched no-go is cited.

#### N5 — Resolution audit

Per edge:5760 native endpoint amplitudes checked against the parity formula.
Per source: a literal three-edge operator is matched to |1>; arbitrary
bounded local support is addressed analytically through its finite word
length. Per color sector: the bound is analytic for every finite M;
complete finite checks cover M0-3. Per mode: exact conservation and dark
interval only on k=(theta,theta,theta); a nearby-mode leakage bound is
separate, and a generic-mode control fails conservation as expected.
Lattice-wide: only the polarized representation is considered. The entire
fiber has no gap above E_pol, and the source at theta=pi has a spectral
atom. The claim is not extended to all momenta, all sources uniformly,
all vacua or all physical particles.

#### N6 — Surviving closure paths

At theta=0 the symmetric source reaches the full threshold. At J=0 an
orthogonal local source reaches it at every diagonal momentum. At positive
J the symmetric source still has an explicitly computed continuum and a
special-momentum atom. Generic momentum mixes color sectors. Other neutral
backgrounds and periodic states remain untouched. None of these requires
an axiom revision; deriving a physical vacuum is a distinct task.

#### N7 — Strongest objection

The apparent invisibility may just be a symmetry selection rule in an
extreme boundary state, so it cannot diagnose a failed particle theory.
Correct. The exact local symmetry and conserved count identify precisely
that rule, and(14) bounds its loss away from the line. A useful next task
is to determine the observable spectral response in the periodic or another
nonpolarized vacuum, or to prove a native law selects one. The result
should be used to reject unqualified inference from a whole-sector floor,
not to reject the framework.

#### N8 — Prior comparison

Block9 established the all-momentum full-sector threshold but explicitly
left local-source weight open. This block settles a local channel exactly
and all finite-length sources along a symmetry line through a uniform
color-sector estimate. Standard half-line spectra, Cauchy-Schwarz and
Sylvester bounds are not new mathematics. The quantum-string source-sector
idea was already credited in Block9. Everything remains personal and
provisional; no independent audit grade is asserted.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: local_spectrum_check_2026_09_15](../scripts/local_spectrum_check_2026_09_15.py); [current cache](../logs/runner-cache/local_spectrum_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
