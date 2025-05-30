==============
Issue tracking
==============


We use `GitHub Issues <https://docs.github.com/en/issues>`__ as our `issue tracking system <https://en.wikipedia.org/wiki/Issue_tracking_system>`__. All issues pertaining to the Qubes OS Project (including auxiliary infrastructure such as this website) are tracked in `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__.

How to open a new issue
-----------------------


First, let’s make sure the issue tracker is the right place.

I need help, have a question, or want to discuss something.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We’re happy to help, answer questions, and have discussions, but the issue tracker is not the right place for these activities. Instead, please see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>`.

I see something that should be changed in the documentation.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


We encourage you to submit the change yourself! Please see the `how to edit the documentation <https://www.qubes-os.org/doc/how-to-edit-the-documentation/>`__ for instructions on how to do so. If it’s something you can’t do yourself, please proceed to open an issue.

I would like to report a security vulnerability.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Thank you! If the vulnerability is confidential, please do not report it in our public issue tracker. Instead, please see :ref:`Reporting Security Issues in Qubes OS <project-security/security:reporting security issues in qubes os>`.

I still want to open an issue.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Great! Thank you for taking the time and effort to help improve Qubes! To ensure the process is efficient and productive for everyone involved, please follow these steps:

1. Carefully read our issue tracking `guidelines <#guidelines>`__. If your issue would violate any of the guidelines, **stop**. Please do not submit it.

2. `Search through the existing issues <#search-tips>`__, both open and closed, to see if your issue already exists. If it does, **stop**. :ref:`Do not open a duplicate. <introduction/issue-tracking:new issues should not be duplicates of existing issues>` Instead, comment on the existing issue.

3. Go `here <https://github.com/QubesOS/qubes-issues/issues/new/choose>`__.

4. Select the `type <#types>`__ of issue you want to open.

5. Enter a descriptive title.

6. Do not delete the provided issue template. Fill out every applicable section.

7. Make sure to mention any relevant documentation and other issues you’ve already seen. We don’t know what you’ve seen unless you tell us. If you don’t list it, we’ll assume you haven’t seen it.

8. If any sections of the issue template are *truly* not applicable, you may remove them.

9. Submit your issue.

10. Respond to any questions the official team asks. For example, you may be asked to provide specific logs or other additional information.



Eventually, your issue may be closed. See :ref:`how issues get closed <introduction/issue-tracking:how issues get closed>` for details about when, why, and how this occurs.

How issues are organized
------------------------


Issues can have several different properties and be organized in various ways. This section explains how we use labels, issue types, projects, and other features of GitHub’s issue tracking system in order to keep `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__ organized.

Labels
^^^^^^


When an issue is first created, it will receive the ``P: default`` (i.e., default priority) `label <https://github.com/QubesOS/qubes-issues/labels>`__ automatically. After an issue has been created, only Qubes team members have permission to modify labels. Many labels have descriptions on them that can be viewed by hovering over them or on the `list of labels <https://github.com/QubesOS/qubes-issues/labels>`__. Let’s go over some of the most important ones.

Priority
^^^^^^^^


There are several issue **priority** levels ranging from ``P: minor`` to ``P: blocker`` (see `here <https://github.com/QubesOS/qubes-issues/labels?q=P%3A>`__ for the full list). Every open issue should have exactly one priority. An open issue should not have more than one priority, and it should not lack a priority entirely. See :ref:`here <developer/releases/version-scheme:bug priorities>` for details about how the developers use these priorities.

Component
^^^^^^^^^


There are many **component** labels, each beginning with ``C:`` (see `here <https://github.com/QubesOS/qubes-issues/labels?q=C%3A>`__ for the full list). Every open issue should have at least one component. An open issue may have more than one component, but it should not lack a component entirely. When no other component applies, use ``C: other``.

Affected release
^^^^^^^^^^^^^^^^


A label of the form ``affects-<RELEASE_NUMBER>`` indicates that an issue affects the corresponding Qubes OS release. An issue can have more than one of these labels if it affects multiple releases.

Types
^^^^^


There are three issue `types <https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization>`__: Bug, Feature, and Task.

- **Bug** — An unexpected problem or behavior

- **Feature** — A request, idea, or new functionality

- **Task** — A specific piece of work



Every open issue should have exactly one type. **Bug** reports are for problems in things that already exist. If something doesn’t exist yet, but you think it ought to exist, then that issue should instead be a **Feature** request. If something already exists, but you think it could be improved in some way, that also qualifies as a **Feature** request. The **Task** type is for issues that are actionable but that fall under neither the **Bug** nor **Feature** types.

Projects
^^^^^^^^


According to GitHub, a `project <https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects>`__ is “an adaptable spreadsheet, task-board, and road map that integrates with your issues and pull requests on GitHub to help you plan and track your work effectively.” The issue tracker has several `projects <https://github.com/QubesOS/qubes-issues/projects>`__. Github projects allows more detailed issue states, and also attaching more metadata to issues. They also allow more focused view.

There is a special project in Qubes OS project: the `Current team tasks project <https://github.com/orgs/QubesOS/projects/19/views/1>`__ which represents current work of the core team. Issues in this project’s **backlog** section are not yet ready for work - they might be waiting for clarifications, blockers, decisions on priorities etc. Issues that are **ready** can be picked up by any team member. There should not be too many issues in **ready** column to decrease confusion and decision paralysis - good number is around 20. The **in review** state means that the developer is finished with the work (the completion state has been reached) - if something has to be postponed or abandoned, a justification should be posted in issue discussion.

Meta-issues
^^^^^^^^^^^


A meta-issue is an issue that serves primarily to collect and organize a group of other issues. This group of other issues typically exists in a hierarchy of `sub-issues <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues>`__, usually with the meta-issue at the top. (For example, we use meta-issues when we need a way to track work on specific features. We cannot use `projects <#projects>`__ for this, because we already use a project for tracking the work of the Qubes team as a whole, and projects cannot contain milestones or other projects.)

Meta-issues should have informative descriptions, not just lists of issues. In particular, each meta-issue should explain its goal, what is in scope, and what the relevant categories and priorities are.

In addition, meta-issues should have clear, concrete, and actionable criteria for when they will be closed. Meta-issues should never be “open-ended” or expected to stay open indefinitely. If this ever becomes unclear, the meta-issue should be closed until it becomes clear.

Search tips
-----------


- `Search both open and closed issues. <https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aissue>`__ For example, you may be experiencing a bug that was just fixed, in which case the report for that bug is probably closed. In this case, it would be useful to view `all bug reports, both open and closed, with the most recently updated sorted to the top <https://github.com/QubesOS/qubes-issues/issues?q=label%3A%22T%3A+bug%22+sort%3Aupdated-desc>`__.

- `Search with labels. <https://github.com/QubesOS/qubes-issues/labels>`__ For example, you can search issues by priority (`blocker <https://github.com/QubesOS/qubes-issues/labels/P%3A%20blocker>`__, `critical <https://github.com/QubesOS/qubes-issues/labels/P%3A%20critical>`__, `major <https://github.com/QubesOS/qubes-issues/labels/P%3A%20major>`__, etc.) and by component (`core <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+core%22>`__, `manager/widget <https://github.com/QubesOS/qubes-issues/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A%22C%3A+manager%2Fwidget%22+>`__, `Xen <https://github.com/QubesOS/qubes-issues/issues?q=is%3Aopen+is%3Aissue+label%3A%22C%3A+Xen%22>`__, etc.).

- Search by closure reason: `reason:completed <https://github.com/QubesOS/qubes-issues/issues?q=reason%3Acompleted>`__ and `reason:"not planned" <https://github.com/QubesOS/qubes-issues/issues?q=reason%3A%22not+planned%22>`__.

- `Search by project <https://github.com/QubesOS/qubes-issues/projects>`__.



Guidelines
----------


The issue tracker is not a discussion forum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The issue tracker is a tool to help the developers be more productive and efficient in their work. It is not a place for discussion. If you wish to discuss something in the issue tracker, please do so on the forum or mailing lists (see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>`). You can simply link to the relevant issue in your discussion post.

This guideline is important for keeping issues focused on *actionable information*, which helps the developers to stay focused on their work. When developers come back to an issue to work on it, we do not want them to have to sift through a large number of unnecessary comments before they can get started. In many cases, an issue that gets “too big” essentially becomes more trouble than it’s worth, and no developer will touch it (also see `every issue must be about a single, actionable thing <#every-issue-must-be-about-a-single-actionable-thing>`__). In these cases, we sometimes have to close the issue and open a new one. This is a waste of energy for everyone involved, so we ask that everyone help to avoid repeating this pattern.

Do not submit questions
^^^^^^^^^^^^^^^^^^^^^^^


`qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__ is not the place to ask questions. This includes, but is not limited to, troubleshooting questions and questions about how to do things with Qubes. Instead, see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>` for appropriate places to ask questions. By contrast, `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__ is meant for tracking more general bugs, enhancements, and tasks that affect a broad range of Qubes users.

Use the issue template
^^^^^^^^^^^^^^^^^^^^^^


When you open a new issue, an issue template is provided for you. Please use it. Do not delete it. The issue template is carefully designed to elicit important information. Without this information, the issue is likely to be incomplete. (If certain sections are not applicable, you may remove them, but please do so only sparingly and only if they are *truly* not applicable.)

It is also important to note the placement and content of the HTML comments in the issue template. These help us to have issues with a consistent format.

Every issue must be about a single, actionable thing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If your issue is not actionable, please see :doc:`Help, Support, Mailing Lists, and Forum </introduction/support>` for the appropriate place to post it. If your issue would be about more than one thing, file them as separate issues instead. This means we should generally not try to use a single issue as a “meta” or “epic” issue that exists only to group, contain, or track other issues. Instead, when there is a need to group multiple related issues together, use `projects <https://github.com/QubesOS/qubes-issues/projects>`__.

This guideline is extremely important for making the issue tracker a useful tool for the developers. When an issue is too big and composite, it becomes intractable and drastically increases the likelihood that nothing will get done. Such issues also tend to encourage an excessive amount of general discussion that is simply not appropriate for a technical issue tracker (see `the issue tracker is not a discussion forum <#the-issue-tracker-is-not-a-discussion-forum>`__).

New issues should not be duplicates of existing issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Before you submit an issue, check to see whether it has already been reported. Search through the existing issues – both open and closed – by typing your key words in the **Filters** box. If you find an issue that seems to be similar to yours, read through it. If you find an issue that is the same as or subsumes yours, leave a comment on the existing issue rather than filing a new one, even if the existing issue is closed. If an issue affects more than one Qubes version, we usually keep only one issue for all versions. The Qubes team will see your comment and reopen the issue, if appropriate. For example, you can leave a comment with additional information to help the maintainer debug it. Adding a comment will subscribe you to email notifications, which can be helpful in getting important updates regarding the issue. If you don’t have anything to add but still want to receive email updates, you can click the “Subscribe” button at the side or bottom of the comments.

Every issue must be of a single type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Every issue must be exactly one of the following types: a bug report (``bug``), a feature or improvement request (``enhancement``), or a task (``task``). Do not file multi-typed issues. Instead, file multiple issues of distinct types. The Qubes team will classify your issue according to its type.

New issues should include all relevant information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


When you file a new issue, you should be sure to include the version of Qubes you’re using, as well as versions of related software packages (:doc:`how to copy information out of dom0 </user/how-to-guides/how-to-copy-from-dom0>`). If your issue is related to hardware, provide as many details as possible about the hardware. A great way to do this is by :ref:`generating and submitting a Hardware Compatibility List (HCL) report <user/hardware/how-to-use-the-hcl:generating and submitting new reports>`, then linking to it in your issue. You may also need to use command-line tools such as ``lspci``. If you’re reporting a bug in a package that is in a :doc:`testing </user/downloading-installing-upgrading/testing>` repository, please reference the appropriate issue in the `updates-status <https://github.com/QubesOS/updates-status/issues>`__ repository. Project maintainers really appreciate thorough explanations. It usually helps them address the problem more quickly, so everyone wins!

There are no guarantees that your issue will be addressed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Keep in mind that `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__ is an issue tracker, not a support system. Creating a new issue is simply a way for you to submit an item for the Qubes team’s consideration. It is up to the Qubes team to decide whether or how to address your issue, which may include closing the issue without taking any action on it. Even if your issue is kept open, however, you should not expect it to be addressed within any particular time frame, or at all. At the time of this writing, there are well over one thousand open issues in `qubes-issues <https://github.com/QubesOS/qubes-issues/issues>`__. The Qubes team has its own roadmap and priorities, which will govern the manner and order in which open issues are addressed.

Issues and comments must be written in English
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


If English is not your native language, you may post a machine translation. If you wish, you may also include the original non-English text in a `collapsible section <#use-collapsible-sections-for-long-nonessential-content>`__.

Use collapsible sections for long, nonessential content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


On GitHub, create collapsible sections in Markdown like so:

.. code:: bash

      <details>
      <summary>Summary goes here. This line is optional.</summary>
      
      Long, nonessential content goes here. You can put a code block here, but make sure to leave empty lines before and after the fence lines (```).
      
      </details>



**Tip:** Use the “Preview” tab to make sure it renders correctly before posting.

How issues get closed
---------------------


If the Qubes developers make a code change that resolves an issue, then the issue will typically be `closed from the relevant commit or merged pull request (PR) <https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/linking-a-pull-request-to-an-issue>`__.

Bug reports
^^^^^^^^^^^


In the case of bugs, the package containing the change will move to the appropriate :doc:`testing </user/downloading-installing-upgrading/testing>` repository, then to the appropriate stable repository. If you so choose, you can test the fix while it’s in the :doc:`testing </user/downloading-installing-upgrading/testing>` repository, or you can wait for it to land in the stable repository. If, after testing the fix, you find that it does not really fix the reported bug, please leave a comment on the issue explaining the situation. When you do, we will receive a notification and respond on the issue or reopen it (or both). Please **do not** create a duplicate issue or attempt to contact the developers individually about a problem.

Resolution
^^^^^^^^^^


In GitHub, an issue can be `closed as either "completed" or "not planned" <https://github.blog/changelog/2022-03-10-the-new-github-issues-march-10th-update/#%F0%9F%95%B5%F0%9F%8F%BD%E2%99%80%EF%B8%8F-issue-closed-reasons>`__.

Being closed as ``completed`` means that the issue has been fixed (in the case of bugs) or done (in the case of enhancements and tasks). More precisely, it means that a commit containing the relevant work has been pushed. It takes time for this work to make its way into a package, which must then go through the :doc:`testing </user/downloading-installing-upgrading/testing>` process before finally landing in the relevant stable repository. Automated comments on the issue will announce when key events in this process occur.

Being closed as ``not planned`` means that the issue will *not* be fixed (in the case of bugs) or done (in the case of enhancements and tasks). When an issue is closed as ``not planned``, we add a **resolution** label starting with ``R:`` that specifies the reason for the closure, such as ``R: duplicate`` or ``R: cannot reproduce``. Each of these labels has a description that briefly explains the label. We also leave a comment containing a longer explanation for why the issue is being closed along with general information.

While issues that are closed as ``not planned`` get a more specific resolution label, issues that are closed as ``completed`` do not always get one, since the linked PRs, commits, automated messages, and the ``completed`` reason itself are often sufficient to convey all relevant information. For information about using closure reasons in searches, see `Search tips <#search-tips>`__.

Backports
^^^^^^^^^


Issues in GitHub can only be open or closed, but when it comes to bugs that affect multiple versions of Qubes OS, there are several possible states:

1. Not fixed yet

2. Fix developed but not yet committed (PR open)

3. Fix committed (PR merged), but update not yet pushed to any repo

4. Update pushed to testing repo for the most recent development version

5. Update pushed to stable repo for the most recent development version

6. Update backported to stable version(s) and pushed to the testing repo

7. Update pushed to stable repo of stable version(s)



We close issues at step 3. Then, as updates are released, the issue automatically gets the appropriate ``current-testing`` (``rX.Y-*-cur-test``) and ``stable`` (``rX.Y-*-stable``) labels. Based on these labels, it’s possible to select issues waiting for step 6 (see `issues by release <https://github.com/QubesOS/qubes-issues#issues-by-release>`__).

Therefore, if you see that an issue is closed, but the fix is not yet available to you, be aware that it may be at an intermediate stage of this process between issue closure and the update being available in whichever repos you have enabled in whichever version of Qubes you’re using.

In order to assist with this, we have a label called `backport pending <https://github.com/QubesOS/qubes-issues/labels/backport%20pending>`__, which means, “The fix has been released for the testing release but is pending backport to the stable release.” Our infrastructure will attempt to apply this label automatically, when appropriate, but it is not perfect, and the developers may need to adjust it manually.

Understanding open and closed issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Every issue is always in one of two states: open or closed, with open being the default. The **open** and **closed** states mean that, according to our available information at present, the issue in question either **is** or **is not** (respectively) actionable for the Qubes team. The open and closed states do not mean anything more than this, and it’s important not to read anything else into them. It’s also important to understand that closing an issue is, in effect, nothing more than changing a virtual tag on an issue. Closing an issue is never “final” in any sense, and it does not affect the issue itself in any other way. Issues can be opened and closed instantly with a single button press an unlimited number of times at no cost. In fact, since the open and closed states reflect our available information at present, one should expect these states to change back and forth as new information becomes available. Closed issues are fully searchable, just like open issues, and we explicitly instruct all users of the issue tracker to search *both* open *and* closed issues, which GitHub makes easy.

Workflow and what do issue states mean
--------------------------------------


There are some rules we use when assigning issues and tagging them.

Assigning issues
^^^^^^^^^^^^^^^^


To avoid a situation where an issue is “dead” - assigned to someone who is not actively working on it - and to help the team organize their work, an issue should be assigned to a person who currently works on it, or will start working on it in a very near future (about a week or two). One person can have several issues assigned at the same time (for example they may be working on one another issue while waiting for review), but if an issue is no longer actively being worked on (for example when it’s blocked by something else), it should be unassigned. At that point, if there is some partial work already done, there should be a comment about that, including link to the code (some WIP commit in some branch?) if applicable.

Issues should not be assigned as a todo-list several months in the future, or assigned to someone without their explicit confirmation that they are currently working on that issue or will start doing it shortly.

Working on an issue
^^^^^^^^^^^^^^^^^^^


Every issue should involve a clear statement of success: when is the issue finished? It might not be clear to the person making the issue, especially if it’s an enhancement request, but before work starts, the person working on the issue should make sure that it includes clear completion criteria in the description (via editing the description, if necessary). The completion criteria would ideally be a checklist, and consist of a list of pull requests/features, each preferably no more than two weeks of work. It’s also important to remember tests and documentation should also be part of the issue, if applicable.

An issue should also have a rough estimate how much time it needs, if it’s more than one-two days. Of course this might be updated later, if an issue turns out to be more (or maybe less) complicated than it has initially seemed.

When an issue is done (that is, the completion checklist has been completed), the issue should be moved to **ready** column in the *Current team tasks* project.
