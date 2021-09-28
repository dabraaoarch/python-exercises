import unittest

def inverse_string(word: str) -> str:
    result = ""
    word_size = len(word)-1
    for i in range(len(word)):
        result += word[word_size-i]
    return result

def inverser(string_to_reverse: str) -> str:
    string_type = ''
    result = ''
    if type(string_to_reverse) != type(string_type):
        return False

    word_array = string_to_reverse.split()
    for word in word_array:
        result += " " + inverse_string(word)

    return result[1:]

class TestReverse(unittest.TestCase):
    def test_reverse_empty_word(self):
        '''
        An empty word must return an empty response
        '''
        word = ''
        inverse = inverser(word)
        self.assertEqual(inverse, word)
        self.assertIsInstance(inverse, str)

    def test_reverse_invalid_word(self):
        '''
        An invalid word must return False
        '''
        word = int(152)
        inverse = inverser(word)
        self.assertFalse(inverse)

    def test_reverse_valid_word(self):
        '''
        For a valid string, it must return the ivnersed string
        '''
        word = 'abcde'
        inverse = inverser(word)
        reverse = inverser(inverse)
        self.assertEqual(reverse, word)
        self.assertFalse((word==inverse))

    def test_reverse_valid_sentence(self):
        '''
        It must reverse only the words, not the sentence
        '''
        sentence = 'abcde jklm nopq'
        inverse_sentence = inverser(sentence)
        inverse_word = inverse_string(sentence)
        reverse_sentence = inverser(inverse_sentence)
        self.assertEqual(sentence, reverse_sentence)
        self.assertFalse((sentence==inverse_word))
        


if __name__ == "__main__":
    unittest.main()
    #print(inverser("daniel é um cara bem legal"))