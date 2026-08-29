import pygame
import random
import math
import sys

pygame.init()

# =========================================================
# SETTINGS
# =========================================================

WIDTH = 1100
HEIGHT = 650
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Commando Legends Infinite")

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("arial", 24)
SMALL = pygame.font.SysFont("arial", 18)
TINY = pygame.font.SysFont("arial", 15)
BIG = pygame.font.SysFont("arial", 48)
HUGE = pygame.font.SysFont("arial", 64)

# =========================================================
# COLORS
# =========================================================

WHITE = (245, 245, 245)
BLACK = (20, 20, 20)

DARK = (25, 30, 45)
DARK2 = (42, 48, 67)

BLUE = (55, 120, 235)
LIGHT_BLUE = (120, 195, 255)

RED = (220, 60, 60)
GREEN = (70, 170, 80)

YELLOW = (255, 220, 40)
GOLD = (255, 195, 30)

BROWN = (130, 85, 50)
GRAY = (120, 120, 130)

PURPLE = (150, 70, 220)
CYAN = (70, 220, 240)
ORANGE = (240, 140, 40)
PINK = (240, 100, 170)

# =========================================================
# PROFILE
# =========================================================

profile = {
    "coins": 0,
    "xp": 0,
    "player_level": 1,
    "game_level": 1,
    "highest_level": 1,
    "super": False,

    "skin": 0,
    "shirt": 0,
    "pants": 0,
    "hat": "None",
    "gun": "Basic"
}

# =========================================================
# CUSTOMIZATION
# =========================================================

SKINS = [
    (255, 220, 185),
    (235, 190, 145),
    (195, 135, 90),
    (140, 90, 60),
    (90, 55, 40)
]

SHIRTS = [
    BLUE,
    RED,
    GREEN,
    PURPLE,
    ORANGE,
    CYAN,
    PINK
]

PANTS = [
    BLACK,
    DARK2,
    BROWN,
    BLUE,
    GREEN,
    GRAY
]

HATS = [
    "None",
    "Cap",
    "Helmet",
    "Beret",
    "Crown"
]

GUNS = [
    "Basic",
    "Red",
    "Ice",
    "Fire",
    "Gold",
    "Galaxy"
]

# =========================================================
# THEMES
# =========================================================

THEMES = [
    {
        "name": "CITY",
        "sky": (120, 195, 245),
        "ground": (90, 95, 105)
    },
    {
        "name": "JUNGLE",
        "sky": (110, 190, 230),
        "ground": (70, 145, 70)
    },
    {
        "name": "DESERT",
        "sky": (235, 205, 140),
        "ground": (180, 140, 80)
    },
    {
        "name": "NIGHT BASE",
        "sky": (55, 60, 90),
        "ground": (70, 70, 80)
    },
    {
        "name": "VOLCANO",
        "sky": (125, 65, 55),
        "ground": (75, 50, 45)
    },
    {
        "name": "SNOW",
        "sky": (190, 225, 245),
        "ground": (225, 235, 245)
    }
]

# =========================================================
# HELPERS
# =========================================================

def draw_text(message, font, color, x, y, center=False):
    surface = font.render(str(message), True, color)
    rect = surface.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(surface, rect)


class Button:
    def __init__(self, text, x, y, width, height, color=BLUE):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        color = self.color

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = (
                min(color[0] + 25, 255),
                min(color[1] + 25, 255),
                min(color[2] + 25, 255)
            )

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            2,
            border_radius=10
        )

        draw_text(
            self.text,
            SMALL,
            WHITE,
            self.rect.centerx,
            self.rect.centery,
            True
        )

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )

# =========================================================
# LEVEL GENERATOR
# =========================================================

def generate_level(level_number):
    theme = THEMES[
        (level_number - 1) % len(THEMES)
    ]

    # LONG levels
    world_width = min(
        4200 + level_number * 320,
        14000
    )

    # lots of enemies
    enemy_count = min(
        8 + level_number * 2,
        60
    )

    # enemy HP rises
    enemy_hp = min(
        2 + level_number // 2,
        18
    )

    # boss every 5 levels
    boss = (
        level_number % 5 == 0
    )

    reward = (
        400 + level_number * 150
    )

    enemy_fire_delay = max(
        40,
        130 - level_number * 3
    )

    return {
        "level": level_number,
        "name": f"{theme['name']} - LEVEL {level_number}",
        "world": world_width,
        "sky": theme["sky"],
        "ground": theme["ground"],
        "enemies": enemy_count,
        "enemy_hp": enemy_hp,
        "reward": reward,
        "boss": boss,
        "enemy_fire_delay": enemy_fire_delay
    }

# =========================================================
# CHARACTER
# =========================================================

def get_gun_color():
    if profile["gun"] == "Red":
        return RED
    if profile["gun"] == "Ice":
        return CYAN
    if profile["gun"] == "Fire":
        return ORANGE
    if profile["gun"] == "Gold":
        return GOLD
    if profile["gun"] == "Galaxy":
        return PURPLE

    return BLACK


def draw_character(x, y, direction=1, scale=1):
    body_width = int(40 * scale)

    pygame.draw.rect(
        screen,
        PANTS[profile["pants"] % len(PANTS)],
        (
            x,
            y + int(40 * scale),
            body_width,
            int(30 * scale)
        )
    )

    pygame.draw.rect(
        screen,
        SHIRTS[profile["shirt"] % len(SHIRTS)],
        (
            x,
            y + int(18 * scale),
            body_width,
            int(45 * scale)
        )
    )

    head_x = x + body_width // 2
    head_y = y + int(10 * scale)

    pygame.draw.circle(
        screen,
        SKINS[profile["skin"] % len(SKINS)],
        (head_x, head_y),
        int(14 * scale)
    )

    pygame.draw.arc(
        screen,
        BLACK,
        (
            head_x - int(14 * scale),
            head_y - int(14 * scale),
            int(28 * scale),
            int(20 * scale)
        ),
        3.1,
        6.2,
        max(3, int(5 * scale))
    )

    # hats

    if profile["hat"] == "Cap":
        pygame.draw.rect(
            screen,
            RED,
            (
                head_x - int(14 * scale),
                head_y - int(19 * scale),
                int(28 * scale),
                int(7 * scale)
            )
        )

    elif profile["hat"] == "Helmet":
        pygame.draw.arc(
            screen,
            GREEN,
            (
                head_x - int(16 * scale),
                head_y - int(19 * scale),
                int(32 * scale),
                int(30 * scale)
            ),
            3.1,
            6.2,
            max(4, int(7 * scale))
        )

    elif profile["hat"] == "Beret":
        pygame.draw.ellipse(
            screen,
            RED,
            (
                head_x - int(14 * scale),
                head_y - int(20 * scale),
                int(28 * scale),
                int(10 * scale)
            )
        )

    elif profile["hat"] == "Crown":
        pygame.draw.polygon(
            screen,
            GOLD,
            [
                (head_x - 15, head_y - 14),
                (head_x - 10, head_y - 29),
                (head_x, head_y - 18),
                (head_x + 10, head_y - 29),
                (head_x + 15, head_y - 14)
            ]
        )

    gun_width = int(30 * scale)

    if direction == 1:
        gun_x = x + body_width
    else:
        gun_x = x - gun_width

    pygame.draw.rect(
        screen,
        get_gun_color(),
        (
            gun_x,
            y + int(34 * scale),
            gun_width,
            max(5, int(7 * scale))
        )
    )

# =========================================================
# BULLET
# =========================================================

class Bullet:
    def __init__(self, x, y, direction, enemy=False):
        self.rect = pygame.Rect(x, y, 14, 6)

        self.speed = 12 * direction
        self.enemy = enemy

    def update(self):
        self.rect.x += self.speed

    def draw(self, camera):
        pygame.draw.rect(
            screen,
            RED if self.enemy else YELLOW,
            (
                self.rect.x - camera,
                self.rect.y,
                self.rect.width,
                self.rect.height
            )
        )

# =========================================================
# GRENADE
# =========================================================

class Grenade:
    def __init__(self, x, y, direction):
        self.x = float(x)
        self.y = float(y)

        self.vx = 7 * direction
        self.vy = -10

        self.timer = 70
        self.exploded = False
        self.explosion_timer = 12
        self.damage_applied = False

    def update(self):
        if not self.exploded:
            self.vy += 0.45

            self.x += self.vx
            self.y += self.vy

            if self.y >= 535:
                self.y = 535
                self.vy *= -0.4
                self.vx *= 0.7

            self.timer -= 1

            if self.timer <= 0:
                self.exploded = True

        else:
            self.explosion_timer -= 1

    def draw(self, camera):
        if self.exploded:
            pygame.draw.circle(
                screen,
                ORANGE,
                (
                    int(self.x - camera),
                    int(self.y)
                ),
                95,
                5
            )

        else:
            pygame.draw.circle(
                screen,
                GREEN,
                (
                    int(self.x - camera),
                    int(self.y)
                ),
                8
            )

# =========================================================
# ENEMY
# =========================================================

class Enemy:
    def __init__(self, x, hp, fire_delay):
        self.rect = pygame.Rect(
            x,
            490,
            40,
            60
        )

        self.hp = hp
        self.max_hp = hp

        self.direction = random.choice(
            [-1, 1]
        )

        self.speed = random.choice(
            [2, 2, 3]
        )

        self.home = x

        self.patrol_range = random.randint(
            140,
            250
        )

        self.fire_delay = fire_delay

        self.shoot_timer = random.randint(
            30,
            fire_delay
        )

        self.alive = True

    def update(self, player, enemy_bullets):
        if not self.alive:
            return

        distance = (
            player.rect.centerx
            - self.rect.centerx
        )

        if abs(distance) < 850:
            self.direction = (
                1 if distance > 0 else -1
            )

            self.shoot_timer -= 1

            if self.shoot_timer <= 0:
                enemy_bullets.append(
                    Bullet(
                        self.rect.centerx,
                        self.rect.centery,
                        self.direction,
                        True
                    )
                )

                self.shoot_timer = random.randint(
                    max(25, self.fire_delay - 20),
                    self.fire_delay + 25
                )

        else:
            self.rect.x += (
                self.speed
                * self.direction
            )

            if (
                self.rect.x
                < self.home - self.patrol_range
            ):
                self.direction = 1

            if (
                self.rect.x
                > self.home + self.patrol_range
            ):
                self.direction = -1

    def draw(self, camera):
        if not self.alive:
            return

        x = self.rect.x - camera

        pygame.draw.rect(
            screen,
            RED,
            (
                x,
                self.rect.y + 18,
                40,
                42
            )
        )

        pygame.draw.circle(
            screen,
            (120, 195, 100),
            (
                x + 20,
                self.rect.y + 12
            ),
            13
        )

        if self.direction == 1:
            gun_x = x + 40
        else:
            gun_x = x - 22

        pygame.draw.rect(
            screen,
            BLACK,
            (
                gun_x,
                self.rect.y + 34,
                22,
                7
            )
        )

# =========================================================
# BOSS
# =========================================================

class Boss:
    def __init__(self, x, level_number):
        self.rect = pygame.Rect(
            x,
            400,
            120,
            150
        )

        self.max_hp = (
            60 + level_number * 10
        )

        self.hp = self.max_hp

        self.direction = -1

        self.timer = 30

        self.level_number = (
            level_number
        )

    def update(self, player, enemy_bullets):
        distance = (
            player.rect.centerx
            - self.rect.centerx
        )

        self.direction = (
            1 if distance > 0 else -1
        )

        if abs(distance) > 280:
            self.rect.x += (
                self.direction * 1.5
            )

        self.timer -= 1

        if self.timer <= 0:
            for offset in [
                -40,
                -20,
                0,
                20,
                40
            ]:
                enemy_bullets.append(
                    Bullet(
                        self.rect.centerx,
                        self.rect.centery + offset,
                        self.direction,
                        True
                    )
                )

            self.timer = max(
                25,
                60 - self.level_number
            )

    def draw(self, camera):
        x = self.rect.x - camera

        pygame.draw.rect(
            screen,
            PURPLE,
            (
                x,
                self.rect.y,
                120,
                150
            )
        )

        pygame.draw.circle(
            screen,
            RED,
            (
                x + 60,
                self.rect.y + 30
            ),
            30
        )

        pygame.draw.rect(
            screen,
            BLACK,
            (
                x + 25,
                self.rect.y + 80,
                110,
                15
            )
        )

# =========================================================
# PLAYER
# =========================================================

class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            100,
            470,
            40,
            70
        )

        self.speed = 6
        self.velocity_y = 0
        self.gravity = 0.7
        self.jump_power = -16

        self.on_ground = False
        self.direction = 1

        self.health = 100
        self.max_health = 100

        self.cooldown = 0

        self.grenades = 4

    def update(self, platforms, ladders):
        keys = pygame.key.get_pressed()

        dx = 0

        if (
            keys[pygame.K_a]
            or keys[pygame.K_LEFT]
        ):
            dx = -self.speed
            self.direction = -1

        if (
            keys[pygame.K_d]
            or keys[pygame.K_RIGHT]
        ):
            dx = self.speed
            self.direction = 1

        # ladder
        ladder_touching = None

        for ladder in ladders:
            if self.rect.colliderect(
                ladder
            ):
                ladder_touching = ladder
                break

        climbing = False

        if ladder_touching:
            if (
                keys[pygame.K_w]
                or keys[pygame.K_UP]
            ):
                self.velocity_y = -5
                climbing = True

            elif (
                keys[pygame.K_s]
                or keys[pygame.K_DOWN]
            ):
                self.velocity_y = 5
                climbing = True

        if not climbing:
            self.velocity_y += self.gravity

        # jump
        if (
            keys[pygame.K_SPACE]
            and self.on_ground
        ):
            self.velocity_y = (
                self.jump_power
            )

            self.on_ground = False

        # horizontal
        self.rect.x += dx

        # vertical
        old_bottom = self.rect.bottom

        self.rect.y += self.velocity_y

        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(
                platform
            ):
                if (
                    self.velocity_y >= 0
                    and old_bottom
                    <= platform.top + 8
                ):
                    self.rect.bottom = (
                        platform.top
                    )

                    self.velocity_y = 0

                    self.on_ground = True

        if self.rect.y > HEIGHT + 200:
            self.health = 0

        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self):
        if self.cooldown == 0:
            self.cooldown = 10

            return Bullet(
                self.rect.centerx,
                self.rect.centery,
                self.direction
            )

        return None

    def throw_grenade(self):
        if self.grenades <= 0:
            return None

        self.grenades -= 1

        return Grenade(
            self.rect.centerx,
            self.rect.centery,
            self.direction
        )

    def draw(self, camera):
        draw_character(
            self.rect.x - camera,
            self.rect.y,
            self.direction
        )

# =========================================================
# BUILDINGS
# =========================================================

def create_building(
    x,
    width,
    floors
):
    platforms = []
    ladders = []
    windows = []

    bottom = 550
    floor_height = 105

    top = (
        bottom
        - floors * floor_height
    )

    ladder_gap = 95

    gap_left = (
        x
        + width // 2
        - ladder_gap // 2
    )

    gap_right = (
        gap_left
        + ladder_gap
    )

    left_width = (
        gap_left - x
    )

    right_width = (
        x + width - gap_right
    )

    # roof pieces
    platforms.append(
        pygame.Rect(
            x,
            top,
            left_width,
            18
        )
    )

    platforms.append(
        pygame.Rect(
            gap_right,
            top,
            right_width,
            18
        )
    )

    # floors
    for floor in range(
        1,
        floors
    ):
        floor_y = (
            bottom
            - floor * floor_height
        )

        platforms.append(
            pygame.Rect(
                x,
                floor_y,
                left_width,
                18
            )
        )

        platforms.append(
            pygame.Rect(
                gap_right,
                floor_y,
                right_width,
                18
            )
        )

    # ladder
    ladders.append(
        pygame.Rect(
            x + width // 2 - 22,
            top + 10,
            44,
            bottom - top - 10
        )
    )

    # windows
    for floor in range(floors):
        y = (
            bottom
            - floor * floor_height
            - 75
        )

        windows.append(
            pygame.Rect(
                x + 35,
                y,
                42,
                36
            )
        )

        windows.append(
            pygame.Rect(
                x + width - 77,
                y,
                42,
                36
            )
        )

    return (
        platforms,
        ladders,
        windows
    )

# =========================================================
# WORLD GENERATION
# =========================================================

def create_world(mission):
    world_width = mission["world"]

    platforms = [
        pygame.Rect(
            0,
            550,
            world_width,
            100
        )
    ]

    ladders = []
    windows = []
    crates = []

    # denser buildings
    current_x = 400

    while (
        current_x
        < world_width - 550
    ):
        building_width = random.randint(
            260,
            380
        )

        floors = random.randint(
            2,
            5
        )

        p, l, w = create_building(
            current_x,
            building_width,
            floors
        )

        platforms.extend(p)
        ladders.extend(l)
        windows.extend(w)

        current_x += (
            building_width
            + random.randint(
                170,
                280
            )
        )

    # lots of extra platforms
    platform_x = 220

    while (
        platform_x
        < world_width - 300
    ):
        if random.random() < 0.8:
            platform_width = random.randint(
                90,
                150
            )

            platform_y = random.randint(
                410,
                470
            )

            platforms.append(
                pygame.Rect(
                    platform_x,
                    platform_y,
                    platform_width,
                    16
                )
            )

        platform_x += random.randint(
            180,
            280
        )

    # lots of crates
    crate_x = 300

    while (
        crate_x
        < world_width - 250
    ):
        if random.random() < 0.85:
            crates.append(
                pygame.Rect(
                    crate_x,
                    510,
                    40,
                    40
                )
            )

        crate_x += random.randint(
            220,
            400
        )

    return (
        platforms,
        ladders,
        windows,
        crates
    )

# =========================================================
# DRAW WORLD
# =========================================================

def draw_world(
    mission,
    platforms,
    ladders,
    windows,
    crates,
    camera
):
    screen.fill(
        mission["sky"]
    )

    # background
    for x in range(
        -300,
        mission["world"],
        500
    ):
        bx = int(
            x - camera * 0.25
        )

        pygame.draw.rect(
            screen,
            (100, 125, 150),
            (
                bx,
                270,
                240,
                280
            )
        )

        for wy in range(
            300,
            500,
            55
        ):
            pygame.draw.rect(
                screen,
                (170, 210, 220),
                (
                    bx + 30,
                    wy,
                    35,
                    30
                )
            )

            pygame.draw.rect(
                screen,
                (170, 210, 220),
                (
                    bx + 130,
                    wy,
                    35,
                    30
                )
            )

    # platforms
    for platform in platforms:
        rect = pygame.Rect(
            platform.x - camera,
            platform.y,
            platform.width,
            platform.height
        )

        if (
            rect.right >= -50
            and rect.left <= WIDTH + 50
        ):
            color = (
                mission["ground"]
                if platform.y >= 550
                else BROWN
            )

            pygame.draw.rect(
                screen,
                color,
                rect
            )

    # windows
    for window in windows:
        rect = pygame.Rect(
            window.x - camera,
            window.y,
            window.width,
            window.height
        )

        if (
            rect.right >= 0
            and rect.left <= WIDTH
        ):
            pygame.draw.rect(
                screen,
                CYAN,
                rect
            )

            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                3
            )

    # ladders
    for ladder in ladders:
        x = (
            ladder.x - camera
        )

        if (
            x > -100
            and x < WIDTH + 100
        ):
            pygame.draw.line(
                screen,
                BROWN,
                (
                    x,
                    ladder.y
                ),
                (
                    x,
                    ladder.bottom
                ),
                5
            )

            pygame.draw.line(
                screen,
                BROWN,
                (
                    x + ladder.width,
                    ladder.y
                ),
                (
                    x + ladder.width,
                    ladder.bottom
                ),
                5
            )

            rung_y = ladder.y

            while (
                rung_y
                < ladder.bottom
            ):
                pygame.draw.line(
                    screen,
                    BROWN,
                    (
                        x,
                        rung_y
                    ),
                    (
                        x + ladder.width,
                        rung_y
                    ),
                    4
                )

                rung_y += 22

    # crates
    for crate in crates:
        rect = pygame.Rect(
            crate.x - camera,
            crate.y,
            crate.width,
            crate.height
        )

        pygame.draw.rect(
            screen,
            BROWN,
            rect
        )

        pygame.draw.rect(
            screen,
            BLACK,
            rect,
            2
        )

        pygame.draw.line(
            screen,
            BLACK,
            rect.topleft,
            rect.bottomright,
            2
        )

        pygame.draw.line(
            screen,
            BLACK,
            rect.topright,
            rect.bottomleft,
            2
        )

# =========================================================
# LEVEL COMPLETE
# =========================================================

def level_complete_screen(
    mission,
    next_level
):
    frames = 180

    while frames > 0:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN
            ):
                return

        screen.fill(DARK)

        draw_text(
            "LEVEL COMPLETE!",
            HUGE,
            GREEN,
            WIDTH // 2,
            150,
            True
        )

        draw_text(
            mission["name"],
            BIG,
            WHITE,
            WIDTH // 2,
            245,
            True
        )

        draw_text(
            f"+{mission['reward']} COINS",
            FONT,
            GOLD,
            WIDTH // 2,
            320,
            True
        )

        draw_text(
            f"NEXT LEVEL: {next_level}",
            BIG,
            CYAN,
            WIDTH // 2,
            400,
            True
        )

        seconds = max(
            1,
            frames // 60
        )

        draw_text(
            f"Starting in {seconds}...",
            FONT,
            WHITE,
            WIDTH // 2,
            475,
            True
        )

        draw_text(
            "Press ENTER to continue now",
            SMALL,
            GRAY,
            WIDTH // 2,
            525,
            True
        )

        pygame.display.flip()

        frames -= 1

# =========================================================
# GAME OVER
# =========================================================

def game_over_screen():
    retry_button = Button(
        "RETRY LEVEL",
        370,
        350,
        170,
        60,
        GREEN
    )

    home_button = Button(
        "HOME",
        560,
        350,
        170,
        60,
        BLUE
    )

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if retry_button.clicked(event):
                return "retry"

            if home_button.clicked(event):
                return "home"

        screen.fill(DARK)

        draw_text(
            "MISSION FAILED",
            HUGE,
            RED,
            WIDTH // 2,
            180,
            True
        )

        draw_text(
            f"Level {profile['game_level']}",
            FONT,
            WHITE,
            WIDTH // 2,
            270,
            True
        )

        retry_button.draw()
        home_button.draw()

        pygame.display.flip()

# =========================================================
# INFINITE GAME
# =========================================================

def play_infinite():
    current_level = profile[
        "game_level"
    ]

    while True:
        mission = generate_level(
            current_level
        )

        player = Player()

        (
            platforms,
            ladders,
            windows,
            crates
        ) = create_world(
            mission
        )

        bullets = []
        enemy_bullets = []
        grenades = []

        enemies = []

        # spaced enemy positions
        positions = []

        x = 600

        while (
            x
            < mission["world"] - 400
        ):
            positions.append(x)

            x += random.randint(
                180,
                280
            )

        random.shuffle(
            positions
        )

        for i in range(
            mission["enemies"]
        ):
            if i < len(positions):
                enemy_x = positions[i]
            else:
                enemy_x = random.randint(
                    650,
                    mission["world"] - 450
                )

            enemies.append(
                Enemy(
                    enemy_x,
                    mission["enemy_hp"],
                    mission["enemy_fire_delay"]
                )
            )

        boss = None

        if mission["boss"]:
            boss = Boss(
                mission["world"] - 500,
                current_level
            )

        camera = 0

        score = 0

        level_running = True

        while level_running:
            clock.tick(FPS)

            # =============================================
            # EVENTS
            # =============================================

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        bullet = player.shoot()

                        if bullet:
                            bullets.append(
                                bullet
                            )

                    if event.key == pygame.K_g:
                        grenade = (
                            player.throw_grenade()
                        )

                        if grenade:
                            grenades.append(
                                grenade
                            )

                    if event.key == pygame.K_ESCAPE:
                        profile[
                            "game_level"
                        ] = current_level

                        return

            # =============================================
            # PLAYER
            # =============================================

            player.update(
                platforms,
                ladders
            )

            player.rect.x = max(
                0,
                min(
                    player.rect.x,
                    mission["world"]
                    - player.rect.width
                )
            )

            # =============================================
            # CAMERA
            # =============================================

            camera = (
                player.rect.centerx
                - WIDTH // 2
            )

            camera = max(
                0,
                min(
                    camera,
                    mission["world"] - WIDTH
                )
            )

            # =============================================
            # PLAYER BULLETS
            # =============================================

            for bullet in bullets[:]:
                bullet.update()

                remove = False

                for enemy in enemies:
                    if (
                        enemy.alive
                        and bullet.rect.colliderect(
                            enemy.rect
                        )
                    ):
                        enemy.hp -= 1

                        remove = True

                        if enemy.hp <= 0:
                            enemy.alive = False

                            score += 100

                            profile["coins"] += (
                                random.randint(
                                    10,
                                    30
                                )
                            )

                        break

                if (
                    boss
                    and boss.hp > 0
                    and bullet.rect.colliderect(
                        boss.rect
                    )
                ):
                    boss.hp -= 1

                    score += 20

                    remove = True

                if (
                    remove
                    or bullet.rect.x < 0
                    or bullet.rect.x
                    > mission["world"]
                ):
                    if bullet in bullets:
                        bullets.remove(
                            bullet
                        )

            # =============================================
            # GRENADES
            # =============================================

            for grenade in grenades[:]:
                grenade.update()

                if (
                    grenade.exploded
                    and not grenade.damage_applied
                ):
                    grenade.damage_applied = True

                    for enemy in enemies:
                        if enemy.alive:
                            distance = math.dist(
                                (
                                    grenade.x,
                                    grenade.y
                                ),
                                enemy.rect.center
                            )

                            if distance < 105:
                                enemy.hp -= 5

                                if enemy.hp <= 0:
                                    enemy.alive = False

                                    score += 120

                                    profile["coins"] += 20

                    if (
                        boss
                        and boss.hp > 0
                    ):
                        distance = math.dist(
                            (
                                grenade.x,
                                grenade.y
                            ),
                            boss.rect.center
                        )

                        if distance < 125:
                            boss.hp -= 8

                if (
                    grenade.exploded
                    and grenade.explosion_timer <= 0
                ):
                    grenades.remove(
                        grenade
                    )

            # =============================================
            # ENEMIES
            # =============================================

            for enemy in enemies:
                enemy.update(
                    player,
                    enemy_bullets
                )

            # =============================================
            # BOSS
            # =============================================

            if (
                boss
                and boss.hp > 0
            ):
                boss.update(
                    player,
                    enemy_bullets
                )

            # =============================================
            # ENEMY BULLETS
            # =============================================

            for bullet in enemy_bullets[:]:
                bullet.update()

                if bullet.rect.colliderect(
                    player.rect
                ):
                    player.health -= 10

                    enemy_bullets.remove(
                        bullet
                    )

                    continue

                if (
                    bullet.rect.x < 0
                    or bullet.rect.x
                    > mission["world"]
                ):
                    enemy_bullets.remove(
                        bullet
                    )

            # =============================================
            # DEATH
            # =============================================

            if player.health <= 0:
                result = (
                    game_over_screen()
                )

                if result == "retry":
                    level_running = False

                else:
                    profile[
                        "game_level"
                    ] = current_level

                    return

            # =============================================
            # CHECK STATUS
            # =============================================

            alive_enemies = [
                enemy
                for enemy in enemies
                if enemy.alive
            ]

            boss_dead = (
                boss is None
                or boss.hp <= 0
            )

            # =============================================
            # LEVEL COMPLETE
            # =============================================

            if (
                len(alive_enemies) == 0
                and boss_dead
                and player.rect.x
                > mission["world"] - 250
            ):
                profile["coins"] += (
                    mission["reward"]
                )

                gained_xp = (
                    250
                    + current_level * 35
                )

                profile["xp"] += (
                    gained_xp
                )

                while (
                    profile["xp"]
                    >= profile[
                        "player_level"
                    ] * 500
                ):
                    profile["xp"] -= (
                        profile[
                            "player_level"
                        ] * 500
                    )

                    profile[
                        "player_level"
                    ] += 1

                current_level += 1

                profile[
                    "game_level"
                ] = current_level

                profile[
                    "highest_level"
                ] = max(
                    profile[
                        "highest_level"
                    ],
                    current_level
                )

                level_complete_screen(
                    mission,
                    current_level
                )

                level_running = False

            # =============================================
            # DRAW
            # =============================================

            draw_world(
                mission,
                platforms,
                ladders,
                windows,
                crates,
                camera
            )

            # exit
            exit_x = (
                mission["world"]
                - 170
                - camera
            )

            pygame.draw.rect(
                screen,
                GREEN,
                (
                    exit_x,
                    450,
                    90,
                    100
                )
            )

            draw_text(
                "EXIT",
                SMALL,
                WHITE,
                exit_x + 45,
                490,
                True
            )

            # enemies
            for enemy in enemies:
                enemy.draw(
                    camera
                )

            # boss
            if (
                boss
                and boss.hp > 0
            ):
                boss.draw(
                    camera
                )

            # bullets
            for bullet in bullets:
                bullet.draw(
                    camera
                )

            for bullet in enemy_bullets:
                bullet.draw(
                    camera
                )

            # grenades
            for grenade in grenades:
                grenade.draw(
                    camera
                )

            # player
            player.draw(
                camera
            )

            # =============================================
            # HUD
            # =============================================

            pygame.draw.rect(
                screen,
                DARK,
                (
                    0,
                    0,
                    WIDTH,
                    85
                )
            )

            draw_text(
                mission["name"],
                FONT,
                WHITE,
                20,
                10
            )

            draw_text(
                f"HP: {player.health}",
                SMALL,
                RED,
                20,
                50
            )

            draw_text(
                f"Coins: {profile['coins']}",
                SMALL,
                GOLD,
                120,
                50
            )

            draw_text(
                f"Score: {score}",
                SMALL,
                WHITE,
                270,
                50
            )

            draw_text(
                f"Enemies: {len(alive_enemies)}",
                SMALL,
                WHITE,
                400,
                50
            )

            draw_text(
                f"Grenades: {player.grenades}",
                SMALL,
                GREEN,
                550,
                50
            )

            if (
                boss
                and boss.hp > 0
            ):
                draw_text(
                    f"BOSS: {boss.hp}/{boss.max_hp}",
                    SMALL,
                    PURPLE,
                    720,
                    50
                )

            if (
                len(alive_enemies) == 0
                and boss_dead
            ):
                draw_text(
                    "GO TO THE EXIT!",
                    FONT,
                    GREEN,
                    WIDTH // 2,
                    115,
                    True
                )

            draw_text(
                "A/D Move | SPACE Jump | W/S Ladder | F Shoot | G Grenade | ESC Home",
                TINY,
                WHITE,
                WIDTH // 2,
                628,
                True
            )

            pygame.display.flip()

# =========================================================
# CHARACTER MENU
# =========================================================

def character_menu():
    back = Button(
        "BACK",
        30,
        30,
        120,
        50
    )

    skin_button = Button(
        "CHANGE SKIN",
        220,
        185,
        240,
        50
    )

    shirt_button = Button(
        "CHANGE SHIRT",
        220,
        255,
        240,
        50
    )

    pants_button = Button(
        "CHANGE PANTS",
        220,
        325,
        240,
        50
    )

    hat_button = Button(
        "CHANGE HAT",
        220,
        395,
        240,
        50
    )

    gun_button = Button(
        "CHANGE GUN",
        220,
        465,
        240,
        50
    )

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back.clicked(event):
                return

            if skin_button.clicked(event):
                profile["skin"] = (
                    profile["skin"] + 1
                ) % len(SKINS)

            if shirt_button.clicked(event):
                profile["shirt"] = (
                    profile["shirt"] + 1
                ) % len(SHIRTS)

            if pants_button.clicked(event):
                profile["pants"] = (
                    profile["pants"] + 1
                ) % len(PANTS)

            if hat_button.clicked(event):
                current = HATS.index(
                    profile["hat"]
                )

                candidate = HATS[
                    (current + 1)
                    % len(HATS)
                ]

                if (
                    candidate != "Crown"
                    or profile["super"]
                ):
                    profile["hat"] = (
                        candidate
                    )

            if gun_button.clicked(event):
                current = GUNS.index(
                    profile["gun"]
                )

                candidate = GUNS[
                    (current + 1)
                    % len(GUNS)
                ]

                if (
                    candidate not in [
                        "Gold",
                        "Galaxy"
                    ]
                    or profile["super"]
                ):
                    profile["gun"] = (
                        candidate
                    )

        screen.fill(DARK)

        draw_text(
            "CHARACTER",
            BIG,
            WHITE,
            WIDTH // 2,
            70,
            True
        )

        back.draw()
        skin_button.draw()
        shirt_button.draw()
        pants_button.draw()
        hat_button.draw()
        gun_button.draw()

        pygame.draw.rect(
            screen,
            DARK2,
            (
                660,
                145,
                300,
                400
            ),
            border_radius=15
        )

        draw_character(
            760,
            285,
            1,
            2
        )

        draw_text(
            f"Hat: {profile['hat']}",
            SMALL,
            WHITE,
            810,
            485,
            True
        )

        draw_text(
            f"Gun: {profile['gun']}",
            SMALL,
            GOLD,
            810,
            520,
            True
        )

        pygame.display.flip()

# =========================================================
# SHOP
# =========================================================

def shop_menu():
    back = Button(
        "BACK",
        30,
        30,
        120,
        50
    )

    helmet = Button(
        "HELMET - 500",
        300,
        180,
        300,
        55
    )

    red_gun = Button(
        "RED GUN - 800",
        300,
        255,
        300,
        55
    )

    fire_gun = Button(
        "FIRE GUN - 1200",
        300,
        330,
        300,
        55
    )

    ice_gun = Button(
        "ICE GUN - 1600",
        300,
        405,
        300,
        55
    )

    message = ""

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back.clicked(event):
                return

            if helmet.clicked(event):
                if profile["coins"] >= 500:
                    profile["coins"] -= 500
                    profile["hat"] = "Helmet"
                    message = "Helmet equipped!"
                else:
                    message = "Not enough coins."

            if red_gun.clicked(event):
                if profile["coins"] >= 800:
                    profile["coins"] -= 800
                    profile["gun"] = "Red"
                    message = "Red Gun equipped!"
                else:
                    message = "Not enough coins."

            if fire_gun.clicked(event):
                if profile["coins"] >= 1200:
                    profile["coins"] -= 1200
                    profile["gun"] = "Fire"
                    message = "Fire Gun equipped!"
                else:
                    message = "Not enough coins."

            if ice_gun.clicked(event):
                if profile["coins"] >= 1600:
                    profile["coins"] -= 1600
                    profile["gun"] = "Ice"
                    message = "Ice Gun equipped!"
                else:
                    message = "Not enough coins."

        screen.fill(DARK)

        draw_text(
            "SHOP",
            BIG,
            WHITE,
            WIDTH // 2,
            70,
            True
        )

        draw_text(
            f"Coins: {profile['coins']}",
            FONT,
            GOLD,
            850,
            80
        )

        back.draw()
        helmet.draw()
        red_gun.draw()
        fire_gun.draw()
        ice_gun.draw()

        draw_text(
            message,
            SMALL,
            YELLOW,
            WIDTH // 2,
            525,
            True
        )

        pygame.display.flip()

# =========================================================
# SUPER RANK
# =========================================================

def super_menu():
    back = Button(
        "BACK",
        30,
        30,
        120,
        50
    )

    activate = Button(
        "ACTIVATE SUPER",
        400,
        475,
        300,
        65,
        PURPLE
    )

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back.clicked(event):
                return

            if activate.clicked(event):
                profile["super"] = True
                profile["hat"] = "Crown"
                profile["gun"] = "Gold"

        screen.fill(DARK)

        draw_text(
            "SUPER RANK",
            HUGE,
            GOLD,
            WIDTH // 2,
            100,
            True
        )

        features = [
            "Golden Crown",
            "Golden Gun",
            "Galaxy Gun",
            "SUPER title",
            "Exclusive cosmetics"
        ]

        y = 220

        for feature in features:
            draw_text(
                feature,
                FONT,
                WHITE,
                WIDTH // 2,
                y,
                True
            )

            y += 45

        back.draw()

        if profile["super"]:
            draw_text(
                "SUPER ACTIVE",
                BIG,
                GOLD,
                WIDTH // 2,
                510,
                True
            )
        else:
            activate.draw()

        pygame.display.flip()

# =========================================================
# HOME
# =========================================================

def home_menu():
    play_button = Button(
        "PLAY",
        400,
        190,
        300,
        65,
        GREEN
    )

    character_button = Button(
        "CHARACTER",
        400,
        275,
        300,
        60,
        BLUE
    )

    shop_button = Button(
        "SHOP",
        400,
        355,
        300,
        60,
        GOLD
    )

    super_button = Button(
        "SUPER RANK",
        400,
        435,
        300,
        60,
        PURPLE
    )

    quit_button = Button(
        "QUIT",
        400,
        515,
        300,
        55,
        RED
    )

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if play_button.clicked(event):
                play_infinite()

            if character_button.clicked(event):
                character_menu()

            if shop_button.clicked(event):
                shop_menu()

            if super_button.clicked(event):
                super_menu()

            if quit_button.clicked(event):
                pygame.quit()
                sys.exit()

        screen.fill(DARK)

        draw_text(
            "COMMANDO LEGENDS",
            BIG,
            WHITE,
            WIDTH // 2,
            60,
            True
        )

        if profile["super"]:
            draw_text(
                "SUPER SOLDIER",
                FONT,
                GOLD,
                40,
                130
            )
        else:
            draw_text(
                "SOLDIER",
                FONT,
                WHITE,
                40,
                130
            )

        draw_text(
            f"Current Level: {profile['game_level']}",
            SMALL,
            WHITE,
            40,
            180
        )

        draw_text(
            f"Highest Level: {profile['highest_level']}",
            SMALL,
            GOLD,
            40,
            215
        )

        draw_text(
            f"Player Level: {profile['player_level']}",
            SMALL,
            WHITE,
            40,
            250
        )

        draw_text(
            f"XP: {profile['xp']} / {profile['player_level'] * 500}",
            SMALL,
            CYAN,
            40,
            285
        )

        draw_text(
            f"Coins: {profile['coins']}",
            SMALL,
            GOLD,
            40,
            320
        )

        pygame.draw.rect(
            screen,
            DARK2,
            (
                820,
                145,
                220,
                340
            ),
            border_radius=15
        )

        draw_character(
            890,
            280,
            1,
            2
        )

        play_button.draw()
        character_button.draw()
        shop_button.draw()
        super_button.draw()
        quit_button.draw()

        pygame.display.flip()

# =========================================================
# START
# =========================================================

home_menu()



        

