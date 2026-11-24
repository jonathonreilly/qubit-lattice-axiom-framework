lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T02:37Z

# gap-k2-end-class-fable (row 1471): the end class (END-K2) with numbers

Started 2026-11-24T14:37Z (date -u), Mac mini worker 1, Claude Fable 5.2 medium, pinned at bf0e5e0ec.
Status of this file: IN PROGRESS. Nothing below is checked by a second party.

## 0. Plan (written first, per the save protocol)

Item: component C2 of the K-II tool of row 1468 (`library/gap-k2-tool-design-fable.md` sections 3-4, 7).
To prove, with numbers: explicit eps_E > 0 and v_E(m) = O(log m) such that every family realizing a local
rule of norm at most eps_E (weighted norm of 4.2 at x of order one, or a justified variant) on the sixteen
twisted tori of spatial side m and time sides v, 2v, v >= v_E(m), wrap error <= 1/100, has purity >= 457/625.
Also the entry: largest beta_E such that Wilson at beta_E after one Q2 step of stated strength is in the class.

Steps (each appended here before the next starts):
1. Read row 1468 sections 3-4, 7 (statement, norm 4.2, Fact PUR, map Q2). Record exact statements used.
2. Read Theorem E (row 1354), Theorem END-D (row 1353), Theorem BS (row 1340): what they prove, with which
   norm (supremum bounds), and what ports.
3. Compare the weighted norm of 4.2 with the supremum bounds those theorems use; find the first failure or
   show the port goes through.
4. Prove (END-K2) with explicit constants, or repair the norm and prove the repaired statement.
5. Entry: beta_E and the Q2 strength.
6. Count of certified entry steps from beta about 2.3 to beta_E; next two rows with decisive outcomes.

Marks used below: [PROVED] = full argument written here or cited to a row with its location;
[SKETCHED] = argument outlined, a named step not written; [GUESSED] = no argument.

## 1. Step 1: what row 1468 fixes (read: sections 3, 4, 5, 7, 8 of `gap-k2-tool-design-fable.md`)

Read in full: 3.1 (Fact PUR, twisted field spaces F^z), 3.2 (map Q2, Lemma TW), 3.3 (Theorem K2), 4.1-4.5, 5, 7, 8.
Facts used below, with their standing there:

- Purity of a family: P = Z_+(2v)/Z_+(v)^2, Z_+(tau) = (1/8) sum over z in Z_2^3 of the mass Z^z(tau) of the
  density on the torus m^3 x tau with temporal twist z. (3.1, 3.3.)
- Weighted norm (4.2): norm(Phi)_(x,r) = sup_c sum_{X contains c} e^(r size X) sup_V |Phi_X(V)|/(1 + theta x E_X(V)),
  E_X = sum over plaquettes inside X of (1 - Re V_p), theta in (0,1]. Label there: GUESSED adequate.
- "Realizes Phi with site constant e and wrap error eta": on each torus T of shortest side s,
  |log D(V) + e size(T) + sum over X of diameter below s/2 of Phi_X(V)| <= eta for every V. (4.2.)
- In Theorem K2 the end level has m = 512 v (l_N = 512 v_E, v_N = v_E). So the consumer has v = m/512.
- (END-K2) is SKETCHED there, with "Not checked: that the weighted norm at x of order one gives the supremum
  bounds those theorems use". That is the question of Step 3.
- Lemma TW (Q2 is well defined on the twisted tori and keeps each mass) is PROVED BY HAND, UNCHECKED there
  (check row 1469 is queued). I use it in Section 6 only.

Plan of the proof, decided in this step (one approach): a polymer expansion of the sixteen masses in the
supremum norm, with the Kotecky-Preiss criterion in its two-function form (a, d). The weighted norm is first
reduced to a supremum norm at a smaller rate (Step 3). This is the strong-coupling expansion of Osterwalder
and Seiler in abstract form. Twists are invisible to every cluster that does not wrap the time direction.

## 2. Step 2: the three relatives, read (what each proves, in which norm, what ports)

Read at this pin: Theorem E (`gap-mini-nphys-fable.md` L185-240), Theorem END-D (`gap-mini-neutral-step-fable.md`
L268-345), Theorem BS (`gap-blockstep-fable.md` L264-270) and the RESULT text of rows 1340, 1353, 1354.

| Theorem | Class | Norm | Conclusion | Use here |
|---|---|---|---|---|
| E (row 1354) | plaquette weights a_p(alpha_p + beta_p (-1)^(z_p)) with a centre bit split off | L^6 norms under a product reference: norm(alpha_p - 1)_6 <= 1/4096, norm(beta_p)_6 <= 1/40 | eight twisted masses within e^(2 tau); two-period bound | NOT a port. A local rule in SU(2) block links has no split centre bit and no product reference. Its content that I keep: the end class must be of the small-coupling kind (C3), so the twisted masses come out equal. |
| END-D (row 1353) | functions f_W on windows W = link sets of boxes, centre invariance (G), Haar links | supremum norm N_kappa(f) = sup_l sum_{W contains l} e^(kappa size W) sup abs(f_W), size = sites of the box | N_kappa <= kappa/32 gives every Z^e > 0 and abs(2 log Z_+(T) - log Z_+(2T)) <= 4 v e^(-kappa j_0/4), j_0 = min(T, m) - 1 | The nearest relative. Same method (polymers, rooted sums, two-period bookkeeping). It is a supremum-norm theorem. See the two differences below. |
| BS (row 1340) | Wilson datum at one coupling, block Dobrushin condition (B-pin) | chord coupling numbers of a block law | the seed, given (B-pin) | NOT a port for the end. It proves a seed from a mixing hypothesis. It gives no local form of an image density. |

Two places where END-D does not give (END-K2) as stated. Both are bookkeeping, not analysis.

- (D1) Windows against connected sets. END-D indexes by boxes, with size = number of sites of the box. A rule
  of 4.2 is indexed by connected bond sets X. The bounding box of a connected set of n bonds can have of
  order (n/4)^4 sites. So a rule that is small in e^(r size X), size X = number of bonds, is not small in
  e^(kappa size W). If "size(X)" in 4.2 is read as the number of bonds (4.2 does not say), END-D cannot be
  quoted. Theorem END-K2 below is proved for connected sets with size = number of bonds. If size is read as
  the sites of the bounding box, both theorems apply (bonds of X <= 4 sites of the box).
- (D2) The remainder. END-D's remainder is 4 v e^(-kappa j_0/4) with j_0 = min(T, m) - 1. At the consumer's
  shape (time side v = m/512) this is the same kind of bound as below. END-D states the two-period bound for
  Z_+ only; the purity needs exactly that, so END-D's conclusion is already the purity bound
  P >= exp(-4 v e^(-kappa j_0/4)) for its class. [PROVED there, unchecked at this pin.]

So I do not redo END-D. I prove the statement for the class of 4.2 by the Kotecky-Preiss theorem, which gives
the constants in a few lines, and I record END-D as the window form.

Search (rule 0a). `grep END-K2` in FINISH.md: one hit, my own queue row 1471. In `library/open-core.md`: no hit.
In `library/` and `parts/`: only row 1468's file and this file. Strong-coupling relatives on file: Theorem 1 and
Theorem 3 of `gap-seed-sc.md` (row 701: the seed for the Wilson weight at beta below 1/12800), Theorem DOB (row
785), Lemma END-RAY (row 1340), END-D, Theorem E. None is stated for a local rule in a weighted norm. So the
statement below is new on file as a statement; its method is standard and is not new.

## 3. Step 3: the weighted norm gives the supremum bounds, with an explicit loss [PROVED]

Convention. size(X) = abs(X) = the number of bonds of X. The diameter of X is its largest coordinate extent,
so diam(X) <= abs(X) for a connected X. w_X = sup over V of abs(Phi_X(V))/(1 + theta x E_X(V)).

**Lemma W.** For every X and V: abs(Phi_X(V)) <= w_X (1 + 3 theta x abs(X)). Hence for 0 < q < r,

    sup_c sum_{X contains c} e^(q abs(X)) sup_V abs(Phi_X(V)) <= M norm(Phi)_(x,r),
    M = M(theta x, r - q) = sup over n >= 1 of (1 + 3 theta x n) e^(-(r - q) n) <= 1 + 3 theta x/(e (r - q)).

Proof. 1 - Re V_p lies in [0, 2]. A plaquette inside X has its four bonds in X, and a bond lies in six
plaquettes. So X holds at most 6 abs(X)/4 plaquettes and E_X <= 3 abs(X). The second line follows term by
term. For the last bound, n e^(-s n) <= 1/(e s). QED

Answer to the question of row 1468 4.3 ("Not checked: that the weighted norm at x of order one gives the
supremum bounds"): it does. The weight costs a factor 1 + 3 theta x abs(X), which a part r - q of the decay
rate pays. There is no failure and no repair of the norm is needed for the end. The loss is the factor M, of
order theta x / (r - q). So eps_E is of order 1/(theta x): the end class shrinks as x grows, as it must,
because a rule of weighted norm eps may equal eps theta x times the Wilson action.

Remark (the weighted class is not a small-coupling class at large x). Phi = -c sum_p (Re V_p - 1) has
w_p = sup of c (1 - Re V_p)/(1 + theta x (1 - Re V_p)) = 2c/(1 + 2 theta x), so its weighted norm is about
6 e^(4r) c/(theta x). A Wilson rule of coupling c of order eps theta x is inside the ball of radius eps. So
(END-K2) can hold only with eps_E theta x below the hand range of the Wilson weight. This is why the
statement says "x of order one".
