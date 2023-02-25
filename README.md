# Bot LinkedIn
To facilitate the search for job openings in the developer area, a Python code was developed with the presence of the Selenium library to automate this task.
# How it works
## First Step
When running the program, it is automatically redirected to the LinkedIn URL. Initially, after entering the login and password information into the code, it will use this information to access the user's account automatically.
## Second Step
After login, it will scrape job by job present in the forwarded URL.
## Third step
It will check if the job in question has a number of applicants below 100.
## Fourth step
If the above condition is met, it will save that job and move on to the next one.
## Fifth (last) step
It will analyze the number of jobs saved, if this is equal to 15 jobs, the program will be finalized.
