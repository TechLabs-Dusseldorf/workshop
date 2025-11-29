# GitHub Commands

These are the main commands that we are going to use during the Project phase.
Make sure to download and install git on your pc first.
https://git-scm.com/downloads

### Only for the first Time

- Download the Project on your PC:
```
git clone THE_GITHUB_LINK_OF_THE REPOSOTRY
git pull
```
### GitHub setup
Sometimes you get an error message due to conflict with your github localy and Remote
To fix it, apply: 

```
git config --global user.email YOUR_GITHUB_EMAIL
git config --global user.name YOUR_NAME
```

### Preparing Your Branch

Make a new branch at the begging with your name
```
git switch -c YOUR_NAME_Branch
git push
```
### Implementing new Features

when working on a Task use a new branch based on YOUR_NAME_Branch

```
git checkout YOUR_NAME_Branch 
git switch -c YOUR_TASK/Feature_Title
git push
git branch --set-upstream-to=origin/master Iebo_Branch 
```

### Updating Branches
Adding new Files/ changes to the Branch is done by applying:

```
git add .
git commit -m "Message"
git push
```
### Switching between branches

```
git checkout Branch_Name
git pull 
```

### Merge conflicts

When error because of a conflict you have to solve the conflict first then continue with the normal update:

```
git add .
git merge --continue
accept the commit message
git push
git pull
```

## Delete a branch

```
git branch -d 
```
### Update a Branches based on main Branch

```
git pull origin main  
```
## Pull Requests to merge changes to other branches
Live example
