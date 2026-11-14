# r55a_1 — criteria (written BEFORE the script). Reviewer: claude-opus-5-5, batch C6 (REVIEW55_ARS.md)

## Object (definitions read in PROOF.md by string, not by line)
- PROOF.md "S4 Averaging (L1)": fine blocks B(X) of side L, odd L, roots = block centres c_X. So at L = 3,
  y - c_X ranges over {-1,0,1}^d (L^d sites).
- PROOF.md "S4' [S3] Order-averaged averaging": for each of the d! coordinate orders sigma, P^sigma is the
  complete-axial transporter moving in the coordinates in the order sigma, and
  T^sigma_y = P^sigma(c_X -> y) . S_y . P^sigma(c_Y -> y + L e_mu)^dag, S_y = straight leg of L steps in +mu.
  c_Y = c_X + L e_mu (block centre of the mu-neighbour block, PROOF "Decision 4: the RG kernel", c = (X, X+e_mu)).
- PROOF.md "Decision 4: the RG kernel": M_bar_c(U) := (d!L^d)^{-1} sum_sigma sum_{y in B(X)} T^sigma_y(U).
- Model used by the script: a lattice path is the sequence of unit steps (axis, +/-1) starting at c_X.
  Two paths give the same transporter for EVERY gauge field iff their freely reduced step sequences agree
  (cancel adjacent (a,s)(a,-s)). The holonomy is the ordered product of link variables, reverse = inverse.

## Claims under test
- KN_ADOPT.md §1.6 (string "633 distinct (path, y) pairs"): 1944 index pairs collapse to 633 distinct, with
  induced weights {1/1944, 1/486, 1/162, 1/81}, presented as the weights "on the set of distinct transporters".
- CODEX_REVIEW_KN.md F1: 633 is the (y, axial-path) LABEL count, multiplicity histogram {1:384,4:192,12:48,24:9};
  freely reduced full paths number 475, histogram {1:288,4:96,6:48,12:12,20:24,48:6,72:1}.

## Pre-registered checks and verdicts (d = 4, L = 3, mu = axis 0)
- E1 index count == 1944.                                   PASS / FAIL
- E2 distinct (y, order-of-moving-coordinates) labels: count and multiplicity histogram.
     LABELS-633-CONFIRMED iff count == 633 and histogram == {1:384,4:192,12:48,24:9}; else LABELS-DISAGREE.
- E3 distinct freely reduced full paths: count and histogram.
     REDUCED-475-CONFIRMED iff count == 475 and histogram == {1:288,4:96,6:48,12:12,20:24,48:6,72:1};
     else REDUCED-DISAGREE (report the actual count and histogram).
- E4 KN_ADOPT's "633 distinct transporters": REFUTED iff the E3 count != 633 AND the exact-SU(2) leg E7
     confirms the E3 count as the number of distinct transporter VALUES; CONFIRMED iff E3 == 633 and E7 agrees;
     otherwise NOT-SETTLED.
- E5 independent closed form sum_{k=0}^{3} C(3,k) 2^k k! (1+2k) == the E3 count.  AGREES / DISAGREES.
- E6 induced weights (multiplicity/1944) all > 0 and sum exactly 1 for BOTH the label and the reduced
     partitions.                                            CONVEX-PRESERVED / FAIL
- E7 (the leg with real power; independent of my reduction code): two gauge fields with every link an exact
     rational unit quaternion (inverse stereographic image of a rational point; SU(2) = unit quaternions),
     on every link the paths touch. For each field compute the 1944 holonomies exactly (Fraction arithmetic).
     PASS iff, on EACH field, (i) all index pairs in one reduced class give identical holonomies, and (ii) the
     number of distinct holonomy values equals the E3 count. If (ii) gives FEWER distinct values on one field
     but the full count on the other, report COINCIDENCE-ON-ONE-FIELD (not a FAIL of E3). If (i) fails on any
     field the reduction code is wrong: FAIL.
- Designed-FAIL controls (must fire, else NO POWER):
     C1 switch off free reduction: the distinct-raw-word count must come out 633 (= labels) and != E3 count,
        i.e. the 633-vs-E3 gap is caused by reduction alone.     FIRES / DOES-NOT-FIRE
     C2 "unpaired" far end (far-end path uses the REVERSED order of sigma): the E7 distinct-value count must
        change from the paired count (shows E7 is sensitive to the path family, not a constant).
                                                                 FIRES / DOES-NOT-FIRE
     C3 the identity field (all links = 1): exactly ONE distinct holonomy value (shows that distinctness is a
        property of generic fields, as Codex F1 says "at the identity field they all coincide").
                                                                 FIRES (count 1) / DOES-NOT-FIRE
## Arithmetic rules
Plain python3 -I, integers and fractions.Fraction only, no floats anywhere, no numpy/BLAS.
