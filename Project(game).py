import time
import random
sentences = [
    "Python programming is very interesting",
    "Artificial intelligence is the future",
    "Practice makes a person perfect",
    "Computer science is fun to learn",
    "Coding improves logical thinking",
    "Technology is changing the world"
]
selected = random.sample(sentences, 2)

print("🧠 Typing Speed Test Game")
print("\nType these sentences exactly as shown:\n")

for line in selected:
    print(line)

input("\nPress Enter when ready...")

start = time.time()

print("\nStart typing:")
typed1 = input()
typed2 = input()

end = time.time()

time_taken = end - start

original_text = selected[0] + selected[1]
typed_text = typed1 + typed2

words = len(original_text.split())
wpm = (words / time_taken) * 60

correct_chars = 0
for i in range(min(len(original_text), len(typed_text))):
    if original_text[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(original_text)) * 100

print("\n⏱ Time taken:", round(time_taken, 2), "seconds")
print("⌨ Typing Speed:", round(wpm, 2), "WPM")
print("🎯 Accuracy:", round(accuracy, 2), "%")
