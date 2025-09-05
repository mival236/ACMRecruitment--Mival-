# frequency.py

from collections import Counter
import re

def word_frequency(text: str, sort_by_freq: bool = True):
    """
    Count the frequency of each unique word in the text.
    
    Args:
        text (str): Input paragraph of text.
        sort_by_freq (bool): Whether to sort output by frequency (highest → lowest).
    
    Returns:
        dict: A dictionary of word → count.
    """
    # Normalize text: lowercase and extract words only
    words = re.findall(r"\b\w+\b", text.lower())
    
    # Count word frequencies
    counts = Counter(words)
    
    if sort_by_freq:
        # Sort by frequency (descending), then by word
        counts = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))
    
    return counts


if __name__ == "__main__":
    paragraph = """
    This is a simple test. This test is only a test.
    In the event of an actual emergency, this text would be much longer.
    """
    
    freq = word_frequency(paragraph)
    
    for word, count in freq.items():
        print(f"{word} → {count}")
