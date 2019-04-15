The Artima Developer Community
Articles | News | Weblogs | Buzz | Books | Forums
Artima Weblogs | Guido van van Rossum's Weblog | Discuss | Email | Print | Bloggers | Previous | Next
Sponsored Link •

All Things Pythonic
Python main() functions
by Guido van van Rossum
May 16, 2003
Summary
For Python programmers, I've got some suggestions on how to write a main() function that's easy to invoke in other contexts, e.g. from the interactive Python prompt when you feel like experimenting.
ADVERTISEMENT
I've written a few main() functions in my time. They usually have a structure roughly like this:

"""Module docstring.

This serves as a long usage message.
"""
import sys
import getopt

def main():
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    main()
I'm sure many people write similar main() functions. I've got a few suggestions that make main() a little more flexible, especially as option parsing becomes more complex.
First, we change main() to take an optional 'argv' argument, which allows us to call it from the interactive Python prompt:

def main(argv=None):
    if argv is None:
        argv = sys.argv
    # etc., replacing sys.argv with argv in the getopt() call.
Note that we fill in the default for argv dynamically. This is more flexible than writing
def main(argv=sys.argv):
    # etc.
because sys.argv might have been changed by the time the call is made; the default argument is calculated at the time the main() function is defined, for all times.
Now the sys.exit() calls are annoying: when main() calls sys.exit(), your interactive Python interpreter will exit! The remedy is to let main()'s return value specify the exit status. Thus, the code at the very end becomes

if __name__ == "__main__":
    sys.exit(main())
and the calls to sys.exit(n) inside main() all become return n.
Another refinement is to define a Usage() exception, which we catch in an except clause at the end of main():

import sys
import getopt

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        # more code, unchanged
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
This gives the main() function a single exit point, which is preferable over multiple return 2 statements. This also makes it easier to refactor the argument parsing: raise Usage works just fine from inside a helper function, but return 2 would require careful passing on of the return values.
You might think that taking this to the extreme would move the try/except clause out of the main() function, into the code at the end of the module (if __name__ == "__main__": .... But that would mean that when you call main() interactively, you'd get a traceback for command line syntax errors, which isn't very helpful.

However, another generalization can be helpful: define another exception, perhaps called Error, which is treated just like Usage but returns 1. This can then be used for expected errors like failure to open necessary files, which are not command line syntax errors, but yet expected, and where again a traceback doesn't feel very friendly.

What's your favorite convention for writing main()?

Talk Back!

Have an opinion? Readers have already posted 31 comments about this weblog entry. Why not add yours?

RSS Feed

If you'd like to be notified whenever Guido van van Rossum adds a new entry to his weblog, subscribe to his RSS feed.

 DiggDigg |  del.icio.usdel.icio.us |  RedditReddit
About the Blogger

	Guido van Rossum is the creator of Python, one of the major programming languages on and off the web. The Python community refers to him as the BDFL (Benevolent Dictator For Life), a title straight from a Monty Python skit. He moved from the Netherlands to the USA in 1995, where he met his wife. Until July 2003 they lived in the northern Virginia suburbs of Washington, DC with their son Orlijn, who was born in 2001. They then moved to Silicon Valley where Guido now works for Google (spending 50% of his time on Python!).

This weblog entry is Copyright © 2003 Guido van van Rossum. All rights reserved.
Sponsored Links


 Google	 
 	  Web Artima.com   

Copyright © 1996-2018 Artima, Inc. All Rights Reserved. - Privacy Policy - Terms of Use

