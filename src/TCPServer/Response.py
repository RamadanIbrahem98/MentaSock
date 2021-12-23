from db.talk import Questionnaires
from typing import List, Dict


class Response:
  '''
    Class for the handling user input with a server response.

    ...

    attributes
    ----------
    q : Questionnaires
        an instance of the Questionnaires class to READ data from database.
    questionnaires : List[str]
        a list of all available questionnaires in the database.
    chosen_questionnaire : str
        the chosen questionnaire by the user.
    questions : List[List[str, Dict[str, int]]]
        a list that contains every question along with its answers and weight for each answer as dictionary.
    result : bool
        whether the user has reached the end of the questionnaire or not.
    current_question : int
        represents the current question in the list of available questions.
    summed_weights : int
        represents current user score, which is the sum of all weights of chosen answers.

    methods
    -------
    get_response(user_input : str):
      returns the server response to the user input
  '''
  def __init__(self) -> None:
    self.q : 'Questionnaires' = Questionnaires()
    self.questionnaires : List[str] = None
    self.chosen_questionnair : str = None
    self.questions : List[List[str, Dict[str, int]]] = None
    self.result : bool = False
    self.current_question : int = 0
    self.summed_weights : int = 0

  def _get_all_questionnaires(self) -> List[str]:
    '''
      Responsible for retrieving all available questionnaires from the database.

      returns
      -------
      questionnaires : List[str]
          list of all available questionnaires.
    '''

    self.questionnaires = self.q.get_all_questionnaires()
    return self.questionnaires
  
  def _set_questions(self, questionnaire : str) -> None:
    '''
      Responsible for retrieving all questions for a specific questionnaire from the database.

      parameters
      ----------
      questionnaire : str
          the questionnaire to retrieve chosen by the user.
    '''

    self.chosen_questionnair = questionnaire
    questions = self.q.get_all_questions(self.chosen_questionnair)
    self.questions = []
    for index, (question, responses) in enumerate(questions.items()):
      self.questions.append([question, {}])
      for (answer, weight) in responses:
          self.questions[index][1][str(answer)] = weight

  def _get_next_question(self) -> str:
    '''
      Responsible for retrieving the next question from the questions list.

      returns
      -------
      question : str
          the next available question from the questions list. (empty string in case of reaching the end of the list).
    '''
    question = ''
    if (self.current_question < len(self.questions) and not self.result):
      question = str(self.current_question + 1) + ' - ' + self.questions[self.current_question][0]
    return question

  def _set_answer(self, answer : str) -> None:
    '''
      Responsible for adding the weight of a user answer to a question to the summed_weights.

      parameters
      ----------
      answer : str
          the user answer to add to the summed_weights.
    '''
    if not self.result:
      self.summed_weights += self.questions[self.current_question][1][answer]
      self.current_question += 1

  def _get_the_result(self) -> str:
    '''
      Responsible for retrieving the result from the database after completing the questionnaire.

      returns
      -------
      result : str
          the result of the questionnaire with some description to that result.
    '''

    result, description = self.q.get_the_result(self.chosen_questionnair, self.summed_weights)
    self.result = True
    return 'Your Results are: ' + result + '\n' + description

  def get_response(self, user_input : str) -> str:
    '''
      Responsible for handling user input with some server response.

      parameters
      ----------
      user_input : str
          the input of the user and it has to be one of the following categories
            - (yes, no) at the beginning of the questionnaire
            - Name of the chosen questionnaire, and it has to match the name provided by the server response.
            - integers 0, 1, 2, or 3 to represet how the statement apply to him
      
      returns
      -------
      response : str
          represents the right way to respond to different messages from the user.
    '''

    # At the beginning of questionnaire we self.questionnaires is None
    # and we ask the user whether they are ready or not.
    if (self.questionnaires is None):
        if user_input.lower() in ['yes', 'no']:
          # if not ready, wait till he is
          if user_input.lower() == 'no':
            return "Whenever you're ready say yes"
          else:
            # once he is ready, retreve all available questionnaires
            questionnaires = self._get_all_questionnaires()
            res = 'Please Enter the exact name of one of the following tests [' + ', \n'.join(questionnaires) + ']'
            return res
        else:
          # if they responded with something other than yes or no at the beginning reply with this
            return "I couldn't recognise your message. please replay with yes or no"
    
    # Now we want to figure out what is the desigred questionnaire to take
    # in order to retrieve all of its questions.
    elif (self.questionnaires is not None and self.questions is None):
        if (user_input.capitalize() in self.questionnaires):
          # Once he chose a valid questionnaire, we retrieve all of its questions.
          self._set_questions(user_input.capitalize())
          # this returns the first question to the user
          return self._get_next_question()
        else:
          # If the user tries to enter a questionnaire name which is not available in the list.
          return "I couldn't recognise your message. please reply with one of the listed tests Names"
    
    # Now after choosing a correct questionnaire, user keeps on providing answers to the list of all available questions.
    elif (user_input in self.questions[self.current_question][1].keys()):
      self._set_answer(user_input)
      # This returns the next question if exists or returns the result once the quetions list is empty.
      return self._get_the_result() if self.current_question >= len(self.questions) else self._get_next_question()
    
    # If the user types a not correct answer to any of the questions, returns this string
    return "I couldn't recognise your message. Please replay with " + ', '.join(self.questions[self.current_question][1].keys())
