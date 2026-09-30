# Focused precomparison: actual all-N native pair structure

Root reconstruction before reading native-dilute-phase-route/REPORT.md, its
runner or results. Exposure: author CONTRACT and concise proposed results;
previous complete source/model and earlier independent threshold work. Thus
not an undisclosed-target check. Same landed30a9461 model, all original M2
hard-core occupations, no auxiliary pair bosons. Formal review not claimed.

Let Delta be the18 length-two cubic neighbor vectors, m_x their occupied
count, D=sum n_x(m_x-1)(m_x-2)/2, V3/mu=sum n_x binom(m_x,2). Egrad is the
sum of all15 literal bare-pair nearest-center gradient norms. Current SOS
provides H0>=mu D+a Egrad, a=min(tau,mu/12).

## Independent averaged pin derivation

For each ordered occupied triple x,x+d,x+e, d!=e inDelta, represent the
pair(x,x+d) by its literal bare monomial B_t(c). An axial edge has one such
representation, a diagonal edge has two; average uniformly over them, instead
of selecting the author's undisclosed convention. Signs on v do not affect
norms. With y=x+e, n_y B_t(c+e)=0 exactly, whereas n_y commutes with B_t(c).
Along each shortest two-step center path c,c+s,c+e, Cauchy gives

 n_x n_(x+d) n_y expectation
 <=2 sum_(two steps) ||n_y Delta_step B_t psi||^2
 <=2 sum_(two steps) ||Delta_step B_t psi||^2.

Average uniformly over the two shortest paths when e is diagonal. Summing
V3/mu=(1/2)sum_orderedtriples cancels the factor2. Translation ofx maps each
step to the complete sum over centers. For a fixed bare axial pair and
coordinatej, the two choices of its endpoint asx give multiplicity
2*(12-|d_j|)=24-4*1_(j=axis). For a fixed diagonal bare pair, representation
weight1/2 gives12-|d_j|<=12. Here sum_(e inDelta)|e_j|=12; excluding e=d
subtracts|d_j|. Positive/negative directed gradients give the same center sum.
Therefore V3<=24mu Egrad. This proof uses an averaged representation/path
and is independent of any finite matrix certificate.

## Defect count and absolute gaps

Let O count particles outside isolated two-vertex components of the induced
Delta occupation graph. Isolated vertices are bounded byD. In components
ofsize>=3 every degree-one vertex has a degree>=2 neighbor. Their number is
at most sum_(degree>=2)degree <=2sum_x binom(m_x,2). The number of nonleaves
is at most that same binomial sum. Thus O<=D+3V3/mu<=D+72Egrad<=72H0/a.
No component-size-independent phase assumption was used. Since N-O is even,
oddN hasO>=1. On the even-N complement of the isolated-dimer configuration
space, O>=2. These give an odd-sector absolute bounda/72 and an even
COMPRESSION bounda/36; that complement need not be invariant underH0, and
neither is an excitation gap over a finite-density ground energy.

## Actual pair correlations

Use R=(QE1,QE2,QT12/sqrt2,QT13/sqrt2,QT23/sqrt2).
The exact energy identity is H0=mu N-2mu sum R*R+V3+W. Hence
C(0)>=rho/2-e/(2mu). Translation-AVERAGED, not necessarily invariant,
Re C(r)=C(0)-(1/(2V))sum_x,A ||(R_A(x+r)-R_A(x))psi||^2.
A path ofl=|r|_1 steps bounds the last term by l^2 e/(2tau), because the
normalized R-gradient sum is <=W/tau<=H0/tau. Therefore
Re C(r)>=rho/2-e/(2mu)-l^2 e/(2tau). A ground state ofH0-nu N has
e<=nu rho since vacuum is a zero trial. Ifnu<=mu/4 and l^2<=tau/(4nu),
Re C(r)>=rho/4. Explicitly check whether the author defines Re; a complex
correlator itself is not ordered. No ODLRO at fixednu follows by takingr
outside this finite window.

## Distant one-particle correlation

Let D_x be the occupied defect indicator, sumD_x=O; I_(x,d) projects onto
the isolated dimer x,x+d. Let y=x+r, |r|_1>4. The portion of b_y* b_x with
right D_x has expectation at most sqrt(<n_y><D_x>). For an isolated-dimer
input, moving x toy leaves its former partner j=x+d isolated, sincey cannot
be a Delta neighbor ofj. Thus

 b_y* b_x I_(x,d)=D_(x+d) b_y* b_x I_(x,d).

The expectation is bounded by sqrt(<D_(x+d)><I_(x,d)>). Sumx,d and use
Cauchy: there are18 possible partners and sumI=N-O. Together with the
first portion this gives

 |V^-1 sum_x <b_(x+r)* b_x>| <=(1+sqrt18)sqrt(rho <O>/V).

Insert the defect bound and grounde<=nu rho. This uses no commutation of
D_(x+d) with b_y or b_x; inserting a commuting-defect argument would be
unsafe because D_j examines a two-neighborhood.

## Pair commutators: independent conservative bound

For a primitive monomial b_u b_v, the commutator with another adjoint
pair vanishes for disjoint supports. The identical-pair vacuum-subtracted
commutator is -n_u-n_v. A one-endpoint overlap is (1-2n_u)b_w* b_v,
whose expectation is at most sqrt(<n_w><n_v>). The diagonal factor has
norm1 and commutes with the other endpoints. For fixed pair types at most
four relative center offsets overlap; averaging translations bounds each
vacuum-subtracted contribution by2rho. If lambda_A is the sum of absolute
coefficients of R_A, lambda_E1=sqrt2, lambda_E2=4/sqrt6, lambda_T=sqrt2.
Thus EACH fixed(k,l),channel entry differs from its exact vacuum Gram by
at most8lambda_A lambda_B rho<=64rho/3. A five-channel fixed-mode matrix
can instead be bounded by8(sum lambda_A^2)rho=256rho/3<324rho.
The same entry argument holds for different momenta; a multi-mode MATRIX
operator norm must include the number of modes. Do not infer uniform CCR
on the whole Fock space or an identity vacuum Gram for allk.
Vacuum Gram should be diag(1,1,S12(k)/2,S13(k)/2,S23(k)/2), Sij=1+coski coskj,
with the appropriate delta_(k,l). This is a geometric control to reconstruct,
not permission to replace physical composite operators by bosons.

No author program, author proof or output has been read at this point. Next:
small independently written exact geometry/operator checks, then full proof
comparison, binding actual hashes and distinguishing sample from proof scope.
