import mysql.connector as mys
import random
import time
mycon=mys.connect(host='localhost',user='root',passwd='2130',database='funland')
mycursor=mycon.cursor()
def maths_quiz():
    print("!"*25,"HI! WELCOME TO MATHS QUIZ MASTER","!"*25)
    a=input("ARE YOU READY TO PLAY????(Y/N): ")
    if a.upper()=="Y":
        print("PLEASE ENTER YOUR NAME: ")
        nm=input()
        start=time.time()
        time.sleep(1)
        operators=['+','-','*','/']
        score=0
        print("!"*25,"LET'S START THE QUIZ","!"*25)
        print('''RULES:
     FOR EVERY CORRECT ANSWER : +4
     FOR EVERY WRONG ANSWER : -1
     MAXIMUM MARKS: 40''')
        correct=0
        wrong=0
        for i in range(10):
            print("-"*75)
            n1=random.randrange(1,100)
            n2=random.randrange(1,100)
            i=random.randrange(0,4)
            a=operators[i]
            result=0
            if a=='+':
                result=n1+n2
            elif a=='-':
                if n1<n2:
                    n1,n2=n2,n1
                result=n1-n2
            elif a=='*':
                result=n1*n2
            elif a=='/':
                print("please write the answer in integer ")
                if n1<n2:
                    n1,n2=n2,n1
                result=n1//n2
            print(n1,a,n2,'=')
            ans=int(input())
            if ans==result:
                print("!"*25,"CORRECT ANSWER","!"*25)
                correct+=1
                score+=4
            else:
                print("!"*25,"WRONG ANSWER","!"*25)
                print("THE CORRECT ANSWER IS",result)
                score-=1
                wrong+=1
        print("_"*75)
        end=time.time()
        a=round(end-start)
        b=str(a)+"sec"
        print("YOUR SCORE: ",score)
        print("TIME TAKEN: ",b)
        print("!"*25,"THANKS FOR PLAYING","!"*25)
        qry="insert into maths values(%s,%s,%s,%s,%s)"
        l=[nm,score,correct,wrong,b]
        mycursor.execute(qry,l)
        mycon.commit()
def GK_QUIZ():
    score=0
    correct=0
    wrong=0
    start=time.time()
    time.sleep(1)
    print("!"*30,"WELCOME TO GENERAL KNOWLEDGE QUIZ","!"*30)
    a=input("ARE YOU READY TO PLAY????(Y/N): ")
    if a.upper()=="Y":
        print("!"*25," LET'S START THE QUIZ","!"*25)
        print('''TOTAL QUESTIONS:10
RULES:-
FOR EVERY CORRECT ANSWER : +4
FOR EVERY WRONG ANSWER : -1
MAXIMUM MARKS: 40''')
        print("PLEASE ENTER YOUR NAME: ")
        nm=input()
        print("_"*75)
        ques="Who was the first Indian woman in space? "
        a="Sunita Williams"
        b="Kaplana Chawla"
        c="Koneru Humpy"
        d="None of these"
        print("Q1) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Who was the first Man to climb mount everst without oxygen?"
        a="Junko Tabei"
        b="Reinhold Messner"
        c="Peter Habeler"
        d="Phu Dorji"
        print("Q2) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="d"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Which country is hosting olympics 2021?"
        a="USA"
        b="China"
        c="Japan"
        d="Germany"
        print("Q3) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="What is the capital of australia? "
        a="Sydney"
        b="Canberra"
        c="Melbourne"
        d="Brisbane"
        print("Q4) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Who is the second president of india?"
        a="Dr. Sarvepalli Radhakrishnan"
        b="Dr. Rajendra Prasad"
        c="Pratibha Patil"
        d="Dr. A.P.J Abdul Kalam"
        print("Q5) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="a"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="First india to win noble prize?"
        a="C.V.Raman"
        b="Mother Teresa"
        c="Rabindranath Tagore"
        d="Amartya Sen"
        print("Q6) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="which is the largest city in the world?"
        a="Tokyo-Yokohama"
        b="Jakarta"
        c="Delhi,DL-UP-HR"
        d="Manila"
        print("Q7) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="a"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Which is the tallest statue in the world?"
        a="Spring Temple Buddha"
        b="Statue of Unity"
        c="Ushiku Daibutsu"
        d="Statue of Liberty"
        print("Q8) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Which is the least populated country in the world?"
        a="Nauru"
        b="San Marino"
        c="Palau"
        d="Vatican City"
        print("Q9) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="d"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="Who founded Facebook?"
        a="Kevin Systrom"
        b="Bill Gates"
        c="Mark Zuckerberg"
        d="Elon Musk"
        print("Q10) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
    end=time.time()
    a=round(end-start)
    b=str(a)+"sec"
    print("YOUR SCORE IS ",score)
    print("TIME TAKEN: ",b)
    print("*"*30,"THANKS FOR PLAYING","*"*30)
    qry="insert into GK values(%s,%s,%s,%s,%s)"
    l=[nm,score,correct,wrong,b]
    mycursor.execute(qry,l)
    mycon.commit()
def trick():
    start=time.time()
    time.sleep(1)
    score=0
    correct=0
    wrong=0
    print("!"*30,"WELCOME TO TRICK QUESTION'S QUIZ","!"*30)
    a=input("ARE YOU READY TO PLAY????(Y/N): ")
    if a.upper()=="Y":
        print("!"*25," LET'S START THE QUIZ","!"*25)
        print('''TOTAL QUESTIONS:10
RULES:-
FOR EVERY CORRECT ANSWER : +4
FOR EVERY WRONG ANSWER : -1
MAXIMUM MARKS: 40''')
        print("PLEASE ENTER YOUR NAME: ")
        nm=input()
        print("_"*75)
        ques="which thing is more heavier 1000kg steel or 1000kg cotton?"
        a="Steel"
        b="Cotton"
        c="Both are equal"
        d="Data is not sufficient"
        print("Q1) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="divide 30 by half and add ten?"
        a="12"
        b="25"
        c="50"
        d="70"
        print("Q2) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="d"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques='''A little girl kicks a soccer ball. it goes 10 feet and comes back to her.
how is this possible?'''
        a="The ball is slippery"
        b="The ground must have been slippery"
        c="Gravity"
        d="She can't kick"
        print("Q3) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques='''an electric train is moving north at 100mph and a wind is blowing to the west at 10mph.
which way the smoke blow?'''
        a="South"
        b="East"
        c="There's no smoke"
        d="North"
        print("Q4) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="if it took eight men ten hours to build a wall, how long would it take four men to build? "
        a="20 Hours"
        b="48 Hours"
        c="10 Hours"
        d="None because it's already built"
        print("Q5) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="d"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="some months have 31 days, other have 30 days. how many have 28 days?"
        a="One"
        b="Two"
        c="Every month have 28 days"
        d="Chinese months have 28 days"
        print("Q6) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="What goes up and down, but still remains in the same place?"
        a="A Scale"
        b="Stairs"
        c="A Wheel"
        d="The lift"
        print("Q7) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="what gets wetter & wetter the more it dries?"
        a="Sponge"
        b="A towel"
        c="Bread"
        d="Pasta"
        print("Q8) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="you,re 3rd place right now in the race. what place are you in when you pass the 2nd person?"
        a="1st"
        b="2nd"
        c="3rd"
        d="none of the above"
        print("Q9) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="b"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
        ques="there are 45 apples in your basket. you take three apples out of the basket. how mant apples are left?"
        a="3"
        b="42"
        c="45"
        d="None of these"
        print("Q10) ",ques.upper())
        print("A) ",a)
        print("B) ",b)
        print("C) ",c)
        print("D) ",d)
        ans=input("PLEASE ENTER THE CORRECT OPTION: ")
        result="c"
        if result==ans.lower():
            print("!"*25,"CORRECT ANSWER","!"*25)
            score+=4
            correct+=1
        else:
            print("!"*25,"WRONG ANSWER","!"*25)
            print("THE CORRECT ANSWER IS : OPTION ",result.upper())
            score-=1
            wrong+=1
        print("_"*50)
        print()
    end=time.time()
    a=round(end-start)
    b=str(a)+"sec"
    print("YOUR SCORE IS ",score)
    print("TIME TAKEN: ",b)
    print("*"*30,"THANKS FOR PLAYING","*"*30)
    qry="insert into trick values(%s,%s,%s,%s,%s)"
    l=[nm,score,correct,wrong,b]
    mycursor.execute(qry,l)
    mycon.commit()
import turtle as t

def Benzene():
    t.speed(0)
    t.bgcolor("black")
    t.color("red")
    t.pensize(5)
    for i in range(8):
        t.left(45)
        for i in range(8):
            t.forward(100)
            t.left(45)
    t.hideturtle()

def circle_rangoli():
    t.pencolor('red')
    t.pensize(2)
    t.bgcolor('black')
    t.speed(0)
    
    def drawcircle(radius):
        for i in range(10):
            t.circle(radius)
            radius=radius-4
    def drawdesign():
        for i in range(10):
            drawcircle(150)
            t.right(36)
    drawdesign()
    t.done()
def Colourful_Benzene():
    t.bgcolor("black")
    t.colors=['red','purple','blue','green','orange','yellow']
    t.speed(0)
    for i in range(280):
        b=i%6
        t.pencolor(t.colors[b])
        a=i/88+1
        t.pensize(a)
        t.forward(i)
        t.left(59)
    t.done()

def Toroid():
    t.bgcolor("black")
    t.speed(0)
    x=1
    c=1
    while c<150:
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        t.colormode(255)
        t.pencolor(r,g,b)
        t.circle(100+x)
        t.fd(50+x)
        t.rt(90.911)
        c+=1
        x*=1
    t.exitonclick()
def Star_of_Stars():
    t.bgcolor('black')
    t.penup()
    t.goto(-200,75)
    t.color('yellow') 
    t.pendown()
    t.speed(0)
    def star(turtle,size):
        if size<=10:
            return
        else:
            t.begin_fill()
            for i in range(5):
                t.forward(size)
                star(turtle,size/3)
                t.left(216)
                t.end_fill()
    star(5,360)
    t.done()
def rangoli():
    t.bgcolor("black")
    t.pencolor("red")
    t.speed(0)
    c=0
    d=0
    while True:
        for i in range(4):
            t.forward(80)
            t.right(90)
        t.right(15)
        c+=1
        if c>=390/15:
            t.forward(50)
            c=0
            d+=1
            if d>=12:
                 break
    t.hideturtle()
    t.done()
def Tiranga():
    t.speed(0)
    t.pensize(5)
    t.color('#054187')
    def draw(x , y):
        t.penup()
        t.goto(x,y)
        t.pendown()
    for i in range(24):
        t.forward(80)
        t.backward(80)
        t.left(15)
    draw( 1 , -80)
    t.circle(80, 360)
    t.color('green')
    t.begin_fill()
    t.forward(350)
    t.backward(700)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(700)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.end_fill()
    t.color('orange')
    draw( -350 , 80 )
    t.begin_fill()
    t.right(180)
    t.forward(700)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(700)
    t.left(90)
    t.forward(200)
    t.end_fill()
    t.done()
def steroid():
    t.pencolor("red")
    t.bgcolor("black")
    a=0
    b=0
    t.speed(0)
    while True:
        t.forward(a)
        t.right(b)
        a+=3
        b+=2
        if b==200:
            break
        t.hideturtle()
def olympic_logo():
    def draw_cirle(x,y,c='red'):
        t.pu()
        t.goto(x,y)
        t.pd()
        t.color(c)
        t.circle(30,360)
    t.pensize(10)
    draw_cirle(0,0,'blue')
    draw_cirle(60,0,'black')
    draw_cirle(120,0,'red')
    draw_cirle(90,-30,'green')
    draw_cirle(30,-30,'yellow')
    t.done()


def Quiz():
    print("_"*70)
    print("WHICH TYPE OF QUIZ YOU WOULD LIKE TO PLAY:-")
    a=int(input('''1. MATHEMATICAL CALCULATION QUIZ
2. GENERAL KNOWLEDGE QUIZ
3. TRICK QUESTIONS QUIZ
PLEASE ENTER YOUR CHOICE: '''))
    if a==1:
        maths_quiz()
        print("_"*70)
    elif a==2:
        GK_QUIZ()
        print("_"*70)
    elif a==3:
        trick()
        print("_"*70)
    else:
        print("PLEASE ENTER ANY VALID OPTION")
        Quiz()

def Turtle():
    a=''
    print("_"*70)
    nm=input("PLEASE ENTER YOUR NAME: ")
    print()
    print("!"*30,"HI ",nm," WElCOME TO TURTLE DESIGNS ANIMATIONS","!"*30)
    c=input("ARE YOU READY TO SEE TURTLE DESIGNS????(Y/N): ")
    if c.upper()=="Y":
        print("WHICH TURTLE DESIGN YOU WOULD LIKE TO SEE:-")
        opt=int(input('''1. BENZENE
2. OVAL RANGOLI
3. TORNADO OF BENZENE
4. TOROID
5. STAR OF STARS
6. RANGOLI
7. TIRANGA
8. STEROID
9. OLYMPIC LOGO
PLEASE ENTER YOUR CHOICE: '''))
        if opt==1:
            a="BENZENE"
            Benzene()
        elif opt==2:
            a="OVAL RANGOLI"
            circle_rangoli()
        elif opt==3:
            a="TORNADO OF BENZENE"
            Colourful_Benzene()
        elif opt==4:
            a="TOROID"
            Toroid()
        elif opt==5:
            a="STAR OF STARS"
            Star_of_Stars()
        elif opt==6:
            a="RANGOLI"
            rangoli()
        elif opt==7:
            a="TIRANGA"
            Tiranga()
        elif opt==8:
            a="STEROID"
            steroid()
        elif opt==9:
            a="OLYMPIC LOGO"
            olympic_logo()
        else:
            print("PLEASE ENTER ANY VALID OPTION")
            Turtle()
        
    qry="insert into turtle values(%s,%s)"
    l=[nm,a]
    mycursor.execute(qry,l)
    mycon.commit()
    print("_"*70)
print()
print("!"*30," WELCOME TO FUNLAND ","!"*30)
while True:
    opt=int(input('''WHAT WOULD YOU LIKE TO DO:-
1. TEST YOUR KNOWLEDGE BY GIVING QUIZ
2. TO SEE CREATIVE DESIGNS ON PYTHON TURTLE GRAPHICS
3. EXIT 
PLEASE ENTER YOUR CHOICE: '''))
    if opt==1:
        Quiz()
    elif opt==2:
        Turtle()
    elif opt==3:
        break
    else:
        print("PLEASE ENTER ANY VALID OPTION")
    
