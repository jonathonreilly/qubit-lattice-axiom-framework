# Actual finite-time filtered response: independent check

Checked 2026-10-18 against the second half of `/private/tmp/neutral_normalform_gap_root.md`. The first-half form gap is treated as a conditional input, as requested. The finite-time/filter conclusion follows from that gap and the actual local remainder theorem; it does not require transferring an outgoing pole to the full Hamiltonian.

## Assumed normal form and state

In a finite periodic cube, take the exact unitary U_40 and

    U_40 H U_40 dagger = Jz B_40 + R_40,
    ||R_40|| <= C_40 Jz V lambda^41.

The global norm bound follows directly from the uniform interaction-norm remainder by summing terms over sites. Scalar vacuum offsets do not affect time evolution. The prepared physical state is explicitly U_40 dagger |all-up>, not a claimed microscopic ground or thermal equilibrium state. Under the transformation it becomes exactly the all-up vector.

Because B_40 commutes with N termwise and every retained local support is shorter than a whole column, it cannot turn the all-up configuration into another zero-wall configuration. Thus all-up is an eigenvector of B_40. The exact transformed microscopic evolution need not keep it stationary; that discrepancy is controlled below.

## Source and volume bounds

For C=sum_r c_r/sqrt(V) with ||c_r||<=1, ||C||<=sqrt(V). Unitary conjugation preserves this norm. The order-40 transformed-source truncation has operator error

    ||C'-C'_40|| <= C_40 sqrt(V) lambda^41,

from its uniform local analytic expansion. For small lambda its norm remains O(sqrt(V)). Consequently its effect on a two-point correlation or the connected subtraction is O(V lambda^41). With L=ceil(lambda^-4), V=O(lambda^-12), this is O(lambda^29). Center C'_40 with its own all-up expectation; the difference from exact centering is covered by the same estimate.

## A simpler sufficient microscopic time bound

The proposed locality estimate has arithmetic

    V lambda^41 T(1+lambda Jz T)^3=O(lambda^16)

for T=c lambda^-4/Jz. Its use requires the separate uniform locality/velocity proof. It is unnecessary for this particular volume choice and target precision. Ordinary finite-volume Duhamel gives

    ||C'_(B+R)(t)-C'_B(t)||
      <= 2 |t| ||R_40|| ||C'||,

and hence the connected correlation difference is bounded by

    C |t| ||R_40|| ||C'||^2
      <= C_40 (Jz T) V^2 lambda^41
      =O(lambda^13).

This weaker but elementary estimate already tends to zero faster than lambda^6 and lambda^8. It applies even to the nonstationary exact prepared state and controls the time-dependent mean entering a connected definition. No global state norm, Lieb-Robinson velocity, or infinite-volume argument is needed here. It is uniform for |t|<=T, including negative times.

Since the window uses dt/T, integration multiplies this bound only by the fixed L1 norm of psi, not by another T. Source truncation contributes the still smaller O(lambda^29).

## N sectors and the high-sector filter

On a periodic column the number of broken longitudinal bonds is even. N=2 would consist of one partial flipped interval on a single column, with all other columns fully ordered. Such an interval changes the parity of the transverse z plane between its inside and outside; fully flipped columns contribute only a z-independent parity. Thus N=2 is impossible in the stipulated even-parity sector at every z. The first possible nonzero sector is N=4, and the next is N>=6.

A fixed-order finite-support source applied to all-up cannot create a different N=0 configuration, because that requires flipping an entire column. Its centered N=0 component therefore vanishes once L exceeds the source support radius. Exact untruncated dressing can have long tails, but those are already included in the operator truncation error.

Assume the separately checked form gap B_40-Evac >=(2-C_40 lambda)N. Then every N>=6 state has energy difference at least 12-O(lambda)>10 in Jz units. Since B_40 conserves N, the q_4 and q_high correlations have no cross terms. Their total spectral weights are bounded by ||C'_40||^2=O(V).

For psi in C_c^infinity((-1,1)), its Fourier transform obeys |psi_hat(s)|<=C_p(1+|s|)^-p. The high-sector contribution to the normalized window is therefore bounded, uniformly for omega/Jz in [7,9], by

    C_p V (Jz T)^-p.

At p=5 this is O(lambda^8). The separation from the high spectrum is at least a fixed positive energy, independent of V. This estimate is valid for all high energies, not just a finite set of levels. Smooth compact support is material; an abrupt rectangular time cutoff would not supply arbitrary powers.

Together with the Duhamel and source errors, the actual prepared-state filtered response equals the finite-volume full N=4 coefficient response plus O(lambda^8), at frequency resolution O(Jz lambda^4). This error is o(lambda^6), the proposed residue scale.

## Necessary finite-volume qualification

The finite-volume N=4 response here must use the FULL N=4 block of B_40. Although its initial source is compact relative to all-up, long finite-torus evolution can in principle access configurations involving winding intervals or changed fully ordered column backgrounds while retaining four walls. Initial finite support alone does not identify that full finite-volume block exactly with the infinite compact relative-coordinate graph used for outgoing poles. A finite-volume/infinite-volume or propagation comparison is still needed to replace it by the latter. The draft correctly leaves such a comparison open; do not silently omit these states in a numerical coefficient response.

The windowed response is not a positive isolated spectral line in general (psi need not have nonnegative Fourier transform), and the exact prepared state need not be stationary. The result neither proves a full-H outgoing pole nor selects the preparation or a physical detector map.

Conclusion: conditional on the form gap and actual local normal-form remainder, the finite-time filtered comparison is valid. The elementary O(lambda^13) global Duhamel estimate is already sufficient and avoids depending on the sharper O(lambda^16) locality estimate for this step.
