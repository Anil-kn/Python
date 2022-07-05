import logging

logging.basicConfig(filename="stringstaskfile1", level=logging.INFO)
logging.info("This task is related to strings please go to the corresponding logging file to find the results ")


class Stringstask:

    # Extract string

    def extractdata1(self, extractstr):
        self.extractstr = extractstr
        logging.info("1 . Try to extract data from index one to index 300 with a jump of 3 ")
        logging.info(extractstr)
        try:
            if len(extractstr)==0:
                logging.info("this  is empty string")
            else:
                str = extractstr[0:300:3]
                logging.info("this is the extracted string:- "+str)
                return str
        except Exception as e:
            logging.exception(e)


    def reversestr(self,extractstr):
        self.extractstr=extractstr
        logging.info("2. Try to reverse a string without using reverse function ")
        logging.info(extractstr)
        try:
            if len(extractstr)==0:
                logging.info("this is an empty string please provide valid")
            else:
                rev=extractstr[::-1]
                logging.info("this is the reverse string:-  "+str(rev))
                return rev
        except Exception as e:
            logging.exception(e)

    def splitstr(self, extractstr):
        self.extractstr = extractstr
        logging.info("3. Try to split a string after conversion of entire string in uppercase ")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                spltupper=extractstr.upper()
                spltstr=spltupper.split()
                logging.info("this is the split string:-  " + str(spltstr))
                return spltstr
        except Exception as e:
            logging.exception(e)


    def stringlower(self, extractstr):
        self.extractstr = extractstr
        logging.info("4. try to convert the whole string into lower case ")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                strlower=extractstr.lower()
                logging.info("this is the lowercase string:-  " + str(strlower))
                return strlower
        except Exception as e:
            logging.exception(e)

    def stringcapitalize(self, extractstr):
        self.extractstr = extractstr
        logging.info("5 . Try to capitalize the whole string ")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                strcapitalize = extractstr.capitalize()
                logging.info("this is the string capitalize string:-  " + str(strcapitalize))
                return strcapitalize
        except Exception as e:
            logging.exception(e)

    logging.info("6 . Write a diference between isalnum() and isalpha() ")
    def diffisalphandnum(self, extractstr):
        self.extractstr = extractstr
        logging.info("6 . Write a diference between isalnum() and isalpha() ")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                strisalpha = extractstr.isalpha()
                stralphanum= extractstr.isalnum()
                logging.info("this is the string isalpha string:-  " + str(strisalpha))
                logging.info("this is the string isalpha string:-  " + str(stralphanum))
                return strisalpha
        except Exception as e:
            logging.exception(e)

    def strexpand(self, extractstr):
        self.extractstr = extractstr
        logging.info("7. Try to give an example of expand tab")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                stringexpand = extractstr.expandtabs()
                logging.info("this is the string expand  string:-  " + str(stringexpand))
                return stringexpand
        except Exception as e:
            logging.exception(e)




    def stringstrp(self, extractstr):
        self.extractstr = extractstr
        logging.info("8 . Give an example of strip , lstrip and rstrip")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                stringrstrip = extractstr.rstrip()
                stringlstrip=extractstr.lstrip()
                stringstrip=extractstr.strip()
                logging.info("this is the string of rstrip:-  " + str(stringrstrip))
                logging.info("this is the string of rstrip:-  " + str(stringlstrip))
                logging.info("this is the string of rstrip:-  " + str(stringstrip))
                return stringlstrip,stringstrip,stringrstrip
        except Exception as e:
            logging.exception(e)




    def replacestring(self, extractstr):
        self.extractstr = extractstr
        logging.info("9.  Replace a string charecter by another charector by taking your own example")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                replacestr = extractstr.replace("storage", "container")
                logging.info("this is the string of rstrip:-  " + str(replacestr))
                return replacestr
        except Exception as e:
            logging.exception(e)



    def stringcenter(self, extractstr):
        self.extractstr = extractstr
        logging.info(" 10 . Try  to give a defination of string center function with and exmple")
        logging.info(extractstr)
        try:
            if len(extractstr) == 0:
                logging.info("this is an empty string please provide valid")
            else:
                strcenter = extractstr.center(10,'*')
                logging.info("this is the string of rstrip:-  " + str(strcenter))
                return strcenter
        except Exception as e:
            logging.exception(e)





#calling the function based on object creations methods
#first extract calling
e_string = Stringstask()
out_string=e_string.extractdata1("this is My First Python programming class and i am learNING python string and its function")
print(out_string)

#2nd reverse calling
reversestring=e_string.reversestr("this is My First Python programming class and i am learNING python string and its function")
print(reversestring)

splitstring=e_string.splitstr("this is My First Python programming class and i am learNING python string and its function")
print(splitstring)

stringlower=e_string.stringlower("this is My First Python programming class and i am learNING python string and its function")
print(stringlower)

stringcapitalize=e_string.stringcapitalize("this is My First Python programming class and i am learNING python string and its function")
print(stringcapitalize)

strdiffisalphaandnum=e_string.diffisalphandnum("sudhfsdf12345")
print(strdiffisalphaandnum)

strexpanding=e_string.strexpand("xyzyu\t12345\tabc")
print(strexpanding)

stringstriptask=e_string.stringstrp("               baby           ")
print(stringstriptask)

replacestring=e_string.replacestring("Cold storage")
print(replacestring)

strcenter=e_string.stringcenter("Coder")
print(strcenter)
