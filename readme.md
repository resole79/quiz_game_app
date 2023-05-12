## Quiz Game App   

GUI version of [Quiz Game](https://github.com/resole79/quiz_game)

List of random questions and the user must click True/False answer.    

The question are from [Open Trivia Database](https://opentdb.com/) using API   

###### It's a part of the **#100DaysOfCode** challenge by Angela Yu. ######


#### Installation
To get started with the Quiz Game App, follow these steps:

1. **Clone** the repository:

```sh
git clone https://github.com/resole79/quiz_game_app.git
```

2. **Run** the **main.py** file:

```sh
python3 main.py
```     

#### *File Structure*
 - **main.py**: Main program.
 - **question_model.py** : Class "Question"
	 - *Instance*:
		- text,
		- answer
 - **quiz_brain.py** : Class "QuizBrain" 
	 - *Instance*:
		- question_list,
		- question_number,
		- score, 
		- question_current
	- *Method*:
		- "still_has_question"( check if are still question left ), 
		- "check_answer"( check if the answer are correct ),
		- "nex_question" ( show next question )
 - **ui.py** : Class "QuizUi"
 	- *Method*:
		- "get_question"( get_question ), 
		- "check_true"( get 'true_answer_button' click ),
		- "check_false"( get 'false_answer_button' click ),
		- "get_feedback" ( give feedback from your answer ) 
 - **data.py** : File contains the questions using API requests

#### **Usage**


**How program present**

 - Click True / False about a question

<p align="center"><img src="./image/quiz_game_0.png"/><br><i></i></p>

## **Credit**

Author : Emilio Reforgiato (resole79)

##
<p align="right"><a href="https://www.linkedin.com/in/emilio-reforgiato/" target=”_blank” ><img src="./image/in_logo.png" /></a></p>


