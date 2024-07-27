"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts, and the text
    of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "party",
    "Party Time!",
    ["place", "adverb", "verb_past_tense", "adjective", "plural_noun"],
    """Once upon a time, there was a(n) {adjective} party at the {place}. 
        Everyone {verb_past_tense} and danced with {plural_noun}. 
        They all had a(n) {adverb} time!"""
)

story3 = Story(
    "nature",
    "Magical Forest",
    ["noun", "noun_2", "verb_past_tense", "adjective", "adjective_2"],
    """In a(n) {adjective} forest, there lived a(n) {noun} that {verb_past_tense}.
        It was known for its {adjective_2} {noun_2} and magical powers."""
)

story4 = Story(
    "adventure",
    "My Adventure",
    ["adjective", "noun", "verb_past_tense", "adjective_2", "plural_noun"],
    """Today, I went on a(n) {adjective} adventure to find a lost {noun}.
        I had to {verb_past_tense} through {adjective_2} {plural_noun} to reach my goal."""
)

# Make dict of {code:story ...}
stories = {s.code: s for s in [story, story2, story3, story4]}