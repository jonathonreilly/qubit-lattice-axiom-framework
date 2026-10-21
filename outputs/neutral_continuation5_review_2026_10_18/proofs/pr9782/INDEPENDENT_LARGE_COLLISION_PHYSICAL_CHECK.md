<!-- Original PR9782 source SHA256 18cd6abad93a5713319b8a5038772f0fe553f474cea2a19b56772aacafffaa4f. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# General-b native contact identity and permanent normalization

Focused independent check of `/tmp/neutral_large_collision_root.md`. Control script `/private/tmp/neutral_general_contact_control.py`; output `/private/tmp/neutral_general_contact_control.json`. No shared/root file edits.

## General native identity: verified beyond the anchor

The direct control uses arbitrary complex, finite-support host pair coefficients f(i,j)=f(j,i), with f(i,i)=0, and independent arbitrary complex length-two ray coefficients on BOTH adjacent x and y pairs. Neither the anchor profile nor a two-body eigen-equation is imposed.

For each four-singleton same-z output S, it enumerates backward native transverse bond flips, evaluates their exact XX/YY spin matrix element, filters the input by its directly counted eight longitudinal walls, and constructs the input B†² amplitude by ordered disjoint feature partitions. Separately it computes the native two-body action h2 f, including the two longitudinal placements of each length-two ray with opposite XX/YY signs.

The stronger identity checked is

    [K8 P8 B†²]_S
      -2 sum_(three pairings ij|kl) [(h2 f)_ij f_kl + f_ij (h2 f)_kl]
    =4 sum_(occupied directed nearest xy i->j) f(j,k) f(j,l).

400 arbitrary complex tests give maximum error 6.40e-15. Thus substituting the actual bound-state equation h2 f=Eb f yields precisely the claimed (K8-2Eb) residual for general b. This does not depend on the anchor's absent x ray or its alternating y profile.

The enumeration has a simple exhaustive justification. One native bond can connect a four-spin output only to two-, four-, or six-spin inputs. Two-spin inputs have zero two-feature creation amplitude. Four-spin inputs are mixed-spin transverse hops. A nonzero six-spin host-ray input must complete a length-two rectangle one layer above or below an adjacent pair in S; each remaining singleton belongs to the host feature. There is no extra overlap contribution: the four output columns are distinct, and the two added sites are exactly the partners needed by that ray. Each of these six-spin inputs has eight walls. Longer rays and two-ray inputs cannot connect to this output with a single two-spin bond flip.

The x-ray input sign is negative and the y-ray sign positive; both are already present in h2 and cancel correctly in the identity. Canonical creators are all-lowering extensions, so overlapping factors vanish rather than introduce a new amplitude. The P8 input projection is retained explicitly; it must not be omitted for arbitrary outputs, but it adds no missing terms here.

## Full 24-term outgoing permanent: factor verified

For fixed anchor 0,d, fix outgoing label a at 0 and b at d. There are 12 ordered choices a!=b. For the remaining labels c,e, the unordered k<l sum includes the two assignments of c,e. Exactly

    sum_(k<l) f_k f_l [exp(-ip_c k-ip_e l)+exp(-ip_e k-ip_c l)]
    = S_c S_e-G_(p_c+p_e),

where S_c=sum_k f_k exp(-ip_c k) and G=sum_k f_k² exp[-i(p_c+p_e)k]. The subtraction is the complex square f_k², NOT |f_k|². Hence the root coefficient

    4 sum_d sum_(a!=b) exp(-ip_b d) [S_c S_e-G_(p_c+p_e)]

has the correct factor. There is no additional half or two. A separate finite computation with arbitrary complex f_k and four arbitrary distinct momenta compared the full 24-permutation sum against this factorization; error 4.15e-14.

For f(0,r)=exp(iQ r/2) phi(r), the root's S argument p-Q/2 and G argument p_c+p_e-Q follow immediately. Removing r=d subtracts f_d exp(-ip d) and f_d² exp[-i(p_c+p_e)d], respectively; r=0 is absent because phi(0)=0. Total outgoing momentum 2Q modulo the reciprocal lattice makes translation anchoring consistent. Repeated outgoing momenta still leave 24 labelled permutations; at the anchor with two repeated pairs this indeed equals four times the six-term convention.

## Boundaries of this check

The physical contact identity and the Fourier factorization are verified. This report does not certify the critical-b Green-function distributional limit, the numerical elementary constant C, or its proposed interval lower bound; those are separate analytic/numeric steps. Infinite sums need the stated decaying bound profile at each delta>0 before taking the threshold limit. Finite COM normalization is explicitly omitted in the root convention and must not be reconstructed as a physical rate from this coefficient alone.

The result remains a native contact/Born numerator for the specified canonical two-feature state and free outgoing plane-wave comparison. It is not an exact distorted four-body scattering amplitude, a decay rate, an actual spectral linewidth, or a source/detector identification.
