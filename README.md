# Instructions

In this challenge, you will create your first commit. Happy branching! 🎋

## 🎯 Data and Context

Until now we have only been working and making changes on one branch, the `master` branch.

This is actually not good practice! The `master` branch should always have the version in production that is fully functional. If you push bad code to your `master` branch, it can break your application.

That's why when we want to modify code, we create new branches called "feature branches".

We test our code and when we are "sure" that it works, we merge it back into the `master` branch.

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

This will:

- Create and navigate to a directory (folder) for this challenge in your terminal
- Download all of the files for this challenge
- Set up a new repository locally and on GitHub
- Open the challenge in VS Code
- Run the test suite for this challenge

At this point the tests will fail with a lot of red, that is expected: we haven't started working yet. Keep on reading.

Run the following command in the terminal to check you are in the right directory:

```bash
pwd
```

Your result should look like this:

```bash
~/code/<user.github_nickname>/{{ local_path_to("03-Data-Transformation/08-Intro-To-Git-And-Versioning/03-Branching-Out") }}/
```

❌ If it doesn't, consult a TA!

✅ If it does, then you are ready to take on this challenge!

## 🧩 Implementation

### 1. First Feature Branch

We only have two rules so far from [Zen of Python](https://peps.python.org/pep-0020/) in our `zen.txt` file. That means our first test is already passing, but none of the rest! Let's add them, but carefully.

Keep in mind, we still want to track our changes regularly to avoid losing work, but we also want to make sure all our tests pass before we merge it into `master`, so let's create a new branch to work in.

1. First, as this is a new repository, let's push what we have locally to our remote with `git push origin master` in your terminal.

1. Now create a new feature branch using the terminal. There are two ways we could do this:

    **OPTION A**

    - Use the command `git branch add_more_rules` to create a branch named `add_more_rules`.

    - Then use `git checkout add_more_rules` to navigate into the branch.

    **OPTION B**

    - Use the command `git checkout -b add_more_rules`. The `-b` lets us combine the two steps, it both creates `add_more_rules` and navigates into it.
    <br>

1. Go to VS Code and update `zen.txt` to add more of the lines from `Zen of Python`. Let's start with these:

    ```markdown
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    ```

1. Run your tests with `make`. You should only pass two tests. That's okay because we want to show you how this will display on Kitt!

1. Go back to your terminal and check the status of your git, you can see that git has detected your change.

1. Commit your change (Don't forget to add a commit message!).

1. Go back to your terminal and checkout to  `master`. Now go back to VS Code and have a look at the `zen.txt` file. Can you see the new lines we added? Why is that?

    <details>
    <summary markdown="span">Solution 🔓</summary>

    You can’t see the line because you added it when you were on your feature branch.  We have not made any changes on `master` locally or remotely.

    Take a few minutes to think about it, it’s hard to understand that you have a single file on your computer `zen.txt` but that its content changes depending on which branch you are on. This is what we call versioning. You have different versions of the same file.

    </details>
    <br>

1. Go to your terminal and change your current branch to `add_more_rules`. Push your branch to the remote repository. Remember, we're not pushing our `master` branch this time, you'll need to specify the feature branch in your `git push` command.

1. Go to [github.com](http://github.com/) and check that your changes are there. You won't find it in your `master` on the repository, but you will see it if you select your branch from the dropdown in the top right.

    ![Choosing your branch in GitHub](https://wagon-public-datasets.s3.amazonaws.com/data-analytics/03-Data-Transformation/08-Intro-To-Git-And-Versioning/03-Branching-Out/branches_in_github.png)

### 2. Merge to Master

Now that we learned about developing new code on a separate branch, it’s time to learn how to integrate our feature into the `master` code base.

To do this, you will need to create a pull request to merge your feature branch `add_more_rules` into the `master` branch.

1. On your repository on [github.com](http://github.com/). Go to the Pull Requests tab and **click on the “New pull request” button.**

1. In the section on “Comparison of changes”, choose the `master` base (the branch you want to update with the new code) and `add_more_rules` as a comparison. We want to merge `add_more_rules` into `master`. Click on the “create pull request” button.

   Choose a title for your pull request. The name will default to your last commit message, if you have multiple commits in a branch it can be useful to give your pull request a more general name relating to your feature. For this pull request, you can let it be the last commit message. When you are ready to create the pull request, click on the “Create pull request” button.

1. You should get a similar screen:

    ![Screenshot of open pull request on github.com](https://wagon-public-datasets.s3.amazonaws.com/data-analytics/03-Data-Transformation/08-Intro-To-Git-And-Versioning/03-Branching-Out/pull_request_comparison.png)

    Click on **“Merge pull request”** then on **"Confirm Merge"**. Our changes in the `add_more_rules` branch are now integrated into `master` in our remote repository, the repository on GitHub.

    Congratulations! 🎉 You have merged your feature into the `master` branch on your **remote repository**.

1. Go to this challenge on Kitt and you should see the challenge tests have been run, but the challenge is **only 50% complete**. This makes sense as we were only passing 2 out of 4 tests when we pushed our work.

    Throughout the course, challenges can often be completed in stages so you can check your work as you go! Get used to running tests regularly and pushing your work to Kitt when you pass a test. It's a great habit to get into.

In our next step, we're going to create a new feature branch and add the last few lines to your `zen.txt` file:

### 3. Updating Local Master

Our code is now up to date on our **remote master** branch, but our **local master** branch is now out of date! The other half of a pull request is making sure our **local master** is up to date. Let's see how to do it!

1. Just as we had to ***push*** our local code to update the remote code, now we have to ***pull*** the remote code to update the code in our local `master` branch.

    Change the branch to `master` in your terminal and then double check your text file in VS Code. See if it has the `add_more_rules` update. Take a few minutes to make sure you understand. Discuss with your buddy.

    Go back to your terminal and run `git pull origin master`, this will fetch all the changes from your remote master and merge them into your local master.

1. Check to see if your changes to `zen.txt` are now appearing in your local master in VS Code.

1. Now it's time to delete your `add_more_rules` branch. Your work won’t be lost because it has been integrated into the `master` branch after the merge.

    To delete a branch, just use the following command `git branch -D add_more_rules`

    Note: You can't delete the branch from inside the branch, so make sure you're in `master`

    Extra note: with your `data-analytics-setup` you can also use `git sweep` a handy command we've written that will search for and delete any branches that have been merged into `master`

    You can also delete branches directly in github after you've merged your pull request, but that won't remove them locally.

### 4. The Final Push

Ok, try this one on your own. If you get lost refer to the step-by-step instructions above. Don't push and merge to `master` until you have passed all four tests.

1. Create a new feature branch, call it whatever you like. Use it to add the last few lines to your `zen.txt` file:

    ```markdown
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    ```

1. Stage, Commit, and Push to your new feature branch.

1. Merge to `master` with a Pull Request.

1. Update your local `master` and delete the feature branch.

## 🏁 Finishing up

Congratulations! You've just made your first feature branches. Git is described as a flow, it can feel nebulous at first, but with some practice, you build an intuition for how things are working.
