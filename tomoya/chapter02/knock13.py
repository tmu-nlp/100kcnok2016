#coding: utf-8
import sys
col1 = open("col1.txt", "r").readlines()
col2 = open("col2.txt", "r").readlines()
merge = open("merge.txt", "w")
for (cl1, cl2) in zip(col1, col2):
        merge.write(cl1.rstrip("\n") + "\t" + cl2)
merge.close()

#flamie:chapter02 tomoya$ paste col1.txt col2.txt
#高知県  江川崎
#埼玉県  熊谷
#岐阜県  多治見
#山形県  山形
#山梨県  甲府
#和歌山県    かつらぎ
#静岡県  天竜
#山梨県  勝沼
#埼玉県  越谷
#群馬県  館林
#群馬県  上里見
#愛知県  愛西
#千葉県  牛久
#静岡県  佐久間
#愛媛県  宇和島
#山形県  酒田
#岐阜県  美濃
#群馬県  前橋
#千葉県  茂原
#埼玉県  鳩山
#大阪府  豊中
#山梨県  大月
#山形県  鶴岡
#愛知県  名古屋
