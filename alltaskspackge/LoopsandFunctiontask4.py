import logging
import os
import datetime
import smtplib
import time
import socket
#import winapps

logging.basicConfig(filename="Loopsandfuntaskfile4", level=logging.INFO)

logging.info("please find the  logging file to find the results more ")

class Loops_Functions:
    def startpattern1(self,i1):
        logging.info("q1 : Try to print this by using while loop ")
        self.i1=i1
        try:
            n = 1
            while n <= i1:
                logging.info('* ' * n)
                print('* ' * n)
                n = n + 1

        except Exception as e:
            logging.exception(e)

    def starpattern2(self,x):
        self.x=x
        logging.info("q2 : try to print below by using while loop : ")
        try:
            while x < 8:
                content = ""
                y = 0
                while y < x:
                    z = 0
                    sum = 0
                    while z < y:
                        sum += 6 - z
                        z += 1
                    if (x + 64 + sum) <= (64 + 26):
                        content += " " + chr(x + 64 + sum)
                    y += 1
                logging.info(content)
                print(content)
                x += 1
        except Exception as e:
            logging.exception(e)

    def divisble3(self,i):
        self.i=i
        logging.info("q3 : Try to print all the number divisible by 3 in between a range of 40 - 400")
        try:
            while i <= 400:
                if i % 3 == 0:
                    logging.info(i)
                    print(i)
                i = i + 1

        except Exception as e:
            logging.exception(e)

    def vowel(self,s):
        self.s=s
        logging.info("q4 : Try to filter out all the vowels form below text by using while loop : ")
        try:

            i = 0
            v = 'aeiou'
            s = s.lower()
            while i < len(s):
                if s[i] in v:
                    logging.info(s[i])
                    print(s[i])
                i = i + 1
        except Exception as e:
            logging.exception(e)

    def allevenum(self):
        logging.info("q5 : Try to generate all the even number between 1- 1000")
        i = 1
        try:
            while i <= 1000:
                if i % 2 == 0:
                    logging.info(i)
                    print(i)
                i = i + 1
        except Exception as e:
            logging.exception(e)


    def timeofsystem(self):
        logging.info("q7 : write a code to get a time of your system ")
        logging.info(datetime.datetime.now().time())
        print(datetime.datetime.now().time())

    def dateofsysytem(self):
        logging.info(" q8 : Write a code to fetch date form your system")
        logging.info(datetime.date.today())
        print(datetime.date.today())


    def mailtourfriend(self):
        logging.info(" q9 : Write a code to send a mail to your friend")
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login('anilkumarkn298@gmail@gmail.com', "Anil298@a")

            server.sendmail('anilkumarkn298@gmail@gmail.com', 'knanilkumar274@gmail.com', 'TEST EMAIL from Python')

        except:
            logging.info("mail not able to sent due to server issue ")
            print("mail not able to sent due to server issue")


    def triggralarm(self):
        logging.info("q10 : write a code to trigger alarm for you at scheduled time ")
        try:
            import playsound
            alarm_time = '10:22'
            if time.asctime()[11:-8] == alarm_time:
                absolute_path = os.path.abspath("texttovoice.mp3")
                logging.info(absolute_path)
                playsound.playsound(absolute_path)
        except:
            logging.info("not able play alaram due invalid path no module present")


    def ipaddresspic(self):
        logging.info("q11 : write a code to check ip address of your system")
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        logging.info("your ip address is " + str(ip))
        logging.info("your computer name is " + str(host))

    def oscheckinsystem(self):
        try:
            import winapps
            logging.info(list(winapps.list_installed()))
        except:
            logging.info("winapps package not istandle kindly install then execute")

    def txt_to_voice(self,str1):
        self.str1=str1
        logging.info("q13 : Write a code to convert any text in to voice ")
        try:
            import gtts
            from playsound import playsound
            tts = gtts.gTTS(str1)
            tts.save("Hello.mp3")
            playsound("Hello.mp3")
        except:
            logging.info("there is no playsound package installed plz insatll first")

    def lenghtofstring(self,s):
        self.s=s
        logging.info("q14 : you have to write a fun which will take string and return a len of it without using a inbuilt fun len")
        logging.info(len(s))

    def print_prim(self,l):
        logging.info( "q15 :write a fun which will be able to print an index of all premitive element which you will pass ")
        self.l=l
        try:
            for i in range(len(l)):
                logging.info(i)
        except Exception as e:
            logging.exception(e)

    def dic_to_list(self,d):
        logging.info("q16 : Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work . ")
        self.d=d
        l = []
        try:
            for i in d.values():
                if type(i) != dict:
                    l.append(i)
                if type(i) == dict:
                    for j in i.values():
                        l.append(j)
            logging.info(l)
        except Exception as e:
            logging.exception(e)

    def read_img(self):
        logging.info("q19 : write a function whihc will be able to read a image file and show it to you .")
        try:
            import cv2
            a = cv2.imread('D:/abc.png')
            cv2.imshow("myimg", a)
            cv2.waitKey(5000)
            cv2.destroyWindow('myimg')
        except:
            logging.info("there is some package not installed please install to convert image")


#This is used to create a object of class and to call functions
s =  """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc"""
functionsobj=Loops_Functions()
functionsobj.startpattern1(9)

functionsobj.starpattern2(0)
functionsobj.divisble3(40)

functionsobj.vowel(s)
functionsobj.allevenum()
functionsobj.timeofsystem()
functionsobj.dateofsysytem()
functionsobj.mailtourfriend()
functionsobj.triggralarm()

functionsobj.ipaddresspic()
functionsobj.oscheckinsystem()
functionsobj.txt_to_voice("anilkumar" )
functionsobj.lenghtofstring("sudh")

functionsobj. print_prim([4, 5, 6, 7, 7, "sdfs", [3, 4, 5, 6]])
d = {'k1' :"value" , "k2" : "values " ,"k3" : { "k12" : "sudh" , "k13"  : "gafasd"}}
functionsobj.dic_to_list(d)

functionsobj.read_img()

