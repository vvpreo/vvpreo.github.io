#! /usr/bin/python3
# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''

52
<article class="hentry">
  <!-- <header>
    <h1 class="entry-title">But Will It Make You Happy?</h1>
    <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
    <p class="byline author vcard">
        By <span class="fn">Stephanie Rosenbloom</span>
    </p>
  </header> -->

  <div class="entry-content">
      <p>...article text...</p>
      <p>...article text...</p>

      <figure>
        <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
        <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
      </figure>

      <p>...article text...</p>
      <p>...article text...</p>

      <aside>
        <h2>Share this Article</h2>
        <ul>
          <li>Facebook</li>
          <li>Twitter</li>
          <li>Etc</li>
        </ul>
      </aside>

      <div class="entry-content-asset">
        <a href="photo-full.png">
          <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
        </a>
      </div>

      <p>...article text...</p>
      <p>...article text...</p>

      <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
  </div>

  <footer>
    <p>
      A version of this article appeared in print on August 8,
      2010, on page BU1 of the New York edition.
    </p>
    <div class="source-org vcard copyright">
        Copyright 2010 <span class="org fn">The New York Times Company</span>
    </div>
  </footer>
</article>'''.strip())

if __name__ == '__main__':
    from html.parser import HTMLParser

    N = int(input().strip())
    text = '\n'.join([input().strip() for _ in range(N)])


    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            print("Start :", tag)
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

        def handle_endtag(self, tag):
            print("End   :", tag)


        def handle_startendtag(self, tag, attrs):
            print("Empty :", tag)
            for attr in attrs:
                print("->", attr[0], ">", attr[1])


    parser = MyHTMLParser()
    parser.feed(text)
