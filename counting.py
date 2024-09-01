def histogram(source_text):
  source_text = source_text.split()
  words = []
  for word in source_text:
    word = word.lower()
    if word not in words:
      words += [1, word]
    else:
      words[words.index(word) - 1] += 1
  return words

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[histogram.index(word) - 1]

if __name__ == '__main__':
      def source_text():
        with open('dnd5esrd.txt', 'r') as f:
            return f.read().replace('\n', ' ')
        
      source_text = source_text()

      histogram = histogram(source_text)


      print("Unique words:")
      print(unique_words(histogram))

      print("Frequency of 'the':")
      print(frequency('the', histogram))

      print("Frequency of 'dragon':")
      print(frequency('dragon', histogram))

      print("Frequency of 'sword':")
      print(frequency('sword', histogram))

