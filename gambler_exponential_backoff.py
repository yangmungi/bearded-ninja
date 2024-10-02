import math
from random import random


def col_round(x):
    """from https://www.reddit.com/r/learnpython/comments/92ne2s/why_does_round05_0/"""
    frac = x - math.floor(x)
    if frac < 0.5:
        return math.floor(x)
    return math.ceil(x)


class Gambler:
    def __init__(self, wallet: int = 20, exit_ratio: int = 30, divisor: int = 20):
        self.wallet = wallet
        self.initial = wallet // divisor
        self.memory = 0
        self.state = None
        self.exit_cond = self.initial * exit_ratio

    def gamble(self):
        if self.state is None:
            gambled = self.initial
        elif self.state == "grow":
            gambled = self.memory * 2.0
        elif self.state == "half":
            gambled = self.memory / 2.0
        elif self.state == "linear":
            gambled = self.memory + self.initial

        gambled_round = col_round(gambled)
        if gambled_round == 0:
            print(gambled, gambled_round)

        if gambled_round > self.wallet:
            gambled_round = self.wallet

        return gambled_round

    def spend(self, gambled=0):
        self.memory = gambled
        self.wallet -= gambled

    def earn(self, winnings):
        self.wallet += winnings
        self.react(winnings)

    def react(self, winnings):
        """Starts off geometrically growing, then goes to backoff to linear growth."""
        if winnings > 0:
            if self.state is None or self.state == "grow":
                self.state = "grow"
            else:
                self.state = "linear"
        else:
            self.state = "half"

    def exits(self):
        return self.wallet > self.exit_cond


class Casino:
    def __init__(self, minimum_gamble=5, win_rate=0.5055, return_rate=2):
        self.minimum_gamble = minimum_gamble
        self.win_rate = win_rate
        self.return_rate = return_rate

    def is_valid_gambler(self, gambler):
        """Bouncer"""
        if gambler.wallet < self.minimum_gamble:
            return False
        return True

    def play(self, gambled):
        card = random()

        win_int = 0
        if card > self.win_rate:
            win_int = 1

        return win_int * self.return_rate * gambled


###
if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--win-rate", "-w", type=float, default=0.5)
    ap.add_argument("--return-rate", "-r", default=None)
    ap.add_argument("--min-gamble", "-m", type=int, default=1)
    ap.add_argument("--start-money", "-s", type=int, default=20)
    ap.add_argument("--bet-divisor", "-d", type=int, default=20)
    ap.add_argument("--exit-ratio", "-e", type=int, default=30)
    ap.add_argument("--num-games", "-n", type=int, default=5)

    pa, _ = ap.parse_known_args()

    casino = Casino(pa.min_gamble)

    total_rounds = 0
    max_game_length = 0

    total_maxes = 0
    max_max = 0

    enders = []

    total_games = pa.num_games
    initial = pa.start_money

    for i in range(total_games):
        gambler = Gambler(initial)
        counter = 0
        maximum = 0
        print(f"-- game {i + 1} / {total_games} --")

        while casino.is_valid_gambler(gambler):
            if gambler.exits():
                print(f"{counter + 1:3d} won enough - quit")
                break

            elif not casino.is_valid_gambler(gambler):
                print(f"{counter + 1:3d} not enough to gamble - quit")
                break

            gambled = gambler.gamble()

            if gambled <= 0:
                print(f"{counter + 1:3d} gambled 0 - quit")
                break

            if gambled < casino.minimum_gamble:
                gambled = casino.minimum_gamble

            gambler.spend(gambled)
            earned = casino.play(gambled)
            gambler.earn(earned)

            if gambler.wallet > maximum:
                maximum = gambler.wallet

            print(
                f"{counter + 1:3d} gambling {gambled:3d} - earned {earned:3d} - has {gambler.wallet:4d}"
            )
            counter += 1

            if counter > max_game_length:
                max_game_length = counter

            if maximum > max_max:
                max_max = maximum

        total_rounds += counter
        total_maxes += maximum

        enders.append(gambler.wallet - initial)

        print(f"played {counter}, max {maximum}")

    enders_count = len(list(filter(lambda x: x > 0, enders)))

    print("-- stats --")

    print(
        f"play length average: {float(total_rounds) / total_games:.1f} max: {max_game_length}"
    )
    print(f"average max: {float(total_maxes) / total_games:.1f} max max: {max_max}")
    print(f"winning plays: {enders_count} / {total_games}")
    print(f"outcome: {sum(enders)}")
