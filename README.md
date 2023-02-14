Title: Lab 4 Linux User Management Part 2
Course: INET-4031
By: Genuine Song

---

Contents: create-users.input, create-users.py
  
---

create-users.input - Input file which contains user accounts including their name, password, and groups which is used as a input file for create-users.py

create-users.py - An automated script which allows the terminal to automate adding users from an input file in linux which then saves their passwords and assigns them to corresponding groups

---

To run this command use "sudo ./create-users.py < create-users.input" or "cat create-users.input | sudo ./create-users.py" without the quotaitons.
