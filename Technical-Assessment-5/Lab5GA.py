happy = {
    "happy", "joy", "love", "wonderful", "excellent",
    "great", "good", "amazing", "awesome", "beautiful",
    "excited", "glad", "cheerful", "delightful", "smile",
    "laugh", "laughing", "enjoy", "fantastic", "perfect",
    "pleased", "hopeful", "kind", "fun", "brilliant"
}

sad = {
    "sad", "unhappy", "cry", "crying", "angry",
    "hate", "pain", "hurt", "lonely", "depressed",
    "miserable", "terrible", "awful", "disappointed",
    "heartbroken", "fear", "bad", "sorry", "hopeless"
}

def number_happy(sentence):
    words = sentence.lower().split()
    return sum(word.strip(".,!?") in happy for word in words)

def number_sad(sentence):
    words = sentence.lower().split()
    return sum(word.strip(".,!?") in sad for word in words)

sentence = input("Enter a sentence: ")

h = number_happy(sentence)
s = number_sad(sentence)

print("Happy words:", h)
print("Sad words:", s)

if h > s:
    print("Positive")
elif s > h:
    print("Negative")
else:
    print("Neutral")