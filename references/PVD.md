**Product Vision Document**

Post Here: Subreddit Predictor
> Post Here helps you find the best place to share on Reddit.

# ☝️ Proposal

- What problem does your app solve?
    - Allows user to decide where to post
    - Guides user to relevant subreddits
    - Streamlines user experience regarding post location
- Be as specific as possible; how does your app solve the problem?
    - Use Natural Language Processing to compare topics of post and subreddit contents
    - Provides simple interface to guide input of post and output suggestions
    - Grab data from API, display previous posts, interact with posts and reddit

- What is the mission statement?
    - Provide a well designed product to guide users to optimize subreddit posting location
        - (Define metric by which we should steer project: frontpage,  post karma(most points), answer question, find community of like-minded user)

# 💡 Features

- What features are required for your minimum viable product?
    - App to input post and result subreddit recommendation
    - A text field for the user to enter their words / content

    1. As a user I can login and create an account

    2. As a user I can send a post to the DS API to find out where the best place on reddit is to post

    3. As a user I can save the response to my profile

    4. As a user I can search through my saved posts

    5. As a user I can delete my saved posts

    6. A model that uses NLP techniques to determine which subreddit has the most similar posts

- What features may you wish to put in a future release?
    - Visuals
    - Display hottest post on that subreddit
- What do the top 3 similar apps do for their users?
    - Flowchart on how to decide which subreddit

# 🛠 Frameworks - Libraries


- What 3rd party frameworks/libraries are you considering using?
    - spacy, keras
    - React (js)

- Do the APIs you need require you to contact them to gain access?
    - [basilica.ai](http://basilica.ai), reddit api
- Are you required to pay to use said API(s)?
    - No

# 🧮  For Data Scientists


- Describe the established data source with at least rough data able to be provided on day one.
    - Scrape data from reddit, maybe kaggle
    - Find pre-assembled reddit datasets
    - Tasks to delegate:
        - model creation (NLP on post and subreddits, save model)
        - data engineering (linking the database to  backend, query the database)
        - data scraping / allocation

- Write a description for what the data science problem is. What uncertainty or prediction are you trying to discover? How could this data be used to find a solution to this problem?
    - Problem is that it is unknown which subreddit the sample post most belongs to.
    - The prediction will tell us which subreddit the post will best belong to according to the metric of our choosing
- What kind of target output can you deliver to the Web/UX/iOS teams to work with? Is it in JSON format or something else?
    - At minimum, the target output would be the name or url of the most relevent subreddits.
    - Stretch: Data on the subreddit's most common words (maybe average post length?)

# 🎯 Target Audience

- Who is your target audience? Be specific.
    - Content seekers (I just want to scroll through similar stuff)
    - Hot Pagers (peeps who want to have their post go hot)
    - Community Searchers (I want to find likeminded people)
    - "Karma Foragers" (possibly scrape upvote score and filter subreddit to popular only)
    - Answer Seekers [I have a question I want answered well!] (probably not worried about karma)

- What feedback have you gotten from potential users?
- Have you validated this problem and your solution with a target audience? Describe how,

# 🔑 Prototype Key Feature(s)

- How long do you think it will take to implement these features?
    -
- Do you anticipate working on stretch functionality after completion of a Minimal Viable Product?
    - Yes
