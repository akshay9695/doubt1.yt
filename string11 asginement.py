import logging
logging.basicConfig(filename= "strinm.log" , level= logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")


l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]


def reverse_list (l):
    try :
         logging.info("the given list for opraion is %s", l)
         l1 = l
         l2 = l1.reverse()
         logging.info("the outpur of opration is %s", l2)
         return l2

    except Exception as e :
         logging.exception("the erroe we got %s", e)
