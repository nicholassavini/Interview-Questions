# Udacity Full Stack Interview Practice Questions
This repository will hold my answers to the practice interview questions that are part of Udacity's Full Stack Web Development Nanodegree. Text answers will be located in the readme, while code answers will be stored as separate files.

## Questions
Q. **What is the most influential book or blog post you’ve read regarding web development?**

A.

Q. **Tell me about a web application you have built. Why did you choose to build it? What did you learn? What challenges did you face and how did you overcome them?**

A. The first programming project that I considered complete was a web-based Sales Rotation for my current employer. The concept was to replace the existing Excel document that had to be manually created every night, and then printed and distributed to ten employees each day, could be replaced by a web app that would automate the processing, and present everyone with more accurate live data. I took an iterative approach to developing it by first laying out the most functional aspects of the app, and then additional stylistic features later. Midway through its development, I decided to ask the Operations team for some feedback on the basic functionality to ensure that it made sense to everyone. What I presented was a purely functional prototype with no styles added. Unfortunately, while I had a complete understanding of the app since I built it, the Operations department struggled to contextualize it the same way that I did. After quelling what nearly seemed like a riot, I went back to my desk and added some styles to the app to make it look like something closer to completion and went back one more time. The change in response shocked me. Everyone loved it, minus a few constructive criticisms. I took away from this experience that not everyone will see your project through the same lens that you do, and that communication is just as important to the success of a project as the code behind it.

Q. **Write a function in Python that takes a list of strings and returns a single string that is an HTML unordered list of those strings. You should include a brief explanation of your code. Then, what would you have to consider if the original list was provided by user input?**

A. The code for this answer can be found in the `question_2.py` file. The file contains a Python function which accepts a list as an argument. After an initial result string is set with the string variable `list`, the list `l` if iterated through, and each item in the list is added to the `list` string variable wrapped in `<li></li>` tags. After the loop has completed, the closing `</ul>` is added to the string, and the entire string is return. A simple test case is provided contain a list of fruit names as strings. If you wanted to use a similar function to accept user input, you would need to add an input box for a user to enter information, and then add another function that would capture that information, and pass it to the `return_list` function.

Q. **List 2-3 attacks that web applications are vulnerable to. How do these attacks work? How can we prevent those attacks?**

A.

Q. **Here is some starter code for a Flask Web Application. Expand on that and include a route that simulates rolling two dice and returns the result in JSON. You should include a brief explanation of your code.**

A.

Q. **If you were to start your full-stack developer position today, what would be your goals a year from now?**

A.
