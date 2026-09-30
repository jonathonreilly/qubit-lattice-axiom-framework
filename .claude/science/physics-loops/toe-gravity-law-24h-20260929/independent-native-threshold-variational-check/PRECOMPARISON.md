# Independent precomparison: compact four-particle dressing of a uniform pair pulse

Frozen before reading the new author's REPORT.md, check_word.py or word_results.
The contract was read and already discloses the proposed state, target factors,
source word and source amplitude. This is an independent derivation of its
mechanism and necessary limits, not a blind guess of that target. No author
implementation has been imported or run. Selected procedure is7146; observed
main is30a9461. The original deadline/STOP sentinel was checked before work.

## Inputs actually read and their scope

I read the entire landed NATIVE_QUBIT_PAIR_DENSITY_ONSET note at origin/main,
the actual native-stability model report, the complete previous N4 threshold
proof and its independent check, and the complete strict-positivity extension
and check. The previous independent interaction report was also reread; the
coercivity check was revisited, with its full proof in the landed source.
No novelty conclusion follows from this focused mathematical check.

The precise reused statements are: the full occupation-carrier SOS, H0>=0,
H0 Omega=H0 C_z^dagger Omega=0, uniform normalized pair Gram V I5,
the bounded nonnegative N4 translation-zero operator H4, compact F=H4 Phi,
and the finite affine threshold form

    T(z)=inf_(eta in l2) {E(Phi_z)+2Re<F_z,eta>+<eta,H4 eta>},
    Phi_z=(C_z^dagger)^2 Omega/sqrt2.

The checked strict-positivity proof makes the full 15-dimensional incoming
form positive for fixed mu,tau>0. It does not give an l2 minimizer, a bounded
zero inverse, an on-shell scattering matrix or a many-particle lower expansion.
The landed coercivity constant is c=min(tau,mu/12)/99090432.

## 1. Exact amplitude and the identical-pair factor

Choose C_z^dagger=sum_(x,A) z_A R_A(x)^dagger, where R=(QE1,QE2,
QT12/sqrt2,QT13/sqrt2,QT23/sqrt2), ||z||=1, and Y=C_z^dagger-C_z.
Let chi=sum_s chi_s |[S_s]> be finitely supported in physical N4 translation
orbits; choose one finite four-distinct-site representative per orbit. Define

    J_chi,L=(1/sqrt2) sum_(s,t in torus) chi_s product_(x in S_s+t)b_x^dagger,
    X_chi,L=J_chi,L-J_chi,L^dagger.

This is a finite-range anti-Hermitian operator on the original qubits. It
uses a trial-state preparation, not an alteration of H0 or a pair-boson law.
For sufficiently large L, let chi_L be its ordinary orbit lift. Then
X_chi,L Omega=chi_L/sqrt2, exactly. Put v=C_z^dagger Omega, w=(C_z^dagger)^2Omega.
The exact normalized state has second-order expansion

    exp(u^2 X) exp(uY)Omega
      =Omega+u v+u^2[w/2-V Omega/2+chi_L/sqrt2]+O_L(u^3).

Here ||v||^2=V and Y^2Omega=w-V Omega, from the literal hard-core action.
Since H0 kills Omega and v, its fourth-order energy coefficient is exactly

    <w/2+chi_L/sqrt2,H0(w/2+chi_L/sqrt2)>/V
      =(1/2) E_L(Phi_z+chi).

All apparent vacuum normalization terms and the first/third-order cross
terms vanish against H0; no extensive Taylor truncation is used as a state.
The leading number density is 2u^2. The factor 1/sqrt2 in J is essential;
using J Omega=chi_L would instead relax toward Phi+sqrt2 chi.

The number phase P=exp(i pi N/2) sends Y to -Y, X to X, fixes Omega and
commutes with H0,N. Hence the exact energy and number expectations are even
in u, also for complex z and chi. This removes fifth/third-order terms.

## 2. An explicit uniform remainder, without a cluster theorem

Write H0=sum_x h_x with support at most25 sites and ||h_x||<=h=182mu+240tau,
as proved in the actual source. Decompose Y by center; support size is at
most6 and each site belongs to6 centers. A safe center norm is
kY=2sqrt(32/3), from the squared coefficient-sum bounds 2,8/3,2,2,2
for the normalized R components. Thus kappaY=6kY bounds the sum of generator
term norms incident to any fixed site. For X, each four-site term has norm
|chi_s|/sqrt2, so kappaX=2sqrt2 sum_s|chi_s| is a safe weighted incidence bound.
This remains finite for every fixed compact chi, without uniformity in chi.

For G=X or Y put B_G(O)=[O,G]. A commutator chain only attaches terms meeting
the previous support. Each attachment costs at most2 kappaG times its
current support size and adds at most mG-1 sites (mX=4,mY=6). Consequently

    ||B_Y^a B_X^b H0|| <=V C_H(a,b),
    C_H(a,b)=h (2kappaX)^b (2kappaY)^a
        product_(j=0..b-1)(25+3j)
        product_(j=0..a-1)(25+3b+5j).

For N replace25 by1 and h by1 to define C_N(a,b). These count connected
sequences before summing them, not the support of a global commutator.
Bounds also allow repeated local terms and hold on all sufficiently large
tori with constants independent of L.

Consider f(u,v)=<Omega,e^(-uY)e^(-vX)O e^(vX)e^(uY)Omega>.
Taylor expand first in v through degree2, with third-order remainder;
then set v=u^2. For H0 expand its b=0 coefficient through degree5,
b=1 through degree3 and b=2 through degree1 in u. Unitary conjugation
preserves the commutator norm bounds at every remainder point. Parity and
H0 Omega=H0 v=0 give

    |<H0>/V-(1/2)E_L(Phi+chi)u^4| <=K_H(chi)|u|^6,
    K_H=C_H(6,0)/720+C_H(4,1)/24+C_H(2,2)/4+C_H(0,3)/6.

For N, expanding first in v through degree1 and then using its evenness gives

    |<N>/V-2u^2| <=K_N(chi)u^4,
    K_N=C_N(4,0)/24+C_N(2,1)/2+C_N(0,2)/2.

In particular <[N,X]>_Omega=0 because X changes number by four. This proof
has no V u^2<<1 assumption and needs no infinite-volume unitary in the vacuum
Fock representation. The bounded finite-volume unitaries are the actual trials.
The displayed constants are conservative; their correctness, not sharpness,
is the obligation when comparing with the author's later proof.

## 3. Orbit normalization and eventual finite-volume equality

Compact physical four-site shapes have no infinite-lattice translation
stabilizer. If all relevant compact shapes have coordinate span at most D,
L>4D is a conservative sufficient exclusion of torus stabilizers: a torus
translation preserving four sites has order at most4; any nonzero coordinate
shift then has circular magnitude at least L/4, whereas the points' differences
have magnitude at most D. Anchoring at one point also shows that distinct
compact translation shapes cannot merge after periodization once their
relative-coordinate boxes embed injectively. The cutoff D must include
H's finite transition range, chi, and the compact source/row defect support.

The general incoming Phi contains far-separated shapes, including possible
finite-torus exchange stabilizers. It would be wrong to assert every N4
torus orbit has size V. Their energy contribution is instead controlled by
the actual SOS: outside a finite contact neighborhood, each row kills the
complete zero-energy pair factors. Only a compact relative set contributes
to E(Phi). The previously checked connected-support proof of the bare quartic
is one way to make this exact. Cross terms use compact F=H Phi; chi-H-chi
uses finite transition range. Thus for each fixed compact chi, all these
terms agree exactly with the infinite orbit form for sufficiently large L.
No finite-torus zero-energy inverse is introduced.

## 4. Compact corrections approximate the infimum

For eta,eta' in l2, boundedness ||H4||<=C gives

 |E(Phi+eta)-E(Phi+eta')|
 <=[2||F||+C(||eta||+||eta'||)]||eta-eta'||.

Finite orbit-support vectors are dense. First choose an l2 approximate
minimizer for the defining infimum (or a fixed negative-energy resolvent
correction), then truncate it. This gives compact chi with E(Phi+chi)<=T(z)+delta
for any delta>0. It requires neither an l2 zero-energy limit nor a compact
exact minimizer. Its constants/support may grow when delta decreases.

## 5. Ordered upper limit and coherent-channel lower coefficient

For fixed z and compact chi write tchi=E(Phi_z+chi)>0. The exact trials give

    <H0-nu N>/V=(tchi/2)u^4-2nu u^2+O_chi(u^6+nu u^4).

Choosing u^2=2nu/tchi yields -2nu^2/tchi+O_chi(nu^3), uniformly for all
L>=Lchi. First take limsup_L, then limsup_(nu down0), then improve the fixed
compact correction delta down0. Finally minimize over unit z. Continuity
and positive definiteness of the finite incoming form imply a positive
minimum on this compact coherent subset, giving the proposed -2/min_zT(z).
No assertion is made about replacing this coherent minimum by the smallest
eigenvalue on all15 incoming components.

The same exact trial and the LANDED coercivity inequality give, for every
fixed chi, after L->infinity and only then u->0,

    tchi/2 >=4c, hence T(z)>=8c for ||z||=1.

At fixed L the negative term -2c rho/V prevents extracting this coefficient;
reversing these limits would be invalid. This bound is only on coherent
incoming z tensor z. It does not automatically prove the operator inequality
T0>=8c I on all Sym^2 C5. It is consistent with the universal lower grand
energy -nu^2/(4c) and the proposed upper bound.

## 6. Independent prediction for the concrete word

For S={0,(3,-1,1),(3,1,1),(6,0,0)}, only the middle y-axis pair is a G edge.
The two outer vertices have degree0 and the middle vertices degree1, so
V3(S)=0. Its axial E projector diagonal is2/3. Its annihilation-amplitude
sequence is supported at one center and has squared norm2/3; summing three
positive gradient directions multiplies by6. Therefore

    H_SS=(8/3)mu+4tau=4(2mu+3tau)/3=:d.

All twelve oriented nonzero differences between its points are distinct.
Any translation preserving two points would repeat such a difference, so
no nonzero translated copy can be connected back by a two-body transition.
Thus the translation-zero orbit diagonal is also d, not an unexamined
sum of same-orbit hopping matrix elements.

The source in the contract can also be reconstructed: remove its only
middle y pair, translate its center down one z step, and create the x pair.
The axial E projector cross element is -1/3; W contributes -tau, giving
tau/3. The returned straight four-site chain has one E1 matching of amplitude
one in (C_E1^dagger)^2Omega. Other available returned words have zero incoming
matching amplitude. Thus F_Phi(S)=tau/(3sqrt2).

Take chi=-(F_Phi(S)/d)|[S]>. Its affine threshold energy drops by
|F_Phi(S)|^2/d=tau^2/(18d), so the actual dressed pulse quartic coefficient
is predicted to be

    52mu+120tau-tau^2/[48(2mu+3tau)].

The quartet-creation coefficient in X is -tau/(6d). This is an exact
single-orbit variational improvement, not a threshold-inverse evaluation.
A small independent occupation-action control should test d, same-orbit
hops, source matching and the factor before final comparison.

## Remaining checks before conclusion

The later author proof must realize the indicated quartet amplitude, give
legitimate mixed-commutator rather than global-norm bounds, keep finite-torus
stabilizers separate from the compact support, and use the stated ordered
limits. I have not read that proof or its code/results at this freeze. The
mechanism appears valid under the reused threshold inputs; any mismatch or
unproved compact-support/normalization assertion will remain an explicit gap.
No matching lower equation of state, fixed-N dilute limit, condensate,
scattering cross section, tensor mode or physical record claim follows.
