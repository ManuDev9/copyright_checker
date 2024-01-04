# copyright_checker
This is a very simple python project that let you check the license date in all files in all subdirectories and change it if the copyright notice does not have the current year.

If no copyright notice is found, the script will just print the path to the file

The copyright is expected to be in the fourth line

There are the expected formats:
- Copyright (c) XXXX-YYYY
- Copyright (c) XXXX

Which will be respectively transformed into:
- Copyright (c) XXXX-ZZZZ
  - If ZZZZ is the current year and ZZZZ != YYYY
- Copyright (c) XXXX-ZZZZ
  - If ZZZZ is the current year and ZZZZ != XXXX

