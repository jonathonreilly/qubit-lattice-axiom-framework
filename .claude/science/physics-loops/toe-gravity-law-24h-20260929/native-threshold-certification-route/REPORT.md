# Full-channel compact threshold bounds and an uninformative dual lift

Authored provisional calculations and proof, not independently checked or
formally reviewed. The supplied benchmark is mu=tau=1 in the actual native
qubit Hamiltonian. No physical value is fitted or selected. The full threshold
form remains unevaluated; these are compact variational upper bounds.

The new finite construction lowers the normalized E1 identical-pair threshold
upper from344 to206.4408418656 and T12 from420 to260.7505245002. It supplies
an exact rational upper matrix in all15 holomorphic quadratic channels, not
only those two directions. A natural dual residual lift is valid at the stated
operator hypotheses but too loose here to produce useful matching bounds.
Its failure and an uncertified Fourier diagnostic are preserved below. No
channel ordering, full interaction anisotropy, equation of state or phase is
inferred from different upper bounds.

## 1. Actual inputs and normalization

Use the main native H0 law at30a9461, with separately supplied positive mu,tau,
qubit number, pair operators, stabilizer and clock. The complete source and
transitive construction were read in the continuing campaign. Provisional
native-scattering-route/REPORT.md supplies the focused-checked infinite
translation-fiber threshold construction, not a retained status. The actual
N4 operator is bounded positive with H<=16mu+144tau. Its exact one-pair
removal identity is H=mu D+T* K2 T, D>=1 on configurations with no perfect
G-matching. The independent channel check verifies this graph fact. For a
physical finite four-site configuration there is no nonzero translation
stabilizer, so its infinite K=0 orbit basis has norm one. No finite-torus
orbit isometry is used.

Raw pair coordinates are x=(u1,u2,v12,v13,v23), u3=-u1-u2. The physical
single-pair norm is

    s=|u1|²+|u2|²+|u1+u2|²+2 sum|vij|².

For an axial edge with displacement plus/minus2ei set w=ui, and for a
diagonal edge si ei+sj ej set w=-si sj vij. The pulse incoming amplitude on
an unordered four-site word S={a,b,c,d} is the matching polynomial

    phi_x(S)=w(a,b)w(c,d)+w(a,c)w(b,d)+w(a,d)w(b,c).

It is C(x)^2 Omega/2. The normalized identical-pair threshold convention uses
Phi_x=sqrt(2)phi_x; hence its quadratic form is TWICE the pulse energy, at
s=1. The ordered raw monomials (i,j), i<=j, are recorded in CORE_RESULTS.
The earlier independently reconstructed225+225 bare matrices give

    <phi_x,H phi_x> = p(x)* B12 p(x)/12,

where B12 is their sum at the stated benchmark. This is a finite source
pairing although phi_x itself is a generalized constant incoming profile.
All affine compact corrections below have the same prescribed asymptotic
incoming amplitude as the checked threshold variational definition.

For the orthonormal five-coordinate frame z, use
u1=z1/sqrt(2)+z2/sqrt(6), u2=-z1/sqrt(2)+z2/sqrt(6),
and (v12,v13,v23)=(z3,z4,z5)/sqrt(2). If q(z) has entries z_i² and
sqrt(2)z_i z_j for i<j, the explicitly implemented matrix P satisfies
p(x)=P q(z). A raw pulse upper matrix Q therefore means

    0 < T0 <= 2 P* Q P.

Strict positivity is inherited from the previously independently checked
threshold proof, not established by floating eigenvalues in this packet.

## 2. Connected-core rational trial

Enumerate every connected four-site set in the graph with18 displacements
plus/minus2ei, plus/minus ei plus/minus ej, quotienting by translations only.
Exactly1487 of these have a perfect matching. This is a compact support for
trial corrections; it is not the full Hilbert space or a closed dynamics.
The literal main-law action has integer coefficients for12H. The source
matrix on these rows is F12(S,I)=sum_T (12H)_(S,T)phi_I(T), retaining every
actual output word before restricting the source row.

A12 is the compression of12H to this connected core. Its exact integer
matrix is symmetric. A floating sparse solve proposes X=-A12^-1 F12.
This solve and its residual are diagnostics only. Round every entry to the
specified rational trial Xi/65536. The upper matrix is then evaluated with
exact integer arithmetic:

    Qcore = [65536² B12 + Xi* A12 Xi
                    +65536(F12*Xi+Xi*F12)]/(12*65536²).

Every intermediate int64 product has a checked worst-case bound below2^63;
the largest displayed N*rowL1*maxXi² bound is6,658,022,361,689,856.
No accuracy or condition-number hypothesis about the sparse solve is needed:
any such compact trial gives an upper bound by the variational definition.
The artifact CORE_TRIAL.npz includes core configurations, all sparse A12
entries, F12, Xi and its denominator. CORE_RESULTS.json records the entire
exact rational matrix, together with explicitly diagnostic frame eigenvalues.

This trial gives normalized E1 upper458127122491/2147483648 and T12
upper1178131184533/4294967296. Its useful reduction is not the tiny residual
of a finite sampled torus equation; it is the energy of a literal compact
infinite-lattice wave correction.

## 3. Complete compact source, not a row-restricted residual

To compute the full residual without enumerating a large N4 box, use the
local positive decomposition already used for the exact bare quartic.
For a removed physical pair (a,b) at center x and residual pair (c,d),
the annihilated incoming profile is w(a,b)w(c,d) plus the two crossed
matchings when all sites are distinct, and zero on overlaps. Subtract the
constant background w(a,b)w(c,d). This leaves only

    -w(a,b)w(c,d) on an overlap,
    w(a,c)w(b,d)+w(a,d)w(b,c) otherwise.

The latter is supported only when the two crossed graph edges exist. This
is a finite, exhaustive list of local defects. There are three axial types
and twelve signed plane types at each center. Denote their signed defect
vectors by d_i(x;eta). On axes the onsite positive form has coefficients
(2/3) times the all-ones matrix. In each four-entry plane the onsite form is
I-(1/4)11*, equivalently(1/4)sum_(i<j)|d_i-d_j|². The gradient form has
axis projector I-(1/3)11* and plane projector(1/4)11*, applied to forward
center differences. Constant backgrounds are killed by each relevant onsite
or gradient form.

Thus the exact source12Hphi can be produced by creating each actual pair
back onto its residual, skipping occupied-site collisions. On axes its mu
coefficient is8 sum_i d_i, and on each plane it is3(4d_i-sum_j d_j).
Writing l_i=6d_i(0)-sum_(six neighbors)d_i(e), its tau coefficients are
12l_i-4sum_j l_j on axes and3sum_j l_j on a plane. Multiply the creation
by its original sign. The remaining positive D term is generated by each
rooted three-neighbor star, with coefficient12phi; for perfect-matching
four-site configurations D is exactly the number of occupied degree-three
roots. On all nonmatching configurations phi=0. Translation-canonicalizing
these finitely many contributions gives the full compact source.

complete_source.py implements precisely these formulas using the disclosed
previous author polynomial geometry. It finds29,907 source configurations,
maximal coordinate span6, with5,481 nonzero mu rows and29,907 tau rows.
The computed source reproduces every one of the225 mu and225 tau bare-energy
coefficients and every1487x15 direct core source entry. SOURCE_RESULTS.json's
field named residual_pair_keys inadvertently repeats the source-row count;
that field is not used or claimed as a residual-pair count. Full source data
are in COMPLETE_SOURCE.npz. An initial missing __file__ setup error is
preserved; no mathematical assertion failed in the corrected run.

## 4. A full-residual norm step

Let chi be the rational core trial and r=Hphi+Hchi on the full actual N4
space. Reapply the literal operator to every core-supported correction word,
without dropping exterior or nonmatching outputs. The residual has35,430
configuration rows. Its exact common denominator is786432; its numerator
matrix and all configurations are saved in RESIDUAL.npz. The full residual
Gram is evaluated with arbitrary-size integers to avoid overflow.

At this benchmark H<=160. The compact correction chi-r/160 has energy

    E(chi-r/160)=E(chi)-||r||²/80+<r,Hr>/25600
                        <=E(chi)-||r||²/160.

This holds simultaneously for every channel vector, hence as a matrix upper
bound. RESIDUAL_RESULTS.json records the full rational improved pulse matrix
with denominator98,956,046,499,840. The resulting normalized threshold bounds
are exactly

    T0(E1,E1) <=5107142386779523/24739011624960,
    T0(T12,T12)<=358372792045843/1374389534720.

Their decimal displays are206.44084186559658 and260.75052450021246. These
are energy inequalities; the local correction remains compact. No inference
about T0 eigenvectors or its exact entries is made.

## 5. Dual lift and why this attempt does not give a matching answer

For any compact residual r, separate its perfect-matching and nonmatching
components. For a perfect-matching word S with m perfect matchings, place
r(S)/(2m) on each ordered removal into a residual G edge and a removed G
edge. Identify both edges by their actual orthonormal nine bond types and
relative anchor. Distinct ordered removals of an infinite orbit are distinct
coordinates; otherwise a finite configuration would have a nonzero translation
stabilizer. The adjoint physical removal map sums the2m coordinates and so
T*g=r_P exactly. Put q=r_Q on the nonmatching configurations.

Cauchy-Schwarz in the positive form H=mu D+T*K2 T gives

    |<r,psi>|² <= [sum_Q |q(S)|²/(mu D(S))
                         +<g,K2^-1g>] <psi,Hpsi>.

The second term is a compact-source Green quadratic form, not a globally
bounded inverse. It is finite by the checked symbol inequality
K2(q)>=min(tau,mu/6)ell(q)I9 and three-dimensional integrability of1/ell.
The variational dual definition then bounds <r,G_Hr> by the bracket and
would give a lower bracket on E(chi). Optimizing over every possible lift
would be a reformulation of the original inverse problem, not its solution.

The direct equal-distribution lift was checked exactly for both normalized
coherent directions:2,127/1,891 perfect rows,4,308/3,868 coordinates, and
all adjoint sums exact. Its nonmatching cost is already167.3524559389(E1)
and168.1675151011(T12). The rigorous scalar-Green/l1 upper estimate, using
g0<=sqrt(3)pi/8 and min(tau,mu/6)=1/6, costs126,464 and280,249. It is far
too loose to improve the previously proved positive lower bound.

To price whether replacing only that Green estimate would help, an explicitly
uncertified Fourier diagnostic evaluates the actual9-channel K2 inverse on
32³ and48³ grids, dropping the singular soft q=0 contribution. It gives
total dual costs779.97 then832.92(E1), and711.38 then749.62(T12). These are
not certified upper/lower integrals or a proven convergence sequence. They
suggest that this particular lift is itself inefficient; no rigorous negative
claim rests on those samples. The rigorous coarse inequality alone is already
uninformative. No further grid refinement is justified before a better lift
or a substantially different lower-bound mechanism.

## 6. Actual execution and limits

The initial core solve/exact trial used9.247934 CPU seconds,9.431800 wall,
64,389,120 peak RSS. Full source used6.199753 CPU seconds,6.207185 wall,
106,823,680 bytes. Full residual used7.011946 CPU seconds,7.027351 wall,
79,691,776 bytes. Dual lift used1.203755 CPU seconds,1.204479 wall,
49,299,456 bytes. All were single-thread bounded scripts with deadline/STOP
checks and declared envelopes.

An initial32³/64³ Green diagnostic exceeded its200MB envelope at the final
RSS assertion. Exact resources were not printed and no result file was
written; the code/contract and failure disclosure are preserved in history.
The reduced32³/48³ run used2.097926 CPU seconds,2.101404 runner wall,
186,384,384 runner peak RSS; the external envelope reports2.21seconds and
186,400,768 bytes. It is explicitly a diagnostic resource correction, not an
unrecorded successful first run. This optional diagnostic is not evidence for
the exact rational upper matrices.

The exact constructions still require focused independent checking before
high-fanout reuse or milestone inclusion. No formal review, audit, main change
or PR is claimed. Source Hamiltonian, carrier, time, vacuum and couplings
remain supplied. The full15 threshold form, its coherent minimizer, a matching
many-body lower functional, EOS, phase and any physical identification remain
open. Useful next work is a genuinely sharper physical dual/comparison
mechanism, not treating the compact trial as the full scattering answer.
