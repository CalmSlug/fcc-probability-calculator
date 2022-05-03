import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for k, v in balls.items():
            for n in range(v):
                self.contents.append(k)

    def draw(self, number):
        if number >= len(self.contents):
            bag = copy.copy(self.contents)
        else:
            bag = random.sample(self.contents, k=number)

        for i in bag:
            self.contents.remove(i)

        return bag


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0

    for n in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_dict = {}
        for item in hat_copy.draw(num_balls_drawn):
            balls_dict[item] = balls_dict.get(item, 0) + 1

        succ = False
        for key in expected_balls:
            if key in balls_dict and expected_balls[key] <= balls_dict[key]:
                    succ = True
            else:
                succ = False
                break

        if succ:
            num_success += 1

    return num_success / num_experiments


# Output showcase
random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)