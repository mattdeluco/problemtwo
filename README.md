#Problem Two: Sales Taxes#
To download and run problemtwo:

    $ git clone https://github.com/mattdeluco/problemtwo.git
    $ cd problemtwo
    $ ./run.sh
   
   ```run.sh``` assumes a Python 2.7 interpreter is on PATH and will run problemtwo.py with each of the three input sets.

problemtwo.py must have an input file as its first argument, and may have an optional sales tax exception file as a second argument.

    $ python ./problemtwo.py
    problemtwo.py <line items input file> <sales tax exceptions file> 

A small set of unit tests are also available:

    $ ./test.sh
    $ # or
    $ python -m unittest discover -s test/

####Input File####
To run an alternative problem set create a plain text file, each line formatted similar to ```1 imported bottle of Woodford Reserve at 30.00``` or ```<Quantity> <description> at <cost>```, where quantity may include fractional values using a decimal, and cost may have 0, 1, or 2 decimal places.  See [input3.txt](https://github.com/mattdeluco/problemtwo/blob/master/input3.txt) for an example.

####Sales Tax Exception File####
This file contains a string on each line to be matched against an item description.  If any of the strings match an item description, basic sales tax (10%) will not be applied to that item.  See [sales_tax_exceptions.txt](https://github.com/mattdeluco/problemtwo/blob/master/sales_tax_exceptions.txt) for an example.

##Notes##
###Design Considerations###
I initially started out with the intention to create a set of tax classes to apply to items on the receipt.  However, I realized a more modular approach could be taken using "Categories".

Since a comprehensive set of product descriptions were not given for tax-free products (books, food, medical) I wanted to create something configurable.  Categories are named, have a list of descriptions (from a file for example), and a function to be applied to any item with a matching description.

When printing a receipt calculated values for each category are aggregated from the line items and printed out as a single line ("Sales Taxes" for example.)  Different categories may share the same name so that they are aggregated on the same line - in problemtwo.py, both Basic Sales Tax and Import Duties are named "Sales Taxes" such that they're summarized on the same line.

Categories aside from taxes may also be created, such as "Student Discount".  See [problemtwo.py:61](https://github.com/mattdeluco/problemtwo/blob/master/problemtwo.py#L61) for example.



###Python Decimal module###
Floating point values should be avoided when working with monetary values and calculations (or anything else that requires accuracy.)  See [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/2/tutorial/floatingpoint.html) and [Decimal fixed point and floating point arithmetic](https://docs.python.org/2/library/decimal.html).

When working with money an alternative to using Python's Decimal is to store values in cents and only use the integer type.

##Known Issues##

 1. "Sales Taxes" will not appear on the receipt if there are none to be calculated
 2. "Total" will print as "0" if there is no total to be calculated (rather than "0.00")

##Problem Specification##
Basic sales tax is applicable at a rate of 10% on all goods, except books,
food, and medical products that are exempt. Import duty is an additional sales
tax applicable on all imported goods at a rate of 5%, with no exemptions.

When I purchase items I receive a receipt which lists the name of all the items
and their price (including tax), finishing with the total cost of the items,
and the total amounts of sales taxes paid.  The rounding rules for sales tax
are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up
to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping
baskets...

INPUT:

Input 1:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85

Input 2:
1 imported box of chocolates at 10.00
1 imported bottle of perfume at 47.50

Input 3:
1 imported bottle of perfume at 27.99
1 bottle of perfume at 18.99
1 packet of headache pills at 9.75
1 box of imported chocolates at 11.25

OUTPUT

Output 1:
1 book : 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83

Output 2:
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15

Output 3:
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85
Sales Taxes: 6.70
Total: 74.68

