#
# MIT License
# 
# Copyright (c) 2024 Manuel Bottini
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

#!/usr/bin/python3

import datetime
import sys
import os
import re

def update_copyright_year(file_path):
    current_year = datetime.datetime.now().year

    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if the fourth line contains the copyright information
    if len(lines) > 3:
        copyright_line = lines[3]  # Index 3 corresponds to the copyright line

        # Check if the line contains 'Copyright' and the name of the copyright owner
        # Change "Manuel Bottini" with any name
        if 'Copyright (c)' in copyright_line and "Manuel Bottini" in copyright_line:
            if str(current_year) not in copyright_line:
                # Copyright (c) XXXX-YYYY
                matches = re.findall(
                    r'Copyright\s\(c\)\s\d{4}-\d{4}\s',
                    copyright_line)
                if matches:
                    print("Found Copyright (c) XXXX-YYYY")
                    matches = re.findall(
                        r'\d{4}-\d{4}',
                        copyright_line)
                    copyright_line = re.sub(
                        r'\d{4}-\d{4}',
                        f'{matches[0].split("-")[0]}-{current_year}',
                        copyright_line)
                else:
                    # Copyright (c) XXXX
                    matches = re.findall(
                        r'Copyright\s\(c\)\s\d{4}\s',
                        copyright_line)
                    if matches:
                        print("Found Copyright (c) XXXX")
                        matches = re.findall(
                            r'\d{4}',
                            copyright_line)
                        copyright_line = re.sub(
                            r'\d{4}',
                            f'{matches[0]}-{current_year}',
                            copyright_line)

                print(copyright_line)
                # Update the line in the list of lines
                lines[3] = copyright_line

                # Write the updated content back to the file
                with open(file_path, 'w') as file:
                    file.writelines(lines)
                    print("Copyright year updated to ", current_year)
            else:
                print("Copyright year is up to date")
        else:
            print("There is no copyright notice in the file")
    else:
        print("File does not even have three lines")

def get_files_in_subfolders(root_folder):
    file_list = []
    if os.path.isfile(root_folder):
        file_list.append(root_folder)
    elif os.path.isdir(root_folder):
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                full_path = os.path.join(root, file)
                if ".git" in full_path:
                    continue
                if "gradle" in full_path:
                    continue
                if "__pycache__" in full_path:
                    continue
                if "build" in full_path:
                    continue
                if "bin" in full_path:
                    continue
                if "obj" in full_path:
                    continue

                if ".idea" in full_path:
                    continue
                if ".json" in full_path:
                    continue
                if ".xml" in full_path:
                    continue
                if ".iml" in full_path:
                    continue
                if ".apk" in full_path:
                    continue
                if ".jar" in full_path:
                    continue
                if ".bin" in full_path:
                    continue
                if ".dex" in full_path:
                    continue
                if ".class" in full_path:
                    continue
                if ".png" in full_path:
                    continue
                if ".jpg" in full_path:
                    continue
                if ".keystore" in full_path:
                    continue
                if ".pbxproj" in full_path:
                    continue
                if ".storyboard" in full_path:
                    continue
                if ".blend" in full_path:
                    continue
                if full_path.endswith(".o"):
                    continue
                if full_path.endswith(".webp"):
                    continue
                if full_path.endswith(".meta"):
                    continue
                if full_path.endswith(".so"):
                    continue
                if full_path.endswith(".fbx"):
                    continue
                if full_path.endswith(".ods"):
                    continue
                if full_path.endswith(".ilk"):
                    continue
                if full_path.endswith(".obj"):
                    continue
                if full_path.endswith(".idb"):
                    continue
                if full_path.endswith(".pdb"):
                    continue
                if full_path.endswith(".dll"):
                    continue
                if full_path.endswith(".exp"):
                    continue

                if ".tlog" in full_path:
                    continue
                if "/build/intermediates" in full_path:
                    continue
                if "/build/generated" in full_path:
                    continue
                if "/build/tmp" in full_path:
                    continue
                if "/node_modules" in full_path:
                    continue
                if "/x64/Debug" in full_path:
                    continue

                file_list.append(full_path)
    else:
        print("The path is neither a file nor a directory.")

    return file_list

if __name__ == "__main__":
    base_path = None
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    if base_path == None:
        print("No base path given. Usage: python3 copyright_checker.py <base_path>")
        exit(1)

    if not os.path.exists(base_path):
        print("Invalid base path, it does not exist.")

    files_list = get_files_in_subfolders(base_path)
    for file_path in files_list:
        print(file_path)
        update_copyright_year(file_path)

