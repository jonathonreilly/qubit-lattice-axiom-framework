# Post-PRE comparison and independent finite-time reconstruction

September 24, 2026 UTC. The root released the two author packets only after
authenticating this checker's PRE seal
82e5b45bc8ecf0aad7deb8f2af8c457062c2bcb860dc83d18c4538a1ac3053d9.
Every PRE artifact is preserved byte-for-byte. This report is a source-bound
proof comparison and extension check, not an audit or landing verdict.

No mathematical discrepancy was found in the two released notes. The exact
microscopic birth calculation agrees with the separately sealed PRE
reconstruction. The finite-time extension's eigenvalue argument and supply
inequalities are valid in the explicitly stated domains below.

## 1. Source identities and comparison coverage

Read in full after PRE:

* EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH.md, SHA256
  41408b6da165147fec4ce48e4ce2b063daeda2d42d939ced0fe7927b54c4e32c;
  its complete code exact_star_energy.py, SHA256
  ce202e534e19254516e7a3437c5c19e8a229334170eda73f65a16ae2f1fa377e.
  Author seal: ff9362d4ad06b36c86153d71b23b361843a77a26ceb4400f7b6ed14bea12aff5.
* FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND.md, SHA256
  f118d1fc459bafedd535cec6e7e22aaf940f4c89aae7260fb16017f0493d03d5;
  its complete code star_finite_time_energy.py, SHA256
  41060fa782b2aa4e25105360339f4fc0ae5b4bdecbe57d2364dee44a275ae8a8.
  Author seal: 4812c28ae4ec3cfcace52536cecd9156557cd851b1fd2b2958d361cc49fca3b1.

Both author seals and every listed artifact were authenticated before and
after the POST calculation. The author exact result's complete N=1 and N=3
Gauss bases and F matrices were compared, after basis alignment, with the
independently enumerated PRE matrices. Every published marked output vector,
rate, squared norm, conditional mean, high-energy probability and variance
was compared exactly. Both full initial energy derivatives agree exactly.
The PRE additionally supplies the full N=1 spectrum and both instruments'
complete loss matrices.

The author's extension imports the first author's builder and correctly
labels that computation as internal consistency evidence. The POST control
imports only this checker's frozen PRE engine. It does not import or execute
either author builder. Its symbolic two-dimensional matrix is projected from
the independent complete local-operator matrices.

## 2. Separate reconstruction of the extension's asymptotic step

Use epsilon,delta,kappa>0, a=1+3epsilon², and the orthonormal N=1 basis
(g,u), where u=(x_1+x_2+x_3)/sqrt(3). The independently constructed full
loss is 4 times the N=1 vacancy projector. Projecting the actual no-event
generator onto this reducing subspace gives

    G = [ -3i delta/epsilon²         i sqrt(3)delta/epsilon³ ]
        [ i sqrt(3)delta/epsilon³  -i delta/epsilon⁴-2kappa/epsilon² ].

The matrix G+G* is diag(0,-4kappa/epsilon²). It follows by evaluating this
quadratic form on an eigenvector that both eigenvalues have nonpositive
real parts, even though G is not normal.

Set eta=epsilon². Direct determinant expansion gives

    eta² z² + [i delta(1+3eta)+2kappa eta]z+i6kappa delta=0. (1)

At eta=0 this has the simple finite root z0=-6kappa; the z derivative
there is i delta, nonzero because delta>0. The analytic implicit-function
theorem applies to this polynomial in a neighborhood of (eta,z)=(0,z0).
Solving the coefficient of eta, independently in the POST control, gives

    z_s=-6kappa+(18kappa-12i kappa²/delta)epsilon²
                           +O(epsilon⁴).              (2)

The other root is z_f=tr(G)-z_s. For small epsilon they are distinct,
with z_f=-i delta/epsilon⁴+O(epsilon^-2). This separation, rather than
diagonalizability at every finite parameter value, is all the asymptotic
argument requires.

Now rotate to the exact orthonormal energy basis

    ell=(1,sqrt(3)epsilon)/sqrt(a),
    r=(sqrt(3)epsilon,-1)/sqrt(a).

The Hamiltonian in this basis is diag(0,delta a/epsilon⁴), and the
no-event generator becomes [[A,B],[B,D]], where

    A=-6kappa/a,
    B=2sqrt(3)kappa/(epsilon a),
    D=-2kappa/(epsilon²a)-i delta a/epsilon⁴.            (3)

Choose the slow eigenvector as (1,q) and the fast eigenvector as (p,1).
Their exact expressions, whenever epsilon is sufficiently small, are

    q=-B/(D-z_s)=(z_s-A)/B,
    p=B/(z_f-A).

Using either (2) or the separated denominator in (3),

    q=-2sqrt(3)i kappa epsilon³/delta+O(epsilon⁵),
    p=+2sqrt(3)i kappa epsilon³/delta+O(epsilon⁵).       (4)

In particular pq=O(epsilon^6), so 1-pq stays bounded away from zero.
The prepared initial coordinates are exactly (1,0). Without discarding
the fast component, the evolved low and high coordinates are

    alpha(t) = [exp(z_s t)-pq exp(z_f t)]/(1-pq),
    beta(t)  = q[exp(z_s t)-exp(z_f t)]/(1-pq).         (5)

Since both scalar exponentials have modulus at most one for t>=0,
(4)--(5) imply beta(t)=O(epsilon³) uniformly in t>=0. For each fixed T,
(2) gives alpha(t)=exp(-6kappa t)+O_T(epsilon²), uniformly on [0,T].
No large phase from z_f defeats this estimate because its coefficient
has already been bounded.

The exact positive no-event energy and birth probability therefore obey

    E_no(t)=(delta a/epsilon⁴)|beta(t)|²=O(epsilon²),
    P_birth(t)=1-|alpha(t)|²-|beta(t)|²
              =1-exp(-12kappa t)+O_T(epsilon²).         (6)

This is a direct moment argument; it does not derive the energy estimate
from trace-norm convergence. Constants may depend on fixed delta,kappa,T.
The expansion does not cover delta or kappa tending to zero with epsilon,
long times that scale with epsilon, or a changing graph.

## 3. Finite-time energy and the joint limit

The PRE independently derived the exact identity

    E_total(t)=E_no(t)+(3delta/2epsilon²)P_birth(t).      (7)

Its ingredients were independently checked: every first-event mark has
the time-independent normalized output already reconstructed; all resolved
marks have equal instantaneous probabilities; coherent marks double each
resolved intensity; no N=3 birth is possible; and subsequent N=3 Hamiltonian
evolution preserves its energy. Equation (7) includes the entire no-event
contribution and is valid for either supplied instrument at every finite
epsilon>0 and t>=0.

Combining (6) and (7) yields

    epsilon² E_total(t)
       -> (3delta/2)[1-exp(-12kappa t)].                (8)

The convergence is uniform on each fixed [0,T], and its limit is strictly
positive for each fixed t>0. Under epsilon² S(S+1)=delta/K,

    E_total(t)/[S(S+1)]
       -> (3K/2)[1-exp(-12kappa t)].

The source's stated fixed-time result follows. This is a divergence of
microscopic energy for the fixed original instrument and Hamiltonian.
It coexists with convergence to the zero-Hamiltonian effective density.
It says nothing about higher-dimensional graphs, repeated formation, or
an unchanged coefficient after adding another physical Hamiltonian term.

## 4. Conditional energy-supply inequalities

The reservoir statements add hypothetical assumptions; none is supplied
by the star GKLS law itself.

For the first inequality, suppose a joint system/environment state starts
with the system in ell, so its system energy is exactly zero. Let H_R>=0
and let the initial environment energy E_R(0) be finite. Assume the
joint unitary preserves the free sum H_system+H_R and reproduces the
actual microscopic system state, including its energy expectation at t.
The expectations are understood on their finite-energy domains. Then

    E_R(0)=E_total(t)+E_R(t)>=E_total(t)
               >=(3delta/2epsilon²)P_birth(t).          (9)

For the second inequality, suppose instead that an autonomous conserved
Hamiltonian has the explicitly supplied decomposition
H_system+H_R+V, with H_R>=0 and bounded self-adjoint V satisfying
||V||<=v_*. Then the conserved expectation gives

    E_total(t)
      =E_R(0)-E_R(t)+<V>_0-<V>_t
      <=E_R(0)+2v_*.                                  (10)

The coefficient two is justified by separately bounding the two interaction
expectations. It is not permissible to drop the final interaction energy
or to replace it with zero without another premise. At each finite epsilon
the star H_system is bounded, while positivity and the finite initial
reservoir energy make the displayed accounting meaningful. A claimed
unbounded-reservoir realization still needs its actual conservation and
domain hypotheses checked.

These are necessary conditions, not constructions or sufficient conditions.
They permit an initial supply or interaction norm that grows with
S(S+1), and they do not rule out changed microscopic instruments, external
work, different energy decompositions, or a representation that matches
only the limiting density. They do not establish a universal obstruction
to autonomous dilations.

Reproducing the exact finite-epsilon reduced state reproduces its energy
automatically because this finite star H is bounded for that epsilon.
The explicit energy qualification matters when a proposed approximation
reproduces states only in a limiting trace-distance sense. Here ||H|| is
of order epsilon^-4. An O(epsilon) density error gives no useful control
over an epsilon^-2 energy bill. The PRE already exhibits a normalized
exact-zero-energy projection of each output at O(epsilon) trace distance
from the actual output. This shows why (9) cannot be assigned to every
construction that reproduces only the limiting target density.

## 5. Completed evidence and limits

POST run 02 completed 249 checks, including provenance checks. It
exactly compared all first-author output formulas and reconstructed the
extension polynomial and low/high rotation. It compared 18 complete
256-dimensional GKLS propagations from the frozen independent builder
(both instruments in each of the author's nine parameter/time cases)
with the scalar spectral expression (5), implemented at 90 decimal
digits without using a two-dimensional matrix exponential.

The largest absolute full-matrix-versus-spectral energy discrepancy was
2.5366375666635577e-11; the largest full-matrix birth-probability discrepancy
was 5.10702591327572e-15. The largest difference from the author's recorded
full-matrix energy was 2.6716406864579767e-12. These floating checks are not
interval certificates.

All seven author high-precision joint-limit rows, S=1,2,4,8,16,32,64,
agree with the independently implemented spectral expressions within their
30-digit rounding. Twenty-five additional epsilon/time samples corroborate
the bounded scaled quantities in (6), including times close to zero.
Sampling is not the proof of uniformity; equations (1)--(6) provide that
argument. A control rejects replacing the slow rate by twice its value,
and another detects deleting the positive no-event energy term.

POST run 01 failed in its change of symbolic variable eta=epsilon²:
sequential substitution of epsilon⁴ first caused SymPy, using positive
epsilon but unrestricted eta, to introduce sqrt(eta²). The subsequent
coefficient extraction was therefore invalid. Run 02 converts the exact
even polynomial by its monomial degrees; it then derives (2) directly.
No source formula, scientific assumption, expected coefficient or tolerance
was changed. The failed runner and complete failure receipts are preserved.
A short diagnostic also wrongly declared its trial eigenvalue positive,
so solve correctly returned no negative root; that diagnostic failure is
recorded separately.

The new code, all rows, source bindings, logs and failure history are bound
by FINAL_COMPARISON_SEAL.json. This is an independent same-family
reconstruction and subsequent source comparison. It supplies no audit
status and no instruction to land, publish or extend the conclusions
beyond their explicitly supplied model and reservoir premises.
