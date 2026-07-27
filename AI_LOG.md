AI Collaboration Log

Tools Used

- ChatGPT

Prompt Examples

Prompt 1: Project Architecture

What I asked:
Help me design an expense tracker project using the AIDE workflow. What files should I create and what should each file handle?

What worked:
The response helped me break the project into smaller features instead of building everything at once.

What I changed:
I separated my project into multiple files including main.py, expenses.py, storage.py, and tests.py.



Prompt 2: Debugging Import Error

What I asked:
Help me fix an ImportError in my Python project.

What worked:
The AI helped identify that I accidentally imported the expenses file into itself.

What I changed:
I separated the code correctly between main.py and expenses.py.

Bugs Found in AI Code

1. I accidentally placed main.py code inside expenses.py, which caused an ImportError. I fixed it by moving the code into the correct files.

2. The program originally accepted invalid inputs like negative amounts. I added validation to prevent incorrect values.

Key Learnings

- Breaking projects into smaller features makes debugging easier.
- AI works best when given specific problems and error messages.
- Generated code still needs to be tested and verified.
- Git commits help track progress and improvements.