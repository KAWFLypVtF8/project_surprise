#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,time as J,numpy as B

H=True
G=input
A=print
V=range
F=chr
a=len
X=None
Q=''
B.t=B.random


# Function to clear the console
def D():os.system('cls'if os.name=='nt'else'clear')
    
def E(d):
	C=a(d);A=Q
	for D in d:A+=F((ord(D)-B.t.randint(C)%256)%256)
	return A
def O(r):
	C=a(r);A=Q
	for D in r:A+=F((ord(D)+B.t.randint(C)%256)%256)
	return A

# Function to ask a question and get the user's response
def K(e, t,f):
    while H:
        B.t.seed(f)
        r = G(E(e))
        B.t.seed(f)
        if O(r) == t:
            return H
        elif r == F(27):
            return 'ESC'
        else:
            A("Mauvaise réponse. Essaye encore")
            J.sleep(0.7)
            D()

# Function to display the menu and get the user's choice
def DM(p,s):
    D()
    B.t.seed(s)
    A(E('\x82%\x91\x9c´/°üY\x00\x95Ø\x92%ÄÖÑ¨tï,\x97ì\x10\x80Ð~ ðµÌæç¦\x93ç\x82\x1a\x85\x1e¹hd\x91.\x86\x9b²+b\x7fRÏ¤d\x04}èÎþsËßÌ±\x9f\x99Câ\x1bá\x17!:\x89\x97\x1aÁÀu)ã\x8dvkÇ\x00íè\x88²\x12\x95âÚçÚ\x1aQ\x84$/\x93\x08û*zÃ\x8a\x9d£ÂðæÎÏþÅ×\x97]c\x11oÊghÿÞ\x87\x1cùcO¯*ÝQÌ3\x9eÕýíj¿\x9e\x98ë®¯µ\x0cÄ¢\x96\x1eÍ°É\x9d¨´ä}Þ`Ï\x91\x8e\x92Ôn\x00ÁutÁ¾®\x15U\x9a*\x9aP·Y·ÃÖ\x93'))
    if p["choice1"]:
        B.t.seed(s)
        A(E(';2/jcLWZKPÙa*Sumu'))
    else:
        B.t.seed(s)
        A(E('70$Pnfz'))
    if p["choice2"]:
        B.t.seed(s)
        A(E('<2/jcLWZKPÙa*Km|e'))
    else:
        B.t.seed(s)
        A(E('80$Hfuj'))
    if p["choice3"]:
        B.t.seed(s)
        A(E('I8$jcTnTNgÖ_8O\x7f}ou,lv;t\x90e\x86\x82|z~\x92'))
    else:
        B.t.seed(s)
        A(E('=2/\\~\x80j{"fu$~ymv\x84ps\x81\x80'))
    A("\nAppuie à tout moment sur \"ÉCHAP+ENTRÉE\" pour revenir au menu")
    v = G("\nTon choix: ")
    return v

def DsM(p,x):
    D()
    B.t.seed(x)
    A(E('\x8f%?\x96OÃ\x81«ü;\x9e\x11\r\x8e\x1dB\x1c\rÏ\\\x98¨zìÞ\x9aÙÏ\x80Ð,Da÷³\x1bàäP\x955õ\x89\x1cÊ$t¸l\x97.Xx§¿,bt×Ç$d\x01G<ç]Ð\x035¼\x19Ðw÷\xadS`F`\x0cã\x172a\x9eÎ"\x7fF<\x9e\x19¼Àtj#Ùw¢Ò\x00å\x00Ö\x0f\x8b·ÀëêÐòHÓ\x0b]@0\x84\x8c¹Eë&1+WÉ\x86àSÄQ\'ÖÎÔ\x0e¼àØñ¬B^½-iÊ¨.jÌ\x84,\x0cù@\x01\x9c´\x1ar\x1e\x9a Jg@[=ø@æéúë²±bO,\x91£½Q«®\x10¶çBè·Uy*\x9d¬f®)®×8Ï¥\x82£K\x9a\x97\x8dv÷UÕ3 3Èå÷+²Jæóì\x19·\x19·\x0fDÖÖ»\x80\x85¡\x04´v'))
    if p["choice1"]:
        B.t.seed(x)
        A(E(";R/j[JqokrÑn pm,\x8ei~{\x86#jy4t'c\x85pjt\x97f\x7f\x88\x81"))
    else:
        B.t.seed(x)
        A(E('G8$[p/wn\x8c\x81g8fu$v.Mzthm\x8cto\x7fq'))
    if p["choice2"]:
        B.t.seed(x)
        A(E('<R/j[Jqokró\x84(]aD|\x94\x7f\x92e+k\x86v&a\x95\x93\x88ig\x90x\x80"M\x95\x84o\x7f|\x81\x9b'))
    else:
        B.t.seed(x)
        A(E('<=/Sf?xzs\x80q>dpzAPu\x82\x88ig\x81ru+C\x88u\x8az}l\x8a'))
    
    A("\nAppuie à tout moment sur \"ÉCHAP+ENTRÉE\" pour revenir au menu")
    v = G("\nTon choix: ")
    if v == F(27):
        return 'ESC'
    return v

# Function to execute a series of questions
def Gr(f,e):
    for i, t, y, u in f:
        if u:
            continue
        D()
        o = K(t, y,e)
        if o == "ESC":  # Check if the answer is the "ESC" key
            return o, f
        f[i][3]=H
    return X, f

# Main function of the script
def main():
    
    Trigger_before_menu =H
    Trigger_Initiation =H
    
    TH = {
        "choice1": False,
        "choice2": False,
        "choice3": False
    }
    
    THX = {
        "choice1": False,
        "choice2": False}


    Z1 = [
        [0,"\x83\x85£´IF\x15¨\x14_B\x1c\x0b[Ñ\x83hé,\x89~\x8bxa««Øæ\x95A'_4Ù!Âhc\x83w\x97®.n+×0!\x125\x8f\x96Ëz½Æ§\\FT\x84×\x8c\x8bø\x9f\x1d³Ðxn#vÉ±ìAÞ{·é×¦Ü\x15¦\x92/\x84\x05w¿\x8aSÄyÐÈèÜïcGlYômF´j¾æ\x87÷ûJ\x97©\x0em\x96X3X==¤òq\xad\x98ç\x87¶¹´\x10Æk\x8e\x96kÆWM¬+º8Ü¡Ô¤K\x9a\x98\x807À\x15\x80\x11J.+¿N*¢\x9a\x16R+¾\x81LOO\x1f\x06|Í?qú\x8bÓY\x05´Mê\x02ý'y²aKþº\x14T³\x8eH\x1c\x0bð'\x81\x9bw¸\x8c¶\x87\x83¦s\x84Ï1g¤ºB¢Áã\nø¸xw\x898>\x87\x0e\x8cÉ¬\x02\x81\x8dxtÖØq\x81@\x19@\n¸/û\x85Í~4eèÓ®¿b\tX\x890fÑ\x1cÁÑ\x94\x07Kh\x82ÎÐ\x95\x8aÂ#\x84\x1eg=C)mu?74[h±\x95jEãá,î\x8e±òÉ6ê\x05Yxc0¥¥l^X\x92©ü\x88ØÙ\x05\x10\x01\x87\x15;\x85z¬hÉr3\\pJØe¿8¤&\x91\x8f\x96Ð",'R;w@qj}4>;hov~', False],
        [1,'\x94\x92O¿t°ð9Y\x08[\x86!\x85Ï\x07Ü÷\x86m\xa0*\x85\x98~Ú\x81tðg¶|\x84\x96ã]îy×\x15¼\xadsB\x88\xa0²Ù¦lÝÈç!\x0bÍ<ÚÖ\x83ª\x8bÇö³^S]\x91\x8eÔ\x83\x8bFO\x1fÀÊw\x7fhß2÷Òö\x98DÓ\x8a®À£¯\x92¦vôX\x88ø\x96\x02úpÍ8í\x94Ã\'R\x89Ç\tÈÛãé¨E\x1d`þ9tË¼yÊ\x9a\x8eéûU\x8e²\x15}QJ\x86[èMìé¨ê³±\x9dç\x86ø¿¯¦\x1cÄc\x95\x8f"¾ºZ¢¡æ¦ç\x90\x8c¯Ô\x95E\x91\x90Å|²KÅ\'c.ù\x06+¼^ã*í\x91\r\x9e\x05\x17ÿ\x9fÖ»\x91\x94\x94MÖ\x8cX\x94Îû\x8cjb«\x86Á«¹»?=9û\xad\x81¿f\x03«\x06\x15Þi\x0f\x96ªÔá9\x8dWÖ\x82e\x88¬\x87:\x98ô\x89Æxg°»\x8bN¾(\x1dò¯x\x84\x853\x92C\x8aè\x85Xþþ¶\x81\x8exjÏÇîzzí\\A\x8eÂÎêý\x80\x8c\x82«tç"Úü"½äù\x89\x14,Ó0ºÊÓÙ³Fä»=Ì%\x98>ÇüÒà~\x9eu1\x97\'{\x00{?\x89ëmÛd±\x8dðy\x8a\x96â*·\x8dµE¾õ\x9fÿcÁbêV\x9aeêªBÏ®§~\x1dí\x14\x12\x949LÞÓoÞígÀr7ik\x14WMª\x9d~+ûo*\x9bYÆèöá\x96áà\x81¾','8=37=839115', False]
    ]

    Z2 = [
        [0, '\x8c\x93¨´}\\ë\x9e¿\x96\x94\x11\x12ÝÜ÷\x83ôD\x82¹]àu þ¬\x1eØ\x92\x94\x90ôwÆÑ\x13t¸e\x94\x86¡»°p\x89Æp\n\x80ëÐ\x88¨\x19ßw\x05\xad\x94CÑ\nä \x1d\x8d\x99\x94ËºÀ"srâ\x84¢®±·\x92W¼Íéö\x84úÞ\x15¦\x96øCØ\x903¿\x8c\x9d¡¿u\x92ÌÆºÁ\x99Üð·½p½º%\x12é\x8b±\x96/\x12o]Ì|ê¤üíj¹\x90\x91ôÂ«a\x0c¿Ø\x91\x1b\x12k½\x92\\µ×\x8aÙ©ÕP\x8d\rÈò»j\x11P\x13müz¸\x9aXé\x9d·s·', 'Rrkyst/Ohqmt\x7fczk' , False],
        [1, '\x81(+\x9a\x9eo=jµÏCÍPæB\x1d\x05Óß¨tï+\x91ÝÏvÐ,Nrt\xad\x94é×P\x0b7øyÆØ\xadÆhq\x97 3¦ÂÙ£~\x89Ó\x1ct¼:}ßÛ÷y¼ËÝ¼\x05°\x95PÓ\x170Û\x1c\x13\x7f\x98A\x9d\x12nËq~u\x8d\x86ôÓ\x06îEäBi\nÚ¡ÚçÕ\x19Q\x94$/\x93\x08Eë&ð\x80È}\x9d\x94Å{äÎ\x81\x0bÈ×êñ¬B\x0bç:|Q\x13z\x03æB ÷O\x01\x95ªÅn"¦$|°EB\x9e÷ø÷¼ÀO-\x84ù¼Q¯a\x0b¶\x95\x8e\nÍ»¶\x9f¯44³×8ÝµËPR\x86DÔn²Ãvn-\x16í\x00pkZ*Ü\x9f\x05Y\x07\x12Q*\x93\x8b&*\x82K\x19Þ3;\x94³', 'S\x7fwjzuc|kor', False],
        [2, 'iu¢*\x9c\x13V.\x87TÑ\x7fo\xa0ß.\x16ºz ðå\x92$j\x84×\x17ÂdB\x87¼.~\x83\'f\x0fô\x86åÜ\x87Ê^R\x8bW\x91\x8eYF"\x10{ujysúë\x00âw¼\x95öÑ\x18\x93~\x91\x07pÆ\x84lÎ×åñq\x01+\x10ÑD¶s\x0cß¤HP\x0e*\x9eF|U<=òé\x9d;C¹§a\x0b²r\x12qM+8Ù©ÕA\x80n\x00\x07ji;nÀUk¤\x0cN$l\x80\x85OO\x19T;½\x80oý\x85Ó\x0c´\x08ê#ä§,Áh÷ì\rÐß»\x1d\x9d²Ô\x9c2ÂW~\x88u\x8b\x7fz\x81i¼_¼\x17+\x10ì¿v{@(\x83\x91\x83\túû<~j~\x87.bFu´ü\x84Ñ53u\x9c(û\x1aÖ`Þ+x/Çã\x01ö\x81ÀÐ\x8b\x1b}ªvv\x96á,xC\x85:f\x1f¿W3EØá&î¯AJéó[½\x0fß\x00\x7f|\x83®ì6àâ\x0cÜ\x85\x1døûíT¼{ã1\x1c','8;65B1:21;', False],
        [3, "\x96\x1e9\x99\x90{/°®*¬¿\x88'\x94$\t\x8a\x8d\x92\x1bÄ#\x96æ\x18ôÝqþéû¹\x11ìè\x95Mãóu\x0fØÒÂ·nB\x1fx¥m&±t×Ç-f\x0f\x02J¤qáh°ËßÌ±®\x87\x95Ñ\x18>ä!Î\x8f\x94ø\x9f\x10Ã{nnv\x8d\x86ùÉöìS\x92zpáÜâØîÑÒQ\x89+/\x9c¹7ôÔ1+Ï\x86\x9d¤Åp\x92ÍÆ\x10ÅÓàñc4\x11;iÎ¬4%\x12é\x90ÛåOU\x8e³\x19s,\x9fÚ3Ò,Oíùþíj¹\x9e0Cï²ÿ¶´\x0cÆÙ\x91É\x11°q\x99\x9då6ªä\x8bÛ®Ð\x95ü\x96\x99É)ó\x80wo<\x15m®n°\x9amé\x9e\x0b\x9e\x05\x18\rÀ}Á\x8f\x85¡I\x0bÙ$;\x94³",'rmzfeita:', False]
    ]
    
    Z3 = [
        [0, '\x93«j\x85¢os«u¨Y\x82\x8a§\x8b£\x8d(}a^\x94\x98\x7f\x80Ã o¬L\x9cH\x84xw\x8e\x9bÈ\xadc\x96\xa0A<W\x86£t®!\x8dÉ\x85wzº\x9fwu\xad\x94\x86I¬\x93¢:gÊ\x92\x93·Ïglww"P6S*Qx\x0f\x9f\x8f¬/q\x88¿@TY', 'Kyv\x84\x82{n{"R\x7fmxz\x7fwt', False],
        [1, '\x81\x8d\x94½/¦ö®\x0bB\x8b\x8cÝ\x7f\xa0\x97ÙoÝõ ò0åÛ\x95Aéy\x85»©r\x95@\x9e-bo\x90Äj\x08\x88ÛÜ\x87º\x8b\x85¿l0-·Þ:\x94V¯{rjv\x8d\x86ñÙûçç\x88¼\x95jØo\x8c¦\x8e/\x89\x02ë}z\x85ì¡ÄhÙ×Â\x0c·\x9e\x97í¨\x12x\x89»z¾ç\x87¤\x8d´x\x9fxð¤ûéj¼¡\x0cæ6ª¦¿é\x87k²\x91®ªå\x8bÑ`¡:/e¤[×³ZE¤ÞZ\x9eÎKÆu·s·','>=/Q^\\QRXCbH*Naa_EQT^', False],
        [2, '\x88#:\x96\x94Â\x82¥ö3§\x00[\x96ØPÞÒ\x8añvQ\x81må3\x9aÝÏ|×\x81s««\x15ÝØ\x99\x84,fë4\x13Æ\x1bÇhj\x87Û\x86§¶,b~dÕÛr\x119<êÜ5½\x0cÞw\n^K\x98`\x8cä\x0e;\xa0Î÷\x86F9O\x18¯Çjnxßw÷×öåEà\x8ai\x04p¡ÈoÙ\x8f\x9f\x81&t\x95¹ö#\x80Ì8ï\x98ºvÛ×Å\x0c¸\x92ÇÞµ<p\x1c½4aÅºân\n\x9a\x83Ûð@\x01\x9c´\x1a\x80"\x9f\x15W3X==\x9eð¯é±±\x9d*\x88£¶³®\x16³gá\x8b\x91\x1f°qÒ¡\x9d.:eæ\x8aT³\x82\x95B\x8b\x8dÃjõL\x8c\'e=Áíú+¬Rçoì\x91\x00\xad·\x0fD)\x93¾\x81\x83\x9eI\x1eÍ"Z\x80Ì³\x13\x8eöoåìyÈ\x9e:þÁú\x1889\x04³|²eÄ:óû\x1cÐ½Î\x08\\WÝæÎ¦ß\x82¦\x83µyàB\x9bv5Ñf¹\xa04\x96N½%(Çü\x06jm1\x86\x893\x83C=\x8aï\x96\tõ\x07\x0c\x81\x8dÌnÓ\x84ãi\x83@\x19\x14ù\x8aÂ,Ø,ñ~Õz4,\x95\x18à\xad&Í\x1b*cÎÅ¦ÜfÚ*ÁÐ\x8aé\x01öå\x15\xad\x8b\x87Ð\x94\x93Çè \x1e\x9c\x80ªg1\x86\x1a,þtC\x8bëm\x18\x8ds\x03\x9eò%\x88åá$ñüJ\x9c7ÎM¤\x06ixc0¥¥lÚªÅ\x8eÏZõ\x8b%a\x14\x1c\x94|\x88Ð9\x18×\x0eíUÇ·ã[a¿M\x8b¦ä»8ý¥ÝmJf\x88\x1bÞ\x9aÊòà', '6::7B:8309', False],
        [3,'\x85\r\x9b¸r¥û&\xad\x08\\\x90+B\x8b\x07v\x92[`\xa0"\x93á\x7f\x8b\x80\'ì½æç\x95\x93ãhouÓ\x1fÃ±n\x953£Â\x1ebnÎ×/f¼5\x83ÛÕx¬\x8b@\x05\x9fS\x9a\x0e\x99àÓ\x83\x93=\x9d\x1fn¾njtâûç\x84òí\x00å\x85µ¡¡Óô\x8c\x07Q\x8dx\x96¹ûyzyëS±}Ó×ÕsÖÜ\x9d¹8kT9e|³f¾ç\x83íNP\x97eÓ8_ï\x1d,6>çò´¨®±¡5\x8ck¿«a\x90ÁpÚ\x97#°qJ£\x9d4¹\x92\x89á¥\x82\x9aAE\x98Å)öVÎueéðµt¹MãmßPª\x18DÖçÁ<\x81£O\x0fÚJ\x8ez\x07\x80ïq¹6£\x9e¹²B3|±²\x85½X÷ïÁñÝ¬\x16\x91°Pß:ÆWZ\x82¦\x85»4\x8f\xa0o5Ôfª±/\x87N®5\x1cý¯*{\x8eå\x8b\x84\x99â\x95\x15¬û\x90:»j\x81Èg{5@h@AÅÕ?û2Öz7nÚÓNô\x1a\x86Ö?Î;}\x91/Í~×Ù³Jõ·\x92Ñ\x15¥>¿®\x1bàt£vz\x89\x1emùyú\x88@\x1fÖk±\x8a\x05f\x8eê\x92$=\x9c¿ò½:\x97\x05UxS#¨\x9e_]ª\x87\x8a\x9dö\x83(a\x16\x16è\x81\x92\x1eé¤¤\x96AÊ¿%ia\x01De²v-¨&\x94\x90Îã:\x99hØ','5443:', False ],
    ]
    
    Z4 = [
        [0,"p\x9då©\x08`,\x87\x07Ð`óÞq{Ù\x80aòå×6\x1a§\x1eµn\x85µ\x1e~\x91é/¦ÞÀÌ5Å£\n\x8aS\x99à\x87A\x1e{rjv±ì\x07Ó²ÙëÞÒC\x06lÃ\x8b'ÔÛ\x97ñ¸óf^:iºy\x03í²\t\x0f¯\x14\x80GZ-JúíO+\x92»©a\x1bÃæ qY8\x01Ï©ÕÅÍn\x00['l.~k6y\x9e\x17@\x1dº\x85¢ûìR»kî~Å\x0coK?~±²\x81mTJ«þ\x99Õ)Î\x8b®Zå9J\x9c\x81<xkÏxg³µ\x9cã\x0c÷»\x7f\x00\x94*E\x8c^ÿ\x07\x91Aå(\x85?âEº8ü@\x8cÌDä!û\x1aÖ\\Ø/%'\x85Ý\x01:\x86¾\x15>#ªgC)\x81%;@j`\x04Iy\x97åç.·l6:\x97\x06YË\x0f-Xè\x9d\x94°è\x8a!ç\x10 Ð6\x03úhÏ»(loF¸\x04`", '9PW]NHi', False],
        [1, '\x8e\x9evD£Á÷¯\'§¨\x8d\x8d\x8b¦\x86\x99\x87Ï\x87Ïmtä _.\x82s{ÙzÃ x¶\x95\x97Ö\x9f\x8f¦\x9aryFÓ¡Áhd\x97\x98®Ô\x85¨¶\x9c§+ÜØ\xad!eÂ\x90ÛÚÕ¼\x89g\x9càÀ1´Ë\x8d\x96Ý\x98ä\x98²à\x92\x93¦\x8a\x92Ç\x98\x9f³Í"lhá2kÒuáÃ×\x96 ScänÔgÎÚã\x8bQZ_', 'Dmxm{', False],
        [2, '\x85\x9f6\x8d\x92¸\x83\x9dû.¨\r\rCØ,ºç\x91Lßü1_ï,\x87\x98\x14rÑqcÿ°"Üß\x95\x8f7\x1aû\x82\x0b\x85\x13¸ºe\x95.xR¯"¶wâ\x8fÛr\x11=<ê\x8e8\x82/\x19Ðw\x05\xad_\x9a\x0e\x87à\x182æÎ\x12{\x94KO ¼À"klÏ~ëÓ\x05àÈã\x8b®À\x96\x8b¸û\x8c\x19\x96\x8e2/\x94\x0e7¦ ÷tÈ|æ\x96µ\'ãÞÆºÇç\x97à«8oS\x05,s|¬5y¾î\x910øûQ\x9b-\x186Ý\x9e\rN\x86\x07+Gëñíö¾l¢(\x99ò¶¸a\x0b²lèB\x1a"°½\t\x99¥;8ª\x92\x88Þ)Å\x99O\x0e\x91Åw\x06\x07\x9f\x11\n\x19\x02÷®o°\tíyï\x93\x00¬·\rDÖæÁ\x85\x93OG\x8a\x8c/U\x90Ì³EÊ\x80êa;7«7\x80C\x13ú@Âú\x062z\x02³qmf\tI\x01\x03\x13Ði\x13\x9b°\x0bì\'Ú\x98ß\x82q<¬\x88à}¡w\x82Æ%´®´B\x9e¾\x1f*\x19ê\x12·oâ\x84\x85å\x8e\x88<\x99\x9a\x92Jÿ¹\x80\x90\x8c½%ÑÅøñóz;\x19\x163\x95Ê1Îö¨{Ø58a\x95\x19Íù!Ç\x1b(\x0fÕ\x1a/ÜiÓ)ÆÃÜ\x94÷;£\x18o\x86É\x16D¥\x8b´û\x1b\x19ê=c0\x1b-\x06\x81ìs>7,\x18\x93áè±\x8c\x01Àî\x8a\x96Õ\x1d<B\x8flBÈGFÜ²X\x7fT,ª¢ßÚX\x1b\x87Ü\xad§y\x1dì\x16\x12\x94z\x8c\x125\x12?Ù\x02tdÐ·ã6\x06©%Å¹âvòû¡ì\x9b\x97\x8bè1¨\x96\x12áúg', '8=37<82:11=', False]
    ]
    
    Z5 = [
        [0, "t\x81«,«\x00ZØ\x97UØ\x80^ë#\x88\x16uNiðåè(h\x89ÊÒ¸a\x90\x86m\x1cp\x83+f\x10=ê\x87\x85É\xadQ\x98O\x90Û\x7fFùµ¯w)ys\x04\x98MÓ\x7f·éëÚ\x07}\x97¹{É\x8d}ÐÛé\x9d¤I^^*e¹%\x02ÛòN\x01\x19y\x9f\x05xU9Mnü\x94ç\x88Áf´\x1cÃr\x1cÆ]æyâ¯ËN\x80m÷Z'c.}¿R~¥\x07D)l\x93¤MÊR¿p«ÿÌþ¼?8\x8d\x04^}ÂX÷ÿ\x0fÐß»\x1d\x9d²Pïôk\x87}\x91\x86:m\x84Îr¬\xad©\x935Ó©¾|\x85\x95;\x8aBMû\x04\x7f:qm5:Z;Áêìw\x8c\x81# å\x18ÿ(%]×+%\x1c×Õ\x01J=Ð \x8a!p\x99ë1\x86\x1a,x=\x894hs½In\x91\x96â'C¾D6à\x06\x14Ì\x16¨jç\x9dB¯û\x7f$ÝÐÛFºÓÿùTÄ¾ý\x17\x05", '{\x80;FCt\x8dk{\x8ds0\x7fc\x85goymvQ\x82me\x81{:n{m', False],
        [1, '\x81\x9f¯\x92O¹~±ðeZ?,Bf\x9f\x92vv «\x93\x98,yatµ\xa0\x95\x8f¤t\x88F\x9e\xad \x90ª\x80R±\x9ebn\xa0u<\x91\x89°\x97z±\x87\x97\x8e¾\xa0Na\x8f£\x93Ãd\x13\r`q~6\x99\x92êt\x95\x9eZ_\x18','Qe\x84rtyf{"I\x85mvsm}~e', False],
        [2, '\x88£º\x96\x94Â\x82¥v³§\x80Û\x96XCP.tªÛv\x85i¬\x99\x9ezÞ,Ñu}g\x8f\x95\x95·k4\x92Æ\xa0·1eP[Âx¤®¢µ8ÝØ[d}Ä}ÊÓ¼5«\x90\x8bË\x83\xadßã\x8bàCÚ\x8eiÜ\x9d\x9b:\x8a½O\x9e¯{onlÙ~gÙ\x83Å\x88w¶\x89f\x84Eqvt\xa0\x8dy/,', 'Ijevijs', False],
        [3, '\x85\x1f¶\x8d\x92¸\x83\x9d{®¨\x8dàBY,:iØ\x87Òw\x86iª\x90\x90zß,Ón+·\x91¥Mcv\x83\x9b×¤µ±sO¯\x88RÁ«±\x80ßÈ\xad!\x80¹<ÙÜ¼\x81³\x90\x8b@t\xadÖÒF\x88\x9c½N\x97\x8d\x99Í\x94K±Àv}h\x8d\x82gÖ\x84ÏÖ\x84®@@n\x100¯u}ey/,', 'GWTDK', False],
        [4, "y½¡å\x9b\x08\x87\x90ÐÎíì*\x89,ToMlÜ\x9ePjõÚ$ts\x1d¤mÚ,\x83Å\x0bï=<êÜ5¨\x1e\x8bË°Yb\x9c\x0c\x8e\x15.\x92\x1b\x89\x9aø¿g)ss×ëE\x92X»\x89ØjKÑ\x14\x94Cô:8\x9fQ'ÞÐ\x13_ÞÜ\x9fo\x10\x11ugÞF»\x17k&¤\x05aHAìøí¸\xad\x9d\x97£®UµªÃ\x1e\x8e¬q\x9d4å\x8bÕ¢ËH\x8dÔò\x07Äl =\x8aðô®QÛ|á\x95«ÃÁ\x8eOÐU½\x08\x10;ù\x8a\x80³C\x15~ô²qºX\x12Kÿþ\x15Û¾\x17\x9b\\W>ïæÔ\x9c\x80»\x81\x892¥5Å¬_²Uìø\x9a\x05_NQõE,<\x02\x04\x8b\x88\x8d(5~\rÃ¨|Û\x8aé\x15UÓàü\x1ex&^Þ\x17æÊ\x91Õ\tE\x15\x8f{\x14:\x94¼õ\x93\x9c¢c\x8c(«N\x1f±\x8e\x02÷r\x86ßà<3ººå\x06\rº*¥gê!\x87\x06Zù{.áÙ\x86\x96é\x12ï\\{Ã8\x00O©\x06ñ?º¡£Î(¡Ê,2\r¸9Îà,\xa0V\x017H\x05éªZ¶¯Pê\x90\x9a|4\x82I\x19\x12¶Pôað\x0f\x81ðYäÍØjFÊU\x19´ÜËÉ\x98v\x00Ó*I½\x87³g¦\x03g|ÕÅH¢Ã6^v¬Aé\x18\x7f\\\x96âBLûÄ\x90ù¥äÀÑ³\xadï©hX\x1a\x1f¿-Ýûô1\xa0µ5YÖB\x80\xa0k\x8eÌ\x98.¾A÷ÀÙ=Ó\x89Ä\x1bâ\x8cÃ©+Õ~f¡|\x98C|\x86¯\r\x9að°\x0eëÊlB\x05!õRØcÃøÞi\x9b\x1eË\x7fv¿j\x8aÞÏ\x8f\x16\x99À\n\x8d Ì*;\x0b¾ÖÏqã¸\x1a\x87\x1f[R¥\x8f\x87cÛ(2$3ÆÍ\x06è\x02Ìq>¹ÿn]CªásË\xa0\x9d¡Êµ¤LÑÉ\x83â\x91ëÇY¿yUHÖ\x96¤NÕ\x19<£\x879\x14\x02È\x83ÞM?xÒy\x10çã\x0f:íRyþ\x1d\x9cã\x94ÜÝÙck1\x00«îý\x80ê\x0b\x04m\x93ty\x9cën{}¶ÃÖ\x9eÑghÁ0J\x9a\x95È!\x95Ï\x10lµÍê\x05J[?rºí\x87ê¼@¶", 'Xsc/HQkBvlsus[1TlM\x7f,_RP\'uoYOgog`M ceR"SrgEabJ', False]
    ]
    
    
    
    D()
    A("Welcome !\n\nInitialization in progress")
    for i in V(4):
        dots = '.'*i
        A("\r{}".format(dots), flush=H, end='')
        J.sleep(0.9)
    A("\nSuccess !")
    J.sleep(1.5)
    D()
    
    while Trigger_Initiation:
         try :
             cv=int(G("Unlock program : "))
         except:
             A("\nCannot convert into an integer\nPlease write only numbers\n\n")
         
         else:
             for i in V(4):
                 dots = '.'*i
                 A("\r{}".format(dots), flush=H, end='')
                 J.sleep(0.9)
             A("\nTrying to unlock program ... ")
             J.sleep(1.5)
             D()
             B.t.seed(cv)
             Trigger_Initiation=False
             D()
     
    while Trigger_before_menu:
        result, Z5 = Gr(Z5, cv)
        progression=[Z5[i][3] for i in V(a(Z5))]
        
        if B.array(progression).all():
            Trigger_before_menu=False
    
    menu_choice = X
    menu_subchoice= X
    D()
    B.t.seed(cv)
    G(E('\x81(\x85¥¾/]¨Yó\x0b$\x0b\x13\x0cËÞïv\xa0\x90ÝÏrÔohô¬\x1e\x97â\x9f\x96ø4\x1cÔ\x1bÆhl\x87\x86RÀ§nÛÈu\x0f<ßÕ\x89°\x18ÐÊ±¯\x9bJ×\x15\x92 \x97}\x0e\x9b\x10n|"\x13M\x94wõÔyê×6³\x15èõÉ¦Ý\x1bX\x89{C\x07ëÔ~¿\x8aÞSÀhå\x89Õ\x0cÂâ\x97é²\x12rÀgu\rï\x94¤\x9d´\x13*\xa0\x1ewçòéü¯Á¡C±{ta±[\x9dc\x19\x1dÀº\x92\\¸ç\x8a\x8cµÐ\x95E\x98Ï~õÈl \x11ó\x03}kÝyè¤\x00§\x0c\x08(\x9c'))
              
    
    while menu_choice != "ESC":
        
        if B.array(list(TH.values())).all()==H:
            menu_choice="ESC"
            break
        
        
              
        menu_choice = DM(TH,cv)
        if menu_choice == "1":
            if TH["choice1"]:
                B.t.seed(cv)
                A(E("^\x99/pz%\x83\x0b\x8c\x04G|\x83o\x99\x82õ>ll'\x85dzyREzñl\x8bvvvl\x97j\x8b\x82<I"))
                G("\n(Appuie sur n'importe quelle touche pour continuer)")
                D()
            else:
                
                while menu_subchoice!='ESC':
                    
                    if B.array(list(THX.values())).all()==H:
                        B.t.seed(cv)
                        A(E('\x93«D\x90\x82\\k.£ÿB¬\x94\x9f\x99~ú ª\x89¢,pe\x80¿L\x99\x8f§ow\x8b¥ \x92ª\x88¤Y¶}ªv\x92\x81\x87g\x97v^\x92\x8c\x8e£Z:\x8c\x18\x97kll\x86c\x85\x7f\x8foyFR'))
                        G("\n(Appuie sur n'importe quelle touche pour continuer)")
                        D()
                        menu_subchoice="ESC"
                        break
                    
                    menu_subchoice= DsM(THX,cv)
                    
                    if menu_subchoice=="1":
                        if THX["choice1"]:
                            B.t.seed(cv)
                            A(E('\x93«D\x90\x82\\k"\x89\x02X\x96¢\x93}\x87é^\x90Vuzdt\x8f\x95Ag\x87\x99¡c\x8b$3\x12Yn\xa0u\x90\x815\x9bz±\x9a\x88UN\x94\x03\x92\x98\x8ek}d\x86k\x80\x84\x93!\''))
                            G("\n(Appuie sur n'importe quelle touche pour continuer)")
                            D()
                        else:
                            sub_result, Z3=Gr(Z3, cv)
                            if sub_result=="ESC":
                                continue
                            THX["choice1"]=H
                            D()
                            B.t.seed(cv)
                            A(E('\x81\x96\x90Å~\\æZ¿÷,\x0c\x97\x07Í\x84\x1bò§\x99\x7fÞu ÿ¶ìæ\x95\x94ãfyØÒ=¸r\x87\x88¨²,b9\x91é!\x009<ÙÌ\x89»¼^Z\x8fa\x97Ó:Gø9µ¤Êkll2ý\x9fIàz²Øë\x8c\x17¦\x85/\x97\x0e+½\x80\x98ÂjÉ´Ûê©cAld,-³j¾Ü\x8béI\x01cO¯,}T\x85Z9Mé¨¾ÁO(\x98¿§´Ç¾g\x95Í·²\t\x9a\x9d/³D\x8cJµ¥NE\x87Å)\x02Yðc2pÀa*\xa0\x9a\x15B\x1e±\x89\x89\x9d\x07ÊðpÈ\x84\x1dì\x88Í\x9e¹³\x01?\x87±¡q¿g8ô\x08Ð®ª\x1a\x91\x9e]áæÕ¬.©\x81½\x86{¥*\x8aÕn³¨¹\x87\xa0xã±Ù¹\x7f\x88@*\x8cC\x99\x87a\x00û<\x86½%|\x87.gE\x87Ä<õwÞCâ\n\x7f÷î#ËÖRÎæk*ÍÇàÿ?»=¿\x15S\x8bÂ&\x82a\x0cW\x84\x1e\x80%=\x868ed±\x92qEê×ØB\x8fºF:£²þ¥P\'©Pjç§\x97°ì6\x1bÝ\x0e"\x81C\x11>ºúhÈ;5f\x06\x14{\x8düvíP'))
                            G("\n(Appuie sur n'importe quelle touche pour continuer)")
                            D()
             
                    elif menu_subchoice=="2":
                        if THX["choice2"]:
                            B.t.seed(cv)
                            A(E('\x93«D\x90\x82\\k"\x89\x02X\x96¢\x93}\x87é^\x90Vuzdt\x8f\x95Ag\x87\x99¡c\x8b$3\x12Yn\xa0u\x90\x815\x9bz±\x9a\x88UN\x94\x03\x92\x98\x8ek}d\x86k\x80\x84\x93!\''))
                            G("\n(Appuie sur n'importe quelle touche pour continuer)")
                            D()
                        else: 
                            sub_result, Z4=Gr(Z4, cv)
                            if sub_result=="ESC":
                                continue
                            THX["choice2"]=H
                            D()
                            B.t.seed(cv)
                            A(E( '\x85\r\x9b¸r¥û\x9a\x13\x8b\x91Øß¨2¡D\x82\x16Á{iî°\x97Ö\x9f\x8fé4Ñ{±n\x86|\x95²b\x7fÊÑu¼}êÛzµÏÌ±xF-x\x94f\x8bOºÄx{h\x8d\x84çÇùÝäy±\x89¡¡nÓÍ\x9d\x87\x81\x0c¹úzÏ\x8câ¦pz×Ü\x81\x0bÈÓãæ·\x86s\x88g\x0fì¡\x83¤\x93¦w\x92|ñ¤qü3l£\x95kÀf¢ºâ\x0bwq7\x81¹\x92\x88ÛµÔP\x99\x93Õs\x01ÕysÁ÷ó}¬\x9a|ß\x9aü\xad\x80\x95'))
                            G("\n(Appuie sur n'importe quelle touche pour continuer)")
                            D()
                   
                    if menu_subchoice == "ESC":
                         menu_subchoice=X
                         break
               
            if B.array(list(THX.values())).all()==H:
                D()
                G("""FÉLICITATIONS !!
            
Tu es venue à bout de cette petite chasse au trésor ... pour cette partie seulement ! 

(Appuie sur n'importe quelle touche pour continuer)""")
                D()
                TH["choice1"] = H
                    
        
        
        elif menu_choice == "2":
            if TH["choice2"]:
                B.t.seed(cv)
                A(E("^\x99/pz%\x83\x0b\x8c\x04G|\x83o\x99\x82õ>ll'\x85dzyREzñl\x8bvvvl\x97j\x8b\x82<I"))
                G("\n(Appuie sur n'importe quelle touche pour continuer)")
                D()
            else:
                result, Z1 = Gr(Z1, cv)
                if result == "ESC":
                    continue
                TH["choice2"] = H
                D()
                G("""FÉLICITATIONS !!
                
Tu es venue à bout de cette petite chasse au trésor ... pour cette partie seulement ! 

(Appuie sur n'importe quelle touche pour continuer)""")
                D()
        
                 
        elif menu_choice == "3":
            if TH["choice3"]:
                B.t.seed(cv)
                A(E('\x93\x99O°\x82\\ë"\x8c\x02\x8aàú\x80õ\x9aa,ß{n«´æë\x95\x8f¦xÊt¼r\x83\x81¥½±}Ý\x83k\x11\x8fçÜ<\'\x8bË\x00¬F\x86ÏÖ\x7f\x87¤|\x890\x13Há2ñÙú\x98Û\x82iÚôØ¦à\x96\x8c{\x88\x06ëyÎ8f¡¿yßÎ\x81\x0bÈ\x99àécnÁgyã\x87ò\x9dez\x92\x86\x9eèéö½l¤\x91èm³¢ºè\x91¹}M¥±\x92\x8eÍ`È\x91\x91\x90Ïr\x04\x80{e¤òô»ækÝ\x95\tY¸'))
                G("\n(Appuie sur n'importe quelle touche pour continuer)")
                D()
            else:

                
                result, Z2 = Gr(Z2, cv)
                if result == "ESC":
                    continue
                TH["choice3"] = H
                G("""FÉLICITATIONS !!
                
Tu es venue à bout de cette petite chasse au trésor ... pour cette partie seulement ! 

(Appuie sur n'importe quelle touche pour continuer)""")
                D()
                
    
        
    J.sleep(1)
    D()
    A("All data completed. Checking in progress")
    for i in V(4):
        dots = '.'*i
        A("\r{}".format(dots), flush=H, end='')
        J.sleep(0.9)
    A("\nSuccess !")
    J.sleep(1.5)
    D()
    A('''     ___   ___   _____ _   _ _____   _ _
    (  _ \|  _ \(  _  ) ) ( )  _  ) ( ) )
    | (_) ) (_) ) (_) | | | | ( ) | | | |
    |  _ (|    /(  _  ) | | | | | | | | |
    | (_) ) |\ \| | | | \_/ | (_) | (_)_)
    (____/(_) (_)_) (_)\___/(_____)
                                    (_)_)''')
    B.t.seed(cv)    
    A(E('n´/¯:¢\x12\r\x8b%\x92"Lßûzjî,\r,\x8c-è\nÑ`Þ\x99\x84,nç\x88Î!ÂsBx\xa0°(}Èç!\x10I<×Ú5¹\x94àÊ±S\r\x06\x0e\x97Ý\x1e=\x92"\x8c\x95M!Àt)$\x1cnáçUä\x08\x882\x13êîo\x13\x8c\x1a\x8f}Cü3o¿y¨\x10{\x99Â\x0er×åá¶óa_\x0b* \x81\x0fË\x9a\x02¤"S¦\x18}"]\x05d\x85V+@ã¤ìíj¯\x97,\x9d£ÁN¯KÔqj\x87ÍÁ¶W\x917+Ö\x81\x8cq\x93ü\x85Ï\x04\x06\x07Ölr<Áµ<³ó§*î\x9f§ÃO\x9e¾\x81@\x9dJ\x1fß\x06|Ç{\x11\x84\x1d:ì\x84Ó¹ÄH\x08ê\x8f\x00§\x80Âe\t÷ôL\x07\x11ß»\x17\x8b±WÂáæ¦\x88.uSMàpu\x14\x1f¦yg¤´B\x91+\x0cû\x08²k0\x8a@9\x8d\x98;\x8a\x95\tÿþ\t<\x83sÇwE\x82.m\x11A\x8fÈêü\x87\x8cv7rVèÓÐv\x18Ç+eÎ\x17:%+ÊÏÝ\x01ö\x10\x82{$G\x93¶úÒ\x0fð/\x96u\x85\x98\x18qþ1ú!:mÊs\x00\x9e\x03÷x\x8eãâ$-;±@ÍõÛ÷g\rÁ]$¥i\x95¥\x83L¬è\x84,Ý\x15Íç\x8d\x95Ð5\x0e\r¬ZÀÀ6\x17m\x14JeYì8\x0e`!\x97Ï7\x9dÊ+5\x10\x10¬ó7J26\xa00Vù8ù9ì?\x0ed\xa0V\x04»\x01Þ\x8b\x15vï\x83ÝºúÊ®WëqHÌ\x81\x19O\x06\x013RÔÓ\x93é±\x86\x1e³tÊÏÁ»¨n-\x898Ë9I\x97\x9b²n\x9dE\x06´}\x90ìF\x87\xa0û\x15+c\x15\x81\xad\x96÷ÓÀ^\x1cßË\t÷Ì\x94Xmùµ¬\x97¼Ø³Ô=´\x1c\x9cÜ\x15%±|ßöæ1 ½º\x9eÖrÎ\x10[a\x88\x7f\x11\x95.N\x12ÿ\x9c\x90-\x10û\x03?Òô\x8e\x9f)\x99ë\x88PÃµ+5Ù;²ÜÂÞ".%Ò\xa0\x0b\x96>þl\x15ß4Än¼÷\x1dñL!k\x8f~<Ö\x1a\x9bmÜ\x8ev6j7\x93wÞ\x8f\x15\x0bÅ\x9a°\råÔÛoç\x89³`O[àrôfA\x04\x18B\x17b×\x8c¥\x8d\x8b\x0flÈ6\x85¬ï¸Í\x06\x95\x05O!\x91\x9cD\x11þÏ1dÈMl#6²Ô\x87s#È\x8e \x90¦¼í\x95>\x89§e\x1e®\x9fö\x82\x90Î$\x88\\F\x7f,â\x8a¨\x8c\x8e\t\x02K\xa0\rUE\x1bóv\x923\x01?*¿ÌÇ\x83\x0bïÞ\x93:¨\x1bDÔâ3\x9a\x83nHâUâÎÜÕÙccZÜ I¼Þ«\x84å\x0b\x18v\x8f\x83&\x94Rúí\x11a{}kµÊ\x952\x08\xadv¾\x84òô\x02¦\x83¾3N\xadË\x10p»xäJ\x07_2gÄ\x9fvéï*/'))
    G("\n\n(Appuie sur n'importe quelle touche pour clore le programme)")

# Call the main function to run the script
if __name__ == "__main__":
    main()



