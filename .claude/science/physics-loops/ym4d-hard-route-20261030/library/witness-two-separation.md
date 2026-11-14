# A two-separation NT1 criterion without a full Gaussian limit

Author: openai/gpt-6-astra/max mac-mini-codex, 2026-11-01.
Pinned source: `5f5f1693a60cfcb7aff5ccd1534f626294a37188`.
Status: discharged probability identities and static-law test; implication
for NT1 with explicit, presently unproved Wilson inputs. Author work only.
No numerical computation or literature lemma is used.

## 1. Kill the soft version first [discharged]

Let Z be any nonconstant bounded real random variable and put X(x)=Z at
every Euclidean point. Translation and reflection act identically, so
E[(Theta F) F]=E|F(Z)|^2>=0. Its OS space is L^2(law(Z)), its translations
are the identity and H=0. Every connected two-point function of X is
Var(Z)>0, independent of separation. Holder's inequality gives the usual
chessboard upper bound for functions of this one variable. Neither that
bound nor non-strict reflection-positive monotonicity supplies strictness.

More precisely, under H-NET a centred reflected self-correlator is

    C_F(t)=<f,exp(-tH)f>=int_[0,infinity) exp(-t lambda) d rho_f(lambda).

For t2>t1>=0 its difference is the integral of
exp(-t1 lambda)(1-exp(-(t2-t1)lambda)), strictly positive exactly when
rho_f((0,infinity))>0. Thus proving *strict* monotonicity would already
prove the dynamical content on this vector; RP alone permits rho_f at zero.
For two different vectors, or with an extra spatial translation, no such
positive-measure monotonicity is asserted.

The interface's DEC is a bound on E|Cov_W(F,G)|, not on Cov_mu(F,G).
In the static example choose the coarse field W to reveal Z in every read
cube. Then every conditional covariance is zero, as are SCR comparisons
between conditionally independent coarse fields agreeing on a read cube.
The unconditional covariance is still Var(Z). This refutes the inference
from those conditional inequalities and RP alone; it is not a model of all
Wilson/LOC/FILL/OS clauses, nor a counterexample to Yang--Mills.

## 2. Near--far theorem [implication; elementary proof discharged]

The minimal observable input read by Theorem 4.1 is just
c(y_n)!=c(y_f). There is no uniquely weakest list of producer estimates:
different sufficient estimates need not imply one another. The criterion
below is one quantitative route to that input, not a claim of optimality.

Use exactly one map, its source-free hierarchy, and the law and geometry
conventions of upper-chain **The interface**. Fix Theta first. Take
j_i=K_i-m at one fixed physical scale, and assume the part of H-SCALE
gamma_(j_i,i)->gamma_m>0 and a_(j_i,i)->r_m>0, together with H-NET for
the observables below. Write nu'_i for the actual level-(j_i+1) marginal,
nu_i=nu'_i P_(j_i); these belong to LL as stipulated in that interface.
All estimates below concern these actual laws, not a law conditioned on a
rare event. No assertion for every law in LL is needed by this theorem.

Let A_i,B_i be two real bounded local observables at level j_i, uniformly
bounded in i, and let B_(y,i)=tau_y B_i. For example take energies divided
by gamma_(j_i,i)^2; at this fixed m these are still uniformly bounded
sequences. Choose two offsets y_n,y_f=y_n+t e4, t>0 in physical units,
whose supports are strictly ordered along all axes. Define

    a_i(W)=E_W A_i,        b_(y,i)(W)=E_W B_(y,i),
    n_i=E_nu'_i Cov_W(A_i,B_(y_n,i)),
    v_(y,i)=sqrt(Var_nu'_i(a_i) Var_nu'_i(b_(y,i))).          (NF-1)

The far configuration must fit DEC *as printed*: for an admissible
m_f with r_(j+1)<=m_f<=M_(j+1), both supports fit cubes of radii
n<=floor(m_f L/2), centre distance is at least 4m_f L, and the prescribed
nonwrapping shells and thickness D>=28w_0 fit. Put

    d_i=C(Theta)||A_i||_(L4(nu_i))||B_(y_f,i)||_(L4(nu_i))
                         tau_(j_i)(m_f)^theta.             (NF-2)

Assume this instance of DEC and the single quantitative inequality

    liminf_i [n_i-v_(y_n,i)-v_(y_f,i)-d_i] > 0.             (NF-3)

Then the limiting connected correlators at y_n and y_f are unequal and
NT1 holds. A sufficient supplier version is n_i>=a-o(1),
v_(y_n,i),v_(y_f,i)<=v+o(1), d_i<=d+o(1), with **a>2v+d**.
This needs one lower bound on a conditional *separated* covariance and a
small oscillation of its conditional means. A one-site variance is not a
substitute for that lower bound (independent-site noise has such variance).

Proof. The tower identity gives, exactly,

    Cov_nu_i(A_i,B_(y,i))
      =E_nu'_i Cov_W(A_i,B_(y,i))+Cov_nu'_i(a_i,b_(y,i)).   (NF-4)

Cauchy--Schwarz bounds the absolute value of the last term by v_(y,i).
Consequently c_i(y_n)>=n_i-v_(y_n,i), whereas DEC gives
c_i(y_f)<=d_i+v_(y_f,i). Subtract and use (NF-3). H-NET passes the two
ordered correlators to the same limit. Theorem 4.1, with its reflection
and mollification argument, then gives H nonzero on Omega-perp. If the
observables were normalized energies, multiplying back by the common
positive gamma_m^4 preserves the strict difference. No m->infinity
exchange, Gaussian law, vertex or sixth moment occurs in this proof. []

**Static test, including an imperfect coarse variable [discharged].** For
A_i=B_(y,i)=Z, n_i=E Var(Z|W) is the same at both separations, so any
valid DEC bound has d_i>=n_i. Also v_(y,i)=Var(E[Z|W])>=0. Hence the
left side of (NF-3) is nonpositive for every choice of W. The test cannot
mistake a static random law for dynamics.

## 3. A possible near input needs only a quartic pair [implication]

This paragraph identifies a smaller possible supplier for NF-3; it does
not assert that the supplier has been delivered. On the OS regular event
let X_p=s_p/gamma_j^2 and Q_p=|phi_p+b_p|^2/8, with b conditionally centred
Gaussian of covariance Gamma(W). Suppose the actual conditional means
and conditional pair covariance have the following integrated errors,
including G^c and the pullback/chart failures:

    ||E_W X_p-E_b Q_p||_(L2(nu'))<=epsilon,
    |E_nu' Cov_W(X_p,X_q)-E_nu' Cov_b(Q_p,Q_q)|<=epsilon.   (PAIR4)

One may define phi=Gamma=0 off G; PAIR4 must then include that loss.
Only these finitely many energy tests are asked for. Their degree in b
is at most four. Gaussian integration by parts gives

    E_b Q_p=(|phi_p|^2+Tr Gamma_pp)/8,
    Cov_b(Q_p,Q_q)=||Gamma_pq||_HS^2/32
                         +phi_p^T Gamma_pq phi_q/16.        (NF-5)

For completeness the quadratic--quadratic contractions are the two cross
pairings, giving 2||Gamma_pq||_HS^2; the linear--linear contraction is
4 phi_p^T Gamma_pq phi_q; odd terms vanish. Division by 64 gives NF-5.

If on G, ||Gamma_pq||_op<=B, E||Gamma_pq||_HS^2>=h^2, and
E|phi_p||phi_q|<=u, then n_i>=h^2/32-Bu/16-epsilon. For any constant
v_p^0, the standard deviation of E_W X_p is at most

    k_p=(1/8)|| |phi_p|^2 ||_2
          +(1/8)||Tr Gamma_pp-v_p^0||_2+epsilon.             (NF-6)

Thus v_(y,i)<=k_p k_q. This follows by bounding variance by the squared
distance to the constant v_p^0/8 and applying the triangle inequality.
These are usable finite inequalities, not an assertion that their right
sides have the desired relative size.

**Supplier map / stop [gap for Wilson].** DEC is the existing named
clause. OS(b), OS(c) restricted to the needed degree-four tests, OS(d)'s
traces/norms, FF with Lemma 10.6, and suitable pullback/chart moments are
candidates for PAIR4 and NF-6. Their use requires uniform integrability
for BOTH the actual and replacement laws and bounded chart-test
coefficients. No covariance orientation is required in NF-5: its signed
mean term was bounded in absolute value. No COV8 or completed polynomial
transfer contraction is read.

What has not been proved is **NF-3 for the Wilson trajectory**, including
a nonzero uniformly controlled near fibre covariance and sufficiently
small conditional-mean oscillation. In particular a bound written only
C(L)L^(-2 kappa) does not become small by increasing L without control of
C(L). DEC also need not become arbitrarily small in the ultraviolet at
one fixed separation: its x_j^P prefactor and its admissible radii must be
checked at the chosen fixed physical scale. No clustering claim follows
by dropping the second term of NF-4. The exact residual is a>2v+d (or
NF-3), strictly weaker in requested information than a full local Gaussian
limit, but still an unproved quantitative input. This is an honest stop
for this route, not a no-go theorem about other NT1 arguments.
