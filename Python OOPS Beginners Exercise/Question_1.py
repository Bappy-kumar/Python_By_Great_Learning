class Flashcard:
    def __init__(self, term, definition, category):
        self.term = term
        self.definition = definition
        self.category = category
    
    def check_definition(self, user_definition):
        return self.definition == user_definition
class FlashcardDeck:
    def __init__(self): # dont modify this method
        self.flashcards = []

    def add_flashcard(self, flashcard):  # dont modify this method
        self.flashcards.append(flashcard)

    '''
    Method to remove a flashcard based on the term.
    Parameters: self, term
        (the term of the flashcard to be removed)
    Return Value: 
        True if the flashcard was successfully removed, False if the flashcard was not found.
    '''
    def remove_flashcard(self, term):
        for flashcard in self.flashcards:
            if flashcard.term == term:
                self.flashcards.remove(flashcard)
                return True
        return False        
        
        
    '''
    Method to retrieve all flashcards of a specific category.
    Parameters: self, category
    Return Value:
        A list of flashcards in the specified category.
    '''
    def get_flashcards_by_category(self, category):
        return len([flashcard for flashcard in self.flashcards if flashcard.category == category])
        


flashcardDeck = FlashcardDeck()

num = int(input())

for i in range(num):
    term = input()
    definition = input()
    category = input()
    
    flashcard = Flashcard(term, definition, category)
    
    flashcardDeck.add_flashcard(flashcard)
    
ch = int(input())

if ch==1:
    term_to_remove = input()
    status = flashcardDeck.remove_flashcard(term_to_remove)
    print("Flashcard",term_to_remove,"removed:",status)
elif ch==2:
    category = input()
    cards = flashcardDeck.get_flashcards_by_category(category)
    print("Number of Flashcards in",category,":",cards)