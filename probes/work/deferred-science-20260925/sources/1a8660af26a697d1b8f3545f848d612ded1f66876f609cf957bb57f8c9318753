# A limited attaining construction for the no-first-birth target

Personal root supplement, 2026-09-24. Written and sealed before reading the
new independent PRE. It depends on the frozen no-first-birth derivation;
it is not a construction of the full original continuous process.

Fix a positive observation time t. Let v be the original N=4 no-event ket,
p=||v||^2, phi=v/sqrt(p), and Q_0,Q_1 its exact Hermitian energy clusters.
The target is only the subnormalized N=4 block omega=p|phi><phi|. The other
number-sector outputs are unconstrained in this relaxation.

## Truncation and invariant subspace

The same analytic grade counting as in the frozen argument gives

    ||Q_r E_0||=O(epsilon^(r+2)), r>=1,

where the estimate concerns the action of the no-event low column and the
Hermitian r-th cluster. Equivalently use Q_r J_0 P; the low Hermitian and
no-event subspaces differ first through a degree-two diagonal loss insertion
and r adjacent hops. The propagated exact high components have norms
O(epsilon^4), O(epsilon^5), O(epsilon^6) for r=2,3,4, and the first-high
component decays exponentially on a fixed later interval. Therefore

    ||(I-Q_0-Q_1)v||=O(epsilon^4).

Normalize phi01=(Q_0+Q_1)phi/||(Q_0+Q_1)phi|| and retain the exact p.
Pure-state trace distance gives

    ||p|phi01><phi01|-omega||_1
       =2p||(I-Q_0-Q_1)phi||=O(epsilon^4)=o(epsilon^3). (A1)

Let e8 be any physical fully occupied N=8 vector, of exactly zero energy.
Take the invariant system subspace

    D=ran(Q_0,N4) direct-sum ran(Q_1,N4) direct-sum span{e8}.

It contains the initial canonical psi. Let E_min=min spec(H|D). The low
canonical block is KD plus uniformly bounded terms and D is nonnegative;
hence E_min>=-O(1). Since the zero eigenvalue of e8 is included, E_min<=0.
The first high band is positive for small epsilon and has center
delta epsilon^-4 with width O(epsilon^-2). Thus

    diam spec(H|D)=delta epsilon^-4+O(epsilon^-2).       (A2)

## Exact conserving swap and resources

Use a replica apparatus R of D with H_R=H|D-E_min I and prepare

    sigma_R=p|phi01><phi01|+(1-p)|e8><e8|.              (A3)

The sectors in (A3) are orthogonal and reduce H_R. On system D tensor R,
apply the swap, and on the orthogonal system complement apply identity.
The invariant decomposition makes this a global unitary commuting exactly
with H_system+H_R. For the given canonical input in D, the system output is
exactly (A3), while R holds the input. Its N=4 block is the target in (A1).
No extra time or outcome flag is needed: N distinguishes success and failure
and commutes with H. Both R's preparation and the observation time are supplied.

The initial apparatus's energetic Fisher information is

    F_R(sigma_R)=4p Var_H(phi01).

Removing the omitted Hermitian high bands does not change the leading
conditional second moment: their total probability is O(epsilon^8), their
energy norm is O(epsilon^-4), and their contribution to the second moment
is O(1), which vanishes after multiplication by epsilon^2. The first two
energy clusters retain the leading epsilon^-2 variance from the frozen proof.
The conditional means remain bounded. Consequently

    epsilon^2 F_R(sigma_R) ->192 kappa^2 exp(-48 kappa t),
    epsilon^4 diam spec(H_R) ->delta.                  (A4)

The frozen covariance lower bounds apply to this one-block target, so (A4)
attains their leading coefficients for the class eta=o(epsilon^3), using
this particular O(epsilon^4) sequence. It does not meet every separately
prescribed smaller tolerance. Preloading the full phi would match omega
exactly but includes further high clusters and is not a sharp-range result.

The ground-relative apparatus mean is

    Tr(H_R sigma_R)=p<phi01,H phi01>-E_min=O(1).        (A5)

It is nonnegative by construction. The high-band contribution to this mean
is only O(epsilon^2); the low-band and ground offset are bounded. This is
a bounded mean statement, not its optimum or a specific physical value.

## Why this is a restricted comparison

The apparatus preloads the answer. It returns (A3) on every system input in
D and thus generally fails the original channel on other inputs. Its entire
failure probability is placed in N=8; the actual original process generally
has both N=6 and N=8 outcomes. Consequently this construction does not match
the full one-time ensemble, a trajectory, a multi-time process or a sustainable
apparatus. It only proves that the no-first-birth block's resource lower
coefficients alone do not force a divergent mean energy.

The quantitative lower bounds still apply to an approximation of the full
original ensemble, because that stronger task includes the specified block.
No full-process attainable optimum is inferred from this one-block escape.
Large classical energy fluctuations alone remain different from energetic
coherence, and a different interacting conservation law changes the premise.
