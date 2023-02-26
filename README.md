# prairie-learn-deadline-feature

##Inspiration

Every time we log in to PrairieLearn, all we really care about is which assignments are upcoming. However, it can be time-consuming and tedious to manually go through every course instance to find all the upcoming assignments, which has resulted in us missing deadlines. To solve this problem, we wanted to create a tool that would easily display upcoming assignments and add them to our Google Calendar, so that we could get notifications.

## What it Does
Our program parses all the relevant course data on the user's PrairieLearn homepage, and then sorts it by the most recent deadlines. Then we add sub-sections to each course instance in the homepage displaying the upcoming assignments in a clickable view that redirects them to the given assignment. Additionally, you can export your assignments to Google Calendar such that all assignment instances that exist get added to PrairieLearn.

We built the tool mostly using the Beautiful Soup and Selenium libraries. Parsing the data was done by reading and inspecting a lot of the elements since the data is all rendered client-side. We faced some challenges while parsing the data since the structure of loading all the elements into Python was not straightforward, and the Beautiful Soup docs were not that helpful. However, we were able to figure it out by working together as a team and experimenting with different approaches.

Adding elements, and especially the deadline course instances to the home page was really challenging since we were building it using Python, and the code was not robust enough to add a JavaScript environment to it. Therefore, we had to code the JavaScript using Python scripting and string insertions. This was a very time-consuming process, but it helped us to understand how the front-end and back-end interact with each other.

Working with the Google Calendar API proved to be non-trivial, and we faced a lot of issues by integrating the PrairieLearn data into a large-scale object that can be created into calendar event instances. However, we were able to overcome these issues by working collaboratively and breaking down the problem into smaller sub-problems.

## Accomplishments that we're proud of
We are extremely proud of our teamwork and how well we were able to delegate tasks based on each member's interests. When we first got all the data in a representable object, and being able to push events to the calendar using the data was an incredible breakthrough moment for the group that we all enjoyed.

Another accomplishment that we are proud of is learning many good team practices in coding, especially using git as a team, and maintaining different branches in an organized manner. We also learned all the tech we used for this project, including Beautiful Soup, Selenium, and all the Google APIs we had to use.

## What we learned
We learned that altering some small sections of a website is a lot more work than it seems like. We also learned how to work collaboratively as a team to overcome complex problems. Additionally, we gained a lot of experience working with the different technologies we used for this project, such as Beautiful Soup, Selenium, and Google APIs.

## What's next for PrairieLearn Deadline Calendar View
Our next step is to make the tool more user-friendly and scalable. We want to integrate it fully into the browser, so that the script doesn't have to re-run every time we want to use it. We can do this in two different ways. We can add it as a Chrome extension, or we can try to create a pull request to the open-sourced PrairieLearn git and see if we can commit our changes with the main base.

On top of that, there are a lot of design choices we want to add, such as being able to alter how many upcoming assignments are available and how the Google Calendar implementation is for each

## Built With
beautiful-soup
css
github
google
google-calendar
html5
javascript
pycharm
python
selenium


## [Video Demo](https://youtu.be/_aYr_QjD5A8)

