from tournament import Tournament

def main():
    teams = [
        "Team A", "Team B", "Team C", "Team D",
        "Team E", "Team F", "Team G", "Team H",
        "Team I", "Team J", "Team K", "Team L",
        "Team M", "Team N", "Team O", "Team P"
    ]

    t = Tournament(teams)

    while True:
        t.display()
        for i, match in enumerate(t.rounds[t.current_round]):
            if not match.winner:
                winner = input(f"{i + 1}번 경기 승자 입력 ({match.team1}/{match.team2}): ").strip()
                t.record_result(i, winner)
        if not t.advance_round():
            break

if __name__ == "__main__":
    main()
