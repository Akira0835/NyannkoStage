# NyannkoStage
This project will use to search the stage of a mobile game "にゃんこ大戦争" with given enemy number in that stage.

Currently, the first version of this job is been done. This first version doesn't have a GUI, but it basically works.
run the FindStage.py, and input the number of enemies and the number of ParentStage, it will return the stage match your requirement. 

This function will be useful for the New event "Legend Quest", by just input the parameter, which you can find in the game page, to get the stage you have will meet. 

This project could be expanded in the future. Eg.1. building a GUI and make it an exe or html page, which will be more user friendly. 
Or 2. import all the enemy data, not only the stage data, to find the minimum cost and stage to complete the "monthly mission". 
3. the content.sqlite database is quite redundent with some repeated information, I could make it more slim later. 

Thanks to the https://battlecats-db.com/, where I spider all the data from their website. 

readme.txt will talk more details about each function and the project process. 
