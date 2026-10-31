# COEFF — complete coefficient records and causal AF tuning

The coefficient system and its conditional stability/tuning argument are
written through the endpoint below. The actual all-history finite-coupling
theorem is not established: G1–G4 identify its missing inputs. In particular,
the real contract's activity bound alone does not imply the marginal error
bound needed for asymptotic freedom.

One premise is stronger than the brief's older status description:
`UNIFORM_ONE_LOOP_COUPLING_ASTRA.md` supplies the reviewed, volume-first
Gaussian partial-sum bound. P6 imports that result at its exact scope. The
open list in FLOW §110 is not used to declare this newer result absent.

This is the sole author deliverable for `briefs_q/COEFF/AUTHOR.md`, dated
2026-10-30. The numbered P, D and G headings are the counted steps. A P
label imports a previously integrated, reviewed statement within this proof
push; a D label is an argument written here, without independent review;
a G label names an undischarged actual-model obligation. None grants audit
or retained status. The four gaps are coupled obligations, not four
independent impossibility results.

## Contract and source identities

**Target and domain.** Fix SU(N), N>=2, odd L>=3, kappa>0, the probability-Haar
normalized Decision-4 paired-contour kernel, and compatible finite periodic
four-dimensional lattice chains of arbitrary finite depth n. Use the
REALRGA field order six and original-source order four, including mixed
words through total order ten, complete readers and inactive roots. Constants
may depend on N,L,kappa and declared norm/domain data, never on n, volume,
cutoff or an admitted history. Cutoffs are a=ell_IR L^-n with ell_IR fixed.
Positive history fibres have their exact masses; zero fibres remain zero.

**Supplied conditions.** The Wilson/S4-prime model, its observable/source
identifications and its normalized-kernel scheme are supplied mathematical
data. They are not derived here from the framework axioms. No primitive or
physical axiom is added. The primitive registry was inspected; no approved
units, kinetic-isotropy or realized-state primitive supplies the analytic
estimates at issue here.

**Closest existing results.** LOCOP L13–L16 and FLOW §§7–9 already give the
scalar conditional bracket and shooting argument. SPURION supplies the
mixed coefficient inventory. UL4, below, supplies the newer Gaussian
bound. The missing work is their simultaneous realization with the full
real selected state and the other coefficient budgets. The new organization
here makes all coefficient maps, derivative units, summability requirements
and prefix-only tuning inputs explicit; it does not claim novelty for the
elementary shooting or variation-of-constants methods.

**Revision.** Working branch `claude/q-S4`, HEAD
`b4bcd59bea4e37d3f1a0410454d7a15a2d7772b2`. Successfully fetched
`origin/main=bcab5d2ee4a908fbb4e6025635fb878e6c157ebe` and
`origin/ai/execution=56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
The proof-push files below match HEAD but are absent at that main ref.
Thus “integrated” here means this supplied proof-push branch, not main or
audit ratification. LOCOP was integrated at `b872c85503`, SPURION at
`c53c4f5f4d`, EXTCONT at `575d228ec4`, REALRGA at `0f561ef0b2`, and the
corrected UL result at `6c152197e8`. FLOW's current session-13 snapshot and
review are available in this same branch.

| Read source | SHA256 |
|---|---|
| LOCOP.md | `0295d071a60d0ba3abfa23e4722634c7c2ea54921423cd0451aec7381e2c9253` |
| SPURION.md | `8474bec9faca8b0d9a1318846088e26cf47a06f89748236c8d440bc0ab046667` |
| EXTCONT.md | `b10015bbd6be5fac97fd636fdc79f665800fe9921651575b9d03b0167b534b6e` |
| REALRGA.md | `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` |
| FLOW.md | `085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f` |
| REVIEW_LOCOP.md | `826f585ec42dac8d55990814c9cad4ec53554389b8b81db71d3bd139cf3a7be7` |
| REVIEW_SPURION.md | `35f01a083a23d572879204c325991d58a5d18ca172576043203bb0a5960add70` |
| REVIEW_EXTCONT.md | `e202cb50bdf0db2853bb7b68a3b59e48caa3c9cdda21c6aaad76097ec96783d1` |
| REVIEW_REALRGA.md | `37f34b77fd487bc2eff8b3b624854cb636b8dd016c2e5d201a2a02a88fdac2d7` |
| REVIEW_FLOW_S1_S2.md | `313c3409453a109fc403a3d153d48cd6d9b4434b7f0c180dbf2ebef6a8c3e93b` |
| REVIEW_FLOW_S7.md | `c5e44d79579897de860eda4c1c99226a2bb205c4c4be2ffe3516ba3d3c12f829` |
| REVIEW_FLOW_S12.md | `90f810bbf340620b8ea65674b1388733bef9bd9dadb80a461fc80427c8d64307` |
| REVIEW_FLOW_S13.md | `9ebb3352f7f0cce4920125ce1700ee33ec7b50b924eada5c55b1c9af5e3b9708` |
| UNIFORM_ONE_LOOP_COUPLING_ASTRA.md | `b7baa6a711969c8fc96538009bb8f9f9acdde3f14f6d2f570a6ca5b9391516ce` |
| REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA.md | `ca80f189e924ac7d15462258d4a1e95734cfa55e45d382e7791dabdf0de2cc27` |

The four requested short notes and UL were read completely. FLOW coverage:
§§0–4, §§6–9, §52, and §§94–110, including the corrected statements and
their proofs. Reviews S12, S13 and the UL review were read completely;
S7's FP-exact review and S1/S2's remainder/flow/tuning review were read at
the consumed sections. The four short-note reviews were checked for exact
source hashes and item dispositions, not re-executed as new audits.

A statement search located UL in addition to the requested files. The
finite-u scope paragraphs of `FINITE_COUPLING_KERNEL_ASTRA.md` and
`INTERACTING_SELECTED_CORE_ASTRA.md` were also checked: they explicitly
exclude the inherited all-history finite-u flow estimate. Their narrower
positive results are not used as substitutes. The main-branch search did
not supply a matching coefficient theorem.

For method context, the primary abstract of
[Bauerschmidt–Brydges–Slade's structural-stability paper](https://arxiv.org/abs/1211.2477v3)
describes weighted sequences and mixed initial/final boundary conditions for
different RG systems. Their
[RG introduction](https://arxiv.org/abs/1907.05474v2)
primarily treats hierarchical phi-four theory. Only these abstracts were
checked in this turn. No theorem from either is imported into the present
gauge model; the elementary arguments used here are written below.

## Reviewed inputs

### P1 — PROVEN(LOCOP.md)

**Consumes:** a complete positive additive output, a source-free infinite-volume
translation/B4 bulk with absolutely summable Hessian moments, and the
normalized tree functional W with beta[W]=1.

**Exact statements used, L13–L14:**

    b_j=-beta[Gamma_j],  rho_j=-beta[R_j^other],
    u_(j+1)=u_j-b_j-rho_j,
    G_(j,h)=F_(j,h)-(u_(j+1)-u_j) W_(j+1)^tree,
    u=2N/g_std^2,  beta0=11N^2/(12 pi^2).                 (C1)

Gamma_j contains the complete Gaussian one-loop term; every other term
occurs once in R_j^other. In particular an RLF action contribution
`-delta beta_j W` contributes `+delta beta_j` to rho_j. A source derivative
does not differentiate the prescribed kernel or retune u.

The finite coefficient estimate L7 is

    sum_(r=0)^4 |D_J^r b_X|/r! <= 2 A_X^2 h^-2 H_X^T,     (C2)

with the declared source directions, affine-test size A_X and complete
weighted Taylor bound H_X^T. The scalar bulk reduction requires the full
symmetry orbit, not each selected activity. LOCOP L15–L16 are conditional
brackets, not trajectory existence. **Produces:** a defined scalar extraction,
its signs/units, and an explicit cost for extracting coefficients.

### P2 — PROVEN(SPURION.md)

**Consumes:** the exact normalized kernel, its complete readers, and the
specified invariant local domains for any projector used.

**Exact statements used, S5, S11 and S20–S21:**

    -log k_t(exp(z t_a);1)=constant+(t/2)z^2+O(z^4),
    t=kappa u_j,
    D^2 S_eff(1)[d omega,B]=0,
    Loc^mixed F=(P_4 f)(log C(U),J),
    ||P_4 f||_T<=16||f||_T,  ||(1-P_4)f||_T<=17||f||_T. (C3)

The Ward identity concerns a smooth invariant single-connection action;
locality is needed to identify a local mass coefficient. Independent
relative fields remain in the mixed chart. The kernel's fixed-fine
coarse Hessian is exactly kappa u_j. The Haar chart action has quadratic
Hessian N^2/6 in the normalized colour metric. Neither is an extra tunable
bare gluon mass. The mixed projector is a finite graph/cycle-chart
construction; its uniform group-norm conversion is not included.
**Produces:** the legal coefficient inventory and exact primitive checks.

### P3 — PROVEN(REALRGA.md)

**Consumes:** fixed original-source directions, the actual normalized
conditional chain law, and sufficient differentiated-integral bounds when
norm estimates are taken.

**Exact statements used, RGA8 and RGA19:**

    T(FH)<=T(F)T(H),
    J_(j+1),B=sum_(pi partition B)
                 kappa(J_j,C:C in pi | U_(j+1)).          (C4)

Here J_j,B is the B-labelled derivative at zero of the conditional log
generating function. This includes singleton means and outer cumulants.
All 15 nonempty subsets of four labels are retained, with no 4! in the
distinct-label coefficient. **Produces:** the exact source recursion and
finite real calculus. RGA14–RGA16 for the actual mixed state remain inputs.

### P4 — PROVEN(FLOW.md)

**Consumes:** §52's critical Gaussian background; injective orbit map
Gamma, Q Gamma=0, positivity on its gauge quotient S, h onto, and chi Gamma
invertible, with chi=(h,chi_2). Write Delta'=Gamma*Gamma and H=ker h.

**Exact statement used (FP-exact, also LOCOP's FP display):**

    Delta_FP=|det(chi Gamma)| det(hh*)^(-1/2),
    (1/2)log det_H(Q+chi_2*chi_2)-log Delta_FP
                =(1/2)log det_S Q-(1/2)log det Delta'.    (C5)

REVIEW_FLOW_S7 §2 confirms this with the composite-slice admissibility
and positivity assumptions. Delta_FP is not the inverse normalization
of the orthogonal-slice integral. **Produces:** the correct Gaussian
coefficient bookkeeping, not a nonlinear all-history gauge fixing.

### P5 — PROVEN(FLOW.md)

**Consumes:** §94(W3)'s common determinant spaces, zero-mode removals and
invertibility, with criticality for its total determinant identity. At a
defined differentiable covariant block map use
`T_k D_k=D_(k+1) ev` and `P_k D_k=0`.

**Exact statements used, T-tel and SLICE-U:**

    total_n=(1/2)sum_(k<n) Phi_k^T+G_(gh,n),
    Phi_k^T=log det_perp Ytilde_(k+1)-log det_perp Ytilde_k,
    A^(n<-j)=Q^(n<-j)-D_n h^(n<-j),
    P_n A^(n<-j)=P_n Q^(n<-j),
    P_n A Pi^-1 A* P_n=P_n Q Pi^-1 Q* P_n.              (C6)

All projectors and gradients in the last line are at the current U.
The first line has no omitted longitudinal level remainder. The slice
algebra holds at any U satisfying the stated covariance; its analytic
norm estimates in §§106–107 have the narrower Cartan-plane-wave scope.

The chain Cartan derivative in §103(X3) is

    T(U)phi=avg_T(N_T xi_T(phi))/avg_T(Nbar_T),
    N_T=e^(i psi_i(T))+e^(-i psi_j(T)),
    Nbar_T=e^(-i psi_i(T))+e^(i psi_j(T)),
    psi_k(T)=h_k theta_T-phi_k.                         (C7)

The xi_T are the transported line sums of §103, not bare contour sums;
phi_k are the SU(N) maximizing phases. Carry S13-8's reviewed correction:
with r_k=e^(-i phi_k)m_k, stationarity under sum phi_k=0 gives equal
Im r_k. Therefore avg N-avg Nbar=2i(Im r_i-Im r_j)=0. This is the missing
step in the stored §105(c) proof for N>=3. It is stated here as part of
the reviewed import, without editing FLOW.

Cartan-m gives the chain background through order two, with no quadratic
part; its plane-wave amplitude ratio is

    rho_i(P)=sin(P L^-i/2)/sin(P/2),
    |rho_i(P)|<=(pi/2)L^-i,  0<|P|<=pi.                (C8)

For the log-averaged map the form factor is exact on the appropriate
small branch. We use only the branch near the identity, never infer a
global unwrapped line-sum logarithm from closeness of a holonomy to one.
For the actual maximizing chain the form factor is only second-order exact.

VC-T1 supplies the C-part, orders <=2, given Pi-loc; its heavy normalized
momentum estimate is not an unweighted full-norm estimate. S13 records the
M-part and constant-flux exchange as open on that route. The withdrawn
first-order lower-decay assertion is not consumed. **Produces:** the exact
cancellations to perform before estimating Gamma. P6 supplies the newer
Gaussian bound by its own reviewed route; C6–C8 alone do not supply it.

### P6 — PROVEN(UNIFORM_ONE_LOOP_COUPLING_ASTRA.md)

**Consumes:** UL1's normalized stationary tree phase with the actual paired
S4-prime mean, fixed kappa at every level, and UL's named US/CJ/BC/full-colour
residual contracts. Their quantitative hypotheses remain attached to the
import. It is a Gaussian Taylor theorem, defined volume first at each fixed
depth, then infrared limit, then a bound uniform in depth.

**Exact statement used, UL4 and UL31:**

    |a_n-a_0|<=C_FP,
    B_n-B_j=beta0 (n-j)log L+a_n-a_j,
    |B_n-B_j-beta0(n-j)log L|<=2 C_FP,
    B_n=sum_(k<n)b_k,  B_0=0.                          (C9)

The final corrected source hash matches the review's final hash. Its
fixed-free-complement correction UL13a is present; no finite-volume
determinant invariance is inferred merely from det M=1. Neither the
Gaussian coefficient nor C_FP is numerically fitted. **Produces:**

    b_*=beta0 log L>0,  R0=C_FP,  R=2 C_FP,
    d_j=B_j-j b_*,  |d_j|<=R0.                        (C10)

This resolves LOCOP LC4's Gaussian partial-sum sub-obligation at the
supplied-model, volume-first scope. It does not prove finite-u SF-g,
selected-history estimates, finite-torus marginal convergence rates, or
causal tuning. Convergence of b_j is unnecessary and not inferred.
In C1 and C15, choose Gamma_j to be this tree-reference Gaussian
increment. Differences between that reference and the actual inherited
coefficient state or prefix weights belong to R_j^other. The bound C9
does not automatically apply to a different Gaussian reference.

### P7 — PROVEN(EXTCONT.md)

**Consumes:** the complete MS/SEL/HOLE/EXT hypotheses in the SAME full rooted
real norm, a regenerated support reserve mu+2, and the separate COEFF
condition. The scalar continuation statement E18–E19 is exactly

    x_(j+1)<= (lambda+B s_j+eta_j)x_j+C_K x_j^2+B e_j^new,
    theta=lambda+B s_*+eta_*+C_K M<1,
    B e_*^new <=(1-theta)M,  x_0<=M.                  (C11)

**Produces:** x_j<=M by induction, once those inputs hold. C11 controls
the irrelevant activity; it does not itself control projected coefficients,
vacuum/source prefactors or coefficient derivatives with respect to u.
Only the finite q=4 contract is imported, not the all-order H6 modules.

## Complete coefficient system

### D1 — DRAFTED(high): an exact system once the additive representation exists

**Most likely failure point:** applying this finite/chart algebra to an
actual history not covered by G1. **Consumes:** P1–P3 and a supplied positive
supported additive representation with its full reader labels. **Produces:**
the complete coefficient maps C12–C17, not estimates on those maps.

Use a fixed ownership convention. A supported single-field container gets
LOCOP's full curvature tensor projector. An eligible independent mixed
graph gets SPURION's tree-labelled degree-four projector instead; do not
apply both to the same activity. Reconstruct in exactly the same chart.
Constants and the common bulk scalar are assigned once. An original source
reader never becomes an empty-support constant merely because its field
degree is zero. Genuine unlocalized prefactors are separately recorded.

On the represented part of a history state write the action as

    S_(j,h)(.;J)=u_j W_j^tree+e_j N_j+zeta_(j,h)(J)
        +sum_X [z_(j,h,X)(J)
                 +sum_(alpha in I_(j,h,X)) c_(j,h,X,alpha)(J) O_alpha]
        +sum_X K_(j,h,X)(.;J).                         (C12)

N_j is the number of level-j sites; e_j is the common source-free bulk
vacuum density. zeta is any separately recorded global prefactor action,
including a history mass if that convention puts it there; it need not
vanish at J=0. z_X are supported field-independent coefficient functions.
Every source-independent and source-dependent tensor left after the common
bulk extraction is in c. On the single-field sector I contains the full
symmetric six-plane curvature tensor before bulk reduction. On a mixed
cycle chart it contains every surviving monomial of degrees one through
four. Linear, cubic, anisotropic, exterior, boundary and winding labels
are not removed by homogeneous bulk arguments. Non-chart sectors remain
in the original exact state and require a separate representation.

This is generally a growing direct sum of coefficient spaces, not four
real running constants. For example the relative quadratic block is

    (1/2)sum_(a mu,b nu) M_(a mu,b nu)(J)
                                  <r_mu^a,r_nu^b>.       (C13)

Its finite homogeneous no-extra-spurion count is (4q)(4q+1)/2 for q
relative one-forms, reduced to q(q+1)/2 only for a complete B4 bulk.
Actual source/history/position labels are additional. SPURION's graph
container instead has at most binom(d+4,4) coefficient functions with
d=(N^2-1)(E-V+c); it supplies no uniform bound on d.

Define the exact step by its original density, schematically

    R_(j+1,h')(V;J)=sum_(h -> h') int
          rho_(j,h)(U;J) K_j(V,U) I_(h'|h)(U,V) dU.       (C14)

Any separately represented complementary contribution is included in this
sum before its logarithm. Partial eliminations leave all their remaining
readers as arguments. Pull the common factor exp(-e_j N_j) outside and
take the real logarithm only on positive fibres. Let F_j be the complete
non-tree output after that factor is removed. With a fixed linear
coefficient extractor E and reconstruction i satisfying E i=1 on the
chosen range, the full recursion is

    u_(j+1)=u_j-b_j-rho_j,
    e_(j+1)=L^4 e_j+alpha_j,
    (zeta_(j+1),z_(j+1),c_(j+1))
       =E_(j+1)[F_j+(b_j+rho_j)W_(j+1)^tree-alpha_j N_(j+1)],
    K_(j+1)=(1-i_(j+1)E_(j+1))
       [F_j+(b_j+rho_j)W_(j+1)^tree-alpha_j N_(j+1)].     (C15)

alpha_j is the specified common bulk vacuum projection of F_j. E includes
the disjoint global/supported scalar convention of C12. The bulk beta
in the first line is taken after the necessary mixed fields have actually
been eliminated, at J=0. It is not a beta test on a partially frozen
joint kernel. Finite-volume and selected-history differences remain in
the other lines. Exact reconstruction proves C15 by substitution into
C12, with no discarded action or adjusted bare term.

For clarity, source normalization is a whole block of this system. Put
Phi_j=log E[exp(sum_i J_i O_i^original)|retained level-j state] using the
unperturbed chain. At a transfer,

    Phi_(j+1)=log E_(nu_j)[exp(Phi_j)],
    partial_B Phi_(j+1)|_0
        =sum_(pi partition B) kappa_(nu_j)(J_j,C:C in pi). (C16)

For |B|=2 this is E J_j,12+Cov(J_j,1,J_j,2). For |B|=3 it is the
conditional mean of J_j,123, the three covariances between a pair jet and
the remaining singleton, and the third cumulant of the singleton jets.
For |B|=4 it contains E J_j,1234, four (3,1) covariances, three (2,2)
covariances, six (2,1,1) third cumulants and one fourth cumulant. These
formulas follow by expanding exp and log in commuting nilpotent source
labels; their coefficient identity is exact through the specified jets.
History sums with their masses and the final outer expectation are also
subject to C16. The action source coefficients have the opposite sign to
Phi. In a fixed linear local observable basis, the singleton coefficients
form a normalization/mixing matrix Z_j; higher source jets and source
vacua are separate records, not powers of Z_j.

Initially J_0,{i}=O_i^original, with all higher distinct-label jets zero
for the specified linear tilt. C12 still carries the full C^4 coefficient
functions in J; a fourth-order Taylor polynomial is not substituted for
those functions on a finite source interval. No scalar multiplicative
Z recursion follows unless the actual map preserves the chosen observable
subspace and its mixing has been computed.

To expose the stability data, subtract a declared, exactly compensated
reference vector c_j^ref(u_0,...,u_j). For the remaining coefficient
vector v_j, including all source records, write the exact projected map as

    v_(j+1)=A_j v_j+f_j+r_j(v_j,K_j).                    (C17)

Here f_j is the projected reference output minus the next reference;
A_j is the specified linearization in the coefficient state if it exists;
r_j is the exact remaining difference. Defining this difference proves
the identity, not a smallness estimate. A_j is not presumed to be a
diagonal engineering-dimension matrix. Its computation and its domain
are part of G3. The only physical shooting parameter below is u_0.

### G1 — GAP: all-history realization of C12–C17

**Consumes:** the actual inherited rho, normalized references, all selected
and complementary sectors. **Needed output:** an exact supported additive
representation on a specified stable real domain, uniform group/chart
conversions through (6,4), complete original readers and bounded extractors
on the full rooted sums. Empty or zero fibres must not be logged.

The precise missing transition includes

    Q_(j,4)=sup_x sum_(i:x in H_i) exp[(mu+2)|H_i|]alpha_i <=1/4,
    ||E_(j+1)F||_coeff <= C_E ||F||_(mu,6,4),            (C18)

with the actual matched integrated jets and the explicitly chosen
coefficient units. A finite tree projector proves neither inequality.
Hard moving selectors also require the differentiated boundary/transport
terms of EXTCONT SEL. The existing conditional algebra is not a producer
of these bounds. Continue below conditional on this representation.

## Remainder strength, AF estimates and the other budgets

### D2 — DRAFTED(high): the derivative units required by the AF error

**Most likely failure point:** an unrecorded support or chart conversion in
the actual producer. **Consumes:** P1's coefficient test and an actual bound
on the complete non-Gaussian output. **Produces:** a sufficient real
remainder inequality and its causal weight conversion.

At step j, before defining u_(j+1), measure the newly output field in
the provisional units h_pre=sqrt(N/u_j). Earlier retained fields keep
their already known weights. This avoids defining a bound in terms of
the as-yet unknown output coupling. On eligible single-field bulk
containers let H_X^T be the provisional Taylor bound on R_j^other and set
H_j^mom=sum_X A_X^2 H_X^T, with the translation-family convention of LOCOP.
Then C2 and absolute summation give

    |rho_j|<= (2u_j/N) H_j^mom.
    H_j^mom <= N C_rho/(2u_j^2)
                  implies |rho_j|<=C_rho/u_j.           (C19)

Alternatively supply the unweighted Hessian moment directly:

    sum_z |z_1 z_2| |Pi^(R_j^other)_12(z)|<=C_rho/u_j.  (C20)

REALRGA §6/EXTCONT E8 is another sufficient certificate: an unweighted
entry bound H exp(-kappa_p d(X)), with H<=C_H/u_j and kappa_p>log 6400,
gives C_rho=64 M_block^6 C_H sum_(m>=1)m^3(6400 e^-kappa_p)^(m-1).
Its graph/coordinate conversion remains attached. None of these bounds
can omit inherited fluctuations, normalizers, Haar/FP/reference terms,
returned terms or complementary sectors from R_j^other.

The power loss is real. On |z|<=h, with derivative weight h, f(z)=z^2 has
T(f)=sup_(|z|<=h)(z^2+2h|z|+h^2)=4h^2=4N/u, while its quadratic
coefficient is one. This elementary jet example diagnoses the inference,
not a gauge-model mass. In C19, a bound H_j^mom<=C_H/u_j gives only
|rho_j|<=2 C_H/N. The desired inequality

    2 C_H/N <= C_rho/u_j                                (C21)

fails as a sufficient uniform bound for arbitrarily large u_j with fixed
positive C_H,C_rho. It does not prove that the actual rho_j violates C20.

Once u_(j+1)>=u_min and the bracket of D3 holds, set
D=b_*+R+C_rho/u_min. Then |u_(j+1)-u_j|<=D, and changing just the output
weight to h_(j+1)=sqrt(N/u_(j+1)) costs at most

    max(1,(h_(j+1)/h_pre)^6)
       <= (1+D/u_min)^3                                (C22)

in the full Taylor sum. The inverse conversion has the same bound.
Pay C22 in the actual step constants once. Products of bare weight ratios
are endpoint ratios, e.g. product_(j=m)^(n-1) h_j/h_(j+1)=h_m/h_n;
a fixed per-step comparison constant raised to n is not a uniform proof.

### G2 — GAP: the interacting marginal estimate

**Needed output:** C20, or a stronger proved certificate such as C19, for
the complete causal finite-u output, uniformly in the declared state class.
Its input may use only the chain's prefix through j. This is the residual
finite-u part of LC4, not the Gaussian part supplied by P6.

The real contract bounds weighted activities; it does not include an
evaluated C19/C20 for this output. The newer single-kernel finite-u result
does not bound the connected interacting log, and the selected-core result
explicitly excludes inherited actions, sources and hard complements.
Thus those estimates cannot be relabelled as this bound. C21 identifies
the precise insufficient inequality of the obvious weighted-norm shortcut.
All following steps assume a finite C_rho with C20; no value is invented.

### D3 — DRAFTED(high): stable AF coordinate and summability along every prefix

**Most likely failure point:** applying a prefix bound before G2 has supplied
its per-level estimate. **Consumes:** C1, C9, C20, and an admitted prefix
u_j>=u_min with C_rho/u_min<=b_*/2. **Produces:** C23–C26.

Define b_-=b_*-C_rho/u_min, b_+=b_*+C_rho/u_min and w_j=u_j+d_j,
where d_j is C10. Since b_j=b_*+d_(j+1)-d_j,

    w_(j+1)=w_j-b_*-rho_j,
    b_-<=w_j-w_(j+1)<=b_+,
    b_-(k-j)-R<=u_j-u_k<=b_+(k-j)+R.                 (C23)

This proves monotonicity of the corrected coordinate w, not of u itself.
It uses the actual b_j, not a replacement b_j=b_* at each step.
Set U=u_k and v=U-R>0. For j<k, C23 gives
u_j>=v+b_-(k-j). Integrating a decreasing function over consecutive unit
intervals proves

    sum_(j<k) u_j^-1 <= b_-^-1 log(1+b_- k/v),
    sum_(j<k) u_j^-p <= v^(1-p)/[(p-1)b_-],  p>1.     (C24)

The second bound also follows by integrating over [0,infinity), so it
is independent of k. These sums exclude the terminal index; including it
adds U^-p. In particular

    |u_j-U-(k-j)b_*|
        <=R+(C_rho/b_-)log(1+b_-(k-j)/(U-R)).          (C25)

For estimates used before the final scale is selected, choose u_min>R
and apply C24 to the current prefix endpoint u_k>=u_min. With the fixed
lower slope a_-=b_*/2 this yields the causal bound

    S_p^*= (u_min-R)^(1-p)/[(p-1)a_-],
    sum_(j<k)u_j^-p<=S_p^*,  p>1.                    (C26)

No final target or future coupling occurs in C26. An O(1/u) marginal
forcing is generally not summable uniformly in depth; C24 gives logarithmic
growth. This distinction determines the source/coefficient budgets below.

### D4 — DRAFTED(high): vacuum and source-scalar growth budgets

**Most likely failure point:** a producer omitting a source-dependent
normalizer from alpha,z or zeta. **Consumes:** C15 and bounds on the actual
projected increments. **Produces:** an exact vacuum solution and sufficient
scalar growth bounds, without asserting the needed increment estimates.

Because N_j=L^4 N_(j+1), the common scalar factor gives exactly

    e_k=L^(4k)e_0+sum_(j<k)L^(4(k-1-j))alpha_j,
    L^(-4k)e_k=e_0+sum_(j<k)L^(-4(j+1))alpha_j.        (C27)

For any causal upper envelope |alpha_j|<=A_j, the absolute-value version
of C27 is the permitted budget. For example, IF
|alpha_j|<=A_v[1+log(1+u_j)], then C23 with j=0 implies u_j<=u_0+R and

    |L^(-4k)e_k|<=|e_0|
       +A_v[1+log(1+u_0+R)]/(L^4-1).                (C28)

The logarithmic bare-coupling dependence in this example is explicit;
it is not a cutoff-independent bound on the raw vacuum density. Vacuum
growth is allowed and tracked. A field-independent source-free factor
cancels in normalized expectations but remains in the exact partition
function. Its J-dependent counterpart contributes to derivatives and
cannot be removed for H6.

A genuinely common source scalar zeta_j(J), factored before a single
conditional transfer, obeys zeta_(j+1)=zeta_j+delta zeta_j, hence
||zeta_k||_(C_J^4)<=||zeta_0||+sum_(j<k)||delta zeta_j||.
For different parent history scalars C14 must first sum their weighted
densities; there is no unweighted additive recursion across that sum.
Supported source-scalar terms retain their rooted coefficient norm and
use C17/C29 below. A uniform scalar budget requires a summable increment,
or an explicitly allowed growth/subtraction with its derivatives retained.

### D5 — DRAFTED(high): projected coefficient and source-normalization stability

**Most likely failure point:** the actual projected transfer may have a
relevant or nonsummable component that does not satisfy the stated bound.
**Consumes:** C17 and independently supplied estimates on A_j,f_j,r_j in
the full coefficient spaces. **Produces:** exact sufficient stability tests,
including the required treatment of large relative and marginal terms.

Use diagonal coordinate weights W_j to convert stored monomial coefficients
to their declared dimensionless units. A degree-r monomial with retained
levels l_1,...,l_r has weight product_s h_(l_s); source-jet weights are
the original ones. Full norms additionally sum complete supports, tensor
entries and labels. Write vhat_j=W_j v_j and
Ahat_j=W_(j+1) A_j W_j^-1, with the corresponding fhat,rhat. Then a
sufficient invariant-ball condition is precisely

    ||Ahat_j|| V_*+||fhat_j||
       +sup_(||vhat||<=V_*, ||K||<=M)||rhat_j(v,K)||<=V_*.
                                                               (C29)

Triangle inequality and induction prove the assertion. All species,
including supported source vacua, enter the same norm or separately
declared compatible balls. If ||Ahat_j||<=lambda_v<1 and the two forcing
terms sum to at most F_v, it suffices that F_v<=(1-lambda_v)V_*.
Engineering dimensions alone do not prove lambda_v<1.

For a neutral sector use a more flexible criterion. Define
Phi(k,i)=Ahat_(k-1)...Ahat_i, Phi(i,i)=1. Repeated substitution gives

    vhat_k=Phi(k,0)vhat_0
       +sum_(j<k)Phi(k,j+1)[fhat_j+rhat_j].             (C30)

Thus the exact sufficient budget is the norm majorant of this display
<=V_k for every admitted prefix. In particular, suppose on the full ball

    ||Ahat_j||<=1+A/u_j^p,
    ||fhat_j||+||rhat_j||<=F/u_j^p,  p>1.             (C31)

C26 and 1+x<=exp x imply

    ||vhat_k||<=exp(A S_p^*)[||vhat_0||+F S_p^*].      (C32)

Choose V_*>||vhat_0|| and require the right side <=V_* before induction.
The estimates C31 need hold only on that chosen ball: induction then makes
C32 legitimate. If A,F depend on V_*, their dependence stays inside this
inequality; it is not solved by naming V_* “large enough.”

The known kernel coefficient illustrates why units matter. On its
fixed-fine joint sector P2 gives M_block=kappa u_j exactly, so

    h_(j+1)^2 M_block=kappa N u_j/u_(j+1)
                       <=kappa N(1+D/u_min).            (C33)

The raw requirement kappa u_j<=M_* for a cutoff-independent M_* fails
on the tuned ultraviolet family, since C23 gives u_0>=U+b_- n-R.
This is a failure of that proposed budget for the known primitive term,
not a claim about the completely integrated physical Hessian. Its
dimensionless coefficient is bounded by C33. The Haar quadratic similarly
has weighted Hessian N^3/(6u_j). Preserve the prescribed reference/blocking
terms and compensate any reallocation exactly. For an absorbed Gaussian
correction take Q_ref positive and Delta Q self-adjoint on the admissible
slice. A separate sufficient precision condition is

    ||Q_ref^-1/2 Delta Q Q_ref^-1/2||<=eta_Q<1.          (C34)

Then (1-eta_Q)Q_ref<=Q_ref+Delta Q<=(1+eta_Q)Q_ref on the admissible
slice. The determinant and all source derivatives are still recorded.
The source files do not establish C34 for arbitrary returned relative
coefficients. Symmetry removes a local physical single-field mass; it
does not supply C29, C31 or C34 for the relative sector.

For a real scalar source-normalization subblock, IF its computed
recursion is z_(j+1)=(1+gamma/u_j)z_j+r_j^z, define

    P_0=1,  P_(j+1)=(1+gamma/u_j)P_j,
    z_k/P_k=z_0+sum_(j<k)r_j^z/P_(j+1).              (C35)

Assume |gamma|/u_min<=1/2. Each factor is positive and

    |log P_k-gamma sum_(j<k)u_j^-1|
                           <=gamma^2 S_2^*.            (C36)

This follows by summing |log(1+x)-x|<=x^2 for |x|<=1/2. A bound
|r_j^z/P_(j+1)|<=F_z/u_j^p, p>1, therefore keeps z_k/P_k bounded.
It does not keep P_k itself bounded: its logarithmic accumulation can
be the expected source renormalization. No gamma is assigned to this
model without computing the actual mixing. For matrix mixing use C30;
scalar integrating factors cannot be imposed on noncommuting matrices.
These bookkeeping normalizations never retune the original source in C16.

### G3 — GAP: actual coefficient, reference and prefactor budgets

**Needed output:** the actual A_j,f_j,r_j and alpha_j, or direct bounds on
their full projections, satisfying C29 or C30, the chosen C27 scalar
envelope, and C34 wherever a Gaussian reference is changed. Their field
and all original-source jets and full history-labelled rooted sums are
part of the demand. A bound uniform for one history does not bound a sum
over all history suprema.

For a neutral block the uncomputed inequality is

    sup_k [||Phi(k,0)|| ||vhat_0||
       +sum_(j<k)||Phi(k,j+1)|| (||fhat_j||+||rhat_j||)]<=V_*.
                                                               (C37)

If only O(1/u_j) same-sign forcing is supplied with Ahat_j=1, its sum
can grow logarithmically. For the admissible comparison sequence
u_j=U+b_*(n-j), rho_j=0, b_j=b_* and forcing c/u_j with c>0,

    sum_(j<n)c/u_j >= (c/b_*) log[(U+b_*(n+1))/(U+b_*)].

The inequality integrates the decreasing function c/(U+b_*t) over
[1,n+1]; its right side diverges at fixed U. This is a counterexample
to deriving C37 from those bounds alone, not a claim that this forcing
occurs in the gauge model. One needs cancellation, a summable error after
a computed leading normalization, a contracting propagator, or a
permitted growth budget. A relevant expanding block instead needs its
actual slaving or reference argument; its recorded coefficients are not independently
adjustable bare parameters. C33 handles a specified primitive, not the
entire inherited relative matrix. None of these missing inequalities has
been numerically evaluated here. Continue conditional on their satisfaction.

## Causal tuning and the endpoint

### D6 — DRAFTED(medium): a deterministic bare-coupling selector without monotonicity

**Most likely failure point:** extending the actual represented state
continuously to the boundary of its admissible bare-parameter interval.
**Consumes:** P6, G1–G3 as hypotheses, and the following prefix-extension
condition, denoted CT. **Produces:** a bare-coupling selector for every n
and target U in C39, with constants independent of n and volume.

**CT, stated exactly.** For every finite prefix in the proposed closed
coefficient/activity sets with u_0,...,u_j>=u_min, the actual next output
and raw scalar update are defined, finite and continuous in the bare
parameter. They use only this prefix. Whenever the raw next coupling is
>=u_min, all the other sets and fixed positive domain margins are
reproduced. There is no additional stopping boundary inside the coupling
region. These assertions hold on the boundary, with the local extensions
needed to compose finitely many continuous steps. The initial state is
the prescribed Wilson/source state for each u_0>=u_min and belongs to
these sets with the same constants, uniformly in volume. In particular
G2's marginal estimate is valid for the step from an admissible prefix,
before knowing whether its next coupling exceeds the threshold.

CT is an analytic input, not the definition of “admissible.” The actual
domains/sets must first be specified geometrically and analytically.
Let C_rho and all state constants be obtained under a fixed lower prefix
slope a_-=b_*/2 and defect R, before choosing a target. Choose

    u_min>=u_adm,
    u_min>R,
    C_rho/u_min<=b_*/2.                                (C38)

u_adm is the supplied lower coupling threshold for those same fixed
estimates. Increase u_min only by restriction of that established class;
do not recompute an uncontrolled C_rho(u_min) and assume C38 solves itself.
All C11/C29/C30 margins must hold at this same choice. Fix

    U>=u_min+R,
    g_std,target=sqrt(2N/U),
    b_+=b_*+C_rho/u_min.                              (C39)

For a trial s=u_0>=u_min iterate the actual system until the first raw
coupling below u_min, if any. The estimates use no final target. Let
A_n be the s for which all n steps remain above threshold with their
complete states. CT and induction imply

    [u_min+b_+ n+R, infinity) subset A_n,               (C40)

because C23 on the next prefix gives u_k>=s-b_+ k-R>=u_min.
That bracket needs only earlier admissible inputs, so C40 is not circular.

Define the lower endpoint of this tail component by

    s_sharp=inf{s>=u_min : [s,infinity) subset A_n}.    (C41)

Every s>s_sharp is in A_n. For s decreasing to s_sharp, CT inductively
defines each boundary state and gives u_k(s_sharp)>=u_min. Hence
s_sharp belongs to A_n. If s_sharp>u_min and all its u_k were strictly
above u_min, continuity of the finitely many steps, CT's reproduced
noncoupling sets and fixed margins would extend A_n to a neighborhood
below s_sharp, a contradiction. Thus some k_star<=n has
u_(k_star)(s_sharp)=u_min; if s_sharp=u_min take k_star=0.

Apply C23 from k_star to n along this admitted boundary trajectory:

    u_n(s_sharp)<=u_min-b_-(n-k_star)+R<=u_min+R<=U.    (C42)

Put S_hi=U+b_+ n+R. C40 makes [s_sharp,S_hi] admissible and C23 gives
u_n(S_hi)>=U. The continuous terminal map on this compact interval
therefore has a nonempty closed U-level set. Define, unambiguously,

    u_0(n,U)=min{s in [s_sharp,S_hi] : u_n(s)=U},
    g_0,std(a;g_std,target)=sqrt(2N/u_0(n,U)).           (C43)

For n=0 simply take u_0=U. C43 is a mathematical construction via a
specified extremal root, not a numerical root or a uniqueness theorem.
No uniform modulus of continuity or computational stopping time is
claimed. In FLOW's older lattice units g_0,lat=u_0^-1/2 instead.

The selected path obeys, for every 0<=j<=n,

    U+b_-(n-j)-R<=u_j<=U+b_+(n-j)+R,
    |u_0-U-n b_*|
       <=R+(C_rho/b_-)log(1+b_- n/(U-R)).             (C44)

In particular g_0,std tends to zero with the cutoff along this sequence
and u_0=n b_*+O(log(1+n)) for fixed U. The target enters only the outer
choice C43. Each kernel and extraction at j is determined by its own
prefix, as required by FI-1. This is the real full-state version of the
already reviewed FLOW shooting mechanism, with its extension hypothesis
exposed rather than assumed from the AF bracket.

**Volume clause.** If the bulk coefficient maps and initial bulk state are
common to every compatible torus, and all wrapping/finite-volume differences
stay in the bounded nonbulk state, then A_n and u_n(s) in C41–C43 are
those common bulk maps. The same u_0(n,U) serves every volume. This is an
additional hypothesis, not a consequence of C9. The tuned coarse coupling
is FLOW/LOCOP's bulk coupling; no exact equality of finite-torus raw
susceptibilities to U is asserted.
Here “common” requires that evaluating the bulk trajectory at a given
bare parameter gives the same result for every torus. Sharing a formula
whose nonbulk inputs still vary with the torus would not suffice.

### G4 — GAP: prefix extension and the finite-u common bulk map

**Needed output:** CT and the volume clause of D6 for the actual state.
In particular, one needs continuous parameter-dependent bulk Hessian
limits, closure of the represented state at the shooting boundary, fixed
margins for every necessary domain, and all transition estimates from
prefix [0,j] alone. These are LC5/FI-1 plus the finite-u SF-cont/SF-infinity
content. Gaussian volume-first coefficients from P6 do not establish them.

A finite unselected Haar integral can be smooth in u while a chosen local
log representation, a moving selected sector, or its infinite-volume
Hessian limit lacks the required uniformity. Positivity is not this
extension theorem. A statement proved only under the future condition
u_n=U cannot be inserted into C40. That would assume the trajectory the
shooting argument is supposed to construct.

No bound on d u_n/d u_0 or uniqueness is needed above. The optional scalar
product formula in REALRGA applies only when the shift is actually a
scalar function of u_j with its stated derivative bound. Here rho_j can
depend on the entire coefficient/activity state; differentiating C17
introduces the corresponding derivatives. Ignoring them would not prove
continuity or monotonicity of the full map.

### D7 — DRAFTED(medium): conditional end-to-end closure and consistent windows

**Most likely failure point:** a producer satisfying the separate estimates
on incompatible domains or with constants depending on a future target.
**Consumes:** the P inputs, G1–G4 as explicit hypotheses, and all windows
below simultaneously. **Produces:** the finite-q coefficient/AF part of
EXTCONT COEFF/E19 and the tuned family C43–C44, conditionally.

| Interface | Required window on the same state class | Consumer |
|---|---|---|
| Gaussian bulk | b_*=beta0 log L, R=2 C_FP, P6's named input contracts | C23 and C38 |
| Finite-u marginal | C20 on each prefix; finite C_rho fixed first | C19, C23, C40 |
| Coupling/domain | u_min>=u_adm, u_min>R, C_rho/u_min<=b_*/2 | C22, C26, D6 |
| Source factor, if used | abs(gamma)/u_min<=1/2 and the normalized C35 forcing sum finite | C35–C36 |
| Irrelevant return | t0=lambda+B s_*+eta_*<1; C_K M<1-t0; B e_*^new<=(1-t0-C_K M)M; x_0<=M | C11 |
| Projected coefficients | C29 or C30 with the chosen budgets; e.g. C32<=V_* | C15, CT |
| Reference absorption, if used | eta_Q<1 in C34, plus retained determinant/source costs | Gaussian/regulator domains |
| Locality and holes | full (6,4) SEL/HOLE/EXT; regenerated mu+2; C18 | C11 and the next C20 |
| Volume and continuity | CT and common bulk maps; finite-size terms kept separately | C41–C43 |
| Vacuum/source prefactors | the actual C27 envelope and supported/global source budgets | H0 and H6 |

The scalar windows are compatible for abstract constants with t0<1 and
suitable initial bounds; no actual YM tuple is certified at any L.
For example, for already fixed finite C_rho,R,u_adm, a sufficiently
large u_min solves C38; if A,F are already bounded independently of that
restriction, S_p^* tends to zero and C32 fits any fixed V_*>||vhat_0||.
For the shooting family, this last comparison uses the supremum of the
initial weighted coefficient norm over all admitted bare parameters and
volumes; a bound for one chosen initial state does not suffice.
For C11 with C_K>0 the available M must solve

    C_K M^2-(1-t0)M+B e_*^new<=0,
    0<M<(1-t0)/C_K,  M>=x_0.                          (C45)

Thus (1-t0)^2>=4 C_K B e_*^new and an intersection with this interval
are required. If C_K=0, the test is B e_*^new<=(1-t0)M. Merely taking
u_min large cannot force t0<1 or manufacture the missing representation.
In particular LOCOP's general ideal gain 4/L+8/L^2 is >1 at L=3,5;
it is not a certified return contraction there. Even at larger L its
conversion, selected-return, hole and nonlinear costs must satisfy C11.

**Proof of the conditional endpoint.** Start with the specified bare
state in all chosen sets. C14–C15 preserve its exact density and coefficient
records. On every admitted prefix G2 and P6 give C23. If the next coupling
is above threshold, G1 and the supplied SEL/HOLE/MS estimates give the
supported real log and regenerated reserve. C11 gives the next irrelevant
ball. D4–D5 and the coefficient windows give the scalar and projected
budgets, including every source jet. CT gives the common margins and
continuous finite-prefix composition. This proves simultaneous continuation
until a coupling exit, without presuming the final target. D6 then selects
a trajectory with no exit and exactly u_n=U. Its volume clause makes the
choice common to all compatible tori. C44 gives uniform constants and
the stated AF asymptotics. No further induction conclusion is hidden in
this last paragraph.

This closes the implication. G1–G4 are not established by it, so actual
EXTCONT COEFF/E19, a full continuum limit, all-order source bounds and a
mass gap are not conclusions of this deliverable. The next decisive work
is the complete projected finite-u return with its real Hessian moment
C20 and all source/relative coefficient costs, followed by CT on that
same invariant class. Reopen a shortcut only when it supplies those
missing estimates or a proved compatible alternative, not another
finite-dimensional projector or a re-run of Gaussian identities.

## Author check and recovery checkpoint

The argument reaches C43–C45 before this check. Checks are of this author
packet and do not change D labels into independently reviewed results.

- Signs: action extraction uses rho=-beta[R^other]; the RLF term has the
  sign in C1. w=u+d gives exactly w'=w-b_*-rho.
- Units: u=2N/g_std^2; source directions keep kernels fixed. Provisional
  h_pre avoids use of an undefined future coupling, and C22 pays the
  subsequent sixth-order weight conversion.
- Normalization: FP/Gram factors, the SU(N) maximizing phase and the
  current-background projectors remain in the Gaussian imports. The UL
  correction and its exact reviewed hash are used.
- Endpoints: C24 sums only j<k; R is retained twice where needed; n=0,
  R=0, C_rho=0, and C_K=0 are covered. CT explicitly covers the closed
  shooting boundary and cannot be replaced by positivity alone.
- Counterterm scope: the coefficient index set can grow; source vacua,
  higher labelled cumulants and exact history masses remain. C33 is a
  primitive joint-sector check, not an integrated physical mass.
- Verification limits: no numerical simulation, historical runner replay,
  fresh independent review, commit, PR or audit was performed. Only
  `COEFF.md` is authored; no editable prompt file is changed.
- Mechanical checks: all 15 tabulated source hashes and the brief's
  SHA256 `8bc10c436bac15ed5ba29f4457a9224990a64e37d3273df2e625eb246d33f95b`
  were rechecked unchanged, as were the three recorded Git revisions.
  Numbered equations C1–C45 and the step counts were checked; tables have
  consistent columns and there is no trailing whitespace. These are
  identity/format checks, not an independent mathematical verification.

Current counts: **7 PROVEN, 7 DRAFTED, 4 GAP** (numbered steps only).
The three weakest links are the complete finite-u marginal estimate G2,
the all-history representation and coefficient budgets G1/G3, and the
prefix-continuous volume-independent tuning map G4. P6 removes the older
Gaussian partial-sum gap at its reviewed scope; it does not remove these.

Recovery starts from the exact source hashes above, C15's full state,
C18–C20/C37's unevaluated actual-model inequalities, and C38–C45's common
windows. The next decision is whether one complete actual projected return
meets those inequalities; if its source changes, refresh the affected
interface before using this conditional chain.
