---
claim_id: energy_transfer_correlation_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Compact-time subsequential fixed ordinary L2 even-cell correlations for actual-energy-bounded normal states; explicit sufficient spectral, form and leakage comparisons for broader bounded even words."
upstream_dependencies:
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/energy_transfer_correlation_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Control bounded even correlations through energy transfer and low-state limits in the supplied two-branch model."
source_of_blocker_text: frontier_question
next_trace_action: "Complete exact assembly review and source integration; retain stated model and observation hypotheses."
conditional_surface_status: "Supplied massive free chain and chosen Fock representation; Current remains open_gate."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional correlation and quantitative comparison theorems; no unique state selector or independent audit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem

Status: conditional-support

Primary runner: [source identity and reconstruction only](../scripts/energy_transfer_correlation_identity_2026_10_12.py).
It executes zero mathematical predicates or scientific mutations. Source hashes,
archive reconstruction and cache freshness do not establish a proof or N-gate PASS.

**Publication review record:** The complete 957-line synthesis received a
source-exposed ordinary check of its exact frozen bytes. The complete 343-line
review, SHA-256
`009043c543e809e4a19483bdc3d2932e61ff92170f1f76428cf8e851e3c48e57`,
found no material mathematical error and required no repair. Root read the
entire source and review. Two review stream failures are preserved; the second
occurred after the complete review and its completion receipt were saved. Root
recovered that complete artifact rather than inferring a result from a missing
final message. Exact exposure limits are in the archived root acceptance record.

The separate transfer and normal-limit cores and their source-exposed comparisons
are preserved with shared-model and shared-premise limitations. The synthesis
review checked the assembled normality/correlation proof directly; it did not
claim to reread every underlying normality note or to audit the parents. This
wrapper is packaging, not another independent mathematical check. Publication
wrapper review and root execution acceptance remain pending at preparation.
Pending-review language in the unchanged source records its original chronology.


# Energy-controlled even correlations in the supplied current refinement

**Author synthesis, 2026-10-12.** In the supplied massive chain, every sequence
of normal initial states with uniformly bounded actual energy has a subsequence
whose fixed ordinary L2 even-cell multitime correlations converge, uniformly
on compact time sets, to a normal full low-Fock state of finite energy. The
proof combines a full-CAR normal-limit lemma with Current C25 and a low partial
trace. It does not require energy-transfer conditions on those ordinary cells.

For more general varying observation families, this note proves separate
sufficient comparison criteria. Two-sided energy ceilings or two-sided
energy-form bounds improve scalar sector compression to order c. A different
norm-leakage route needs neither condition. The actual low dispersion admits
a two-sided energy-weighted phase estimate of order c^(2/3), with explicit
finite-word constants. Fixed ordinary smooth compact cells also satisfy these
quantitative form hypotheses. General trace/strong and weighted/CAR state-limit
routes remain distinct sufficient alternatives.

These are conditional implications, not a derivation of the chosen model,
state, physical observation rule, or a unique continuum state. The current
refinement parent remains `open_gate`, with its N1/N5 packet obligations
unchanged. No independent audit, retained status, Lean result, or physical
selector is supplied by this synthesis.

## 1. Sources, exposure and conventions

The exact sealed mathematical inputs are:

| Input | SHA-256 | Role |
|---|---|---|
| ENERGY_TRANSFER_ROOT_RECONSTRUCTION.md | dc3a429afc045d6bf39564f1ada2c1dddfab056ce3c2ba5ad34f1f13a095d75a | Two-sided compression and weighted low-phase reconstruction |
| ENERGY_TRANSFER_ROOT_ADDENDUM_A.md | 8d9d3852b98d3fc069e49a23717e9d01a9534384a1057c3e7e09225a075fc0a5 | Commutator domain proof and ordinary smooth cells |
| ENERGY_TRANSFER_INDEPENDENT.md | 43e18b4aea04768989d2e8a7cf31276653ca471a2af6259f4e47a044a532f80b | Separately frozen spectral/form/leakage proofs and comparison limits |
| energy_transfer_correlation/DERIVATION_CHECKPOINT.md | 0797320a95c5f0757e85b8f9b8c41a6bfbab4a758d4215ae037a1888d14f7284 | Preserved partial author work; not an independent completed source |

The first three are ordinary derivations produced before mutual comparison,
with shared-model and shared-premise limitations. This author read them before
writing this note. Their agreement is not a proof certificate; the complete
arguments used here appear below. The unsealed recovered author draft is
preserved unchanged and is not part of this note's proof basis.

Canonical parent bytes were selected at main revision
`7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de` and inspected in the shared
worktree. Root subsequently refreshed that worktree onto main
`516cb69d8487ff04f8a48e065d3dcbe71d7dd237`; the relevant canonical parent
and procedure bytes remain unchanged. The finite-energy publication source
listed separately below is a proposal, not a file on either main revision.

- `docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md`, C20-C22:
  the actual positive full spin-GNS Fock Hamiltonian, with vacuum energy zero.
- `docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md`, L1-L10,
  L18-L25: supplied scaling, real CAR normalization, generator domains,
  physical cells and the compatible even-spin identification.
- `docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md`,
  C1-C25 and its erratum/disposition: the real state-preserving current
  embedding, both branches, actual energies, and ordinary cell limits.
- `docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md`,
  complete section 3: prior finite-word energy ceilings, including adjoint
  rows. That generic mechanism is not new here; its scattering premises are
  not used in this chain.

The complete proposed publication source
`docs/FINITE_ENERGY_SECTOR_SELECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md`
was also read, with SHA-256
`f554bf91ca35673a30ca840c7b358ae8d19407c92a289e454cb43ac720dbcd8d`.
It is on root's proposal head `173c0d4d281bb67c7795f6bf87d4d25c2b2ed2d3`
(PR9499), not the assigned main base. Its original source is pinned at
`648e61978fc5b7d7b84ec6ddc7cb4c6d506405827e7aad1fa80f99cf9211d52c`.
The full-band gap and normalized compression used here are reproved below;
this citation supplies conditional source lineage, not main or audit authority.

Exact hashes and read coverage are in `energy_transfer_synthesis/`. The
registered realized-state primitive was checked: it supplies pointwise
specialization, not the energy bound, state convergence, or the chosen state.
The mathematical construction uses no new physical axiom or primitive.

Fix m,v>0, an arbitrary fixed reference energy mu>0, and 0<=M<infinity.
Empty products below are one. All energy expectations mean positive
quadratic-form expectations.
All bounded operators under discussion may be non-self-adjoint even words;
real and imaginary parts give self-adjoint observables. The Hilbert space and
normal density class include both particle parities.

## 2. Actual Fock space, the gap, and two extension conventions

The current parent's real coefficient isometry J_c intertwines its chosen
polarizations. Restriction to the positive polarizations and exterior powers
therefore give the vacuum-preserving Fock isometry into

    F = F_-(h_L direct-sum h_H),

where each one-particle summand has one complex fiber over p in R. Let F_c
be the Fock space over both bands I_c=(-1/c,1/c), and let Pi_c project onto
F_c. Let P be the no-high-particle projection, Q=1-P. P commutes with Pi_c.
On F_c, the actual transported positive Hamiltonian is

    H_c = dGamma(e_c,L direct-sum e_c,H),
    w_c(p) = sqrt(1-c^2 p^2),
    e_c,L(p)^2 = m^2 + (2v^2/c^2)(1-w_c(p)),
    e_c,H(p)^2 = m^2 + (2v^2/c^2)(1+w_c(p)),
    Lambda_c = sqrt(m^2+2v^2/c^2).                     (1)

The operator is the direct sum of positive sums on particle sectors, with
its maximal multiplication domain. Its form domain is Dom(H_c^(1/2)). In
particular, it is not the signed two-component coefficient generator. The
one-particle inequality e_c,H>=Lambda_c on the entire high band implies

    H_c >= Lambda_c N_H >= Lambda_c Q                 (2)

as forms, first on finite sectors and then by positive spectral truncation.
No energy offset has been subtracted. Set U_c(t)=exp(itH_c) and
alpha_c(t)(A)=U_c(t) A U_c(-t).

A density rho_c on F_c with energy at most M satisfies

    delta_c=Tr(rho_c Q)<=M/Lambda_c,
    tau_c=P rho_c P,
    p_c=Tr(tau_c)=1-delta_c.                           (3)

For p_c>0 put sigma_c=tau_c/p_c. These densities can be embedded into the
common Fock space by zero. Purify rho_c as Psi, and use
(P tensor 1)Psi/sqrt(p_c) as a purification of sigma_c. Their overlap is
sqrt(p_c). The two-dimensional pure-state eigenvalue calculation, followed
by contractivity of partial trace, gives

    ||rho_c-sigma_c||_1 <= 2sqrt(delta_c).              (4)

P is only a representation-level projection here; no quasilocal preparation
operation or physical selection is inferred.

There are two distinct operator extensions. The real coefficient isometry
induces a **unital CAR embedding** into the common CAR algebra, represented
on all of F. An even in-band CAR element acts also on spectator outside-band
states. Its restriction to F_c is the physical finite-c represented operator.
By contrast, extending that restriction by zero gives Pi_c A Pi_c, whose
identity is Pi_c, not 1. The corner extension is not the unital CAR extension.
All finite-c expectations agree on states supported in F_c.

Likewise identify P F with F_L=F_-(h_L), and write
q_c=Gamma_-(1_{I_c}) on F_L. A compressed physical operator B_c on the
finite-c low band has zero extension a_c=q_c B_c q_c. An even low-band CAR
extension b_c, when available, acts on all of F_L and satisfies

    a_c=b_c q_c=q_c b_c.                              (5)

For an even in-band common CAR element, high-vacuum conditional expectation
produces such a b_c. This map is unital, completely positive and contractive,
but is not a *-homomorphism. In particular P A_1 A_2 P need not equal
P A_1 P A_2 P.
The correlation estimates below control precisely these missing insertions.

## 3. Two-sided energy ceilings give an O(c) scalar estimate

Fix n>=1 and bounded even A_j,c on F_c, with ||A_j,c||<=a_j. Write
A_j=A_j,c(t_j), W=A_1...A_n, C=P A_1 P...P A_n P, and a=product_j a_j.
The times are arbitrary real numbers and need not be ordered. An empty word
has correlation one and needs no comparison theorem.

Suppose, for E_c(R)=1_[0,R](H_c) and all R>=0,

    A_j,c E_c(R) F_c subset E_c(R+L_j,c) F_c,
    A_j,c* E_c(R) F_c subset E_c(R+L_j,c) F_c,         (6)

where L_j,c>=0. Evolution preserves these inclusions. Put L_c=sum_j L_j,c.
For 0<R<Lambda_c-L_c, every successive factor of W applied from the right
to E_c(R) stays below Lambda_c and hence in P F_c. The same is true for
the reversed adjoint word. Thus D=W-C satisfies

    D E_c(R)=E_c(R) D=0,
    D=(1-E_c(R))D(1-E_c(R)),     ||D||<=2a.

The positive trace-class compression of rho_c to that spectral tail has
trace at most M/R. Consequently

    |Tr(rho_c W)-Tr(tau_c C|F_L)| <= 2a M/R,          (7)
    |Tr(rho_c W)-Tr(sigma_c C|F_L)|
                           <= 2a M/R + a delta_c.    (8)

Here C|F_L is identified with the product of the compressed low factors.
Taking R=(Lambda_c-L_c)/2 gives the sufficient bound

    a[4M/(Lambda_c-L_c)+M/Lambda_c].                  (9)

For fixed n and uniformly bounded a_j,L_j,c,M this is O(c), uniformly in
all t_j. This is only a sector-compression statement; continuum dynamics
will require compact time windows. If the initial state is supported in
E_c(R_0) with R_0+L_c<Lambda_c, the compression is exact.

Only a forward ceiling proves D E_c(R)=0. It does not prove the left
annihilation used in (7). Cauchy-Schwarz then gives at best the corresponding
square-root tail argument without more information; section 10 supplies
an actual one-sided Theta(sqrt(c)) witness. Compact-current-support low CAR
words are a nonempty two-sided class: each creator or annihilator changes
energy by at most the uniform maximum of e_c,L on its packet support, and
finite products add those bounds. Such packets are generally not compact
in physical position. The underlying finite-word ceiling principle already
appears in the compact-patch Fock note, section 3.

## 4. Two-sided form control gives an explicit O(c) bound

Put G_c=H_c+mu. Suppose A_j,c and its adjoint preserve Dom(G_c^(1/2)) and

    ||G_c^(1/2) A_j,c G_c^(-1/2)|| <= k_j,c^+,
    ||G_c^(1/2) A_j,c* G_c^(-1/2)|| <= k_j,c^-.       (10)

These are bounded extensions with the domain preservation included in the
hypothesis. They are unchanged by the actual time evolution. P is a
contraction in this graph norm.

The exact left-to-right insertion identity is

    W-C = sum_(j=0)^n L_j Q R_j,
    L_0=1, R_0=A_1...A_n,
    L_j=P A_1 P...P A_j  (1<=j<=n),
    R_j=A_(j+1)...A_n, R_n=1.                         (11)

There are n+1 slots, including both endpoints. With X=rho_c^(1/2), finite
energy means ||G_c^(1/2)X||_HS^2<=M+mu. Cyclicity of trace-class products
and the Hilbert-Schmidt inner product give

    Tr(rho_c L_j Q R_j)=<Q L_j* X,Q R_j X>_HS.

Since Q commutes with G_c and ||Q G_c^(-1/2)||<=(Lambda_c+mu)^(-1/2),

    |Tr(rho_c L_j Q R_j)|
      <= (M+mu)/(Lambda_c+mu)
          (product_(i<=j) k_i,c^-)(product_(i>j) k_i,c^+).

The graph estimates for the prefix adjoints and suffixes are both used.
This calculation is valid for an arbitrary density of finite form energy:
write X in columns in an orthonormal basis, use (10) on each form-domain
column, and sum the square bounds. Alternatively use finite-rank and spectral
truncations and closedness of G_c^(1/2). No action of H_c on a merely bounded
observable vector has been assumed.

Define

    S_c = (M+mu)/(Lambda_c+mu)
            sum_(j=0)^n (product_(i<=j) k_i,c^-)
                          (product_(i>j) k_i,c^+).     (12)

Then

    |Tr(rho_c W)-Tr(tau_c C|F_L)| <= S_c,
    |Tr(rho_c W)-Tr(sigma_c C|F_L)| <= S_c+a delta_c.  (13)

If k_j,c^+,k_j,c^-<=K_j uniformly, S_c is at most
(n+1)(M+mu) product_j K_j/(Lambda_c+mu), hence O(c). This improves the
unrestricted trace-distance order (4) only for this restricted observation
class. Neither (6) nor (10) is asserted necessary or equivalent to the other.
A weaker word-dependent condition is directly visible in (11): the sum of
the two intermediate graph-norm products divided by Lambda_c+mu must vanish.

## 5. A domain-valid bounded-commutator sufficient condition

Let H>=0 be self-adjoint and A bounded. Assume A maps Dom(H) into Dom(H)
and C=HA-AH on Dom(H) has a bounded extension of norm d. Let G=H+mu.
The resolvent identity gives

    [(G+s)^(-1),A]=-(G+s)^(-1) C (G+s)^(-1).

For x in Dom(G), the square-root integral

    G^(1/2)x=(1/pi) integral_0^infinity
                        s^(-1/2) G(G+s)^(-1)x ds

converges strongly: its integrand is bounded by s^(-1/2)||x|| near zero
and s^(-3/2)||Gx|| at infinity. Apply it to Ax and x, use
G(G+s)^(-1)=1-s(G+s)^(-1), and subtract. This proves on Dom(G)

    [G^(1/2),A]=(1/pi) integral_0^infinity
                  s^(1/2)(G+s)^(-1) C (G+s)^(-1) ds. (14)

The right integral converges in operator norm, since

    (1/pi) integral_0^infinity s^(1/2)/(mu+s)^2 ds
                                              =1/(2sqrt(mu)).

The equality follows by s=mu u^2 and then u=tan(theta). Thus its norm is
at most d/(2sqrt(mu)). For x in Dom(G^(1/2)), approximate x by its bounded
spectral cutoffs x_N in Dom(G). In
G^(1/2)A x_N=A G^(1/2)x_N+[G^(1/2),A]x_N both terms on the right converge,
and A x_N converges to Ax. Closedness proves form-domain preservation and
extends (14). In particular

    ||G^(1/2) A G^(-1/2)|| <= ||A|| + d/(2mu).        (15)

Apply this separately to A*. A sufficient way to establish the initial
operator-domain assumptions for both is norm differentiability of
alpha_t(A)=exp(itH)A exp(-itH) at zero. If its derivative is delta(A), then
for x in Dom(H),

    exp(itH)Ax=alpha_t(A)exp(itH)x

has a strong derivative at zero. The generator characterization gives
Ax in Dom(H) and [H,A]x=-i delta(A)x. The adjoint evolution is also norm
differentiable, with the same derivative norm. This supplies the domain
statement rather than assuming it from a formal commutator.

## 6. Norm leakage gives a different sufficient route

Suppose only that epsilon_j,c=||Q A_j,c P|| tends to zero. It is invariant
under alpha_c. Inserting P successively from the right in W P yields

    ||(W-C)P|| <= sum_(j=1)^n epsilon_j,c product_(i!=j) a_i.

Using (4), then computing within sigma_c, proves

    |Tr(rho_c W)-Tr(sigma_c C|F_L)|
      <= 2a sqrt(M/Lambda_c)
             + sum_j epsilon_j,c product_(i!=j) a_i.  (16)

No energy-form domain condition on the observables is used. Exact
preservation of P is included. This route is useful when common full-CAR
observables converge in norm to low even elements: such a target preserves
P, so its norm difference bounds epsilon_j,c. It does not identify P with
a physical measurement, and it gives no automatic convergence of low states
or low dynamics.

## 7. Actual low dispersion and the global weighted phase estimate

On F_L put H_0=dGamma(E), E(p)=sqrt(m^2+v^2 p^2), and U_0(t)=exp(itH_0).
For comparison only, define bar e_c=e_c,L on I_c and bar e_c=E outside I_c,
and bar H_c=dGamma(bar e_c), bar U_c(t)=exp(it bar H_c). This auxiliary
extension agrees with actual low dynamics on q_c F_L. It does not assert
additional physical finite-c modes or change any physical energy.

Rationalization of (1), throughout I_c, gives

    E <= e_c,L <= sqrt(2) E,
    e_c,L-E = v^2 c^2 p^4/[(1+w_c)^2(e_c,L+E)]
                      <= kappa c^2 E^3,
    kappa=1/(2v^2).                                    (17)

Indeed e_c,L^2=m^2+2v^2p^2/(1+w_c), and its squared difference from E
is v^2 c^2 p^4/(1+w_c)^2. The lower denominator e_c,L+E>=2E and
v^4 p^4<=E^4 give (17). The extension preserves these inequalities.
Thus H_0<=bar H_c<=sqrt(2)H_0, with identical operator domains and
identical form domains, with equivalent graph norms.

Define Delta_c to be the nonnegative self-adjoint multiplication operator
whose value on a particle configuration is sum_i(bar e_c(p_i)-E(p_i)).
It agrees with bar H_c-H_0 on their common operator domain, but that
algebraic difference is not asserted to have the maximal domain of Delta_c.
For total continuum energy x=sum_i E(p_i), including x=0 in the vacuum,

    0<=Delta_c(configuration)<=kappa c^2 sum_i E(p_i)^3
                                      <=kappa c^2 x^3. (18)

As a form assertion this in particular holds on Dom(H_0^(3/2)); it is
not an equality of domains. The following phase estimate instead uses (18)
pointwise in joint functional calculus and requires no third moment of a state.

Let G_0=H_0+mu and define

    r_c(s)=min(2/mu, 2^(2/3)(kappa |s| c^2)^(1/3)).

Since min(2,y)<=2^(2/3)y^(1/3),

    ||G_0^(-1/2)(bar U_c(s)-U_0(s))G_0^(-1/2)||
      <= r_c(s).                                      (19)

To see the constant, the scalar expression is bounded by
min(2,kappa |s|c^2 x^3)/(x+mu), at most
2^(2/3)(kappa |s|c^2)^(1/3) x/(x+mu). It is also at most 2/mu,
and is zero when s=0. This is a global two-sided c^(2/3) estimate.
No optimality claim is made.

For comparison, min(4,y^2)<=2^(5/3)y^(1/3) gives, for every
psi in Dom(H_0^(1/2)),

    ||(bar U_c(s)-U_0(s))psi||
      <=2^(5/6)(kappa |s|c^2)^(1/6)||H_0^(1/2)psi||.  (20)

Density and the uniform norm bound 2 imply strong convergence on every
vector, uniform in bounded s intervals. On a fixed spectral window
H_0<=R one has the stronger operator bound |s|kappa c^2 R^3. The window
need not be finite dimensional. The high branch has not been replaced by
E; its fixed-compact-momentum energy remains 2v/c+O(c).

## 8. Full finite-word comparison with explicit constants

Use the state rho_c of (3), fixed n, and the two-sided actual form bounds
(10). Let a_j,c be the zero-extended low compression of A_j,c on F_L,
and let a_j,0 be a bounded candidate continuum operator. Assume uniform
bounds ell_j^+,ell_j^- for both their forward and adjoint G_0 form norms,
including form-domain preservation, and define

    eps_j,c=||G_0^(-1/2)(a_j,c-a_j,0)G_0^(-1/2)||.

These errors are assumed to tend to zero. They are weighted operator-norm
errors, not bare strong convergence. Let

    s_0=t_1, s_j=t_(j+1)-t_j (1<=j<n), s_n=-t_n,
    T_j=(product_(i<=j) ell_i^-)(product_(i>j) ell_i^+),
    O_j=(product_(i<j) ell_i^-)(product_(i>j) ell_i^+),
    a_0=product_j ||a_j,0||.

For any density rho_0 on F_L, the correlation error obeys

    |Tr[rho_c product_j alpha_c(t_j)(A_j,c)]
       -Tr[rho_0 product_j alpha_0(t_j)(a_j,0)]|
    <= S_c
       +(M+mu)[sum_(j=0)^n T_j r_c(s_j)
                        +sum_(j=1)^n O_j eps_j,c]
       +a_0 ||tau_c-rho_0||_1,                        (21)

where S_c is the explicit expression (12). If all actual k_j,c^+ and
k_j,c^- are bounded by K_j, and ell_j^+,ell_j^- by L_j, a convenient
version is

    (n+1)(M+mu) product_j K_j/(Lambda_c+mu)
    +(M+mu)[(product_j L_j) sum_(j=0)^n r_c(s_j)
                  +sum_j eps_j,c product_(i!=j) L_i]
    +a_0 ||tau_c-rho_0||_1.                           (22)

No division by a possibly zero operator norm occurs in these constants.

Proof. Equation (13) first replaces the full word by its low compressed
word in tau_c. Because P reduces H_c, that low word is

    bar U_c(s_0) a_1,c bar U_c(s_1) ...
                                      a_n,c bar U_c(s_n).

The auxiliary extension gives exactly the same expectation as the physical
low group: tau_c and every a_j,c are supported on q_c, which the group
preserves. Intermediate *mixed comparison words* need not stay in q_c;
they are legitimate operators on the explicitly defined common F_L.

Telescope the alternating n observable and n+1 unitary factors, replacing
factors from left to right. In each term the left prefix contains target
factors and the right suffix contains finite-c factors. All groups commute
with G_0, so their graph norms are one. If D is the changed factor, put
X=tau_c^(1/2). The graph-domain hypotheses and Hilbert-Schmidt Cauchy-Schwarz
give

    |Tr(tau_c L D R)|
      <= ||G_0^(-1/2)D G_0^(-1/2)||
         ||G_0^(1/2)L*X||_HS ||G_0^(1/2)R X||_HS.

Here ||G_0^(1/2)X||_HS^2=Tr(tau_c H_0)+mu p_c<=M+mu, because
H_0<=H_c on the low band. At a unitary slot, the product of graph constants
is T_j; at an observable slot it is O_j, omitting the changed observable.
Use (19) or eps_j,c accordingly. Trace duality for the remaining fixed target
word gives the last term in (21). This proves the complete finite sum.

On |t_j|<=T,

    sum_(j=0)^n |s_j|^(1/3)
              <=2T^(1/3)+(n-1)(2T)^(1/3).             (23)

Thus fixed n, uniform form constants, eps_j,c->0 and
||tau_c-rho_0||_1->0 give compact-time correlation convergence. The last
state assumption is equivalent to ||sigma_c-rho_0||_1->0 when p_c->1,
since ||sigma_c-tau_c||_1=delta_c. Positive bounded spectral truncations
of H_0 show Tr(rho_0 H_0)<=M. None of these statements extracts that state
convergence from a mean-energy bound alone. Section 12 gives a separate
CAR-state alternative with its own topology and target-algebra conditions.

The low graph constants can be checked from the actual ones. Compression
by the reducing P does not increase the actual H_c+mu form constants.
On q_c F_L,

    G_0 <= H_c,L+mu <= sqrt(2)G_0.

Commutation of q_c with G_0 then gives for a_j,c and its adjoint the
G_0 form bounds 2^(1/4) k_j,c^+ and 2^(1/4) k_j,c^-. Thus one may take
ell_j^+ and ell_j^- as maxima of these bounds and the corresponding
continuum bounds. This proves the conversion rather than concealing it
in a word-dependent constant.

There is a separate qualitative route: suppose zero-extended a_j,c converge
strong-* to a_j,0, uniformly bounded in norm, and sigma_c converges in trace
norm to rho_0. Equation (20) implies compact-time strong-* convergence of
the time translates. For a fixed vector, strong convergence is uniform on
its compact target-unitary orbit by a finite-net argument and the uniform
operator bounds. Finite products have the same property, and a finite-rank
trace approximation gives a compact-time error eta_c(T)->0 against rho_0.
Combining this with any normalized sector bound (8), (13), or (16), denoted
S_c^norm, proves

    error <= S_c^norm + a ||sigma_c-rho_0||_1 + eta_c(T). (24)

The target operators must additionally belong to continuum CAR if that is
the intended target algebra: strong-* convergence alone does not prove that
membership. Formula (24) has no rate without rates for its two limiting
terms. It cannot be combined with merely CAR convergence of varying states
by replacing trace norm with an unspecified weak topology; section 12
explains the needed uniform comparison.

## 9. Ordinary smooth compact cells satisfy the quantitative hypotheses

For each j choose a fixed finite even list of real two-component functions
f_j,r in C_c^infinity(R;R^2), 1<=r<=2k_j. Use the parent's actual cells

    (C_c f)_n=c^(-1/2) integral_[cn,c(n+1)] f(x) dx

and actual even-spin word

    A_j,c=j_c[product_(r=1)^(2k_j) c_c(C_c f_j,r)].

Every word is supported in the finite hull of its occupied cells, by the
compatible even Jordan-Wigner construction. The number of cells can grow
as c decreases. Odd auxiliary fields are not identified with bilateral
quasilocal spin observables. Arbitrary single-site or staggered families
are not silently included in this chosen fixed-envelope class.

The exact normalization is ||c_c(z)||=||z|| for real z. The actual coefficient
flow is exp(+itD_c); its derivative coefficient is iD_c z, which is again
real. It is not in general the scalar coefficient e_c z. For 0<c<=c_0,
Local L10 and contraction of C_c give

    l_j,r=||f_j,r||,
    d_j,r=||D f_j,r||
             +(c_0/2)(m||f_j,r'||+v||f_j,r''||),
    ||C_c f_j,r||<=l_j,r,
    ||D_c C_c f_j,r||<=d_j,r.                         (25)

There is no extra sqrt(2). Finite field products are norm differentiable
under the actual flow, so set

    a_j=product_r l_j,r,
    d_j=sum_r d_j,r product_(s!=r) l_j,s,
    K_j=a_j+d_j/(2mu).                               (26)

The word and its adjoint have norm at most a_j and commutator norm at most
d_j. The norm-derivative/domain argument of section 5 proves the two-sided
actual form bounds k_j,c^+,k_j,c^-<=K_j. The continuum word b_j,0 has
analogous constants K_j,0 obtained by replacing d_j,r by ||D f_j,r||.
Here D=iv sigma_x partial_x-m sigma_y on H^1, and the smooth functions
lie in its domain. These constants are finite and independent of c.

For extension bookkeeping, let tilde A_j,c be the full unital common-CAR
image with coefficient fields c_*(J_c C_c f_j,r). Current C21 proves
J_c C_c f_j,r->(f_j,r,0). The CAR norm estimate and telescoping therefore give

    ||tilde A_j,c-tilde A_j,0||<=nu_j,c ->0,
    nu_j,c=sum_r ||J_c C_c f_j,r-(f_j,r,0)||
                                      product_(s!=r) l_j,s.              (27)

The target is the low-only even word b_j,0. Identify
F=F_L tensor F_H with the usual parity factor on high odd fields. In the
high-vacuum compression only terms with an even number of high fields
survive. Each is a scalar high contraction times an even low-band word.
Thus b_j,c, the full low-CAR image of that compression, belongs to the
low-band even-CAR algebra and has the identity on outside-band low modes.
It commutes with q_c and satisfies ||b_j,c-b_j,0||<=nu_j,c. Generally it
is not the product of the separately compressed fields; high contractions
must be kept. Its physical low restriction has zero extension

    a_j,c=b_j,c q_c.

Every vector in (1-q_c)F_L has at least one particle outside I_c, so
H_0>=E_edge,c=sqrt(m^2+v^2/c^2) there. The adjoint continuum graph estimate
makes G_0^(-1/2)b_j,0 G_0^(1/2) bounded by K_j,0. Consequently

    a_j,c-b_j,0=(b_j,c-b_j,0)q_c-b_j,0(1-q_c),
    eps_j,c<=nu_j,c/mu + K_j,0/(E_edge,c+mu) ->0.       (28)

For the second term, factor its weighted version as
(G_0^(-1/2)b_j,0 G_0^(1/2))G_0^(-1)(1-q_c). This explains the use of
the adjoint form bound. Although q_c tends strongly to 1, it never tends
to 1 in norm when the outside band is nonempty; (28) is deliberately
weighted. Uniform low graph constants in (21) may be chosen

    ell_j^+=ell_j^-=max(2^(1/4)K_j,K_j,0).             (29)

This supplies a nonempty actual local even-spin class for the full
quantitative comparison theorem. The vacuum, or any fixed finite mixture
of finite-particle compact-low-momentum densities at sufficiently small c,
gives examples of the state-convergence hypothesis. These are test families,
not derived physical state or measurement selection rules. The phase term
has the explicit c^(2/3) rate, but (27) has not supplied a rate for nu_j,c,
nor has an arbitrary state convergence assumption supplied its rate.

## 10. Counterexamples and exact quantitative limits

**Initial energy alone does not control operator-created high excursions.**
Choose disjoint normalized compact-current-support high packets u,v and
B=a*(u)a*(v), of norm one. For small c this is an actual even in-band CAR
and hence even quasilocal spin element. With phi=u wedge v, the vacuum
energy is zero, while h_c=<phi,H_c phi>=4v/c+O(c). Actual evolution gives

    <Omega,B* alpha_c(t)(B)Omega>
                  =exp(i4vt/c)+O(|t|c)               (30)

for each fixed t, because both high energies equal 2v/c+O(c) uniformly
on the packet supports. For t!=0, c_n=4v|t|/(2pi n) and
c'_n=4v|t|/((2n+1)pi) give different limits. On c_n=c_0 2^(-n),
t=pi c_0/(6v) gives alternating cube-root phases. All low compressions
of B vanish. Its forward ceiling grows like 1/c, its form norm grows at
least like c^(-1/2) on the vacuum, and ||QBP||=1. Thus (30) violates the
actual sufficient observation hypotheses, rather than contradicting them.

**One-sided control can have a square-root loss.** The pair annihilator
B* has a forward ceiling L=0: it only removes positive-energy particles.
For fixed M>0, eta_c=M/h_c<1, and
psi_c=sqrt(1-eta_c)Omega+sqrt(eta_c)phi, the energy is M and

    <psi_c,B*psi_c>=sqrt(eta_c(1-eta_c))=Theta(sqrt(c)),
    P B* P=0.                                        (31)

Its adjoint creates energy of order 1/c. B* also has a forward form
contraction: on the finite-particle form core, the annihilation-density
formula ||H_c^(1/2)psi||^2=integral e(p)||a(p)psi||^2 dp, summed over
branches, and a(p)B*=B*a(p) give
||H_c^(1/2)B*psi||<=||H_c^(1/2)psi||. The same holds with H_c+mu,
since ||B*||=1; closure extends it to the form domain. Its adjoint has
no uniform reverse bound. Thus neither one-sided ceiling nor one-sided
form control can replace both legs in the uniform O(c) theorem.

**The O(c) sector order is sharp uniformly over the stated classes.**
For the same fixed M>0 use
rho_c=(1-eta_c)|Omega><Omega|+eta_c|phi><phi| with eta_c=M/h_c,
and the high number projection n_u=a*(u)a(u). Its low compression is zero
and Tr(rho_c n_u)=eta_c=Theta(c). It satisfies two-sided ceilings uniformly.
If the high energy on the fixed compact support of u lies in [r_c,s_c],
annihilation removes at least r_c and creation adds at most s_c, so n_u
has ceiling L_c=s_c-r_c in both directions. Here r_c,s_c=2v/c+O(c),
and s_c-r_c=O(c). Spectators retain their energies.

It also satisfies uniform form bounds. Split off all one-particle modes
in that support K. Then r_c N_K<=H_K<=s_c N_K, and n_u commutes with N_K.
Thus q_(H_K)(n_u psi)<=s_c <psi,N_K psi><=(s_c/r_c)q_(H_K)(psi).
The complementary energy commutes with n_u and is contracted by it.
Adding mu shows a two-sided graph bound at most sqrt(max(1,s_c/r_c)),
first on the finite-particle core and then by closedness. It is bounded
and tends to one. This is a sharpness statement for uniform sector error,
not a rate claim for all terms of (21).

**The low state can alternate.** Alternate the vacuum with a fixed compact
low two-particle density along a sequence of spacings. Both are already in P
and their actual energies are uniformly bounded; a fixed low number observable
distinguishes them. For any prescribed M>0, use instead a sufficiently small
fixed positive mixture with that pair density. The example then fits that
energy budget and still has two different limits. At M=0 the massive positive
Hamiltonian permits only the vacuum, so that boundary case is different.

**The low observable limit is a separate condition.** Alternating the even
observables A_c=1 and A_c=-1 in the vacuum gives alternating one-point
functions, despite zero transfer and form constants one. The corresponding
zero extensions are alternating q_c and -q_c. Energy control alone does not
supply their fixed observable limit.

**Unrestricted observable norm persists.** The same n_u has norm one at
every sufficiently small c and P n_u P=0. Its full C*-norm therefore does
not vanish, even though all its expectations in the energy-M state class
are bounded by M/Lambda_c. This does not erase the doubled equal-time algebra.

**Compact time is substantive.** On a fixed compact low momentum set,

    (e_c,L-E)/c^2 -> f(p)=v^2 p^4/(8E(p))             (32)

uniformly. For a nonzero packet supported away from p=0 and
t_c=tau/c^2, the squared norm of the difference of the two evolved
one-particle vectors tends to the integral of
|exp(i tau f(p))-1|^2 against its packet density. Choose small nonzero
tau so this integral is positive. Two disjoint such low packets give an
even pair-creator version: apply the difference of its evolved operators
to Omega and obtain the positive limiting integral with relative phase
exp(i tau[f(p)+f(q)]). This rules out an unqualified all-time operator
comparison; it does not assert that every fixed scalar correlation fails
at those times. For growing times or word lengths the actual sums in
(12), (21) and (23), together with all state/observable errors, must vanish.

These examples refute only the stated implications with missing hypotheses.
The spectral, form and leakage conditions are positive sufficient routes,
not independent physical obstructions or an exhaustive list of admissible
observations. No universal impossibility result or N1-N8 packet completion
is asserted; the inherited current-parent N1/N5 obligations remain open.

## 11. Normal subsequential limits on the full CAR algebra

This section was added only after explicit authorization to read the two
separately sealed normal-limit sources:

| Input | SHA-256 |
|---|---|
| LOW_ENERGY_NORMAL_LIMIT_ROOT_PROBE.md | 3c30599a04ee55ed51b3f1d6514b67e3015ab8a2e74d6ce464912944cd65fd73 |
| LOW_ENERGY_NORMAL_LIMIT_INDEPENDENT.md | 2274b6e0a045a27d54f2888ce6f7482e466af956a76dbd33a48a630ca258ccf0 |

They were both read completely after sections 1-6 had first been saved.
Their pre-comparison derivations are separate evidence with shared-model
and shared-premise limitations. The following composition is author work;
final-source mathematical review remains separate. In particular it makes
no normality assertion in an even-only vacuum Hilbert space.

**Lemma.** Let h be separable, e>=m>0 positive self-adjoint, and
H=dGamma(e) on the full vacuum fermionic Fock space. Any sequence of normal
densities with energy at most M has a subsequence converging pointwise on
CAR(h). Every such CAR cluster state is represented by a unique normal
full-Fock density rho with Tr(rho H)<=M. This is CAR weak-star convergence;
it is not trace-norm convergence or convergence on all bounded Fock operators.

If h is finite dimensional, Fock space is finite dimensional and the lemma
follows from compactness of the density matrices and continuity of their
energy expectation. Assume henceforth that h is infinite dimensional.
First, CAR(h) is separable. A countable norm-dense set in its unit ball and
successive subsequences extract convergent scalar expectations on that set.
The diagonal subsequence extends, by the uniform functional bound one, to a
positive unital functional omega on the whole algebra. This proves
subsequential existence; the rest proves normality of any cluster state.

Choose an orthonormal basis u_1,u_2,... and n_j=a*(u_j)a(u_j). For every K,

    sum_(j<=K) omega(n_j)<=M/m,

because the finite sum is a bounded CAR element and m sum_(j<=K)n_j<=H
as forms. Hence r_K=sum_(j>K)omega(n_j) tends to zero for this one limit
state. This does not assert a uniform tail bound for the original sequence.

Let d_L be omega's density on the finite full matrix algebra of its first
L modes. In the ordered Fock factorization, the first-K algebra acts as
B(F_K) tensor 1. High-factor odd fields carry the parity string, but ordinary
partial trace still gives the correct first-K marginal d_K, including when
the state has parity coherences. For L>K, project onto the vacuum of modes
K+1,...,L. Its failure probability obeys

    delta_(K,L)<=sum_(K<j<=L)omega(n_j)<=r_K.

For r_K<1, (4) on this finite matrix algebra bounds the distance of d_L
to its normalized compressed state s_K tensor vacuum by 2sqrt(r_K).
Partial trace bounds ||s_K-d_K||_1 by the same amount. Extending all
remaining modes by their vacuum therefore gives normal full-Fock densities
D_L,D_K satisfying

    ||D_L-D_K||_1<=4sqrt(r_K).                        (33)

They are trace-norm Cauchy. Their positive trace-one limit rho has every
prescribed finite-mode marginal, and therefore represents omega on the
norm-dense union of finite-mode algebras. This proves normality.

For completeness, uniqueness does not require confusing a finite-mode
CAR algebra with an exterior-vacuum projection. Let Q_K be the latter
representation-level projection; Q_K increases strongly to 1 on full
Fock. For trace-class T, ||T-Q_K T Q_K||_1->0. A norm-one matrix testing
the trace norm of Q_K T Q_K on F_K is realized in the first-K CAR algebra,
acting with identity on its complementary modes. If T vanishes as a
functional on CAR, its pairing with that test is zero, so
||Q_K T Q_K||_1<=||T-Q_K T Q_K||_1. Letting K increase proves T=0.

To recover the full unbounded energy, take e_R=e 1_[0,R](e) and any
increasing finite-rank projections p_K->1 on h. The bounded finite-rank
positive operators

    b_(R,K)=e_R^(1/2) p_K e_R^(1/2)                  (34)

increase strongly in K to e_R and obey b_(R,K)<=e_R<=e as forms. Each
dGamma(b_(R,K)) is a bounded positive CAR element: diagonalizing its
finite-rank one-particle operator writes it as a finite sum of eigenvalues
times number projections. Its norm is the sum of those eigenvalues.
Second quantization preserves the form inequality, so the original states
and then omega have expectation at most M on every one of these tests.

Now rho is normal. On each finite particle sector dGamma(b_(R,K))
increases strongly to dGamma(e_R). Positive particle-sector truncation
and monotone trace convergence give

    Tr[rho dGamma(e_R)]
            =lim_K Tr[rho dGamma(b_(R,K))]<=M.

Finally e_R increases to e, sector by sector and in positive forms;
monotone trace convergence gives Tr(rho H)<=M. This avoids the generally
invalid order claim p_K e p_K<=e and avoids requiring the range of an
arbitrary p_K to lie in an unbounded operator domain. The lemma is proved.

For the present low states, Tr(sigma_c H_0)<=M/p_c and p_c->1. The same
extraction argument uses an eventual uniform bound M+1. Each bounded test
in (34) then has limiting expectation at most limsup M/p_c=M. Thus every
sequence c_n->0 has a subsequence whose sigma_c states converge on the whole
low CAR algebra to a normal density rho_0 with energy at most M. The same
subsequence works for all CAR observables, not a separately chosen sequence
for each word. The functional tau_c differs from sigma_c by norm delta_c,
so its CAR limit is the same state.

Three topology qualifications are essential. An orthonormal sequence of
one-particle modes in a fixed finite-energy band has CAR states tending to
the vacuum but densities pairwise at trace-norm distance 2. This construction
is available in the continuum chain's infinite-dimensional compact momentum
band. The vacuum projection, a bounded Fock operator, has expectation zero
in those densities and one in the limiting CAR state's normal extension.
Thus full B(Fock) state cluster points need not equal that extension or be
normal. Also, strong operator convergence with uniform form bounds is
insufficient for changing-state correlations: for e=mI, the number
projections n_j tend strongly to zero and have form constant one, while
Tr[|u_j><u_j| n_j]=1. Their weighted errors in (21) do not tend to zero.

Finally, parity invariance passes to the CAR limit as a symmetry, and
uniqueness of its normal extension implies that density commutes with
(-1)^N. A fixed global parity sector need not pass. Fix u_0 and take
orthonormal u_j orthogonal to it, all in a bounded-energy band. The even
pair states u_0 wedge u_j have CAR limit the odd one-particle state u_0.
The finite-mode marginals in a basis containing these packets show this
directly. Extend u_0 to any complete basis (u_0,w_1,w_2,...). On the even-only
vacuum Fock space, the even CAR projections

    n(u_0) product_(j=1)^K(1-n(w_j))

tend strongly to zero, but the limiting odd one-particle state assigns one
to each. That limit is therefore not normal in the even-only representation.
It is normal on full Fock,
which is exactly the representation used throughout this note. No claim
that particle number, energy value, or fixed parity is conserved in a CAR
state limit is made; the energy conclusion is an upper bound.

## 12. CAR-state correlation limits and the direct ordinary-cell theorem

In (21), if the target a_j,0 belong to low CAR, replace the final trace-norm
term by the exact state error

    d_c(T)=sup_(|t_j|<=T)
       |Tr[(tau_c-rho_0) W_0(t)]|,
    W_0(t)=product_j alpha_0(t_j)(a_j,0).             (35)

Every preceding error term and proof remains unchanged. If sigma_c converges
pointwise on CAR to rho_0, then d_c(T)->0. Indeed free CAR dynamics is
point-norm continuous: it is so on a*(f) by strong one-particle continuity
and ||a*(f)||=||f||, then on polynomials and by norm approximation on CAR.
The target words on a compact time rectangle therefore form a norm-compact
subset of CAR. Uniformly bounded functionals converging pointwise converge
uniformly on this subset by a finite epsilon-net argument. The difference
between tau_c and sigma_c adds at most delta_c a_0.

Combining (12), (19), (21), (28) and the normal-limit lemma gives the
following conditional subsequential result. Given any sequence c_n->0 of
actual normal initial states with a uniform energy bound, extract one
subsequence whose low states converge on all CAR. For every fixed finite
family satisfying the two-sided form hypotheses, weighted observable
convergence and CAR target membership, the actual multitime correlations
converge uniformly on compact time rectangles to those of that subsequence's
normal rho_0 under the actual low continuum dynamics. Fixed ordinary smooth
compact cells are a verified instance. This is not a unique all-spacing
state selector, and no rate for d_c(T) follows from extraction.

There is a stronger and simpler observation-specific route for ordinary
cells that does not require smoothness or form bounds. Take any fixed finite
even words in real f_j,r in L2. For compact position support these remain
actual finite-support even spin words at every c; otherwise they are even
quasilocal words. Current C25 gives

    sup_(|t|<=T)
       ||J_c exp(itD_c) C_c f_j,r-(exp(itD)f_j,r,0)|| ->0.

The common full-CAR images tilde A_j,c(t) therefore converge in norm,
uniformly in that interval, to the low-only word b_j(t)=alpha_0(t)(b_j,0).
Put a_j=product_r||f_j,r|| and

    nu_j,c(T)=sum_r sup_(|t|<=T)
        ||J_c exp(itD_c)C_c f_j,r-(exp(itD)f_j,r,0)||
                                      product_(s!=r)||f_j,s||,
    nu_word,c(T)=sum_j nu_j,c(T) product_(i!=j)a_i.

Finite product telescoping yields

    sup_(|t_j|<=T)||tilde W_c(t)-tilde W_0(t)||
                                      <=nu_word,c(T)->0.                 (36)

The full target tilde W_0 is W_0 tensor 1_H. For this direct route define
a different low density, supported on q_c F_L, by ordinary partial trace

    widehat rho_c=Tr_(F_H)(rho_c),
    Tr(widehat rho_c)=1,
    Tr(widehat rho_c H_0)
                =Tr[rho_c(H_0 tensor 1_H)]<=M.        (37)

The last inequality follows on F_c from the positive decomposition
H_c=H_c,L tensor 1+1 tensor H_c,H and H_0<=H_c,L. Positive bounded spectral
truncations justify the unbounded partial-trace equality; no commutation of
rho_c with H_c is required. This density is not tau_c=P rho_c P. It retains
low reduced states from all high occupation sectors and needs no normalization.

Apply the normal-limit lemma directly to widehat rho_c, retaining the exact
bound M. Along its CAR-convergent subsequence with limit rho_0, the completely
explicit direct comparison is

    sup_(|t_j|<=T)
      |Tr(rho_c tilde W_c(t))-Tr(rho_0 W_0(t))|
      <=nu_word,c(T)
        +sup_(|t_j|<=T)|Tr[(widehat rho_c-rho_0)W_0(t)]| ->0.             (38)

Indeed Tr(rho_c tilde W_0)=Tr(widehat rho_c W_0) exactly, so (36) is the
only operator-comparison cost. The compact-word argument controls the last
term. The finite-c expectation is physical because rho_c is supported in
F_c. No high-vacuum normalization or gap-compression error enters (38).

The two low-state routes are consistent. Partial trace kills the off-diagonal
P/Q blocks, so widehat rho_c=tau_c+R_c, where
R_c=Tr_(F_H)(Q rho_c Q) is positive of trace delta_c.
Hence ||widehat rho_c-tau_c||_1=delta_c and
||widehat rho_c-sigma_c||_1<=2delta_c. Their CAR subsequential limits therefore
agree along any common subsequence. This comparison does not identify the
two finite-c constructions or make high-vacuum compression multiplicative.

Equation (38) proves a subsequential finite multitime limit for fixed ordinary
L2 cell words under the uniform actual-energy bound on states. A separate
energy-transfer condition on these observables is unnecessary because C25
already controls their whole common-CAR time evolution. One state subsequence
works for every fixed finite word and compact time set. The quantitative
general theorem remains useful for other admissible families where only
weighted comparison is available.

Formula (38) does not include arbitrary c-dependent envelopes, alternating
cell sections, unrestricted microscopic observables, growing words or
unbounded time windows. In particular C24's alternating sections retain a
high component, so the high-pair counterexample is not removed by this
ordinary-cell conclusion. Neither (21) nor (38) asserts a universal rate
for the total error without rates for the displayed observable and state
terms. There is no interaction, higher-dimensional, thermal infinite-volume,
boost or measurement-selection conclusion.

## 13. Proof disposition and verification limits

The transfer crosscheck `ENERGY_TRANSFER_CROSSCHECK.md`, SHA-256
`e058ef395ffe717d2813a56e384091673eca0406ad2f5f2f7ecd57b2c5048c95`, was
read completely after the first source increment. It supports the sealed
core estimates and supplied the same finite-interval bookkeeping as (21).
The present source explicitly incorporates its precision corrections:
real-field derivatives use the signed coefficient generator; Delta_c is
defined by joint multiplication functional calculus; high-vacuum compression
is distinguished from multiplication and from unital extension. Originals
were preserved rather than silently rewritten.

The normal-limit crosscheck `LOW_ENERGY_NORMAL_LIMIT_CROSSCHECK.md`, SHA-256
`0b6f580c6feacdfc0723dbe8922a7721af8d02efcac06220e3649f83e48ffa41`, was
read completely after the first complete draft. It confirms the two sealed
normality proofs and supplies the stronger low-partial-trace application.
Section 12 adopts that application explicitly, using widehat rho_c to keep it
distinct from tau_c=P rho_c P. The superseded direct draft bound with a
2a delta_c normalization cost is recorded in the exposure/change evidence;
it was a valid weaker comparison, not a hidden repair of the sealed inputs.

The new normal-limit section and its correlation composition are proposed
ordinary proofs pending review of this exact final synthesis. Earlier source
checks do not certify this newly assembled argument. The independent cores
were frozen before cross-exposure but share model family and supplied
premises; no different-family, formal or audit independence is claimed.
The recovered prior author checkpoint/draft remains incomplete as a certified
delivery and is not counted as another independent completion.

No scientific numerical runner is required by the analytic proofs, and none
was run or fabricated. Mechanical checks in the evidence directory establish
source identities and preservation only. No audit verdict, retained status,
repository publication, Git mutation, or editable prompt change was made by
this bounded author task. Root owns further review and publication.


## Publication dependencies and review boundary

The direct mathematical parents are [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md)
for the state-preserving embedding, exact dispersions and ordinary-cell C25;
[Concrete](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md) for the
actual positive full spin-GNS Fock Hamiltonian; and
[Local Even](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md) for real
CAR normalization, cells, generator domains and the even-spin identification.
Their exact main bytes at 516cb69d8487ff04f8a48e065d3dcbe71d7dd237 are declared
inputs. Current remains open_gate. These are explicit conditional mathematical
imports, not new physical axioms or an effective retained-status claim.

The earlier finite-energy proposal is source lineage only. Its complete bytes
and original source are carried in the archive; the high-gap and compression
arguments needed here are reproduced in this note. No file from PR9499 needs
to exist on main or in the new child. Compact-patch section 3 already supplies
the generic spectral-ceiling mechanism; the present use claims no novelty for it.

The theorem's obligation graph is internal: the actual positive gap precedes
sector estimates; energy ceilings, energy forms and norm leakage are alternative
sufficient routes; the exact low dispersion supplies the weighted phase bound;
explicit state and observable comparison terms precede broader-word limits.
The full-CAR normal-limit argument and Current C25 supply the separate ordinary
L2-cell subsequential theorem. Full Fock is essential: parity invariance passes
under CAR convergence while fixed even-particle-sector support need not pass.
Low partial trace and normalized high-vacuum compression are distinct states.

The present source's c^(2/3) term is an upper phase estimate. This note makes no
optimality claim for its full correlation theorem. A separate companion source
in this proposal supplies a precisely scoped uniform phase comparison witness.
Its argument is not retroactively part of this unchanged synthesis.

Publication reconstruction removes only the original YAML metadata and adds
this header and appendix. Every mathematical-body byte is unchanged. The full
original file, original metadata, complete source/review cores and the exact
transformation are retained. The final assembled source remains subject to
root's exact-source review and acceptance.

The [No-Go Discipline Gate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/3679df3c7901b4660f5d9e9d69023e2e82772a83/.claude/science/physics-loops/toe-energy-correlations-20261012/NO_GO_DISCIPLINE_CHECKLIST.md)
records partial narrowing and the still-pending N1/N5 packet requirements.
No five-route exhaustiveness, no-go packet PASS, scientific execution, retained
promotion, Lean certificate or audit verdict is supplied. The strongest open
framework obligation is a derivation of the chosen dynamics, representation
and physical state/observation rules; this conditional theorem does not supply
that obligation. No unique or full-sequence selector is claimed.
