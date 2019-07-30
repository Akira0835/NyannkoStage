Jul.27.2019 Created
This function start with getfile.py. 
	Extract the row data from https://battlecats-db.com/stage/index_legendstory.html
	and save into the database content.sqlite

Then apply getstage.py
	This function will clean the row data taken from last function, and get only 
	the stage name and its url suffix.

Next apply stagefilter.py
	This function will filter all the stage, that are not from legendstory.
	After this function, all the stage remain should be legend story

Then Apply getLenStageFile.py
	This function will start to get all the webpage from the legendstory list.
	And save Row text content into the LegendStage Table


>>>Then ready to analyze the stage data. Basically we want the enemy number and stage name.

Apply getEnemyList.py 
	this function will collect information about the enemy number each stage, and it's 	parent stage into the new sqlite table LegStageDetail

>>> Use the data base to search the stage we want.
Use FindStage.py
	This function need input of ParentStage Number and EnemyNumber, 
	then return the stage name that matches requirement.