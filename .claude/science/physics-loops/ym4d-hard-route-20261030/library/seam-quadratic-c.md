lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T19:25Z

# seam-quadratic-c: quadratic (LC) at the flat background, blind rerun

Queue item 33, mapped side. Pinned at commit ba5277f05. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work:
not independent in model, not a gate, not an audit, no status.

**Firewall.** `library/seam-quadratic.md` was not opened (no grep touched it;
every search ran on an allow-list that excludes it and the mapped-side
exclusions of FINISH.md). Read: FINISH.md, GOAL.md,
`library/excess-seam.md` (whole), `library/excess-shell-end.md` Sections 1 to
4.2, `parts/hard-core--mapped.md` Text 1 and 3.1 to 3.2 (the block operator,
Lemma 3.1), `parts/hard-core--excess.md` 1.1 (Lemma K) and 2.1 (the tensor
right inverse), `library/excess-localized-competitor-stop.md` Sections 1 and 2.

Status while writing: in progress; sections are appended in order.

## 1. The statement tested, and criteria fixed before any computation

**Setting (from the sources).** Trivial background, linearized fields. Fine
lattice of unit spacing; L odd >= 3; depth n >= 1; B := L^n, the top block
side; top units are B fine units. The one-step map is the linearization Q of
Balaban's average as in mapped Text 3.1,

    Q theta(c) = avg_{x in B(y)} [ theta(Gamma_{y,x}) + theta([x,x+L e_mu])
                                    - theta(Gamma_{y',x+L e_mu}) ],

with contours Gamma (or an average over contour orders) whose family at y' is
the translate of the family at y. Q_n is the n-fold composite. A_* minimizes
||dA||^2 on {Q_n A = v}; A_t is any field with Q_n A_t = v. The energy of a
fine field is sum over fine plaquettes of |dA(p)|^2, the quadratic part of
the normalized Wilson action. D is any set of fine plaquette anchors (in
particular a superlevel set of a weight), distances are sup-norm distances
in top units, D^{+r} = {d(., D) <= r}, D^{-r} = {z : d(z', z) <= r implies
z' in D}, S_r(D) = D^{+r} minus D^{-r}.

**Statements to deliver** (excess-shell-end 4.2 and Section 3,
excess-seam Section 2):

    sum_p |R(p)|^2 <= C_seam sum_p (K*1_{S_r(D)})(p) [|dA_*(p)|^2+|dA_t(p)|^2]   (LC)
    A_*(D) - A_t(D) <= A_s [A_*(K*1_{S_r(D)}) + A_t(K*1_{S_r(D)})]               (E-SHELL)
    beta_* = 2 A_s M_* sinh(nu r) < 1,   M_* = sum_z K(z) exp(nu d(z,0))         (RATE-exact)

where R is the curvature defect of an admissible competitor X_D,
Q_n X_D = v, with dX_D = (1 - chi) dA_* + chi dA_t + R.

**Registered criteria for the kill test (written before any run).**
1. Identities. Every exact identity used by the hand proof (chain maps,
   right inverses, the homotopy, the vanishing of the path average on the
   chosen primitive, the exact parent and the curvature of the glued field,
   and the reduction of the composite contour map) must hold to relative
   error below 1e-10 in double precision. Any failure above 1e-8 means the
   written proof has an error and stops this item there.
2. Depth and L. At fixed top-unit geometry (slab D, cutoff Lipschitz 1/r in
   top units), the measured ratio rho(B) = sum|R|^2 / sum_{enlarged shell}|G|^2,
   G = dA_t - dA_*, worst over the test family (transverse modes crossing a
   block face, white noise, smooth noise, and a power-iteration search), is
   recorded for B = 3, 5, 7, 9, 11, 13 at least. KILL if rho grows by more
   than a factor 1.5 from B = 5 to the largest B with log-log slope above 0.3
   over the last two points. SURVIVE otherwise. Also record that rho stays
   below the hand bound of Section 5.
3. What a run can and cannot show. A bounded ratio on a finite family proves
   nothing; only the written argument of Sections 2 to 6 is offered as a
   proof. A violated identity or a growing ratio would refute.
