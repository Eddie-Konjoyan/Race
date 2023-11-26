def start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Render and display "ENTER TO CONTINUE" text
    text_surface = font.render("Race Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)
    text_surface2 = font.render("Player1: [W] to ready  Player2: [Up arrow] to ready", True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface2, text_rect2)

    if oner == True and twor == False: #if player one ready
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY    Player2: [Up arrow] to ready", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return 0
    if oner == False and twor == True: #if player two ready
        screen.fill((0, 0, 0))
        text_surface2 = font.render("Player1: [W] to ready    PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return 0
    if oner and twor and not ret: # if both players are ready and enter has not been hit
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY   PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        text_surface = font.render("[Enter] to start.", True, (255, 255, 255))
        screen.blit(text_surface, text_rect)
        return 0
    if oner and twor and ret: # start game
        return 1
    else:
        return 0

def end_screen(screen, font, car, high, WIDTH, HEIGHT):
    screen.fill((0, 0, 0))
    top = font.render(f"WINNER!!! : P{car}", True, (255, 255, 255))
    top_rect = top.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(top, top_rect)
    mid= font.render(high, True, (255, 255, 255))
    mid_rect = mid.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(mid, mid_rect)


def end_screen_tie(screen, font, WIDTH, HEIGHT):
    screen.fill((0, 0, 0))
    top = font.render(f"TIE", True, (255, 255, 255))
    top_rect = top.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(top, top_rect)
    bot = font.render("[Enter] to Play again", True, (255, 255, 255))
    bot_rect = bot.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(bot, bot_rect)