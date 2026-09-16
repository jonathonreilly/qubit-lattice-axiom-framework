# Charged-ring conventions for the finite state check

This is a supplied test model for the general fixed-volume theorem, not native matter or a three-dimensional phase. Four links form one oriented plaquette. A single mobile particle at j in{0,1,2,3} has charge delta_(v,j), with one fixed opposite charge at vertex0. Tail-minus-head divergence is E_v-E_(v-1).

An integer physical basis is

    E_e=n-1_(e<j), n in Z,
    Q_v=delta_(v,j)-delta_(v,0).

The angle wavefunction is exp[i n sum_e theta_e-i sum_(e<j)theta_e]. This solves integer Gauss exactly, and its modulo-N restriction gives a complete4N-dimensional physical basis in the4N^4-dimensional finite-clock space. For each j, the divergence equations determine all four electric labels from one label; thus no extra finite-clock states were discarded in the reduction.

A hop j->j+1 raises the particle charge at j+1 and lowers it at j. Its multiplier is exp(-i theta_j), lowering E_j by1 and preserving Gauss. For j<3 it preserves n in the reduced basis; the wrap3->0 sends n->n-1. After writing phi=sum theta_e, the reduced matter matrix has entries h_(j+1,j)=-t for j<3 and h_(0,3)=-t exp(-i phi), plus adjoints and the shift2t I. Its eigenvalues are nonnegative because the unshifted ring adjacency has norm at most2t.

The rotor Hamiltonian has diagonal

    (g^2/2)[j(n-1)^2+(4-j)n^2]+1/g^2+2t,

magnetic matrix elements -1/(2g^2) between n and n+/-1 at fixed j, matter matrix elements -t between adjacent j at fixed n, and the wrap described above. The separately assembled rotor matrix uses these entries directly.

The exact temporal transfer on the physical clock basis has diagonal

    lambda_(n-1)^j lambda_n^(4-j),

with labels moduloN. The spatial multiplier is the actual normalized Villain b_y(phi), y=delta/(2g^2), and the matter multiplier is exp[-delta h(phi)/2]. The complete transfer is M Q M. No commutation of its factors is assumed.

For N3 and N4 the program separately constructs all N^4 link-angle configurations and all four matter states, applies the full local matter/magnetic multiplier, applies the four-link convolution by FFT, and projects with the explicit physical basis. Its matrix agrees with the reduced construction. The finite rotor comparison uses even clock orders8,16,32,48,64 and three time-step paths. Centered Fourier labels are embedded before comparing ground overlap and the trace norm of normalized Gibbs operators.

The general convergence proof is in Block03, not inferred from these finite rings. The test includes exact charge offsets, noncommuting factors, a winding hop and even-clock boundary labels, which are absent from a neutral one-variable harmonic example.
