# Independent check: D3 cell classification (B1 Theorem 5) and k^4 isotropy bound (B3 Theorem 7)

A fresh agent context was given only the two problem statements, not the
notes, the runners or the expected answers. Its findings:

- **D3.** The walks are exactly 1 and exp(+-i (k1+k2+k3) n.sigma), up to
  phase. The route: det U is a monomial, which forces SU(2) form. A
  body-diagonal line lemma gives the cases m in {0..3}, using the symmetries
  U -> -U and U -> U^dagger. Singular then shows m = 1 and m = 2 have ideal
  <1>, and for m = 0 and m = 3 the `finduni` eliminants are powers of linear
  factors (scripts `q1_*`).
- **Isotropy bound.** G(b) is unique (rank-10 linear system). The massless
  band is f = phi0^T G phi. The quartic coefficients are
  alpha = s(s^3 + 3b0 - 6b1 - 9b2)/12 and beta = -s(b0 - b1 - 2b2)/3.
  The supremum of |s| on beta = 0 is sqrt(2/3), attained only at +-b_iso. The
  argument: on that plane the walk region is compact, and its maximiser
  satisfies P = dP/dt = 0. Lex elimination leaves the real roots
  sigma = 0, +-sqrt(2/27). Exact sign checks of e1, e2, e3 at b_iso follow.
  On the plane the |k|^2 sum k^4 coefficient is -s^2/360. An mpmath
  build of the 4x4 walk at b_iso is unitary to 2e-16 (scripts `q2_*`).

Both results agree with the notes. Limit of independence: the checker is the
same model family in a new context. The scripts were written in a scratch
directory and may use absolute scratch paths.
