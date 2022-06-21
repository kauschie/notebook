# def show_notes():
#     print("show notes")

# def search_notes():
#     print("search notes")

# def add_note():
#     print("add note")

# def modify_note():
#     print("modify note")

# def quit():
#     print("quit")

# choices = {
#             "1": show_notes,
#             "2": search_notes,
#             "3": add_note,
#             "4": modify_note,
#             "5": quit,
#         }

def match(string, filter):
    """Determine if this note matches the filter text. Return True if it
        matches, False otherwise.

        Search is case sensitive and matches both text and tags."""
    return filter in string
    
def search(list_of_strings, filter):
    """ Find all notes that match the given filter string."""
    return [string for string in list_of_strings if match(string, filter)]