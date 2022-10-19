#Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical notes
# beginning with the start position and following the moves given as parameter.

#	Example:
# compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def music(musical_notes, list_of_moves, start_position):

    new_list = [musical_notes[start_position]]

    for move in list_of_moves:
        if move < 0:
            start_position -= (move + 1)
            start_position = start_position % len(musical_notes)
        else:
            start_position = start_position + move
            start_position = start_position % len(musical_notes)
        new_list.append(musical_notes[start_position])
    return new_list

print(function4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))