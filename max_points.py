#             1
#           /   \
#          /     \
#         /       \
#        /         \
#       4           3
#      / \         / \
#     /   \       /   \
#    2     6     6     5
#   / \               / \
#  1   7             2   1


class Checkpoint():
    def __init__(self, points, children):
        self.points = points
        self.children = children or []


game = Checkpoint(
    1,
    [
        Checkpoint(
            4,
            [
                Checkpoint(
                    2,
                    [
                        Checkpoint(1),
                        Checkpoint(7)
                    ]
                ),
                Checkpoint(6)
            ]
        ),
        Checkpoint(
            3,
            [
                Checkpoint(6),
                Checkpoint(
                    5,
                    [
                        Checkpoint(2),
                        Checkpoint(1)
                    ]
                )

            ]
        )
    ]
)



class Traverser():
    def __init__(self, game):
        self.max_score = 0
        return self.getMaxScore(game)

    def getMaxScore(checkpoint):
        current_score += checkpoint.points
        if not checkpoint.children:
            self.max_score = max(self.max_score, current_score)
        else:
            return self.getMaxScore(checkpoint)


print(Traverser(game))




