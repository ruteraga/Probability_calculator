import prob_calculator as pc

hat1= pc.Hat(blue=4, red=2, green=6)
probability= pc.Hat.experiment(hat=hat1, expected_balls={"blue": 2, "red": 1}, num_balls_drawn=4, num_experiments=3000)

print("Probability", probability)
