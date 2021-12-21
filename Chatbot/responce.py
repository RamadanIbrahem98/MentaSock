import re

class Responce:
  def __init__(self):
    self.quetions = ["(1)  I found it hard to wind down ? " ,

            ]
    self.quetion_num = 0
    self.result = 0 

  def get_response(self , user_input ):
    if (self.quetion_num == 0):
        self.quetion_num = 1
        return self.quetions[0]
    if (len(self.quetions) == self.quetion_num  ):
        self.result  = int (user_input) + self.result 
        return "your result is ready " + str (self.result )



    # sends the splitted array to a function that checks all the words and see if we have a designated response for it
    # response = check_all_messages(client_message)
    if (user_input == "0" or user_input == "1" or user_input == "2" or user_input == "3")  :
        next_question = self.quetions[self.quetion_num -1 ]
        self.quetion_num = self.quetion_num + 1
        self.result = self.result + int (user_input)
        print(self.result)
        return (next_question)
    
    return "i couldnt recognise your message please replay with 0 or 1 or 2 or 3 "

