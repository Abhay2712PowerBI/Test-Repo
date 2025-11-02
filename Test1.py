


def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]
if __name__ == "__main__":
    # demo
    print(reverse_string("hello"))  # olleh
    print(reverse_string("Machine Learning"))  # gninraeL enihcaM
    print(reverse_string("Data Science"))  # ecneicS ataD
    print(reverse_string("Python"))  # nohtyP
    print(reverse_string("OpenAI"))  # IAnepO
    print(reverse_string("ChatGPT"))  # TPGtahC

    def to_uppercase(s: str) -> str:
        """Return the input string converted to uppercase."""
        return s.upper()

    # convert to uppercase demo
    print(to_uppercase("hello"))  # HELLO
    print(to_uppercase("Machine Learning"))  # MACHINE LEARNING
    print(to_uppercase("Data Science"))  # DATA SCIENCE
    print(to_uppercase("Python"))  # PYTHON
    print(to_uppercase("OpenAI"))  # OPENAI
    print(to_uppercase("ChatGPT"))  # CHATGPT
    def count_vowels(s: str) -> int:
        """Return the number of vowels in the input string."""
        return sum(1 for c in s.lower() if c in "aeiou")

    # count vowels demo
    print(count_vowels("hello"))  # 2
    print(count_vowels("Machine Learning"))  # 6
    print(count_vowels("Data Science"))  # 5
    print(count_vowels("Python"))  # 1
    print(count_vowels("OpenAI"))  # 4
    print(count_vowels("ChatGPT"))  # 1
    
    def concatenate_strings(*parts: str, sep: str = "") -> str:
        """Return the concatenation of the input strings, using sep between parts."""
        return sep.join(parts)

    # concatenate demo
    print(concatenate_strings("hello", "world"))  # helloworld
    print(concatenate_strings("Machine", " ", "Learning"))  # Machine Learning
    print(concatenate_strings("Data", " ", "Science"))  # Data Science
    print(concatenate_strings("Python", "3"))  # Python3
    print(concatenate_strings("Open", "AI"))  # OpenAI
    print(concatenate_strings("Chat", "GPT"))  # ChatGPT
    
    def join_two_strings(a: str, b: str, sep: str = "") -> str:
        """Return the two input strings joined using sep between them."""
        return f"{a}{sep}{b}"

    # join demo
    print(join_two_strings("hello", "world"))  # helloworld
    print(join_two_strings("hello", "world", sep=" "))  # hello world
    print(join_two_strings("Data", "Science", sep=" "))  # Data Science
    print(join_two_strings("Python", "3"))  # Python3

    def find_even_odd(numbers):
        """Return a tuple (evens, odds) from an iterable of integers."""
        evens = [n for n in numbers if isinstance(n, int) and n % 2 == 0]
        odds = [n for n in numbers if isinstance(n, int) and n % 2 != 0]
        return evens, odds

    # demos
    nums = [1, 2, 3, 4, 5, 6]
    ev, od = find_even_odd(nums)
    print(ev)  # [2, 4, 6]                              
    print(od)  # [1, 3, 5]

    ev, od = find_even_odd(list(range(1, 11)))
    print(ev)  # [2, 4, 6, 8, 10]
    print(od)  # [1, 3, 5, 7, 9]

    ev, od = find_even_odd([10, 15, 20, 25, 30])
    print(ev)  # [10, 20, 30]
    print(od)  # [15, 25]

 