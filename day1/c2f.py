#!/usr/bin/env python
# coding: utf-8

print("This is a C' to F' converter.")
temp_in_celsius = input("Please enter a temperature, in C\n--> ")
temp_in_fahrenheit = float(temp_in_celsius) *9/5 + 32

print("The temperature in Fahrenheit is: {:.2f}".format(temp_in_fahrenheit))
