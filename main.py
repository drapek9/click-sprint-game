# Importy
import pygame

# Inicializace hry
pygame.init()

# Nastavení screenu
width = 771
height = 430
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click sprint game")

# Fps & clock
fps = 60
clock = pygame.time.Clock()


# Game class
class Game:
    def __init__(self, players):
        self.group_of_players = players
        self.colors = ["blue", "green", "pink", "red", "yellow"]
        # Začáteční barva hráčů
        self.first_number = 0
        self.second_number = 1

        # Obrázky avatara
        self.first_player = Player(10, 148, pygame.image.load(f"img/Avatar_{self.colors[self.first_number]}.png"), "w", self.first_number)
        self.second_player = Player(10, 308, pygame.image.load(f"img/Avatar_{self.colors[self.second_number]}.png"), "UP", self.second_number)
        self.players_list = [self.first_player, self.second_player]
        for one in self.players_list:
            group_of_players.add(one)

        # fonty
        self.font = pygame.font.Font("fonts/Sport_font.ttf", 25)
        self.font_2 = pygame.font.Font("fonts/Sport_font.ttf", 40)
        self.font_3 = pygame.font.SysFont("Arial", 20)
        self.font_4 = pygame.font.Font("fonts/Sport_font.ttf", 18)
        self.font_5 = pygame.font.Font("fonts/Sport_font.ttf", 70)
        self.font_6 = pygame.font.SysFont("Arial", 15)

        # Proměnné času
        self.round_time = 0
        self.slow_dowm_cykle = 0
        self.best_round_time = 0

        # délka plochy pro finish
        self.width = width

        # Skóre hráčů a jméno výherce kola
        self.win = ""
        self.wins_first = 0
        self.wins_second = 0

        # choose avatar text
        self.choose_avatar_text = self.font_3.render("Choose an avatar", True, "yellow")
        self.choose_avatar_text_rect = self.choose_avatar_text.get_rect()
        self.choose_avatar_text_rect.center = (width//2 - 150, 55)

        # Pokud chci hned při startu vypisovat skóre barev
        self.full_score = True

        # Proměnné pro odpočet
        self.count_number = 3
        self.count_number_slow = 0

        # win sound
        self.win_sound = pygame.mixer.Sound("media/mixkit-fantasy-game-success-notification-270.wav")

        # Again image
        self.again_image = pygame.image.load("img/Again_picture.png")
        self.again_image_rect = self.again_image.get_rect()
        self.again_image_rect.topright = (width - 150, 10)

    def update(self):
        # update počítání času
        self.slow_dowm_cykle += 1
        if self.slow_dowm_cykle % 60 == 0:
            self.round_time += 1

        # kontrola dosažení cíle
        self.finish()

    # Vypíše vše co zde je
    def draw(self):
        # běžící dráha
        place_image = pygame.image.load("img/place_3.jpg")
        place_image_rect = place_image.get_rect()
        place_image_rect.topleft = (0, 70)

        # Čas kola
        time_text = self.font.render(f"Time: {self.round_time}", True, "white")
        time_text_rect = time_text.get_rect()
        time_text_rect.topleft = (10, 12)

        # Nejlepšího čas
        if self.best_round_time != 0:
            # Pokud několikáté kolo
            best_time_text = self.font_4.render(f"Best time: {self.best_round_time}", True, "yellow")
        else:
            # Pokud první kolo
            best_time_text = self.font_4.render(f"Best time:", True, "yellow")
        best_time_text_rect = best_time_text.get_rect()
        best_time_text_rect.topleft = (8, 45)

        # Nadpis hry
        main_text = self.font_2.render("Click sprint game", True, "purple")
        main_text_rect = main_text.get_rect()
        main_text_rect.midtop = (width // 2 - 20, 15)

        # Skóre prvního hráče
        score_first_text = self.font.render(f"{self.colors[self.first_number]}: {self.wins_first}", True, self.colors[self.first_number])
        score_first_text_rect = score_first_text.get_rect()
        score_first_text_rect.topright = (width - 20, 10)

        # Skóre druhého hráče
        score_second_text = self.font.render(f"{self.colors[self.second_number]}: {self.wins_second}", True, self.colors[self.second_number])
        score_second_text_rect = score_second_text.get_rect()
        score_second_text_rect.topright = (width - 20, 35)

        name_author_text = self.font_6.render("Šimon Drápal 8.11. 2023", True, "black")
        name_author_text_rect = name_author_text.get_rect()
        name_author_text_rect.bottomright = (width - 5, height - 5)

        # blitování všech textů
        screen.blit(place_image, place_image_rect)
        screen.blit(time_text, time_text_rect)
        screen.blit(best_time_text, best_time_text_rect)
        # Vyblituje se, pokud chceme skóre textu na začátku (teď se blituje i na začátku)
        if self.full_score:
            screen.blit(score_first_text, score_first_text_rect)
            screen.blit(score_second_text, score_second_text_rect)
        screen.blit(main_text, main_text_rect)
        screen.blit(self.again_image, self.again_image_rect)
        screen.blit(name_author_text, name_author_text_rect)

    # Vybrání svého avatara
    def choose_avatar(self):
        pause = True
        global lets_continue
        first = 0
        second = 0

        while pause:
            for event_2 in pygame.event.get():
                if event_2.type == pygame.KEYDOWN:
                    # Jiný obrázek
                    if event_2.key == pygame.K_d and self.first_number < 4 and first == 0:
                        self.first_number += 1
                        self.first_player.image = pygame.image.load(f"img/Avatar_{self.colors[self.first_number]}.png")
                    elif event_2.key == pygame.K_a and self.first_number > 0 and first == 0:
                        self.first_number -= 1
                        self.first_player.image = pygame.image.load(f"img/Avatar_{self.colors[self.first_number]}.png")
                    if event_2.key == pygame.K_RIGHT and self.second_number < 4 and second == 0:
                        self.second_number += 1
                        self.second_player.image = pygame.image.load(f"img/Avatar_{self.colors[self.second_number]}.png")
                    elif event_2.key == pygame.K_LEFT and self.second_number > 0 and second == 0:
                        self.second_number -= 1
                        self.second_player.image = pygame.image.load(f"img/Avatar_{self.colors[self.second_number]}.png")
                    # Vybrání obrázku zmáčknutím dolů
                    if event_2.key == pygame.K_DOWN and (self.first_number != self.second_number or first == 0):
                        second = 1
                    if event_2.key == pygame.K_s and (self.second_number != self.first_number or second == 0):
                        first = 1
                    # Pokud chceme změnit výběr
                    if event_2.key == pygame.K_UP:
                        second = 0
                    if event_2.key == pygame.K_w:
                        first = 0
                    # Začátek hry, pokud si oba vybrali své avatary
                    if first == 1 and second == 1:
                        pause = False
                        self.full_score = True
                        self.count_down()
                if event_2.type == pygame.QUIT:
                    pause = False
                    lets_continue = False
            screen.fill("black")
            self.draw()
            # Vypsání charakterů, aby je viděl
            group_of_players.draw(screen)
            # Text, pokud si první nevybral
            if first == 0:
                self.choose_avatar_text_rect.center = (width // 2 - 250, 170)
                screen.blit(self.choose_avatar_text, self.choose_avatar_text_rect)
            # Text, pokud si druhý nevybral
            if second == 0:
                self.choose_avatar_text_rect.center = (width // 2 - 250, 330)
                screen.blit(self.choose_avatar_text, self.choose_avatar_text_rect)
            # Vypsání šipek co dělají, pokud si ještě všichni nevybrali
            if first == 0 or second == 0:
                # Šipka nahoru
                up_arrow_image = pygame.image.load("img/Up-Arrow.png")
                up_arrow_image_rect = up_arrow_image.get_rect()
                up_arrow_image_rect.center = (width//2 - 110, 225)

                # Šipka dolů
                down_arrow_image = pygame.image.load("img/Down_Arrow.png")
                down_arrow_image_rect = down_arrow_image.get_rect()
                down_arrow_image_rect.center = (width//2 - 110, 280)

                # Šipka doleva
                left_arrow_image = pygame.image.load("img/Left-Arrow.png")
                left_arrow_image_rect = left_arrow_image.get_rect()
                left_arrow_image_rect.topright = (width//2 - 120, 228)

                # Šipka doprava
                right_arrow_image = pygame.image.load("img/Right-Arrow.png")
                right_arrow_image_rect = right_arrow_image.get_rect()
                right_arrow_image_rect.topleft = (width//2 - 100, 228)

                # Další avatar text
                next_avatar_text = self.font_6.render("Next avatar", True, "black", "white")
                next_avatar_text_rect = next_avatar_text.get_rect()

                # Vybrání avatara text
                select_text = self.font_6.render("Select", True, "black", "white")
                select_text_rect = select_text.get_rect()
                select_text_rect.midtop = (width//2 - 110, 305)

                # Změna avatara text
                unselect_text = self.font_6.render("Unselect", True, "black", "white")
                unselect_text_rect = unselect_text.get_rect()
                unselect_text_rect.midbottom = (width//2 - 110, 200)

                # další avatar doleva a doprava
                next_avatar_text_rect.topleft = (width//2 - 50, 242)
                screen.blit(next_avatar_text, next_avatar_text_rect)

                next_avatar_text_rect.topright = (width//2 - 170, 242)
                screen.blit(next_avatar_text, next_avatar_text_rect)

                # Blit
                screen.blit(unselect_text, unselect_text_rect)
                screen.blit(select_text, select_text_rect)
                screen.blit(up_arrow_image, up_arrow_image_rect)
                screen.blit(down_arrow_image, down_arrow_image_rect)
                screen.blit(left_arrow_image, left_arrow_image_rect)
                screen.blit(right_arrow_image, right_arrow_image_rect)
            pygame.display.update()

    # pokud někdo dorazil do cíle
    def finish(self):
        global lets_continue
        if self.first_player.rect.right >= width or self.second_player.rect.right >= width:
            # Jméno barvy výherce
            if self.first_player.rect.right >= width:
                self.win = self.colors[self.first_number]
                self.wins_first += 1
            if self.second_player.rect.right >= width:
                self.win = self.colors[self.second_number]
                self.wins_second += 1

            self.draw()
            # Vypsání barvy výherce
            winner_text = self.font_2.render(f"{self.win} win!", True, self.win, "black")
            winner_text_rect = winner_text.get_rect()
            winner_text_rect.center = (width//2, height//2)

            # Text pro stisknutí mezerníku pro pokračování
            escape_text = self.font.render("Press escape for next round", True, "black", "white")
            escape_text_rect = escape_text.get_rect()
            escape_text_rect.midtop = (width//2, height//2 + 21)

            # Blitování textu
            screen.blit(winner_text, winner_text_rect)
            screen.blit(escape_text, escape_text_rect)
            pygame.display.update()
            # Spuštění zvuku
            self.win_sound.play()
            pause = True
            while pause:
                for event_3 in pygame.event.get():
                    # Pokud chce končit
                    if event_3.type == pygame.QUIT:
                        lets_continue = False
                        pause = False
                    if event_3.type == pygame.KEYDOWN:
                        # Pokud chce pokračovat
                        if event_3.key == pygame.K_SPACE:
                            # Zpátky na pozici
                            self.back_to_position()
                            # Kontrola nejlepšího času
                            self.best_time()
                            # Čas = 0
                            self.reset_game()
                            # Odpočítávání
                            self.count_down()
                            pause = False
                    if event_3.type == pygame.MOUSEBUTTONDOWN:
                        click_3_x = event_3.pos[0]
                        click_3_y = event_3.pos[1]
                        # Pokud chce dát hru úplně od znova
                        if self.again_image_rect.collidepoint(click_3_x, click_3_y):
                            self.restart_full_game()
                            pause = False

    # Zpátky na pozici
    def back_to_position(self):
        self.first_player.rect.topleft = (10, 148)
        self.second_player.rect.topleft = (10, 308)

    # Restart pro další kolo
    def reset_game(self):
        self.round_time = 0
        self.slow_dowm_cykle = 0
        self.win = ""

    # Změna nejlepšího času
    def best_time(self):
        if self.best_round_time > self.round_time or self.best_round_time == 0:
            self.best_round_time = self.round_time

    # Odpočítávání do začátku hry
    def count_down(self):
        # Nastavení a spuštění odpočítávající hudby
        count_down_sound = pygame.mixer.Sound("media/Countdown_sound.mp3")
        count_down_sound.set_volume(1)
        count_down_sound.play()
        global lets_continue
        self.count_number = 3
        self.count_number_slow = 0
        while self.count_number > 0:
            for event_2 in pygame.event.get():
                # Pro ukončení během odpočítávání
                if event_2.type == pygame.QUIT:
                    lets_continue = False
                    self.count_number = 0

                if event_2.type == pygame.MOUSEBUTTONDOWN:
                    click_2_x = event_2.pos[0]
                    click_2_y = event_2.pos[1]
                    # Pro hru úplně od začátku
                    if self.again_image_rect.collidepoint(click_2_x, click_2_y):
                        count_down_sound.stop()
                        self.restart_full_game()
                        self.count_number = 0

            # Počítání času
            self.count_number_slow += 1
            if self.count_number_slow % 60 == 0:
                self.count_number -= 1
            screen.fill("black")
            self.draw()
            count_text = self.font_5.render(f"{self.count_number}", True, "black")
            count_text_rect = count_text.get_rect()
            count_text_rect.center = (width//2, height//2)
            screen.blit(count_text, count_text_rect)
            self.group_of_players.draw(screen)
            pygame.display.update()
            # fps pro správné odpočítávání
            clock.tick(fps)

    # Restart úplně od začátku- skóre, barvy, čas (ale nejlepší čas se nechá)
    def restart_full_game(self):
        self.round_time = 0
        self.slow_dowm_cykle = 0
        self.wins_first = 0
        self.wins_second = 0
        self.full_score = True
        self.count_number = 3
        self.count_number_slow = 0
        self.back_to_position()
        self.choose_avatar()


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, file_name, player_type, color):
        super().__init__()
        # Nastavení obrázku a v cyklu vypsaný pomocí- player_group.draw(screen)
        self.image = file_name
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.type = player_type
        self.speed = 10
        self.color = color

    # definice pro pohyb- pokud se rovná tlačítko a typ(w/UP)
    def update(self):
        if event.key == pygame.K_w and self.type == "w":
            self.rect.x += self.speed
        if event.key == pygame.K_UP and self.type == "UP":
            self.rect.x += self.speed


# proměnná pro začáteční vybrání avatara- pokud 0 spustí se potom, se to rovná 1
cykle = 0
# vytvoření groupy player
group_of_players = pygame.sprite.Group()
# Vytvoření my_game z classy Game
my_game = Game(group_of_players)

# cyklus pro hru
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        # Pro ukončení hry
        if event.type == pygame.QUIT:
            lets_continue = False
        # Kontrola, kdo se má pohnout
        if event.type == pygame.KEYDOWN:
            group_of_players.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            # Pro restart hry (ne kola)
            if my_game.again_image_rect.collidepoint(click_x, click_y):
                my_game.restart_full_game()

    screen.fill("black")
    # Čas a kontrola cíle
    my_game.update()
    # Vypsání- Čas, nejlepší čas, skóre, nadpisu, běžící dráhy
    my_game.draw()
    # Vypsání hráčů
    group_of_players.draw(screen)

    # Update pygame
    pygame.display.update()

    # Pokud je začátek- výběr
    if cykle == 0:
        my_game.choose_avatar()
        cykle += 1
    # fps
    clock.tick(fps)

# Konec pygame
pygame.quit()
