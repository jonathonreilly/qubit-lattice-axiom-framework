# Exact interacting pair-pulse functional on the native hard-core carrier

**Status:** conditional mathematical discovery in an explicitly supplied
Hamiltonian. Independent checking is pending. No formal audit verdict,
framework law selection, condensate, scattering theorem or tensor phase is
claimed.

The complete fourth-order energy and number-density functionals are derived
below for arbitrary complex amplitudes of the five uniform E plus T2 pair
channels. The calculation keeps their actual overlapping hard-core N=4
states. It gives a positive, phase-sensitive interaction functional with
explicit cubic anisotropy. This is a new nonlinear discriminator beyond the
previous two-particle Gram and dispersion.

In particular, if s is the pair-state norm per site, a pure E pulse has
energy coefficient `(52 mu+120 tau)s²`; its 45-degree-rotated pure T2 partner
has `(54 mu+156 tau)s²`. Their tensor eigenvalues and s agree. The difference
is an exact uniform quartic interaction effect, not an inference from the
harmonic comparator proposals.

## 1. Domain, source and supplied model

Use the frozen `native-stability-route/REPORT.md`, SHA256
`7eba7d0092eb4990f5ae1a46825e015c6edc18692c09cab69ad5cd3ed4d24ca9`.
The parent has selectively reconstructed its mobile Hamiltonian and
completion of squares. Its source identities are preserved in SOURCES.json.
The present calculation does not use the later coercivity theorem or
the parent's density trial as a mathematical premise.

Initial main was `e75578f7136401d4bd750131671aed9212c06291`; the final
read-only refresh found `9d15f404c63ff5b9d877e2bdc06ea8713493ffb4`. Relevant
axiom, primitive and procedure bytes did not change. Selected campaign
procedure is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. These are distinct
from the separately recorded working HEAD. The native carrier is one ordinary
physical-site qubit on the cubic torus, with commuting different-site tensor
factors, `b=|0><1|`, `n=b†b`, and vacuum Omega. The Hamiltonian, continuous
unitary pulse, chosen vacuum and its quantum interpretation are supplied
conditions, not derived from the framework axioms or its three registered
primitives. No actual record instrument is supplied here.

For the coefficient theorem take `mu,tau>0` and a cubic torus of side
`L>=13`, `V=L³`. This conservative size bound removes aliases in every
connected cluster used below. The previous Hamiltonian itself is defined
already for `L>=5`; no assertion that these coefficients are unchanged on
every smaller torus is made.

Write, at each center x,

\[
 d_i=b_{x+e_i}b_{x-e_i},\quad
 v_{ij}^{st}=st\,b_{x+s e_i}b_{x+t e_j},\quad
 Q_{E1}=(d_1-d_2)/\sqrt2,\quad
 Q_{E2}=(d_1+d_2-2d_3)/\sqrt6,
\]
\[
 Q_{Tij}=\tfrac12\sum_{s,t=\pm1}v_{ij}^{st},\quad
 P_E=\sum_{A\in E}Q_A^\dagger Q_A,\quad
 P_T=\sum_{A\in T}Q_A^\dagger Q_A.
\]

Let G have the eighteen displacements `±2e_i` and `±e_i±e_j`, and put
`m_x=sum_(y~Gx)n_y`. The exact supplied law is

\[
 H=\mu N-2\mu\sum_xP_E(x)-\mu\sum_xP_T(x)
       +\mu\sum_xn_x\binom{m_x}{2}+W_\tau,                    \tag{1}
\]
\[
 W_\tau=\tau\sum_{x,k,A}[Q_A(x+e_k)-Q_A(x)]^\dagger
                                    [Q_A(x+e_k)-Q_A(x)].
\]

The full-carrier identity used here is

\[
 H=\mathcal A+\mu\mathcal D+W_\tau,\qquad
 \mathcal D=\tfrac12\sum_xn_x(m_x-1)(m_x-2),                 \tag{2}
\]
\[
 \mathcal A={2\mu\over3}\sum_x(d_1+d_2+d_3)^\dagger(d_1+d_2+d_3)
 +{\mu\over4}\sum_{x,i<j}\sum_{a<b}(v_{ij}^{a}-v_{ij}^{b})^\dagger
                                               (v_{ij}^{a}-v_{ij}^{b}).
\]

Every term in (2) is nonnegative. No bosonic commutator for the Q's is used.

## 2. Pulse and exact coefficient theorem

For arbitrary complex five-component zeta, define

\[
 C=\sum_{x,A}\zeta_AQ_A(x)^\dagger,\qquad
 \psi(t)=\exp[t(C-C^\dagger)]\Omega.                          \tag{3}
\]

The real parameter t is a prescribed pulse parameter; (3) is not evolution
under H. The generator `i(C-C†)` is Hermitian and finite range. On each
finite torus the state is exactly normalized. Thermodynamic limits of these
states are states on the quasi-local algebra, not generally normal vectors
in the finite-particle vacuum representation; no infinite Fock-space unitary
is asserted here.

Use trace-free diagonal coordinates

\[
 u_1=\zeta_{E1}/\sqrt2+\zeta_{E2}/\sqrt6,\quad
 u_2=-\zeta_{E1}/\sqrt2+\zeta_{E2}/\sqrt6,\quad
 u_3=-2\zeta_{E2}/\sqrt6,
\]

and `v_ij=zeta_Tij`. For the invariant formula abbreviate
`v_1=v_23, v_2=v_13, v_3=v_12`, and define

\[
 U=\sum_i|u_i|^2,\quad p=\sum_i|v_i|^2,\quad
 q_E=\sum_i u_i^2,\quad q_T=\sum_i v_i^2,\quad r=\sum_i|v_i|^4,
\]
\[
 J=\sum_i|u_i|^2|v_i|^2,\quad
 L_4=\sum_i u_i^2\bar v_i^2,\quad
 M_4=\sum_{i=1}^3\bar u_i\bar v_i v_jv_k\quad(\{i,j,k\}=\{1,2,3\}),
 \qquad s=U+2p.                                               \tag{4}
\]

Each term of M4 is included once. The letter L4 denotes an invariant, not
the torus side. The pair-state norm is `||C Omega||²=Vs`; the factor two
on T follows from its actual shared-center pair incidence.

The exact small-pulse expansions, with volume-uniform remainders, are

\[
 {\langle H\rangle_t\over V}
   =t^4[\mu f_\mu(u,v)+\tau f_\tau(u,v)]+O(t^6),\qquad
 {\langle N\rangle_t\over V}=2s t^2+\kappa_4(u,v)t^4+O(t^6).    \tag{5}
\]

The full coefficients are

\[
\begin{aligned}
 f_\mu={}&52U^2+{700\over3}p^2+24|q_T|^2-{124\over3}r
 +{490\over3}Up+66J\\
 &+{22\over3}\operatorname{Re}(q_E\bar q_T)
   +{4\over3}\operatorname{Re}L_4-48\operatorname{Re}M_4,       \tag{6}\\
 f_\tau={}&120U^2+632p^2+72|q_T|^2-80r+620Up-60J\\
 &-28\operatorname{Re}(q_E\bar q_T)
   +56\operatorname{Re}L_4-96\operatorname{Re}M_4,               \tag{7}\\
 \kappa_4={}&{-26U^2+11|q_E|^2\over9}
 -{16\over3}p^2+8|q_T|^2-{28\over3}r-16Up+{32\over3}J\\
 &+{8\over3}\operatorname{Re}(q_E\bar q_T)
   +{16\over3}\operatorname{Re}L_4.                            \tag{8}
\end{aligned}
\]

Equations (6)–(8) are invariant under common phase, complex conjugation,
and all 24 proper cubic rotations. They retain coherent cross terms rather
than averaging over channel phases. They are exact Taylor coefficients on
the full hard-core carrier; their interpretation as an effective scattering
vertex would require another argument.

## 3. Full N=4 derivation and support reduction

For an unordered G edge e={a,b}, the coefficient of `b_a†b_b†` in C is

\[
 w(a,b)=u_i\quad(b-a=\pm2e_i),\qquad
 w(a,b)=-\delta_i\delta_j v_{ij}
       \quad(b-a=\delta_i e_i+\delta_j e_j),                  \tag{9}
\]

and zero on other pairs. Opposite pairs have one shell center; orthogonal
pairs have two, with equal signed coefficients. This is why the latter
weight is v rather than v/2. The weight is symmetric in a,b.

For four distinct physical sites S={a,b,c,d}, let

\[
 F(S)=w(a,b)w(c,d)+w(a,c)w(b,d)+w(a,d)w(b,c).                 \tag{10}
\]

The exact occupation-basis coefficient of `C² Omega` is `2F(S)`. Overlapping
creation pairs give zero, not an additional bosonic contribution. For a
bare annihilator with endpoints a,b and sign sigma, its residual two-site
amplitude is `2 sigma F({a,b,c,d})` when all four sites are distinct, and
zero when the residual pair {c,d} meets {a,b}.

Every uniform single-pair state satisfies `H C Omega=0`, directly from (2):
the opposite coefficients sum to zero, the signed plane coefficients agree,
the center differences vanish, and a G pair has diagonal degree one.
Also `H Omega=0`. Expansion of the *unitary* state (3), not an unnormalized
pair exponential, therefore gives

\[
 [t^4]\langle H\rangle_t={1\over4}
                   \langle C^2\Omega,H C^2\Omega\rangle.     \tag{11}
\]

For a bare type t at center x, subtract from its amplitude divided by two
the disconnected term `sigma w(a,b)w(c,d)`. The defect is

\[
 D_t(x;c,d)=\begin{cases}
 -\sigma w(a,b)w(c,d),&\{a,b\}\cap\{c,d\}\ne\varnothing,\\
 \sigma[w(a,c)w(b,d)+w(a,d)w(b,c)],&\text{otherwise}.
 \end{cases}                                                  \tag{12}
\]

The subtraction is exact within each local square: its opposite sum
vanishes because `sum u_i=0`, its plane differences vanish, and its center
differences vanish. It is not a subtraction from a positive expectation
made after discarding interference. The entire disconnected tail cancels
before a finite sum is evaluated.

Regard each Dt as a vector over unordered residual pairs, with its ordinary
occupation-basis norm. The coefficient of mu in (11)/V is exactly

\[
 f_\mu={2\over3}\|D_{d1}(0)+D_{d2}(0)+D_{d3}(0)\|^2
 +{1\over4}\sum_{i<j}\sum_{a<b}\|D_{v^a_{ij}}(0)-D_{v^b_{ij}}(0)\|^2
 +\sum_{\{y,z,w\}\subset D}|F(\{0,y,z,w\})|^2.              \tag{13}
\]

Here D in the last sum is the eighteen-site neighbor set, so there are
816 unordered triples. The diagonal term reduces to precisely these
occupied degree-three stars: a four-site configuration with nonzero F has
a perfect matching and no isolated vertex; on degrees 1,2,3 the polynomial
`(m-1)(m-2)/2` is 0,0,1. Multiple degree-three vertices are counted exactly
as they are in the actual diagonal operator.

Write `Delta_k D=D(e_k)-D(0)`. The tau coefficient is

\[
 f_\tau=\sum_k\left[
 \sum_i\|\Delta_kD_{di}\|^2
 -{1\over3}\|\sum_i\Delta_kD_{di}\|^2
 +{1\over4}\sum_{i<j}\|\sum_{a=1}^4\Delta_kD_{v^a_{ij}}\|^2
 \right].                                                     \tag{14}
\]

The first two terms together are the E doublet's orthogonal projector,
not a negative contribution assigned to an independent mode. The factors
two in `C² Omega` cancel the 1/4 in (11), yielding exactly (13)–(14).

There is a further support check on (14). Every residual pair in a defect
has the same site parity as the annihilated pair, opposite to its center.
Defects at neighboring centers are consequently orthogonal. Thus f_tau is
also six times the sum of the five one-center collective defect norms.
This identity is checked on all matrix coefficients. For the stated large
odd tori, it is a statement about these locally embedded supports, not a
claim that global parity is a torus symmetry.

Every nonzero defect has either a residual edge incident to an endpoint,
or one residual site neighboring each endpoint. Thus (12) has bounded
support. The union for a center has 946 residual pairs, and the complete
vertex set for centers 0,e1,e2,e3 has 114 vertices. These are residual-word
indices in the real N=4 carrier, not additional site factors. All sites
lie in the coordinate cube from -3 to 4. The starred diagonal sets lie
in -2 to 2; the number cycles below lie in -4 to 4. Their comparisons use
only pair displacements of size at most two. The stated `L>=13` makes these
sets and edge tests identical to their infinite-lattice versions and
prevents disconnected periodic images from becoming local interactions.

Expanding the finite sums (13)–(14) in the fifteen quadratic monomials of
`z=(u1,u2,v12,v13,v23)`, `u3=-u1-u2`, gives the complete rational Hermitian
matrices in `quartic.json`. Their denominator is 12 and their monomial order
is recorded there. A separate coefficientwise invariant expansion checks
all 225 entries of each matrix against (6)–(7), not just selected values.
All proper cubic rotations are checked coefficientwise too.

## 4. The number coefficient and its connected cancellation

Put `S=||C Omega||²=Vs` and `R=||C² Omega||²`. The N=0,2,4 components needed
from `exp[t(C-C†)]Omega` are

\[
 \psi_0=\Omega-t^2 S\Omega/2+O(t^4),\quad
 \psi_2=tC\Omega-{t^3\over6}(C^\dagger C^2\Omega+S C\Omega)+O(t^5),
 \quad \psi_4=t^2C^2\Omega/2+O(t^4).
\]

Consequently

\[
 [t^4]\langle N\rangle_t={R-2S^2\over3}.                    \tag{15}
\]

For disjoint, noninterfering pair edges the two extensive terms cancel.
The connected remainder consists of negative repeated-edge and shared-site
exclusions, and coherent four-cycle contributions. In a finite graph it is

\[
 R-2S^2=-2\sum_e|w_e|^4
 -4\sum_{e<f:e\cap f\ne\varnothing}|w_e|^2|w_f|^2
 +8\operatorname{Re}\sum_{|A|=4}\sum_{m<n}\bar P_m(A)P_n(A), \tag{16}
\]

where Pm are the three perfect-matching products in (10). For the uniform
coefficient per site, root the overlapping edges at their common site.
Root four-vertex cycle sets at an occupied site and divide by four. There
are 440 such rooted vertex sets in the geometric G graph; a missing
matching simply contributes zero. Expanding (16)/(3V) gives (8).

Two different author controls check this cancellation. One explicitly
creates C twice on a nineteen-site induced graph and compares its full
N=4 norm to (16), retaining coherent multiple matchings. Another evaluates
the central site's actual Taylor coefficient on the complete radius-two
G patch (85 physical sites), constructing only N=4 words containing the
central site. If `S0=<C Omega,n0 C Omega>`,
`R0=<C² Omega,n0 C² Omega>` and
`L0=<C Omega,n0 C†C² Omega>`, that coefficient is

\[
                  R_0/4-\operatorname{Re}(L_0+S S_0)/3.       \tag{17}
\]

Its exact agreement with (8) checks the volume/root normalization through
an actual local occupation calculation, without using the cycle builder.
Connected fourth-order number contractions are doubled edges sharing a
vertex or four-cycles, all contained in this radius-two patch.

## 5. Remainders and a strictly positive pulse interaction

Conjugation by `exp(i pi N/2)` reverses `C-C†` and leaves H,N and Omega
invariant. Both expectations are even in t. The finite-range commutator
expansion supplies volume-uniform sixth-derivative bounds, so the O(t6)
in (5) is a controlled remainder, not an assumed dilute-boson expansion.

For an explicit conservative bound, let
`wmax=max_i(|u_i|,|v_i|)` and `h0=(526/3)mu+200tau`. Write H as V translated
local terms using (1), each supported in a 125-site cube with norm at most
h0. The bounds follow from the sums of absolute coefficients of each Q,
the 153 density triples at a center, and the fifteen mobility squares.
Each site touches eighteen pair-generator edges, each of norm at most
wmax. A nonzero nested commutator of order n adds at most one site per
step. Therefore

\[
 \|\operatorname{ad}_{C-C^\dagger}^{n}H\|
 \le Vh_0(36w_{\max})^n(125)_n,\qquad
 \|\operatorname{ad}_{C-C^\dagger}^{n}N\|
 \le V(36w_{\max})^n n!,                                     \tag{18}
\]

where `(125)_n=125*126*...*(124+n)`. Unitary conjugation preserves these
norms at the Taylor remainder point. The energy remainder in (5) is at
most `h0(36wmax)^6(125)_6 |t|^6/720`; the number remainder is at most
`(36wmax)^6 |t|^6`. These loose constants prove the needed uniformity.

The quartic form is strictly positive away from zero. An exact rational
matrix certificate gives the convenient bound

\[
                  \mu f_\mu+\tau f_\tau
                       \ge(40\mu+100\tau)s^2.                \tag{19}
\]

Specifically, in the recorded fifteen-monomial basis, the matrices for
`f_mu-40s²` and `f_tau-100s²` have positive rational LDL pivots. The full
pivot lists and exact reconstruction checks are in `invariant_checks.json`;
`check_invariants.py` constructs their entries directly from (6)–(7) and
checks the rational factorization. This is a finite exact positivity
certificate, not a floating eigenvalue test or use of the coercivity result.
It bounds this pulse coefficient, not an exact scattering length.

## 6. Nonlinear channel and phase discriminators

For `v=0`, (6)–(7) give

\[
                      \epsilon_4=(52\mu+120\tau)U^2.          \tag{20}
\]

Thus all complex E directions have the same leading energy at fixed s.
Their fourth-order number coefficient can still differ through |qE|².

Identify the amplitudes with the complex symmetric trace-free matrix T
having diagonal ui and off-diagonal vij; then `s=Tr(T†T)`. The matrices
`diag(1,-1,0)` and the matrix with `T12=T21=1` and other entries zero are
related by a proper 45-degree spatial rotation. Both have s=2 and the same
eigenvalues. Their exact energy coefficients are, respectively,

\[
             208\mu+480\tau,\qquad216\mu+624\tau.             \tag{21}
\]

The nonzero difference `8mu+144tau` proves that this quartic functional is
not SO(3)-invariant under the natural tensor-amplitude action. It remains
exactly cubic invariant. This does not rule out emergent rotational
invariance after a controlled infrared analysis of another state.

The pure T subspace already displays phase selection within the trial
family. With `U=0` and fixed p, its minimum is

\[
          \min\epsilon_4=({638\over3}\mu+592\tau)p^2,          \tag{22}
\]

attained by two equal-magnitude components in quadrature and the third
zero. For the proof use
`r <= (p²+|qT|²)/2`, because the difference is
`2 sum_(i<j)(Re(v_i bar v_j))²`. In (6)–(7) the resulting coefficient of
|qT|² is `(10/3)mu+32tau>0`; the stated amplitudes saturate the bound with
qT=0. This is minimization within the pure T pulse slice, not spontaneous
time-reversal breaking of the ground state. Its normalized minimum,
`(319/6)mu+148tau`, still exceeds the pure E value in (20).

Mixing E and T changes the conclusion within another explicit trial slice.
Take `u=(x,-x,0)`, `v12=y`, and all other v zero. Then s=2(|x|²+|y|²) and

\[
 \epsilon_4=A|x|^4+B|y|^4+C_0|x|^2|y|^2
                      +R_\phi\operatorname{Re}(\bar x^2y^2),    \tag{23}
\]
\[
 A=208\mu+480\tau,\quad B=216\mu+624\tau,\quad
 C_0={980\over3}\mu+1240\tau,\quad R_\phi={44\over3}\mu-56\tau.
\]

For nonzero x,y the minimizing relative phase is real if
`mu<42tau/11` and in quadrature if `mu>42tau/11`; at equality this term
does not select the phase. Put `D0=C0-|Rphi|` and
`f=|y|²/(|x|²+|y|²)`. At fixed s, minimize
`[A(1-f)²+Bf²+D0 f(1-f)]/4`. Within this slice its minimum is pure E for
`mu<=3tau`, while for `mu>3tau` the minimizing T fraction is

\[
                f_*={2A-D_0\over2(A+B-D_0)}\in(0,1),          \tag{24}
\]

and the value is strictly below the pure E endpoint. Both threshold claims
follow by the two signs of Rphi and direct quadratic minimization. Neither
is claimed to be the global minimum over all five complex channels or a
phase boundary of H. In particular there is no justified reading of f as
the ground state's pair population.

At fixed small actual pulse density rho, (5) gives
`e=epsilon4 rho²/(4s²)+O(rho³)`. Thus the anisotropy is present in the
leading density-squared variational energy too. This does not replace
the many-body lower bound or prove a condensate. For example a pure E
pulse in `H-nu N` gives the uniform variational upper bound
`e0(nu)<=-nu²/(52mu+120tau)+O(nu³)` as nu approaches zero from above by
choosing `t²=nu/[(52mu+120tau)s]`. That limited consequence needs only the
remainder bound here; no ground-state dispersion or polarization follows.

## 7. Evidence, prior art and remaining obligation

The new exact target is the full-carrier N=4 interference coefficient of
a specified local quantum trial, not another harmonic mode count. The
mathematical family is **(hard-core occupation words and weighted perfect
matchings; connected local square/number cancellation; quartic tensor-channel
interaction and phase anisotropy)**.

Prior-art search was targeted, not exhaustive. Main's actual native Weyl
interaction note fixes a two-orbital CAR carrier, Grassmann quartics and a
bare continuum vertex; its proof and scope were read. Its supplied model
and vertex are not the present physical-site hard-core pair model. The
native quartic Ward note is a dual-certificate problem, not pair scattering.
PR9363 remains at `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`; the actual
finite-slot tensor harmonic note, read in the earlier route and refreshed
here at its premises, explicitly excludes the nonharmonic and one-qubit-per-
site questions tested here. No theorem from that proposal is imported.
The newly landed 9d15 source refresh also includes a one-pair integer-rotor
formation band, whose actual carrier/operator definitions were read; it is
a different compensated charged-matter/rotor instrument. The just-landed
versions of PR9285 and PR9287 were compared to their previously read heads,
and their complete note diffs were inspected: conditional classical ordering
and walker collision/placement results do not supply this pair functional.
Prior native source/check reports were read fully; their closest result is
the exact N=2 band calculation, with full-carrier stability handled in the
frozen stabilizer report. Matching open heads and exact read coverage are
recorded in SOURCES.json. No general external-priority claim is made.

All jobs were priced, single-threaded and local. There was no full-torus
N=4 enumeration, dense many-body diagonalization or unmanaged worker.

| Evidence | Exact coverage | Observed resources |
| --- | --- | --- |
| `compute_quartic.py` | Complete connected coefficient matrices, 816 stars, 440 rooted cycle sets, 24 coefficientwise cubic rotations | 1.264 s; 26,099,712 bytes peak RSS |
| `check_occupation_action.py` | Actual four-site amplitudes on 6,443 residual pairs for five real/complex directions; full nineteen-site N=4 number controls | 46.173 s; 18,890,752 bytes |
| `check_local_number.py` | Central occupation Taylor coefficient on 85 actual sites; at most 7,718 central N=4 words | 0.328 s; 19,513,344 bytes |
| `check_invariants.py` | All entries of three invariant/matrix identities; exact positive LDL certificates | 0.162 s; 18,415,616 bytes |

The numerical-looking Gaussian-integer controls use only integer-valued
complex arithmetic, with explicit integrality and exact-representability
bounds. The primary matrices and positivity certificates are integer or
rational throughout. Different author calculation paths are disclosed as
author controls, not substituted for the independent checker assigned by
the parent. Deadline and STOP_REQUESTED were checked before every script.

The next attainable nonlinear question is an actual two-pair scattering
problem: construct the asymptotic collective-pair channels of the N=4
Hamiltonian, account for their nonorthogonal overlaps and virtual states,
and establish a controlled zero-energy resolvent/on-shell interaction
matrix. Equations (6)–(7) are a zero-momentum *unrelaxed trial functional*;
they are not that resolvent or scattering matrix. A scattering result is
strictly weaker than a finite-density phase theorem and may change the
channel preferences of this trial.

The ultimate missing statement remains a controlled finite-density
spectrum and observable analysis yielding two linear tensor modes with
the required source/action and actual record interpretation. Assuming that
statement would simply assume the target. Neither positivity, an O(nu)
density, a complex trial minimum, nor the cubic E plus T2 representation
establishes it. No bosonic condensate, helicity-two identification, gauge
constraint or record-readout rule has been silently introduced.

Reproduce each script with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
MKL_NUM_THREADS=1 python3 <script>`. Full outputs, source bindings and frozen
artifact hashes accompany this report in the same directory. Earlier
frozen author routes remain unchanged.
