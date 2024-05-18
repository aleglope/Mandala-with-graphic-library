import turtle
import random
from time import sleep

# Constants for the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_SPEED = 0.1
FOOD_SIZE = 20
SNAKE_SIZE = 20
MOVE_DISTANCE = 20

# Directions
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"


# Snake Class
class Snake:
    """
    Class to represent the snake in the game.
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a snake body"""
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        """Adds a segment to the snake."""
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if self.segments:
            new_x = self.segments[-1].xcor()
            new_y = self.segments[-1].ycor()
            new_segment.goto(new_x, new_y)
        else:
            new_segment.goto(0, 0)
        self.segments.append(new_segment)

    def extend(self):
        """Extends the snake by adding a new segment."""
        self.add_segment()

    def move(self):
        """Moves the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change the snake's direction to up."""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Change the snake's direction to down."""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Change the snake's direction to left."""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Change the snake's direction to right."""
        if self.head.heading() != 180:
            self.head.setheading(0)


# Food Class
class Food(turtle.Turtle):
    """
    Class to represent the food in the game.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Change the food's location on the screen."""
        random_x = random.randint(-SCREEN_WIDTH // 2 + FOOD_SIZE, SCREEN_WIDTH // 2 - FOOD_SIZE)
        random_y = random.randint(-SCREEN_HEIGHT // 2 + FOOD_SIZE, SCREEN_HEIGHT // 2 - FOOD_SIZE)
        self.goto(random_x, random_y)


# Scoreboard Class
class Scoreboard(turtle.Turtle):
    """
    Class to represent the scoreboard in the game.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, SCREEN_HEIGHT // 2 - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard with the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase the score when the snake eats food."""
        self.score += 1
        self.update_scoreboard()


# Main Game Loop
def game():
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)  # Turn off the screen updates

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Keyboard bindings
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.right, "d")

    game_is_on = True
    while game_is_on:
        screen.update()
        sleep(SNAKE_SPEED)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if (snake.head.xcor() > SCREEN_WIDTH // 2 - SNAKE_SIZE or
                snake.head.xcor() < -SCREEN_WIDTH // 2 + SNAKE_SIZE or
                snake.head.ycor() > SCREEN_HEIGHT // 2 - SNAKE_SIZE or
                snake.head.ycor() < -SCREEN_HEIGHT // 2 + SNAKE_SIZE):
            game_is_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False

    # Game over
    scoreboard.goto(0, 0)
    scoreboard.write("Game Over", align="center", font=("Arial", 24, "normal"))
    screen.exitonclick()


if __name__ == "__main__":
    game()
