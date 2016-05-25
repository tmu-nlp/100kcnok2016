#-*- coding:utf-8 -*-

def mkChunkclass(morphlist):
    class Chunk:
        def __init__(self,morph,dst,srcs):
            self.morph=morph
            self.dst=dst
            self.srcs=srcs

    import re
    l=list()
    la=list()
    morph=list()
    c1=0
    c2=0
    dst=""
    srcs=""
    for line in open("neko.txt.cabocha","r"):
        if line.startswith("EOS")==True:
            c1+=1
            la+=[l]
            l=list()
            c2=0
        elif line.startswith("*")==True:
            srcs=line.split(" ")[1]
            dst=line.split(" ")[2].strip("D")
            if c1+c2!=0:
                chunk=Chunk(morph,dst,srcs)
                l+=[chunk]
                morph=[]
        else:
            morph+=[morphlist[c1][c2]]
            c2+=1
    return(la)

if __name__=="__main__":
    from knock40 import mkMorphclass
    c=0
    for l in mkChunkclass(mkMorphclass()):
        c+=1
        if c==8:
            for ch in l:
                print(ch.dst+" "+ch.srcs)