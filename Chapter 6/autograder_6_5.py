text = "X-DSPAM-Confidence:    0.8475"

colon = text.find(':')
piece = text[colon + 1 : ]

number = float(piece.strip())

print(number)
