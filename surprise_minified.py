#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:30:54 2023

@author: Gus
"""

T=range
B=chr
S=len
Q='choice3'
P='choice2'
O='choice1'
K='ESC'
H=True
G=input
A=print
import os,time as J,numpy as C
def D():os.system('cls'if os.name=='nt'else'clear')
def F(d):
	D=S(d);A=''
	for E in d:A+=B((ord(E)-C.random.randint(D)%256)%256)
	return A
def I(r):
	D=S(r);A=''
	for E in r:A+=B((ord(E)+C.random.randint(D)%256)%256)
	return A
def E(question,expected_answer,seed):
	while H:
		C.random.seed(seed);E=G(F(question));C.random.seed(seed)
		if I(E)==expected_answer:return H
		elif E==B(27):return K
		else:A('Mauvaise réponse. Essaye encore');J.sleep(.7);D()
def h(progress,seed):
	E=progress;B=seed;D();C.random.seed(B);A(F('\x82%\x91\x9c´/°üY\x00\x95Ø\x92%ÄÖÑ¨tï,\x97ì\x10\x80Ð~ ðµÌæç¦\x93ç\x82\x1a\x85\x1e¹hd\x91.\x86\x9b²+b\x7fRÏ¤d\x04}èÎþsËßÌ±\x9f\x99Câ\x1bá\x17!:\x89\x97\x1aÁÀu)ã\x8dvkÇ\x00íè\x88²\x12\x95âÚçÚ\x1aQ\x84$/\x93\x08û*zÃ\x8a\x9d£ÂðæÎÏþÅ×\x97]c\x11oÊghÿÞ\x87\x1cùcO¯*ÝQÌ3\x9eÕýíj¿\x9e\x98ë®¯µ\x0cÄ¢\x96\x1eÍ°É\x9d¨´ä}Þ`Ï\x91\x8e\x92Ôn\x00ÁutÁ¾®\x15U\x9a*\x9aP·Y·ÃÖ\x93'))
	if E[O]:C.random.seed(B);A(F(';2/jcLWZKPÙa*Sumu'))
	else:C.random.seed(B);A(F('70$Pnfz'))
	if E[P]:C.random.seed(B);A(F('<2/jcLWZKPÙa*Km|e'))
	else:C.random.seed(B);A(F('80$Hfuj'))
	if E[Q]:C.random.seed(B);A(F('I8$jcTnTNgÖ_8O\x7f}ou,lv;t\x90e\x86\x82|z~\x92'))
	else:C.random.seed(B);A(F('=2/\\~\x80j{"fu$~ymv\x84ps\x81\x80'))
	A('\nAppuie à tout moment sur "ÉCHAP+ENTRÉE" pour revenir au menu');H=G('\nTon choix: ');return H
def N(questions,seed):
	A=questions
	for(I,F,G,I)in A:
		if I:continue
		D();B=E(F,G,seed)
		if B==K:return B,A
		A[I][3]=H
	return None,A
def L():
	g='Press any key to continue...';f="\n(Appuie sur n'importe quelle touche pour continuer)";e="^\x99/pz%\x83\x0b\x8c\x04G|\x83o\x99\x82õ>ll'\x85dzyREzñl\x8bvvvl\x97j\x8b\x82<I";d='\nSuccess !';c='\r{}';W="FÉLICITATIONS !!\n                \nTu es venue à bout de cette petite chasse au trésor ... pour cette partie seulement ! \n\n(Appuie sur n'importe quelle touche pour continuer)";B=False;X=H;Y=H;I={O:B,P:B,Q:B};Z=[[0,'Question 1: What is the capital of France?','Paris',B],[1,'Question 2: What is the color of the sky?','Blue',B],[2,'Question 3: What is the result of 2 + 2?','4',B],[3,'Question 4: What programming language is used in this script?','Python',B],[4,'Question 5: What is the chemical symbol for oxygen?','O',B]];a=[[0,"\x83\x85£´IF\x15¨\x14_B\x1c\x0b[Ñ\x83hé,\x89~\x8bxa««Øæ\x95A'_4Ù!Âhc\x83w\x97®.n+×0!\x125\x8f\x96Ëz½Æ§\\FT\x84×\x8c\x8bø\x9f\x1d³Ðxn#vÉ±ìAÞ{·é×¦Ü\x15¦\x92/\x84\x05w¿\x8aSÄyÐÈèÜïcGlYômF´j¾æ\x87÷ûJ\x97©\x0em\x96X3X==¤òq\xad\x98ç\x87¶¹´\x10Æk\x8e\x96kÆWM¬+º8Ü¡Ô¤K\x9a\x98\x807À\x15\x80\x11J.+¿N*¢\x9a\x16R+¾\x81LOO\x1f\x06|Í?qú\x8bÓY\x05´Mê\x02ý'y²aKþº\x14T³\x8eH\x1c\x0bð'\x81\x9bw¸\x8c¶\x87\x83¦s\x84Ï1g¤ºB¢Áã\nø¸xw\x898>\x87\x0e\x8cÉ¬\x02\x81\x8dxtÖØq\x81@\x19@\n¸/û\x85Í~4eèÓ®¿b\tX\x890fÑ\x1cÁÑ\x94\x07Kh\x82ÎÐ\x95\x8aÂ#\x84\x1eg=C)mu?74[h±\x95jEãá,î\x8e±òÉ6ê\x05Yxc0¥¥l^X\x92©ü\x88ØÙ\x05\x10\x01\x87\x15;\x85z¬hÉr3\\pJØe¿8¤&\x91\x8f\x96Ð",'R;w@qj}4>;hov~',B],[1,'y}\\5\x9e\x13V,BPÚ_é!\x89,Û{uý\x97Þ$\x1a×!Ét\x87mø\x15·0!ÿ<ÛÙx¿£]Fc\x91ÓF<\x0cÏg5#\x00q\x00Ö¸ãé\x8c\x16t\x98\r8É\x86\'ÃÛÜëcGo_<v¬w¾ïò@\x01\tk¥J\x07ö\x06²¨9\x0f\x0cÀ¯µ\x0cÄ\x1e\x1d²\\æø\x8c¦ÑQÉuþLy 9l½]y¥\x17\x0bÖ¸\x85OO\x0fSÊp«{Ó\roO8~±\xa0u²a÷î\x0f"Ô®#\x9b¡\x0bß.ÐªsJ4X\x88t¼¡²\x97(Çù«}6\x91:\x8aB]\x01¶\x80\x89n{5AkAÊ@í\x84\x8c7nÚÓñ\x16*T\x896w¤ÁÝ\x06;=\x83\x1d\x8d\x1b\x82a"\x8d$\x81wú0l\x1fù\x8ez\x97Û\x92Ù÷zÜß»óh½\x0f2hä\xad\x98#ì6àÙ\x03Ü\x1d6Éö]\x8aº+ \x1c\x1beÓ','8=37=839115',B]];b=[[0,'Question 1: What is the capital of Italy?','Rome',B],[1,'Question 2: What is the color of a banana?','Yellow',B],[2,'Question 3: What is the result of 7 - 4?','3',B]];R=[[0,'t\x81«,«\x00ZØ\x97UØ\x80^ë#\x88\x16uNiðåè(h\x89ÊÒ¸a\x90\x86m\x1cp\x83+f\x10=ê\x87\x85É\xadQ\x98O\x90Û\x7fFùµ¯w)ys\x04\x98MÓ\x7f·éëÚ\x07}\x97¹{É\x8d}ÐÛé\x9d¤I^^*e¹%\x02ÛòN\x01\x19y\x9f\x05xU9Mnü\x94ç\x88Áf´\x1cÃr\x1cÆ]æyâ¯ËN\x80m÷Z\'c.}¿R~¥\x07D)l\x93¤MÊR¿p«ÿÌþ¼?8\x8d\x04^}ÂX÷ÿ\x0fÐß»\x1d\x9d²Pïôk\x87}\x91\x86:\x80þÓn\xad¨«\xa0ã\x18þ¯*\x8a\x95å\x86\x95\tîÿ\x81\x88%zz;mD>êôw\x8cw1n\x95\x16ü\x19\x1b\x1b\x89:w*Óêøö\x89ÀÐ\x8b\x13x¡"u\x88Õxfú\x870jr\x00\x97s\x8a\x96Ó1/ºFõì\x02`ÇP"ß\x95\x9b\x87Zúy*á\x12!FºÓÿùTÄ¾ý\x17\x05','{\x80;FCt\x8dk{\x8ds0\x7fc\x85goymvQ\x82me\x81{:n{m',B],[1,'\x81\x9f¯\x92O¹~±ðeZ?,Bf\x9f\x92vv «\x93\x98,yatµ\xa0\x95\x8f¤t\x88F\x9e\xad \x90ª\x80R±\x9ebn\xa0u<\x91\x89°\x97z±\x87\x97\x8e¾\xa0Na\x8f£\x93Ãd\x13\r`q~6\x99\x92êt\x95\x9eZ_\x18','Qe\x84rtyf{"I\x85mvsm}~e',B],[2,'\x88£º\x96\x94Â\x82¥v³§\x80Û\x96XCP.tªÛv\x85i¬\x99\x9ezÞ,Ñu}g\x8f\x95\x95·k4\x92Æ\xa0·1eP[Âx¤®¢µ8ÝØ[d}Ä}ÊÓ¼5«\x90\x8bË\x83\xadßã\x8bàCÚ\x8eiÜ\x9d\x9b:\x8a½O\x9e¯{onlÙ~gÙ\x83Å\x88w¶\x89f\x84Eqvt\xa0\x8dy/,','Ijevijs',B],[3,'\x85\x1f¶\x8d\x92¸\x83\x9d{®¨\x8dàBY,:iØ\x87Òw\x86iª\x90\x90zß,Ón+·\x91¥Mcv\x83\x9b×¤µ±sO¯\x88RÁ«±\x80ßÈ\xad!\x80¹<ÙÜ¼\x81³\x90\x8b@t\xadÖÒF\x88\x9c½N\x97\x8d\x99Í\x94K±Àv}h\x8d\x82gÖ\x84ÏÖ\x84®@@n\x100¯u}ey/,','GWTDK',B],[4,"y½¡å\x9b\x04\x8e\x8e\x15\x8cqã-\x90q\x97,Noç¢\x1aù`$t!CRWÃ^ÌÛu\x11ô}é\x87\x89¹\x1aàÍ'\nY\x8bCÛ\x18=\x92\x12\x7fFH¼u|h2ÔR[K2\x04Úï[\x8cÈ\x00C>»8\x9f_\x80ÓÍÿ \x9e\x9d·e½d¬ðS¦\x0e}Ý\x9eF]ULãòé¸ÀO\x84ù¼H¸a½_B»À\xa08ÛzÕ¬ËP\r\x80mL\x80{é5\x8açs¬[áoìP®\x11l\x84\x9eÏ[Çø\x11J«zÉÁ?\x06\x8dö«q»gÄ;D\n%Ô¼Î\x94¡^ù9Æ©\x84ª\x91\x863RyÆg«msúõ\x8d\x0bDNQç/uR\x07\x05\x8aF\x81j<z\x16uò\x81áþ Õ\x95'ÛöÕÈ%dÛÅ2\x85Ëê\x02?\x1e=¿\x15K\x87ÁpÊé\x96k\x96ÕÿOÊö\x9c¯Df\x8eäæ-<\xadÇë²OÄ-§k^\x9dNú¬ì\x8c!Ù\x86\x96é\x12ï\\{Ã8\x00O©\x06ñ?º¡£Î(¡Ê,2\r¸9Îà,\xa0V\x017H\x05éªZ¶¯Pê\x90\x9a|4\x82I\x19\x12¶Pôað\x0f\x81ðYäÍØjFÊU_\x1cû»Æ\x1ew}\x862\x8aº\x8b¾tQõ¬8Ó\n\x05©\x0c/c1¢\x86¥'HT\x96¼QôÕ\x85÷\xadÜÉ×y\x938¬\x1c\x9d( k}ßøù¦\x1e7zKù&¾®l:!\x91à\x0e6\x07k\x1cIÒ;\x08 \x8cÃ©+Õ~f¡|\x98C|\x86¯\r\x9að°\x0eëÊlB\x05!õRØcÃøÞi\x9b\x1eË\x7fv¿j\x8aÞÏ\x8f\x16\x99À\n\x8d Ì*;\x0b¾ÖÏqã¸\x1a\x87\x1f[R¥\x8f\x87cÛ(2$3ÆÍ\x06\x10\x11WXÏÿÙZ=xÇ»×\xa0\x99¤\x91ª¤\x86ÖÊ\x8aÍ\x93í\x90\x90Ï3\x8dB\x96¤NÕ\x19<£\x879\x14\x02È\x83ÞM?xÒy\x10çã\x0f:`{ï§\x10òÙ\x8bÙé¨\x170UjÚ\x00\x91Ø^Âf\x97kÇIc÷Í)¸ÆÐ\x9d^0'\xad\x85ú©\x83È3\x8fÑU\x1c¶ÇZY\x0c4m¿ó{ó¿k\x08ã\xa0",'Xsc/HQkBvlsus[1TlM\x7f,_RP\'uoYOgog`M ceR"SrgEabJ',B]];D();A('Welcome !\n\nInitialization in progress')
	for U in T(4):V='.'*U;A(c.format(V),flush=H,end='');J.sleep(.9)
	A(d);J.sleep(1.5);D()
	while Y:
		try:E=int(G('Unlock program : '))
		except:A('\nCannot convert into an integer\nPlease write only numbers\n\n')
		else:
			for U in T(4):V='.'*U;A(c.format(V),flush=H,end='');J.sleep(.9)
			A(d);J.sleep(1.5);D();C.random.seed(E);Y=B;D()
	while X:
		L,R=N(R,E);i=[R[A][3]for A in T(S(R))]
		if C.array(i).all():X=B
	M=None;D();C.random.seed(E);G(F('\x81(\x85¥¾/]¨Yó\x0b$\x0b\x13\x0cËÞïv\xa0\x90ÝÏrÔohô¬\x1e\x97â\x9f\x96ø4\x1cÔ\x1bÆhl\x87\x86RÀ§nÛÈu\x0f<ßÕ\x89°\x18ÐÊ±¯\x9bJ×\x15\x92 \x97}\x0e\x9b\x10n|"\x13M\x94wõÔyê×6³\x15èõÉ¦Ý\x1bX\x89{C\x07ëÔ~¿\x8aÞSÀhå\x89Õ\x0cÂâ\x97é²\x12rÀgu\rï\x94¤\x9d´\x13*\xa0\x1ewçòéü¯Á¡C±{ta±[\x9dc\x19\x1dÀº\x92\\¸ç\x8a\x8cµÐ\x95E\x98Ï~õÈl \x11ó\x03}kÝyè¤\x00§\x0c\x08(\x9c'))
	while M!=K:
		M=h(I,E)
		if M=='1':
			if I[O]:C.random.seed(E);A(F(e));G(f)
			else:
				L,Z=N(Z,E)
				if L==K:continue
				I[O]=H;D();G(W)
		elif M=='2':
			if I[P]:C.random.seed(E);C.random.seed(E);A(F(e));G(f)
			else:
				L,a=N(a,E)
				if L==K:continue
				I[P]=H;D();G(W)
		elif M=='3':
			if I[Q]:C.random.seed(E);A('You have already completed Choice 3.');G(g)
			else:
				D();A('You have chosen Choice 3.');L,b=N(b,E)
				if L==K:continue
				I[Q]=H;G(W)
	J.sleep(1);D();C.random.seed(E);A('You have completed the script. Goodbye!');G(g)
if __name__=='__main__':L()