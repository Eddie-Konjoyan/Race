def start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT):
    """Creates the ready up screen before the game starts"""
    # Clear the screen
    screen.fill((0, 0, 0))


    text_surface = font.render("Race Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)
    # Render and display ttext prompting players to enter
    text_surface2 = font.render("Player1: [W] to ready  Player2: [UP ARROW] to ready", True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface2, text_rect2)

    if oner == True and twor == False:
        #if player one ready
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY    Player2: [UP ARROW] to ready", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return 0
    if oner == False and twor == True:
        #if player two ready
        screen.fill((0, 0, 0))
        text_surface2 = font.render("Player1: [W] to ready    PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return 0
    if oner and twor and not ret:
        # if both players are ready and enter has not been hit
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY   PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        # Render and display enter to start  text
        text_surface = font.render("[ENTER] to start.", True, (255, 255, 255))
        screen.blit(text_surface, text_rect)
        return 0
    if oner and twor and ret:
        # start game
        return 1
    else:
        #if loop occurs and nothing has happened
        return 0

def end_screen(newhs,screen, font, car, high, WIDTH, HEIGHT):
    """called after both cars have finished and one car beat the other
        Displays winning car, winning time, and all-time highscore"""
    screen.fill((0, 0, 0))
    top = font.render(f"WINNER!!! : P{car}", True, (255, 255, 255))
    top_rect = top.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(top, top_rect)
    mid= font.render(high, True, (255, 255, 255))
    mid_rect = mid.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mid, mid_rect)
    #checks if the highscore is new or existing, then displays score and message
    with open('highscore') as hs:
        contents = hs.read()
    if newhs:
        bot = font.render(f"NEW HIGHSCORE: {contents}", True, (255, 255, 255))
        bot_rect = bot.get_rect(center=(WIDTH // 2, HEIGHT*2 // 3))
        screen.blit(bot, bot_rect)
    else:
        bot = font.render(f"HIGHSCORE: {contents}", True, (255, 255, 255))
        bot_rect = bot.get_rect(center=(WIDTH // 2, HEIGHT * 2 // 3))
        screen.blit(bot, bot_rect)

def end_screen_tie(newhs,screen, high, font, WIDTH, HEIGHT):
    """called after both cars have finished and finish times are the same
            Displays time, and all-time highscore"""
    screen.fill((0, 0, 0))
    top = font.render(f"TIE", True, (255, 255, 255))
    top_rect = top.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(top, top_rect)
    mid = font.render(high, True, (255, 255, 255))
    mid_rect = mid.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mid, mid_rect)
    # checks if the highscore is new or existing, then displays score and message
    with open('highscore') as hs:
        contents = hs.read()
    if newhs:
        bot = font.render(f"NEW HIGHSCORE: {contents}", True, (255, 255, 255))
        bot_rect = bot.get_rect(center=(WIDTH // 2, HEIGHT*2 // 3))
        screen.blit(bot, bot_rect)
    else:
        bot = font.render(f"HIGHSCORE: {contents}", True, (255, 255, 255))
        bot_rect = bot.get_rect(center=(WIDTH // 2, HEIGHT * 2 // 3))
        screen.blit(bot, bot_rect)