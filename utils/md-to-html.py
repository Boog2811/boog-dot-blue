# Converts a markdown file into a valid HTML file, conserving the syntax

# Algorithm
# Read in the provided markdown file
# Place each line into the corresponding HTML tag, based on formatting
# Markdown syntax reference: https://www.markdownguide.org/basic-syntax/
# This list is not exhaustive in examples, and is intended to generally cover what is supported by this script.
# These include:
#  Headings:
#   # -> <h1>
#   ## -> <h2>
#   ### -> <h3>

#  Paragraphs:
#   these two need to be decided upon how to handle it, if that's two spaces, <br>, \, or something else
#   Text\n\n -> <p>
#   Text\nText2 -> <p>Text<br/>Text2</p>

#  Emphasis:
#   **Text** | __Text__ -> <strong>
#   *Text* | _Text_ -> <em>
#   ***Text*** | ___Text___ | __*Text*__ | **_Text_** -> <em><strong>

#  Blockquotes:
#   > Text -> <blockquote>

#  Lists:
#   1. item 1 -> <ol><li>
#   - item -> <ul><li>
#   Indented lists are supported

#  Code:
#   `text` -> <code>
#   

#  Links:
#   [hyperlink](https://link) -> <a href=https://link>hyperlink</a>

#   The following are not inherently markdown syntax, but I'm adding them for my purposes:
#   The first # -> Page title
#   The line following the first # -> class=author