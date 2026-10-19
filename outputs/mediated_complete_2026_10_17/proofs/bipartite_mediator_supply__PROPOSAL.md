# A gapped bipartite mediator as an integer-length coupling supplier

Status: new conditional constructive exploration requiring a distinct check. A dimerized finite mediator gives an exactly zero diagonal bandcenter self-energy and a geometrically small off-diagonal Schur entry. For an isolated cell with sufficiently weak endpoint connections, a two-dimensional dressed subspace and product-endpoint preparation error can also be controlled. This does not derive native interactions, assemble the three-source ratios, or transfer a complete apparatus theorem.

## Positive physical realization and what is supplied

Take endpoints u,v and 2n internal head sites 1,...,2n, with integer n>=1. Supply fixed positive coefficients J,q,gamma with 0<q<J. The internal bonds (2l-1,2l) have magnitude J, l=1,...,n; the bonds (2l,2l+1) have magnitude q, l=1,...,n-1. Connect u to1 and2n to v with magnitude gamma. All exchange hoppings have negative sign. The graph is one path; there are no other contacts or internal degrees coupled to the mediator.

Use the same full-qubit positive-head convention as the checked source attachment:

    Q_a(i,j)=a(n_i+n_j-X_ij),
    X_ij=|10><01|+|01><10|.

On a pair, Q_a has eigenvalues 0,0,2a,2a: vacuum00 has0, the one-head symmetric/antisymmetric states have0 and2a, and11 has2a. Thus each block is PSD and preserves head number. Choose a supplied common onsite mu>=max{J+gamma,J+q}; this also dominates endpoint incident sum gamma. Add at each site the nonnegative occupation

    [mu-sum_(bonds incident to site i) a] n_i.

For n=1 the q bonds are absent; the same sufficient mu bound is harmless. The FULL qubit Hamiltonian is exactly

    H_cell=mu N_head-sum_edges a X_edge.                (1)

In the one-head sector this is mu I minus the weighted adjacency matrix; the all-blank vacuum has energy zero. The carrier exp(-it mu) in the one-head sector must be retained. Subtracting mu I is not a full-qubit global shift across different head-number sectors. Any pre-existing supplied vacancy scalar would have to be added separately and retained. This construction itself adds none.

The coefficients J,q,gamma, common onsite relation, exact bipartite graph, selective installation and initial one-head sector are substantial supplied premises. The occupations depend on the incident coefficients, although they need no n-dependent exponentially small subtraction. This is not a proof that independently varying microscopic bonds preserve equal onsite energies. At fixed J,q,gamma, only the integer n changes the coupling family.

The explicit isolated cell has 2n+2 heads, 2n+1 bonds and at most4n+3 unmerged positive blocks if every site occupation is counted, including any zero term. This is a construction count, not a minimum or the count of an attached processor.

## Genuine internal gap and exact bandcenter Schur matrix

Write z=E-mu and let A be the positive-weight adjacency matrix on the 2n INTERNAL sites only. The internal one-head Hamiltonian relative to mu is -A. In odd/even ordering,

    A=[[0,B],[B^T,0]], B=J I+q S,

where S is a one-step shift (its orientation depends only on the ordering). Since ||S||<=1,

    sigma_min(B)>=J-q=:a>0.

Thus every internal eigenvalue has modulus at least a. This is a genuine finite-size-uniform gap, not a formal inverse of a zero mode. At n=1 the actual gap is J; using a is conservative.

Let C map the endpoint basis to internal ends: C|u>=|1>, C|v>=|2n>. Then C^T C=I and the source-to-internal block is -gamma C. The exact eliminated equation is

    [z I-Sigma(z)] psi_end=0,
    Sigma(z)=gamma^2 C^T(zI+A)^-1 C.                  (2)

The sign in (2) comes from two negative endpoint hoppings. At z=0 the inverse of A is off-diagonal in the bipartition, so its two same-sublattice diagonal entries vanish. The opposite-end entry follows either from the bidiagonal inverse

    (J I+q S)^-1=J^-1 sum_(l=0)^(n-1)(-q S/J)^l

or a path recurrence. In the original endpoint order,

    Sigma(0)=t0 X_uv,
    t0=(-1)^(n-1) gamma^2 q^(n-1)/J^n.               (3)

For n=1 this gives positive gamma²/J; for n=2 it is negative gamma²q/J². Thus the induced off-diagonal Hamiltonian entry has the sign displayed, rather than being automatically a negative hopping. Its magnitude is (gamma²/J)(q/J)^(n-1). A fixed endpoint sign gauge can convert a positive entry to the negative-hopping convention, but that gauge must also be applied to endpoint states and every external contact; it cannot be silently dropped in a phase-sensitive apparatus target.

The exact zero diagonal in (3) is a chiral/bipartite bandcenter fact. No gamma²/J endpoint counterterm is required to cancel a diagonal shift at E=mu. It is not an assertion that the finite-energy self-energy is diagonal-free.

## Finite-energy dependence with explicit bounds

For complex |z|<a, the resolvent series and norm bound give

    ||(zI+A)^-1||<=1/(a-|z|),
    Sigma'(z)=-gamma² C^T(zI+A)^-2 C,
    ||Sigma'(z)||<=gamma²/(a-|z|)²,
    ||Sigma(z)-Sigma(0)||<=gamma²|z|/[a(a-|z|)].       (4)

In particular no inverse power of the exponentially small t0 appears in these absolute local bounds. The first-order expansion is

    Sigma(z)=Sigma(0)-gamma² z C^T A^-2 C+R2(z),
    ||R2(z)||<=gamma²|z|²/[a²(a-|z|)].                (5)

Reflection symmetry makes the two diagonal entries equal. Chiral symmetry makes the diagonal part odd in z and the off-diagonal part even. More explicitly,

    C^T A^-2 C=d_n I,
    d_n=J^-2 sum_(l=0)^(n-1)(q/J)^(2l).

Therefore Sigma(z)=s(z)I+t(z)X with s(0)=0, t(0)=t0, s'(0)=-gamma²d_n and t'(0)=0. The odd/even parity follows from the resolvent series, not from neglecting terms. The diagonal remainder after its linear term even admits the stronger bound gamma²|z|³/[a³(a-|z|)] by dropping the symmetry-forbidden quadratic term. Equation (5) is a sufficient bound for the entire matrix.

This exhibits energy renormalization and dressing rather than an additive constant detuning. Uniform onsite matching and reflection/bipartite structure are still exact premises. The effective energy-independent hopping t0 is not claimed to be the exact dressed splitting at finite gamma.

## Isolated dressed pair and product-endpoint preparation

For the following conclusions impose the additional explicit small-connection condition

    0<gamma<=a/4.

Let Hbar=H_cell-mu I in the one-head sector and V embed the two bare endpoint states. The decoupled Hbar_0 has two zero eigenvalues and internal spectrum outside (-a,a). The endpoint coupling perturbation has norm gamma, since C is an isometry. Weyl's bound gives exactly two eigenvalues in [-gamma,gamma], with all others outside (-a+gamma,a-gamma). The low pair is isolated. The same conclusion in each reflection-parity subspace gives one low eigenstate for each endpoint vector w_+=(u+v)/sqrt2 and w_-=(u-v)/sqrt2.

The full path is bipartite with an even total number of sites. Its chiral sign operator anticommutes with Hbar and reverses reflection parity. Consequently the low eigenvalues are z_+=t_eff and z_-=-t_eff, for a real signed t_eff, and their endpoint components have parity w_+,w_-. They cannot be zero: the full even path has nonzero determinant when all its bonds are nonzero. This is consistent with the Schur equation (2).

For each low eigenvalue z_s, its normalized eigenvector may be chosen as

    phi_s=[V w_s ; chi_s]/sqrt(1+||chi_s||²),
    chi_s=-gamma(z_s I+A)^-1 C w_s.

Here the notation separates endpoint and internal coordinate ranges. The sign follows directly from the internal row of E-H. Since |z_s|<=gamma,

    ||chi_s||<=rho:=gamma/(a-gamma)<=1/3.              (6)

Reflection makes the two channels orthogonal, and chiral symmetry gives equal internal norms for the pair. Let W_d map w_s to phi_s with positive endpoint overlap. It is an isometry onto the exact low spectral subspace P_low, and

    H_cell W_d=W_d(mu I+t_eff X),
    ||W_d-V||<=rho,
    ||(I-P_low)V||<=rho/sqrt(1+rho²).                 (7)

For clarity, in each parity channel the overlap is 1/sqrt(1+||chi_s||²), so the squared vector difference is 2[1-1/sqrt(1+||chi_s||²)]<=||chi_s||². The outside probability in that channel is ||chi_s||²/(1+||chi_s||²). Orthogonality of parity sectors lifts these scalar statements to the two-input operator norm, including arbitrary passive references.

Thus a bare occupied endpoint with blank mediator is a legitimate product preparation with explicitly bounded leakage from the isolated dressed pair. No adiabatic preparation is presumed. If gamma/a is not small, this particular product-preparation bound need not be useful.

A controlled relation to t0 follows from (4). Put

    epsilon_d=gamma²/[a(a-gamma)]<=1/12.

On the low plus-parity eigenvalue the exact Schur equation and (4) imply

    |t_eff-t0|<=epsilon_d |t_eff|,
    sign(t_eff)=sign(t0),
    |t_eff-t0|<=epsilon_d/(1-epsilon_d) |t0|.          (8)

The sign statement follows because epsilon_d<1 and t0 is nonzero. This is a relative approximation to the exponentially small hopping, not an absolute O(gamma²/a) uncertainty replacing it. The exact low pair remains centered at mu by chiral symmetry.

For the ISOLATED cell, (7) also yields the explicit bare-endpoint dynamic comparison

    ||exp(-it H_cell)V-V exp[-it(mu I+t_eff X)]||<=2rho,

uniformly in real t. Replacing t_eff by the bandcenter t0 adds at most |t|epsilon_d|t0|/(1-epsilon_d). These are two-level coherent-motion bounds, not irreversible transfer or storage. At times of order1/|t0| the extra approximation cost is controlled by epsilon_d; it is not made small merely by increasing n at fixed gamma/a. No external load is included in these statements.

## What the mechanism removes and what remains

At exactly equal onsite mu and exact bipartite couplings, the mediator introduces no additive endpoint self-energy at bandcenter. Increasing integer length makes the Schur hopping geometrically small while the internal gap lower bound a and preparation-error envelope remain uniform in n. The exact dressed hopping has the same magnitude scaling up to the bounded relative factor in (8). This is a constructive integer-length family, not continuous coefficient tuning or arbitrary source-ratio synthesis.

Several precision requirements remain substantial:

- The common onsite identity must be maintained. An independent endpoint diagonal error can act directly in the low endpoint pair at first order; it need not inherit the exponential suppression. Such errors may therefore overwhelm t0. Chiral symmetry does not certify generic diagonal-disorder tolerance.
- The positive Q realization needs occupations mu minus incident sums. Their values are ordinary supplied scales with no length-dependent exponentially small endpoint adjustment, but bond/occupation correlations are still required if the supplied coefficients change.
- J,q,gamma and the graph must be supplied. Exponential dependence on n does not prove a native supplier, an adjustable continuous parameter, arbitrary target precision or stable assembly of the critical three-source ratios. At fixed q/J the leading family is geometrically spaced; increasing n also increases distance and qubit count.
- Attaching endpoints to a processor changes the spectral and preparation problem. The isolated low-pair gap, reflection symmetry, target phases and dynamics cannot be transferred without a new loaded analysis. Leakage bounds here do not establish the full apparatus's source vacuum, spectral windows or performance.

No new physical axiom, native interaction identification, common-mode source theorem, permanent halt or full-apparatus resource advantage is claimed. This isolates one mathematically viable bandcenter mechanism and its unresolved implementation obligations.

## Source convention and exposure

The positive-head convention was refreshed from `three_site_actual_attachment/PROPOSAL.md`, SHA-256 `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006`; its distinct check is `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`. Only the Q-block convention is imported, not that apparatus's source, calibrated spectral theorem or performance.

Root requested this specific bipartite mediator exploration and proposed the expected Schur scale. I reconstructed the gap, sign, finite-energy expansion and isolated preparation estimates here; the suggested scale was not evidence. I have authored and reviewed source/phase interfaces in the same campaign, but this is new author work requiring a distinct check, especially of the full-qubit onsite realization, inverse signs, low-pair isolation and preparation bounds. No numerical spectrum, sweep, dynamics simulation, solver, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.
