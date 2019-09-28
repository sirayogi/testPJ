def Nabeatsu(max_):
    if max_ >= 100:
        print("あほなので100以上は言えません")
        return
    
    strAho1 = ("いちぃ")
    for i in range(1, max_ + 1):
        if i % 3 == 0 or '3' in str(i):
            print("ここをあほにする")
        else:
            print(i)
            
            
if __name__ == "__main__":
    Nabeatsu(40)