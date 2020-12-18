

#import nakanishi yuya
from flask import Flask, render_template,url_for 
app = Flask(__name__) 
import random 

count=0 #1ren nedan
count2=0 #11ren nedan

player = "あなた" 
# メニューを表示 
@app.route("/")
def menu(): 
    return render_template("menu.html", player = player) 
#gatya = ["N","N+","R","R+","SR","SR+"] 


gazou =["n.jpg","n+.jpg","r.jpg","r+.jpg","sr.jpg","sr+.jpg"] 
deta =[0,0,0,0,0,0] #6個 1連ガチャ deta n n+ r r+ sr sr+



#11連と1連で分けた場合deta deta11 gazou gazou11 gatya gatya11などと
#分けたほうがいい　defの定義も変えないとエラーになる.




def detacheck(detalist): #一連 試運転　#def→定義　この場合 detacheckを関数定義した。
    for i in range(len(detalist)): #len(datalist)→長さはdatalistの長さ→6桁とか
        if detalist[i] == 0:
            return False #リストから０消えたらTrue
    return True
#最後のSR+のみ揃ったときにするには → i を数字に変える[] の中身の数字
#if 分追加でで11回目に出るように設定する100

#11連の画像関係
#gatya11 = ["R","R+","SR","SR+"]
#gazou11 =["r.jpg","r+.jpg","sr.jpg","sr+.jpg"] 
#deta11=[0,0,0,0]

#11連の
gatya50 = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R13","R14","R15","R+1","R+2","R+3","R+4","R+5","R+6","R+7","R+8","R+9","R+10","R+11","R+12","R+13","R+14","R+15","SR1","SR2","SR3","SR4","SR5","SR6","SR7","SR8","SR9","SR10","SR+1","SR+2","SR+3","SR+4","SR+5","SR+6","SR+7","SR+8","SR+9","SR+10"]
deta50list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gazou50=["RARE(1).jpg","RARE(2).jpg","RARE(3).jpg","RARE(4).jpg","RARE(5).jpg","RARE(6).jpg","RARE(7).jpg","RARE(8).jpg","RARE(9).jpg","RARE(10).jpg","RARE(11).jpg","RARE(12).jpg","RARE(13).jpg","RARE(14).jpg","RARE(15).jpg","RARE(16).jpg","RARE(17).jpg","RARE(18).jpg","RARE(19).jpg","RARE(20).jpg","SRARE+(1).jpg","SRARE+(2).jpg","SRARE+(3).jpg","SRARE+(4).jpg","SRARE+(5).jpg","SRARE+(6).jpg","SRARE+(7).jpg","SRARE+(8).jpg","SRARE+(9).jpg","SRARE+(10).jpg","SRARE(1).jpg","SRARE(2).jpg","SRARE(3).jpg","SRARE4().jpg","SRARE(5).jpg","SRARE(6).jpg","SRARE(7).jpg","SRARE(8).jpg","SRARE(9).jpg","SRARE(10).jpg"]

#1連
gatya = ["N","N+","R","R+","SR","SR+"] 


#gatya70 = ["N1","N2","N3","N4","N5","N6","N7","N8","N9","N"10,,"N11","N12","N13","N14","N15","N16","N17","N18","N19","N20","N+1","N+2","N+3","N+4","N+5","N+6","N+7","N+8","N+9","N+10","N+11","N+12","N+13","N+14","N+15","N+16","N+17","N+18","N+19","N+20","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12","R"13,"R14","R15","R+1","R+2","R+3","R+4","R+5","R+6","R+7","R+8","R+9","R+10","R+11","R+12","R+13","R+14","R+15","SR1","SR2","SR3","SR4","SR5","SR6","SR7","SR8","SR9","SR10","SR+1","SR+2","SR+3","SR+4","SR+5","SR+6","SR+7","SR+8","SR+9","SR+10"]
#deta70list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
#gazou70=["NOMAL(1).jpg","NOMAL(2).jpg","NOMAL(3).jpg","NOMAL(4).jpg","NOMAL(5).jpg","NOMAL(6).jpg","NOMAL(7).jpg","NOMAL(8).jpg","NOMAL(9).jpg","NOMAL(10).jpg","NOMAL(11).jpg","NOMAL(12).jpg","NOMAL(13).jpg","NOMAL(14).jpg","NOMAL(15).jpg","NOMAL(16).jpg","NOMAL(17).jpg","NOMAL(18).jpg","NOMAL(19).jpg","NOMAL(20).jpg","NOMAL+(1).jpg","NOMAL+(2).jpg","NOMAL+(3).jpg","NOMAL+(4).jpg","NOMAL+(5).jpg","NOMAL+(6).jpg","NOMAL+(7).jpg","NOMAL+(8).jpg","NOMAL+(9).jpg","NOMAL+(10).jpg","NOMAL+(11).jpg","NOMAL+(12).jpg","NOMAL+(13).jpg","NOMAL+(14).jpg","NOMAL+(15).jpg","NOMAL+(16).jpg","NOMAL+(17).jpg","NOMAL+(18).jpg","NOMAL+(19).jpg","NOMAL+(20).jpg","RARE(1).jpg","RARE(2).jpg","RARE(3).jpg","RARE(4).jpg","RARE(5).jpg","RARE(6).jpg","RARE(7).jpg","RARE(8).jpg","RARE(9).jpg","RARE(10).jpg","RARE(11).jpg","RARE(12).jpg","RARE(13).jpg","RARE(14).jpg","RARE(15).jpg","RARE(16).jpg","RARE(17).jpg","RARE(18).jpg","RARE(19).jpg","RARE(20).jpg","SRARE+(1).jpg","SRARE+(2).jpg","SRARE+(3).jpg","SRARE+(4).jpg","SRARE+(5).jpg","SRARE+(6).jpg","SRARE+(7).jpg","SRARE+(8).jpg","SRARE+(9).jpg","SRARE+(10).jpg","SRARE(1).jpg","SRARE(2).jpg","SRARE(3).jpg","SRARE4().jpg","SRARE(5).jpg","SRARE(6).jpg","SRARE(7).jpg","SRARE(8).jpg","SRARE(9).jpg","SRARE(10).jpg"]



#複数あるのは listっていう名前にしたほうがわかりやすい
#string とかアンダーバーで勘違い対策を行う。
#試運転領域-------------------------------
def ren(deta50list):
    for i in range(len(deta50list)):
        if deta50list[40:49] ==0: # =を１つにするとエラー
            return False
    return True
#-----------------------------------------
#1125動かない理由


#def ren(deta11list):
#    for i in range(len(data11list)):
#        if deta11list[i] ==0:
#            return false
#    return True
#作動しない理由

#deta11 =[0,0,0,0]
#def deta11check(deta11list):
#    for i in range(len(deta11list)):
#        if deta11list[i] == 0:
#            return False #リストから０消えたらTrue
#    
#    return True

@app.route("/itiren") 
def itiren(): 
    global count,count2
    count += 1 #ガチャ回数
    count2 +=100 #ガチャ料金
    kakuritu = random.randint(1,100)
    index = 0
    if kakuritu <=2: #2
        index =5
    elif kakuritu<=7: #7
        index =4
    elif kakuritu<=22: #22
        index =3
    elif kakuritu<=42: #42
        index =2
    elif kakuritu<=67: #67
        index =1
    elif kakuritu<=100: #100
        index =0
    #else kakuritu=<70:
    
    deta[index] += 1
    message = player + "は1連ガチャを購入！現在の購入金額は合計" + str(count2) + "円です！"
    #合計の購入金額のメッセージ
    
    
    message2 =(gatya[index]) + " がでた！<img src=\"../static/" + gazou[index] + "\"><br>" #画像改行
    #message2 += str(detacheck(deta)) flase trueの表示
    message2 += "<br>" + ",".join(map(str,deta)) +"(N.N+.R.R+.SR.SR+)｛購入カウンター｝"
    #↑一連ガチャカウンター表示
    #A="a","b","c" s="".join(A) →abc となる
    
    if detacheck(deta) == True:
        message2+="<br>" + "すべてのカードが揃った！" + str(count2) + "円でコンプリートしました！"

    
    return render_template("itiren.html", player = player, message = message,message2=message2) 
    
# 11連ガチャ
@app.route("/juuitiren") 
def juuitiren():
    global count,count2
    count += 11
    count2 +=1000
    index11=0
    for i in range(11): #がちゃの数11だから１１
        kakuritu = random.randint(1,1000)
        index11 = 0
        if kakuritu<=3: #3
            index11 =49
        elif kakuritu<=6: #13
            index11 =48
        elif kakuritu<=9: #43
            index11 =47
        elif kakuritu<=12:
            index11 =46
        elif kakuritu<=15:
            index =45
        elif kakuritu<=18:
            index =44
        elif kakuritu<=21:
            index =43
        elif kakuritu<=24:
            index =42
        elif kakuritu<=27:
            index =41
        elif kakuritu<=30:
            index =40 #1０個
        elif kakuritu<=40:
            index =39
        elif kakuritu<=50:
            index =38
        elif kakuritu<=60:
            index =37
        elif kakuritu<=70:
            index =36
        elif kakuritu<=80:
            index =35
        elif kakuritu<=90:
            index =34
        elif kakuritu<=100:
            index =33
        elif kakuritu<=110:
            index =32
        elif kakuritu<=120:
            index =31
        elif kakuritu<=130:
            index =30 #２０個
        elif kakuritu<=150:
            index =29
        elif kakuritu<=170:
            index =28
        elif kakuritu<=190:
            index =27
        elif kakuritu<=210:
            index =26
        elif kakuritu<=230:
            index =25
        elif kakuritu<=250:
            index =24
        elif kakuritu<=270:
            index =23
        elif kakuritu<=290:
            index =22
        elif kakuritu<=310:
            index =21
        elif kakuritu<=330:
            index =20 #30
        elif kakuritu<=350:
            index =19
        elif kakuritu<=370:
            index =18
        elif kakuritu<=390:
            index =17
        elif kakuritu<=410:
            index =16
        elif kakuritu<=430:
            index =15
        elif kakuritu<=468:
            index =14
        elif kakuritu<=506:
            index =13
        elif kakuritu<=544:
            index =12
        elif kakuritu<=582:
            index =11
        elif kakuritu<=620:
            index =10
        elif kakuritu<=658:
            index =9
        elif kakuritu<=696:
            index =8
        elif kakuritu<=734:
            index =7
        elif kakuritu<=772:
            index =6
        elif kakuritu<=810:
            index =5
        elif kakuritu<=848:
            index =4
        elif kakuritu<=886:
            index =3
        elif kakuritu<=924:
            index =2
        elif kakuritu<=962:
            index =1
        elif kakuritu<=1000:
            index =0
            
        deta50list[index11] += 1#+すれば調整可能かも
        #else kakuritu=<70:
        #<img src="../static/gu.png" alt="Result">
        message = player + "は1連ガチャを購入！現在の購入金額は合計" + str(count2) + "円です！"
        message2 =""

        message2 += (gatya50[index11]) + " がでた！<img src=\"../static/" + gazou50[index11] + "\"><br>"
        #ずれ問題 def gatya gazou を別に作成して解消
        
        
        #message2 += (gatya[index]) + " がでた！<br>"
        #message2 +=str(count)  #文章をつけて、一連にもつける
    

    
    #↓ここミスるとリストが6個になるから data11に変更して4個にする。下も買えないとエラー注意
    message2 += "<br>" + ",".join(map(str,deta50list))+"(R.R+.SR.SR+)" ##deta11変更点
    if ren(deta50list) == True:
        message2+= "すべて揃った！" + str(count2) + "円でコンプリートしました！"
    #messege2 += str(deta)
 ##data11 変更点みすったらけすこと
    
    return render_template("juuitiren.html", player = player, message = message,message2=message2) 



#リセット
@app.route("/reset") 
def pa(): 
    global deta,deta11,count,count2
    deta =[0,0,0,0,0,0] #6個 1連ガチャ deta n n+ r r+ sr sr+
    deta11=[0,0,0,0]
    count=0
    count2=0
    message = player + "はリセットを選択" 
    message2 ="数値はリセットされた"
    #"私は " + (gatya[random.randint(0,2)]) + " を出した" 
    return render_template("pa.html", player = player, message = message,message2=message2) 
    #golobal count = 0 
#    if count>=0:
#        count = 0
#        global count = 0
