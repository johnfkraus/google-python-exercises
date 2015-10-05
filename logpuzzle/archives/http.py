## Given a url, try to retrieve it. If it's text/html,

## print its base url and its text.

def wget(url):

    ufile = urllib.urlopen(url)  ## get object for url

    info = ufile.info()   ## meta-info url content

    if info.gettype() == 'text/html':

        print 'base url:' + ufile.geturl(

            text = ufile.read()  ## read all

            print text

        The above code works fine, but does not include error handling if a url
        does not work for some

        reason. Here's a version of the function which adds try/except logic to
        print an error message if

        the url operation fails.

        ## Version that uses try/except to print an error message if the

        ## urlopen() fails.

        def wget2(url):

          try:

            ufile = urllib.urlopen(url)

            if ufile.info().gettype() == 'text/html':

              print ufile.read()

          except IOError:

            print 'problem reading url:', url
