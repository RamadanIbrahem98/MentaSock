-- GET All Questionnaires at the beginning of connection
SELECT q.for
FROM questionnaire q
LIMIT 10;
-- GET All questions with their answers related to a questionnaire
SELECT q.body,
  a.body,
  a.weight
FROM questionnaire_question
  JOIN question q on questionnaire_question.question_id = q.id
  JOIN questionnaire q2 on questionnaire_question.questionnaire_for = q2.for
  JOIN question_answer qa on q.id = qa.question_id
  JOIN answer a on qa.answer_id = a.id;
-- GET All Results Related to a questionnaire
SELECT res.minimum,
  res.maximum,
  res.body,
  res.description
FROM questionnaire_result r
  JOIN result res on r.result_id = res.id
  JOIN questionnaire q on r.questionnaire_for = q.for;
