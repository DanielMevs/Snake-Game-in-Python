# Import the Turtle Graphics module
import turtle
from random import randint

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 200
FOOD_SIZE = 30

offsets = {
    'up': (0, 20),
    'down': (0, -20),
    'left': (-20, 0),
    'right': (20, 0)
}


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'), 'Up')
    screen.onkey(lambda: set_snake_direction('down'), 'Down')
    screen.onkey(lambda: set_snake_direction('right'), 'Right')
    screen.onkey(lambda: set_snake_direction('left'), 'Left')


def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        # - No self-collision simply by pressing wrong key
        if snake_direction != 'down':
            snake_direction = 'up'
    elif direction == 'down':
        # - No self-collision simply by pressing wrong key
        if snake_direction != 'up':
            snake_direction = 'down'
    elif direction == 'right':
        # - No self-collision simply by pressing wrong key
        if snake_direction != 'left':
            snake_direction = 'right'
    elif direction == 'left':
        # - No self-collision simply by pressing wrong key
        if snake_direction != 'right':
            snake_direction = 'left'



def game_loop():
    # - Remove existing stamps made by stamper.
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # - Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        # - Add new head to snake body.
        snake.append(new_head)

        # - Check for food collision
        if not food_collision():
            # - Keep the snake the same length unless fed
            # If not feed, remove last segment of snake.
            snake.pop(0)


        # - Draw snake 
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # - Refresh screen
        screen.title(f'Snake Game. Score: {score}')
        screen.update()

        # - Rinse and repeat
        turtle.ontimer(game_loop, DELAY)



def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)  

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    # - Pythagoras' Theorem
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    # - Create snake as a list of coordinate pairs.
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = 'up'
    score = 0
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()

# - Create a window where we will do our drawing.
screen = turtle.Screen()
# Set up the dimensions of the Turtle Graphics window
screen.setup(WIDTH, HEIGHT) 
screen.title('Snake')
screen.bgcolor('pink')
# Turn off automatic animation
screen.tracer(0)

# - Event handlers
screen.listen()
bind_direction_keys()

# - Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('green')
stamper.penup()



# - Food
food = turtle.Turtle()
food.shape('triangle')
food.color('yellow')
food.shapesize(FOOD_SIZE / 20)
food.penup()



# -Set animation in motion
reset()

# - Finish nicely
turtle.done()


    