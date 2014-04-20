import re
def clearSRT(fichier):
    src = open(fichier, "r")
    t = src.readlines()
    file = []
    file2=[]
    i=0
    for j in range(len(t)):
        if re.match(r"^\s",t[j],re.UNICODE):
            pass
        else:
            file.append(t[j])
    while i < len(file):
        if re.match(r"^\d+\s$",file[i],re.UNICODE):
            if re.match("\d{2}\:\d{2}\:\d{2}\,\d{3}",file[i+1]):
                i+=1
                pass
        file2.append(file[i].strip())
        i+=1 
    src.close()
    return file2
def conv(source,position):
    dataConverted=[]
    data = clearSRT(source)
    for i in range(len(data)):
        if re.match("\d{2}\:\d{2}\:\d{2}\,\d{3}",data[i]):
            temps1=data[i].split("-->")[0].replace(",",".").strip()[:-1]
            temps2=data[i].split("-->")[1].replace(",",".").strip()[:-1]
            x=i+1
            string=""
            while not re.match("\d{2}\:\d{2}\:\d{2}\,\d{3}",data[x]):
                if x-i>1:
                    string+="\\N"
                if x<len(data):
                    string+=data[x]
                x+=1
                if x>=len(data):
                    break
            dataConverted.append("Dialogue: 0,"+str(temps1)+","+str(temps2)+","+position+",,0000,0000,0000,,"+string)
    return dataConverted
def dualSubMaker(fichier1, fichier2):
    data = conv(fichier1,"Top")+conv(fichier2,"Bot")
    data.sort()
    data = "\n".join(data)
    content="[Script Info]\n"
    content+="ScriptType: v4.00+\n"
    content+="Collisions: Normal\n"
    content+="PlayDepth: 0\n"
    content+="Timer: 100,0000\n"
    content+="Video Aspect Ratio: 0\n"
    content+="WrapStyle: 0\n"
    content+="ScaledBorderAndShadow: no\n\n"
    content+="[V4+ Styles]\n"
    content+="Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
    content+="Style: Default,Arial,16,&H00FFFFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,10,10,10,0\n"
    content+="Style: Top,Arial,16,&H00F9FFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,8,10,10,10,0\n"
    content+="Style: Mid,Arial,16,&H0000FFFF,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,5,10,10,10,0\n"
    content+="Style: Bot,Arial,16,&H00F9FFF9,&H00FFFFFF,&H80000000,&H80000000,-1,0,0,0,100,100,0,0,1,3,0,2,10,10,10,0\n\n"
    content+="[Events]\n"
    content+="Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    content+=data
    fichier=open(fichier1[:fichier1.find(".")]+"_converted.ass","w")
    fichier.write(content)
    fichier.close()
def main():
    GHT = '''

            +=======================================+
            |........DualSubtitlesMaker v1.0........|
            +---------------------------------------+
            |#Author: Vladimir                      |
            |#Date: 17/04/2014                      |
            |#This tool can convert two .srt files  |
            |in one .ass file : one is displayed at |
            |the top of the video, the other one at |
            |the bottom. Use VLC.                   |
            +=======================================+
            |........DualSubtitlesMaker v1.0........|
            +---------------------------------------+
    '''
    print(GHT+"\n")
    fichier1=str(raw_input("Enter the name of the first file : "))
    fichier2=str(raw_input("Enter the name of the second file : "))
    dualSubMaker(fichier1, fichier2)
    print("File "+fichier1[:fichier1.find(".")]+"_converted.ass successfully generated")
if __name__ == '__main__':
    main()
