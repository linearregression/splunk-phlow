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

    # update your production branch
    git checkout production
    git rebase upstream/production
    git push # push to origin, but NEVER force-push production

    # update your topic branch(es)
    git checkout <branch-name>
    git rebase upstream/production
    git push -f # force-push to origin since you rewrote history (i.e., changed hashes)
    ```

4. Hack away at your branch and test

   a. Edit your branch and commit: `git add <files>; git commit [--amend]`

   b. Force push: `git push` or `git push -f` (for amended commits)

   c. You should receive an email from no-reply@ise.com
      (see *Autostager*, below) within 60 seconds of pushing

   d. Test on a telx host by copy-pasting the commands from the email

      See the document, `TESTING.md`, in this directory.
      It contains instructions for smoke test, host impersonation,
      rspec, and the helpful files you can use to validate your code.
      It also contains a list of custom facter facts that you can
      use for your puppet manifests.

   e. If your branch is not perfect, go back to step 4a

5. Prepare your branch for merge

   a. When you believe your branch is ready for merging into the
      production branch, add a **Signed-off-by** signature:

    ```
    git commit --amend -s
    ```

   b. Add a comment to your pull request, saying that
      you've signed off on the branch and request approval for it.
      Make sure you mention **@iseoptions/puppet-committers** to get
      our attention.

6. After your branch is merged (or whenever upstream/production is updated),
   it's time to do some repo maintenance. See *Git housecleaning*, below.


