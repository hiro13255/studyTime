#coding:utf-8
import os

#メニュー選択
def menu():
    print("1:目標値入力　2:学習時間入力　3:今までの学習時間を確認　4:目標までの時間を確認 5:終了")

#入力
def studyInput():
    print("学習時間を入力してください ->")
    time = input()
    return time
    
#終了
def inputEnd():
    print("アプリを終了します")


#メイン関数
if __name__ == "__main__":
    print("----------学習記録アプリへようこそ--------------")
    
    #データパス
    path = './goalTime.txt'
    path_total = './totalTime.txt'

    #データが存在するかチェック
    checkGoal = os.path.exists(path)
    checkeTotal = os.path.exists(path_total)

    #ファイルが存在するか確認
    if checkGoal == False:
        print("目標時間を入力してください ->")
        f = open(path,mode='w')
        goalTime = input()
        f.write(goalTime)
        f.close()

    #ファイルが存在するか確認
    if checkeTotal == False:
        ans = "0"
        fTotal = open(path_total,mode='w')
        fTotal.write(ans)
        fTotal.close()

    #ループ
    while True:

        menu()
        input_line = input()

        #目標値入力
        if "1" == input_line:
            f = open(path, mode='r')
            ing = f.readline()
            print("現在設定されている目標時間は" + ing + "時間です。")
            print("変更しますか？ 1:Yes 2:No")
            select = int(input())

            #１が入力されたら目標を上書きする
            if 1 == select:
                f = open(path,mode='w')
                print("新しい目標時間を設定してください ->")
                goal = input()
                f.write(goal)
                f.close()
            else:
                print("メニューに戻ります")

        #学習時間入力
        elif "2" == input_line:
            #読み込み
            fTotal = open(path_total,mode='r')
            writeTime = fTotal.readlines()
            time = studyInput()
            writeTime1 = int(writeTime[0])
            ans = writeTime1 + int(time)
            #書き込み
            fTotal = open(path_total,mode='w')
            fTotal.write(str(ans))
            fTotal.close()

        #今までの学習時間を確認
        elif "3" == input_line:
            fTotal = open(path_total,mode='r')
            totalTime = fTotal.readline()
            print("あなたが今まで学習した時間は" + totalTime+ "時間です")
            fTotal.close()

        #目標と結果の差分
        elif "4" == input_line:
            f = open(path,mode='r')
            writeGoalTime = f.readlines()

            fTotal = open(path_total,mode ='r')
            writeTotal = fTotal.readlines()

            sub = int(writeGoalTime[0]) - int(writeTotal[0])
            if 0 > sub:
                print("目標を達成しています。")
            else:
                print("目標まであと" + str(sub) + "時間です。")
            f.close()
            fTotal.close()

        #終了
        elif "5" == input_line:
            inputEnd()
            print("--------------------------------------------------")
            break

        else:
            print("指定した番号を入力してください")


