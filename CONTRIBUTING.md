# How to contribute to PyOData

## **Did you find a bug?**

* Create a pull request for simple problems.

* Otherwise open a new issue with steps to reproduce.

## **Did you write a patch?**

* Before contributing, please, make yourself familiar with git. You can [try
  git online](https://try.github.io/). Things would be easier for all of us if
  you do your changes on a branch. Use a single commit for every logical
  reviewable change, without unrelated modifications (that will help us if need
  to revert a particular commit). Please avoid adding commits fixing your
  previous commits, do amend or rebase instead.

* Every Pull Request must contain test or a good justification why
  the test part is not included.

* If you believe that it is not necessary to add a test because there is
  already a test going through the statements you have modified, you are probably
  wrong because you either added something new and it should be tested or you fixed
  a bug which was not detected by the test and hence the test must be enhanced
  (ideally, you fist fix the test to reproduce the bug and then you fix the bug).

* Link commits to issues via referencing issue numbers: https://help.github.com/en/articles/closing-issues-using-keywords

* Every commit must have either comprehensive commit message saying what is being
  changed and why or a link (an issue number on Github) to a bug report where
  this information is available. It is also useful to include notes about
  negative decisions - i.e. why you decided to not do particular things. Please
  bare in mind that other developers might not understand what the original
  problem was.

* Try to follow the seven rules when writing commit messages: https://chris.beams.io/posts/git-commit/

* If you are not sure how to write a good commit message, go through
  the project history to find some inspiration.

* Update [CHANGELOG.md](CHANGELOG.md) (Unreleased section)

## **Did you fix whitespace, format code, or make a purely cosmetic patch?**

Changes that are cosmetic in nature and do not add anything substantial to the
stability, functionality, or testability of PyOData will generally not be
accepted.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies within all project spaces, and it also applies when
an individual is representing the project or its community in public spaces.
Examples of representing a project or community include using an official
project e-mail address, posting via an official social media account, or acting
as an appointed representative at an online or offline event. Representation of
a project may be further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
