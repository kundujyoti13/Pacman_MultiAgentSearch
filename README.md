[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8208588&assignment_repo_type=AssignmentRepo)
# RMIT AI'22 - Project 2 - Multiagent Search

You must read fully and carefully the assignment specification and instructions detailed in this file. You are NOT to modify this file in any way, except if instructed by the teaching staff in writing.

* **Course:** [COSC1127/1125 Artificial Intelligence](http://www1.rmit.edu.au/courses/004123) @ Semester 2, 2022
* **Instructor:** Prof. Sebastian Sardina
* **Deadline:** Sunday August 21st, 2022 @ 11:59pm (end of Week 5)
* **Course Weight:** 7%
* **Assignment type:**: Group of 3 (or 2 in some cases)
* **CLOs covered:** 2, 3, 4 and 5
* **Submission method:** via git tagging (see below for instructions)
* **Files to modify:** `multiAgents.py`

The **aim of this project** is to get you acquainted with search techniques that account for behavior against an adversarial agent. It is also aimed at preparing and "bonding" the team for the upcoming projects!

 <p align="center"> 
    <img src="logo-p2.png" alt="logo project 2">
 </p>

## Table of Contests

- [RMIT AI'22 - Project 2 - Multiagent Search](#rmit-ai22---project-2---multiagent-search)
  - [Table of Contests](#table-of-contests)
  - [Your task](#your-task)
  - [Marking criteria](#marking-criteria)
  - [Submission Instructions](#submission-instructions)
  - [Important information](#important-information)
  - [AI'22 Code of Honour](#ai22-code-of-honour)
  - [Conclusions](#conclusions)
  - [Acknowledgements](#acknowledgements)

## Your task

In this assessment, **your task** is to fully complete [Pacman Project 2 - Multiagent Search](http://ai.berkeley.edu/multiagent.html) from the set of [UC Pacman Projects](http://ai.berkeley.edu/project_overview.html). 

This is a **group/team project**. One member of the team will first create the team in GitHub. The team will have a name and will be given a repository with the project. After that, the remaining members will just select the team when accessing the project via GitHub Classroom.


* You **must build and submit your solution** using the sample code we provide you in this repository, which is different from the original UCB code base. 

* You should **only work and modify** file `multiAgents.py` in doing your solution. Do not change any of the other Python files in this distribution.

* Your code **must run _error-free_ on Python 3.6/3.8**. Staff will not debug/fix any code. Using a different version will risk your program not running with the Pacman infrastructure or autograder and may risk losing (all) marks. 

* You should **never tamper with the Pacman infrastructure**, neither at the source code level (e.g., changing files other than the ones for the task) nor at the run-time level (e.g., changing infrastructure properties or catching all exceptions with bare `except:` code). Check [this](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-PACMAN.md#can-i-change-the-pacman-infrastructure-at-run-time) and [this](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-PACMAN.md#can-i-use-catch-all-exceptions-in-my-code-or-exceptions-from-the-infrastructure) questions in the FAQ on this and ask if in doubt.

* Your code **must not contain any personal information**, like your student number or your name. That info should go in the [TEAM.md](TEAM.md) file, as per instructions below. If you use an IDE that inserts your name, student number, or username, you should disable that.

* Being a group assignment, you must use your **Github project repository and team** to collaborate among the members. The group will have write access to the same repository, and also be members of a GitHub team, where members are expected to engage in discussions and collaboration. Interactions outside the GitHub team will not be considered as evidence of collaboration. Refer to the marking criteria below. 

* You **must follow good SE practice** during you development, individually and as a team; please refer to Marking criteria below.

* You are free to **add additional testing scenarios** under the [`test_cases/`](test_cases/) folder.
  
## Marking criteria

We will follow the marking weights specified in the official project instructions, but other factors will be judged and taken into consideration for the final overall mark.

While the autograder provided is a useful indication of your performance, it is only a feedback tool and _may not represent the ultimate mark_. The **ultimate mark** will be provided to you after marking. We reserve the right to run more tests, inspect your code and repo manually, and arrange for a face-to-face meeting for a discussion and demo of your solution if needed. **We will also run [Codequiry](https://codequiry.com/)** on all submitted solutions; see _Academic Dishonesty_ below.

You must also **follow good SE practices**, including good use of git version control during your development such as:

* _Commit early, commit often:_ single or few commits with all the solution or big chunks of it, is not good practice.
* _Use meaningful commit messages:_ as a comment in your code, the message should clearly summarize what the commit is about. Messages like "fix", "work", "commit", "changes" are poor and do not help us understand what was done.
* _Use atomic commits:_ avoid commits doing many things; let alone one commit solving many questions of the project. Each commit should be about one (little but interesting) thing. 
* _Do not just upload files:_ git for software development should not be used as a storage service. Setup your system to do proper meaningful commits and do not use GitHub's upload button.
* _Commit evenly across the group team members_ (for team project/assignment components). This means there should be meaningful commits from _all_ participating members. 
* [Peer programming](https://en.wikipedia.org/wiki/Pair_programming) is encouraged, but it does _not_ mean that one member always (or mostly always) acts as the "driver" and commits; *all* members should take turns, be the "driver" and commit to the repo. 
  * When peer-programming, make use of the [co-author facility](https://docs.github.com/en/github/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) in GitHub to be accounted in the contributions. See [this post](https://gitbetter.substack.com/p/how-to-add-multiple-authors-to-a) and [this post](https://github.blog/2018-01-29-commit-together-with-co-authors/) as well about co-authors commits. You can conveniently include multiple co-authors to a commit via GitHub Desktop or via VScode (or otherwise by writing special commit messages) as explained in the links given.
* _Use the Issue Tracker:_ use issues to keep track of tasks, enhancements, and bugs for your projects. They are also a great way to collaborate in a team, by assigning issues and discussing on them directly. Check GitHub [Mastering Issues Guide](https://guides.github.com/features/issues/).
* _Follow good workflow:_ use the standard branch-based development workflow, it will make your team much more productive and robust! Check GitHub [Workflow Guide](https://guides.github.com/introduction/flow/). 
* _Communicate in the GitHub Team:_ members of the group are expected to communicate, in an adequate and professional way, in the GitHub team created along the repo. For example, you could use GitHub team discussions, use issues and pull requests to track development status, or create project plans in the Wiki. Video and voice chats outside of GitHub are permissible (and encouraged), but text communication should be through the GitHub team where possible.

**We will inspect the commit history in your remote repo** as well as the **GitHub team** to check for good and proper SE practices, and evidence of meaningful contributions of _all_ members. The results of these checks can affect the overall individual marks significantly, as point deductions may be applied when poor SE practices have been used or no clear evidence of contributions can be found. For example, few commits with a lot of code changes, or poor communication in the corresponding GitHub team may result in deductions, even if the performance of the submission is excellent. An HD submissions requires evidence of high-quality SE practices. Finally, work outside the GitHub project and team will not be considered for assessment. 

**We reserve the right to call for team and/or individual interviews when needed.**

## Submission Instructions

To **submit your assignment** you must complete the following four steps:

1. Complete the [TEAM.md](TEAM.md) file with the team details.
2. Check that your solution runs on Python 3.6/3.8.
3. Check that your source code does not include any personal information, like your student number or name.
4. Tag the commit version in the `main` remote branch that you want to be submit with tag name "`submission`" (case sensitive; excluding quotes) before the assessment deadline.
    * Make sure your submission is merged into the `main` branch of your remote repo, which should contain your latest stable version. Check the GitHub web interface to make sure it has all been pushed successfully.
    * Remember that a _tag_ is a name given to a specific commit in your git history. It is  NOT a branch nor a commit message nor a release. For info on (re)tagging, please read the relevant entries in the [PACMAN FAQ](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-PACMAN.md) in the Pacman FAQ.
5. Fill the [Project 2 Certification Form](https://forms.gle/s7QqMwcNpjBzeT8k6).
   * Every member of the team must certify.
   * You will get an email receipt after submitting the certification; please check it and keep it for your records.
   * Non-certified submissions will not be marked and will attract zero marks.

**IMPORTANT:** Submissions not compatible with the instructions above will attract zero marks and do not warrant a re-submission. Staff will not debug or fix your submission. Read carefully and ask for help (in forum or drop-in lab) if needed.

## Important information

**About this repo:** You must ALWAYS keep your fork **private** and **never share it** with anybody in or outside the course, except your teammates, _even after the course is completed_. You are not allowed to make another repository copy outside the provided GitHub Classroom without the written permission of the teaching staff. Please respect the [authors request](http://ai.berkeley.edu/project_instructions.html):

> **_Please do not distribute or post solutions to any of the projects._**

**Corrections:** From time to time, students or staff find errors (e.g., typos, unclear instructions, etc.) in the assignment specification. In that case, a corrected version of this file will be produced, announced, and distributed for you to commit and push into your repository.  Because of that, you are NOT to modify this file in any way to avoid conflicts.

**Late submissions & extensions:** A penalty of 10% of the maximum mark per day will apply to late assignments up to a maximum of five days, and 100% penalty thereafter (see [this question](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-COURSE.md#can-i-submit-late-what-is-the-penalty) in the course FAQs. Extensions will only be permitted in _exceptional_ circumstances; see [this question](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-COURSE.md#what-is-the-policy-on-special-consideration) in the course FAQs.

**Academic Dishonesty:** This is an advanced course, so we expect full professionalism and ethical conduct.  Plagiarism is a serious offense. Please **don't let us down and risk our trust**. Sophisticated _plagiarism detection_ software via [Codequiry](https://codequiry.com/) will be used in this edition to check submitted code against other submissions in the class as well as resources available on the web. These systems are really smart, so just do not risk it and keep professional and safe. We trust you all to submit your own work only; again, don't let us down. If you do, we will pursue the strongest consequences available to us according to the **University Academic Integrity policy**. In a nutshell, **never look at solution done by others**, either in (e.g., classmate) or outside (e.g., web) the course: they have already done their learning, this is your opportunity! If you refrain from this behavior, you are safe. For more information on this see file [Academic Integrity](ACADEMIC_INTEGRITY.md).

**We are here to help!:** We are here to help you! But we don't know you need help unless you tell us. We expect reasonable effort from your side, but if you get stuck or have doubts, please seek help. We will run a drop-in lab to support these projects, so use that! While you have to be careful to not post spoilers in the forum, you can always ask general questions about the techniques that are required to solve the projects. If in doubt whether a questions is appropriate, post a Private post to the instructors. There is also a dedicated [**PacMan FAQ**](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-PACMAN.md) available to record common questions, check them before asking, your question may already be there!

**Silent Policy:** A silent policy will take effect **48 hours** before this assignment is due. This means that no question about this assignment will be answered, whether it is asked on the newsgroup, by email, or in person.

## AI'22 Code of Honour

We expect every RMIT student taking this course to adhere to the **Code of Honour** under which every learner-student should:

* Submit their own original work.
* Do not share answers with others.
* Report suspected violations.
* Not engage in any other activities that will dishonestly improve their results or dishonestly improve or damage the results of others.

Unethical behaviour is extremely serious and consequences are painful for everyone. We expect enrolled students/learners to take full **ownership** of your work and **respect** the work of teachers and other students.

## Conclusions

This is the end of the assessment specification. We hope you will enjoy executing it and hence learn a lot about techniques for adversarial search. We also hope the project serves as a bonding tool for the team.

Remember the [**PacMan FAQ**](https://github.com/RMIT-COSC1127-1125-AI22/AI22-DOC/blob/main/FAQ-PACMAN.md) is available to answer common questions you might have about this project.

If you still have doubts about the project and/or this specification do not hesitate asking in the [Course EdStem Discussion Forum](https://edstem.org/au/courses/8118) and we will try to address it as quickly as we can!

**I very much hope you enjoy this project and learn from it a lot**. 

**GOOD LUCK & HAPPY MINIMAX!**


## Acknowledgements

We are very grateful to UC Berkeley CS188 for developing and sharing their [UC Pacman Projects](http://ai.berkeley.edu/project_overview.html) with us for teaching and learning purposes.
