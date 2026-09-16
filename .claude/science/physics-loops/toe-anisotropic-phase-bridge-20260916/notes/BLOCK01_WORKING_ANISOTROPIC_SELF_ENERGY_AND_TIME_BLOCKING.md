# Working anisotropic self-energy and time-blocking analysis

Personal derivation in progress, 2026-09-16. This identifies one failed direct theorem substitution and a concrete resummation target. It is not a no-go for the phase, an axiom wall, or a claim to invent electric-flux Hamiltonians.

## 1. What the primary proof actually supplies

The full available text of the Frohlich-Spencer IHES/P/81/40 preprint has been read. Many displayed equations are absent from extraction; pages24 and35-37 were rendered and inspected. Sections2.8-2.12 extract a local Gaussian self-energy for defect currents, establish positive small-activity factors and derive a covariance comparison proving nonsummable field correlations at sufficiently large common coupling beta. This is stronger than a Wilson perimeter statement and weaker than a complete Gaussian scaling-limit theorem. The higher-rank and finite-clock sections do not, merely by their existence, supply a uniform Hamiltonian time-step limit.

Primary source: https://archives.ihes.fr/files/original/c59d65f61f9b1aba2d8eb6f4c01ceb88.pdf . The published version is DOI10.1007/BF01213610; its44 pages have not been obtained/read. The publisher exposes subscription metadata and Project Euclid returned an access-service error. The calculations below are derived directly rather than importing an unchecked numerical constant from the preprint.

## 2. Weighted conditional Gaussian identity

Write a dual real1-form alpha with Gaussian density proportional to

    exp[-(1/2) sum_(dual plaquettes p) w_p (d alpha)_p²],
    w_p=1/beta_(original plaquette *p).

A small positive diagonal regulator can first make the full Gaussian nondegenerate. For a dual link e, condition on all other links. The conditional precision is

    a_e=sum_(p containing e) w_p,

and its conditional mean u_e is determined by the cross term. Completing the square gives exactly

    E[exp(i rho alpha_e)|other links]
       =exp[-rho²/(2a_e)] exp(i rho u_e).            (1)

For a set of links with no common plaquette, their conditional precision is diagonal, so the extracted exponent is the sum of rho_e²/(2a_e). In the isotropic convention w=1/beta, an interior link has a_e=6/beta and the exponent is beta rho²/12.

Normalization caution: the displayed preprint Gaussian density on page24 and its conditional density on page36 have coefficient1/(2beta), while its displayed equation2.63 on page35 prints a damping exponent beta rho²/n_e. Direct completion of the square gives beta rho²/(2n_e) for those displayed conventions. The published version has not been checked, so no claim about a published error is made. A factor2 changes a loose threshold, not the existence mechanism. All calculations here will use the directly derived(1).

## 3. Substitution of the actual Hamiltonian scaling

First take the Haar rotor version of the calibrated temporal kernel. At fixed delta its eigenvalues are exp(-delta g² n²/2), corresponding to

    beta_tau=1/(g² delta).

The actual spatial factor in PR8162-8163 has Fourier weights y^(n²), where y=delta/(2g²)<1/8, hence its Villain parameter is

    beta_s=1/[2 log(2g²/delta)].

Hodge duality exchanges spatial and temporal plaquette types. An interior dual time link belongs to six dual temporal plaquettes, while an interior dual spatial link belongs to two dual temporal and four dual spatial plaquettes. Therefore

    a_0=6/beta_s=12 log(2g²/delta),
    a_i=2/beta_s+4/beta_tau
       =4 log(2g²/delta)+4g²delta.                  (2)

Both conditional variances1/a_e tend to zero as delta->0. For a fixed elementary integer defect charge rho=2pi, the extracted damping in(1) consequently tends to1. The direct single-link small-activity estimate from the isotropic proof loses its suppression. This is a statement about that particular estimate, not about the true defect activity after another resummation or about the phase itself.

The issue is already present in the Haar time-continuum target. The finite-clock calibration has additional crossover behavior, so beta_tau=1/(g²delta) must not be asserted on every joint finite-N path before taking its appropriate limit.

## 4. The integer time-step law that should be resummed

The dual temporal plaquette factor contains the one-dimensional integer law

    q_delta(k)=y^(k²)/sum_j y^(j²), k in Z,
    y=delta/(2g²).

Its variance is delta/g²+O_g(delta²). Replacing it by the real Gaussian with the same quadratic exponent instead gives variance beta_s=1/[2log(2g²/delta)]. Over T/delta steps the former has finite limiting variance T/g², while the latter diverges as T/[2delta log(2g²/delta)]. Thus the real Gaussian used before treating the integer constraint is a poor time-continuum reference. This is an explicit mechanism, not a proof that no Gaussian infrared limit exists after blocking.

The exact characteristic function of q_delta is the same b_y(theta) used in the spatial weight. Uniformly in real theta,

    b_y(theta)=1-(delta/g²)(1-cos theta)+O_g(delta²).

For M delta->T, its M-fold convolution converges to

    p_T(k)=exp(-T/g²) I_k(T/g²),
    sum_k p_T(k) exp(i k theta)
          =exp[-(T/g²)(1-cos theta)].               (3)

This is the difference of two independent Poisson counts, each of mean T/(2g²). It has a finite physical jump rate and retains non-Gaussian cumulants at fixed g and T. The following explicit bound uses L1 distance, twice the usual total-variation distance:

    ||q_delta^{*M}-p_(M delta)||_1 <=24 M y²
                                  =6 (M delta) delta/g4.       (3a)

Here is a direct proof for 0<y<=1/8. Put r=2 sum_(k>=2)y^(k²). Since successive exponents differ by at least5,

    r<=2y4/(1-y5)<=3y4,   Z=1+2y+r.

Compare q_delta with the probability b(0)=1-2y, b(1)=b(-1)=y. The zero-site error is nonnegative and at most4y², because

    q_delta(0)-b(0)=[4y²-r(1-2y)]/Z.

Each one-site error is at most2y²+3y5, and the remaining mass is at most3y4. Their sum is at most10y². Next compare a Bernoulli count of mean lambda=2y with a Poisson count of that mean, assigning independent equiprobable signs to each jump. Before the sign map, the L1 distance is exactly2 lambda(1-exp(-lambda))<=2lambda²=8y². Pushforward cannot increase this distance. Thus ||q_delta-p_delta||_1<=18y²<=24y². Convolution with a probability contracts L1, so telescoping proves(3a). The Poisson semigroup also satisfies ||p_s-p_t||_1<=2|s-t|/g², which treats rounded physical times.

For completeness, the variance convergence does not follow just by unweighted total variation. Directly,

    sum_(k>=2) k² y^(k²)<=5y4   (y<=1/8).

Indeed, k=j+2 gives k²>=4+5j and (j+2)²<=4(j+1)², so the sum is bounded by4y4(1+y5)/(1-y5)^3<=5y4. Consequently |Var(q_delta)-2y|<=16y², and |M Var(q_delta)-(M delta)/g²|<=4(M delta)delta/g4. These constants are deliberately loose.

For the isolated blocked increment X=g k, the exact real characteristic exponent is

    log E exp(i h X)=(T/g²)(cos(g h)-1),

with quadratic remainder bounded by T g² h4/24. A further large-time rescaling X/sqrt(T) makes that remainder O(g²/T). This illustrates the distinction between coarse graining and merely adding more sites. It is not a Gaussian limit of the coupled gauge theory.

## 5. Actual electric-flux representation and the missing interaction estimate

Let C be spatial curl, c_p=C*1_p its integer plaquette cycle, and D incidence, so Dc_p=0. In the physical rotor Fourier space, E is an integer link flux satisfying DE=0. The supplied pure-gauge Hamiltonian is

    H=K-L,
    K(E)=g²||E||²/2,
    (L f)(E)=(1/(2g²))sum_p[f(E+c_p)+f(E-c_p)-2f(E)].          (4)

Thus a classical continuous-time plaquette-jump process with quadratic killing gives the Feynman-Kac kernel of exp(-T H). This is standard electric-flux Hamiltonian/Markov machinery, not a new physics law; the canonical gauge Hamiltonian has direct prior art in Kogut-Susskind, Phys.Rev.D11,395(1975), DOI10.1103/PhysRevD.11.395. For a finite spatial graph, each signed plaquette jump has rate1/(2g²), and

    <E',exp(-T H)E>
      =E_E[exp(-integral_0^T K(E_s)ds) 1_(E_T=E')].            (5)

The jumps preserve DE=0 exactly. On any chosen integer Gauss sector, L is bounded and self-adjoint, K is nonnegative self-adjoint multiplication, and H=K-L is self-adjoint on Dom(K). One proof of(5) first bounds K by min(K,R), applies the bounded-generator expansion, and then takes R upward to infinity by monotone convergence of the positive path weights and of the associated quadratic forms. Finite volume is essential to this bounded-L argument. Fermion determinants or CAR signs have not been appended to this positive Markov representation.

For P spatial plaquettes, multiplication by B_delta in angle space is precisely convolution in electric space by the pushforward of P independent q_delta variables under (k_p)->sum_p k_p c_p. Relations between plaquette cycles do not affect that assertion. Independent Poisson variables under the same map give exp(delta L). By(3a) with M=1 and tensor-product telescoping,

    ||B_delta-exp(delta L)||_(ell2->ell2)<=24 P y².             (6)

Both factors are contractions. Inserting the common contractions Q_delta^(1/2)=exp(-delta K/2) and telescoping M transfer steps gives an operator-norm error at most24 M P y²=6 P (M delta)delta/g4 between the actual Villain-jump sandwich and its Poisson-jump sandwich. The latter tends strongly to exp(-T H) by the semibounded Trotter product formula. This is a finite-graph strong-limit proof with an extensive comparison error, not a volume-uniform phase estimate.

The original positive angle-space sandwich sqrt(B) Q sqrt(B) is not automatically entrywise positive in electric space: sqrt(B) can have signed Fourier coefficients. The alternative sandwich Q^(1/2) B Q^(1/2) does have a positive electric kernel because B has positive integer Fourier weights. For the pure-gauge E=0 boundary state, Q^(1/2)|0>=|0>, and, for M spatial slices,

    <sqrt(B)0,(sqrt(B) Q sqrt(B))^(M-1) sqrt(B)0>
       =<0,B Q B ... Q B 0>
       =<0,(Q^(1/2) B Q^(1/2))^M 0>.                         (7)

There are M copies of B and M-1 interior copies of Q in the middle expression. This is an exact boundary-amplitude identity; the whole transfer operators have not been identified.

Resumming independent jumps alone does not control(4), because the weight exp[-integral K(E(t))dt] couples spatial plaquette paths and all times. A useful next theorem would bound the connected physical-source response of this coupled process uniformly in volume at fixed small g, or compare a blocked positive weight with a controlled compact Gaussian-phase carrier. No such bound has yet been derived here.

## 6. Other routes still open

Integrating a whole temporal strip in the Gaussian dual field improves suppression of an isolated low-frequency current, but nearby opposite currents can cancel that gain. Microscopic temporal dipoles must be resummed; estimating isolated charges is not sufficient. This has not been turned into a no-go theorem.

A fixed microscopic Euclidean model followed by a macroscopic space/time scaling limit is another route to photons and need not equal the specific Kogut-Susskind Hamiltonian at fixed spatial lattice spacing. Main's provisional fixed-beta Haar full-score proposal and its finite-clock electric extension remain relevant alternatives. Composing the two-defect finite-clock carrier is a separate obligation; neither Gaussian smoothing nor a closed-current central limit theorem alone supplies the full photon field. If the Hamiltonian route does not produce a decisive estimate, reassess these alternatives rather than treating its failure as an axiom contradiction.

## Review and proposal status

The [claim-status contract](../CLAIM_STATUS_CERTIFICATE.md) and
[premise inventory](../ASSUMPTIONS_AND_IMPORTS.md) apply to this author
proposal. The [negative-claim checklist](../NO_GO_DISCIPLINE_CHECKLIST.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.
