# SEL Programming Classes
This repository contains the interactive materials, i.e.
scripts/assignments/examples, for programming classes designed and hosted at
SEL.

Contact: Brett Deaton, STEM Fundamentals program


### Course Catalog

**Getting Started with Python.** An active orientation to Python using Jupyter
Notebooks. The audience is anyone with little to no programming experience.
When done, participants will be able to run, modify, and write simple scripts
using basic syntax like `print`, `for`-loops, `if`-statements, `input`,
and put a `list` to work through its methods and Python's built-in functions.


### Quick Start For Class Participants
If your class is run through a cloud based interpreter like
[Binder](https://mybinder.org/), you may be interacting with this code through
a server and won't need to download a local copy at all.

If you do want the code on your local machine:
1. Download zip of this repository.
2. Navigate to `<yourclass>` directory.
3. Follow the instructions in `<yourclass>/README.md`.

Or for an updateable copy with the entire version history, follow the
instructions for `git clone` below.


### Quick Start For Contributors
If you want to create a new or improve an old SEL programming class, reach out.
We'd love your ideas! To join the development team:
1. Create your own github account with conventional handle `<username>SEL`.
2. Request an invite to the organization `Schweitzer-Engineering-Laboratories`
   (contact Thomas Benda, Jason Kemp in 2020).
3. Request write access to this repository (contact Brett Deaton in 2020).
4. Clone this repo:
   `git clone https://github.com/Schweitzer-Engineering-Laboratories/programming-classes.git`.
5. Develop using the git workflow: add/remove/modify files > `git add` >
   `git commit` > `git push`.
   Keep your commits *small* (e.g. a few hours of work) and
   *coherent* (e.g. avoid commits that solve multiple unrelated issues).


### Conventions
Create new classes in the root directory using a short name in CamelCase
containing no whitespace, dashes, or underscores.

Add a short class description to [Course Catalog](#course-catalog) above for
each new class.

Create a `README` file in each course root directory describing the course
simply, including information common to other `README`s

Store images in `images` directory at the root level for each course.

Make your commit messages clear and concise. Limit the first line
(i.e. the subject of the commit) to
[50 characters or less](https://chris.beams.io/posts/git-commit/#limit-50) and
write in the
[imperative mood](https://chris.beams.io/posts/git-commit/#imperative).
Refrain from a body unless further explanation is needed.
For example:
```
Introduce new problems to Get Started Python
```


### License
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text">
<a rel="cc:attributionURL" property="dct:title" href="https://github.com/Schweitzer-Engineering-Laboratories/programming-classes">Programming Classes</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://selinc.com/">Schweitzer Engineering Laboratories</a> is licensed under <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a>
</p>

This is a copyleft license, allowing free reuse, modification, and
distribution of this material as long as it is given proper attribution,
linked to the original license,
and identifies any changes. Derivative works must be distributed
under the same license.

Note, this CC license is usually used for works of art and education not
software, for which the MIT or GPL licenses are more appropriate.
We use the CC license because this repository's primary purpose is to educate
not to create a usable software tool.

Note, we distribute this material under the BY-SA license rather than the
more permissive BY license, in order to incorporate other learning material
distributed under the BY-SA license (e.g. Wikipedia).
