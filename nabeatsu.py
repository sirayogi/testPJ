import gc

def Nabeatsu(min_, max_):
    if max_ >= 1000000000000:
        print("あほなので1兆以上は言えません")
        return
    
    tplAho1 = ("", "イ～チ", "ニ～", "サ～ン", "ヨ～ン", "ゴ～", "ロ～ク", "ナ～ナ", "ハ～チ", "キュ～ウ")
    tplAho2 = ("", "", "ニ", "サン", "ヨン", "ゴ", "ロク", 'ナナ', 'ハチ', 'キュウ')
    tplAhox = ("", "", "ジュ", "ヒャク", "セン", "マン","ジュウ","ヒャク","セン","オク","ジュウ","ヒャク","セン")
    tplAhox2 = ("", "イチ", "ニ", "サン", "ヨン", "ゴ", "ロク", 'ナナ', 'ハチ', 'キュウ')
    for i in range(min_, max_ + 1):
        if i % 3 == 0 or '3' in str(i):
            strAho = ""
            
            for digit, str1 in enumerate(str(i)[:-1]):
                if (int(len(str(i))) - digit) % 4 == 1:
                    strAho += tplAhox2[int(str1)] + tplAhox[int(len(str(i)) - digit)]
                elif str1 != "0":
                    strAho += tplAho2[int(str1)] + tplAhox[int(len(str(i)) - digit)]
            strAho += tplAho1[int(str(i)[-1])] + "！！"
            
            print(strAho)
        else:
            print(i)
            
        if i % 100 == 0:
            gc.collect()
        
if __name__ == "__main__":
    Nabeatsu(1, 10000003)