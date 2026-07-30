#!/usr/bin/env python3
"""Cycle 811: the rule-level W2 source-bootstrap mechanism theorem.

The four copied primaries are inert text/AST audit inputs.  The executable
experiment below is a stdlib-only reimplementation of the exact frozen
two-bank gate fixture used by the 752 lineage.  Its transition rules are
expanded into source-emission and clean-return predicates so the certificate
explains the boundary-0 obstruction rather than merely correlating it.
"""
from __future__ import annotations

import ast
import base64
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
import zlib


# Literal, existing, worktree-relative, text/AST-only audit inputs.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle783_functional_order_w2_2026_07_28.py",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py",
    "scripts/frontier_cycle810_satisfiable_start_discriminator_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "d773f3ce86d7c7f6fba9d49cddb2e9839f4dce26a30310b7b2bb5568418c94c1",
    AUDIT_INPUT_PATHS[2]:
        "d9a8cb70f3c0a99c112b7ca3e962941f7524dc743c56979ef9d4f6b06fa58c5c",
    AUDIT_INPUT_PATHS[3]:
        "2f39e834f89be02bf40bbe9a0d9cac905dc8f4294096faaa7914cfc31fed26a7",
}
BLOCKED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
EXPECTED_SUCCESS_COUNTS = (512,) + (0,) * 10
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 200 * 1024
EXPECTED_FIXTURE_RAW_SHA256 = (
    "3b45537e75b8b1c3157073ff603604b56c9db107511a2d2ab43d4f54ad50ff0c"
)
EXPECTED_TARGET_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
FROZEN_LINEAGE_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
)
EXPECTED_LINEAGE_SHA256 = {
    FROZEN_LINEAGE_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    FROZEN_LINEAGE_PATHS[1]:
        "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
}

SOURCE_POINTER = 40
LEFT_ENDPOINT = 1
RIGHT_ENDPOINT = 6
BANK0_POINTER = 123
BANK0_U_TO_V = 124
BANK0_V_TO_U = 125
BANK0_DIRECTION_OK = 131
FINALIZER_WORK = 132
SOURCE_PROTOCOL_WIRES = (
    SOURCE_POINTER,
    BANK0_POINTER,
    BANK0_U_TO_V,
    BANK0_V_TO_U,
    BANK0_DIRECTION_OK,
)
SOURCE_PROTOCOL_NAMES = (
    "source_pointer",
    "bank0.pointer",
    "bank0.u_to_v",
    "bank0.v_to_u",
    "bank0.direction_ok",
)
CLEAN_SOURCE_RETURN = (1, 0, 0, 0, 0)
NAMED_CONFLICT = "UNCLEARED_SOURCE_EMISSION_AT_CLEAN_RETURN"
CONFLICT_RULE = (
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py:"
    "source_finalizer_word"
)
RULE_PROVENANCE = {
    "initial_two_A_tokens": (
        "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py:"
        "initial_full_state"
    ),
    "boundary_Q_pair": (
        "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py:"
        "q_block,fixed_q_order_tick_blocks"
    ),
    "token_successor_transport": (
        "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py:"
        "lift_block,land_block,route3_adjacent_full_battery"
    ),
    "program_rows": (
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py:"
        "interleaved_program,mapped_macro"
    ),
    "source_emission": (
        "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py:"
        "source_compute_word"
    ),
    "body_mapping": (
        "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py:"
        "mapped_action"
    ),
    "clean_source_return": CONFLICT_RULE,
    "allocator_target": (
        "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py:"
        "global_allocator_word"
    ),
    "boolean_gate_update": (
        "scripts/frontier_cycle810_satisfiable_start_discriminator_2026_07_28.py:"
        "apply_word_int (text/AST anchor only; reimplemented here as apply_gate)"
    ),
}

# The exact frozen 752/719 two-bank fixture will be inserted in the next
# incremental commit.  It contains only integer wire constants and X/CNOT/TOF
# rows, never executable copied-module code.
FROZEN_FIXTURE_B85 = (
    "c-rlK-OlAkuHC!z^}bNCR6m+mF?`|7naMHYj04XE$vHvZJtB*gNG^4wVYeG;dmAvmQg3bTQmOd2NOAq25C7}OfBV<JfA~wArM*7<"
    "_>Uj|_2UmeefZ0V?SGfQZJ++H{&oBNfRl<1_U*&#!~gi@=l}Z45C8qcU%vb9!#{uipTGR|Zy#RU>$~sDYu{dl>i4hjh==_=*zKU4"
    "2kkuIzx%7yqT?px@6V$T|K*2&{5QK&DaZN2rYCJW-d=lIe`x)w>(9RawDqU2KV$uw>(3#7+PX?xS83}iZC$0UtF(2Mwyx6FRoc2r"
    "TUY7pDt%q0udDQRmA<ah*H!wuN?%v$>neR+Wvr`=b(OKMGS*ebS~p#V^M6{$m3V>Azg3TUe6CQ{^Xs{^bgp}CdVDS~jq`8UV}2&{"
    "{5$mc{EYZFrXJ68h0i~S9v<gPzskO?!<|?B{8RMseBkHr?K-#f%>DeiU8i=Qxu3tb>&(tG_w&bgo!EKie$Hdpd7WqO=QMVm)_G<-"
    "?|Ro+ooBXlR=dvXJhPpDn$D{66FmRutj;srIjg3#I?rt9teVd1JhPp%YC5a)%y!PI>8#E(+c~SIvpUag=d7B}>O8ZbvuZl4^UQwE"
    "s_CrGGyD0c>#REOi1Uxm>O8Zbv+6pl^UQwEs_U%IGy6HKuCqGN?B}ey&gwj~pR?*ZtMkl$&Z_II&NIh3tFE&;&m8Bhy3Xo6bDV#M"
    "&T8-uJOAjc&NBz^nDY2(`fk2*`rS0EH0N|j>3-8{q_v7GnbtW!h4hTl6HL!HJ^i#d(#}cyD(<?pC-aU?`#J6QBnwGWk{l%|OEMTG"
    "G|6w4?kxOSIb`LLl}lDWNjU}Or8@1_a1^xP<~5_~$q{sD3;MMN-CMj~RxNEhdjx&ng08Q@4is-A)MA+Z7{Ru*V0UV;NqR@?l(D`r"
    "*4M|n*jSgI>xbt0!dzdU>tb_VdakR?b(OiUGS^k+y2`Pxa;&Qy>ng{(%CW9;tg9UBD#yCYv95BgtDF{I{}%mA`nT%eUH>-y+x73z"
    "zq*N*t^TSOYqVgoMh_Nij9{_G3>Iq~!D7uVSgcus#hMf>)~vx|%{^GG*@DHIJy@(cg2kFMSgd&ji*;<lVjU$|tb>BZI%=?3#~v)!"
    "(SpS~dazi>2o~#@!D1apuvq7o2`1~@I>Bb0TPPT<b1Ma_b#AF(w$7~;?AE!(g5f&1TCiN_mOHlsJ%66R57*DXpXZn7pYJc<e_Ecj"
    "cyVdd!so}59$I>&>4B&1kTy%&N@=6TZJ0J`-oj~vr|qAFBZ*EDtR!|xD5J<GfzIOoJDaee%}mRAt=E%Q+>_R%q*XVsbWH`1pq^V$"
    "-8HE7;#IyH05b<8n2Hw6NDU^Yc=Myi$V}4+W~+T73@K5m%d$D8F3akbdQVDyB&9xsQkTbS(hQ&H@8|31-_P?)^UwDu+U0odPT3SS"
    "@OD^UwtwZ2UbegCu)b{X%i;bq$&kbLGP#k%{xYeO!|^hilf(HkiPZ0gr%-x)3T4Enz+Z14`8a(&U;cA{uFT(dy)r(1e(4JZSjXYB"
    "R>Cqi3d`7PT*m#njwsVL6cw$*c@K|kIJSFupDSLh4&8&N{pBpwF5Bon<Qu-9B|GZHoy<?`z5#af%Y6eJ0+jvFDUFXVC4J-fOCK>Z"
    "xAqw=XrIx8_8B8+pD}~>8As4QGis0-#b!panNe)!{+qPVJpQoSXSTSEJuc&j%Xll7qufJx^^M%Py7BJD{`}#_Gw7h@k0`*?f)Zk9"
    "$|)gswVV=SN6aZ9cGH{^VkfTn*&KgP0c8ax3d<=dIiGI4x*Tqw@%bBmCjU<9I>lY5IG~(#yy;(B_ds#oIS%^Nvj3V;+u*@p<6Ng@"
    "4b#iBH`L$lA`a2M`0daayPY^cKmW}=x$VwmXjVhg9smBrKmP6KzyEz@JkE0z5i1Ii6~)VnB1uJk@}e$!QIEZ-17FmiFY4YG_4bQ8"
    "|3zbgqM<?2NTF!pP&AGx8demIGKvNrMPrbnAxY5)rD(uXG=3=>&J>MqiUvERu@7l1L>e2B#!95I6KO0(8e5UZTBNZTZF;?;*DHFx"
    "qSq^Wy`tAEdcC68D|)@6*DHEG((934kMw$^*CV|i>GepjM|wTd>ychhGghQhOS&(p>h-E#uj=)xUa#u)s$Q?^^%SKf1uaQ&N>bR8"
    "c0JzhSkG5@k`%2Z1usdlOj2l*6zL=dK1m@~QpA-MfF;FaN#R*iw3ZaSCB<?{p<U8_O}ej1_ciIhCf(Ph`<irLlkRKMeNDQrN%uAB"
    "z9!w*r2Cq5Uz6@@(tS<3uSxec>Aoi2*QEQJbYGM1Ytns9y01z1HR-;ty05G5>uUR2L1|K~nG|}aX6vW&r2DSuzAI$<!~Uwg>3%7?"
    "UyAORqWh)jekr<NitdM^`=RK5D7qht?uVlLq3C`nx*v+}hobwT=zc4@--_<XqWiJveHOjXqW4)8fG>*27lr4GqV+}Bsn~kxzAL)#"
    "itf9j`>yD|E4uHB?z^J<t_-u1+ht`XQDx!NIZ*7+{JGAK9!ZYL;68CB8SgXyu(Pwt=AfI$c@CDr=w{Em7<9q?40aTg&cL7<(Q|Na"
    "0sa<U$SR%xBHuFf@SF=Z`PKz5?&pS)MY1__=6uM&=FGF>{9PxTGtX{FD$VB1vty62lg(KiDZVdTuU^H-@WAHGE5WW|H{0CV_zeL("
    "FF?4m3F3jxnGGnzfW2OzX=Ag*1Di7&VFnVrS>euRnvuqC-dtyQZ%Tg9=3EapU%W+Z&bt^g9@v~Y_-3@T8*I}#{$@C|8*<Y*1V3b}"
    "T`=~}29F0eXAZ;<8C+0sXCuf1n=|L@7_;pL<aAExF{s-O%jul)6V%t>oZiG(^1$ZIIYYsX4aw-7R1{#@z>IUirj!RZ=eDy^<-rBM"
    "H#V<4usOHRhL#5xz&+UH^1$YN?m-fa+>q#Vz-E|5&*t34AoIZH+zXp#9@v~av61G1&AC@L*F3N}_ni$l4{Xl8u?gqFl``mT%z0pQ"
    "?t{%b4=&h#vVrG;&AA_J>RC<LoQD{F9@w1E;DuOv`>;8ml0-%F*EZ)<l88jz*ql#EB6i8UMds&#-2@)koKHz2(In$abPRSKcwlor"
    "C5c#i`?!)32fGuj(ynxcI2JsxIiHe5qFXFnKL_k=@WAGLN)lC3jW*{~l1TKJ1*_+PT@fDGoKHz2mfmh5>p5Wega=o8X0oHg1Do?H"
    "NyO6I51aEL&I=E&Burs9h6gt1Q<8|Kw;wj=gLRz@Y|f`75$D$XVRJquiJGW-oAW72)TA20=6p&L?Q)LI`IIEu<(w<2bg)~*rs7H~"
    "iG#$0s|KR5tHgsVwM6VR@xVgiQ<7+x?2>^arz8<;fpJCNrz8<;fw37ba7q%f78sjB1E(ZWmtVK|{gfo?^6M6|pOQqJjT(2<E>0K^"
    "uE4#pJH~@6b|-escyNX9m0dI*T!7Bb&KeIcw4kxu#)AvX=<LAp;DR#-yK+3ZFo(%b9S<&;;b8ZU?UT)!#L?q{&6({WTbXgC@YoKr"
    "l^JFS2irlmGQ;fPU^_S^Sh6{vl0<A}hS|Y$z)m6$Y|f`75nGvIcJLgq<H!S>^C?NhR%VzTJO}Jd^1$YNN)oY^85c@)N)oY^85iz!"
    "N)oY^8D<C10Xv;MusNTSL~Lb-*}-$bjwlao&Zi_1TbW^Y@Eovn$^)D8DM`duW|$p32kfx&z~+2P03G57*ql!ZAht5&%3z!lKx}2k"
    "mBctDpl%X`+MG`bsBC4%mC86Jpl&j-Iq$rm<s6&yDFMV~Gvmr>oDx7>S2M1(MiZx)2R7%%`&kAy=ce$;xIlf@5Uh=d*}=iTLo%>A"
    "x3<FcVRmq|z5@ASc5t+@Lj7TOaIh~{Wrj9q_QhD&4YPxzZwpWuW(Nn~H|x4#c5w8SzB~suXO{I{LV24r%R1|*VRmq^tc#8^J2+U@"
    "MMs$(94zaiqs$HtmUYolW(Nn$y6C7Yg+9c&=Yh?cWnFZX*}*YZBKREGoLSbJc!V}*mUY&><3gxe)|(7$&MfQvgvNzav#iTbxS(p5"
    "b=e6QTFtU9JK+MXrvwl@usO4=^Aj2uY&};>{T$ew#iJC6#O5p>rFgM6XYnXyU~?9alIMIux67mCfz4SwN}jXX!66<c&)MwY5Ra1Q"
    "Y<6&nN6B+GJ2(!lQ5a?ihse6XIW}jJb)K`?!NIaF_Wjc859i=@@V9V2FlW54hkM8M!8OEn#%F=g3!f=Ici0=ae;)Q2?nB(GxSw&)"
    "qg<fupnQQ0qMSa+GRiyZ1k@X-TTuU?jzT>Kx(@Z>gU&>~in<r|GwN{E^JojuUVu$OyYpb1(0-wfLpzAJ674D4T(rwzyV1Ts_yFi9"
    "pf7>`2KprEx1eu>{tx&_=tn*HTIi3V&xU>-`hMsiq7R9FCitT0uRi#+==Y*;jQ%tF*yx9&ua5pa`1}|bJj4zdUtkP^aSFyV81G<A"
    "gmF`jtuX$2iqSBR!&ndFL5vwOuEf|A<5P%XG0uI6g)v^nm>T15jLk8A#~2@R0Kf_mPk6u_5SKvg0`U#RKoBQEECulvz+@1&dBAoM"
    "|3QohaU{f=5RXF43UMvKz7QXKz|at9Lo5#QI>hu4_d{$D@k78E5r=%hDiO~_%oA}@#7+@kMGO{kTEKD<?|s085jRF`8S!Vts1e6T"
    "tQ+xgz|0X>f56@mpGOQIaemANV7>rz3Yd3*+yv$?9&#L*2f<tk=2LRcC1hpp_xrBwjb(EzyK`lGM#=`Ylr5?$n^a=9$+AyZHfp47"
    "RZH2dnzCIbX2UEyc4f;(%BHoHZL298S7Nr#vUgWDZ=`HrOWD90vxSyDyt0W~$TnWt$15AThis)~FYj#T7P6gp_H(4{XiM4CnzE}U"
    "W?wBEdu3-w%HFn=-K{D6TVi(Dvc*^Sc%<xdOWEg|vePAIuPvK>Ww%Glez%kzuQ7XmWz$E>wzrgxuPIxfviX+Xzq0)`Rs&ddz*Q|U"
    "QZ+$K)dn?HBa~RJVATs(HN!~N4lPwf)Ko1|Vl{<TS6tN=BUNLxRIO1{HAjin9#;KvRfCLFEz(joNln!zB~+tWb;@0>GEy~5OVutl"
    "Rl}56Eo0R)S2fK@)iy0v<J45GQ(`rbRrg%gJ|k5FwNx!+)kCX>Ox)yKcUMuoYcu%|%ksH5e<BAM`<6Z|%Uv&<zoKnh|6y64ekuOM"
    "qWj!`SXPi=k<L1iR51L98ef#^Ppm3Q{=>3DlRMvEr3iM3p8v3{sOByMs8ZLtWYvFIRzP%HvnmyzOSt`qWyMmrAzW3eOB?tP%L>D8"
    "8(O7Gbg2*jVObaj`MVZ#zo!q&f;Y(DHG2xJr4P$OM#$ea2ivWu4;56Y{t?!qrsV!mirIeo+fP6I$5qOvLVuOEyh~ZWKq<?+B<t&x"
    "WLasd!~rTKbJG&yX(-9uw8(fGk}@|fL!O4V%uNfGrzzISN|n9vX&Q90_GC|enyQ?vCfS>xrW2<iL}DDO{mati=U}&g*%vB0O`Xl6"
    "=;}1RHH#v!(-hP!iqcNgM6)Q8JI!j$qG<25s9=&J!qXy$Ns1azi!LT9vOG<7O;YrEnvR;J2=z2&G)YnHY0=IkMY^X&M3WQ^pB6Pu"
    "Qp9{(WHm`q^=Z-9tctu((`U0PIzKInn^h6~X_4Nnit<m324~ewz_f^QR?QYniz;W;jKZ|Yb5_kdOp8uu)y%}S2zFM@UQCN}=dKx!"
    "X_4^UH48E=TAsURN~T5BbJuLjw5WUTnsJ#Hna^FbGSi~>xohTTT7*A$&F)M?0p_k5plL|K+%-!y4NaI$GfC4BhuJjSG!2!QO*2x{"
    "kc-(gYc&nsm`yWV(-4r^H2XCTC7Fz*$eayHnT)o`oDFT6jL68G4Uw6Q+Q^&@wV8cec<VG|XEORDb2gPQ86lE68$vW0MUpuiiZmH%"
    "k~tgFG#QN=GO#%_V#N{uG{kB$s>LY4G*oLc^2JEOG~{bCI>u<iG<0l^ZQ<I}5VXlC8>14_P`1fP93vOgkhsZc-4wUf=FEs5BOucd"
    "y~(KGl!48ekwHdMrXhoq(L+XCrlE(E5k^L2rXh@zQAkE@rlF8?ZYzH<4XK=rW-|IS4b7a4crrpX4e^|eiXP%p+ngCWJp?zhIWxL?"
    "$iU{z2rMI3(-7FnC@rH}(@@&UNG>B^(~#WBXfLB<)6m{|Y%5PQ4H2G<8Z*i^4K<#OEHe@}4Ou=1D<?D!eLe>(Z!`^|J_jqeG!4a`"
    "jC6~f8qz%(4Hvy(X!vBrT=a$^=95u%)*FYR>c_S%?`&@S$If}W4*nL-2j`6Uh4+r@gKG%ujL+iXdEqm~=Z<>=_Ydwd+=sYVVL#)Z"
    "e~=559h5JWL6lRJWt4Z+37|Jnw>;<{)KRF%P}iY8M4gFx6?HG@XVl>jdLC^7+6%NPXm`*yq5VP|2X+u`<%2y%n~QcCZ8zF?^a0RM"
    "Kwkp<4fIJK{1)_W(EmXn3H>Pawa_0!pAGyv^!*<EL-Zlh&qQAo{Z;g7(eFjy82o4Su^;?!^wrUyN1q?#0*oCnzQ7m+;uMT!9^xI0"
    "i7;-;u~iJe-r)7u0<Ygmm@k!t(d(R|o6)g^=gn>ZJUnlm_!)TKI`K2`JUQ`Wc;4#8S#-iCVnqruOx)gYtok=r$<|55iNw|5=Sk}8"
    "uros9?&$gKFo~1W^|*_QCH1J-<sor&rXEjG)1+S6DkCBld(uLqs_KBW6lqsAL0YWTRDF<^Gj&xfqy<ky)eUJ$)KoP@S~PX2dLnfr"
    "O>Jr66+6l5=`L54RLzk(t5ww>sXM!?S|oLNo2pAvm$<7MC3Bipy^^}sQ`Ii1<9(<)rsbL+rlz%+jROyj9>l$u&_w5V$X-!(Pb);="
    "!Xk}PB#7YBBaLDt%-|47;~WV@IEd0nNJ143vouzcV1@%Rjixx<;gSy0c#8ufF8Uyi$T(!;vXH7V8wXWfI8wEqio-50EvZ^@#eo?Y"
    "pHQQZd>+4_uaCc<=a=W7?=RnfUZ1>vd41FR=jQ{@FF)V>{PX_E`zP<Oy#Mn4O#3(QZ`l7?KC=8|`O5N_<ul7~mhUA0SwDdO$oeJg"
    "pRAv<{!02S=)ZR^Hs)gA9Svef12SLYtJ+I0*Yoz03;Mjh<dQ#cFS#ht+e<DR^!Abq3%$MM(nD`Axj50=OOk@%+g_5C4Bz&WOCY_y"
    "<RVFLFS(4;+e<FA^!AcVF}=OyVoh%^xt!D6OD_2I_L8K?`nH!OW!Sg9<g!w4FS+p4+e<D@_4bmBSG~RD@>Xvzxd7JNOD>W1_L7Te"
    "gT0i(b!RW7wB6au+M~TZ!|Y%$&p<rbOD?fj6bC<#-_O^_-_P^Q^UwE}??10kUcbD)Y5nu_f#;W>Z+`xHf8_m>_gCJ3d4Hz;oA)>D"
    "|12L_ezJUJ`OET|<u}WBlK-q9es_CWqP=|AaydKsv3QE2eUSBZ_CeO$+lP_t!;JPpo~N@9eY@lzKhNLK*U!J7=a=T6?oag5ZvKKD"
    "7xg3TnAE?p<Enm#9q;Oo*l|-o#g4oBFLpfCud(B){*E0V>IdE556?qhnR3r#pYeIf_xndakKfPN|Lot}kKcB^eSZ3UE%VajxR#UR"
    "TF#o*a!+g7u4@(T2`J;Ey76)U-nO}MapUU7yBoW`uwE;;jwKe@H+NjMaL<l+t<SULre%0`+_l=yj)xZ2{rP0|*>|nq`2E(8*rr=I"
    "nQk`SMB50uiMAPZ6KzM(O;om^o2Vq+QldOjiSk4x$`h6Ln{*S=_J`F?RC-#=k=AmiwRC!i$c^1^RHt{U(>t}fu|I#h@ey@Xb@P)K"
    "6W!imzs%_-@!NKfa~(l9iQngRllX<Zo0DGq&nCB`w?vOQy(Q<@8_#c>yOzCkkUo=tujxAEu0wYsLC&L4QYrV)(z<iJ^{I9LHL-r9"
    "U+=5ubq({&^EaE|?uTQ+FMdDu%iT|ypP&Eco?UUdo|X5JgwS7q`T3v!yx7^K7W{NeztQa0yITESt^UWUR_9WQRX-7`)dy6oPpDQu"
    "QnmW3=ZMwn6ROpZT&=!pM_jeK)|dEd^;Lu7tJPPXN~l(^P_4d0wR(eU^$ykQ1FF?0RI4AkT7A{=glhEy)#?P*>J_Thcc@lxP_5pf"
    "T75vZ`h;rrBUh`hdZ|#YUZ7f?pjy2`wfYX#>J6&ZJ5;L=s8*j)t$yTc^;MS^s?`frs}oeKSEyFsp<2B`wR(qY^#RrD6ROpZT&=$9"
    "|3bBT$<^wsj?h)BYpr3ZR^Opoy+O5lhidf!)#?+f)sI}QzUnMPwR(YSb%JX33f1a6RI4|rR_{=)KA>8CLbdvltJPOMYp7N)P_0f-"
    "tzMy8eTQoG2G!~vs?`Tnt52v_KXSGDsv8c~>IJIR398jARIBe$t=^zoy+gJ7fNJ##)#^v8R@eIMP_15|TAfn0y4HgGYV}nw9;($F"
    "RIB$~t)6Pr@f^Gk{ua&$=ZyD-_m1lWYl!Ro@GS6o;WNeOj(Y?55AHGChp<<1KR@hwlnay{lrNM)lv9*tly}exs5c&T3+f-#QK-jI"
    "*P%W{or!uCbT8`X2OW-j9&G{I3$!U{chEMW{Q?_@cJRSgqCG{Mi*^}pH`;gf0nkqXUjqG&2cHD}7W8e<|3M!K{V4Rc&>sVz4gI<Y"
    "-w*vm^dZsDL|+vBRrG1m?*-o&{pSZC8~t$f)zP0vpC97_j2$q(fEWbhl!sUb;~k8Na@-U{t9K>(yAu5yuS5@|L;wHxmUunkb6Pe~"
    "irt%?r}wO72gO=TX<0(iGKHdL3q{Kq-oz`v6aM!ucl<m8r#DXeRd7<F2;Vai&}vf`h=6(~0$L650uj&zBA_D?0j-v$o(O0)bo4|("
    "t9@f20+JSwfe1)iMFt`uxeHGOv|3JjA|P$`=ZJu`9iSru(w2da2xzqx3`9WE$TJWDNwd#D1hfGWPyr&K0z^Osh=2+Z0TmzuDnJBO"
    "fC#7n5l{glAZcP6h=7PP5m2Q}1SBn80}+t4eGNoF(i%1p0ZIGVKm;T$W&;tBw4n_|K+>u<5CKVBTu%ff4u2p5lAs_E0ZHHxh=3%x"
    "2t+^<fCM5S2~q+PkOVS;2&k-}(GdZa^@_720+OI95CKVG6^MW&_zFZo5}*YlAPM3E5s(CWfe1)~!9WBg0b?KnlAtmW0ZHH)h=3$G"
    "4Mac^zy=~9333AwkOabk2uOnEKm;TKbsz$gpgRx&Nnjp`fFyViL_iYY2O=N=0Rj<_00n^vXi*0QA|PpA8;F3U!EGP{k|wx;2uS2T"
    "5CMt22O=Pm_do<xC=&sRyays6k@r9ZB=R1JfJEK{5s=7xAOaG34@5ws#{v<Mw2%)(K+<MD5CIWoA|R@n2#EGf1SBn60}+t4bqz#7"
    "()u+J0ZDt<Km;T$WCIb9w3!V=K+=jf5CK)nL_pGXKM(;)WBxz{B+dH+5s)<a4@5vh0uYFRgeV{o0STEvAOdQXiGT#g3PeCcq!5UJ"
    "q-}X10+QC|fe1+2p9dl!X^|d?fTWFjAOezB>wySpy(i^~fYzH-o(M?ZwF*Q)gEA42yss6AfaHy?Km;W3d<7yPc`Gas0ZF_1Km;T$"
    "?E?{zw7m~RK++mN5CKX1{6GXWDH8#SrU*np(yHGR0j+lao(O2Q{P#paixwad0SR?LAOaG4fj|T#6a;|?NN5TI5zvu|fEL|>CjwfO"
    "2%ZRN(I$8zphd0ViGUXUf+qr66b+sTXwf)$BA`X};E8}19fT(W(rQ^p1hi-+JQ2{Mp72CKi=M(00WAs(PXr`^@lF5oa1LGve+%b>"
    "bB6oEdw*CTTti%Ed=~h;@R{Os$Grjj2lv>+KE%C>`x*B<$_2^}$`{HY$SKP5gS?|oK)r#w1@#Z=DAZ%9>p&l(&V10TsC!XAqYg(s"
    "kG25q1=<v_J7}98>=)WNw1a3X(Vn8sMZ1i)8|*v!01tiw`V#1GpihE+3;H(b|DcbQ{V4Rcp8PTN+0d^;-w*vm^dZsDL|+vARrF~e"
    "{9g2p(SJrC8~t$f)zP0vpC94^j2#~03yeW9PQh3P;~k8NFmA%w3gRz}(H`PBjP)=c#F!D|N{l@*KE)Uo;#`b{AL3<<sWI-x*c{_`"
    "jPVf%K&$}p1jHO3a0$dN5Z^!y1aT6?QV?%JOa^cp#C9I=AH;|dM?$O#@hHTs5Z6NN3-B?-&>nC$#NrUILrf2GKg0$RKSYcXa7e@|"
    "AMi}XJP{W~>@?x45rKVYQ@<K1#hX0hv&bXfS?Ax0gvK(hSLU^+%<P^rx0EuwDf64N+JFD?A3yx`<A46`m+PGl)5xdN-fdzema5-*"
    "?EE2|Tkcf$^SP#I**3h)PMrt+buA^oa`OG_!w*0G^z&bT_}9<BeE16|-rbka;XNn*_bWxtIreoY@^5!W{M~phH5htlnm;Sk+!DFa"
    "MK(l<jA&0}MLm%j%}93i&R~Cq47SsI?~0Y*p<*SI(mm4FJyF{s{T))|A&nkT?I9iC17#o5`XTin(gPxeAkqvX6(Q0U0;M6+9zIYb"
    "B7GuKEFujfQZ*u-BT_yhEhJD!BE94T1tro{B9$f5T_PnW(q<yHCem*LMJLjDK2Uuk9Vk+UBCRM=k0L!OQkWvmDNvyzUFrj+D$=eZ"
    "H7nA$BE>7xz#>&F(#ZnlEYi|GP}d^8EmGhjO)gUDBHb=h@*-_7Q2QeN?*m0J(g-8fFwzktWiiqkBlR)TBLjsp(kwqvF(X|wQaU5;"
    "Gg3n%eKb-`BMo(?szy5NC(3K2#YXCEq}N6YZlvi(DsQCw21;<G4S%2(NBVK3C`TG|q&i1Bbfip2T6LgaM|$=L3U{P=M=E%vi$_X%"
    "q@71<dZe!hiu<~0elS!BNDeVn2uPkWR0v2eGE@jizA{t@NKP|U2pp6v1SB^aDg-2d8Y%=N#~LaGBo7-Z1SD4*Dg-2-8!7}O=j$s3"
    "R$kaw2&~+(uMp4<Q@%n#a?qhdK=Ra~LO^oap+Z3N-JwFD=L!MAX+wp8;Lo8#Krrf1As`Wds1OjWJ5&e=9v&(L1Tzm60)nfD3IW01"
    "Lxq6g^PxgOF#J#<AUJ=h5RhCzs1T5RL8uUroWd|WIJy#D46}oyD;dTxJ2<)$W(>1~V<@S{FgrMg5^oH%gJUQ;$1poMh7x!Tvx8$O"
    "$;U7|IEE5|46}n{C|SrbJ2-|CiVU-ZV<_p!FgrMg5|a$GgJUXr$uK)OrV^YCvx8$Q3Cb`#IHnS%46}n{Dw)bKJ2<8it_-t-V=5`j"
    "FgrM=61NPqgJUYW%P>1QrV_vmvxDPMl9*w3a2!e`Gt3T-L&;`_*}-urA<Zy5I1VMP8D<B^p~N<Kt;oYUcpdyLoDa+y@9W{-aeZ(N"
    "ah>s5;Pb*~iq9SP2JWASJ%;-b_bTpZ-18_GC_5-$AcH8U53-E%jyeJL2I>~nKd7TnkAbd3efXd=QLm!zMg5FA9Q8cf0<;%kQ_$`_"
    "*e0}JXyechqOC-GiZ&PRGT3gk?+-oz`U&Vupud4W3HmMQ+o1mgJ`(y-555-qW9YM?Ux&UQ`iJO4qMr%ADEg}pJ}vsa=o_Q|j6OE{"
    ";pnTQKMy`X#sv?t1I8B^gJ7J3u?)sL7!zUKlw&K5zn)?=jN>rY!*~#5MvN;l_Qd!UVpxoGA7WvQmocWsxEo`0jNdWFM;rjK0>l#@"
    "FbBjX5W7Hp12GW9Nf1jxyag~B#BCn19mIbSBSIVru_nZ$5VJyD3$QQ5#~v^=#MuywL%a?#J;ePG8$|pNFh;~7AFxWqGZFJdTokcW"
    "#8(l6MVuC}T*P}HFk!@v5nD$588K?au@UP=JRC4{#MK|Lcf{ur!$+JSa{-tyz?=f+9UwP>`HP1f2j)RASAzMJoO20TnRk`O?^dN@"
    "S?zaK*4L@Zvh4YlO&=-S-cmNcrfhx6=393EUG4Q*)n0FUDo;<PFHGFJdy&Mh&E!8U%je$wiPDUFOCOfyu9wYU(YCGsuq;o%_+B8="
    "zMImAWd#Wq>8uk;1;c-+@kQ~CO*oj^_w->|p-J(LO*jtI&f)imWkof`H#XrAZtv;CvI3&pnpLS{wm$9mhh@c5w;`-j0KK$<|FEnu"
    "?6#p*YNwa_@E?Ao?Ofi)EAMv8-%`8f$WHx8VEsgLjYQZ;mJNj3NV@$%%#GyTNbrp$;7AmXWa3CTj-=#3T#n@C4+Q8)l8!{`NVblI"
    ">`2;<#O_G`4g~Q?BL6@%k7V>nSdXOkNPOR|0byvjyhFR?2JMzRv|Ap~Zh7W*%d4?sXt%sUyX6AymI>M|S7^7qL%Zb$?Up;VTOQDE"
    "dFFP@tAS-`x4h+c%c~KlYqzY;GDExN3hkD6Xt&&;-ExO^%LCdi&)jZ#H3|*wmN#g(T%g@DLA&J&?Ur|Fx7?uJa))-y1KKUm+-`X_"
    "WDV_>H)yw9pxrV-yX6Y)mUn2k+@RfZhjz;Y+AYuAZh1An4egdUXt!LT-7-PD<qGYVcWAfVpxttZcFP0WEzi_$SsM(8cFP;ITP~^H"
    "vNkjJ?Uq-=<Irw-hjz;?w_9etaTtz%Y#TIS&gVQ`2Y(CagLB6F!h6T{!8L?+#%J;HyzrUgbH}}b`v><J?nB(Gu%B_yKgb2j4$2qG"
    "Aj&DqGRiyZ1kf9(TORZe>L}D>sOwN4qRvFUin<r{GwSdMJ&(2k?FHHtv^!{<(0-wf13QSe^1+^>%|*M6wj1p``T*!Bpf3Ub2Kpoq"
    "ehd0G=>MRPgnktITIi3V&jx-S`hE}oA^MQ$XQD5P{wn&k==Y*;4E{6v*bja<`s(P<qtB0V0mcp(UtkOZaSFyV5AhDhL>M>a*eZr!"
    "Z@Bv1lKI<h$^7~T2-D={Q_(=1zKDA71zj3lDP1^SM_pE3WnFZA2Kq?!3F!mV=ckWTpRPV^efGK)bZ6*B(S4)aNOzTPGTn2!1$9U2"
    "2G#wl+gEq9Zf=zw6(w__)+)p|gjp4t0jdl2EM}ruAG7W<BUZJ&yqUSG4d~4fR&7ylrt-84d(jQI498Bo4_6nEz3TQPF+KaPyOzW@"
    "?M*i`iSgRI?r{?9wh!I<B<63QDiI|1aX(a0NDOE*`602et*BTn6WmCpZS_-WRfUkmh__v3lf=rmrXow?2DGk{OyVcBp#o0gNVKVP"
    "PvU8`L)8I^E7DC%koYRSsPb6OjC8EA<OA;rRW*W7zoh5QmEL|yQ=BVj|B|jbS0Tbn+Ui`@6))+#bCry|q%qG`2eWe3S8>lvTKilT"
    "OE0McyUMU$t4z!)w_fZ;U!`X8)AZeZ<@CF0R%y=Zj?(?6)ktd<S2C@0ehTRsr6-u4Z+iM^Z={`*_Ep?<X;0=IoAz_s?MW7rq$D{?"
    "QkG;eN@$YbEZtf7vvSDFBP*Aze3Ehs%1d?Ht>GwWzs+k#(~~3U&=&M-4Z62@y{uZ=boL1PyaiofgB>W|MySOw`!RxTX~FK)V3YKY"
    ")+y>TsRyMFmHJoeZmIXB&Y1dU>Z+;drjDHYb?WA+*QZXP`h@Bts>i4fr23QUUaGgL&ZniAE#<7fYEj>{Xo|XM%DSizT&#hKrnrka"
    ")XP?XRg1;YfU{VP9XN}{;DWPQj6OJv#qfl)SaS;&ivbR2u_gtJ#Sn?JSd5`Ki^U*|vsjG6IE%$Fjk8#c<2Z}OK##Ln#}+IWLq*PF"
    "9TY4UgH6t2F&gD87Q<D}Vo9ytZLy>n@3vS{t#?~2Dd)Q_R@t^-vdSt6y!3yOqQTo}6)7vct=1~Jy3JOR(!|?tm8}QERkjf<SCR0J"
    "o<GmuhwJCx&-2Uk&-a(_KP^vMytuS!;qzlj4=p{?^uW`0NSh^XrL@uFHcXo|Z{f7T)Amookwhm6Rua1;lu=}pKxc9PolRKKW~Sx5"
    "*6T?t?n!G>(yE(Rx~76hP|q!>?i$p3@hV>pfSH34OhpT3qy`gHy!laMWTt5Zv(-KkhLot(W!aokmu2-zy(gtUl2V^Rsmo(EX@<}9"
    "_w)7h@8|iY`RDr+?Q*<!r)-KEcsnew>t&fDH9^<gG({?ZuGejf)c0KP;}oglxn9^QQmb>l(Nm-%=X&L5^(?&J30mI`PhmlB_gyYf"
    "?p_7{di%)7>FfFOpZjwL|NYwQmGSBGwRTC5!)L98Wo#6dvDLVY`*oc*uAyQNGMxADxQ1i9hxfUo-b44`X@5BjwU@hUjSuOrP2<CQ"
    "SD=mM#@}z$h?9T6aw8!?+5eo<_~=s7H-5kL5hHVJpV5N$89iv9F@p9PGiaZ21no1U2ANT8W)zzl#b)lmN&8r8^be?gW{b<%<1&u8"
    "jJI+*$~|;f-^h)t8}DxH&mV3)gAOX&JvDZhoDyPZ$|)gswVV=SN6aZ9cGH{^n%h;Is+;uBDWLKuN{I?e&Zir%wlrC_^EdoV{+-fw"
    "in~s6%@|!ht7|p6=60|9*gn1Nzb4c+c<|Ra*J)Y9^z!Tt^>@2SG6Y}xcIb=UPMn{g|K^_Dc4snNR)g!?SEjJY8>E&se7D;4tv1Ql"
    "Nwb2BcY%{sq@g$0RFG6{==s7>GBmqLQkOwejWP6iNG_Q)^yk_R>XxM><B-toB^k?vW;IFQq24vyN&1#`(=4cQS#-^glD?@uG;2!w"
    "F89=ID(Tzahh|wxt6?nrs&9<XqFGt1s3FbP8tHk}EG}tP&aT;A(z>0dSzqM`nO(ENWVJt<B_^#7nwmW(tsgoxt4yoH=&)?FzJ-4j"
    "%|dIHl2lmf{0`YGnzg1?>2&Ox&8Afgbu`U#E9c75HTzAgp6VEy6{l5k#nob3@+CD{Tu-J&VO+Jv@1l~Hjd5KUzpYAISjLrK{61^d"
    "(lf3N<2PQbz6j3MWBg8R)mO#2zKq|RrA8n5Jbpi4AAdj3FV8>UU%vmmK6(A}`lj{I&j+4ge!ltn=lzlQPu^d7|K<Ie_HW+bu>Z4s"
    "WckVRmE|wXXO`bA-%0+negOTE^-I=2SwCg{mGoQCfA5#b;!9-jR?M*#Gnp^(RqZAB8SwU!I}vz$$-N4^z2t5N-d=LQ18*<6BZ9Y="
    "+%v)3OYW-R?IlSkliOaB^g6liCHHRd_L93hczenHAH2Qf4iVm7at{e_FS*Nvx0l?9!rM#kRN?I<Nq3mrUXt{Wx$PzQ!|?W!J7#!$"
    "$vri^z2vSN-d=KF4sS2HbBDK=+}p$3OYZ&=?4@+varRPr@;G~0d$gCQFCFaV8Ic8h$-RLTe#6h>_w)7f_w)Sn{PX?g`_Jo>*DtSc"
    "TL1if;Q8g}o1cH)A9?@e{gwA$-k)jz=KT%(Kg&m!pDbTl{<3^#`OWg3<Ui|&-`!r8XfNL{p*uVIv3QE2eUSBZ_CeO$+lP_t!;JPp"
    "o~N@9eY@lzKhNLK*U!J7=a=T6?oag5ZvKKD7xg3TnAE?p<Enm#9q;Oo*l|-o#g4oBFLpfCud(B){*E0V>IdE556?q-y}9SH&-gs#"
    "`~4%I$M5IsfA;U~$8WpdK0kfFzMrngaV;mswVXAr<(}5EUDqm#w95FXZhYLow{31*+_<{&?#6B}tbRz>vBU!V=8mg&9I)eE8w=QR"
    ")BXW=+_g=B9S`jW@aL1&XWzAc<M&%XVw-N=WV+dO6Kx~tCfa7uO|%_BH&NMwZlaQOONsJCCCU?(C{I+{Z_-Uf+aFdpQR!(dM_S97"
    "*3#)6A~$xwQJvnYPVdy_#{T^2#z)jm)y+>jD!RSFewouv;<xP{=Q@IJ62H&sCh-e*Hz&RJpG|H>Z;2jrdP~l)H=f@%cP(p{ls;>l"
    "`<`8g+;!-FJ3`K*&>2GRp`~@_c<WQ^{%d0WM!()y&+8iIm*;Ob!QBtXf?xc8>X*BpFh4*4%{{x~ay@t6XSJ;v^&5FD=iN%@-Ad;h"
    "Z>7Tt-1Ty2Xr(itmCl4#I!9`yvtBlht#l@|(m8S~o%Ld?Yo((vzxq}>>jhcgN@u-98(Qg9Xr;45E1d?dbUL)s8PG~+LMxpkx6)ZJ"
    "8HZLn1zPD4w9={2N@s^wIt^OsbZDhBpq0*qRys#+rL$h<4y|+ww9+AHrBk7m&JL|~8nn{s&`M`OE1e0gbdKCgXT3BZTIm#Mr9;q4"
    "r$Q^89a`x$Xr<GkmCk@xIulyy9J!UwYEBSZ>6F|`XEix+t#q^zLTIJ4Lo1yIt#mrH(izZ7XF@BTBe&97O&~%modT_N2wLe>Xr;45"
    "E1d?dbUL)s8PG~+LMxpkx6)b7HbN_%0<CliTIp11rL#jTod&IRI<(Rm&`M`QE1e^^(pgPSLMxpDt#k-l=~QT?vqLML2CZ~Dw9*;S"
    "N@qeVog=l<(dIFsl}>?HI+R-JXrmh6N@q2*39WP*w9@Ihl}>7$gXiFN@V9V2IA^>symwq5SVLUrhi8G$3!f=IcibDee{hfCK7_rB"
    "`}twdqg<fupnRbWqMV{Eqr8JoK)vyxTTuU?jzT?#x(@Xr>P*zDpnFk2Kj?7O^JojuUZ71uyMwj~?HAZMw1W?}674D4T(rw*yV1U*"
    "4}g9G_!8)EJoqH&x1eu>{tx;{=trTih5i`$Z0OfL_<ragq7R9FCi<f2ucA+jelPgO=s!RB*yx9&ua5pa`urFdVC;bL1;ij2r#!?m"
    "81G<Al;frtTD{xkyxZjbf!gGJE3K_H`Cp3Ni=C(UsKo=tm@TxpplGo{(c*)m#RzZS_umQcdlxOn;v8d)xELhfxail!MWubhZj3j^"
    "iL+R8n&-{wfj6fc|IYCIJ2UX_=(}2uqvue@w2Q}wHszDLxPI9Al70#|9}p?S)Xf=Gm8t6H721`}>gFD5%6N726Ln)68aL08vJuUj"
    "3rQJ^j+-xOu^L@`Np)M!*UhP9?=v~xC6X68JvY;0r11PryS&cnIi8xl(dl`hy1dlsxuS-=*XjAB=6YYzaZVlU4ab|8YTwp7lQ(zO"
    "zFtoB{8suhuH(R}>+Lhglcmn7<I++G*70qrlj}IS)Dd>PUFs}5ZZCDHZ~m{QPWR0b*3>a~JYwp+JFYQx@EsqS1_6$<OaleSYo@`3"
    "<37`X!||hOP~te$G;q0j*185aHy2yi0LbyRX^`YN-87JLyl)z8Ic_)&$Q*y125pXGP6Io~L#M%?<EqmD@#eD|8bsclcS8eB$BU=I"
    "sN>GlfYtHqX;AAp_%!f!JbfA*J1##BpdH_z2HB1iPy_LsH*jjOesc>>4d@;Jpa%VpqfmhX$787Af#W)C%AI%fA$H~0yEzkwa`4@}"
    "ic@*|ZtlfHx%@7E#$!{yzl+0>LA64G=aG~*@aBT7$}M>FMefQ!cymfN<tV&)C%f_(-rST!xejms%Bg&aH^=3%I1?`(OySBDmfNj3"
    "K24&)r%8*S(Q$6p#o_39Irqi$=(s!E;(~Pio_+B}Iu6jWI3*oV=v=&$j!X1d+>|%pXxSEj<;_XT!EvR)TS|)u({Y>D#g*y!Pxr;A"
    "={Qo`;@osRs(tZtI<D2RxH}ym>s<Vvj<fYx9H2L^E3Ik}$NfsmgXH*ONm)~G4%w>AsyEN<uI#Hf7j099)|;=kD~s#RX*-nZ_2#{u"
    "_O{dE_;c6$P@Ch}l{cm?j$IB_1_d5od+X}v>aF@-*3IX;>zi9Q=Wo+@yKY|Ku57tCckoa~-J4%{D(mjeL3}7P@5NKRZ_3_#HF)8g"
    "yGeoXSl?uGoXAy~f^XjBUD<?hZsn$o!#DqOS61Siqj@NE@y+8rmEHK}dOnl^`Re`BHf2e^dY*7i$q{*__3c2%JzbTN`R1qIm9_ci"
    "ux`rieDhp)Wq-c8u!k~4-+b9qS)^}H?L(QSFWzmb&?=sryBDi@rJLh>v0C38-&L8fZyxYn*|Be~@TLsfH=lT4f$_~g|8Ndo2Y(Ca"
    "gL8)a!h3&MA6!FRXM7g;yzrUgbH}{_`v>>f!#>2liu)P&Jjw;i4$2qGAjm1o@`JpiPC&hZx&`$Q>L}D>sOvx<qRxEKtEhWXKcfyu"
    "J&(2k?FHHtusdj*9_$y|IJARkE76{!%|*M6wj1m_`T!4p0{Rl@Z=g?tehd0G=>MRPl>I35wVwPj^x4p_L*EbmL-Zlh&qQAo{8jX6"
    "AN*eQjnRKb9~=E}^wrUyN1q?!0*oCV;tPyHFiyc(2IC!!i7;-$*b3q=jL{zAIE?i$9>kat<4TM@F+Rl@7UEotg&*Q&jHxm1#@HO="
    "cZ~572SBU<@C3vh9&ic7E)d^93<Pl!#8MD%K}-g48^m@V@E^p85Jy6+3GpbztPs~i><jQQ#LymaHpJo(uR}}^aX-Wc5kEwX5pYPv"
    "Dj)Dn#5@rfMeH=;s}X^HXHUNxC-$4W`m?yJ-&y7_m1U-wS+z{-m3i$cGrOnEEv3wE%KU~bc5D{6$6j&$&RXXW;oNd3uAk2(*9Gl$"
    "b!#r?k6a5^zW@IJ{y*deUak"
)


class _CopiedInputBlocker(importlib.abc.MetaPathFinder):
    """Fail closed on executable imports of every copied primary."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in BLOCKED_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in Cycle 811")
        return None


_IMPORT_BLOCKER = _CopiedInputBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def assignment_value(tree: ast.Module, name: str) -> ast.expr:
    matches: list[ast.expr] = []
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
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def command_output(arguments: tuple[str, ...]) -> str:
    return subprocess.run(
        arguments,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def decode_fixture() -> dict[str, object]:
    compressed = base64.b85decode(FROZEN_FIXTURE_B85.encode("ascii"))
    raw = zlib.decompress(compressed)
    if sha256(raw).hexdigest() != EXPECTED_FIXTURE_RAW_SHA256:
        raise AssertionError("frozen fixture digest mismatch")
    return json.loads(raw)


Gate = tuple[int, ...]
Word = tuple[Gate, ...]


def apply_gate(state: int, gate: Gate) -> int:
    """Exact Boolean gate update: 0=X, 1=CNOT, 2=TOF."""

    kind, *wires = gate
    if kind == 0:
        return state ^ (1 << wires[0])
    if kind == 1:
        return state ^ (((state >> wires[0]) & 1) << wires[1])
    if kind == 2:
        enabled = (
            ((state >> wires[0]) & 1)
            & ((state >> wires[1]) & 1)
        )
        return state ^ (enabled << wires[2])
    raise AssertionError(("unsupported frozen gate kind", kind))


def apply_word(state: int, word: Word) -> int:
    for gate in word:
        state = apply_gate(state, gate)
    return state


def apply_pair(
    state: int,
    words: tuple[Word, ...],
    first: int,
    second: int,
) -> int:
    return apply_word(apply_word(state, words[first]), words[second])


def bit_signature(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def named_source_signature(state: int) -> dict[str, int]:
    return dict(
        zip(
            SOURCE_PROTOCOL_NAMES,
            bit_signature(state, SOURCE_PROTOCOL_WIRES),
        )
    )


def bit_digest(state: int, width: int) -> str:
    return sha256(
        bytes((state >> index) & 1 for index in range(width))
    ).hexdigest()


def state_set_digest(states: set[int], width: int) -> str:
    byte_width = (width + 7) // 8
    return sha256(
        b"".join(
            state.to_bytes(byte_width, "little")
            for state in sorted(states)
        )
    ).hexdigest()


def normalized_fixture() -> dict[str, object]:
    decoded = decode_fixture()
    program = tuple(
        (
            str(row[0]),
            int(row[1]),
            tuple(tuple(int(value) for value in gate) for gate in row[2]),
        )
        for row in decoded["program"]
    )
    return {
        "width": int(decoded["width"]),
        "initial": int(decoded["initial"], 16),
        "program": program,
        "words": tuple(row[2] for row in program),
        "allocator": tuple(
            tuple(int(value) for value in gate)
            for gate in decoded["allocator"]
        ),
    }


def gate_record(gate: Gate) -> dict[str, object]:
    kind_names = ("X", "CNOT", "TOF")
    wire_names = {
        SOURCE_POINTER: "source_pointer",
        LEFT_ENDPOINT: "left_endpoint",
        RIGHT_ENDPOINT: "right_endpoint",
        BANK0_POINTER: "bank0.pointer",
        BANK0_U_TO_V: "bank0.u_to_v",
        BANK0_V_TO_U: "bank0.v_to_u",
        BANK0_DIRECTION_OK: "bank0.direction_ok",
        FINALIZER_WORK: "finalizer_work",
    }
    return {
        "kind": kind_names[gate[0]],
        "wires": tuple(gate[1:]),
        "named_wires": tuple(
            wire_names.get(wire, f"wire[{wire}]")
            for wire in gate[1:]
        ),
    }


def source_gate_trace(initial: int, source_word: Word) -> tuple[dict[str, object], ...]:
    rows = []
    state = initial
    for ordinal, gate in enumerate(source_word, start=1):
        before = state
        state = apply_gate(state, gate)
        changed = tuple(
            wire
            for wire in gate[1:]
            if ((before >> wire) & 1) != ((state >> wire) & 1)
        )
        rows.append(
            {
                "ordinal": ordinal,
                "rule": gate_record(gate),
                "before": named_source_signature(before),
                "after": named_source_signature(state),
                "changed_wires": changed,
                "provenance": RULE_PROVENANCE["source_emission"],
            }
        )
    return tuple(rows)


def rule_derivation(fixture: dict[str, object]) -> dict[str, object]:
    initial = fixture["initial"]
    words: tuple[Word, ...] = fixture["words"]
    program = fixture["program"]
    target = apply_word(
        apply_word(initial, fixture["allocator"]),
        fixture["allocator"],
    )
    expected_source_word: Word = (
        (1, SOURCE_POINTER, BANK0_POINTER),
        (2, SOURCE_POINTER, RIGHT_ENDPOINT, BANK0_U_TO_V),
        (2, SOURCE_POINTER, LEFT_ENDPOINT, BANK0_V_TO_U),
        (1, BANK0_U_TO_V, BANK0_DIRECTION_OK),
        (1, BANK0_V_TO_U, BANK0_DIRECTION_OK),
    )
    expected_finalizer_word: Word = (
        (0, BANK0_DIRECTION_OK),
        (2, BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK),
        (2, FINALIZER_WORK, RIGHT_ENDPOINT, BANK0_U_TO_V),
        (2, BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK),
        (2, BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK),
        (2, FINALIZER_WORK, LEFT_ENDPOINT, BANK0_V_TO_U),
        (2, BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK),
        (2, BANK0_DIRECTION_OK, SOURCE_POINTER, BANK0_POINTER),
        (2, BANK0_DIRECTION_OK, LEFT_ENDPOINT, SOURCE_POINTER),
        (2, BANK0_DIRECTION_OK, RIGHT_ENDPOINT, SOURCE_POINTER),
        (0, BANK0_DIRECTION_OK),
    )
    body_guard_rows = tuple(
        {
            "station": station,
            "kind": program[station][0],
            "gate_count": len(words[station]),
            "genesis_changed_bits": (
                apply_word(initial, words[station]) ^ initial
            ).bit_count(),
            "guarded_off_on_genesis":
                apply_word(initial, words[station]) == initial,
            "provenance": (
                RULE_PROVENANCE["program_rows"]
                if program[station][0] == "cross"
                else RULE_PROVENANCE["body_mapping"]
            ),
        }
        for station in range(1, RING_STATIONS - 1)
    )
    source_after = apply_word(initial, words[0])
    premature_finalizer_after = apply_word(initial, words[-1])
    return {
        "named_conflict": NAMED_CONFLICT,
        "blocking_rule": CONFLICT_RULE,
        "scope": (
            "exact held two-bank, two-adjacent-token, 11-boundary rule "
            "system; no statistical or fitted premise"
        ),
        "program_rows": tuple(
            {
                "station": station,
                "kind": row[0],
                "charge_row": row[1],
                "gate_count": len(row[2]),
            }
            for station, row in enumerate(program)
        ),
        "source_protocol_wires": dict(
            zip(SOURCE_PROTOCOL_NAMES, SOURCE_PROTOCOL_WIRES)
        ),
        "clean_source_return_postcondition": {
            "ordered_names": SOURCE_PROTOCOL_NAMES,
            "required_signature": CLEAN_SOURCE_RETURN,
            "target_signature":
                bit_signature(target, SOURCE_PROTOCOL_WIRES),
            "meaning": (
                "source pointer returned; POINTER/U_TO_V/V_TO_U emission "
                "registers absorbed; direction witness returned clean"
            ),
            "provenance": CONFLICT_RULE,
        },
        "source_word_exact": words[0] == expected_source_word,
        "source_word": tuple(gate_record(gate) for gate in words[0]),
        "source_emission_equations": (
            "pointer ^= source_pointer",
            "u_to_v ^= source_pointer & right_endpoint",
            "v_to_u ^= source_pointer & left_endpoint",
            "direction_ok ^= u_to_v",
            "direction_ok ^= v_to_u",
        ),
        "source_gate_trace_from_genesis":
            source_gate_trace(initial, words[0]),
        "initial_signature": named_source_signature(initial),
        "source_after_signature": named_source_signature(source_after),
        "source_emits_required_bootstrap": (
            bit_signature(source_after, SOURCE_PROTOCOL_WIRES)
            == (1, 1, 1, 0, 1)
        ),
        "non_source_body_genesis_guards": body_guard_rows,
        "all_nine_body_rows_guarded_off_on_genesis": all(
            row["guarded_off_on_genesis"] for row in body_guard_rows
        ),
        "premature_finalizer_signature":
            named_source_signature(premature_finalizer_after),
        "finalizer_word_exact":
            words[-1] == expected_finalizer_word,
        "finalizer_word":
            tuple(gate_record(gate) for gate in words[-1]),
        "rule_chain": (
            {
                "step": 1,
                "requires": (
                    "two adjacent A tokens select rows left=start and "
                    "right=start+1 at boundary 0"
                ),
                "update": "Q applies the two selected row macros in one of two orders",
                "provenance": (
                    RULE_PROVENANCE["initial_two_A_tokens"],
                    RULE_PROVENANCE["boundary_Q_pair"],
                ),
            },
            {
                "step": 2,
                "requires": (
                    "a body row may act only after source_compute_word has "
                    "created POINTER/U_TO_V and direction_ok"
                ),
                "update": (
                    "all nine non-source, non-finalizer rows are exact "
                    "identity on held genesis"
                ),
                "provenance": (
                    RULE_PROVENANCE["source_emission"],
                    RULE_PROVENANCE["body_mapping"],
                ),
            },
            {
                "step": 3,
                "requires": (
                    "after Q, lift_block and land_block advance both tokens "
                    "one row, producing every cyclic adjacent boundary"
                ),
                "update": "repeat the exact pair update for 11 boundaries",
                "provenance": RULE_PROVENANCE["token_successor_transport"],
            },
            {
                "step": 4,
                "requires": (
                    "the allocator target has clean source-return signature "
                    "(1,0,0,0,0)"
                ),
                "update": (
                    "source_finalizer_word is the only return/absorption row; "
                    "its exact guarded gates must run in the correct phase"
                ),
                "provenance": (
                    RULE_PROVENANCE["allocator_target"],
                    RULE_PROVENANCE["clean_source_return"],
                ),
            },
            {
                "step": 5,
                "requires": (
                    "after either boundary-0 order, the state must belong to "
                    "the exact backward preimage of the clean target under "
                    "boundaries 1..10"
                ),
                "update": (
                    "non-membership is the first dead end at depth 1; forward "
                    "propagation realizes UNCLEARED_SOURCE_EMISSION_AT_"
                    "CLEAN_RETURN by boundary 10"
                ),
                "provenance": (
                    RULE_PROVENANCE["boolean_gate_update"],
                    RULE_PROVENANCE["clean_source_return"],
                ),
            },
        ),
        "two_boundary0_order_requirements": (
            {
                "decision": 0,
                "order": "left_then_right",
                "exact_requirement":
                    "M_right(M_left(genesis)) in Pre[boundaries 1..10](target)",
            },
            {
                "decision": 1,
                "order": "right_then_left",
                "exact_requirement":
                    "M_left(M_right(genesis)) in Pre[boundaries 1..10](target)",
            },
        ),
        "rule_provenance": RULE_PROVENANCE,
    }


def core_experiment() -> dict[str, object]:
    fixture = normalized_fixture()
    width = fixture["width"]
    initial = fixture["initial"]
    words: tuple[Word, ...] = fixture["words"]
    inverse_words = tuple(tuple(reversed(word)) for word in words)
    program = fixture["program"]
    target = apply_word(
        apply_word(initial, fixture["allocator"]),
        fixture["allocator"],
    )

    @lru_cache(maxsize=None)
    def macro(station: int, state: int) -> int:
        return apply_word(state, words[station])

    @lru_cache(maxsize=None)
    def inverse_macro(station: int, state: int) -> int:
        return apply_word(state, inverse_words[station])

    def transition(state: int, first: int, second: int) -> int:
        return macro(second, macro(first, state))

    def predecessor(state: int, first: int, second: int) -> int:
        return inverse_macro(first, inverse_macro(second, state))

    def conditional_count(
        start: int,
        fixed: dict[int, int],
    ) -> int:
        frontier = {initial: 1}
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            decisions = (fixed[step],) if step in fixed else (0, 1)
            next_frontier: dict[int, int] = defaultdict(int)
            for state, count in frontier.items():
                for decision in decisions:
                    first, second = (
                        (left, right)
                        if decision == 0
                        else (right, left)
                    )
                    next_frontier[
                        transition(state, first, second)
                    ] += count
            frontier = dict(next_frontier)
        return frontier.get(target, 0)

    rows = []
    for start in range(RING_STATIONS):
        required: list[set[int]] = [
            set() for _ in range(RING_STATIONS + 1)
        ]
        required[-1] = {target}
        for step in reversed(range(RING_STATIONS)):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            required[step] = {
                source
                for destination in required[step + 1]
                for source in (
                    predecessor(destination, left, right),
                    predecessor(destination, right, left),
                )
            }

        order_rows = []
        for decision in (0, 1):
            left = start
            right = (start + 1) % RING_STATIONS
            first, second = (
                (left, right)
                if decision == 0
                else (right, left)
            )
            after_boundary0 = transition(initial, first, second)
            states = {after_boundary0}
            chain = [
                {
                    "boundary": 0,
                    "stations": (left, right),
                    "row_kinds": (
                        program[left][0],
                        program[right][0],
                    ),
                    "applied_order": (first, second),
                    "applied_kinds": (
                        program[first][0],
                        program[second][0],
                    ),
                    "reachable_states": 1,
                    "source_signatures": (
                        bit_signature(
                            after_boundary0,
                            SOURCE_PROTOCOL_WIRES,
                        ),
                    ),
                    "state_set_sha256":
                        state_set_digest(states, width),
                    "rule": RULE_PROVENANCE["boundary_Q_pair"],
                }
            ]
            for step in range(1, RING_STATIONS):
                step_left = (start + step) % RING_STATIONS
                step_right = (step_left + 1) % RING_STATIONS
                states = {
                    destination
                    for state in states
                    for destination in (
                        transition(state, step_left, step_right),
                        transition(state, step_right, step_left),
                    )
                }
                chain.append(
                    {
                        "boundary": step,
                        "stations": (step_left, step_right),
                        "row_kinds": (
                            program[step_left][0],
                            program[step_right][0],
                        ),
                        "future_orders_propagated": (
                            (step_left, step_right),
                            (step_right, step_left),
                        ),
                        "reachable_states": len(states),
                        "source_signatures": tuple(
                            sorted(
                                {
                                    bit_signature(
                                        state,
                                        SOURCE_PROTOCOL_WIRES,
                                    )
                                    for state in states
                                }
                            )
                        ),
                        "state_set_sha256":
                            state_set_digest(states, width),
                        "rule": (
                            RULE_PROVENANCE["boundary_Q_pair"],
                            RULE_PROVENANCE[
                                "token_successor_transport"
                            ],
                        ),
                    }
                )
            terminal_signatures = {
                bit_signature(state, SOURCE_PROTOCOL_WIRES)
                for state in states
            }
            terminal_all_conflict = all(
                signature != CLEAN_SOURCE_RETURN
                for signature in terminal_signatures
            )
            row = {
                "decision": decision,
                "order": (
                    "left_then_right"
                    if decision == 0
                    else "right_then_left"
                ),
                "after_boundary0_signature":
                    bit_signature(
                        after_boundary0,
                        SOURCE_PROTOCOL_WIRES,
                    ),
                "required_after_boundary0_state_count":
                    len(required[1]),
                "required_after_boundary0_signatures": tuple(
                    sorted(
                        {
                            bit_signature(
                                state,
                                SOURCE_PROTOCOL_WIRES,
                            )
                            for state in required[1]
                        }
                    )
                ),
                "after_boundary0_is_backward_viable":
                    after_boundary0 in required[1],
                "completion_count":
                    conditional_count(start, {0: decision}),
                "first_dead_end": (
                    None
                    if after_boundary0 in required[1]
                    else {
                        "boundary": 0,
                        "depth_after_boundary": 1,
                        "rule":
                            "exact_backward_preimage_of_allocator_target",
                    }
                ),
                "terminal_boundary": RING_STATIONS - 1,
                "terminal_signatures":
                    tuple(sorted(terminal_signatures)),
                "terminal_all_violate_clean_source_return":
                    terminal_all_conflict,
                "named_conflict": (
                    NAMED_CONFLICT
                    if terminal_all_conflict
                    else None
                ),
                "conflict_rule": (
                    CONFLICT_RULE
                    if terminal_all_conflict
                    else None
                ),
                "step_by_step_trace": tuple(chain),
            }
            order_rows.append(row)

        success_count = sum(
            row["completion_count"] for row in order_rows
        )
        rows.append(
            {
                "start": start,
                "left_station": start,
                "left_kind": program[start][0],
                "right_station": (start + 1) % RING_STATIONS,
                "right_kind":
                    program[(start + 1) % RING_STATIONS][0],
                "left_is_non_source": program[start][0] != "source",
                "successful_assignment_count": success_count,
                "orders": tuple(order_rows),
                "both_boundary0_orders_dead": all(
                    row["completion_count"] == 0
                    and not row[
                        "after_boundary0_is_backward_viable"
                    ]
                    for row in order_rows
                ),
                "both_orders_reach_same_named_conflict": all(
                    row["terminal_all_violate_clean_source_return"]
                    and row["named_conflict"] == NAMED_CONFLICT
                    and row["conflict_rule"] == CONFLICT_RULE
                    and row["terminal_boundary"]
                        == RING_STATIONS - 1
                    for row in order_rows
                ),
            }
        )

    dead_rows = tuple(row for row in rows if row["left_is_non_source"])
    source_row = rows[0]
    downstream_decision_counts = tuple(
        {
            "boundary": step,
            "decision_0_completions":
                conditional_count(0, {step: 0}),
            "decision_1_completions":
                conditional_count(0, {step: 1}),
        }
        for step in range(RING_STATIONS)
    )
    theorem = {
        "formal_implication": (
            "For every start s in Z/11Z in this exact rule system: "
            "program[s].kind != 'source' => for each d in {0,1}, "
            "T_s,d(genesis) not in Pre_s,1(target), and every continuation "
            "violates CLEAN_SOURCE_RETURN by boundary 10."
        ),
        "quantified_starts": tuple(row["start"] for row in dead_rows),
        "antecedent_rows": tuple(
            (row["start"], row["left_kind"]) for row in dead_rows
        ),
        "all_ten_antecedents_true": (
            len(dead_rows) == 10
            and all(row["left_is_non_source"] for row in dead_rows)
        ),
        "all_twenty_boundary0_orders_dead": all(
            row["both_boundary0_orders_dead"] for row in dead_rows
        ),
        "all_twenty_traces_match_conflict_step_and_rule": all(
            row["both_orders_reach_same_named_conflict"]
            for row in dead_rows
        ),
        "bounded_boundary_count": RING_STATIONS,
        "first_dead_boundary": 0,
        "conflict_realized_by_boundary": RING_STATIONS - 1,
        "named_conflict": NAMED_CONFLICT,
        "conflict_rule": CONFLICT_RULE,
        "target_clean_source_signature": CLEAN_SOURCE_RETURN,
    }
    sufficiency = {
        "ruling": "SOURCE_ROW_IS_NECESSARY_NOT_SUFFICIENT",
        "necessary_on_complete_battery": (
            all(
                row["successful_assignment_count"] == 0
                for row in dead_rows
            )
            and source_row["successful_assignment_count"] > 0
        ),
        "not_sufficient_for_boundary0_order": (
            source_row["orders"][0]["completion_count"] == 0
            and source_row["orders"][1]["completion_count"] == 512
        ),
        "source_start": 0,
        "source_start_total_successes":
            source_row["successful_assignment_count"],
        "boundary0_order_completion_counts": tuple(
            {
                "decision": row["decision"],
                "order": row["order"],
                "completion_count": row["completion_count"],
                "after_boundary0_is_backward_viable":
                    row["after_boundary0_is_backward_viable"],
            }
            for row in source_row["orders"]
        ),
        "downstream_boundary_decision_counts":
            downstream_decision_counts,
        "additional_requirements": (
            "boundary 0 must put bank before source (decision 1), so the "
            "guarded bank no-ops before source emission",
            "boundary 10 must put source before finalizer (decision 1), "
            "so the last emission is absorbed by source_finalizer_word",
        ),
        "flexible_downstream_boundaries": tuple(
            row["boundary"]
            for row in downstream_decision_counts
            if row["decision_0_completions"]
                == row["decision_1_completions"]
                == 256
        ),
        "counterfactual_passes_at_exact_block_point": (
            not source_row["orders"][0][
                "after_boundary0_is_backward_viable"
            ]
            and source_row["orders"][1][
                "after_boundary0_is_backward_viable"
            ]
        ),
        "honest_scope": (
            "source kind removes the ten-start bootstrap obstruction, but "
            "does not by itself supply either required source/body/return "
            "ordering; therefore it is not a sufficiency theorem"
        ),
    }
    return {
        "certificate_A": rule_derivation(fixture),
        "certificate_B": {
            "theorem": theorem,
            "success_counts_by_start": tuple(
                row["successful_assignment_count"] for row in rows
            ),
            "per_start_verification": tuple(
                {
                    key: row[key]
                    for key in (
                        "start",
                        "left_kind",
                        "right_kind",
                        "left_is_non_source",
                        "successful_assignment_count",
                        "both_boundary0_orders_dead",
                        "both_orders_reach_same_named_conflict",
                        "orders",
                    )
                }
                for row in rows
            ),
        },
        "certificate_C": sufficiency,
        "fixture_certificate": {
            "width": width,
            "program_kinds": tuple(row[0] for row in program),
            "program_gate_counts":
                tuple(len(word) for word in words),
            "initial_sha256": bit_digest(initial, width),
            "target_sha256": bit_digest(target, width),
            "expected_target_sha256": EXPECTED_TARGET_SHA256,
            "target_sha256_matches":
                bit_digest(target, width) == EXPECTED_TARGET_SHA256,
            "assignments_per_start": ASSIGNMENTS_PER_START,
            "total_complete_assignments":
                RING_STATIONS * ASSIGNMENTS_PER_START,
            "exact_arithmetic": (
                "Python integers under explicit Boolean X/CNOT/TOF updates"
            ),
        },
    }


def source_controls() -> dict[str, object]:
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=__file__,
    )
    own_paths = ast.literal_eval(
        assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )
    observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    lineage_observed = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in FROZEN_LINEAGE_PATHS
    }
    required = {
        AUDIT_INPUT_PATHS[0]: {
            "initial_full_state",
            "q_block",
            "lift_block",
            "land_block",
            "fixed_q_order_tick_blocks",
            "route3_adjacent_full_battery",
        },
        AUDIT_INPUT_PATHS[1]: {
            "fixture",
            "functional_battery",
            "functional_mapping",
        },
        AUDIT_INPUT_PATHS[2]: {
            "apply_word_int",
            "build_fixture",
            "enumerate_success_assignments",
        },
        AUDIT_INPUT_PATHS[3]: {
            "apply_word_int",
            "build_fixture",
            "enumerate_and_prune",
            "failure_anatomy",
        },
    }
    anchors = {}
    for path in AUDIT_INPUT_PATHS:
        tree = ast.parse(
            (ROOT / path).read_text(encoding="utf-8"),
            filename=path,
        )
        anchors[path] = tuple(
            sorted(required[path] & function_names(tree))
        )
    branch = command_output(("git", "branch", "--show-current"))
    head = command_output(("git", "rev-parse", "HEAD"))
    required_parent = "9ad09e2faeeb6aebde889c950da0b10e0cb2f172"
    parent_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", required_parent, "HEAD"),
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    ).returncode == 0
    return {
        "audit_input_paths_literal": own_paths,
        "all_paths_worktree_relative": all(
            not Path(path).is_absolute() for path in own_paths
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in own_paths
        ),
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": observed == EXPECTED_SHA256,
        "text_ast_function_anchors": anchors,
        "all_function_anchors_present": all(
            set(anchors[path]) == required[path]
            for path in AUDIT_INPUT_PATHS
        ),
        "import_blocklist": BLOCKED_MODULES,
        "blocklist_active": _IMPORT_BLOCKER in sys.meta_path,
        "blocked_modules_loaded": tuple(
            module
            for module in BLOCKED_MODULES
            if module in sys.modules
        ),
        "frozen_lineage_paths": FROZEN_LINEAGE_PATHS,
        "frozen_lineage_observed_sha256": lineage_observed,
        "frozen_lineage_expected_sha256": EXPECTED_LINEAGE_SHA256,
        "frozen_lineage_sha256_match":
            lineage_observed == EXPECTED_LINEAGE_SHA256,
        "frozen_fixture_raw_sha256": EXPECTED_FIXTURE_RAW_SHA256,
        "git_branch": branch,
        "git_head": head,
        "required_parent_f12_sha": required_parent,
        "required_parent_is_ancestor": parent_is_ancestor,
        "third_party_packages": (),
        "runtime_imports": "stdlib only",
    }


def deterministic_digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def render_report(report: dict[str, object]) -> str:
    lines = (
        f"CERTIFICATE_A_BOUNDARY0_RULE_TRACE="
        f"{compact(report['certificate_A'])}",
        f"CERTIFICATE_B_MECHANISM_THEOREM="
        f"{compact(report['certificate_B'])}",
        f"CERTIFICATE_C_NECESSITY_SUFFICIENCY="
        f"{compact(report['certificate_C'])}",
        f"CERTIFICATE_D_CONTROLS="
        f"{compact(report['certificate_D'])}",
        *(
            f"{'PASS' if passed else 'FAIL'} {label}"
            for label, passed in report["checks"].items()
        ),
        f"CYCLE811_PASS={compact(report['pass'])}",
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = perf_counter()
    first = core_experiment()
    second = core_experiment()
    deterministic = first == second
    runtime = perf_counter() - started
    controls = source_controls()
    controls.update(
        {
            "deterministic_repeated_core_equal": deterministic,
            "deterministic_projection_sha256":
                deterministic_digest(first),
            "runtime_seconds": runtime,
            "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_bytes": 0,
        }
    )
    theorem = first["certificate_B"]["theorem"]
    sufficiency = first["certificate_C"]
    derivation = first["certificate_A"]
    fixture = first["fixture_certificate"]
    checks = {
        "A_exact_rule_chain_and_named_conflict": (
            derivation["source_word_exact"]
            and derivation["finalizer_word_exact"]
            and derivation["source_emits_required_bootstrap"]
            and derivation[
                "all_nine_body_rows_guarded_off_on_genesis"
            ]
            and derivation[
                "clean_source_return_postcondition"
            ]["target_signature"] == CLEAN_SOURCE_RETURN
            and derivation["named_conflict"] == NAMED_CONFLICT
            and derivation["blocking_rule"] == CONFLICT_RULE
        ),
        "B_exact_implication_all_ten_starts_both_orders": (
            theorem["all_ten_antecedents_true"]
            and theorem["all_twenty_boundary0_orders_dead"]
            and theorem[
                "all_twenty_traces_match_conflict_step_and_rule"
            ]
            and first["certificate_B"][
                "success_counts_by_start"
            ] == EXPECTED_SUCCESS_COUNTS
            and fixture["target_sha256_matches"]
        ),
        "C_source_necessary_not_sufficient": (
            sufficiency["ruling"]
                == "SOURCE_ROW_IS_NECESSARY_NOT_SUFFICIENT"
            and sufficiency["necessary_on_complete_battery"]
            and sufficiency[
                "not_sufficient_for_boundary0_order"
            ]
            and sufficiency[
                "counterfactual_passes_at_exact_block_point"
            ]
            and sufficiency["source_start_total_successes"] == 512
        ),
        "D_shas_blocklist_determinism_and_bounds": False,
    }
    report = {
        "certificate_A": derivation,
        "certificate_B": first["certificate_B"],
        "certificate_C": sufficiency,
        "certificate_D": controls,
        "checks": checks,
        "pass": False,
    }
    for _iteration in range(10):
        controls_pass = (
            controls["audit_input_paths_literal"]
                == AUDIT_INPUT_PATHS
            and controls["all_paths_worktree_relative"]
            and controls["all_paths_exist"]
            and controls["sha256_match"]
            and controls["all_function_anchors_present"]
            and controls["blocklist_active"]
            and not controls["blocked_modules_loaded"]
            and controls["frozen_lineage_sha256_match"]
            and controls["git_branch"]
                == "physics-loop/proof-grade-blockF13-20260729"
            and controls["required_parent_is_ancestor"]
            and controls["deterministic_repeated_core_equal"]
            and controls["runtime_seconds"]
                < controls["runtime_limit_seconds"]
            and controls["stdout_bytes"]
                < controls["stdout_limit_bytes"]
        )
        checks["D_shas_blocklist_determinism_and_bounds"] = (
            controls_pass
        )
        report["pass"] = all(checks.values())
        rendered = render_report(report)
        measured = len(rendered.encode("utf-8"))
        if measured == controls["stdout_bytes"]:
            break
        controls["stdout_bytes"] = measured
    rendered = render_report(report)
    if len(rendered.encode("utf-8")) != controls["stdout_bytes"]:
        raise AssertionError("stdout byte fixed point failed")
    sys.stdout.write(rendered)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
