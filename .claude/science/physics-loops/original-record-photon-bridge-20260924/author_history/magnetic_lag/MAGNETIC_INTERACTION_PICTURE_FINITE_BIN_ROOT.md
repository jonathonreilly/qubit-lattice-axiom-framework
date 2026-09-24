# A larger sufficient window for the original two-record packet contrast

Root personal derivation, September 24, 2026. Conditional candidate, not yet
independently checked. The complete original matter-field instrument is kept.
The two-mark effect and prepared boundary contrast are provisional inputs from
the sealed readout candidate. The sharper prebirth electric graph estimate
below was supplied by the finite-bin checker's blind PRE; the new step is the
magnetic interaction picture and its smooth-observable contrast bound.

## 1. Fixed setting and claim

Fix the finite even cubic torus of sides at least six, the original resolved
marks j,l in the readout geometry, a,c,kappa>0, the prepared vacuum and a fixed
normalized one-particle packet, and I=[t,t+h] in a fixed bounded interval.
Write tau_*=a/c and use

    K=g^2/(2 tau_*), delta=1/(4 tau_* g^2), 0<g<=g0<=1.

Let phi_n,g(s), n=0,1, be the normalized exact initial-sector unitary orbits
after removing the scalar energy; the separate first-event survival is
exp(-lambda s), lambda=30 kappa V. The full postbirth generator is

    A_g=-i(K D_+ + delta H4_+) - kappa Lambda_+/2,
    eta_n(s)=B_j phi_n,g(s), M=B_l^*B_l,
    Lambda_+=sum over ALL original marks m of B_m^* B_m.

No postbirth field-only Hamiltonian or dephasing is substituted.
The event is the first original event j in I followed by the next event l
within lag b, with no intervening event and unrestricted later history:

    P_n(g;I,b)=kappa^2 int_I exp(-lambda s)
                    int_0^b <exp(u A_g)eta_n,M exp(u A_g)eta_n> du ds.

Put S_I=int_I exp(-lambda s)ds and
H_I=int_I exp(-lambda s)|chi_p(s)|^2 ds, with the readout packet amplitude.
At fixed graph and other fixed inputs, the claim is

    P_1-P_0 = -2 kappa^2 b g^2 exp(-g^2 v_p/2) H_I
              + kappa^2 b O(g^4 + b/tau_*),                    (1)

uniformly for 0<b<=r0 tau_* g^2, where r0>0 is fixed. In particular

    b/(tau_* g^2) -> 0                                        (2)

is sufficient to preserve the nonzero normalized coefficient -2H_I.
This improves the earlier sufficient b=o(tau_* g^4) estimate. Neither
condition is an optimality claim. A fixed physical b as g->0 is not covered.
All constants can depend on graph, tau_*, kappa tau_*, packet, cutoff and T.
No volume, spacing, or growing-time uniformity is asserted.

## 2. The actual prebirth graph estimate

On the parent's transverse quotient Q, remove the initial scalar and write

    H_g=K Q_E+V_g, Q_E=-Delta_Q,
    V_g=(tau_* g^2)^(-1) sum_p (1-cos(c_p.A)) >=0.

The explicit cutoff finite-Hermite preparation obeys ||H_g phi_n,g(0)||<=C/tau_*.
The parent's residual and Gaussian cutoff estimates prove this on D(Q_E).
Self-adjoint evolution preserves that domain and graph norm, at every s.

For smooth phi, integration by parts gives

    ||H_g phi||^2 =
       K^2||Q_E phi||^2 + ||V_g phi||^2
       +2K int V_g |grad phi|^2 -K int (Delta V_g)|phi|^2.

Here K||Delta V_g||_infinity<=C/tau_*^2 independently of g. Positivity and
approximation on the Q_E graph core therefore imply

    ||Q_E phi_n,g(s)|| <= C g^(-2),
    ||grad phi_n,g(s)|| <= C g^(-1).                           (3)

The second inequality follows from <phi,Q_E phi> and normalization.
This is the stronger estimate in finite-bin-photon-independent/PRE.md,
section 3, used with explicit attribution. It is a graph estimate on the
ACTUAL orbit, not an unbounded operator applied to the vector-norm error.

## 3. Magnetic evolution is a smooth matrix multiplier

Work temporarily on all link angles with the finite matter space in the
postbirth record-number sector. Electric translations are multipliers
exp(i d.A); every entry of H4_+, B_j and M is a finite trigonometric polynomial
with finite matter matrices. They are bounded smooth multipliers, independent
of g. This representation restricts to the physical Gauss space. It does not
assert that every postbirth state remains in the initial zero-winding sector.

Let

    V_g(u)=exp(-i delta u H4_+), r=u/(tau_* g^2).

For 0<=r<=r0, V_g(u)=exp(-i r H4_+/4) and its link-angle derivatives through
any fixed finite order are bounded uniformly in r and g. This follows by
differentiating the finite-matrix exponential using its Duhamel integral;
compactness and the fixed graph bound all coefficients.

In each matter word D_+ is a constant-coefficient diagonal polynomial in E
of degree at most two, with bounded word-dependent coefficients. It may
have unconfined directions. Applying the product rule to V_g(u) B_j phi,
and using (3), gives

    ||D_+ V_g(u) B_j phi_n,g(s)|| <= C g^(-2)                  (4)

uniformly in s and 0<=r<=r0. The bound follows from the sum of ||Q_E phi||,
||grad phi|| and ||phi||; every multiplier derivative is bounded. Smooth
physical electric words form a core; approximation proves that all these
vectors lie in D(D_+), and that u->V_g(u)eta is continuous in that graph norm.
The full torus derivatives of the initial quotient function are bounded by
the same derivatives on its orthogonal transverse subspace.

The contraction U_g(u)=exp(u A_g) and variation of constants now yield

    U_g(u)eta - V_g(u)eta =
      int_0^u U_g(u-v)[-i K D_+ -kappa Lambda_+/2]V_g(v)eta dv.

Equation (4), bounded loss and ||eta||=sqrt(5) imply

    ||U_g(u)eta_n - V_g(u)eta_n|| <= C u/tau_* .               (5)

Thus the magnetic-only and full squared-effect expectations differ by at
most C u/tau_*, separately for each input. The magnetic-only propagator is
an estimation device, not a replacement physical dynamics.

## 4. A smooth-observable contrast lemma

Write psi_n(s) for the harmonic reference vacuum or one-particle packet
and widehat I_g for the normalized cutoff map. Both reference probability
densities on the transverse coordinates x are even under x->-x. This holds
for any complex superposition within the one-particle subspace. The cutoff
need not be even: its departures from one occur in exponentially small
Gaussian tails. The parent gives

    ||phi_n,g(s)-widehat I_g psi_n(s)|| <= C g^2 +C'exp(-d/g^2)

uniformly on the fixed interval.

For any smooth scalar F on Q, subtract F(0). Taylor expansion, the vanishing
linear reference moment and fixed Gaussian polynomial moments give

    |<reference_1,F reference_1>-<reference_0,F reference_0>|
        <= C g^2 ||F||_(C^2).

Also ||(F-F(0))reference_n||<=C g ||F||_(C^1) plus an exponential tail.
Using exact normalization to cancel F(0), the cross terms with the vector
error are O(g^3)||F||_(C^1), and the error-square term is
O(g^4)||F-F(0)||_infinity. Consequently

    |<phi_1,F phi_1>-<phi_0,F phi_0>|
        <= C g^2 ||F||_(C^2).                                (6)

The norm can use a fixed finite chart atlas of the compact quotient.
Subtracting a constant from F does not change the left side. This estimate
requires the particular two preparations and their fixed-time approximation;
it is not a statement about arbitrary low-energy states.

To apply it to the magnetic expectation, compress

    F_r(A)=<q_initial|B_j^* exp(i r H4_+/4)
                         M exp(-i r H4_+/4) B_j|q_initial>.

This is a scalar smooth multiplier. It is gauge invariant because the
operator returns to the initial fixed matter word. It need not be invariant
under constant link-angle translations. The initial wavefunctions are.
Haar-average F_r over that harmonic translation subgroup; equivalently
compress to the initial zero electric-winding sector. The average descends
to Q, preserves the expectation, and does not increase derivative bounds.
This is a projection only of the TESTED initial-sector multiplier; it does
not delete postbirth winding states or paths.

The averaged F_r-F_0 has C^2 norm <=C r for r<=r0, by the differentiated
finite-matrix exponential and the original finite trigonometric coefficients.
Applying (6) to this difference yields

    |Delta_magnetic(r)-Delta_magnetic(0)| <= C g^2 r
                                          = C u/tau_* .       (7)

No field-only postbirth limit, parity of the actual evolved state, or
normalization conditional on a second event was used.

## 5. Integrated contrast and statistical scope

Combining (5) for both inputs and (7) gives, for the exact full lag effects,

    |Delta_full(u)-Delta_full(0)| <= C u/tau_* .                (8)

The provisional readout result gives
Delta_full(0)=-2g^2 exp(-g^2 v_p/2)|chi_p(s)|^2+O(g^4).
Multiplication by kappa^2 exp(-lambda s) and integration proves (1).
For (2), H_I>0 gives a genuine negative finite-bin coefficient.

The vacuum probability has, for r<=r0, the separate conservative estimate

    P_0=kappa^2 b [25 S_I +O(g^2 + b/(tau_* g^2))].

Indeed |F_r-F_0|<=C r, plus (5), and the boundary vacuum value is
25-g^2 v_p+O(g^4). Under (2), P_0~25 kappa^2 b S_I. This estimate does not
claim that the subleading vacuum term is uniformly resolved.

With a supplied known vacuum baseline and N independent resets/trials,
the old count diagnostic still has
SNR^2~4N kappa^2 b g^4 H_I^2/(25 S_I).
For b=tau_* g^(2+zeta), zeta>0, the sufficient fixed-SNR repetition scaling
becomes N of order g^(-6-zeta). Sampling both arms adds the second variance.
These are protocol-specific sufficient scalings, not an optimal detector
bound or a claim that resets and preparations are physically implemented.

The microscopic finite-bin comparison is a separate dependency. If proved
at each fixed positive (g,b), a subsequent diagonal spin choice can preserve
this smaller signal by making each probability error o(kappa^2 b g^2).
No microscopic rate, economical spin size or simultaneous limit is supplied
by this note.

The time scale remains tau_*=a/c and shrinks with g. The result supplies no
fixed-duration laboratory detector, source preparation, calibration of a,c,g
or kappa, stable long-time photon phase, astronomical propagation theorem or
empirical agreement. It removes one overly restrictive sufficient estimate
inside the supplied model.
