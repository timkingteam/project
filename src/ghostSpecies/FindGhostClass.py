from operator import ne
from src.GhostClass import Ghost
from src.map import *
from pygame.math import Vector2


class FindGhost(Ghost):
    def direction_to_player(self, own_cords, player_cords):
        neighbours = [own_cords + Vector2(0, 1), own_cords + Vector2(
            0, -1), own_cords + Vector2(-1, 0), own_cords + Vector2(1, 0)]
        que = [player_cords]
        dist = {}
        visited = []
        for i in range(0, 27):
            for j in range(0, 27):
                dist[i, j] = float('inf')
        dist[(int(player_cords.x), int(player_cords.y))] = 0
        while len(que) > 0:
            current = que.pop(0)
            visited.append(current)
            current_neighbours = [current + Vector2(0, 1), current + Vector2(
                0, -1), current + Vector2(1, 0), current + Vector2(-1, 0)]
            for current_neighbour in current_neighbours:
                if int(current_neighbour.x) < 27 and int(current_neighbour.y) < 27 and int(current_neighbour.x) >= 0 and int(current_neighbour.y) >= 0:
                    if MAP[int(current_neighbour.y)][int(current_neighbour.x)] != 1:
                        if current_neighbour not in visited:
                            que.append(current_neighbour)
                            visited.append(current_neighbour)
                            if dist[(int(current_neighbour.x), int(current_neighbour.y))] > dist[(int(current.x), int(current.y))] + 1:
                                dist[(int(current_neighbour.x), int(current_neighbour.y))] = dist[(
                                    int(current.x), int(current.y))] + 1
        closer_neighbour = neighbours[0]
        for neighbour in neighbours:
            if dist[(int(closer_neighbour.x), int(closer_neighbour.y))] > dist[(int(neighbour.x), int(neighbour.y))]:
                closer_neighbour = neighbour
        return closer_neighbour
