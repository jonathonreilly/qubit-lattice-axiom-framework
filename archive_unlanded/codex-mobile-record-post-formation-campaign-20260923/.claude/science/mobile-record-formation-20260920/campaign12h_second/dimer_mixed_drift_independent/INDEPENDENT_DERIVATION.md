# Independent reconstruction of the initial-drift witness

The four complete specified sources were read at the identities in
PRE_SOURCES.json. No new author checker or output has been accessed. The
calculation below agrees with the supplied finite witness; no correction
has been identified. This is raw compatibility evidence for one fixed
encoding and preparation domain, not a general quantum no-go.

## Encoding and preparation equality

Use the same oriented singlet/Cartesian-triplet basis at every pair. With
q=1/2, r=1/6, lambda_A=1/8 and lambda_B=1/12, the axis and corner Schur
complements are respectively 13/32 and 3/8, both strictly positive.
Every color state has trace one. The choice lambda_B=1/12 is allowed by
the encoding's general positivity condition even though its illustrative
wave-normalized rational example used a different value.

The mixture is exactly

    rho(p)=diag(q,r,r,r)
             + |w(p)><0| + |0><w(p)|,
    w(p)=lambda_A X+i lambda_B Y.

In particular, the A_i plus/minus pair sums both equal twice the same
diagonal state. Moving equal mass between the A_1 pair and A_2 pair
changes neither X nor the encoded density. The stated unprimed and primed
probabilities are normalized and strictly positive; their common minimum
over all sampled sites and both preparations is 3/56. They obey

    X=X'=0, Y=Y'=(0,0,A c_x),
    D_2=1/7, D_2'=5/28=D_2+1/28,
    c_x=cos(pi x/3), A=1/8.

The only nonconstant entries of their common local density are
rho_(3,0)=i c_x/96 and its complex conjugate. Independent classical color
draws and product preparation of the encoded pair states imply the full
state factorization exactly:

    sum_(a_u) [product_u p_(u,a_u)] tensor_u rho_(a_u)
       = tensor_u rho(p(u)).

Thus factorwise equality gives equality of the entire K=864 pair density
operators at N=12. No thermodynamic limit or approximation is involved.
An explicit 16-by-16 two-pair tensor check supplements the algebra; the
exponentially large complete matrix need not be materialized.

## Direct current calculation with the actual rates

For each nonfixed direction put a_delta=delta-e_1. The four positions are
u-a_delta,u,u+a_delta,u+2a_delta. They are distinct at N=12, even though
some profile values at these different sites coincide. Independence may
therefore be used for their initial color probabilities.

Let g(a)=e_2(a). Summing the actual event rate k0/2+h/4 times
g(a)-g(b) under four independent initial colors gives

    J_g=(k0/2)(X_2,u-X_2,w)
       +(1/4){sum_a g(a)(p_u+p_w)_a s_a
                   -X_2,u mu_w-X_2,w mu_u},
    s=S_delta(p_l+p_r), mu_u=p_u.s, mu_w=p_w.s.

All X moments vanish in both preparations, so the floor and the two mu
terms vanish for g. On an A_2 sign state,

    s_(A2,sigma)=(gamma/2) sigma
                         delta.[e_2 cross (Y_l+Y_r)].

The endpoint D_2 values are constant and equal, so the remaining sum is

    J_(delta,X2)=gamma D_2/4
                         delta.[e_2 cross (Y_l+Y_r)].

This retains the rate's outer half factor. Since e_2 cross e_3=e_1,
only the nonfixed delta=-e_1 contributes. Its a_delta=-2e_1, hence

    J_-(x)=-gamma D_2 A [c_(x+2)+c_(x-4)]/4
          =-gamma D_2 A c_(x+2)/2.

The incoming edge is anchored at x+2. Therefore the exact microscopic
time derivative is

    dot X_2(x)=J_-(x+2)-J_-(x)
             =gamma D_2 A [c_(x+2)-c_(x+4)]/2.

At x=1, the bracket is -1-1/2=-3/2. The two derivatives are

    dot X_2=-3/224,  dot X_2'=-15/896,
    dot X_2'-dot X_2=-3/896.

The pair observable A_2=|0><2|+|2><0| has mean 2lambda_A X_2=X_2/4.
Its derivatives are -3/896 and -15/3584, differing by -3/3584. The encoded
local density derivatives differ only in entries (0,2) and (2,0), each
-3/7168. Multiplying the generator by N=12 changes the observable
derivative difference to -9/896; no acceleration is used in the witness.
The site (1,1,0) is a legitimate black anchor.

## Independent exact controls

All probabilities use common denominator 896, since twice the cosine is
the integer sequence (2,1,-1,-2,-1,1). Writing S=Sn/2 makes h=hn/2 and the
actual rate (22+5hn)/40. Direct summation over all 14^4 contexts yields
the entire fourteen-entry current vector. Integer accumulation is exactly
bounded within int64; no floating point or tolerance is used in the
current/density calculations.

The checker evaluates all five nonfixed directions, twelve physical
first coordinates and both preparations: 120 channel cases, or 4,609,920
weighted assignments. Every full color current agrees with a separately
contracted polynomial formula, all color-current sums vanish, all actual
rates lie in [1/20,21/20], and each of the 24 incoming-minus-outgoing
derivatives agrees with the analytic expression above. It also checks
the full local density derivative difference and the observable trace.

The initial execution completed all mathematical assertions but failed
when JSON encountered NumPy integer context coordinates. Its exact source,
partial output, log, traceback and receipt are preserved under
failed_attempts/numpy_json. The only repair converts those coordinates to
Python integers at construction. No formula, grid, assertion or threshold
was changed. The corrected execution succeeded with empty stderr.

## Operational implication and limits

There cannot be one evolution of these complete encoded density operators,
using the same external settings and no additional preparation information,
whose A_2 derivative equals both classical assignments. Equal full input
states produce equal observable predictions for any single quantum
experiment with input-independent ancillary resources. A Hamiltonian,
Markov, locality or long-time assumption is unnecessary for this elementary
well-definedness test.

It is important that the equality concerns the product mixed encoding,
not merely equal one-site marginals of arbitrary correlated inputs. Fixed
color-count conditioning or a retained classical preparation label can
change the full physical state and invalidate that factorization premise;
neither is used here. Different input-correlated purifications/environments
would likewise make the full physical preparations different. The witness
does not exclude those enlarged representations. A fixed change of basis,
triplet phases or consistent endpoint convention applied to both
preparations preserves equality and conjugates the same observable, so it
cannot remove this witness within the specified encoding.

Restricting the preparation domain to omit one of these profiles, retaining
D or other extra moments, changing the generator, or treating immutable
labels as additional physical information changes the tested interface.
The original continuous pure-projector record representation is not asserted
to equal this mixed encoding. No statement is made about alternative
positive quantum constructions, all quantum encodings, native formation,
or any physical-emergence/no-go conclusion. At later times the classical
law need not be a product; only its exact derivative at time zero is used.
