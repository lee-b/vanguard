# Vanguard

# Overview

This is intended to be a modern re-implementation of Nightscout.  **Pre-pre-pre-alpha status; not usable yet.**

It aims to be:

* A lot easier to set up and install
* More secure, especially for sharing data. Perhaps advanced sharing features, like highlighting particular patterns and issues and consulting a community.
* Perhaps automated analytics, like "You may need to reduce your basal, or decrease your bolus ratio at this time of day. To confirm which, do a basal test at this time tomorrow."
* More powerful, especially in terms of analytics
* More modern, in terms of look and feel and speed etc.
* More feature-complete, in terms of fully supporting basals, all macronutrients, etc.
* High-performance, asynchronous code
* Well-tested
* Clean, readable, maintainable code.
* Type-safe, fool-proof code, wherever reasonably possible


# Installation

Install `python3.7+`, then:

```
pip3 install -e .
```

# Running

Simply run:

```
vanguard-api
```

Then open [localhost:5000](http://localhost:5000/) in your browser.

# Contributing

Just submit a pull request.  Features belong in a feature/shortname branch.  Bugfixes belong in a bugfix/shortname_issuenumber branch.

## Setting up a dev environment

```
apt install pyenv
pyenv install 3.7.3
pyenv virtualenv 3.7.3 vanguard_dev
pyenv local vanguard_dev
pip install -r requirements/devtools.pip.in
```

Run `pytest` to test quickly, and `tox` for full, pre-merge-request testing.

# Contact

Email [Lee](mailto:leebraid@gmail.com).
