#creat  class for recieving and retreving test questions 
class Response:
  def __init__(self):
    #array of test questions 
    self.quetions = [
      "(1)   I found it hard to wind down ? " ,
      "(2)   I was aware of dryness of my mouth",
      "(3)   I couldn’t seem to experience any positive feeling at all",
      "(4)   I found it difficult to work up the initiative to do things" ,
      "(5)   I experienced breathing difficulty (e.g. excessively rapid breathing,breathlessness in the absence of physical exertion)",
      "(6)   I tended to over-react to situations",
      "(7)   I experienced trembling (e.g. in the hands)",
      "(8)   I felt that I was using a lot of nervous energy",
      "(9)   I was worried about situations in which I might panic and make a fool of myself",
      "(10)  I felt that I had nothing to look forward to",
      "(11)  I found myself getting agitated",
      "(12)  I found it difficult to relax",
      "(13)  I felt down-hearted and blue",
      "(14)  I was intolerant of anything that kept me from getting on with what Iwas doing",
      "(15)  I felt I was close to panic",
      "(16)  I was unable to become enthusiastic about anything",
      "(17)  I felt I wasn’t worth much as a person",
      "(18)  I felt that I was rather touchy ",
      "(19)  I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)",
      "(20)  I felt scared without any good reason",
      "(21)  I felt that life was meaningless",
      
       ]
    #intialize variable for question number and result number
    self.question_num = 0
    self.result = 0 
  #create function that  take user  user input and return a response 
  def get_response(self , user_input ):
    #retrieve the fist question if the client is ready

    if (self.question_num == 0):
        if (user_input == "yes" or user_input == "no"):
            self.question_num = 1
            return self.quetions[0]
        else:
            # return a message if the client enter random message 
            return "i couldnt recognise your message please replay with yes or no "
    #if the client finished all questions retieve a meesage based on the result  
    if (len(self.quetions) == self.question_num  ):
        self.result  = int (user_input) + self.result
        if self.result >= 28 :
          return "your Depression test result Extremely Severe and your score is " + str (self.result )
        elif self.result >= 21 :
          return "your Depression test result Severe and your score is " + str (self.result )
        elif self.result >= 14 :
          return "your Depression test Moderate and your score is " + str (self.result )
        elif self.result >= 10:
          return "your Depression test Mild and your score is " + str (self.result )
        elif self.result >= 0 :
          return "your Depression test Normal and your score is " + str (self.result )
    #return the rest of the questions and restore the result in result vriable 
    if (user_input == "0" or user_input == "1" or user_input == "2" or user_input == "3")  :
        next_question = self.quetions[self.question_num ]
        self.question_num = self.question_num + 1
        #store the result it result variable 
        self.result = self.result + int (user_input)
        print(self.result)
        return (next_question)
    return "i couldnt recognise your message please replay with 0 or 1 or 2 or 3 "

