import gc

def Nabeatsu(max_):
    if max_ >= 100000:
        print("あほなので100000以上は言えません")
        return
    
    tplAho1 = ("", "イ～チ", "ニ～", "サ～ン", "ヨ～ン", "ゴ～", "ロ～ク", "ナ～ナ", "ハ～チ", "キュ～ウ")
    tplAho2 = ("", "", "ニ", "サン", "ヨン", "ゴ", "ロク", 'ナナ', 'ハチ', 'キュウ')
    tplAhox = ("", "", "ジュ", "ヒャク", "セン", "マン")
    for i in range(1, max_ + 1):
        if i % 3 == 0 or '3' in str(i):
            strAho = ""
            
            for digit, str1 in enumerate(str(i)[:-1]):
                strAho += tplAho2[int(str1)] + tplAhox[int(len(str(i)) - digit)]
            strAho += tplAho1[int(str(i)[-1])] + "！！"
            
            print(strAho)
        else:
            print(i)
            
        if i % 100 == 0:
            gc.collect()
        
if __name__ == "__main__":
    Nabeatsu(10003)