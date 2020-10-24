import random

def game():
    seed = []
    for i in range(0,9): seed.append(i+1)

    Ans = ""
    for i in random.sample(seed ,4):
        Ans += str(i)

    print ("Game start!!")
    print ("Please enter 4 numbers and press \"enter\"")

    x = "0000"
    count = 1
    #print ("Ans : %s" %Ans) # debug
    while Ans!= x:
        print ("============================")    
        print ('ROUND : %s' %count)
        x = input("Your answer is : ")
        if len(x) != 4:
            print ("Enter 4 numbers.")
            continue
        elif len(set(x)) != 4:
            print ("Enter 4 different numbers.")
            continue
        count +=1
        a = 0
        b = 0
        for i in range(4):
            if x[i]== Ans[i]:
                a+=1
            elif x[i] in Ans:
                b+=1
        print ("This round you got %sA %sB." %(a,b))

    print ("You Win!")

if __name__=='__main__':
    game = game()
