# SEL Programming Classes
This repository contains the interactive materials, i.e.
scripts/assignments/examples, for programming classes designed and hosted at
Schweitzer Engineering Laboratories.

Contact: Brett Deaton, STEM Fundamentals Program


### Course Catalog

[Start Programming With Python](StartProgrammingPython/README.md).
An active intro to Python using Jupyter Notebooks.
The audience is anyone with little to no programming experience.

[Python for Programmers](PythonForProgrammers/README.md).
An active overview of Python's core language
features, data structures, and object model. The audience is anyone already
writing code, who wants a boost into Python.


### Quick Start for Class Participants
You can interact with your own instance of this code repository directly
in your browser by visiting this Binder link:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Schweitzer-Engineering-Laboratories/programming-classes/main)

For a source-controlled copy with the entire version history, follow the
instructions for `git clone` below.

Or if you just want the code on your local machine without dealing with git:
1. Download and extract a zip of this repository.
2. Navigate to `<yourclass>` directory.
3. Follow the instructions in `<yourclass>/README.md`.


### Quick Start For Contributors
If you want to create a new or improve an old SEL programming class, reach out.
We'd love your ideas! To join the development team:
1. Create your own github account with conventional handle `<username>SEL`.
2. Request an invite to the organization `Schweitzer-Engineering-Laboratories`.
   (Contact Thomas Benda, Jason Kemp, or Robert Pepka as of 2022.)
3. Request write access to this repository. (Contact Brett Deaton as of 2022.)
4. Clone this repo:
   `git clone https://github.com/Schweitzer-Engineering-Laboratories/programming-classes.git`.
5. Develop using the
   [GitHub workflow](https://guides.github.com/introduction/flow/),
   keeping the `main` branch always deployable. For example:

   * pull current state of main branch:
     `git pull --rebase`
   * create local `dev` branch (name it better than this) from `main` to work in:
     `git switch -c dev`
   * modify > commit > repeat:
     `git add ... git commit ...`
   * push completed development branch to github:
     `git push -u dev`
   * merge `dev` into `main` on github:
     create github pull request > pass code review > merge

   As always, keep your commits *small* (e.g. a few hours of work) and
   *coherent* (e.g. avoid commits that solve multiple unrelated issues).


### Conventions
Create new classes in the root directory using a short name in CamelCase
containing no whitespace, dashes, or underscores.

Add a short class description to [Course Catalog](#course-catalog) above for
each new class.

Create a `README.md` file in each course root directory describing the course
simply, including information common to other `README`s.

Create the following directories at the root level for any course as needed:
`images`, `examples` for real-world applications at the learning level of the
class, `projects` for students' final projects.

Make your commit messages clear and concise. Limit the first line
(i.e. the subject of the commit) to
[50 characters or less](https://chris.beams.io/posts/git-commit/#limit-50) and
write in the
[imperative mood](https://chris.beams.io/posts/git-commit/#imperative).
Feel free to refrain from a body if further explanation isn't needed.

Students who don't use git may contribute by sharing their work with the
instructor who can commit to this repository.


### License
[Programming Classes](https://github.com/Schweitzer-Engineering-Laboratories/programming-classes)
by [Schweitzer Engineery Laboratories](https://selinc.com/) is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).

<a rel="licenseICON" href="https://creativecommons.org/licenses/by-sa/4.0"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a>
</p>

If you are a student or teacher anywhere in the world, please use this material!
It is disributed under a copyleft license, allowing free reuse, modification,
and distribution as long as derivative works give proper attribution,
link to the original license, identify changes, and are distributed under the
same license.

Note, this CC license is usually used for works of art and education not
software, for which the MIT or GPL licenses are more appropriate.
We use the CC license because this repository's primary purpose is to educate
not to create a usable software tool.

Note, we distribute this material under the BY-SA license rather than the
more permissive BY license, in order to incorporate other learning material
distributed under the BY-SA license (e.g. Wikipedia).
