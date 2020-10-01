# Student_Grading_Tool
A simple python script for student record filtering.



## Code Structure

```shell
│   README.md
│
├───code
│       tool.py
│
└───test
        data.csv
        test.py
```

+ code: code for the tool
+ test: test data and a test script



## Usage

Run `py tool.py <arguments> <path>` to use. `<path>` is the path of csv file.

Arguments are listed as follows:

+ `-name <pattern>` : prints all the students whose name matches the given pattern (the pattern is a regular expression, case insensitive)
+ `-email <pattern> `: prints all the students whose email matches the given pattern
+ `-gpa <gpa>[+-]`: prints all the students who belong to the given level. If suffixed with ‘+’, then prints also the students who are above that level. If suffixed with ‘-’, then prints also the students who are below that level.
+ `-help`: help for usage

