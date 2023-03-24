
code = {"a": "● –", "b": "	– ● ● ●", "c": "– ● – ●", "d":"– ● ●", "e": "●", "f": "	● ● – ●", "g": "– – ●",
        "h": "● ● ● ●", "i": "● ●", "j": "● – – –", "k": "– ● –", "l": "● – ● ●", "m": "– –", "n": "– ●",
        "o": "– – –", "p": "● – – ●", "q": "– – ● –", "r": "● – ●", "s": "● ● ●", "t": "–", "u": "	● ● –",
        "v": "● ● ● –", "w": "● – –", "x": "– ● ● –", "y": "– ● – –", "z": "– – ● ●", " ": " ",
        }


code_input = input("Input a secret message\n").lower()

coded_word = []

for l in code_input:
        coded_word.append(code[l])

string = ""
for i in coded_word:
        string += i
        string += "  "

print(string)






