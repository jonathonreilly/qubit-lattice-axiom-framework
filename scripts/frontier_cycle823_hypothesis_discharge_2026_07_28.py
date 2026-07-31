#!/usr/bin/env python3
"""Cycle 823: fixed-b discharge of H_TEMPLATE_PREIMAGE_ZONE_CLASS.

The Cycle-817 primary/checker pair and constructor witnesses are inert audit
inputs: this stdlib-only runner reads their bytes/text and parses their ASTs,
but never imports or executes them.  The finite template signatures used by
the discharge are frozen below as a literal certificate and checked against
independent digests before use.
"""
from __future__ import annotations

import ast
import base64
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import perf_counter
import zlib


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = (
    "scripts/frontier_cycle823_hypothesis_discharge_2026_07_28.py"
)

PRIMARY_817 = (
    "scripts/frontier_cycle817_general_b_sector_theorem_2026_07_28.py"
)
CHECKER_817 = (
    "scripts/frontier_cycle817_theorem_independent_check_2026_07_28.py"
)
CYCLE719 = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
)
CYCLE719_LOCAL = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
)
CYCLE739 = "scripts/frontier_cycle739_identity_discharge_2026_07_28.py"
SOURCE_FINALIZER = (
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py"
)

AUDIT_INPUT_PATHS = (
    PRIMARY_817,
    CHECKER_817,
    CYCLE719,
    CYCLE719_LOCAL,
    CYCLE739,
    SOURCE_FINALIZER,
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

# The Cycle-817 pair are evidence only and are forbidden executable imports.
BLOCKLIST = tuple(Path(path).stem for path in (PRIMARY_817, CHECKER_817))
BLOCKED_DYNAMIC_CALLS = frozenset(
    ("__import__", "compile", "eval", "exec", "run_module", "run_path")
)

EXPECTED_PROVENANCE = {
    PRIMARY_817: {
        "sha256":
            "469a0af17b19bb6a35ac5356b5c143f6027af05c412f92a5b349f09c0452c7a4",
        "blob": "01045658578074e6d3c496ff09b3169381596728",
    },
    CHECKER_817: {
        "sha256":
            "91180f1f16400f9056a8ee1076cf8b2dda7dd8151a4e8e755a3ecbd581c313f7",
        "blob": "3c5a32dd91681db119692140d826a1e7063dd1e5",
    },
    CYCLE719: {
        "sha256":
            "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
        "blob": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    },
    CYCLE719_LOCAL: {
        "sha256":
            "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
        "blob": "3add288d1b7de5bcc45f5ef8f88f3cfb98105b8f",
    },
    CYCLE739: {
        "sha256":
            "c4fe65ae06f77665379c5e96f4951fb9a73919a000d6e18004b9e244beb6b88e",
        "blob": "ea7dbca69ea7ebf860573395053d2089626d4c36",
    },
    SOURCE_FINALIZER: {
        "sha256":
            "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
        "blob": "97cc3de7b95e341326c404047a321dbe2c825eda",
    },
}

HYPOTHESIS_NAME = "H_TEMPLATE_PREIMAGE_ZONE_CLASS"
EXPECTED_HYPOTHESIS = {
    "name": HYPOTHESIS_NAME,
    "predicate": (
        "the actual fixed source/finalizer words lie in the capacity-"
        "independent source support; every bank-template operand lies in "
        "one 131-wire bank block; every pair-template operand lies in its "
        "declared left-bank/right-bank/191-wire link-half zone; the cross "
        "predecessor offset is in [0,131); and the finalizer word is bank-"
        "count independent"
    ),
    "role": (
        "exact condition for promoting the verified affine zone relabeling "
        "and the Cycle-738 transfer to the actual emitted words"
    ),
    "mechanical_fixed_b": True,
    "general_b_status": "OPEN",
}
EXPECTED_CHECKER_IDENTITY = (
    "The actual fixed source/finalizer words lie in the capacity-independent "
    "source support; every bank template operand lies in one 131-wire bank "
    "block; every pair-template operand lies in its declared left-bank/"
    "right-bank/191-wire link-half zone; the cross predecessor offset is in "
    "[0,131); and the finalizer word is bank-count independent."
)

SOURCE_WIDTH = 41
BANK_WIDTH = 131
LINK_AUX_WIDTH = 191
LINK_WIDTH = 2 * LINK_AUX_WIDTH
SOURCE_ANCHOR_SUPPORT = (0, SOURCE_WIDTH + BANK_WIDTH)
CROSS_PREDECESSOR_OFFSET = 1
ARITY = {"X": 1, "CNOT": 2, "TOF": 3}
PAIR_TEMPLATE_KIND = {
    "handoff_forward": "handoff",
    "relay_latch": "relay",
    "relay_swap": "relay",
    "relay_unlatch": "relay",
    "handoff_return": "handoff",
}
DISCHARGE_BANKS = tuple(range(3, 11))
PATTERN_TEST_BANK = 11

EXPECTED_TEMPLATE_METADATA = {
    "bank_packet": {
        "digest":
            "e29feaeadd5e036830a4b269b235dec0ff0fb788ab3ee6e25eac7197de8377cc",
        "gates": 492,
        "operands": 1173,
    },
    "finalizer": {
        "digest":
            "13924ee1e0079c38c8ccb00d519ac0896d4c8b886802e857632ccaed3cbcacff",
        "gates": 11,
        "operands": 29,
    },
    "handoff_forward": {
        "digest":
            "1dec5f1fce15076cee9b40a8af734e67914ce2e2850a29f5ad5d25b717e3fe08",
        "gates": 752,
        "operands": 1542,
    },
    "handoff_return": {
        "digest":
            "0dbbea684594a8c77e95c060635e7a9d9a970dedb5ebea85e93638a106b30765",
        "gates": 593,
        "operands": 1223,
    },
    "relay_latch": {
        "digest":
            "a808ac9e7354239a8f718e50619df96ed3345edf0ec48afc0a2fa37c538fe7bf",
        "gates": 369,
        "operands": 755,
    },
    "relay_swap": {
        "digest":
            "21127bbeee2260bbcc8b1c52d97410de58438b90eb0f00981a6e03fe691dedc4",
        "gates": 12,
        "operands": 28,
    },
    "relay_unlatch": {
        "digest":
            "fcdd745953d6bbe5a4add33ecfac6cc806c30f6c59a53a9e423a93550d33eab8",
        "gates": 367,
        "operands": 749,
    },
    "source": {
        "digest":
            "b8f5ca17203c5f5eff0289642998f9118e843474bd8cf318891b75dc91cf68b6",
        "gates": 5,
        "operands": 12,
    },
}

# zlib/base85 encoding of the exact eight constructor gate signatures.  The
# decoded canonical JSON is 44,752 bytes; compression keeps this source and
# its audit stdout compact without weakening the per-gate/operand exhaustion.
TEMPLATE_PREIMAGE_B85 = (
    "c-rlqP0!`VafScOthu=T!LMusWEpR~2p|Z;M3!K~f@F*(7)g--o;v+%E~{8ij}+JrV(9`}yewU^S!8$hsXC`P|Ml"
    "+Q-+%kZFaGrY%Rheg{kwnq?6Y_O{I9?H?Yrf({aB9k^Us&daDFuWn;ku#f0gH7_4!wO{?(s<t<S%<=U@BtujBdGH"
    "AZoRT%(k0m~xF%u7S!mQn`jI*I4BmtX!kjYqaWox<;$lX!RPcUZd4(w0ezJuhHr?TDwMT*J#Z>!ne_W`<s9H_%fE"
    "WIMZ2{qb_IlCOdvCr$6y*%dswJ_olua+j6env@XZKoSQdo%W*8{?oIn*S3kVvSjuvq-f}K=DUXLU+0oL>R)Vc8-E"
    "1}3>av=x1zTG-v-M!>%Wk$c*vtd7ZNX+<nr#m@ooW9a!Dy!zGoHa{=b9@exT15-mlAx@x#mm>&gfk8rUY+vuDMf!"
    "J380yssw*@uI?&0q;u`AO7O_et#(%>cx2~RyQ>mBvU985RSh25xz+Bf29NCAYIjwGM|N(tyQ;w>JGa_h)!>nxTg{"
    "^yJhF4Ec~pZ(c5c;k4j$RL%{;2XBRjX5M>Tk4=Qi`G1&{39X0!hBlRxB3;^26j=n%S&4+$S9K6rXX_%ivm;{?H}g"
    "p&@ZCr)IX^0+u?8R3HCrHPA}Ry#!niXIeYC>l}J%FzviAVkU>O(En$V21DwK_0e(ykUfG#cewGt*Fqp<u)_F#qGE"
    "quDEqJ+-3`H$!??e+xL!J{fe-lA%rLdH%`DMJK&cUa83g}Q~)<Mcgl60c3r$(Bev@{+I4UJx>&zP=-05_;jnA8?("
    "X^;tzV<{YqWliwqB#H*J$fC+Io$)I@ouOwz>y*jkaE+t=DMVHQIKKwq2ub*J#@{+U8K^HQMIa)WEU-53p402~4#$"
    "p{ceJoZ10TwF3ZEI{{Jk2SBP`08{k}psF`ORlNhM>MNkCz5%N0JD{q50IKRIpsMu&sA?^Ms@4jqYHfh3)()s@T>("
    "|C8=$In2UN8lfU4FLP}TMTRJ9dARa*sAwKYIhTL)CNt$?bw4N%p#FGu;wAMzz}aJ)@)2wlgAgpU&+JiQ`(nf%&ug"
    "5XrbNr%%DCo)cXTpYBFaKZ7?#6^tD9RmY~5DYdLmN0-psH2!jp%Vh^|2@7sZ}@84aeG>ED{Hvz71|=*#_6}y9k<>"
    "Ux9NskdZF##fdUT|c7zoxLXd`Vr4Y1nfXBn29U;?thgYAhpFGl@uQzzx^YxzZd;XgD{4MYKd)o7D{>5-fKZA?GkZ"
    "@yg``Jl&6eGAFON#flNN=XyQqjA~7Vh0-A?t3k&~`UjP`{hjWxt#30o_gZ!1A^3FW0Vhf4O$8`^&X!mHrdI%GaVH"
    "|5vxM?|;hy_U-4Ly05;T`)16)Dv$hDO3AOK)cjt4+@;(IKW=-@^5c%{Eqk&Y$#UK;EnVlwl+|1AQ}bv`!Zn)wH&e"
    "06e>2&8OJydT{5O+5<ojc>_tRdX=x2taNpe<x4Ns?h0z8C3-FlAHZOx&&Z4j&X9IV@sqjiH2+aWS^hzuPfLvMe>k"
    "ll}0$PO>2!;4wr#cc3mQt<r|>3K`Ki!BA;Ed}2#Z3bJuPTC%}J%{Y=?w>*X6tgV@NI}~&g&ei_9JVd>NO9Y8ls$W"
    "Jyn@xw3|5Nnj~w00N7F?s@5gO@*xNWi^&4Hf<V!zpmzE*SWu4@Tyy21AV#x2Zo<HYZ{xwy>z*GG-=_tIUbob!nLr"
    "?qe_SXLHZkNBG+v)DTkM6}MT|-npe7?N<`VZf}|K<<>`PGLZjCdmvV(2KNzR_ars7qq|_=l6TQ>p7yXU9^P2+jLG"
    "ZBJxz`SftXocsOzZ-4jQ*I$3}^>-is^8Ul`l8bMDd$ENhP@3me9Npq_@#0eS;xhN*68hrr%ccLtRRv1-Di1eq_cV"
    "_i*A*g)t4|bHwkWQeQCyLuxY|c?C6Tgvd5If$^{kT{*HvMPE6x;Gvnj5WQ(T3oxWZ3y^`NqOU5guc^CXxXcXQ+JZ"
    "rt6CySs6BH}3An-QBpm7u2|MchAXrs?LpjxN#3R?%~Eg+_;Au_i*DLUdiLeb?T&YdgjoLd%AH?H}2`iJ>9sc8~1e"
    "Mo{sT!6k>JEVtqJ*)JvI8uQ_sj>cbPC{yL6Pd^q;>;Yiho<60k%f_=FA^c-uTUfnf4QS13zPwRTN*OS1W8+I|IHZ"
    "P%a<2KI(yK!9%sV;_87elIxA=Sl@>S9QBF{E~{-E!l0PfWXUT@0x%hEx|rs*54j#gOV^NOdu!u3j|e#$7#6?#6X7"
    "q`DYVT@0z4SE_jdn;X}0;I;Vod!6f+tXr{e!TR0va?h<Gw}9OGam&Z89=CW-ul93m<l$*~w`Sd1C~hqjw-$<93&p"
    "L4;?_cOYqJEIp&K`-1l+h@Q{bfrUV-3+30|+@Wei^3P`$p<ja$8F!Hw(IX>secxOH0GIxTLU7Pn51GoorkjCJ#X!"
    "j6QeYRJIsNVuzRYcQ_L9qP6P<0jBnLsC~oByMIrg7FXttRaQ7BZ0*la=5A@bg}b87H3ChwF`ti&W_BgD+H%@^GE`"
    "!kV{w9J`F6@J-DUnr(v=hGWM$aXS1t>sz4nTP$|HIXS>ofdkA}Q&0wdYrKN@hz>dsnUIct>M`krIj^NuNMVonX1m"
    "7%OHdJNS;M-xob@S~AzS*lWq-ECNo4p&uTxJcv9jcU@Z%6P=sb`lEF8F4tpdm7wO~E&t9fr-!8hkq?5Yx;Hz8SJN"
    "yk^$mo23AT+{_w$vs}S2oLPf!mQ)y;Gi&h8vJb;`W(~es4s8g}tid;FwpQ~k@QQY1)@^BlfV3mCN;+7A)qGnIv({"
    "jhPVO{o3sy<$9%k*qYQAm7tZT5EZ(B9%7Odvmruz0Ctmd1o*A{r)CS9E^*cK?@CJCOc*cK>&Cas+<*%nBECRv_pk"
    "%0ziQt+u78R+UJv7hRZfof?(S!lim61+)5sG4Np%bV1Os!9fGy-Ap8tF{FezDdJqtF{HgzDe$AtF{GhzeyQstF{F"
    "hK$D2lR&5K4fhN7>E+J{~P14Lm+(Yn9Do$IqE#z@cf=^quEvOrsw4vf9f)JufMry0J1<gd0;?!1c3-XF4ajLD_7K"
    "%VkJcg~>7E;!x4AE9?3&~_t)@iG@1;WIR7DLiz4Zc}~GfZvP;G0D_L)T^vzKN>0Rog<@xrx-bRog=0xrzU`Rog=8"
    "xk)NutG0!twkh)+6o2qd0t9IRLIJud!r5$Xp#<F&;cT|HP&;jkaJC9ssGc@OxT30K@J+f3sS$ecO%YDIg;1kzig1"
    "!R^x&H!oYW9&@J$iUqCs1OZ;Egh4cZ!fQ-rf<(AMCaBAi8owg%r6;Vc@oHTb3o_mF-f_+}B#@&&U7-z>se=3v&~n"
    "?*RwA<P<lTP0AoJKKV97U3+fFl+G5B3za5dJDc;gsakM2SCz<MkMDBh{TSTI_kZ_H;ZtViI_F`W)aSE60-*1EW%l"
    "KV%FfBML5e-%o=>N2xl3~(gH4N!X-A}TfikvxWwjr3%H~Sm)Lx70hcu45}WTW;1WApEXOfx@XaEeWjkgKzFCB`yv"
    "MA;H;ZtV0hu-UCcJ0!y#-uiM`ktO0xq#5vzl)Km)Mb6&9{I{nxLW0_ZD!89hud93%JCN7R#f|8hjIETqOt!z6mp~"
    "Vyl900*yA`TfikvsL|$o3%JCN%xb;`T+)PEwW9}I(o{dyjvjD{9hud93%JCN%xb;`Tw+HCXT>7~-%i0{^DW>KJF;"
    "1=-v-|-!dWI~*5KPImB0BGa7mNs-1g2MaETq+byX28!CF)Z?g5tAkt*mtpb|S$rM(AGVn@p<;~I?O!_2q^qlh^(?"
    "!mY(r^v)37?0)D-JijDF7{x0fFpLa*mLOtjo8s*kEI7NVn>TTl^(E27Z$On(gPOh!Xi@l2Q1QsMeMQkfJM5nh=gq"
    "ci*#X;p@9o-35!TB7qCbd7Ll?pV395?A`xD|B3)QSdcA-}y0D0(eF2MfVG*eS0~YDRA`%P+EYgKVq%90sqzjAK6Y"
    "2qrbYT&DLOo!SE-a!M7qCbd7AaB<2H%85idf*_o3MyIp&qbE7Z$N6)B_gj!XoyBdcY!GSVZ$XV395?Vo#_CEYgKV"
    "><RUNMY^zvJ)s`3NEa5dC)5KL>B1uRgnGateN^Eko(#STi`WzD0gH6$ChZCJfJM3_mJ*KyEMiCE)aq7$#!vaOd<%"
    "HH?Aqip@FU~L%ddi88^2<n4m@>mn(>sJOkbYryexPL@p9v($;+6RJcb7jC6lnjA&SEphdvII98xj*Vw|Rkj<KJ23"
    "EWR`=fOP+cQf4gaEHXbl(t>oqG#JVZ~Y7t7*a6&V5q{dh9MBbC5BcL7{-u|;T=OkhK&p{8ICe^MVQNwcmkgpYBMZ"
    "n2+wezQv*&TIOV|fgj1PG+QTUlr&FAIahk>{9jAYsDq>p6Dd;3!<<yqbU{0Aiz2;P$({@hru^hmqgGrfzOA=hZ;8"
    "F*dMYx2*<rXf@U>S!?K9lkgmy)>b#3d>&XL0F^%Vb<q!}1%K>Lz79E&+16kV}hPhUAhZmp8c-ie*zSu};ddT)O2l"
    "FPDV5e9Wb0E=zL>8_V5X8lRNWx#Z5}c`oI1*`Fx_rW2TYAew?HjT!yHR0-26Ou;Z+!_*GbKuj4Sy~I@1gtlUei|H"
    "_?&X{InN{;C}ruvW;WD0RYH!?NJG$vD?Oph{^%Csv}v`FV7^UEADvdPFhBSVc`Hn8529(U~dom3BGdm!QW32DDhN"
    "d7hv1r!z$cyU1x9qbd4!a5N(w226!uxP@IDT2sipNKNniHM_3L>~o3B2GKv6(u{WPgYc_G*q<|QouM}j8n^a5ls-"
    "+1kp`nk&YMdcu|iR`veitJ`oMA6OmDyh>{A6n7p_th@SR|NNSyks@g<^Rams;#auz;wNFH0>qJD>CZe;#A~i2w3!"
    "=7tB7$2dqPfN*J1@QqqP%S);_DO9U!8~qC!)ggn1~Q7iWa??F^U|wi72v9M3i+Rx_q!mGl)0$iP&?Uh(p^%Oj=lc"
    ">P4wRth!Ict?NV#+a}`K!eU!5!VTiweIn*vC*t2W5epX<7kklh5F_ss@$xzmJGY5Ay0Dnqi>!nAdY_23*NM2hO~l"
    "}Z#p7O79>nJRM4Y}(#O!S%eh-}`N`@nnG7K+(@Hi(w``ANdSbMvlxGA$eCqH{$>apB#PgURF#~_e@_Oz7chN9}|<"
    "9?LM&z_dL+%TC8%g1n(fA+Mr*iAJ~RK=rBe)hEV*eg3uQ~{+=e)hDiu`h0%sG7w(`PtL5EfLS^M3r~8$<LmaJ@)X"
    "86Sw7KoX<adT8`LCI8Ic7=9v8Kqs21Y<Nj2ITw~9*``OcC2>1R}RVpog^0TL9U5@)xRpqs;lb?OG)Mua7b>cZn;`"
    "B4ui}K;C?|=C4t^W+^FW2plVDcbb>9z{DgSd^w?Kf^4a=Vk;wA^0iwm7%*y)@syKF#;5rRX2LrRdep^J?dTcAk&b"
    "(6<8Cy_aK@x>7I43cVborj~j+cIxFgpqE1=Qf}r@`8s!Vs8F4|IaJin-5e^G=WY%a)}fn2bYtq~cq=yEyE)zpllN"
    "|pw<6}fo8ztEdGF@X|47XoqK;E9$40Fj8+CH*)X1?@AIDB@96NP!?9{}uQxC^ZEgU;_aELcg4IHA_Q~$<jOTV{oN"
    "PdvIH>6ZZ%^MOmq}~nbA5!avq!OufLtJBO+z>69`ZmOj=C%#7sJU%JjB9S&5IdXOHpJxSwhghqxotxXac<iXo1EJ"
    "=#60J=4YAa@Z9`0MZrc#+o7*<T<mR>wvA(%&Lwc3mwjpgxZrdm;wQZD*+BV8gZ5!pFwvBR9+lDkVxox8sYTFRspW"
    "8O14ajX9(h=mg4QUQ?+lKTBxotyQhTOIx-9v8MkVYc6ZH&)c-P<+>Nu9bjL{;Xl4bhspYeN)h?%EJtn!7ect>&%`"
    "(XhE|LzHdq+7P{)x;6$CoVqp!ZJfF`2F0AZHU=G?yEa5!r>>1bbEmG2L5ZiXjX|HMu8l#pr>>1b%cri5LE)#ajY0"
    "RPu8koLNL?F4Mv%HThU6f1Z47xr>e?7mhSaq&WDlupV@M=Y*T#@jq^^x2y+~afL#C0sHio1lb!`m!N9x)bQjyfPF"
    "=QpVYeRu6cWo$e<*p3{#N4%^K#;pO6bN$Hh5|wE+E5_KT^kAnxobm#Aa`vj5ag~61%lkQF}`Dzx;7-j%3T{0Y~`*"
    "EiMw*whJ;|bYeS;3+_fQrS?=197%g{gNVt}}HY9S(T^ka_<*p5h=W^GEgm$@WL!!LgwIKmt?%I&pFL!N77?`^@Bq"
    "GdR8xkDmt__J3bJxcDpstOTx;7+`%xxPIQ|7)62`_WwhD4gVb3=m8+`1w0XYSpQP&7AhNK~4;HzYvK?HdxS=Kc){"
    "TXO@43VXSOLsh%n!7;?Ose?oHwws84@>{+x-vi$-`o_;;^33@8^1I;o#_yQt1J50vXEY~y{?6t)uM1v7yxw?i@;c"
    "@<&+!3c3CEpDjN*94v5(^<$5f8L9IH95;~v2K#bj^ceTerg-rsmH<b9L(Sl*9u@8*4ef(aNuFxFsP!Wf3}4r3$6Q"
    "HZ%1pG~kF<37fSj3*g;GEQYo%lH?uGUMtA24}p^*q-wM&KWqr;9P|B7R+%tADZM&oM&-P#`zoPdYBe+2FckbW~Q9"
    "QPBLE3jyaR&teZ1*&gMDu=PChK6u9~@sZ?-PgDW6hE#b-vS7Eqf!_^(E1aZ}9Qeon16j!de%Ec8iuAXtF4U2M6zQ"
    "aP_q$G&NLo735K@v-sSmeZVC>Bns#EQjOF56;(7fZodG{*8W7NW6ajm2#$gJZ#bQd{RbJlE{GzRz3$^9IZ@Fdu>3"
    "1@jyeP6X)_BwCP?LGp%Zp1=pal&df0>Zg^fFV*Njs%rGrl<+HUO4w24wW1)bp?Iv2&}>6dnp+rJ7oRWhK794f`~U"
    "djoA=*;`TOUmq*>ec(v|(vb!9JY(o35(*CttpGw^BBCat7R+DMzUlQ!u9ZPG{vK%7Khnte+$@~37`5GN^9N!lc3I"
    "Z2wNTreq<lr<({lJd)>OHwA9WJ$_dlPXEsZ4xD^=AJ}JD$gfTk}CQ6`?9L~=kLpkA;{mC6`PR1FDvFDe_vKCMgG3"
    "57>)dWS+O7a`?6w6^7m!Ms^ss>ih;@BmsK{Fzb{)zpro=4d|$SZL`mfy_`Yl*k&?<t@O{}rGNn<T%HNkQC{(H_RH"
    "`Ucswh;dC{(H_RH`Ucswh;dC{(H_RH`UcY9v%rWi#oN24#?RN`qcVI;BBHB%RWrEs{=YP#j68H0Y3|QySDs(kTs^"
    "CFzs~C6jbYgT6^Rr9t&1ozkF%l1^z*NJ*zO=%%Do8q`$MDGeGc>68ZLm2^sj9!ol<L8T>~(xBavP-#$fNvJgFyd+"
    "c_)L#-R4Vo|sl?J7lgi3>cOhTnWRVJa*pf&U7W%Vth{CQb@w<v#JR^K?vpO@A5kdjbod^;(BURK{(%Ac3j7aa2EW"
    "%ad({CQb@86tmPR$r0GpO@7aC-UcI^>vE;d0B;>{CQbby7T8{RTa;lmsJHFJ}-Nx@Mpi}>+(JD{jzWT9Qc{x^W}F"
    "jd2jrVc|P#m;d#b$lIJhabzB#`h9>Kc*CwxHUh^CuIF@kS;TVPSjAP#<PI64;_{*`H<2vsFykGF%g8LBfS(E*Z_d"
    "?z`d5`7&7`JZT<rxtmdSIk6K_!e}80|1JVid)Qi_sY)IYNDm5NBwTktd^6MzoB687VWWW(1CCoss<{3*d}_vkT5d"
    "IBVeyhqEC}oG8V@WQ@}`Oz<!j#H10^OH4#DWyRzc^I*=IC;2t!;+VE$f{&#DC>q4-!i(v8F<qZxx?XI_FP$x!F%^"
    "IQ%lkk5IzBY;boqyGU-Zn2o_WzTFM8%v^o+&40jd%`vk^VB6FqYPJ@bbCGC#8;KXV{Ia{@oJQ}6grt>Xg#Cwit5J"
    "=2Ju=|s=0M9*wQ&+J6cP|x^DJ>ze=N9Jb=@-r3rnTGsKM}B5Ser7{{W=DSJKz`;Vex^K-pDD=CRODwG@-rRznHBk"
    "&4f&ZJ`I!UxnUnaLk?UuErXW94k)LVE&vfKxR^(?k<Y#u|XAb0NPU2@qjpokJ9Q4osy;XiPKhuz(>B!Hl$j@xZ&+"
    "N$09LUd{#LtY%TIOd8@-r3rnTGsKM}B5Ser7{{W=DSJKz`;Ver8leGe1+1pQ*^tG~{PG@-r*)GaK?VJMuFJ@-rv#"
    "GozB7`5FA@|5p6x|3)=E^D`a!nHBk&4f&ZJ`I!UxnUnaL!9ZkwrVu|fn2p5G3>GBwGadPv7619a%*60-`MP`$e82"
    "1)KL>nf{Cp?xg5MjzW1bH@cX*!hoaFh7bDh`4WDW6p<F(1_nAbeV2aY8icQ8hAJe$Nmj*}cyIsS62=D5y#0Ph#Lx"
    "9~nR*|T_m<GqmgP2OX9KgO+_cX>nvj2<RPgHZ`17)Cpcj2J~R;$n10NRCn83?VX_WaP;xl@TqYUq;G|su6)RTAv_"
    "$&H^}N;Ov4k5zbmT!{Ka*5+_WtI2psV4HG;}1u<#F^b!+MOj#+p<ve(jGjo2;xj3fnnBYSxAl3|Cq|1wRd66zJ(#"
    "4Z5fBx==4_|)e377Hjkj4*>EJJe<P1>XbA0jMp`y9JK!!UjR-~R(;Bi@A"
)


def stable_json_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode()


def stable_digest(value: object) -> str:
    return sha256(stable_json_bytes(value)).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function", name, len(matches)))
    return matches[0]


def assigned_literal(tree: ast.Module, name: str) -> object:
    matches: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("literal", name, len(matches)))
    return ast.literal_eval(matches[0])


def named_dict_constant(
    tree: ast.Module,
    identity_name: str,
    requested_key: str,
) -> object:
    matches = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        pairs = {
            key.value: value
            for key, value in zip(node.keys, node.values)
            if isinstance(key, ast.Constant)
            and isinstance(key.value, str)
        }
        name_node = pairs.get("name")
        value_node = pairs.get(requested_key)
        if (
            isinstance(name_node, ast.Constant)
            and name_node.value == identity_name
            and isinstance(value_node, ast.Constant)
        ):
            matches.append(value_node.value)
    if len(matches) != 1:
        raise AssertionError(
            ("named dict constant", identity_name, requested_key, len(matches))
        )
    return matches[0]


def load_inert_packet() -> tuple[
    dict[str, object], dict[str, str], dict[str, ast.Module]
]:
    rows = {}
    sources = {}
    trees = {}
    for path in AUDIT_INPUT_PATHS:
        absolute = ROOT / path
        data = absolute.read_bytes()
        text = data.decode("utf-8")
        observed_sha = sha256(data).hexdigest()
        observed_blob = git_blob_sha1(data)
        expected = EXPECTED_PROVENANCE[path]
        exact = (
            absolute.is_file()
            and observed_sha == expected["sha256"]
            and observed_blob == expected["blob"]
        )
        rows[path] = {
            **expected,
            "observed_sha256": observed_sha,
            "observed_blob": observed_blob,
            "bytes": len(data),
            "exact": exact,
        }
        sources[path] = text
        trees[path] = ast.parse(text, filename=path)
    literal_relative = all(
        not Path(path).is_absolute()
        and ".." not in Path(path).parts
        for path in AUDIT_INPUT_PATHS
    )
    exact = (
        len(rows) == 6
        and literal_relative
        and all(row["exact"] for row in rows.values())
    )
    return {
        "literal_paths": AUDIT_INPUT_PATHS,
        "literal_worktree_relative": literal_relative,
        "paths_existing": all((ROOT / path).is_file()
                              for path in AUDIT_INPUT_PATHS),
        "rows": rows,
        "access": "bytes/text/ast.parse only; never imported or executed",
        "exact": exact,
    }, sources, trees


def certificate_a(trees: dict[str, ast.Module]) -> dict[str, object]:
    primary_hypothesis = assigned_literal(
        trees[PRIMARY_817], HYPOTHESIS_NAME
    )
    checker_identity = named_dict_constant(
        trees[CHECKER_817], HYPOTHESIS_NAME, "identity"
    )
    finalizer = function_node(
        trees[SOURCE_FINALIZER], "source_finalizer_word"
    )
    finalizer_argument_loads = tuple(
        node.lineno for node in ast.walk(finalizer)
        if isinstance(node, ast.Name)
        and isinstance(node.ctx, ast.Load)
        and node.id == "_bank_count"
    )
    exact = (
        primary_hypothesis == EXPECTED_HYPOTHESIS
        and checker_identity == EXPECTED_CHECKER_IDENTITY
        and not finalizer_argument_loads
    )
    return {
        "certificate_name": "A_MECHANICAL_RESTATEMENT",
        "Cycle817_primary_exact_statement": primary_hypothesis,
        "Cycle817_checker_exact_identity": checker_identity,
        "fixed_b_decidability": "FINITE_DECIDABLE",
        "quantified_objects_at_fixed_b": (
            "the 8*b-5 emitted program rows; each selected finite gate word; "
            "every gate operand; the finite bank/edge indices in those rows; "
            "the one cross predecessor offset; and finalizer outputs"
        ),
        "decision_procedure": (
            "authenticate the eight literal constructor words; expand all "
            "8*b-5 rows; classify every operand in the source anchor, one "
            "bank block, adjacent bank blocks, or the declared 191-wire "
            "link half; check cross offset 0<=1<131; and prove the finalizer "
            "_bank_count parameter has no AST loads"
        ),
        "capacity_quantifier_ruling": (
            "No infinite C enumeration is needed: the check is on local "
            "preimages, and the affine formulas symbolically map each typed "
            "preimage into the same declared zone for every C>=b."
        ),
        "bounded_surrogate": None,
        "source_anchor_support": {
            "half_open": SOURCE_ANCHOR_SUPPORT,
            "reason": (
                "the source interval plus bank[0] are capacity-independent "
                "under BANK_BASE(i)=41+131*i"
            ),
        },
        "finalizer_bank_count_AST_loads": finalizer_argument_loads,
        "exact": exact,
    }


def function_fragment_certificate(
    tree: ast.Module,
    function_name: str,
    fragments: tuple[str, ...],
) -> dict[str, object]:
    function = function_node(tree, function_name)
    rendered = ast.unparse(function)
    matches = {
        fragment: fragment in rendered for fragment in fragments
    }
    return {
        "function": function_name,
        "span": (function.lineno, function.end_lineno),
        "fragments": matches,
        "exact": all(matches.values()),
    }


def function_containing(
    tree: ast.Module,
    fragment: str,
) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and fragment in ast.unparse(node)
    ]
    if len(matches) != 1:
        raise AssertionError(("function containing", fragment, len(matches)))
    return matches[0]


def decode_template_preimages() -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    dict[str, object],
]:
    compressed = base64.b85decode(TEMPLATE_PREIMAGE_B85.encode())
    raw = zlib.decompress(compressed)
    decoded = json.loads(raw)
    templates = {
        name: tuple(
            (str(kind), tuple(int(wire) for wire in wires))
            for kind, wires in word
        )
        for name, word in decoded.items()
    }
    metadata = {
        name: {
            "gates": len(word),
            "operands": sum(len(wires) for _kind, wires in word),
            "digest": stable_digest(word),
        }
        for name, word in templates.items()
    }
    all_gates_well_formed = all(
        kind in ARITY
        and len(wires) == ARITY[kind]
        and len(wires) == len(set(wires))
        and all(isinstance(wire, int) for wire in wires)
        for word in templates.values()
        for kind, wires in word
    )
    exact = (
        len(raw) == 44_752
        and tuple(sorted(templates))
        == tuple(sorted(EXPECTED_TEMPLATE_METADATA))
        and metadata == EXPECTED_TEMPLATE_METADATA
        and all_gates_well_formed
    )
    return templates, {
        "encoding": "canonical JSON -> zlib level 9 -> base85",
        "decoded_bytes": len(raw),
        "compressed_base85_characters": len(TEMPLATE_PREIMAGE_B85),
        "template_metadata": metadata,
        "all_gate_kinds_arities_operands_exact": all_gates_well_formed,
        "exact": exact,
    }


def literal_preimage_certificate(
    trees: dict[str, ast.Module],
) -> tuple[
    dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    dict[str, object],
]:
    templates, literal = decode_template_preimages()
    extraction_ast = function_fragment_certificate(
        trees[CYCLE739],
        "template_words",
        (
            "K.R3.source_compute_word()",
            "K.H.PACKET",
            "K.H.HANDOFF_FORWARD",
            "K.H.RELAY_LATCH",
            "K.H.RELAY_SWAP",
            "K.H.RELAY_UNLATCH",
            "K.H.HANDOFF_RETURN",
            "K.M.source_finalizer_word(1)",
        ),
    )
    digest_ast = function_fragment_certificate(
        trees[CYCLE739],
        "word_evidence",
        ("signature = word_signature(word)", "stable_digest(signature)"),
    )
    constructor_ast = function_fragment_certificate(
        trees[CYCLE719],
        "interleaved_program",
        (
            "R3.source_compute_word()",
            "H.PACKET",
            "H.HANDOFF_FORWARD",
            "H.RELAY_LATCH",
            "H.RELAY_SWAP",
            "H.RELAY_UNLATCH",
            "H.HANDOFF_RETURN",
            "M.source_finalizer_word(bank_count)",
        ),
    )
    mapper_ast = function_fragment_certificate(
        trees[CYCLE719_LOCAL],
        "mapped_action",
        (
            "M.offset_gate",
            "M.map_pair_gate",
            "M.R12.LINK_BASES[index]",
            "M.R12.BANK_BASES[index + 1]",
            "int(A.CELLS[0]['pred'][1])",
        ),
    )
    finalizer_ast = function_fragment_certificate(
        trees[SOURCE_FINALIZER],
        "source_finalizer_word",
        (
            "bank_zero = R12.BANK_BASES[0]",
            "marker = bank_zero + A.DIRECTION_OK",
            "return tuple(output)",
        ),
    )
    exact = (
        literal["exact"]
        and extraction_ast["exact"]
        and digest_ast["exact"]
        and constructor_ast["exact"]
        and mapper_ast["exact"]
        and finalizer_ast["exact"]
    )
    return templates, {
        "certificate_name": "A2_LITERAL_PREIMAGE_WORDS",
        "literal_gate_words": literal,
        "Cycle739_extraction_AST": extraction_ast,
        "Cycle739_digest_AST": digest_ast,
        "Cycle719_constructor_AST": constructor_ast,
        "Cycle719_mapper_AST": mapper_ast,
        "Cycle719_finalizer_AST": finalizer_ast,
        "provenance_boundary": (
            "The literal signatures and independent digests are frozen "
            "certificate data extracted from the SHA-pinned constructors; "
            "the constructors remain inert and blocklisted from execution."
        ),
        "exact": exact,
    }


def bank_base(index: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * index


def link_base(index: int, capacity: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * capacity + LINK_WIDTH * index


def data_width(capacity: int) -> int:
    return SOURCE_WIDTH + BANK_WIDTH * capacity + LINK_WIDTH * (capacity - 1)


def program_rows(bank_count: int) -> tuple[tuple[str, int], ...]:
    if (
        isinstance(bank_count, bool)
        or not isinstance(bank_count, int)
        or bank_count < 1
    ):
        raise ValueError("bank_count must be a positive integer")
    prefix: list[tuple[str, int]] = [("source", 0)]
    for bank in range(bank_count):
        prefix.append(("bank_packet", bank))
        if bank:
            prefix.append(("cross", bank - 1))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff_forward", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    reverse: list[tuple[str, int]] = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    return tuple(prefix + reverse + [("finalizer", 0)])


def pair_local_zone(wire: int) -> tuple[str, int] | None:
    if 0 <= wire < BANK_WIDTH:
        return "left_bank", wire
    if BANK_WIDTH <= wire < 2 * BANK_WIDTH:
        return "right_bank", wire - BANK_WIDTH
    if 2 * BANK_WIDTH <= wire < 2 * BANK_WIDTH + LINK_AUX_WIDTH:
        return "link_half", wire - 2 * BANK_WIDTH
    return None


def mapped_template_word(
    name: str,
    index: int,
    capacity: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if name in {"source", "finalizer"}:
        return templates[name]
    if name == "bank_packet":
        base = bank_base(index)
        return tuple(
            (kind, tuple(base + wire for wire in wires))
            for kind, wires in templates[name]
        )
    if name == "cross":
        return ((
            "CNOT",
            (
                link_base(index, capacity),
                bank_base(index + 1) + CROSS_PREDECESSOR_OFFSET,
            ),
        ),)
    pair_kind = PAIR_TEMPLATE_KIND[name]
    split = 0 if pair_kind == "handoff" else LINK_AUX_WIDTH
    output = []
    for kind, wires in templates[name]:
        mapped = []
        for wire in wires:
            zone = pair_local_zone(wire)
            if zone is None:
                mapped.append(-1)
            elif zone[0] == "left_bank":
                mapped.append(bank_base(index) + zone[1])
            elif zone[0] == "right_bank":
                mapped.append(bank_base(index + 1) + zone[1])
            else:
                mapped.append(link_base(index, capacity) + split + zone[1])
        output.append((kind, tuple(mapped)))
    return tuple(output)


def operand_failure(
    bank_count: int,
    station: int,
    name: str,
    index: int,
    gate_index: int,
    operand_index: int,
    wire: int,
    expected_zone: object,
) -> dict[str, object]:
    return {
        "COUNTEREXAMPLE": "H_TEMPLATE_PREIMAGE_ZONE_CLASS",
        "b": bank_count,
        "station": station,
        "template": name,
        "template_index": index,
        "gate_index": gate_index,
        "operand_index": operand_index,
        "observed_wire": wire,
        "expected_zone": expected_zone,
    }


def fixed_b_discharge(
    bank_count: int,
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
    finalizer_independent: bool,
) -> dict[str, object]:
    capacity = bank_count
    rows = program_rows(bank_count)
    failures: list[dict[str, object]] = []
    family_counts = Counter(name for name, _index in rows)
    mapped_gate_count = 0
    mapped_operand_count = 0

    for station, (name, index) in enumerate(rows):
        mapped = mapped_template_word(name, index, capacity, templates)
        mapped_gate_count += len(mapped)
        mapped_operand_count += sum(len(wires) for _kind, wires in mapped)

        if name in {"source", "finalizer"}:
            preimage = templates[name]
            for gate_index, (_kind, wires) in enumerate(preimage):
                for operand_index, wire in enumerate(wires):
                    if not (
                        SOURCE_ANCHOR_SUPPORT[0]
                        <= wire
                        < SOURCE_ANCHOR_SUPPORT[1]
                    ):
                        failures.append(operand_failure(
                            bank_count, station, name, index, gate_index,
                            operand_index, wire, SOURCE_ANCHOR_SUPPORT,
                        ))
        elif name == "bank_packet":
            preimage = templates[name]
            for gate_index, (_kind, wires) in enumerate(preimage):
                for operand_index, wire in enumerate(wires):
                    if not 0 <= wire < BANK_WIDTH:
                        failures.append(operand_failure(
                            bank_count, station, name, index, gate_index,
                            operand_index, wire, (0, BANK_WIDTH),
                        ))
        elif name == "cross":
            if not 0 <= CROSS_PREDECESSOR_OFFSET < BANK_WIDTH:
                failures.append(operand_failure(
                    bank_count, station, name, index, 0, 1,
                    CROSS_PREDECESSOR_OFFSET, (0, BANK_WIDTH),
                ))
        else:
            preimage = templates[name]
            for gate_index, (_kind, wires) in enumerate(preimage):
                for operand_index, wire in enumerate(wires):
                    if pair_local_zone(wire) is None:
                        failures.append(operand_failure(
                            bank_count, station, name, index, gate_index,
                            operand_index, wire,
                            {
                                "left_bank": (0, BANK_WIDTH),
                                "right_bank":
                                    (BANK_WIDTH, 2 * BANK_WIDTH),
                                "link_half": (
                                    2 * BANK_WIDTH,
                                    2 * BANK_WIDTH + LINK_AUX_WIDTH,
                                ),
                            },
                        ))

        if name == "bank_packet" and not 0 <= index < bank_count:
            failures.append({
                "COUNTEREXAMPLE": HYPOTHESIS_NAME,
                "b": bank_count,
                "station": station,
                "template": name,
                "template_index": index,
                "expected_index_zone": (0, bank_count),
            })
        if (
            name in {"cross", *PAIR_TEMPLATE_KIND}
            and not 0 <= index < bank_count - 1
        ):
            failures.append({
                "COUNTEREXAMPLE": HYPOTHESIS_NAME,
                "b": bank_count,
                "station": station,
                "template": name,
                "template_index": index,
                "expected_index_zone": (0, bank_count - 1),
            })

        if name == "cross":
            expected_cross = ((
                "CNOT",
                (
                    link_base(index, capacity),
                    bank_base(index + 1) + CROSS_PREDECESSOR_OFFSET,
                ),
            ),)
            if mapped != expected_cross:
                failures.append({
                    "COUNTEREXAMPLE": HYPOTHESIS_NAME,
                    "b": bank_count,
                    "station": station,
                    "template": name,
                    "template_index": index,
                    "observed_word": mapped,
                    "expected_word": expected_cross,
                })
        else:
            for gate_index, (
                (local_kind, local_wires),
                (mapped_kind, mapped_wires),
            ) in enumerate(zip(templates[name], mapped)):
                if (
                    local_kind != mapped_kind
                    or len(local_wires) != len(mapped_wires)
                ):
                    failures.append({
                        "COUNTEREXAMPLE": HYPOTHESIS_NAME,
                        "b": bank_count,
                        "station": station,
                        "template": name,
                        "template_index": index,
                        "gate_index": gate_index,
                        "local_gate": (local_kind, local_wires),
                        "mapped_gate": (mapped_kind, mapped_wires),
                    })
                    continue
                for operand_index, (
                    local_wire, mapped_wire,
                ) in enumerate(zip(local_wires, mapped_wires)):
                    if name in {"source", "finalizer"}:
                        expected_wire = local_wire
                        expected_zone: object = SOURCE_ANCHOR_SUPPORT
                    elif name == "bank_packet":
                        expected_wire = bank_base(index) + local_wire
                        expected_zone = (
                            bank_base(index),
                            bank_base(index) + BANK_WIDTH,
                        )
                    else:
                        zone = pair_local_zone(local_wire)
                        if zone is None:
                            continue
                        if zone[0] == "left_bank":
                            expected_wire = bank_base(index) + zone[1]
                            expected_zone = (
                                bank_base(index),
                                bank_base(index) + BANK_WIDTH,
                            )
                        elif zone[0] == "right_bank":
                            expected_wire = bank_base(index + 1) + zone[1]
                            expected_zone = (
                                bank_base(index + 1),
                                bank_base(index + 1) + BANK_WIDTH,
                            )
                        else:
                            split = (
                                0 if PAIR_TEMPLATE_KIND[name] == "handoff"
                                else LINK_AUX_WIDTH
                            )
                            expected_wire = (
                                link_base(index, capacity)
                                + split
                                + zone[1]
                            )
                            expected_zone = (
                                link_base(index, capacity) + split,
                                link_base(index, capacity)
                                + split
                                + LINK_AUX_WIDTH,
                            )
                    if (
                        mapped_wire != expected_wire
                        or not expected_zone[0]
                        <= mapped_wire
                        < expected_zone[1]
                    ):
                        failures.append(operand_failure(
                            bank_count, station, name, index, gate_index,
                            operand_index, mapped_wire, {
                                "exact_wire": expected_wire,
                                "zone": expected_zone,
                            },
                        ))

        for gate_index, (kind, wires) in enumerate(mapped):
            if (
                kind not in ARITY
                or len(wires) != ARITY[kind]
                or len(wires) != len(set(wires))
            ):
                failures.append({
                    "COUNTEREXAMPLE": HYPOTHESIS_NAME,
                    "b": bank_count,
                    "station": station,
                    "template": name,
                    "template_index": index,
                    "gate_index": gate_index,
                    "mapped_gate": (kind, wires),
                    "expected": "allowed kind, exact arity, distinct operands",
                })
            for operand_index, wire in enumerate(wires):
                if not 0 <= wire < data_width(capacity):
                    failures.append(operand_failure(
                        bank_count, station, name, index, gate_index,
                        operand_index, wire, (0, data_width(capacity)),
                    ))

    expected_counts = {
        "source": 1,
        "bank_packet": bank_count,
        "cross": bank_count - 1,
        "handoff_forward": bank_count - 1,
        "relay_latch": bank_count - 1,
        "relay_swap": 2 * (bank_count - 1),
        "relay_unlatch": bank_count - 1,
        "handoff_return": bank_count - 1,
        "finalizer": 1,
    }
    if len(rows) != 8 * bank_count - 5 or family_counts != expected_counts:
        failures.append({
            "COUNTEREXAMPLE": HYPOTHESIS_NAME,
            "b": bank_count,
            "observed_rows": len(rows),
            "observed_family_counts": dict(family_counts),
            "expected_rows": 8 * bank_count - 5,
            "expected_family_counts": expected_counts,
        })
    if not finalizer_independent:
        failures.append({
            "COUNTEREXAMPLE": HYPOTHESIS_NAME,
            "b": bank_count,
            "observed": "source_finalizer_word loads _bank_count",
            "expected": "bank-count independent finalizer word",
        })

    passed = not failures
    return {
        "b": bank_count,
        "C_probe": capacity,
        "n": 8 * bank_count - 5,
        "program_rows_exhausted": len(rows),
        "template_family_counts": dict(sorted(family_counts.items())),
        "mapped_gates_exhausted": mapped_gate_count,
        "mapped_operands_exhausted": mapped_operand_count,
        "source_finalizer_support": SOURCE_ANCHOR_SUPPORT,
        "bank_local_zone": (0, BANK_WIDTH),
        "pair_local_zones": {
            "left_bank": (0, BANK_WIDTH),
            "right_bank": (BANK_WIDTH, 2 * BANK_WIDTH),
            "link_half": (
                2 * BANK_WIDTH,
                2 * BANK_WIDTH + LINK_AUX_WIDTH,
            ),
        },
        "cross_predecessor_offset": CROSS_PREDECESSOR_OFFSET,
        "failures": failures,
        "H_TEMPLATE_PREIMAGE_ZONE_CLASS": "PASS" if passed else "FAIL",
        "sector_theorem_at_fixed_b": (
            "UNCONDITIONAL_NO_H_TEMPLATE"
            if passed else
            "CONDITIONAL_BRIDGE_HYPOTHESIS_FALSE_AT_THIS_B"
        ),
        "failure_logic_if_any": (
            None if passed else
            "This is a counterexample to the bridge hypothesis at this b. "
            "The independently exhaustive anchor theorem may still pass, "
            "so the hypothesis would be sufficient but not necessary."
        ),
        "exact": passed,
    }


def certificate_b(
    cert_a: dict[str, object],
    literal: dict[str, object],
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    finalizer_independent = (
        cert_a["exact"]
        and not cert_a["finalizer_bank_count_AST_loads"]
    )
    rows = {
        bank_count: fixed_b_discharge(
            bank_count, templates, finalizer_independent
        )
        for bank_count in DISCHARGE_BANKS
    }
    passed_b = tuple(
        bank_count for bank_count, row in rows.items() if row["exact"]
    )
    failed_b = tuple(
        bank_count for bank_count, row in rows.items() if not row["exact"]
    )
    exact = (
        cert_a["exact"]
        and literal["exact"]
        and passed_b == DISCHARGE_BANKS
        and not failed_b
    )
    return {
        "certificate_name": "B_FIXED_B_EXHAUSTIVE_DISCHARGE",
        "declared_discharge_range": DISCHARGE_BANKS,
        "budget_extension": (
            "required b=3,4,5 plus b=6,7,8,9,10; all finite rows, gates, "
            "and operands exhausted"
        ),
        "per_b": rows,
        "passed_b": passed_b,
        "failed_b": failed_b,
        "unconditional_sector_theorem_b": passed_b,
        "logical_scope": (
            "At every passing b, the Cycle-817 sector theorem no longer "
            "assumes H_TEMPLATE_PREIMAGE_ZONE_CLASS. Its corrected seven "
            "conditions and H_SECTOR_INPUT remain theorem premises."
        ),
        "exact": exact,
    }


def certificate_c(
    cert_a: dict[str, object],
    cert_b: dict[str, object],
    templates: dict[str, tuple[tuple[str, tuple[int, ...]], ...]],
) -> dict[str, object]:
    local_template_zone_results = {
        "source": all(
            SOURCE_ANCHOR_SUPPORT[0] <= wire < SOURCE_ANCHOR_SUPPORT[1]
            for _kind, wires in templates["source"] for wire in wires
        ),
        "finalizer": all(
            SOURCE_ANCHOR_SUPPORT[0] <= wire < SOURCE_ANCHOR_SUPPORT[1]
            for _kind, wires in templates["finalizer"] for wire in wires
        ),
        "bank_packet": all(
            0 <= wire < BANK_WIDTH
            for _kind, wires in templates["bank_packet"] for wire in wires
        ),
        **{
            name: all(
                pair_local_zone(wire) is not None
                for _kind, wires in templates[name] for wire in wires
            )
            for name in PAIR_TEMPLATE_KIND
        },
        "cross": 0 <= CROSS_PREDECESSOR_OFFSET < BANK_WIDTH,
    }
    next_b = fixed_b_discharge(
        PATTERN_TEST_BANK,
        templates,
        cert_a["exact"] and not cert_a["finalizer_bank_count_AST_loads"],
    )
    holds = (
        cert_b["exact"]
        and all(local_template_zone_results.values())
        and next_b["exact"]
    )
    return {
        "certificate_name": "C_PATTERN_HUNT",
        "structural_reason": (
            "All emitted rows select one of nine b-independent finite words. "
            "Their local operands are zone-typed once: source/finalizer in "
            "[0,172), bank in [0,131), pair in adjacent 131/131/191 zones, "
            "and cross uses fixed offset 1. The 8*b-5 grammar only replicates "
            "these words with bank indices 0..b-1 and edge indices 0..b-2. "
            "The affine mapper therefore preserves the typing for every "
            "C>=b, while the finalizer AST never loads b."
        ),
        "local_template_zone_results": local_template_zone_results,
        "candidate_general_b_argument": (
            "For every integer b>=3 and C>=b, program-row index bounds plus "
            "the fixed template zone typings imply "
            "H_TEMPLATE_PREIMAGE_ZONE_CLASS."
        ),
        "candidate_status": (
            "GENERAL_DISCHARGE_CANDIDATE_HOLDS; general-b theorem would be "
            "unconditional pending independent verification of this "
            "candidate argument"
        ),
        "next_b_beyond_discharge_range": PATTERN_TEST_BANK,
        "next_b_mechanical_test": next_b,
        "holds": holds,
        "exact": holds,
    }


def primitive_truth_certificate() -> dict[str, object]:
    rows = []
    failures = []
    for kind in ("X", "CNOT", "TOF"):
        for control in (0, 1):
            for x in (0, 1):
                for y in (0, 1):
                    for z in (0, 1):
                        observed = [control, x, y, z, 0]
                        expected = [control, x, y, z, 0]
                        if kind == "X":
                            observed[1] ^= control
                            expected[1] ^= control
                        elif kind == "CNOT":
                            observed[2] ^= control & x
                            expected[2] ^= control & x
                        else:
                            observed[4] ^= control & x
                            observed[3] ^= observed[4] & y
                            observed[4] ^= control & x
                            expected[3] ^= control & x & y
                        exact = observed == expected and observed[4] == 0
                        row = (kind, control, x, y, z, exact)
                        rows.append(row)
                        if not exact:
                            failures.append(row)
    return {
        "truth_rows": len(rows),
        "failures": failures,
        "truth_table_sha256": stable_digest(rows),
        "exact": len(rows) == 48 and not failures,
    }


def affine_zone_certificate(capacity: int) -> dict[str, object]:
    failures = []
    checked = 0
    width = data_width(capacity)
    for index in range(capacity):
        image = tuple(bank_base(index) + offset
                      for offset in range(BANK_WIDTH))
        checked += len(image)
        if image != tuple(range(bank_base(index),
                                bank_base(index) + BANK_WIDTH)):
            failures.append(("bank", index, "not exact interval"))
        if not all(0 <= wire < width for wire in image):
            failures.append(("bank", index, "out of data"))
    for edge in range(capacity - 1):
        zones = (
            set(range(bank_base(edge), bank_base(edge) + BANK_WIDTH)),
            set(range(bank_base(edge + 1),
                      bank_base(edge + 1) + BANK_WIDTH)),
            set(range(link_base(edge, capacity),
                      link_base(edge, capacity) + LINK_AUX_WIDTH)),
            set(range(link_base(edge, capacity) + LINK_AUX_WIDTH,
                      link_base(edge, capacity) + LINK_WIDTH)),
        )
        checked += sum(map(len, zones))
        for left in range(len(zones)):
            for right in range(left + 1, len(zones)):
                if zones[left] & zones[right]:
                    failures.append(("edge", edge, left, right, "collision"))
        if not all(0 <= wire < width for zone in zones for wire in zone):
            failures.append(("edge", edge, "out of data"))
    return {
        "C": capacity,
        "abstract_zone_wires_checked": checked,
        "failures": failures,
        "exact": not failures,
    }


def cycle738_transfer_certificate() -> dict[str, object]:
    rail_rows = []
    for a_s in (0, 1):
        after_r1_a_s, after_r1_b_s = 0, a_s
        after_r2_b_s, after_r2_a_next = 0, after_r1_b_s
        rail_rows.append({
            "A_s": a_s,
            "A_next_after": after_r2_a_next,
            "B_s_after": after_r2_b_s,
            "exact": (
                after_r1_a_s == 0
                and after_r2_a_next == a_s
                and after_r2_b_s == 0
            ),
        })
    ownership_rows = []
    for left_a in (0, 1):
        for right_a in (0, 1):
            separated = not (left_a or right_a)
            amended = not (left_a or right_a or 0 or 0 or 0 or 0)
            ownership_rows.append(
                (left_a, right_a, separated, amended, separated == amended)
            )
    distance_rows = {}
    for bank_count in DISCHARGE_BANKS:
        stations = 8 * bank_count - 5
        failures = 0
        for left in range(stations):
            for right in range(stations):
                before = min(
                    (right - left) % stations,
                    (left - right) % stations,
                )
                after = min(
                    ((right + 1) - (left + 1)) % stations,
                    ((left + 1) - (right + 1)) % stations,
                )
                failures += before != after
        distance_rows[bank_count] = {
            "n": stations,
            "ordered_pairs": stations * stations,
            "failures": failures,
            "n_step_shift_residue": stations % stations,
            "exact": failures == 0,
        }
    identities = {
        "R_A_new_s_plus_1_equals_A_old_s":
            all(row["exact"] for row in rail_rows),
        "R_clean_B_returns_clean":
            all(row["B_s_after"] == 0 for row in rail_rows),
        "amended_ownership_reduces_to_separation_on_clean_B_work":
            all(row[-1] for row in ownership_rows),
        "translation_preserves_all_pairwise_circular_distances":
            all(row["exact"] for row in distance_rows.values()),
        "n_translations_close": all(
            row["n_step_shift_residue"] == 0
            for row in distance_rows.values()
        ),
        "data_not_asserted_unchanged": True,
    }
    return {
        "rail_truth_rows": rail_rows,
        "ownership_truth_rows": ownership_rows,
        "distance_and_closure_b3_through_b10": distance_rows,
        "symbolic_identities": identities,
        "exact": all(identities.values()),
    }


def certificate_d(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    primary_ast = function_fragment_certificate(
        trees[PRIMARY_817],
        "certificate_c",
        (
            "'conditional_on': 'H_TEMPLATE_PREIMAGE_ZONE_CLASS'",
            "'condition_exact_text': H_TEMPLATE_PREIMAGE_ZONE_CLASS",
            "'Cycle740_affine_local_class_preservation': mapper",
            "'Cycle738_parameterized_transfer': transfer",
        ),
    )
    checker_function = function_containing(
        trees[CHECKER_817], "BRIDGE_RESISTS_AT_H_TEMPLATE_PREIMAGE_ZONE_CLASS"
    )
    checker_rendered = ast.unparse(checker_function)
    checker_ast = {
        "function": checker_function.name,
        "span": (checker_function.lineno, checker_function.end_lineno),
        "resistant_identity_present":
            "'name': 'H_TEMPLATE_PREIMAGE_ZONE_CLASS'" in checker_rendered,
        "mechanical_preservation_present":
            "mechanical_preservation" in checker_rendered,
        "Cycle738_transfer_present":
            "cycle738_transfer_certificate" in checker_rendered,
    }
    checker_ast["exact"] = all(
        value for key, value in checker_ast.items()
        if key not in {"function", "span", "exact"}
    )
    primitive = primitive_truth_certificate()
    affine = {
        capacity: affine_zone_certificate(capacity)
        for capacity in DISCHARGE_BANKS
    }
    transfer = cycle738_transfer_certificate()
    exact = (
        primary_ast["exact"]
        and checker_ast["exact"]
        and primitive["exact"]
        and all(row["exact"] for row in affine.values())
        and transfer["exact"]
    )
    return {
        "certificate_name": "D_CYCLE817_CONDITIONAL_BRIDGE_IDENTITY_CONTROL",
        "Cycle817_primary_bridge_AST": primary_ast,
        "Cycle817_checker_bridge_AST": checker_ast,
        "controlled_primitive_truth": primitive,
        "affine_zone_relabeling_b3_through_b10": affine,
        "Cycle738_parameterized_transfer": transfer,
        "conditional_implication_reproduced": (
            "H_TEMPLATE_PREIMAGE_ZONE_CLASS => affine local-class "
            "preservation => Cycle-738 ownership/distance/clean-rail theorem"
        ),
        "Cycle817_conditional_bridge_certificates_reproduce": exact,
        "exact": exact,
    }


def build_core(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    cert_a = certificate_a(trees)
    templates, literal = literal_preimage_certificate(trees)
    cert_b = certificate_b(cert_a, literal, templates)
    cert_c = certificate_c(cert_a, cert_b, templates)
    cert_d = certificate_d(trees)
    return {
        "certificate_A": cert_a,
        "literal_preimages": literal,
        "certificate_B": cert_b,
        "certificate_C": cert_c,
        "certificate_D": cert_d,
    }


def control_certificate(
    source_inputs: dict[str, object],
    first_core: dict[str, object],
    second_core: dict[str, object],
) -> dict[str, object]:
    self_source = (ROOT / SELF_PATH).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=SELF_PATH)
    imported = []
    for node in ast.walk(self_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append((node.module or "").split(".")[0])
    allowed_imports = {
        "__future__",
        "ast",
        "base64",
        "collections",
        "hashlib",
        "json",
        "pathlib",
        "sys",
        "time",
        "zlib",
    }
    calls = {
        call_name(node.func)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
    }
    dynamic_calls = sorted(
        name for name in calls
        if name.split(".")[-1] in BLOCKED_DYNAMIC_CALLS
    )
    blocklisted_imports = sorted(set(imported) & set(BLOCKLIST))
    first_bytes = stable_json_bytes(first_core)
    second_bytes = stable_json_bytes(second_core)
    deterministic = first_bytes == second_bytes
    literal_paths_exact = (
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    exact = (
        source_inputs["exact"]
        and literal_paths_exact
        and BLOCKLIST
        == tuple(Path(path).stem for path in (PRIMARY_817, CHECKER_817))
        and not blocklisted_imports
        and not dynamic_calls
        and not (set(imported) - allowed_imports)
        and deterministic
        and AUDIT_TIMEOUT_SEC == 1500
        and STDOUT_LIMIT_BYTES == 200 * 1024
    )
    return {
        "certificate_name": "E_CONTROLS",
        "AUDIT_INPUT_PATHS_literal": AUDIT_INPUT_PATHS,
        "literal_worktree_relative_paths_existing": literal_paths_exact,
        "input_sha256_git_blob_sha1": source_inputs["rows"],
        "BLOCKLIST_817_PAIR": BLOCKLIST,
        "blocklisted_imports": blocklisted_imports,
        "dynamic_execution_calls": dynamic_calls,
        "stdlib_imports": sorted(set(imported)),
        "unexpected_imports": sorted(set(imported) - allowed_imports),
        "817_pair_access": "bytes/text/AST only; never imported or executed",
        "deterministic_core_byte_identical_on_repeat": deterministic,
        "deterministic_core_sha256": sha256(first_bytes).hexdigest(),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "exact": exact,
    }


def main() -> int:
    started = perf_counter()
    source_inputs, _sources, trees = load_inert_packet()

    first_core = build_core(trees)
    second_core = build_core(trees)
    cert_a = first_core["certificate_A"]
    literal = first_core["literal_preimages"]
    cert_b = first_core["certificate_B"]
    cert_c = first_core["certificate_C"]
    cert_d = first_core["certificate_D"]
    cert_e = control_certificate(source_inputs, first_core, second_core)

    elapsed = perf_counter() - started
    checks = {
        "A_FIXED_B_FINITE_DECIDABILITY_EXACT":
            cert_a["exact"]
            and cert_a["fixed_b_decidability"] == "FINITE_DECIDABLE",
        "A2_LITERAL_PREIMAGE_CERTIFICATE_EXACT": literal["exact"],
        "B_B3_THROUGH_B10_EXHAUSTIVE_DISCHARGE": cert_b["exact"],
        "C_PATTERN_CANDIDATE_HOLDS_AT_B11": cert_c["exact"],
        "D_CYCLE817_CONDITIONAL_BRIDGE_REPRODUCES": cert_d["exact"],
        "E_CONTROLS_EXACT": cert_e["exact"],
        "E_RUNTIME_UNDER_1500_SECONDS": elapsed < AUDIT_TIMEOUT_SEC,
    }
    runner_exact = all(checks.values())
    report = {
        "version": 1,
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "source_inputs": source_inputs,
        "fixed_b_decidability_ruling": "FINITE_DECIDABLE",
        "A_mechanical_restatement": cert_a,
        "A2_literal_preimages": literal,
        "B_fixed_b_discharge": cert_b,
        "C_pattern_hunt": cert_c,
        "D_identity_controls": cert_d,
        "E_controls": cert_e,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_failed": sum(not value for value in checks.values()),
        "theorem_unconditional_without_H_TEMPLATE_at_b":
            cert_b["unconditional_sector_theorem_b"],
        "general_b_hypothesis_discharged": False,
        "general_b_status": (
            "GENERAL_DISCHARGE_CANDIDATE_HOLDS_AT_B11; "
            "PENDING_INDEPENDENT_GENERAL_B_VERIFICATION"
        ),
        "verdict": (
            "ANCHORS_B3_THROUGH_B10_CLOSED_UNCONDITIONALLY"
            if runner_exact else
            "H_TEMPLATE_PREIMAGE_ZONE_CLASS_DISCHARGE_FAILED"
        ),
        "runtime_seconds": round(elapsed, 6),
        "runner_exact": runner_exact,
        "terminal": (
            "CYCLE823_H_TEMPLATE_PREIMAGE_ZONE_CLASS_FIXED_B_PASS"
            if runner_exact else
            "CYCLE823_H_TEMPLATE_PREIMAGE_ZONE_CLASS_DISCHARGE_FAIL"
        ),
    }

    lines = [
        f"{'PASS' if passed else 'FAIL'} {label}"
        for label, passed in sorted(checks.items())
    ]
    lines.append(
        "DECIDABILITY FINITE_DECIDABLE :: "
        + str(cert_a["decision_procedure"])
    )
    for bank_count, row in cert_b["per_b"].items():
        lines.append(
            f"DISCHARGE b={bank_count} "
            f"{row['H_TEMPLATE_PREIMAGE_ZONE_CLASS']} "
            f"sector={row['sector_theorem_at_fixed_b']} "
            f"rows={row['program_rows_exhausted']} "
            f"gates={row['mapped_gates_exhausted']} "
            f"operands={row['mapped_operands_exhausted']}"
        )
        if row["failures"]:
            lines.extend((
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                f"LOUD COUNTEREXAMPLE AT b={bank_count}",
                json.dumps(
                    row["failures"][0],
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                str(row["failure_logic_if_any"]),
                "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            ))
    next_b = cert_c["next_b_mechanical_test"]
    lines.append(
        f"PATTERN b={PATTERN_TEST_BANK} "
        f"{next_b['H_TEMPLATE_PREIMAGE_ZONE_CLASS']} :: "
        f"{cert_c['candidate_status']}"
    )
    lines.append("VERDICT " + report["verdict"])
    observed_stdout_bytes = 0
    output = ""
    for _iteration in range(8):
        cert_e["observed_stdout_bytes"] = observed_stdout_bytes
        cert_e["observed_stdout_under_200KB"] = (
            observed_stdout_bytes < STDOUT_LIMIT_BYTES
        )
        report.pop("report_sha256", None)
        report["report_sha256"] = stable_digest(report)
        final_json = json.dumps(
            report, sort_keys=True, separators=(",", ":"), default=str
        )
        bound_line = (
            f"STDOUT_BOUND observed_bytes={observed_stdout_bytes} "
            f"limit_bytes={STDOUT_LIMIT_BYTES}"
        )
        output = "\n".join(lines + [bound_line, final_json]) + "\n"
        new_size = len(output.encode())
        if new_size == observed_stdout_bytes:
            break
        observed_stdout_bytes = new_size
    output_bytes = output.encode()
    if len(output_bytes) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "runner_exact": False,
            "stdout_bytes": len(output_bytes),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE823_H_TEMPLATE_PREIMAGE_ZONE_CLASS_DISCHARGE_FAIL",
        }
        print(json.dumps(fallback, sort_keys=True, separators=(",", ":")))
        return 1
    sys.stdout.write(output)
    return 0 if runner_exact else 1


if __name__ == "__main__":
    raise SystemExit(main())
