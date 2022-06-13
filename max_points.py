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
    def __init__(self, points, children=[]):
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
    def __init__(self):
        self.max_score = 0

    def getMaxScore(self, checkpoint, current_score):
        current_score += checkpoint.points
        if not checkpoint.children:
            self.max_score = max(self.max_score, current_score)
        else:
            for child in checkpoint.children:
                self.getMaxScore(child, current_score)
        return self.max_score


t = Traverser()

print(t.getMaxScore(game, 0))




