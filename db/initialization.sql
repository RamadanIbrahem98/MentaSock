DROP TABLE IF EXISTS questionnaire;
DROP TABLE IF EXISTS answer;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS question_answer;
DROP TABLE IF EXISTS questionnaire_question;
DROP TABLE IF EXISTS result;
DROP TABLE IF EXISTS questionnaire_result;
CREATE TABLE IF NOT EXISTS questionnaire (for VARCHAR(50) PRIMARY KEY);
CREATE TABLE IF NOT EXISTS answer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  body INTEGER NOT NULL UNIQUE,
  weight INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS question (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  body TEXT
);
CREATE TABLE IF NOT EXISTS question_answer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question_id INTEGER NOT NULL,
  answer_id INTEGER NOT NULL,
  FOREIGN KEY(question_id) REFERENCES question(id) ON DELETE CASCADE,
  FOREIGN KEY(answer_id) REFERENCES answer(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS questionnaire_question (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question_id INTEGER NOT NULL,
  questionnaire_for VARCHAR(50) NOT NULL,
  FOREIGN KEY(question_id) REFERENCES question(id) ON DELETE CASCADE,
  FOREIGN KEY(questionnaire_for) REFERENCES questionnaire(for) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS result (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  minimum INTEGER NOT NULL,
  maximum INTEGER NOT NULL,
  body TEXT NOT NULL,
  description TEXT
);
CREATE TABLE IF NOT EXISTS questionnaire_result (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  result_id INTEGER NOT NULL,
  questionnaire_for VARCHAR(50) NOT NULL,
  FOREIGN KEY(result_id) REFERENCES result(id) ON DELETE CASCADE,
  FOREIGN KEY(questionnaire_for) REFERENCES questionnaire(for) ON DELETE CASCADE
);
INSERT INTO questionnaire (for)
VALUES ('Depression');
INSERT INTO question (body)
VALUES ('I found it hard to wind down'),
  ('I was aware of dryness of my mouth'),
  (
    'I couldn’t seem to experience any positive feeling at all'
  ),
  (
    'I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)'
  ),
  (
    'I found it difficult to work up the initiative to do things'
  ),
  ('I tended to over-react to situations'),
  ('I experienced trembling (e.g. in the hands)'),
  (
    'I felt that I was using a lot of nervous energy'
  ),
  (
    'I was worried about situations in which I might panic and make a fool of myself'
  ),
  ('I felt that I had nothing to look forward to'),
  ('I found myself getting agitated'),
  ('I found it difficult to relax'),
  ('I felt down-hearted and blue'),
  (
    'I was intolerant of anything that kept me from getting on with what I was doing'
  ),
  ('I felt I was close to panic'),
  (
    'I was unable to become enthusiastic about anything'
  ),
  ('I felt I wasn’t worth much as a person'),
  ('I felt that I was rather touchy'),
  (
    'I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)'
  ),
  ('I felt scared without any good reason'),
  ('I felt that life was meaningless');
INSERT INTO answer (body, weight)
VALUES (0, 0),
  (1, 2),
  (2, 4),
  (3, 6);
INSERT INTO questionnaire_question (question_id, questionnaire_for)
VALUES (1, 'Depression'),
  (2, 'Depression'),
  (3, 'Depression'),
  (4, 'Depression'),
  (5, 'Depression'),
  (6, 'Depression'),
  (7, 'Depression'),
  (8, 'Depression'),
  (9, 'Depression'),
  (10, 'Depression'),
  (11, 'Depression'),
  (12, 'Depression'),
  (13, 'Depression'),
  (14, 'Depression'),
  (15, 'Depression'),
  (16, 'Depression'),
  (17, 'Depression'),
  (18, 'Depression'),
  (19, 'Depression'),
  (20, 'Depression'),
  (21, 'Depression');
INSERT INTO question_answer (question_id, answer_id)
VALUES (1, 1),
  (1, 2),
  (1, 3),
  (1, 4),
  (2, 1),
  (2, 2),
  (2, 3),
  (2, 4),
  (3, 1),
  (3, 2),
  (3, 3),
  (3, 4),
  (4, 1),
  (4, 2),
  (4, 3),
  (4, 4),
  (5, 1),
  (5, 2),
  (5, 3),
  (5, 4),
  (6, 1),
  (6, 2),
  (6, 3),
  (6, 4),
  (7, 1),
  (7, 2),
  (7, 3),
  (7, 4),
  (8, 1),
  (8, 2),
  (8, 3),
  (8, 4),
  (9, 1),
  (9, 2),
  (9, 3),
  (9, 4),
  (10, 1),
  (10, 2),
  (10, 3),
  (10, 4),
  (11, 1),
  (11, 2),
  (11, 3),
  (11, 4),
  (12, 1),
  (12, 2),
  (12, 3),
  (12, 4),
  (13, 1),
  (13, 2),
  (13, 3),
  (13, 4),
  (14, 1),
  (14, 2),
  (14, 3),
  (14, 4),
  (15, 1),
  (15, 2),
  (15, 3),
  (15, 4),
  (16, 1),
  (16, 2),
  (16, 3),
  (16, 4),
  (17, 1),
  (17, 2),
  (17, 3),
  (17, 4),
  (18, 1),
  (18, 2),
  (18, 3),
  (18, 4),
  (19, 1),
  (19, 2),
  (19, 3),
  (19, 4),
  (20, 1),
  (20, 2),
  (20, 3),
  (20, 4),
  (21, 1),
  (21, 2),
  (21, 3),
  (21, 4);
INSERT INTO result (minimum, maximum, body, description)
VALUES (
    0,
    9,
    'No Depression',
    'There is no sign of depression'
  ),
  (
    10,
    13,
    'Mild Depression',
    'You are experiencing a mild form of depression'
  ),
  (
    14,
    20,
    'Moderate Depression',
    'You are experiencing a moderate form of depression'
  ),
  (
    21,
    27,
    'Severe Depression',
    'You are experiencing a severe form of depression'
  );
INSERT INTO questionnaire_result (result_id, questionnaire_for)
VALUES (1, 'Depression'),
  (2, 'Depression'),
  (3, 'Depression'),
  (4, 'Depression');
