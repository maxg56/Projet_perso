import pyxel

LARGEUR, HAUTEUR = 200, 120
LARGEUR_BASE, HAUTEUR_BASE = LARGEUR // 6, 5
X_BASE_1, Y_BASE = 20, HAUTEUR - 10
X_BASE_2 = X_BASE_1 + LARGEUR_BASE * 2
X_BASE_3 = X_BASE_2 + LARGEUR_BASE * 2


class Block:
    """Classe représentant un bloc dans la tour de Hanoi."""
    def __init__(self, value: int, length: int, height: int, x: int, y: int) -> None:
        self.value = value
        self.length = length
        self.height = height
        self.x, self.y = x, y

    def draw_block(self, color: int) -> None:
        """Dessine un bloc."""
        pyxel.rect(self.x, self.y, self.length, self.height, color)
        pyxel.text(self.x + (self.length // 2), self.y, str(self.value), 7)

    def move(self, x: int, y: int) -> None:
        """Déplace un bloc aux coordonnées spécifiées."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'value={self.value} length,height={self.length,self.height} x={self.x},y={self.y}'


class Tower:
    """Classe représentant une tour dans le jeu de Hanoi."""
    def __init__(self, base_x: int, base_y: int = Y_BASE, num_blocks: int = None) -> None:
        self.blocks = []
        self.base_x = base_x + 1
        self.base_y = base_y - 8
        if num_blocks is not None:
            rec_height = 8
            r = 6
            min_width = 11
            width = min_width + 6 * num_blocks
            if width > LARGEUR_BASE:
                width = LARGEUR_BASE
                r = 2.2

            ref_y = Y_BASE - 8
            for n in range(num_blocks, 0, -1):
                width -= r
                self.blocks.append(Block(n, width, rec_height, self.base_x, ref_y))
                ref_y -= rec_height
                self.base_x += r / 2

    def draw_tower(self) -> None:
        """Dessine la tour."""
        for block in self.blocks:
            block.draw_block(12)

    def is_empty(self) -> bool:
        """Vérifie si la tour est vide."""
        return len(self.blocks) == 0

    def push(self, block: Block) -> None:
        """Ajoute un bloc à la tour."""
        self.blocks.append(block)

    def pop(self) -> Block:
        """Retire et renvoie le bloc supérieur de la tour."""
        return self.blocks.pop()
    def __str__(self):
        return f" {self.blocks} "


class DisplayHanoi:
    """Classe principale pour afficher le jeu de Hanoi."""
    def __init__(self, num_blocks, pause_time):
        pyxel.init(LARGEUR, HAUTEUR, fps=30)

        self.num_blocks = num_blocks
        self.tower_start = Tower(X_BASE_1, num_blocks)
        self.tower_temp = Tower(X_BASE_2)
        self.tower_end = Tower(X_BASE_1)
        self.frame_count = 0
        self.pause_time = pause_time
        self.moves = self.hanoi(num_blocks)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.frame_count += 1
        if self.frame_count == 60:
            if self.moves:
                move = self.moves.pop(0)
                self.move_disk(move[0], move[1])
            self.frame_count = 0
        print(f"{self.tower_start}{self.tower_temp}{self.tower_end}")

    def draw(self):
        pyxel.cls(7)
        for x_base in (X_BASE_1, X_BASE_2, X_BASE_3):
            pyxel.rect(x_base, Y_BASE, LARGEUR_BASE, HAUTEUR_BASE, 13)

        for tower in [self.tower_start, self.tower_temp, self.tower_end]:
             tower.draw_tower()


    def hanoi(self, num_disks, start='A', temp='B', end='C'):
        if num_disks == 1:
            return [(start, end)]
        else:
            return self.hanoi(num_disks - 1, start, end, temp) + [(start, end)] + self.hanoi(num_disks - 1, temp, start, end)

    def move_disk(self, from_tower: str, to_tower: str):
        if from_tower == 'A':
            if not self.tower_start.is_empty():
                if to_tower == 'B':
                    self.tower_temp.push(self.tower_start.pop())
                else:
                    self.tower_end.push(self.tower_start.pop())
        elif from_tower == 'B':
            if not self.tower_temp.is_empty():
                if to_tower == 'A':
                    self.tower_start.push(self.tower_temp.pop())
                else:
                    self.tower_end.push(self.tower_temp.pop())
        else:
            if not self.tower_end.is_empty():
                if to_tower == 'A':
                    self.tower_start.push(self.tower_end.pop())
                else:
                    self.tower_temp.push(self.tower_end.pop())



a = DisplayHanoi(3, 4)
