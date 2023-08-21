def count_words(file_name):
  """Counts the number of words in each line of a text file.

  Args:
    file_name: The name of the text file.

  Returns:
    A list of the number of words in each line.
  """
  with open("/usercode/files/books.txt", "r") as f:
    lines = f.readlines()

  word_counts = []
  for line in lines:
    words = line.split()
    word_counts.append(len(words))

  return word_counts


def main():
  """The main function."""
  file_name = "/usercode/files/books.txt"
  word_counts = count_words(file_name)

  for line_number, word_count in enumerate(word_counts):
    print(f"Line {line_number + 1}: {word_count} words")


if __name__ == "__main__":
  main()