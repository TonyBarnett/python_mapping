import re


def clean_word(word, stop_words, lower_case_everything=True, char_swaps=None):
    if isinstance(word, str):
        #  return singularize(word.lower()) if singularize(word.lower()) not in stop_words else None
        if word in stop_words:
            return None
        w = word.lower() if lower_case_everything else word
        for token, replacement in char_swaps.items():
            w = w.replace(token, replacement)
        return w

    elif isinstance(word, list):
        return_words = list()

        for words in word:
            if words in stop_words:
                continue
            w = words.lower() if lower_case_everything else words
            for token, replacement in char_swaps.items():
                w = w.replace(token, replacement)
            return_words.append(w)

        return return_words
    else:
        raise ValueError()


def split_descripiton_into_tokens(description, token_regex, stop_words):
    return clean_word([word for word in token_regex.findall(description)], stop_words)



def clean_key(word):
    return word.replace('.', '_').replace('$', '¯')


class Document:
    def __init__(self,
                 _id, target_class, description, extended_description=None,
                 is_training=True, token_regex_pattern=r"\b[\w'\-]+\b", stop_words=None,
                 guess=None
                 ):
        self._id = clean_key(_id)
        self.target_class = target_class
        self.is_training = is_training
        self.guess = guess

        token_regex = re.compile(token_regex_pattern)

        self.description = description if isinstance(description, list) \
            else split_descripiton_into_tokens(description,
                                               token_regex=token_regex,
                                               stop_words=stop_words)

        if extended_description:
            self.extended_description = extended_description if isinstance(extended_description, list) \
                else split_descripiton_into_tokens(extended_description,
                                                   token_regex=token_regex,
                                                   stop_words=stop_words)

    def make_a_guess(self, guess):
        self.guess = guess

    def __str__(self):
        return self._id
