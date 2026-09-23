# Direct absolute one-link field tail

Root corollary after the blind independent PRE and its comparison suggested
using the same weighted-generator lemma with an absolute-value weight.
The earlier root note `ONE_LINK_EXPONENTIAL_MOMENT_BOUND.md` is left byte
unchanged at SHA-256
`e9665bd438eb597d5163ee458766b0ac686f3060bf7aa828c4b930fbf756aeb3`.
The independent PRE had already proved a coarser absolute-value bound before
seeing that note; its separate comparison is
`local_field_exponential_independent/POST_COMPARISON.md`.

Keep precisely the supplied compensated target, degree bound z and actual
resolved or coherent channels of the root note. Let

    C_h=4 delta z^4(z-1),
    R_e=2 kappa z(z-1)^2,
    c_z(lambda)=4 C_h sinh(lambda/2)
       +12 exp(lambda/2)sinh(lambda/2) R_e.

For any fixed link e, lambda>=0 and finite initial absolute one-link
exponential moment, the finite-graph target satisfies

    <exp(lambda |E_e|)>_t
       <= exp[c_z(lambda)t] <exp(lambda |E_e|)>_0.        (1)

The same holds for a locally normal infinite-volume target state via the
checked bounded-local-observable volume limit, provided its chosen-link
initial moment is finite. This is a finite-time, volume-uniform bound on
the exact target; it imposes no moments on other links.

For the domain passage use
`W_N=exp(lambda min(|E_e|,N))`. It is bounded and boundedly invertible,
commutes strongly with the diagonal electric Hamiltonian, and is monotone
in N. The function `n -> min(|n|,N)` changes by at most one across adjacent
integer fields. Thus every ratio of adjacent W_N eigenvalues lies between
`exp(-lambda)` and `exp(lambda)`. The root weighted Hamiltonian and jump
lemmas apply with exactly the same `c_z(lambda)`, independently of N.
Gronwall on the bounded weak Heisenberg equation followed by monotone
convergence proves (1); no epsilon regularizer is needed for this weight.
The full effective tensor argument also applies before imposing boundary
Gauss constraints when passing to infinite volume.

For an initial zero field, (1) gives the sharper direct tail

    Pr_t(|E_e|>=R) <= exp[-lambda R+c_z(lambda)t].         (2)

Put `A_z=2 C_h+6 R_e`. Since
`c_z(lambda)<=A_z(exp(lambda)-1)`, choosing
`lambda=log(R/(A_z t))` for `R>A_z t>0` gives

    Pr_t(|E_e|>=R)
      <= exp[-R log(R/(A_z t))+R-A_z t].                 (3)

For a finite set of links, sum (2) or (3) over them. If `A_z=0` and the
field begins at zero, it remains zero. The earlier two-sided sum bound with
prefactor two remains valid, but (2)-(3) are stronger because the absolute
weight is controlled directly. Neither result gives all-future tightness,
spin-uniform microscopic preparation, or a physically selected reservoir.
