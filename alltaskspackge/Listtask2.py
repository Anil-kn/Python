import logging
logging.basicConfig(filename="listsetfile1", level=logging.INFO)
logging.info("this is the taks2 which is related to lists please refer the logging file to observe the results")

class Listtask2:

    def reverselist(self,list1):
        logging.info("1 . Try to reverse a list")
        self.list1=list1
        logging.info(list1)
        try:
            if len(list1)==0:
                logging.info("please enter the valid list it is empty")
            else:
                reversealist=list1[::-1]
                logging.info("this is the reverse list result:- "+str(reversealist))
                return reversealist

        except Exception as e:
            logging.exception(e)



    def accesslist(self,list1):
        logging.info("2. try to access 234 out of this list")
        self.list1=list1
        logging.info(list1)
        try:
            if len(list1)==0:
                logging.info("please enter the valid list it is empty")
            else:
                accessalist=list1[7][0]
                logging.info("this is the accessing a  list result:- "+str(accessalist))
                return accessalist

        except Exception as e:
            logging.exception(e)



    def accesslistnum(self, list1):
        logging.info("3 . try to access 456")
        self.list1 = list1
        logging.info(list1)
        try:
            if len(list1) == 0:
                logging.info("please enter the valid list it is empty")
            else:
                accessalistnum = list1[5][1]
                logging.info("this is the accessing a  listnumber result:- " + str(accessalistnum))
                return accessalistnum

        except Exception as e:
            logging.exception(e)



    def extractlist(self, list1):
        logging.info("4 . Try to extract only a list collection form list l")
        self.list1 = list1
        logging.info(list1)
        try:
            if len(list1) == 0:
                logging.info("please enter the valid list it is empty")
            else:
                extractalistcl = list1[5:7]
                logging.info("this is the accessing a  extractlist from collection result:- " + str(extractalistcl))
                return extractalistcl

        except Exception as e:
            logging.exception(e)




    def extractkey(self, list1):
        """
        It will throughs a list of objects
        :type list1: object
        """
        logging.info("4 . Try to extract only a list collection form list l")
        self.list1 = list1
        logging.info(list1)
        try:
            if len(list1) == 0:
                logging.info("please enter the valid list it is empty")
            else:
                extractkey = list1[8]['key1']
                logging.info("this is the accessing a  extracta key sudh from collection result:- " + str(extractkey))
                return extractkey

        except Exception as e:
            logging.exception(e)




    def extractallkeys(self, list1):
        """
        It will throughs a list of objects
        :type list1: object
        """
        logging.info("6 . Try to list all the key in dict element avaible in list")
        self.list1 = list1
        logging.info(list1)
        try:
            if len(list1) == 0:
                logging.info("please enter the valid list it is empty")
            else:
                extractallkey = list(list1[8].keys())
                logging.info("this is the accessing a  extracta key sudh from collection result:- " + str(extractallkey))
                return extractallkey

        except Exception as e:
            logging.exception(e)



    def extractallvalues(self, list1):
        """
        It will throughs a list of objects
        :type list1: object
        """
        logging.info("6 . Try to list all the key in dict element avaible in list")
        self.list1 = list1
        logging.info(list1)
        try:
            if len(list1) == 0:
                logging.info("please enter the valid list it is empty")
            else:
                extractallvalues = list(list1[8].values())
                logging.info("this is the accessing a  extracta values are  from collection result:- " + str(extractallvalues))
                return extractallvalues

        except Exception as e:
            logging.exception(e)





#This include creation of object of class and claiing the parameters inside  actions

l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]
listobj=Listtask2()
reverlist=listobj.reverselist(l)
print(reverlist)

accesslist=listobj.accesslist(l)
print(accesslist)

accesslistnum=listobj.accesslistnum(l)
print(accesslistnum)


extractalistcollectn=listobj.extractlist(l)
print(extractalistcollectn)

extractkeysudh=listobj.extractkey(l)
print(extractkeysudh)

extractallkeys1=listobj.extractallkeys(l)
print(extractallkeys1)

extractallvalues1=listobj.extractallvalues(l)
print(l)

