lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:40Z

# ypath-port: the real finer-collar path of Y and its three estimates (registry row Y-PATH)

Port by Claude Opus 5.5 (high), Mac mini worker 2, 2026-11-10, at commit 850c442f0. It is not yet checked by another model. It is a port: a check of Y's proof, with the calculations Y gives as one sentence written out. It is not a new proof.

Source: `YM4_1400.tex` at commit 2bc0658f91d2 of the Sussman-Alpoge repository (`/tmp/ym4_1400.tex`, 136,637 lines). "Y n" means line n of that file. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the argument, the constructions and every Y statement used here.

## 0. Result

Stop condition (i): the port is complete. Each of statements P0-P7 below is written with its hypotheses, constants and Y lines, and each step was checked as written. No step failed. Two points of Y needed a calculation that Y gives as one sentence; both are done here (P3.3, P5.3). One point of Y's wording needs care, and it does not break the argument: the factor e^{-c(M/M_1)(j-i)} of (E2) needs every intervening shell to have width at least a fixed multiple of M in its own units, and the rate a of the response to be fixed before M (input G-W and the order of constants, section 2).

Order of dependence (step 0): **no cycle.** The path (P4) reads the promoted-datum bound only through the fixed prospective orbit U^+ and its radius e. (E2) does not use the removal of the preceding guard; that removal reads (E1)-(E3). Section 1 gives the lines.

What stays open: the inputs listed in section 4. They are Y's statements, cited and not proved here. Of these, the response bound (IN-RESP) and the joined response polydisc (IN-POLY) are the substantial ones; (IN-POLY) is in the scope of `yjoin-port` (row 627).

## Repo search

- `library/prior/ypath-read.md` (gpt-6-luna, not checked) sections 1, 2, 4: used as a map only. Its line numbers agree with the file; its summaries agree with what I read, except that it does not give the calculations below.
- `library/inset-chart.md` section 5.3: the consumer. It reads (Y-PATH) with hypotheses "H-GEO; U^+(omega) exists with radius below the fixed ceiling; weak coupling", and conclusions "pivot unique in the regular chart; old datum in the continuation polydisc; regular old orbit U^-(omega,B) exists; (E1), (E2), (E3)".
- `library/open-registry.md` row Y-PATH: OPEN, this row is a named port. `library/open-core.md`: no entry for Y-PATH or the collar path. No other FINISH row attacks these statements (rows 617, 622, 623, 627 are a consumer, its check, the reading, and the joined-datum port).
- The Sussman-Alpoge outline: the prior reading found SA 9783-9789 and 9913 related but not a supplier. I did not repeat that search.

## 1. Order of dependence (step 0)

The five steps, with what each reads.

- (a) Promoted-datum bound on the entering support (Y 65417-65491, 134201-134205). On the entering support, where the preceding guard is still a carried factor, each datum test of the global and joined prospective datum is at most C e_q, e_q = R_q^2 eps_q. With bgc:proper-background (Y 35634-35646) this gives the admitted prospective orbit U^+ with radius e <= C_B C max_q e_q (inset-chart Lemma 5.2). As used downstream, (a) is a statement about the fixed prospective datum omega only: the certificate I(omega) of inset-chart 5.2.
- (b) The path (Y 64860-64978). Its hypotheses read: the admitted prospective datum and U^+ (Y 64863-64867); the ceiling on e (Y 64868-64869, 64929-64932, 64951-64953); the approximate collar bound 2 delta'_j on the released nonpivots, which defines the ball (Y 64902-64907, 64970-64972); the common rows at their prescribed values (Y 64871-64872, 64894, 64966-64967). No clause of the preceding guard is read at a point (omega, B) of the ball. Y says so: "This constructs the old datum without using the preceding guard on that ball" (Y 64976-64977).
  **Decision 1: yes, step (b) reads (a) only at the fixed prospective orbit U^+, through its radius e.** The bound of (a) is used once, to admit U^+ at the fixed datum omega. Every later quantity of the path (the induced field M^j U^+, the anchors, the pivot inverse, the response) is evaluated at U^+ or at a point of the ball defined from U^+.
- (c) (E1) (Y 64979-65014): reads the path (b), the response bound (IN-RESP) at the points of the path, and the plaquette estimate. No guard.
- (d) (E3) (Y 64437-64455) and (E2) (Y 64234-64251): read the decaying form of (c) (Y 65000-65004), the shell geometry (G-W) and threshold arithmetic. (E2) is stated inside the paragraph `hi:preceding-guard-support`, but it is a premise of that paragraph's conclusion, not a consequence of it: Y 64265-64268 "On admitted real data the collar response fits these reserves, by its weighted bound on the old shells".
  **Decision 2: no, the derivation of (E2) does not use the conclusion of (e).** It reads the response at the fixed U^+ over the whole ball and the thresholds of the two guards as numbers. It never evaluates the preceding guard.
- (e) Removal of the preceding guard on the enlarged support (Y 64221-64455). Reads (E1)-(E3), the reserves, and the passing of the prospective guard at the fixed datum (Y 64306-64332, 64382-64394, 64422-64435, 64456-64463). Conclusion: the preceding guard equals one on the whole admitted real collar chart.

The order is (a) -> (b) -> (c) -> (d) -> (e). No step reads a later one. In the consumer this is the fibre lemma (inset-chart Lemma 5.1): (F1) is (a), and (F2) is (e), which is proved at every omega with I(omega) = 1 and every B of the ball, from (b)-(d).
