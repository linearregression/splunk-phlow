Pull requests (PR)
------------------

To submit a patch to iseoptions/puppet, fork the repo and work within
a branch of your fork.

1. Ensure your `~/.gitconfig` contains:

    ```
    [push]
      default = tracking
    ```

2. Set up a remote tracking branch and pull request

   a. `git checkout -b <branch_name>`

   b. Do an initial push: `git push -u origin <branch_name>`

   c. Submit a [Pull Request](https://help.github.com/articles/using-pull-requests)

3. Ensure your branches are up-to-date:

    ```bash
    # retrieve upstream changes
    git fetch --prune upstream

    # Checkout master branch in your fork
    git checkout master
    
    # rebase with the upstream master branch
    git rebase upstream/master
    git push # !! push to origin, but NEVER force-push upstream/splunk-phlow

    # update your topic branch(es)
    git checkout <branch-name>
    git rebase upstream/master
    git push -f # force-push to origin since you rewrote history (i.e., changed hashes)
    ```

4. Hack away at your branch and test

   a. Edit your branch and commit: `git add <files>; git commit [--amend]`

   b. Force push: `git push` or `git push -f` (for amended commits)


5. Prepare your branch for merge

   a. When you believe your branch is ready for merging into the
      splunk-phlow master branch, add a **Signed-off-by** signature:

    ```
    git commit --amend -s
    ```


