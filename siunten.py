from flask import Flask, render_template 
app = Flask(__name__) 
import random 



###

#with open("itiren-count.txt","w",encoding="utf_8")as file: 
#a入れたら実行した回数文追加
#    file.write(count2)
#    file.write("DEF\n")
#    file.write("GHI\n")
    

#読み込み
#file = open("itiren-count.txt","r",encoding="utf_8")
#data =file.read() #(1)にしたら1文字だけ表示される
#print(data)



###
count=0 #1ren nedan
count2=0 #11ren nedan

player = "あなた" 
# メニューを表示 
@app.route("/")
def menu(): 
    return render_template("menu.html", player = player) 
gatya = ["N","N+","R","R+","SR","SR+"] 

gazou =["n.jpg","n+.jpg","r.jpg","r+.jpg","sr.jpg","sr+.jpg"] 
deta =[0,0,0,0,0,0] #6個 1連ガチャ deta n n+ r r+ sr sr+

def detacheck(detalist): #一連 試運転　#def→定義　この場合 detacheckを関数定義した。
    for i in range(len(detalist)): #len(datalist)→長さはdatalistの長さ→6桁とか
        if detalist[5] == 0:
            return False #リストから０消えたらTrue
    return True

gatya11 = ["R","R+","SR","SR+"]
gazou11 =["r.jpg","r+.jpg","sr.jpg","sr+.jpg"] 
deta11=[0,0,0,0]
def ren(deta11list):
    for i in range(len(deta11list)):
        if deta11list[3] ==0: #[2:3]にすると2or3成立で表示される
            return False
    return True


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
        message2+="<br>" + "1連ガチャですべてのSR+が揃った！" + str(count2) + "円でコンプリートしました！"
    return render_template("itiren.html", player = player, message = message,message2=message2) 

@app.route("/juuitiren") 
def juuitiren():
    global count,count2
    count += 11
    count2 +=1000
    message = player + "は11連ガチャを購入！現在の購入金額は合計" + str(count2) + "円です！"
    message2 =""
    index11= 0
    for i in range(11): #がちゃの数11だから１１
        kakuritu = random.randint(1,100)
        index11 = 0
        if kakuritu<=3: #3
            index11 =3
        elif kakuritu<=13: #13
            index11 =2
        elif kakuritu<=43: #43
            index11 =1
        elif kakuritu<=100: #100
            index11 =0
        #elif kakuritu<=57:
          #  index =1
        #elif kakuritu<=57:
         #   index =0 #1からだとエラー
        deta11[index11] += 1#+すれば調整可能かも
        #else kakuritu=<70:
        #<img src="../static/gu.png" alt="Result">
        message2 += (gatya11[index11]) + " がでた！<img src=\"../static/" + gazou11[index11] + "\"><br>"
        #ずれ問題 def gatya gazou を別に作成して解消
        
        
        #message2 += (gatya[index]) + " がでた！<br>"
        #message2 +=str(count)  #文章をつけて、一連にもつける
    

    
    #↓ここミスるとリストが6個になるから data11に変更して4個にする。下も買えないとエラー注意
    message2 += "<br>" + ",".join(map(str,deta11))+"(R.R+.SR.SR+)" ##deta11変更点
    if ren(deta11) == True:
        message2+= "11連ガチャすべてのSR+が揃った" + str(count2) + "円でコンプリートしました！"
    #messege2 += str(deta)
 ##data11 変更点みすったらけすこと
    
    return render_template("juuitiren.html", player = player, message = message,message2=message2) 



#リセット
@app.route("/reset") 
def pa(): 
    with open("itiren-count.txt","w") as f:
        f.write("0")
    with open("juuitiren-count.txt","w") as f:
        f.write("0")
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
