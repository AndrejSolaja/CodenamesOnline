from django.shortcuts import get_object_or_404
from home.models import SetReci
import random

class GameState:
    game_words = {}
    remaining_words = []
    is_game_init = False
    clue = ""
    clue_num = 0
    turn = 3
    # 0 -> reroll Blue (istovremeno)
    # 1 -> reroll Read (istovremeno)
    # 2 -> Blue leader
    # 3 -> Blue guesser
    # 4 -> Red leader
    # 5 -> Red guesser
    # 6 -> victory screen

    redLeaderId = None
    redGuesserId = None
    blueLeaderId = None
    blueGuesserId = None

    @staticmethod
    def init_words():
        print("Initializing game words...")
        active_set = get_object_or_404(SetReci, active=True)
        words = list(active_set.reci.all())
        random.shuffle(words)
        words = [word.rec.lstrip() for word in words]
        group_lengths = [9, 8, 7, 1]
        remaining_length = len(words) - sum(group_lengths)

        if remaining_length > 0:
            group_lengths.append(remaining_length)

        word_groups = []
        start = 0
        for size in group_lengths:
            end = start + size
            word_groups.append(words[start:end])
            start = end

        blue_groups = word_groups[0]
        red_groups = word_groups[1]
        white_groups = word_groups[2]
        black_groups = word_groups[3]

        temp_dict = {}

        for word in blue_groups:
            temp_dict[word] = ["blue", 0]
        for word in red_groups:
            temp_dict[word] = ["red", 0]
        for word in white_groups:
            temp_dict[word] = ["white", 0]
        for word in black_groups:
            temp_dict[word] = ["black", 0]

        keys = list(temp_dict.keys())
        random.shuffle(keys)
        for key in keys:
            GameState.game_words[key] = temp_dict[key]

        GameState.remaining_words = word_groups[4]

        print("before", GameState.is_game_init)
        GameState.is_game_init = True
        print("after", GameState.is_game_init)

        print(GameState.game_words)
