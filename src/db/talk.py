from . import Database
from typing import List, Dict, Tuple

db_handler = Database.DB()    # Creating an instance of the database handler class


class Questionnaires:
  '''
      Class for Retrieving Questionnaires along with the answers and weights of these answers
      and finally returns the result of the overall calculation

      ...

      Attributes
      ----------
      questionnaire : str
          the name of the desired questionnaire
      
      questions : Dict[str, List[Tuple[int, int]]]
          dictionary of questions and their (answer, weight) list of tuples
      
      result : Tuple(str, str)
          tuple containning the (overall, description) of the result

      Methods
      -------
      get_all_questionnaires() -> List[str]:
        returns a list of all questionnaires from the database.
      
      get_all_questions(questionnaire: str) -> Dict[str, List[Tuple[int, int]]]:
        returns all questions with their respective (answer, weight) tuple list

      get_the_result(questionnaire: str, score: int) -> Tuple[str, str]:
        returns the (overall, description) of the result in a tuple
    '''

  def __init__(self):
    self.questionnaires = None  # All Questionnairs in the Database
    self.questions = None       # All Questions of a sinle questionnaire, along with their answers and weight of each answer.
    self.result = None          # Result of returned after finishing the questionnaire

  def get_all_questionnaires(self: 'Questionnaires') -> List[str]:
    '''
      Responsible for retrieving all questionnaires from the database

      returns:
      ------
        a list of strings of all available questionnaires in the database
    '''


    # This is query string to be executed using the Database instance
    get_all_questuinnaires = '''
      SELECT for from questionnaire LIMIT 10;
    '''

    # Executing the query to get the list of all questionnaires
    results = db_handler.execute(get_all_questuinnaires)

    self.questionnaires = []
    
    # appending the list of questionnaires to the questionnaires attribute
    for result in results:
      self.questionnaires.append(result[0][0])
    return self.questionnaires

  def get_all_questions(self: 'Questionnaires', questionnaire: str) -> Dict[str, List[Tuple[int, int]]]:
    '''
      Responsible for retrieving all questions from the database related to a single questionnaire

      arguments:
      ----------
        questionnaire: str
          the name of the questionnaire to fetch its questions
      
      returns:
      --------
        a dictionary containing questions along with their (answer, weight) tuples

      example:
      --------
        > output = get_all_questions('Depression') \n
        > output \n
        {'Question 01': [(0, 0), (1, 2)], ...}
    '''

    get_all_questions = '''
      SELECT q.body,
        a.body,
        a.weight
      FROM questionnaire_question qq
        JOIN question q on qq.question_id = q.id
        JOIN questionnaire q2 on qq.questionnaire_for = q2.for
        JOIN question_answer qa on q.id = qa.question_id
        JOIN answer a on qa.answer_id = a.id
        WHERE q2.for = '{}';
    '''.format(questionnaire)

    results = db_handler.execute(get_all_questions)[0]

    self.questions = {}

    # Appending questions with their answers and their weight to the questions dictionary
    for result in results:
      if result[0] not in self.questions.keys():
        self.questions[result[0]] = []
      self.questions[result[0]].append((result[1], result[2]))
      
    return self.questions

  def get_the_result(self: 'Questionnaires', questionnaire: str, score: int) -> Tuple[str, str]:
    '''
      Responsible for retrieving the result of a questionnaire

      arguments
      ---------
      questionnaire : str
          the name of the questionnaire
      score : int
          the overall score given after answering the questionnaire

      returns
      -------
        a tuple containing the result and description of the result
    '''

    get_the_result = '''
      SELECT res.body,
        res.description
      FROM questionnaire_result r
        JOIN result res on r.result_id = res.id
        JOIN questionnaire q on r.questionnaire_for = q.for
      WHERE q.for = '{}' AND res.minimum <= {} AND res.maximum >= {};
    '''.format(questionnaire, score, score)

    # execute the query responsible for fetching the result
    self.result = db_handler.execute(get_the_result)[0][0]

    return self.result
