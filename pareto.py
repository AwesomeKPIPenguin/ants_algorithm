
# lexicographic tournament selection
#
# tournament: [[[x1, x2, ...], [crit1, crit2, ...]], ...]
# fit_fts: sorted by importance
# crits: number of criteria


def best_tournament(tournament, fit_fts, crits):
    tlen = len(tournament)
    board = [0] * tlen
    afits = [[0 for x in range(crits)] for y in range(tlen)]
    for i in range(tlen):
        for j in range(crits):
            afits[i][j] = fit_fts[j](tournament[i][1][j])
    for a1 in range(tlen):
        for a2 in range(a1 + 1, tlen):
            for c in range(crits):
                if afits[a1][c] > afits[a2][c]:
                    board[a1] += 1
                elif afits[a1][c] < afits[a2][c]:
                    board[a2] += 1
    winner_i = board.index(max(board))
    return [board, winner_i]
