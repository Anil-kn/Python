import logging

logging.basicConfig(filename="listtupledictfile1", level=logging.INFO)
logging.info("this will give information about code output")


class Listtupledict:
    logging.info("")

    def printpattern1(self, num):
        self.num = num
        logging.info(" q1 : print ineuron in trial")
        logging.info("the number of input to print pattern is:- " + str(num))
        try:
            for i in range(num):
                logging.info("ineuron " * (i + 1))
                print("ineuron " * (i + 1))
        except Exception as e:
            logging.exception(e)

    def printpattern2(self, num):
        self.num = num
        logging.info(" q2 : print ineuron in diamond pattern2")
        try:
            for i in range(num):
                if i <= 3:
                    n = i
                else:
                    n = 6 - i
                logging.info(("ineuron " * n).center(30, ' '))
                print(("ineuron " * n).center(30, ' '))
        except Exception as e:
            logging.exception(e)

    def extractlistofentity(self, list1):
        self.list1 = list1
        logging.info("q3 : Try to extract all the list entity ")
        logging.info(list1)
        try:
            for i in list1:
                if type(i) == list:
                    logging.info("extracted list of data from list list1:- " + str(i))
                    print(i)
        except Exception as e:
            logging.exception(e)

    def extractonlydict(self, list1):
        self.list1 = list1
        logging.info(" q4 : Try to extract all the dict enteties")
        try:
            for i in list1:
                if type(i) == dict:
                    logging.info("the only dictionary values are:- " + str(i))
                    print("only dictionaries:-"+str(i))
        except Exception as e:
            logging.exception(e)

    def extractonlytuple(self,list1):
        self.list1=list1
        logging.info("# q5 : Try to extract all the tuples entities")
        try:
            for i in list1:
                if type(i) == tuple:
                    logging.info("extract only tuples fromlist l" + str(i))
                    print("only tuples:-  "+str(i))
        except Exception as e:
            logging.exception(e)

    def allnumericalvalues(self,list1):
        self.list1=list1
        logging.info("q6 : Try to extract all the numerical data it may b a part of dict key and values")
        logging.info(list1)
        l1 = []
        try:
            for i in list1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)

            logging.info(l1)
            print("all numerical value data"+str(l1))
            logging.info("Q7.the sum of all numeric data " + str(sum(l1)))
            print("the sum of all numerical data is:- "+str(sum(l1)))

        except Exception as e:
            logging.exception(e)

    def alloddvalues(self,list2):
        self.list2=list2
        logging.info("q8 : Try to filter out all the odd values out all numeric data which is a part of a list")
        try:
            for i in list2:
                if i % 2 == 0:
                    pass
                else:
                    logging.info("Allodd values in a list l1:- " + str(i))
                    print("all the odd values:- "+str(i))

        except Exception as e:
            logging.exception(e)

    def extractineuron(self,list1):
        self.list1=list1
        logging.info("""q9 : Try to extract "ineruon" out of this data""")
        l2 = []
        try:
            for i in list1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l2.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l2.append(g)

            logging.info("the ineuron number of times:-" + str(l2))
            print(l2)
        except Exception as e:
            logging.exception(e)

    def occurenceofdata(self,list2):
        self.list2
        logging.info("q10 : Try to find out a number of occurances of all the data")
        logging.info(list2)
        try:
            for i in set(list2):
                logging.info(str(i) + ":" + str(list2.count(i)))
                print(str(i)+":"+str(list2.count(i)))

        except Exception as e:
            logging.exception(e)

    def numberofkeys(self,list1):
        self.list1=list1
        logging.info("q11 : Try to find out number of keys in dict element")
        logging.info(list1)
        try:
            for i in list1:
                if type(i) == dict:
                    logging.info("the number of key in a list:- " + str(len(i)))
                    print(str(len(i)))

        except Exception as e:
            logging.exception(e)

    def allstringdata(self,list1):
        self.list1=list1
        logging.info("q12 : Try to filter out all the string data"+str(list1))
        try:
            for i in list1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            logging.info("All the strings in a list" + str(j))
                            print(str(j))

        except Exception as e:
            logging.exception(e)

    def allalphanum(self,list3):
        self.list3=list3
        logging.info("q13 : Try to Find  out alphanum in data")
        try:
            for i in list3:
                if type(i) == str:
                    if i.isalnum():
                        logging.info("All alphanum data in a extracted list:- " + str(i))
                        print("extracted alphanum:- "+str(i))
        except Exception as e:
            logging.exception(e)

    def individualmulcollection(self,list1):
        self.list1=list1
        logging.info(
            "q14 : Try to find out multiplication of all numeric value in the individual collection inside dataset")
        logging.info(list1)
        try:
            for i in list1:
                m = 1
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    logging.info(str(type(i)) + str(m))
                if type(i) == dict:
                    for k in i.items():
                        for n in k:
                            if type(n) == int:
                                m = m * n
                    logging.info(str(type(i)) + str(m))
                    print(str(type(i))+str(m))
        except Exception as e:
            logging.exception(e)


# This is the object creation and passing parameter
pattern1 = Listtupledict()
list1 = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
         {'k1': "sudh", "k2": "ineuron", "k3":
             "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]
list2=[1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8]
list3=[1,2,3,4,2, 3,4,5,6,3,4,5,6,7,45,4,5,23,'k1','sudh','k2','ineuron','k3','kumar', 3,6,7,8,'ineuron', 'data science ']


pattern1.printpattern1(5)
print(pattern1)

pattern1.printpattern2(6)
print(pattern1)

pattern1.extractlistofentity(list1)

pattern1.extractonlydict(list1)

pattern1.extractonlytuple(list1)

pattern1.allnumericalvalues(list1)
pattern1.allstringdata(list1)

pattern1.alloddvalues(list2)
pattern1.extractineuron(list1)
pattern1.occurenceofdata(list2)
pattern1.numberofkeys(list1)
pattern1.allstringdata(list1)
pattern1.allalphanum(list3)
pattern1.individualmulcollection(list1)