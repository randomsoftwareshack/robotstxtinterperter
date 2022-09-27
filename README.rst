================
What Does It Do?
================

In a website, there is a robots.txt file, which tells web crawlers which files
they should and shouldn't access. This project interprets this file into a computer
understandable format.

============
Installation
============

pip3 install robotstxtinterpreter

=============
How to Use It
=============


To use it, run the interpretRobots function, with the root domain (ex 
https://example.com/ or http://example2.com) passed in as an argument

This file will return an array in this format:
[dict: user-agents, list: sitemap]
The dict: user-agents is formatted like this:
{user-id: "allowed": [], "disAllowed": []}


Here is an example usage:
.. code-block:: python
    from robotstxtinterpreter.robotstxtinterpreter import robotsinterpret;

    a = robotsinterpret.interpretRobots("http://example.com");
    print("Allowed files for useragent *: ", a[1]["*"]["allowed"]);
    print("Disallowed files for useragent *: ", a[1]["*"]["disAllowed"]);
    print("Sitemaps: ", a[2])

If it can't find the robots.txt file or the robots.txt file is blank, it will return [{}, []]
