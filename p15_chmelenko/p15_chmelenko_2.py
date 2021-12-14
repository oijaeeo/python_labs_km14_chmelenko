def chunk():
    for suit in suit_list:
        for card in card_list:
            yield str(card) + ' ' + suit
            
card_list = ["A", *range(2, 11), "J", "Q", "K"]
suit_list = ["diamonds", "clubs", "hearts", "spades"]
result = chunk()
while True:
    print(next(result))