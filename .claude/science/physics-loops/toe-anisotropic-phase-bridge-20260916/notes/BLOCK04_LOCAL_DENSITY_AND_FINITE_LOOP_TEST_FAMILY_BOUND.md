# A volume-uniform local density bound and the limit of finite loop tests

Working bounded derivation, 2026-09-16. This supplies a quantitative local
ground-density estimate for the supplied pure compact rotor Hamiltonian and
a restriction on one variational proof method. It does not bound the full
electric susceptibility from above, exclude a Coulomb phase, or force an
axiom update. All coupling constants here are fixed and positive.

## 1. A local comparison that survives large volume

Work first on the full link-angle torus with normalized product Haar measure,

    H=-(g^2/2)sum_e partial_e^2
                     +(1/g^2)sum_p(1-cos F_p).

Its strictly positive normalized ground wavefunction Psi is gauge invariant:
the unique positive ground vector is carried to itself by every vertex gauge
transformation. Thus this is the same physical ground state as in BLOCK02-03.

Take a finite set S of links. Let n(S) count the plaquettes touching S. Split
the potential into V_out, containing all other plaquettes, and W, containing
these n(S) plaquettes. Then

    0<=W<=2 n(S)/g^2=:w_S.

The independent-link heat semigroup on S has kernel

    K_t(theta_S,phi_S)=product_(e in S) k_t(theta_e-phi_e),
    k_t(x)=sum_(n in Z) exp(-g^2 t n^2/2) exp(i n x), t>0.

Let k_min,k_max be the positive minimum and maximum of this circle heat
kernel. Feynman-Kac, with the interaction W bounded along each path, gives
the pointwise positive-kernel sandwich

    exp(-t w_S) K_t tensor exp[-t(H_out)]
       <=exp(-tH)<=K_t tensor exp[-t(H_out)].         (1)

Here H_out includes the outside link kinetic terms and V_out. Applying (1)
to Psi and using exp(-tH)Psi=exp(-tE0)Psi gives, for any two configurations
x,y of S and the same configuration z of all remaining links,

    Psi(x,z)/Psi(y,z)
       <= R_S(t):=exp(t w_S)(k_max/k_min)^|S|.        (2)

Indeed, after applying the outside semigroup, the same positive function of
the S endpoint appears in the two integrals; its integral cancels between
the heat-kernel maximum and minimum bounds. The possibly extensive ground
energy also cancels. This is why (2) contains no volume factor.

For p=Psi^2, the conditional density of S given z, relative to normalized
Haar measure on S, consequently satisfies

    R_S(t)^(-2)<=p(theta_S | z)<=R_S(t)^2.           (3)

The constants are crude but explicit and depend only on g,t and the local
set S. A useful elementary positive bound is obtained from the wrapped
Gaussian and a decreasing Gaussian sum:

    k_min>=sqrt(2pi)/(g sqrt(t)) exp[-pi^2/(2g^2 t)],
    k_max<=1+sqrt(2pi)/(g sqrt(t)).                  (4)

The first keeps one nearest lift with distance at most pi; the second uses
1+2 sum_(n>=1)exp(-g^2 t n^2/2)<=1+2 integral_0^infinity
exp(-g^2 t x^2/2)dx. Thus no unstated strictly-positive constant is needed.
Equation (3) is a local conditional comparison, not a uniform bound on the
full many-link density, and does not imply uniqueness, clustering or a gap.

## 2. Single-plaquette sine tests cannot provide the infrared certificate

For B_h=sum_p h_p sin F_p, its link derivative is

    partial_e B_h=sum_(p containing e) C_pe h_p cos F_p.

In a free three-dimensional cubic box, at most four plaquettes contain one
link. Their combined support S_e has at most 13 links and touches at most
52 plaquettes. Define, for any fixed t>0,

    c_g(t)=exp(-208t/g^2)(k_min/k_max)^26>0.          (5)

By (3), the conditional mean of |partial_e B_h|^2 is at least c_g(t) times
its Haar mean over S_e. Distinct unoriented elementary plaquette characters
are Haar orthogonal, and their cosine squared mean is 1/2. Therefore

    <|gradient B_h|^2>_p
       >=(c_g(t)/2)sum_e sum_(p containing e) h_p^2
       =2 c_g(t) sum_p h_p^2.                       (6)

No cube constraint was dropped: it relates products of characters and does
not identify any two distinct elementary plaquette characters. Thus the
matrix M in BLOCK03 satisfies the volume-uniform positive bound

    M>=2c_g(t) I.

Let eta_sine(f) be the *best lower bound* on eta_f obtainable by varying h
in this sine family. Since m_p=<cos F_p> lies in (0,1],

    eta_sine(f)=ell* M^(-1)ell/|f|^2
       <=|Cf|^2/[2c_g(t)|f|^2].                     (7)

For any sequence with |Cf_L|/|f_L| tending to zero, eta_sine(f_L) therefore
tends to zero at every fixed g>0. The coefficients h may depend arbitrarily
on the volume and the test vector; optimization over all of them is already
included. This rules out obtaining a positive constant eta_* using only
these observables and inequality (5) of BLOCK03.

Crucially, the logical direction is

    eta_f >= eta_sine(f),   eta_sine(f)<=a vanishing bound.

These two inequalities give no vanishing upper bound on eta_f. The exact
susceptibility may remain positive. The result is a restriction on the test
family, not a statement that interactions become weak or that the physical
model is massive. At small g the constant in (5) is extremely small, so the
bound need not be numerically informative at moderate wavelengths.

## 3. Extension to a fixed finite collection of bounded loops

Choose finitely many local integer cycle templates and their translations,
with uniformly bounded support. Keep one representative for each character
up to sign, omitting zero cycles. Denote their link cycles by a_alpha, choose
local integer plaquette fillings b_alpha with a_alpha=C*b_alpha, and take
B=sum_alpha h_alpha sin(a_alpha dot theta). Repetitions would make its Gram
matrix singular for a purely representational reason and are removed here.

For each link e, the union of all selected loop supports touching e is
contained in a uniformly bounded local set. Applying (3) there supplies a
constant c_(g,templates)>0 independent of the large box. Haar orthogonality
of the distinct characters then gives

    <|gradient B|^2>_p
       >=(c_(g,templates)/2)sum_alpha |a_alpha|^2 h_alpha^2.

Meanwhile J_alpha=(f,a_alpha)mu_(a_alpha), with |mu|<=1, and

    (f,a_alpha)^2=(Cf,b_alpha)^2
       <=|b_alpha|_1 sum_p |b_alpha,p| (Cf)_p^2.

Set

    K_templates=max_p sum_alpha
         |b_alpha|_1 |b_alpha,p|/|a_alpha|^2.

Bounded translated templates and their local fillings make K_templates
finite independently of volume, including near a free boundary when only
loops and fillings inside the box are retained. Optimizing the resulting
diagonal quadratic upper bound gives

    eta_templates(f)
       <=[2 K_templates/c_(g,templates)] |Cf|^2/|f|^2. (8)

Thus no fixed such finite template collection supplies a uniform infrared
certificate by this route. Larger loops, an increasing family of harmonics,
nonlinear observables with growing support, or a different proof inequality
remain available. Constants in (8) are allowed to deteriorate when the
template family itself grows; exchanging those limits is not justified.

## 4. Consequence for the campaign

The local conditional comparison is useful on its own and does not require
a presumed weak-coupling phase. Its application explains why finite small-loop
tests can look successful in a small box yet fail to settle arbitrarily long
wavelengths. The next construction must resolve how extended physical loops
or a nonlinear phase corrector retain response in the actual fixed-g state.
The ground-state phase, matter bridge and native model selection remain open.
