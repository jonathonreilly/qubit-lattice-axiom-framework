# Mutation Plan

The primary must reject at least these nonidentical defects:

1. alter one of the 47 frozen conflict signatures;
2. choose the actor as collision winner;
3. choose the target as collision winner;
4. omit target-side rollback at a transverse front/trail contact;
5. drop the front parent dart during quench;
6. drop the trail return-child dart during rollback;
7. let `L` cross a nonmatching child dart;
8. accept one acknowledgement;
9. accept two acknowledgements at nonadjacent endpoints;
10. accept while one marked controller remains live;
11. reuse a root guard before quiescence;
12. leave one orphan `T` after rollback;
13. write a Record from contact or acknowledgement;
14. merge two width-two parallel darts;
15. add a hidden query ID or scheduler owner;
16. add an epoch, coordinate or component size;
17. replace `X_n` by a scalar default;
18. omit the default Kraus identity;
19. coherently add two many-to-one Kraus rows;
20. break one proper-cubic transport;
21. break complement pairing;
22. hard-code `p=1/2` as selected physics;
23. count a positive escape branch as almost-sure absorption;
24. omit a closed nonterminal end component;
25. promote a scoped failure to a finality or axiom no-go.

An independent consumer must use behaviorally disjoint mutations after the
primary table and result are frozen.
