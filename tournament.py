class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None

    def __repr__(self):
        return f"{self.team1} vs {self.team2} → {self.winner or '진행 중'}"


class Tournament:
    def __init__(self, teams):
        if len(teams) != 16:
            raise ValueError("참가 팀은 16개여야 합니다.")
        self.rounds = []
        self.current_round = 0
        self._create_initial_round(teams)

    def _create_initial_round(self, teams):
        matches = []
        for i in range(0, len(teams), 2):
            matches.append(Match(teams[i], teams[i + 1]))
        self.rounds.append(matches)

    def record_result(self, match_index, winner):
        match = self.rounds[self.current_round][match_index]
        if winner not in [match.team1, match.team2]:
            raise ValueError("승자는 해당 경기의 팀 중 하나여야 합니다.")
        match.winner = winner

    def advance_round(self):
        winners = [m.winner for m in self.rounds[self.current_round] if m.winner]
        if len(winners) * 2 != len(self.rounds[self.current_round]) * 2:
            raise ValueError("모든 경기의 승자를 입력해야 다음 라운드로 진행할 수 있습니다.")
        if len(winners) == 1:
            print(f"\n🏆 최종 우승자: {winners[0]}")
            return False
        next_round = []
        for i in range(0, len(winners), 2):
            next_round.append(Match(winners[i], winners[i + 1]))
        self.rounds.append(next_round)
        self.current_round += 1
        return True

    def display(self):
        round_name = {0: "16강", 1: "8강", 2: "4강", 3: "결승"}
        print(f"\n=== {round_name.get(self.current_round, '토너먼트')} ===")
        for i, match in enumerate(self.rounds[self.current_round]):
            print(f"{i + 1}. {match}")
