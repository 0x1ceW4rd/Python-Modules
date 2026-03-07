#!/usr/bin/env python3

more_data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1488,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    hi_scores = [
        highp
        for highp in more_data["players"]
        if more_data["players"][highp]["total_score"] > 2000
    ]
    print("High scorers (>2000):", hi_scores)

    double_scores = [
        more_data["players"][dscore]["total_score"] * 2
        for dscore in more_data["players"]
    ]
    print("Scores doubled:", double_scores)

    activemf = [
        highp
        for highp in more_data["players"]
        if more_data["players"][highp]["sessions_played"] > 20
    ]
    print("Active players:", activemf)
    print()

    print("=== Dict Comprehension Examples ===")
    pscores = {
        player: more_data["players"][player]["total_score"]
        for player in more_data["players"]
    }
    print("Player scores:", pscores)

    score_list = [
        "high" if s["score"] >= 2500 else "medium"
        if s["score"] >= 1500 else "low"
        for s in more_data["sessions"]
    ]
    scores = {cat: score_list.count(cat) for cat in set(score_list)}
    print("Score categories:", scores)

    ach_count = {
        player: more_data["players"][player]["achievements_count"]
        for player in more_data["players"]
    }
    print("Achievement counts:", ach_count)
    print()

    print("=== Set Comprehension Examples ===")
    u_players = {player for player in more_data["players"]}
    print("Unique players:", u_players)

    u_achievements = {achievement for achievement in more_data["achievements"]}
    print("Unique achievements:", u_achievements)

    gamemodes = {mode for mode in more_data["game_modes"]}
    print("Game modes:", gamemodes)
    print()

    print("=== Combined Analysis ===")

    print(f"Total players: {len([player for player in more_data['players']])}")
    print(
        f"Total unique achievements: "
        f"{len([achievement for achievement in more_data['achievements']])}"
    )

    scores = [
        more_data["players"][player]["total_score"]
        for player in more_data["players"]
    ]
    print(f"Average score: {(sum(scores)/len(scores)):.1f}")

    biggest_score = max(
        [
            more_data["players"][biggest]["total_score"]
            for biggest in more_data["players"]
        ]
    )
    top_player = [
        player
        for player in more_data["players"]
        if more_data["players"][player]["total_score"] == biggest_score
    ]
    top_achievement_count = max(
        [
            more_data["players"][biggest]["achievements_count"]
            for biggest in more_data["players"]
        ]
    )
    print(
        f"Top performer: {top_player[0]} ({biggest_score} "
        f"points, {top_achievement_count} achievements)"
    )
